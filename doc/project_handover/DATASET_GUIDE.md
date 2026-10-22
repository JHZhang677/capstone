# Dataset guide

Dataset descriptions below follow the supplied files and source documentation. They describe role and provenance; they do not establish validation or redistribution rights.

## Armstrong Reference Workbooks

Human-blood reference rheology: steady state, SAOS, LAOS and transient protocols in workbook sheets. Two aspirin summary workbooks are not raw core traces. DataZ is a separate industrial chirp reference, not Armstrong blood.

Original mapped paths: 16; distinct byte contents: 16. Formats: .xlsx (16).

## Published Clot Context

Published fibrin/plasma/whole-blood clot context: PolySTAT LAOS, trauma TEG model data, transfusion rheology/TEG/turbidity, fortified sheep-blood clots, sepsis ROTEM images and dysregulated clot mechanics/confocal images. These were not pooled into the final Armstrong feature cohort.

Original mapped paths: 1360; distinct byte contents: 1347. Formats: .jpg (903), .czi (386), .xls (36), .xlsx (9), .md (6), .pdf (2), .bmp (2), .zip (1), .csv (1), [native/extensionless] (1).

## Other Code History

Code outside the main analysis directories, including checkpoint snapshots. Original context is recorded in the source mapping.

Original mapped paths: 11; distinct byte contents: 11. Formats: .ipynb (10), .py (1).

## External Rheology Monitoring

Upstream rheology-health-monitoring scripts and data. Preserve its LICENSE and source README; do not attribute this implementation to the student team.

Original mapped paths: 58; distinct byte contents: 58. Formats: .csv (26), .py (8), .pb (4), .mat (3), .m (3), [native/extensionless] (2), .md (2), .txt (2), .data-00000-of-00001 (2), .index (2), .pdf (2), .cff (1), .npy (1).

## Blood Analysis Saved Results

Measured-feature integrations, Fourier/wavelet comparisons and prior audit outputs. Use corrected results for the final report; this preserves development outputs.

Original mapped paths: 114; distinct byte contents: 109. Formats: .csv (69), .png (40).

## Blood Model Prototypes

Earlier model-derived feature comparisons and transient-detection prototypes. The revised prototype distinguishes designed event timing from measured feature associations.

Original mapped paths: 21; distinct byte contents: 20. Formats: .csv (11), .png (7), .ipynb (2).

## Synthetic Rheology Ten Scenarios

Ten earlier rheology-inspired scenario files with constitutive/latent quantities and known synthetic events. Separate study from the later multisine event benchmark.

Original mapped paths: 50; distinct byte contents: 50. Formats: .csv (40), .png (8), .zip (1), .ipynb (1).

## Shared Ingestion And Step 138

Long signal table, measurement index, dictionaries, source inventories, QC/exclusions and primary conventional step results. 357 core blocks; primary step cohort 138. Original and corrected outputs are kept distinct.

Original mapped paths: 31; distinct byte contents: 31. Formats: .csv (17), .png (8), .md (1), .xlsx (1), .ipynb (1), .py (1), .json (1), .gz (1).

## Conventional Laos

Conventional LAOS feature table and cohort, instrument-comparison and sensitivity results; final cohort 181 records. Includes frequency/strain metadata and G-prime/G-double-prime/harmonic features.

Original mapped paths: 29; distinct byte contents: 29. Formats: .csv (14), .png (11), .md (2), .ipynb (1), .json (1).

## Step Analysis Separate Branch

Separate raw-workbook/step-analysis branch. Its mappings and valid-comparison denominators differ from the primary 138-record analysis. Refer to each saved index instead of merging by count.

Original mapped paths: 19; distinct byte contents: 19. Formats: .csv (9), .png (8), .md (1), .ipynb (1).

## Gel Scope Experiments

Archived gel-scope notebook; its source wording and output remain historical.

Original mapped paths: 1; distinct byte contents: 1. Formats: .ipynb (1).

## Earlier Step Handover

Earlier step notebook and saved handover outputs; version-history material rather than an alternative final denominator.

Original mapped paths: 39; distinct byte contents: 39. Formats: .xlsx (15), .csv (10), .png (8), .pdf (5), .ipynb (1).

