# Data

Updated: 2026-05-19 16:55:11 AEST

This package now includes the user-identified local data folder for `paper-2019-14`:

`/Users/dlev2617/Documents/Data/~Nexus_Data/Crashes and Pavement Quality`

The included data match the paper's stated MnDOT pavement-quality and crash-analysis workflow. The paper states that pavement quality data are available from 2000-2015, crash data from 2003-2014, and the analysis uses the overlapping 2003-2014 period.

## Included

- `processed_crash_panel/Crash2003.csv` through `Crash2014.csv`: model-ready annual segment tables with pavement indices, AADT/truck share, segment length, crash severity counts, and controls.
- `source_mndot_2015_pavement/2015_M-Rec_Pvmt_Condition.*`: MnDOT source pavement GIS layer components.
- `source_mndot_2015_pavement/Map_2015_M-Records.xlsx` plus `MAP_2015_M-Record.csv`: readable workbook and CSV sidecar.
- `source_mndot_2015_pavement/2000-2015_M-Record_History.xlsb`: original MnDOT history workbook, preserved as supplied.
- `source_mndot_2015_pavement/M-RECORDS_2015.mxd`: original ArcMap project file, preserved as supplied.

## Metadata

- `metadata/PROCESSED_CRASH_FILE_SUMMARY.csv`
- `metadata/PROCESSED_CRASH_DATA_DICTIONARY.csv`
- `metadata/MNDOT_GIS_ATTRIBUTE_DICTIONARY.csv`
- `metadata/MNDOT_GIS_LAYER_SUMMARY.csv`
- `metadata/DATA_FILE_MANIFEST.csv`
- `metadata/DATA_EXCLUSIONS.csv`

## Exclusions

System files, lock files, a zero-byte workbook placeholder, and the dataless `R Console.txt` placeholder are not copied. The console transcript should be hydrated later only if we decide the regression-console output is worth preserving.
