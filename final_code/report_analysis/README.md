# Corrected report analysis

## Purpose

This is the corrected report-evidence snapshot prepared on 23 October 2026. It includes the original analysis notebooks, targeted correction scripts, supporting tables and figures. Earlier versions remain in `example_code/analysis_version_history`.

## Inputs and outputs

- `supporting_data/`: saved original and corrected measurements/features/statistical tables.
- `supporting_data/corrected_step_138/`: corrected primary step features and tests.
- `code_corrections/`: correction scripts and notebook copies.
- `analysis_sources/`: original notebook snapshots, with their original configuration assumptions.
- `figures/`: final report figures.
- `audit_environment.json`: recorded audit package versions, not a universal pinned environment for all historical notebooks.

## Run order

From this directory, using Python with NumPy, pandas, SciPy, Matplotlib and the packages imported by the saved analysis functions:

```bash
python3 code_corrections/correct_analysis.py
python3 code_corrections/refine_figures.py --project-root /path/to/haemograph_restored
python3 code_corrections/phase_and_models.py --project-root /path/to/haemograph_restored
```

Restore the original code/data layout using `doc/project_handover/restore_original_layout.py` before supplying that project-root path. The first script uses packaged evidence; the latter scripts need the original shared signal table. Inspect each script's docstring and the environment manifest for dependencies.

## What was corrected

Five missing-reference settling times were changed to missing, step magnitude/direction statistics were recomputed with declared Holm families, and affected figures were redrawn. The primary phase result is 129/130; the separate integration branch has different denominators. The measured entropy comparison and synthetic event timing answer different questions. Synthetic labels are not measured clot times.

The historical scripts `reproduce_report_audits.py` and `redraw_step_summaries.py` predate the final step corrections. Do not use them alone to regenerate final results; run the three scripts above afterwards. Guarded notebook outputs were cleared and that whole notebook was not rerun. Saved model fits and the full synthetic benchmark were not independently rerun during report completion or upload preparation.

See the handover guide for dataset identities, source paths, hashes and historical code versions. Upstream code remains attributed to its original authors; AI assistance is documented in the report.
