# Member 2 Final Submission Package — Conventional LAOS Analysis

## Final dataset freeze
Use **181 analysis-ready LAOS measurements from 10 source workbooks** for the Member 2 report. The earlier 184 count came from an exploratory raw inventory and is not the final shared-pipeline analysis count. See `dataset_freeze_audit.csv` and `dataset_freeze_anomalies.csv`.

## Main deliverables
- `Member2_Conventional_LAOS_Methods_Results.docx` — submission-ready report section.
- `Member2_Conventional_LAOS_Methods_Results.pdf` — PDF version of the same section.
- `Conventional_LAOS_Analysis_Final.ipynb` — cleaned analysis notebook.
- `Member2_Final_Methods_and_Results.md` — editable text version.

## Core result tables
- `laos_features.csv` — measurement-level conventional LAOS feature table.
- `result_strain_amplitude_final.csv` — final workbook-level strain-amplitude results.
- `instrument_crossvalidation.csv` — matched recomputed vs rheometer values.
- `instrument_crossvalidation_summary.csv` — G′/G″/I3/I1 validation statistics.
- `metric_reliability_final.csv` — final valid / caution / exploratory labels.
- `dataset_freeze_audit.csv` — 184 vs 181 reconciliation.
- `dataset_freeze_anomalies.csv` — JUN18 source/pipeline anomaly notes.
- `workbook_level_strain_correlations.csv` — per-workbook Spearman results.
- `sensitivity_summary.csv` — cycle selection and detrending sensitivity summary.

## Figures
`figures/` contains 11 publication-ready PNGs, including strain-amplitude plots, instrument cross-validation plots, a representative Lissajous loop and harmonic spectrum.

## Key findings for group integration
1. G′ and G″ decrease consistently with strain amplitude at 0.5, 1 and 5 rad/s.
2. Phase angle and normalized Lissajous area increase with strain amplitude.
3. I3/I1 is frequency-dependent: weak/moderate positive association at 0.5–1 rad/s and negative at 5 rad/s.
4. Instrument cross-validation is strongest for G″ (MdAPE 1.6%, Pearson r 0.999) and I3/I1 (MdAPE 6.5%, Pearson r 0.987). G′ is strongly correlated with instrument values but has larger relative error near zero.
5. First-harmonic metrics are the strongest conventional baselines for comparison with Member 4 transform features; I5/I1 and THD should remain exploratory because of preprocessing sensitivity.
