# Group 24 — revised thesis, 23 October 2026

## Open in Overleaf
Upload the Overleaf ZIP as a new project, select `main.tex`, and compile with pdfLaTeX. All text is in this single source file. All required images are included in `figures/`; no notebook execution or external bibliography file is needed to compile.

## What was corrected
- Guarded settling time against missing late reference stress. Five invalid values are now missing; valid coverage is 123/138, and median step-down settling time is 3.046 s. Related summaries, correlations, Holm tests and figures were regenerated.
- Separated reference availability, late-window stability and settling-time rules. Corrected the broader first-reading result to 56/130.
- Replaced stale evidence/coverage figures, improved selected plot labels and documented the absolute tolerance and model-fit criteria.
- Added a within-workbook Friedman permutation check (one million permutations), and a direct comparison of the two retained LAOS descriptors.
- Reproduced the primary phase contrast from the shared signals: 129/130. Its dependence on the late-window reference is explained.
- Replaced the untraced 159/181 cycle-change claim with the saved, quantitative cycle-window and detrending sensitivity results. No unsupported result was promoted into the final results section.
- Corrected the Pincot interpretation, removed the RMS proxy AUC from the PELT row, and used “feature shortlist” where minimality was not established.
- Expanded abbreviations, symbols, data/feature dictionaries and the dataset catalogue. Original filenames remain unchanged; no donor identity is inferred.
- Revised prose, captions, contents navigation, conclusion and client handover requirements.

## Evidence and execution status
`supporting_data/step_138/` preserves the original saved step outputs. Use `supporting_data/corrected_step_138/step_features.csv` for the corrected 138-record feature table. The top-level Holm CSVs contain the corrected magnitude/direction results. The nine phase/window tests remain in their separate table.

`code_corrections/correct_analysis.py` reproduces the missing-reference correction, dependent statistics, permutation check, retained-feature overlap and core corrected figures using packaged tables and notebook definitions. It does not refit the blood model.

To regenerate the final illustrated figures and primary phase check, run in this order:

```text
python code_corrections/correct_analysis.py
python code_corrections/refine_figures.py --project-root /path/to/Haemograph_Project
python code_corrections/phase_and_models.py --project-root /path/to/Haemograph_Project
```

The last two commands require the original shared signal table. They write to this unpacked report package, not to the raw workbooks. The original full model fits and synthetic benchmark were not rerun in this revision; their saved outputs remain the basis for those sections.

`Step_UpDown_Analysis_Guarded.ipynb` has the guarded extraction function and cleared outputs. Its original exploratory markdown is development history, not the final report's statistical interpretation. `guarded_step_features.py` records the same function. The separate corrected integration notebook retains the strain-fraction/percent repair in cells 116–118. The original source notebooks are under `analysis_sources/`.

The earlier `reproduce_report_audits.py` and `redraw_step_summaries.py` are historical scripts from the previous revision. Do not use their step outputs as the final results: always apply the three final commands above afterwards. The earlier FFT grid-sensitivity and instrument-agreement evidence remains included.

## Original project path mapping
- Shared ingestion and ARM-STEP: `03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data/`.
- Conventional LAOS: `03_Team_Contributions/Part2_Conventional_LAOS/Extracted_Contents/` (the supplied Part2 subfolder).
- Separate raw-workbook step branch: `03_Team_Contributions/Part3_Step_Transient_Analysis/`.
- Integration notebook: `01_Active_Blood_Project/02_Code/00_feature_integration_Final.ipynb`.
- Measured transform outputs: `01_Active_Blood_Project/04_Results/Final_Real_Data_Analysis/` and `Fourier_Wavelet_Feature_Development/`.
- Synthetic benchmark: `Syn_code_new/Synthetic_Clot_Time_Benchmark_v2.ipynb`, with `v2_data/` and `v2_outputs/`.

## Dataset documentation
`supporting_data/documentation/dataset_catalogue.csv` maps descriptive dataset IDs to exact original filenames, worksheet names and extracted block counts. The two AUG18 sources are deliberately distinct. The full index, QC/exclusion logs and expanded field dictionary are included. Raw blood time-series files are not redistributed in the ZIP.

## Team completion still required
Other student IDs, signatures and dates remain blank. Ria Mishra's ID is 1622419. The team must supply completed meeting records, the assessor-accessible repository/submission location and Canvas peer-review confirmation. These cannot be inferred from a blank meeting template or from typesetting the report. The AI declaration is retained for the team's final review.
