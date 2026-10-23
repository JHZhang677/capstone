# Feature integration for the Haemograph project

This folder contains the code used for the integrated feature review in Part 5 of the report. It combines the final outputs from the LAOS, step-response and signal-transform analyses. It does not replace the analysis code owned by the other group members.

The main tasks are:

- checking that feature tables can be linked to the shared measurement index;
- testing the FFT high-to-low energy ratio at 25 Hz and 50 Hz;
- reviewing overlap between related features within workbooks;
- producing the final candidate-feature table from the saved evidence.

## Folder contents

```text
src/
  audit_inputs.py
  integrate_features.py
  fft_sampling_check.py
  select_features.py
data/
  feature_decisions.csv
  redundancy_checks.csv
tests/
  test_feature_selection.py
requirements.txt
```

## Input files

The scripts expect outputs produced by the shared pipeline and the other analysis parts:

- `measurement_index.csv`
- `standardized_signals.csv.gz`
- `laos_features.csv`

The raw workbooks and measurement-level derived data are not included in this folder. They should remain in the controlled project storage. Paths are supplied through command-line arguments, so the scripts do not depend on one person's computer.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Check the input cohorts:

```bash
python src/audit_inputs.py \
  --measurement-index /path/to/measurement_index.csv \
  --laos-features /path/to/laos_features.csv \
  --output results/input_audit.csv
```

Create a measurement-level table from the final feature outputs:

```bash
python src/integrate_features.py \
  --measurement-index /path/to/measurement_index.csv \
  --laos-features /path/to/laos_features.csv \
  --step-features /path/to/step_features.csv \
  --output results/integrated_features.csv
```

Run the FFT grid check:

```bash
python src/fft_sampling_check.py \
  --signals /path/to/standardized_signals.csv.gz \
  --laos-features /path/to/laos_features.csv \
  --output-dir results/fft_sampling
```

Build the final feature table:

```bash
python src/select_features.py \
  --decisions data/feature_decisions.csv \
  --redundancy data/redundancy_checks.csv \
  --output-dir results/feature_selection
```

The feature table is a record of the report decision. The six criteria were used as a checklist, not as a fitted prediction model. The selected features still need independent testing on Haemograph recordings.
