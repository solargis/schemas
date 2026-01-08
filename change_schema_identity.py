import glob
import os
from pathlib import Path

old_identity = '/v1.1.4/'
new_identity = '/v1.1.6/'

here = Path(__file__).parent
schema_folder = str(here)

file_list = glob.glob(os.path.join(schema_folder, "*.schema.json"))

for filename in file_list:
    with open(filename, "r") as file:
        file_content = file.read()
        # Replace the text
        new_content = file_content.replace(old_identity, new_identity)

    # Open the file again in write mode
    with open(filename, "w") as file:
        # Write the new content to the file
        file.write(new_content)
    print('Updated %s.' % filename)

print('All done.')
