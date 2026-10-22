# Part 1: LAOS and Step-Up/Down Data Processing

## 1. Objective

This part covers data processing only. It does not include interpretation of LAOS harmonics, development of CWT/DWT features, statistical significance testing, or selection of a minimum feature set. The objective was to read the source Excel files, determine the size and structure of the dataset, identify LAOS, step-up, and step-down measurements, and convert the relevant measurements into a consistent format for subsequent analysis by other team members.

## 2. Work completed

### 2.1 Data inventory

- All 15 Excel files in the `0924dataprocess` folder were read.
- The files contain 96 worksheets covering LAOS, UDLAOS, step-up/down, SS/SAOS, Helton/SRFS, cessation, reversal, and aspirin summary data.
- File size, worksheet count, worksheet names, row and column counts, non-empty cell counts, numeric cell counts, and formula cell counts were recorded.
- All 15 files are represented in the inventory. No source workbook was modified or overwritten.

### 2.2 Experiment classification

Worksheets were classified from their names and headers into the following categories:

- `LAOS`
- `STEP_UP_DOWN`
- `UDLAOS`
- `SS_SAOS`
- `OTHER_TRANSIENT`, including Helton, SRFS, and sawtooth measurements
- `CESSATION`
- `REVERSAL`
- `ASPIRIN_SUMMARY`

The core long-format dataset for Part 1 contains only LAOS and explicit step-up/down worksheets. The other worksheet types remain documented in the inventory and exclusion log; they were not deleted.

### 2.3 Measurement-block extraction and classification

The processing program detects repeated `Step time`, `Stress`, `Strain`, and `Shear rate` headers. Each horizontally arranged experimental block is converted into one measurement record.

The final classification contains:

- 200 LAOS measurement blocks;
- 74 step-up measurement blocks;
- 73 step-down measurement blocks;
- 10 step measurements whose direction could not be determined reliably;
- 357 core measurement blocks in total.

Step direction is taken from the condition label when possible. For example, `0.1-->5` is classified as step-up and `300-->5` as step-down. When a complete label is not available, the program compares the measured shear rate at the start and end of the record. Records that still cannot be classified reliably are retained as `STEP_UNKNOWN` instead of being forced into a direction category.

In the source LAOS labels, `Gamma=0.5` represents a dimensionless strain amplitude of 0.5, which is 50%. The measurement index therefore includes both strain fraction and strain percent fields.

### 2.4 Standardized long-format data

The processing produced 437,956 standardized time-series rows. Each row represents one observation at one time point. The principal fields are:

- `measurement_id`: unique identifier for a measurement block;
- `source_file`, `sheet`, and `source_row`: source traceability fields;
- `experiment_type` and `experiment_subtype`: LAOS, STEP_UP, STEP_DOWN, or STEP_UNKNOWN;
- `condition_label`: experimental condition copied from the source;
- `time_s`: elapsed time in seconds;
- `stress_pa`: shear stress in Pa;
- `strain_pct`: strain in percent;
- `shear_rate_1_s`: shear rate in 1/s;
- `qc_flag`: row-level quality flag.

When a channel is unavailable, the value is left blank rather than replaced with zero. Flagged source rows are retained and labelled instead of being silently deleted.

### 2.5 Data-quality and duplicate checks

- The 357 core measurements contain 347 distinct numerical signal traces.
- Ten signals are exact duplicates of another record. They remain in the dataset, but `duplicate_of_measurement_id` identifies the first matching record.
- Twenty-one measurements require manual review. The main reasons are unresolved step direction, disagreement between the labelled and measured final shear rate, duplicate signals, or non-increasing time values.
- There are 132 information-level sampling notes. Most indicate non-uniform time intervals in step measurements. This describes the source acquisition structure and is not treated automatically as an error.
- Sixty-five non-core worksheets were retained in the inventory but not added to the core long table. One LAOS block was excluded because it lacked a stress channel.

The two aspirin workbooks contain laboratory and donor summary worksheets rather than raw LAOS or step-up/down time series. They were included in the inventory but were not forced into the core signal table.

## 3. Output files

- `Part_1_Data_Processing_Summary.xlsx`: reader-facing inventory, classification, and quality workbook;
- `file_inventory.csv`: file-level inventory for all 15 source workbooks;
- `sheet_inventory.csv`: classification and dimensions for all 96 worksheets;
- `measurement_index.csv`: metadata and classification for the 357 core measurements;
- `standardized_signals.csv.gz`: 437,956 standardized time-series rows;
- `data_quality_log.csv`: information-level and manual-review records;
- `exclusion_log.csv`: non-core worksheets and measurement blocks that could not be extracted;
- `field_dictionary.csv`: field definitions and units;
- `data_processing_pipeline.py`: reproducible processing code.

## 4. How the team can use the outputs

Team members responsible for conventional LAOS metrics, transient metrics, CWT/DWT, or feature selection can:

1. select experimental type, condition, and source from `measurement_index.csv`;
2. use `measurement_id` to retrieve the corresponding time series from `standardized_signals.csv.gz`;
3. exclude or separately inspect `STEP_UNKNOWN`, `qc_status=REVIEW`, and duplicate records;
4. use `source_file`, `sheet`, and `source_row` to trace a value back to the source Excel workbook.

## 5. Current limitation

The 15 supplied files are primarily UDEL/ARES-G2 datasets. They support development of a consistent schema and processing rules, but they do not establish the exact column names, sampling rate, or record size of a Haemograph export. At least one genuine Haemograph raw export is still required to report the Haemograph data size and confirm its mapping to the standardized fields.

This part does not provide biomedical interpretation and does not demonstrate that any variable has diagnostic value.
