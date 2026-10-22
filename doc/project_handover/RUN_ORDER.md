# Analysis run order

For final report values, use the corrected package README first. The list below locates original source workflows. Configure paths and read dependencies in each notebook before execution. A saved notebook is not proof that it was rerun in this repository.

## Shared ingestion

Extract time-stamped blocks, inventories and QC tables from the original Armstrong workbooks.

- Code: [`data_processing_pipeline__1233b8e5e7.py`](../../example_code/analysis_version_history/shared_ingestion_and_step_138/data_processing_pipeline__1233b8e5e7.py)
- Original context: `03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data/data_processing_pipeline.py`

## Conventional LAOS

Use the shared signals/index to produce conventional features, matched instrument checks and sensitivity tables.

- Code: [`conventional_laos_analysis_final__93458f79d1.ipynb`](../../example_code/analysis_version_history/conventional_laos/conventional_laos_analysis_final__93458f79d1.ipynb)
- Original context: `03_Team_Contributions/Part2_Conventional_LAOS/Extracted_Contents/Part2 ¿C Conventional LAOS Analysis/Conventional_LAOS_Analysis_Final.ipynb`

## Primary step analysis

Produce the original step-analysis outputs; apply the final corrected report workflow for the missing-reference settling fix.

- Code: [`step_updown_analysis__18231aef66.ipynb`](../../example_code/analysis_version_history/shared_ingestion_and_step_138/step_updown_analysis__18231aef66.ipynb)
- Original context: `03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data/Step_UpDown_Analysis.ipynb`

## Separate step branch

Preserve this branch separately; its raw-workbook crosswalk/denominators are not interchangeable with the primary analysis.

- Code: [`member3_step_updown_analysis__e57cfc41bd.ipynb`](../../example_code/analysis_version_history/step_analysis_separate_branch/member3_step_updown_analysis__e57cfc41bd.ipynb)
- Original context: `03_Team_Contributions/Part3_Step_Transient_Analysis/notebooks/Member3_Step_UpDown_Analysis.ipynb`

## Measured transforms/integration

Load saved feature/cohort tables and compare measured-data Fourier/wavelet features. The report package contains the corrected condition-audit copy.

- Code: [`blood_feature_integration_original_final__19c225949b.ipynb`](../../example_code/analysis_version_history/other_code_history/blood_feature_integration_original_final__19c225949b.ipynb)
- Original context: `01_Active_Blood_Project/02_Code/00_feature_integration_Final.ipynb`

## Synthetic event benchmark v1

Generate and analyse ten designed scenarios; this is the earlier benchmark.

- Code: [`synthetic_clot_time_benchmark__aa8b221a75.ipynb`](../../example_code/analysis_version_history/synthetic_clot_event_benchmarks/synthetic_clot_time_benchmark__aa8b221a75.ipynb)
- Original context: `Syn_code_new/Synthetic_Clot_Time_Benchmark.ipynb`

## Synthetic event benchmark v2

Generate twenty scenario designs with three replicates; write observed data, separate truth labels, quality/manifest tables and paired timing results.

- Code: [`synthetic_clot_time_benchmark_v2__48dbc18380.ipynb`](../../example_code/analysis_version_history/synthetic_clot_event_benchmarks/synthetic_clot_time_benchmark_v2__48dbc18380.ipynb)
- Original context: `Syn_code_new/Synthetic_Clot_Time_Benchmark_v2.ipynb`

## Corrections and archived experiments

Run `correct_analysis.py`, `refine_figures.py` and `phase_and_models.py` as described in `final_code/report_analysis/README.md` to reproduce the targeted report corrections. Model fits are read from saved results; these commands do not refit every model or rerun the synthetic study.

Older chirp/gel/MITMAPS/collagen studies have different data and questions. They are indexed in `CODE_GUIDE.md`; they are not sequential stages of the final blood-analysis pipeline. External MATLAB/LabVIEW/Python reference code may require its own software and licences.