## Previous Semester Rheology

Archived industrial OWCh chirps, metal-crosslinked hydrogel SAOS/LAOS, bovine collagen time/frequency sweeps, MITMAPS multitone/SAOS data, xanthan/salt rheology and settling, hydrogel characterisation, DOE/native rheometer files and ShearView material. Source briefs/READMEs describe these non-blood collections.

Original mapped paths: 10201; distinct byte contents: 9937. Formats: .dps (5981), .txt (3235), .csv (453), .xlsx (73), .vi (42), .pdf (27), .opj (25), .xml (22), .ipynb (21), .mdt (17), .png (9), .zip (8), .py (8), [native/extensionless] (3), .md (3), .sig (2), .jpeg (1), .rar (1), .opju (1), .dpsaa (1), .step (1), .m (1), .1ipynb (1), .xlsb (1).

## Early Gel Detection

Early gel-point research inputs and notebooks: validation materials, chirp recordings and contextual clot data. Exact duplicates may point to files in another collection.

Original mapped paths: 96; distinct byte contents: 96. Formats: .xls (36), .xlsx (29), .csv (26), .ipynb (2), [native/extensionless] (1), .zip (1), .pdf (1).

## Synthetic Clot Event Benchmarks

v1: ten scenario designs; v2: twenty designs with three replicates each. Signal CSVs, manifest, separate ground-truth labels, quality summaries, event scores and result tables. Model-defined events are not clinical labels.

Original mapped paths: 81; distinct byte contents: 80. Formats: .csv (61), .png (14), .ipynb (2), .pdf (2), .zip (1).

## Armstrong workbook aliases

| Original alias | Descriptive name | Meaning |
|---|---|---|
| data1.xlsx | `arm_mar19.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data2.xlsx | `arm_apr18.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data3.xlsx | `arm_may19.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data4.xlsx | `arm_dec18.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data5.xlsx | `arm_jul18.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data6.xlsx | `arm_aug18_prefix.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data7.xlsx | `arm_feb18.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data8.xlsx | `arm_jun18.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data9.xlsx | `arm_dec17.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data10.xlsx | `arm_feb20.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data11.xlsx | `arm_feb19.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data12.xlsx | `arm_aug18_suffix.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data13.xlsx | `arm_nov18.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data14.xlsx | `usma_aspirin_copy.xlsx` | Supplied source-catalogue identity; not a donor identifier |
| data15.xlsx | `usma_aspirin_main.xlsx` | Supplied source-catalogue identity; not a donor identifier |

Other aliases: `Data2.xlsx` in the previous-semester collection is the industrial OWCh temperature-sweep dataset; `Data3_laos/saos` are metal-crosslinked hydrogel records; `Data4` code/data folders are bovine collagen; `Data6` folders are MITMAPS multitone data. These aliases are contextual: the previous-semester Data2 is not the active blood data2 workbook.

## Data dictionary

The current-analysis field dictionary is in `final_code/report_analysis/supporting_data/documentation/report_data_dictionary.csv`; the shared-ingestion source dictionary is retained in the shared-ingestion family. `dataset_schema_index.csv` lists observed file schemas for the broader archive.

| Field / concept | Meaning / units |
|---|---|
| measurement_id | Identifier for a detected source measurement block |
| source_file / sheet / source_row | Provenance back to the original workbook |
| time_s | Time since the measurement block started, seconds |
| stress_pa | Measured shear stress, pascals |
| strain_pct | Measured strain in percent; nominal fractions require conversion |
| shear_rate_1_s | Shear rate, reciprocal seconds |
| experiment_type / subtype | Protocol classification; unresolved direction stays explicit |
| qc_flag / duplicate links | Quality notes and repeated-trace provenance |
| G-prime / G-double-prime | Storage/loss moduli, pascals |
| I3/I1 | Third-to-first stress harmonic amplitude ratio, dimensionless |
| FFT high/low ratio | Supported-band energy ratio; split depends on protocol |
| Synthetic truth time | Programmed event time, seconds; separate from observed channels |
| Missing value | Unavailable/undefined; not zero |

For native `.dps`, `.czi`, instrument projects and binary formats, use the originating software and embedded source metadata. No numerical schema or physical units were guessed from a filename.
