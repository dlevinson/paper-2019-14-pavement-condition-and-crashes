# Pavement Condition And Crashes

Row ID: `paper-2019-14`

This is a public-ready review package for the Transport Findings paper. It includes the final paper reference, legacy Python/QGIS processing scripts, the user-identified local MnDOT pavement/crash analysis data folder, and generated metadata.

## Bibliographic Information

- Authors: Yokoo, Marasteanu, Levinson
- Venue: Transport Findings (2019)
- DOI: https://doi.org/10.32866/5771
- Citation: Yokoo, Marasteanu, Levinson. (2019). Pavement Condition And Crashes. Transport Findings (2019). 10.32866/5771

## Contents

- `paper/5771-pavement-condition-and-crashes.pdf` - local reference copy of the final paper used for audit validation. Review publisher terms before public release.
- `code/legacy_pavement_qgis/` - two legacy processing scripts.
- `data/processed_crash_panel/` - annual model-ready crash/pavement segment CSVs for 2003-2014.
- `data/source_mndot_2015_pavement/` - MnDOT source pavement GIS/workbook files and generated XLSX-to-CSV sidecar.
- `metadata/DATA_FILE_MANIFEST.csv` - data file inventory and checksums.
- `metadata/PROCESSED_CRASH_FILE_SUMMARY.csv` - row counts and crash-count summaries by annual CSV.
- `metadata/PROCESSED_CRASH_DATA_DICTIONARY.csv` - reconstructed column dictionary for processed CSVs.
- `metadata/MNDOT_GIS_ATTRIBUTE_DICTIONARY.csv` and `metadata/MNDOT_GIS_LAYER_SUMMARY.csv` - shapefile attribute/header metadata.
- `metadata/DATA_EXCLUSIONS.csv` and `metadata/SOURCE_FILE_DECISIONS.csv` - source inclusion/exclusion decisions.

## Data Match

The staged processed CSVs cover 2003-2014 and contain the variables described in the paper: segment IDs, AADT/truck share, pavement measures including RQI/PQI/SR/IRI, segment length, crash severity counts, pavement type, geometry, weather, and timing controls. The staged MnDOT source GIS/workbooks provide the pavement-quality/source-map context.

## Limits

The legacy scripts contain hard-coded original workstation paths and are not standalone runnable without path adaptation. The R regression script was not found. `Processed data/R Console.txt` is currently a dataless placeholder and was not copied; it can be hydrated later if the console transcript is needed.

Updated: 2026-05-19 16:55:11 AEST

<!-- package-hardening-status:start -->
## Package Hardening Status

Generated: 2026-05-21 20:57:23 AEST

- Pipeline: `READY-TO-UPLOAD/PUBLIC`
- Sidecars added/updated: `PACKAGE_STATUS.md`, `PACKAGE_MANIFEST.csv`, `LICENSE_STATUS.md`.
- Paper reference copies are for local audit convenience and are not public-upload assets without rights review.
- Final GitHub upload should use the manifest include statuses and the license-status note.
<!-- package-hardening-status:end -->
