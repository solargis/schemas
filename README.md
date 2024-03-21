Solargis public JSON schema files define JSON instances of various request and response object types.

#### RELEASE NOTES:
- **v1.0.8** (Mar 21 2024): Adding new unit mm/hour for the precipitation rate parameter.
- **v1.0.7** (Feb 29 2024): Allowing null value in dataset.DataColumnMetadata.properties.flagColumnName.
- **v1.0.6** (Jan 17 2024): Added two new units for energy system's related parameters (into common enums).
- **v1.0.5** (Sep 25 2023): Added new types (test group), properties (dataset.dataOrigin), column types and units (air pollution, PV domain, Solargis Analyst), column catalogue
- **v1.0.4** (Apr 24 2023): Added AUTODETECT-P1D as a new enum value for the fromDate request property, added SOLARGIS_JSON_HIGH_PREC_FLOAT output format for special use cases.
- **v1.0.3** (Mar 13 2023): Added Environment common type (wraps horizon and surface albedo), added internal request property 'requestId'.
- **v1.0.2** (Mar 8 2023): Updated GTI sub-schema and examples, repo refactored (folder v1 deleted).
- **v1.0.1** (Mar 7 2023): Column names refactored, new UncertaintyColumnTypesEnum added, groundAlbedo renamed to surfaceAlbedo. RequestType is not required for public requests.
- **v1.0.0** (Feb 16 2023): Redefined request property utcOffset from int to string e.g, '9' changed to '+09:00'.
