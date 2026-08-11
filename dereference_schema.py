"""
Dereferences a schema into a single self-contained file - the offline replacement for
https://darosh.github.io/json-schema-bundler/test/ ("Dereferenced" variant), which is how
solargis_public_TS_API_request_dereferenced.schema.json used to be produced.

Python 3, standard library only. Refs are resolved from the schema's own directory by file name,
never over the network, so this works on a branch that has not been pushed to GitHub yet.

    python dereference_schema.py                    # regenerate the TS API dereferenced schema
    python dereference_schema.py --check            # verify it is up to date (exit 1 if not)
    python dereference_schema.py SOURCE TARGET      # any other pair

What it does, matching the output of the online bundler:

- every $ref node is replaced by the schema it points at. Keywords sitting next to a $ref are
  dropped, because draft-07 ignores them anyway - that is why the inlined `gtiConfiguration` in
  the committed file carries no description.
- $defs disappears from the output; there is nothing left to reference.
- $id is stripped. The dereferenced schema is deliberately the one file in this repo without one
  (common-data-model injects it during code generation).
"""
import json
import sys
from pathlib import Path

DEFAULT_SOURCE = 'solargis_public_TS_API_request.schema.json'
DEFAULT_TARGET = 'solargis_public_TS_API_request_dereferenced.schema.json'


class RefCycle(Exception):
    pass


def dereference(source_path):
    """
    Returns the fully inlined schema dict of source_path.
    """
    source_path = Path(source_path)
    here = source_path.parent
    cache = {}

    def load(file_name):
        if file_name not in cache:
            cache[file_name] = json.loads((here / file_name).read_text())
        return cache[file_name]

    def resolve(ref, current_file):
        """
        Returns (target_schema, file_the_target_lives_in) for one $ref string.
        """
        file_part, _, fragment = ref.partition('#')
        target_file = file_part or current_file
        node = load(target_file)
        for part in [p for p in fragment.split('/') if p]:
            part = part.replace('~1', '/').replace('~0', '~')
            if part not in node:
                raise KeyError('unresolvable $ref %s (missing %r)' % (ref, part))
            node = node[part]
        return node, target_file

    def walk(node, current_file, seen):
        if isinstance(node, list):
            return [walk(item, current_file, seen) for item in node]
        if not isinstance(node, dict):
            return node
        ref = node.get('$ref')
        if isinstance(ref, str):
            key = (current_file, ref)
            if key in seen:
                raise RefCycle(' -> '.join('%s%s' % (f, r) for f, r in list(seen) + [key]))
            target, target_file = resolve(ref, current_file)
            return walk(target, target_file, seen | {key})
        return {k: walk(v, current_file, seen)
                for k, v in node.items() if k not in ('$defs', '$id')}

    return walk(load(source_path.name), source_path.name, frozenset())


def normalize_numbers(node):
    """
    Writes integral floats as ints - 0.0 -> 0 - the way JSON.stringify does it in the online
    bundler. Purely cosmetic, but it keeps regeneration diffs free of noise.
    """
    if isinstance(node, dict):
        return {k: normalize_numbers(v) for k, v in node.items()}
    if isinstance(node, list):
        return [normalize_numbers(v) for v in node]
    if isinstance(node, float) and node.is_integer():
        return int(node)
    return node


def as_text(schema):
    # ensure_ascii=False keeps the UTF-8 characters the bundler emitted (degree signs, en dashes)
    return json.dumps(normalize_numbers(schema), indent=2, ensure_ascii=False) + '\n'


def main(argv):
    check_only = '--check' in argv
    args = [a for a in argv if not a.startswith('--')]
    source = args[0] if args else DEFAULT_SOURCE
    target = Path(args[1] if len(args) > 1 else Path(source).parent / DEFAULT_TARGET)

    text = as_text(dereference(source))
    if check_only:
        current = target.read_text() if target.exists() else ''
        if json.loads(current or '{}') == json.loads(text):
            print('%s is up to date' % target)
            return 0
        print('%s is STALE - regenerate it from %s' % (target, source))
        return 1
    target.write_text(text)
    print('Dereferenced %s -> %s (%d bytes)' % (source, target, len(text)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
