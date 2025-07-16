Solargis public JSON schema files define JSON instances of various request and response object types.

### RELEASE NOTES:
- **v1.1.5** (Jul 15, 2025): Added new optional properties to Site in solargis_common_types.
- **v1.1.5** (Jul 07, 2025): PV configuration v1 support included in all requests and datasets (not yet implemented in backend).
- **v1.1.4** (Jun 24, 2025): Added 'PT1M' as supported timeStep for TMY public request. Preparation for having PV system in requests (not yet implemented).
- **v1.1.3** (Apr 3, 2025): Changed time step pattern to cover almost complete ISO 8601 durations standard. Added 'unitless' as supported unit.
- **v1.1.2** (Mar 5, 2025): Added validationPriority to DataColumnMetadata plus its enum
- **v1.1.1** (Dec 16, 2024): Added public TS API request, PvEnergySystemMetadata type added into dataset metadata. TimeShift deprecated as a part of history object in dataset metadata, new timeShifts object added. DataColumnMetadata extended with dataQuality, maintenanceQuality, columnNotes, report added to DatasetMetadata.
- **v1.1.0** (Jun 18, 2024): GtiMountingTrackerOneAxisVertical mounting type has backtracking required, TestGroups object redefined 
- **v1.0.10** (May 29, 2024): Adding new units - W/kWp.
- **v1.0.9** (May 6, 2024): Adding two data parameters - LOSS_SNOW and LOSS_SOIL.
- **v1.0.8** (Mar 21, 2024): Adding new unit mm/hour for the precipitation rate parameter.
- **v1.0.7** (Feb 29, 2024): Allowing null value in dataset.DataColumnMetadata.properties.flagColumnName.
- **v1.0.6** (Jan 17, 2024): Added two new units for energy system's related parameters (into common enums).
- **v1.0.5** (Sep 25, 2023): Added new types (test group), properties (dataset.dataOrigin), column types and units (air pollution, PV domain, Solargis Analyst), column catalogue
- **v1.0.4** (Apr 24, 2023): Added AUTODETECT-P1D as a new enum value for the fromDate request property, added SOLARGIS_JSON_HIGH_PREC_FLOAT output format for special use cases.
- **v1.0.3** (Mar 13, 2023): Added Environment common type (wraps horizon and surface albedo), added internal request property 'requestId'.
- **v1.0.2** (Mar 8, 2023): Updated GTI sub-schema and examples, repo refactored (folder v1 deleted).
- **v1.0.1** (Mar 7, 2023): Column names refactored, new UncertaintyColumnTypesEnum added, groundAlbedo renamed to surfaceAlbedo. RequestType is not required for public requests.
- **v1.0.0** (Feb 16, 2023): Redefined request property utcOffset from int to string e.g, '9' changed to '+09:00'.


### Versioning guidelines
For versioning our JSON schemas, we adopted semantic versioning (SemVer). Semantic versioning uses a three-part version number: MAJOR.MINOR.PATCH. Here's how you should update the version number for different types of changes.

#### MAJOR version
Incremented for breaking changes. This is when changes are made that are not backward-compatible. Examples include:

* Removing required fields.
* Changing data types of existing fields.
* Renaming fields.
* Altering the structure in a way that existing documents will no longer validate.
#### MINOR version
Incremented for adding functionality in a backward-compatible manner. This includes:

* Adding new optional fields.
* Introducing new features that do not affect existing functionality.
* Adding new definitions or sub-schemas that don't break existing validations.
#### PATCH version
Incremented for backward-compatible bug fixes. This might include:

* Fixing typos.
* Clarifying documentation within the schema.
* Minor changes that do not affect the validation of existing documents.
