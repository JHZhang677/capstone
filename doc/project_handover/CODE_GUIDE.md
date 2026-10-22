# Code versions and roles

Use `final_code/report_analysis` for corrected report calculations. The following are preserved source versions, not a claim that every notebook is runnable without configuration. The catalogue separates file hashes from code-only hashes to distinguish output-only changes.

## Other Code History

Code outside the main analysis directories, including checkpoint snapshots. Original context is recorded in the source mapping.

### blood_feature_integration_earlier__e97b3d0c20.ipynb

Source: `01_Active_Blood_Project/02_Code/00_feature_integration.ipynb`

Status: Archived code. Not rerun for this handover.

Imports: IPython.display; matplotlib.pyplot; numpy; openpyxl; pandas; pathlib; pywt; re; scipy; scipy.integrate; scipy.optimize; time.

Source introduction (historical text):

> # Blood Rheology Feature Integration and Cohort Audit This notebook assembles existing blood-rheology measurements and analysis outputs into a traceable, measurement-level dataset. It documents cohort coverage, reconciles step-measurement identifiers, and provides representative signal previews. Previously generated analyses are loaded as inputs; their calculations are not rerun here. The active scope is human blood rheology. Gel and gel-point measurements are excluded. The source packages and cohort filters differ, so their record counts are reported separately before integration. ## Cohort overview - The standardized data catalogue contains

Referenced file strings (inputs and outputs mixed; inspect configuration):

`*.xlsx; 01_raw_step_block.png; 02_baseline_plateau_vs_flowcurve.png; 03_Team_Contributions/Part2*/Extracted_Contents/*/laos_features.csv; 03_tau_lambda_vs_literature.png; 04_representative_fits.png; 05_magnitude.png; 06_direction_pairs.png; 07_transient_vs_stable.png; 08_dec17_storage.png; 9MAY19 UDEL Blood.xlsx; MOVE_MANIFEST.csv; Part2*/Extracted_Contents/*/laos_features.csv; assessing_native_sampling_support_before_applying_time_frequency_methods.png; cwt_features.csv; data_quality_log.csv; dwt_features.csv; excluded_measurements.csv; exclusion_log.csv; fft_features.csv; field_dictionary.csv; fit_failure_log.csv; instrument_crossvalidation_summary.csv; integrated_measurement_features.csv; laos_feature_relationships_by_transform_family.png; laos_features.csv; measurement_index.csv; method_pairwise_rank_agreement.png; metric_reliability.csv; metric_reliability_final.csv; per_measurement_transform_runtime.png; pipeline_cohort_counts.csv; relaxation_fits.csv; result_direction.csv; result_magnitude.csv; result_strain_amplitude_final.csv; result_transient_vs_stable.csv; standardized_signals.csv; standardized_signals.csv.gz; step_cohort_reconciliation.csv; step_events.csv; step_features.csv; step_measurement_id_crosswalk.csv; step_transform_eligibility.csv; step_transform_support_under_a_shared_64_sample_window_rule.png; step_windows.csv; stft_features.csv; transform_cwt_edge_support_sensitivity.csv; transform_dwt_boundary_sensitivity.csv; transform_feature_dictionary.csv; transform_features_long.csv; transform_features_wide.csv; transform_grouped_associations.csv; transform_me`

### blood_feature_integration_original_final__19c225949b.ipynb

Source: `01_Active_Blood_Project/02_Code/00_feature_integration_Final.ipynb`

Status: Archived code. Not rerun for this handover.

Imports: IPython.display; matplotlib.pyplot; numpy; openpyxl; pandas; pathlib; pywt; re; scipy; scipy.integrate; scipy.optimize; time.

Source introduction (historical text):

> # Blood Rheology Feature Integration and Cohort Audit This notebook assembles existing blood-rheology measurements and analysis outputs into a traceable, measurement-level dataset. It documents cohort coverage, reconciles step-measurement identifiers, and provides representative signal previews. Previously generated analyses are loaded as inputs; their calculations are not rerun here. The active scope is human blood rheology. Gel and gel-point measurements are excluded. The source packages and cohort filters differ, so their record counts are reported separately before integration. ## Cohort overview - The standardized data catalogue contains

Referenced file strings (inputs and outputs mixed; inspect configuration):

`*.xlsx; 01_raw_step_block.png; 02_baseline_plateau_vs_flowcurve.png; 03_Team_Contributions/Part2*/Extracted_Contents/*/laos_features.csv; 03_tau_lambda_vs_literature.png; 04_representative_fits.png; 05_magnitude.png; 06_direction_pairs.png; 07_transient_vs_stable.png; 08_dec17_storage.png; 9MAY19 UDEL Blood.xlsx; MOVE_MANIFEST.csv; Part2*/Extracted_Contents/*/laos_features.csv; assessing_native_sampling_support_before_applying_time_frequency_methods.png; cwt_features.csv; data_quality_log.csv; dataz.xlsx; dwt_features.csv; excluded_measurements.csv; excluded_raw_inputs.csv; exclusion_log.csv; fft_features.csv; field_dictionary.csv; file_inventory.csv; fit_failure_log.csv; instrument_condition_match_audit.csv; instrument_condition_match_summary.csv; instrument_crossvalidation.csv; instrument_crossvalidation_summary.csv; integrated_measurement_features.csv; laos_amplitude_tests_holm.csv; laos_feature_relationships_by_transform_family.png; laos_features.csv; measurement_index.csv; method_pairwise_rank_agreement.png; metric_reliability.csv; metric_reliability_final.csv; per_measurement_transform_runtime.png; pipeline_cohort_counts.csv; raw_source_inventory_audit.csv; relaxation_fits.csv; result_direction.csv; result_magnitude.csv; result_strain_amplitude_final.csv; result_transient_vs_stable.csv; reviewed_laos_metric_status.csv; standardized_signals.csv; standardized_signals.csv.gz; step_cohort_reconciliation.csv; step_cohort_review_summary.csv; step_cohort_unmatched_records.csv; step_direction_tests_holm.csv; step_events.csv; step_features.csv; step_magnitude_tests_holm.csv; s`

### wavelet_rheology_analysis_checkpoint__4dbf5a6b4b.ipynb

Source: `01_Active_Blood_Project/02_Code/Previous_Analysis/.ipynb_checkpoints/Wavelet_Rheology_Analysis-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: fcwt; glob; matplotlib.colors; matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.integrate; scipy.interpolate; scipy.optimize; ssqueezepy; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time-Frequency Analysis of Evolving Fluids ## Haemograph Vocational Placement Project **Reference paper:** Armstrong, Scully, Clark, Corrigan, James (2021), *"A simple approach for adding thixotropy to an elasto-visco-plastic rheological model to facilitate structural interrogation of human blood"*, Journal of Non-Newtonian Fluid Mechanics 290, 104503. --- ### Purpose of this notebook This notebook connects two halves of the project: 1. **The signal-processing half** (our project's core question): can wavelet-based time-frequency analysis resolve structural evolution in a rheological signal better than conventional Fourier met

Referenced file strings (inputs and outputs mixed; inspect configuration):

`cross_experiment_validation.csv; data*.xlsx; data1.xlsx; data5.xlsx; data7.xlsx; data8.xlsx; data9.xlsx; dataset_inventory.csv; experiment_catalogue.csv; method_metrics_primary_experiment.csv; method_ranking.csv`

### wavelet_rheology_analysis_1_checkpoint__46153a6709.ipynb

Source: `01_Active_Blood_Project/02_Code/Previous_Analysis/.ipynb_checkpoints/Wavelet_Rheology_Analysis_1-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: fcwt; glob; matplotlib.colors; matplotlib.gridspec; matplotlib.pyplot; numpy; openpyxl; os; pandas; pywt; scipy; scipy.integrate; scipy.interpolate; scipy.optimize; ssqueezepy; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time-Frequency Analysis of Evolving Fluids **Reference paper:** Armstrong, Scully, Clark, Corrigan, James (2021), *"A simple approach for adding thixotropy to an elasto-visco-plastic rheological model to facilitate structural interrogation of human blood"*, Journal of Non-Newtonian Fluid Mechanics 290, 104503. --- ### Purpose of this notebook This notebook connects two halves of the project: 1. **The signal-processing half** (our project's core question): can wavelet-based time-frequency analysis resolve structural evolution in a rheological signal better than conventional Fourier methods? 2. **The mechanics half** (the refere

Referenced file strings (inputs and outputs mixed; inspect configuration):

`cross_experiment_validation.csv; data*.xlsx; data1.xlsx; data5.xlsx; data7.xlsx; data8.xlsx; data9.xlsx; dataset_inventory.csv; experiment_catalogue.csv; method_metrics_primary_experiment.csv; method_ranking.csv`

### fresh_code_checkpoint__6fb8d61477.ipynb

Source: `01_Active_Blood_Project/02_Code/Previous_Analysis/.ipynb_checkpoints/fresh_code-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: IPython.display; fcwt; glob; importlib; ipywidgets; it; matplotlib.colors; matplotlib.pyplot; numpy; os; pandas; plotly.graph_objects; plotly.subplots; pywt; ruptures; scipy; scipy.integrate; scipy.interpolate; ssqueezepy; sympy; sys; time; warnings.

Source introduction (historical text):

> #### Cell 1: Environment Diagnostic

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Full results saved to cross_experiment_validation.csv; cell06_overshoot_check.png; cell07_synthetic_data.png; cell09_cwt_scalograms.png; cell09b_all_five_cwt.png; cell09c_cwt_ranking.png; cell10_dwt_decomposition.png; cell10b_dwt_ranking.png; cell11_stft_spectrograms.png; cell12_fcwt_scalogram.png; cell12b_full_scoreboard.png; cell13_ssqcwt_comparison.png; cell14_pelt_changepoints.png; cell15_master_table.png; cell18_cross_validation_summary.png; cell19_significance_boxplot.png; cell20_final_summary.png; cross_experiment_validation.csv; data*.xlsx; data1.xlsx; data5.xlsx; data7.xlsx; data8.xlsx; data9.xlsx`

### blood_model_analysis_september23__103875aafc.ipynb

Source: `01_Active_Blood_Project/02_Code/Previous_Analysis/Sept23_code.ipynb`

Status: Archived code. Not rerun for this handover.

Imports: datetime; glob; hashlib; importlib; matplotlib.colors; matplotlib.pyplot; numpy; os; pandas; platform; random; re; sys; warnings.

Source introduction (historical text):

> #### Cell 1: Environment Diagnostic Checking that every library this notebook depends on is present before any data is read, and recording the exact versions for the reproducibility appendix. Libraries are split into two groups. A missing **required** library stops the notebook, because the core pipeline cannot run without it. A missing **optional** library disables one specific comparison and is reported as a gap rather than an error, so the notebook still produces a complete result for everything else. If anything is missing, the install command is printed at the end of the output. Nothing is installed automatically, since silently changing

Referenced file strings (inputs and outputs mixed; inspect configuration):

`*.xlsx; data*.xlsx`

### wavelet_rheology_analysis__31b98700cc.ipynb

Source: `01_Active_Blood_Project/02_Code/Previous_Analysis/Wavelet_Rheology_Analysis.ipynb`

Status: Archived code. Not rerun for this handover.

Imports: fcwt; glob; matplotlib.colors; matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.integrate; scipy.interpolate; scipy.optimize; ssqueezepy; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time-Frequency Analysis of Evolving Fluids **Reference paper:** Armstrong, Scully, Clark, Corrigan, James (2021), *"A simple approach for adding thixotropy to an elasto-visco-plastic rheological model to facilitate structural interrogation of human blood"*, Journal of Non-Newtonian Fluid Mechanics 290, 104503. --- ### Purpose of this notebook This notebook connects two halves of the project: 1. **The signal-processing half** (our project's core question): can wavelet-based time-frequency analysis resolve structural evolution in a rheological signal better than conventional Fourier methods? 2. **The mechanics half** (the refere

Referenced file strings (inputs and outputs mixed; inspect configuration):

`cross_experiment_validation.csv; data*.xlsx; data1.xlsx; data5.xlsx; data7.xlsx; data8.xlsx; data9.xlsx; dataset_inventory.csv; experiment_catalogue.csv; method_metrics_primary_experiment.csv; method_ranking.csv`

### wavelet_rheology_analysis_1__5b6e315f03.ipynb

Source: `01_Active_Blood_Project/02_Code/Previous_Analysis/Wavelet_Rheology_Analysis_1.ipynb`

Status: Archived code. Not rerun for this handover.

Imports: fcwt; glob; matplotlib.colors; matplotlib.font_manager; matplotlib.gridspec; matplotlib.patches; matplotlib.patheffects; matplotlib.pyplot; numpy; openpyxl; os; pandas; pywt; scipy; scipy.integrate; scipy.interpolate; scipy.optimize; ssqueezepy; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time-Frequency Analysis of Evolving Fluids **Reference paper:** Armstrong, Scully, Clark, Corrigan, James (2021), *"A simple approach for adding thixotropy to an elasto-visco-plastic rheological model to facilitate structural interrogation of human blood"*, Journal of Non-Newtonian Fluid Mechanics 290, 104503. --- ### Purpose of this notebook This notebook connects two halves of the project: 1. **The signal-processing half** (our project's core question): can wavelet-based time-frequency analysis resolve structural evolution in a rheological signal better than conventional Fourier methods? 2. **The mechanics half** (the refere

Referenced file strings (inputs and outputs mixed; inspect configuration):

`bold_hero_banner.png; bold_overshoot.png; bold_ranking.png; bold_scalogram_hero.png; bold_showdown.png; cross_experiment_validation.csv; data*.xlsx; data1.xlsx; data5.xlsx; data7.xlsx; data8.xlsx; data9.xlsx; dataset_inventory.csv; experiment_catalogue.csv; method_metrics_primary_experiment.csv; method_ranking.csv`

### data_processing_pipeline_final__15475fc4c4.py

Source: `01_Active_Blood_Project/02_Code/data_processing_pipeline_final.py`

Status: Archived code. Not rerun for this handover.

Imports: __future__; argparse; hashlib; json; math; numpy; openpyxl; pandas; pathlib; re; shutil.

Source introduction (historical text):

> #!/usr/bin/env python3 """Final scoped Part 1 pipeline for the haemograph blood-rheology cohort. This copy preserves the teammate pipeline and adds explicit exclusion of DataZ and Excel lock files when selecting workbooks. It does not calculate LAOS 

Referenced file strings (inputs and outputs mixed; inspect configuration):

`*.xlsx; data_quality_log.csv; dataz.xlsx; exclusion_log.csv; field_dictionary.csv; file_inventory.csv; measurement_index.csv; processing_summary.json; sheet_inventory.csv; standardized_signals.csv.gz`

### wavelet_pipeline_eggyolk_checkpoint__0fa57a61d7.ipynb

Source: `05_Presentations/Previous_Semester/MAST90106/rohan/.ipynb_checkpoints/wavelet_pipeline_eggyolk-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib.colors; matplotlib.gridspec; matplotlib.pyplot; numpy; pandas; pywt; scipy.fft; scipy.ndimage; scipy.signal; scipy.signal.windows; statsmodels.tsa.stattools; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time–Frequency Analysis Pipeline ### Haemograph Microfluidic Rheometer — Full Analysis (Phases A–W) ---

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Dashboard saved → phase_V_dashboard.png; egg-yolk-rawdata.xlsx; phase_V_dashboard.png`

### wavelet_pipeline_eggyolk__4fdd8e87f1.ipynb

Source: `05_Presentations/Previous_Semester/MAST90106/rohan/wavelet_pipeline_eggyolk.ipynb`

Status: Archived code. Not rerun for this handover.

Imports: matplotlib.colors; matplotlib.gridspec; matplotlib.pyplot; numpy; pandas; pywt; scipy.fft; scipy.ndimage; scipy.signal; scipy.signal.windows; statsmodels.tsa.stattools; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time–Frequency Analysis Pipeline ### Haemograph Microfluidic Rheometer — Full Analysis (Phases A–W) ---

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Dashboard saved → phase_V_dashboard.png; egg-yolk-rawdata.xlsx; phase_V_dashboard.png`

## External Rheology Monitoring

Upstream rheology-health-monitoring scripts and data. Preserve its LICENSE and source README; do not attribute this implementation to the student team.

### g3_sgr__9047fecba2.m

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/data/synthetic/g3_sgr.m`

Status: Third-party reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> function [ g3, LRw1, LRw2, LRw3, LRsum, g3_tss ] = SGR_function( x, w1, w2, w3 ) w1 = w1( : ); w2 = w2( : ); w3 = w3( : ); data = LR_function( x, [ w1 w2 w3 ] ); % Careful about the "." it makes sure that the complex conjugate isn't % taken. This is 

### sgr_ann__02b48b4085.m

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/data/synthetic/sgr_ann.m`

Status: Third-party reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> clear; format long e; % Define the parameter space over which to do the calculation %k = logspace( -1, 5, 100 ); % Pa %f = logspace( -4, 1, 10 ); % Hz %x = linspace( 1.01, 8, 100 ); % dimensionless %omega_0 = logspace( -5, -1, 10 ); % Hz % Define the

### sgr_lr__589afb6982.m

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/data/synthetic/sgr_lr.m`

Status: Third-party reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> clear; format long e; % Define the parameter space over which to do the calculation %k = logspace( -1, 5, 100 ); % Pa %f = logspace( -4, 1, 10 ); % Hz %x = linspace( 1.01, 8, 100 ); % dimensionless %omega_0 = logspace( -5, -1, 10 ); % Hz freqs = [0.5

### txt_to_csv__2d417d44f7.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/data/txt_to_csv.py`

Status: Third-party reference. Not rerun for this handover.

Imports: numpy; pandas.

Source introduction (historical text):

> import numpy as np import pandas as pd # Read file minutes = 5 with open(f"maps/maps_005Pa_02rads_{minutes}min.txt") as f: text = f.read() text = text.split("[step]") exps = [] strains = [] for exp in text[1:]: lines = exp.split("\n") data = [] for l

Referenced file strings (inputs and outputs mixed; inspect configuration):

`maps/maps_005Pa_02rads_{k+1}.csv; maps/maps_005Pa_02rads_{minutes}min.txt`

### make_plots__5c072bd09f.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/make_plots.py`

Status: Third-party reference. Not rerun for this handover.

Imports: keras.models; matplotlib.pyplot; numpy; pandas; tensorflow; timeit.

Source introduction (historical text):

> import numpy as np import matplotlib.pyplot as plt import tensorflow as tf import keras.models import pandas as pd import timeit def nll_gumbel(y_true, y_pred): # Negative log-likelihood for a Gumbel distribution z = tf.divide(y_true, tf.square(y_pre

Referenced file strings (inputs and outputs mixed; inspect configuration):

`data/saos/saos_{mins[i]}min.csv; noise_temperature.pdf`

### process_maps__e1ef05d0e1.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/process_maps.py`

Status: Third-party reference. Not rerun for this handover.

Imports: matplotlib.pyplot; matplotlib.ticker; numpy; pandas.

Source introduction (historical text):

> import numpy as np import pandas as pd import matplotlib.pyplot as plt from matplotlib.ticker import MultipleLocator data_all = [] for k in range(1,3): w0 = 0.2 # Fundamental frequency # Loop through amplitudes ws = [] stressFTs = [] strainFTs = [] f

Referenced file strings (inputs and outputs mixed; inspect configuration):

`data/maps/maps_{amp}Pa_02rads_{k}.csv`

### sgr_lr__ef0ab0bdfe.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/sgr_lr.py`

Status: Third-party reference. Not rerun for this handover.

Imports: keras; keras.backend; keras.layers; keras.models; matplotlib.markers; matplotlib.pyplot; numpy; numpy.matlib; pandas; scipy.io; tensorflow.

Source introduction (historical text):

> import numpy as np import numpy.matlib as matlib import scipy.io as sio import matplotlib.pyplot as plt import matplotlib.markers from keras.models import Model, Sequential from keras.layers import Input, Dense, add, Lambda, concatenate import keras.

Referenced file strings (inputs and outputs mixed; inspect configuration):

`data/saos/saos_{mins[i]}min.csv`

### sgr_lr_unc__49158ff422.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/sgr_lr_unc.py`

Status: Third-party reference. Not rerun for this handover.

Imports: keras; keras.backend; keras.layers; keras.models; matplotlib.markers; matplotlib.pyplot; numpy; numpy.matlib; pandas; scipy.io; tensorflow.

Source introduction (historical text):

> import numpy as np import numpy.matlib as matlib import scipy.io as sio import matplotlib.pyplot as plt import matplotlib.markers from keras.models import Model, Sequential from keras.layers import Input, Dense, add, Lambda, concatenate import keras.

### sgr_maps__f96cc5650f.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/sgr_maps.py`

Status: Third-party reference. Not rerun for this handover.

Imports: keras; keras.backend; keras.layers; keras.models; matplotlib.markers; matplotlib.pyplot; numpy; numpy.matlib; scipy.io; tensorflow.

Source introduction (historical text):

> import numpy as np import numpy.matlib as matlib import scipy.io as sio import matplotlib.pyplot as plt import matplotlib.markers from keras.models import Model, Sequential from keras.layers import Input, Dense, add, Lambda, concatenate import keras.

### sgr_maps_unc__c39a845594.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/sgr_maps_unc.py`

Status: Third-party reference. Not rerun for this handover.

Imports: keras; keras.backend; keras.layers; keras.models; matplotlib.markers; matplotlib.pyplot; numpy; numpy.matlib; scipy.io; tensorflow.

Source introduction (historical text):

> import numpy as np import numpy.matlib as matlib import scipy.io as sio import matplotlib.pyplot as plt import matplotlib.markers from keras.models import Model, Sequential from keras.layers import Input, Dense, add, Lambda, concatenate import keras.

### sgr_synthetic__13359ce8b3.py

Source: `01_Active_Blood_Project/02_Code/Device_and_Monitoring_Reference/rheology-health-monitoring/sgr_synthetic.py`

Status: Third-party reference. Not rerun for this handover.

Imports: keras; keras.backend; keras.layers; keras.models; matplotlib.markers; matplotlib.pyplot; numpy; numpy.matlib; scipy.io; tensorflow.

Source introduction (historical text):

> import numpy as np import numpy.matlib as matlib import scipy.io as sio import matplotlib.pyplot as plt import matplotlib.markers from keras.models import Model, Sequential from keras.layers import Input, Dense, add, Lambda, concatenate import keras.

## Blood Model Prototypes

Earlier model-derived feature comparisons and transient-detection prototypes. The revised prototype distinguishes designed event timing from measured feature associations.

### blood_model_prototype__4436ce7ba7.ipynb

Source: `02_Synthetic_Benchmark/01_Model_Prototype/fresh_code.ipynb`

Status: Exploratory models. Not rerun for this handover.

Imports: IPython.display; fcwt; glob; importlib; ipywidgets; it; matplotlib.colors; matplotlib.pyplot; numpy; os; pandas; plotly.graph_objects; plotly.subplots; pywt; ruptures; scipy; scipy.integrate; scipy.interpolate; ssqueezepy; sympy; sys; time; warnings.

Source introduction (historical text):

> #### Cell 1: Environment Diagnostic

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Full results saved to cross_experiment_validation.csv; cell06_overshoot_check.png; cell07_synthetic_data.png; cell09_cwt_scalograms.png; cell09b_all_five_cwt.png; cell09c_cwt_ranking.png; cell10_dwt_decomposition.png; cell10b_dwt_ranking.png; cell11_stft_spectrograms.png; cell12_fcwt_scalogram.png; cell12b_full_scoreboard.png; cell13_ssqcwt_comparison.png; cell14_pelt_changepoints.png; cell15_master_table.png; cell18_cross_validation_summary.png; cell19_significance_boxplot.png; cross_experiment_validation.csv; data*.xlsx; data1.xlsx; data5.xlsx; data7.xlsx; data8.xlsx; data9.xlsx`

### blood_model_transient_validation__1a1c50c97f.ipynb

Source: `02_Synthetic_Benchmark/01_Model_Prototype/fresh_code_v2.ipynb`

Status: Exploratory models. Not rerun for this handover.

Imports: IPython.display; ctypes; glob; importlib; importlib.util; math; matplotlib.colors; matplotlib.pyplot; numpy; os; pandas; pathlib; pywt; ruptures; ruptures.base; ruptures.costs; ruptures.exceptions; scipy; scipy.integrate; scipy.ndimage; scipy.stats; ssqueezepy; ssqueezepy.experimental; sympy; sys; time; warnings.

Source introduction (historical text):

> # Transient Detection with the Armstrong Blood-Rheology Data ## Paper-based model, signal-processing comparison, and controlled validation This notebook preserves the original paper-based model and data-parsing approach while rebuilding the validation around the study’s central question: **does a method locate a known event time, or does it only resemble a model output?** The experimental workbooks contain Armstrong blood-rheology measurements. They do not contain independently labelled clot or gel times. The synthetic benchmark therefore provides the primary timing ground truth, while the real measurements are used for sampling-quality check

Referenced file strings (inputs and outputs mixed; inspect configuration):

`benchmark_progress.csv; data*.xlsx; data1.xlsx; data5.xlsx; data7.xlsx; data8.xlsx; data9.xlsx; global_fft_summary.csv; method_performance_summary.csv; method_status_summary.csv; paired_scenario_error_matrix.csv; paired_wilcoxon_holm.csv; physical_frequency_validation.csv; real_step_sampling_audit.csv; synthetic_method_results.csv; synthetic_scenarios.csv; synthetic_trial_manifest.csv; transform_parameter_table.csv`

## Synthetic Rheology Ten Scenarios

Ten earlier rheology-inspired scenario files with constitutive/latent quantities and known synthetic events. Separate study from the later multisine event benchmark.

### synthetic_rheology_benchmark__9bcebf6845.ipynb

Source: `02_Synthetic_Benchmark/02_Ten_Dataset_Ground_Truth_Study/synthetic_rheology_benchmark.ipynb`

Status: Synthetic development study. Not rerun for this handover.

Imports: ctypes; fcwt; fractions; functools; json; math; matplotlib.pyplot; numpy; pandas; pathlib; platform; pywt; scipy; scipy.ndimage; scipy.stats; time; warnings.

Source introduction (historical text):

> # Synthetic Rheology Benchmark: Ten Controlled Data Sets ## Scope This notebook creates ten independent rheology-inspired synthetic experiments with known constitutive inputs, latent structure, event times, and acquisition faults. It evaluates Fourier and wavelet features against the generating truth. The measured channels are used for feature extraction; the truth columns are used only for scoring. The active project concerns Haemograph-style blood rheology. These simulations are engineering benchmarks, not patient data or calibrated physiological estimates. Gel, gelatin, agar, and alginate examples are outside scope.

Referenced file strings (inputs and outputs mixed; inspect configuration):

`01_observed_trace_gallery.png; 02_laos_harmonic_recovery.png; 03_step_transient_method_comparison.png; 04_triangle_ramp_hysteresis.png; 05_sampling_noise_window_sensitivity.png; 06_expanded_cwt_dwt_method_comparison.png; 07_expanded_wavelet_runtime_comparison.png; 08_step_common_window_method_comparison.png; ]}.csv; computation_time_summary.csv; continuous_wavelet_method_inventory.csv; cwt_edge_effect_sensitivity.csv; discrete_wavelet_method_inventory.csv; expanded_wavelet_computation_times.csv; expanded_wavelet_feature_dictionary.csv; expanded_wavelet_runtime_by_engine.csv; feature_dictionary.csv; laos_cwt_family_performance_summary.csv; laos_fourier_and_cwt_method_comparison.csv; laos_full_cwt_family_sweep.csv; laos_harmonic_feature_table.csv; laos_harmonic_method_comparison.csv; laos_sampling_noise_window_sensitivity.csv; model_parameter_table.csv; quality_check_summary.csv; sampling_support_audit.csv; step_all_builtin_dwt_feature_comparison.csv; step_common_window_cwt_dwt_stft_comparison.csv; step_conventional_baseline_feature_comparison.csv; step_conventional_baseline_performance_summary.csv; step_cwt_dwt_feature_summary.csv; step_cwt_variant_performance_summary.csv; step_dwt_basis_performance_summary.csv; step_full_cwt_family_feature_comparison.csv; step_local_transform_features.csv; step_transient_method_comparison_by_experiment.csv; synthetic_dataset_manifest.csv; transform_parameter_table.csv; triangle_ramp_hysteresis_area.csv`

## Shared Ingestion And Step 138

Long signal table, measurement index, dictionaries, source inventories, QC/exclusions and primary conventional step results. 357 core blocks; primary step cohort 138. Original and corrected outputs are kept distinct.

### step_updown_analysis__18231aef66.ipynb

Source: `03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data/Step_UpDown_Analysis.ipynb`

Status: Team analysis source snapshot. Not rerun for this handover.

Imports: matplotlib.pyplot; numpy; openpyxl; pandas; pathlib; re; scipy; scipy.integrate; scipy.optimize.

Source introduction (historical text):

> ## 1. Load the step-up/down blocks Every workbook uses the ARES-G2 export layout: row 1 holds the test label (e.g. `5-->2.5 (1/s)`), row 2 the variable names (`Step time`, `Stress`, `Strain`, `Shear rate`, …) and row 3 the units, with one block of columns per test. The reader below is **non-destructive**: it never edits the workbook and keeps the workbook, sheet and block number for every row, so each measurement can be traced back to its source. APR18 has its header one row lower than the other files; the reader detects this automatically.

Referenced file strings (inputs and outputs mixed; inspect configuration):

`*.xlsx; 01_raw_step_block.png; 02_baseline_plateau_vs_flowcurve.png; 03_tau_lambda_vs_literature.png; 04_representative_fits.png; 05_magnitude.png; 06_direction_pairs.png; 07_transient_vs_stable.png; 08_dec17_storage.png; fit_failure_log.csv; metric_reliability.csv; relaxation_fits.csv; result_direction.csv; result_magnitude.csv; result_transient_vs_stable.csv; step_events.csv; step_features.csv; step_windows.csv`

### data_processing_pipeline__1233b8e5e7.py

Source: `03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data/data_processing_pipeline.py`

Status: Team analysis source snapshot. Not rerun for this handover.

Imports: __future__; argparse; hashlib; json; math; numpy; openpyxl; pandas; pathlib; re; shutil.

Source introduction (historical text):

> #!/usr/bin/env python3 """Part 1 only: inventory, classify, standardize, and quality-check rheology files. This script deliberately does not calculate LAOS harmonics, wavelets, model fits, or feature-selection results. Source workbooks are opened rea

Referenced file strings (inputs and outputs mixed; inspect configuration):

`*.xlsx; data_quality_log.csv; exclusion_log.csv; field_dictionary.csv; file_inventory.csv; measurement_index.csv; processing_summary.json; sheet_inventory.csv; standardized_signals.csv.gz`

## Conventional Laos

Conventional LAOS feature table and cohort, instrument-comparison and sensitivity results; final cohort 181 records. Includes frequency/strain metadata and G-prime/G-double-prime/harmonic features.

### conventional_laos_analysis_final__93458f79d1.ipynb

Source: `03_Team_Contributions/Part2_Conventional_LAOS/Extracted_Contents/Part2 ¿C Conventional LAOS Analysis/Conventional_LAOS_Analysis_Final.ipynb`

Status: Team analysis source snapshot. Not rerun for this handover.

Imports: matplotlib.pyplot; numpy; pandas; pathlib; scipy.

Source introduction (historical text):

> # Member 2 — Conventional LAOS Analysis (Final) **Purpose.** Validate conventional LAOS measures and test whether they describe strain-dependent nonlinear behaviour in the shared Armstrong blood dataset. **Final freeze:** 181 analysis-ready LAOS measurements from 10 source workbooks. The exploratory count of 184 is not used for the final analysis; see `dataset_freeze_audit.csv`.

Referenced file strings (inputs and outputs mixed; inspect configuration):

`9MAY19 UDEL Blood.xlsx; measurement_index.csv; standardized_signals.csv`

## Step Analysis Separate Branch

Separate raw-workbook/step-analysis branch. Its mappings and valid-comparison denominators differ from the primary 138-record analysis. Refer to each saved index instead of merging by count.

### member3_step_updown_analysis__e57cfc41bd.ipynb

Source: `03_Team_Contributions/Part3_Step_Transient_Analysis/notebooks/Member3_Step_UpDown_Analysis.ipynb`

Status: Separate analysis branch. Not rerun for this handover.

Imports: matplotlib.pyplot; numpy; openpyxl; pandas; pathlib; re; scipy; scipy.integrate; scipy.optimize.

Source introduction (historical text):

> # Member 3 — Step-Up / Step-Down and Transient Rheology Analysis (Member 1 standardised data) **Project:** Haemograph capstone, Semester 2 — LAOS and step rheology of human blood **Role (Work Allocation Framework, Member 3):** validate conventional transient measures and determine how the stress response depends on **step magnitude**, **step direction** and **measurement phase** (transient vs stable). > **This version reads Member 1's standardised dataset** (`main-data/`: `measurement_index.csv` + `standardized_signals.csv.gz`, produced by `data_processing_pipeline.py`) instead of opening the Excel workbooks directly, as the framework require

Referenced file strings (inputs and outputs mixed; inspect configuration):

`01_raw_step_block.png; 02_baseline_plateau_vs_flowcurve.png; 03_tau_lambda_vs_literature.png; 04_representative_fits.png; 05_magnitude.png; 06_direction_pairs.png; 07_transient_vs_stable.png; 08_dec17_storage.png; excluded_measurements.csv; fit_failure_log.csv; measurement_index.csv; metric_reliability.csv; relaxation_fits.csv; result_direction.csv; result_magnitude.csv; result_transient_vs_stable.csv; standardized_signals.csv; standardized_signals.csv.gz; step_events.csv; step_features.csv; step_windows.csv; {name}.csv`

## Gel Scope Experiments

Archived gel-scope notebook; its source wording and output remain historical.

### gel_point_pipeline__75dad494cc.ipynb

Source: `90_Archives/Gel_Scope_Experiments/gel_point_pipeline.ipynb`

Status: Archived exploratory work. Not rerun for this handover.

Imports: importlib; itertools; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.integrate; scipy.signal; scipy.special; sklearn.neural_network; sklearn.preprocessing; sys; time; warnings.

Source introduction (historical text):

> # Gel Point Detection in Evolving Fluids **Wavelet-Based Time-Frequency Analysis of Evolving Fluids in a Microfluidic Rheometer** Haemograph Pty Ltd industry project, Master of Data Science. This notebook builds one pipeline that finds the moment a liquid turns into a gel. In blood that moment is the clot point, and finding it quickly and reliably is the whole reason Haemograph's microfluidic rheometer exists. The notebook is organised in five parts. **Part 1. Real chirp data.** We take a genuine chirp rheology recording from an ARES G2 rheometer and turn it into viscoelastic spectra. The sample in that file happens to stiffen by four orders 

Referenced file strings (inputs and outputs mixed; inspect configuration):

`DataZ.xlsx`

## Earlier Step Handover

Earlier step notebook and saved handover outputs; version-history material rather than an alternative final denominator.

### member3_step_updown_analysis__e57cfc41bd.ipynb

Source: `90_Archives/Mixed_Handover_Bundle/Extracted_Contents/New folder/step_mine.ipynb`

Status: Archived team handover. Not rerun for this handover.

Imports: matplotlib.pyplot; numpy; openpyxl; pandas; pathlib; re; scipy; scipy.integrate; scipy.optimize.

Source introduction (historical text):

> # Member 3 — Step-Up / Step-Down and Transient Rheology Analysis (Member 1 standardised data) **Project:** Haemograph capstone, Semester 2 — LAOS and step rheology of human blood **Role (Work Allocation Framework, Member 3):** validate conventional transient measures and determine how the stress response depends on **step magnitude**, **step direction** and **measurement phase** (transient vs stable). > **This version reads Member 1's standardised dataset** (`main-data/`: `measurement_index.csv` + `standardized_signals.csv.gz`, produced by `data_processing_pipeline.py`) instead of opening the Excel workbooks directly, as the framework require

Referenced file strings (inputs and outputs mixed; inspect configuration):

`01_raw_step_block.png; 02_baseline_plateau_vs_flowcurve.png; 03_tau_lambda_vs_literature.png; 04_representative_fits.png; 05_magnitude.png; 06_direction_pairs.png; 07_transient_vs_stable.png; 08_dec17_storage.png; excluded_measurements.csv; fit_failure_log.csv; measurement_index.csv; metric_reliability.csv; relaxation_fits.csv; result_direction.csv; result_magnitude.csv; result_transient_vs_stable.csv; standardized_signals.csv; standardized_signals.csv.gz; step_events.csv; step_features.csv; step_windows.csv; {name}.csv`

## Previous Semester Rheology

Archived industrial OWCh chirps, metal-crosslinked hydrogel SAOS/LAOS, bovine collagen time/frequency sweeps, MITMAPS multitone/SAOS data, xanthan/salt rheology and settling, hydrogel characterisation, DOE/native rheometer files and ShearView material. Source briefs/READMEs describe these non-blood collections.

### draft1_checkpoint__19c2101075.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/.ipynb_checkpoints/Draft1-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy.fft; scipy.signal; scipy.stats; warnings.

Source introduction (historical text):

> No introductory Markdown in source

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Data3_laos.xlsx; Data3_saos.xlsx; Figure saved: cell4_saos_ground_truth.png; cell4_saos_ground_truth.png`

### gelation_analysis_extendedd_checkpoint__295b99b6a4.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/.ipynb_checkpoints/gelation_analysis_extendedd-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib.gridspec; matplotlib.pyplot; numpy; openpyxl; pandas; pywt; scipy.fft; scipy.signal; warnings.

Source introduction (historical text):

> # Gelation Detection — Isothermal Rheology Data **Project:** Wavelet-Based Time–Frequency Analysis of Evolving Fluids (Haemograph) **Sheet used:** `Table 3A_6_ raw data` — isothermal measurements at 85°C, 90°C, 95°C for 6 adhesive systems. **Gelation criteria applied (logical conditions):** 1. **G' > G''** (tan δ < 1) — crossover marks the gel point 2. **Sustained crossover** — G' > G'' must hold for ≥3 consecutive rows (avoids noise spikes) 3. **Rising G'** — storage modulus must be increasing over a rolling window (solid network forming) 4. **tan δ trend** — tan δ must be decreasing toward and below 1

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Figure saved as gelation_plots.png; Figure saved: cwt_features.png; Figure saved: cwt_vs_classical_gelpoint.png; \nFigure saved: fft_stft_cwt_comparison.png; cwt_features.png; cwt_vs_classical_gelpoint.png; fft_stft_cwt_comparison.png; gelation_plots.png; one.xlsx`

### data4_code_checkpoint__6e73727bf5.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/.ipynb_checkpoints/Data4_code-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib.pyplot; numpy; os; pandas; pywt; scipy.signal; scipy.signal.windows; statsmodels.tsa.stattools; sys.

Source introduction (historical text):

> ### Initial Data Inspection and Preparation The dataset consists of rheological measurements of bovine collagen at three concentrations: 0.8%, 1.5%, and 2.3%, each with multiple experimental replicates. For each replicate, two types of measurements are available: - **Time sweep**: capturing the evolution of material properties during gelation - **Frequency sweep**: capturing viscoelastic properties across frequencies After loading and organizing the dataset, all files were successfully structured into a hierarchical format indexed by concentration, replicate number, and data type. Each replicate contains both time sweep and frequency sweep da

### data4_full_analysis_checkpoint__4cb87107f3.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/.ipynb_checkpoints/Data4_full_analysis-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; scipy; scipy.signal; scipy.stats; statsmodels.tsa.stattools; warnings.

Source introduction (historical text):

> # Data 4 — Bovine Collagen Gelation Analysis ## Full Pipeline: Phases A, B, C, K, L, O, R, S, V **Dataset:** Bovine collagen gelation at 3 concentrations (0.8%, 1.5%, 2.3% w/v) at 37°C **Files:** 20 Excel files — tiempo (time sweep) and frecuencia (frequency sweep) per replicate **Project:** Wavelet-Based Time-Frequency Analysis — Haemograph Pty Ltd ### Important Note on Scope This dataset contains **processed G'(t) and G''(t)** at ~1 Hz — NOT raw stress-strain waveforms. Phases requiring raw waveforms (FFT, CWT, harmonic detection, chirp analysis) belong on Data 1/2/3/6. This notebook focuses on what this dataset CAN contribute: gelation phy

### data4_master_pipeline_checkpoint__7a39e3e3a8.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/.ipynb_checkpoints/Data4_master_pipeline-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib; matplotlib.cm; matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.interpolate; scipy.signal; scipy.stats; statsmodels; statsmodels.tsa.stattools; sys; warnings.

Source introduction (historical text):

> # Data 4 — Bovine Collagen Gelation: Master Analysis Pipeline ## Phases A through W | All 20 Excel Files | Complete Analysis **Dataset:** Bovine collagen gelation at three concentrations (0.8%, 1.5%, 2.3% w/v) at 37 degrees Celsius **Files:** 20 Excel files — tiempo (time sweep) and frecuencia (frequency sweep) per replicate **Project:** Wavelet-Based Time-Frequency Analysis Pipeline — Haemograph Pty Ltd **Industry Partner:** Dr Ragil Krishna, Haemograph Pty Ltd ### Scope Note This dataset contains processed G(t) and G(t) at approximately 1 Hz — not raw stress-strain waveforms. Phases requiring raw waveforms (full FFT pipeline, CWT on raw sig

### wavelet_pipeline_eggyolk_checkpoint__0fa57a61d7.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/.ipynb_checkpoints/wavelet_pipeline_eggyolk-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib.colors; matplotlib.gridspec; matplotlib.pyplot; numpy; pandas; pywt; scipy.fft; scipy.ndimage; scipy.signal; scipy.signal.windows; statsmodels.tsa.stattools; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time–Frequency Analysis Pipeline ### Haemograph Microfluidic Rheometer — Full Analysis (Phases A–W) ---

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Dashboard saved → phase_V_dashboard.png; egg-yolk-rawdata.xlsx; phase_V_dashboard.png`

### bovine_collagen_initial_analysis__d2aea51b1d.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/Data4_code.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: matplotlib.pyplot; numpy; os; pandas; pywt; scipy.signal; scipy.signal.windows; statsmodels.tsa.stattools; sys.

Source introduction (historical text):

> ### Initial Data Inspection and Preparation The dataset consists of rheological measurements of bovine collagen at three concentrations: 0.8%, 1.5%, and 2.3%, each with multiple experimental replicates. For each replicate, two types of measurements are available: - **Time sweep**: capturing the evolution of material properties during gelation - **Frequency sweep**: capturing viscoelastic properties across frequencies After loading and organizing the dataset, all files were successfully structured into a hierarchical format indexed by concentration, replicate number, and data type. Each replicate contains both time sweep and frequency sweep da

### bovine_collagen_full_analysis__31e6631ba9.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/Data4_full_analysis.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; scipy; scipy.signal; scipy.stats; statsmodels.tsa.stattools; warnings.

Source introduction (historical text):

> # Data 4 — Bovine Collagen Gelation Analysis ## Full Pipeline: Phases A, B, C, K, L, O, R, S, V **Dataset:** Bovine collagen gelation at 3 concentrations (0.8%, 1.5%, 2.3% w/v) at 37°C **Files:** 20 Excel files — tiempo (time sweep) and frecuencia (frequency sweep) per replicate **Project:** Wavelet-Based Time-Frequency Analysis — Haemograph Pty Ltd ### Important Note on Scope This dataset contains **processed G'(t) and G''(t)** at ~1 Hz — NOT raw stress-strain waveforms. Phases requiring raw waveforms (FFT, CWT, harmonic detection, chirp analysis) belong on Data 1/2/3/6. This notebook focuses on what this dataset CAN contribute: gelation phy

### bovine_collagen_master_pipeline__b06dbb66cb.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/Data4_master_pipeline.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: matplotlib; matplotlib.cm; matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.interpolate; scipy.signal; scipy.stats; statsmodels; statsmodels.tsa.stattools; sys; warnings.

Source introduction (historical text):

> # Data 4 — Bovine Collagen Gelation: Master Analysis Pipeline ## Phases A through W | All 20 Excel Files | Complete Analysis **Dataset:** Bovine collagen gelation at three concentrations (0.8%, 1.5%, 2.3% w/v) at 37 degrees Celsius **Files:** 20 Excel files — tiempo (time sweep) and frecuencia (frequency sweep) per replicate **Project:** Wavelet-Based Time-Frequency Analysis Pipeline — Haemograph Pty Ltd **Industry Partner:** Dr Ragil Krishna, Haemograph Pty Ltd ### Scope Note This dataset contains processed G(t) and G(t) at approximately 1 Hz — not raw stress-strain waveforms. Phases requiring raw waveforms (full FFT pipeline, CWT on raw sig

### wavelet_pipeline_eggyolk__4c1ac2ef81.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data4/wavelet_pipeline_eggyolk.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: matplotlib.colors; matplotlib.gridspec; matplotlib.pyplot; numpy; pandas; pywt; scipy.fft; scipy.ndimage; scipy.signal; scipy.signal.windows; statsmodels.tsa.stattools; sys; time; warnings.

Source introduction (historical text):

> # Wavelet-Based Time–Frequency Analysis Pipeline ### Haemograph Microfluidic Rheometer — Full Analysis (Phases A–W) ---

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Dashboard saved → phase_V_dashboard.png; egg-yolk-rawdata.xlsx; phase_V_dashboard.png`

### data6_master_pipeline_checkpoint__b1bf50af10.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data6/.ipynb_checkpoints/Data6_master_pipeline-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib; matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.fft; scipy.signal; scipy.stats; statsmodels.tsa.stattools; sys; warnings.

Source introduction (historical text):

> # Data 6 — MITMAPS Multi-tone MAPS Rheological Data: Master Analysis Pipeline ## Phases A through W | Two Files (Maps + SAOS) | Complete Analysis **Dataset:** Multi-tone Medium Amplitude Parallel Superposition (MAPS) rheological data **Source:** github.com/krlennon/mitmaps | Lennon et al. 2020 | MIT Hydrodynamics Lab **Instrument:** TA Instruments Discovery HR-3 | Date: 3/6/2020 **Material:** Viscoelastic fluid **Project:** Wavelet-Based Time-Frequency Analysis Pipeline — Haemograph Pty Ltd ### Files - **Data6_maps.xlsx** — 24 steps (Arbitrary Wave 1-24), each ~26,366 rows at 488, 244, 122, or 61 Hz - **Data6_saos.xlsx** — 16 frequency points

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Data6_maps.xlsx; Data6_saos.xlsx`

### data6_master_pipeline_v2_checkpoint__c6f336b84d.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data6/.ipynb_checkpoints/Data6_master_pipeline_v2-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: matplotlib; matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.fft; scipy.signal; scipy.stats; statsmodels.tsa.stattools; sys; warnings.

Source introduction (historical text):

> # Data 6 — MITMAPS Multi-tone MAPS Rheological Data: Master Analysis Pipeline ## Phases A through W | Two Files (Maps + SAOS) | Complete Analysis **Dataset:** Multi-tone Medium Amplitude Parallel Superposition (MAPS) rheological data **Source:** github.com/krlennon/mitmaps | Lennon et al. 2020 | MIT Hydrodynamics Lab **Instrument:** TA Instruments Discovery HR-3 | Date: 3/6/2020 **Material:** Viscoelastic fluid **Project:** Wavelet-Based Time-Frequency Analysis Pipeline — Haemograph Pty Ltd ### Files - **Data6_maps.xlsx** — 24 steps (Arbitrary Wave 1-24), each ~26,366 rows at 488, 244, 122, or 61 Hz - **Data6_saos.xlsx** — 16 frequency points

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Data6_maps.xlsx; Data6_saos.xlsx`

### untitled_checkpoint__4a62b68a63.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/Data6/.ipynb_checkpoints/Untitled-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> No introductory Markdown in source

### gelation_analysis_extendedd__7597ba0464.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/code/gelation_analysis_extendedd.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: matplotlib.gridspec; matplotlib.pyplot; numpy; openpyxl; pandas; pywt; scipy.fft; scipy.signal; warnings.

Source introduction (historical text):

> # Gelation Detection — Isothermal Rheology Data **Project:** Wavelet-Based Time–Frequency Analysis of Evolving Fluids (Haemograph) **Sheet used:** `Table 3A_6_ raw data` — isothermal measurements at 85°C, 90°C, 95°C for 6 adhesive systems. **Gelation criteria applied (logical conditions):** 1. **G' > G''** (tan δ < 1) — crossover marks the gel point 2. **Sustained crossover** — G' > G'' must hold for ≥3 consecutive rows (avoids noise spikes) 3. **Rising G'** — storage modulus must be increasing over a rolling window (solid network forming) 4. **tan δ trend** — tan δ must be decreasing toward and below 1

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Figure saved as gelation_plots.png; Figure saved: cwt_features.png; Figure saved: cwt_vs_classical_gelpoint.png; \nFigure saved: fft_stft_cwt_comparison.png; cwt_features.png; cwt_vs_classical_gelpoint.png; fft_stft_cwt_comparison.png; gelation_plots.png; one.xlsx`

### exploratory_scratch_notebook__27606a5c8e.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/data/Data6/Untitled.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: openpyxl; openpyxl.styles; openpyxl.utils; pandas; re; sys.

Source introduction (historical text):

> No introductory Markdown in source

Referenced file strings (inputs and outputs mixed; inspect configuration):

`maps.txt; mitmaps_maps.xlsx; mitmaps_saos.xlsx; saos.txt`

### exploratory_scratch_notebook__396051031b.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/data/Untitled.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: pandas; pdfplumber; sys.

Source introduction (historical text):

> No introductory Markdown in source

Referenced file strings (inputs and outputs mixed; inspect configuration):

`2490.pdf; 2490_tables.xlsx; \nSaved {len(all_tables)} tables to 2490_tables.xlsx`

### mitmaps__3c0be5c824.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/MITMAPS.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: mapsio; mapsmodels; mapsplot; mapssim; models; process; sys.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

Referenced file strings (inputs and outputs mixed; inspect configuration):

`../Example Data/saos.txt`

### configuration__b5724ed9ef.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/configuration.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: numpy.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

### mapsio__0f593fc81e.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/mapsio.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: configuration; numpy; os; pandas; process.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

Referenced file strings (inputs and outputs mixed; inspect configuration):

`/output.csv`

### mapsmodels__f83e11a19e.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/mapsmodels.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

### mapsplot__b47d78f22a.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/mapsplot.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: mapsmodels; matplotlib.pyplot; matplotlib.ticker; numpy; process; timeit.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

### mapssim__bc705b5902.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/mapssim.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: models; numpy; process; scipy.integrate.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

### models__0f8b1b2928.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/models.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: numpy.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

### process__a01ce61b46.py

Source: `90_Archives/Previous_Semester_MAST90106/data/mitmaps/src/process.py`

Status: Archived development and external reference. Not rerun for this handover.

Imports: itertools; mapsio; mapsmodels; matplotlib.pyplot; numpy; scipy.interpolate; scipy.optimize; sys.

Source introduction (historical text):

> ## Copyright (C) 2020 Kyle R. Lennon, Michela Geri, Gareth H. McKinley, James W. Swan ## ## This file is part of MITMAPS. ## ## MITMAPS is free software: you can redistribute it and/or modify ## it under the terms of the GNU General Public License as

### rheology_doe_analysis__fd177d73ca.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/data/mrrr7rk5pr-1/DOE Analysis/Analysis.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: collections; datetime; itertools; matplotlib.patches; matplotlib.pyplot; numpy; pandas; pathlib; scipy.optimize; scipy.stats.

Source introduction (historical text):

> # Loading and organizing data

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Example_Hill_Am5.png; Pred x meas Gmax.png; Pred x meas Gplat.png; Pred x meas Gstab.png; Pred x meas khills.png; Pred x meas tg.png; ]}.png; evolution NMR 2.png; evolution NMR.png; oscillatory_example_sample5.png`

### profiles_imaging__15d5466bf1.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/Profiles_Imaging.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### shearview_v1_0_oscillatoryshear__bfb7da842b.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/ShearView/shearview_v1.0_oscillatoryShear.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### bring_to_initial_position__d0a7d68fce.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/bring_to_initial_position.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### bring_to_initial_position_chirp__a822c4c730.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/bring_to_initial_position_chirp.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### bring_to_initial_position_producerconsumer__d646e2174d.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/bring_to_initial_position_producerConsumer.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### calculate_strain__4b50c51ef9.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/calculate_strain.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### calculate_strain_from_array__a6961fd85f.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/calculate_strain_from_array.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### calculate_strain_from_array_normalized__6608c52877.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/calculate_strain_from_array_normalized.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### calculate_strain_from_array_normalized2__36f923f621.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/calculate_strain_from_array_normalized2.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### calculate_strain_from_array_normalized3__8910ab378b.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/calculate_strain_from_array_normalized3.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### command_current__28c2e5f573.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/command_current.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### command_current_producerconsumer__401e23a0a1.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/command_current_producerConsumer.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### currentmeasure__9fa348117f.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/currentMeasure.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### get_chirp_point__e55fb91089.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/get_chirp_point.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### get_chirp_point_nowindow__e18cf5ad44.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/get_chirp_point_noWindow.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### get_sine_point__6cd72d9aa1.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/get_sine_point.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### get_sine_point_from_array__f00654564c.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/get_sine_point_from_array.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### get_sine_point_producerconsumer__cf04ce7ac7.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/get_sine_point_producerConsumer.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### header__e6e40d213d.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/header.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### images_recovery__c967ad7004.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/images_recovery.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### imaging_echoes__2743b9f66e.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/imaging_echoes.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### imaging_echoes_producerconsumer__74c06bc642.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/imaging_echoes_producerConsumer.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### imaging_echoes_producerconsumer2__d486f5f016.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/imaging_echoes_producerConsumer2.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### mean_strain__b41b222be2.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/mean_strain.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### pid_controller__9a86859915.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/pid_controller.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### plotting_subvi__f60fe1654c.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/plotting_subvi.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### plotting_subvi_chirp__ac85fa7053.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/plotting_subvi_chirp.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### read_position__3caea5b93d.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/read_position.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### read_position_nodata__f3e8f76318.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/read_position_nodata.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### read_position_producerconsumer__31ba20afea.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/read_position_producerConsumer.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### recovery_point__e7fff1c149.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/recovery_point.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### recovery_pulses__12610e41b4.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/recovery_pulses.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### shear_and_recovery__87515e5cab.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/shear_and_recovery.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### shear_and_recovery_calculation__0b88896683.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/shear_and_recovery_calculation.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### shear_and_recovery_integral_calculation__45bec310ce.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/shear_and_recovery_integral_calculation.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### shear_and_recovery_points_calculation__3e535a12e3.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/shear_and_recovery_points_calculation.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### shear_cessation_voltage__62621484f0.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/shear_cessation_voltage.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### sinewave_and_stop__91854a5d06.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/sinewave_and_stop.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### sinewave_recovery_array__1dabf32195.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/sinewave_recovery_array.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### start_recovery_imaging__7a8101cc3c.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/start_recovery_imaging.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### start_recovery_imaging_subvi__684e5953b9.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/start_recovery_imaging_subvi.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### strain__1822fcd108.vi

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_LabVIEW/strain.vi`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> Native LabVIEW virtual instrument; requires LabVIEW to inspect/run.

### shearview_analysis__b668a33965.m

Source: `90_Archives/Previous_Semester_MAST90106/data/shearview/shearview_analysis.m`

Status: Archived development and external reference. Not rerun for this handover.

Imports: Not detected / non-Python source.

Source introduction (historical text):

> clear; close all; clc; path = input('Enter path: '); % enter path of the data file A = readmatrix(path); A(end,:) = []; % write results to txt file file = 'your_file.txt'; % file where the resluts will be saved %--------Parameters-------------% volt=

Referenced file strings (inputs and outputs mixed; inspect configuration):

`your_file.txt`

### supervisor_notebook_final_checkpoint__ad7ca75973.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/final_data/.ipynb_checkpoints/supervisor_notebook_final-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: math; matplotlib; matplotlib.colors; matplotlib.pyplot; numpy; os; pandas; pywt; scipy.fft; scipy.ndimage; scipy.optimize; scipy.signal; scipy.special; scipy.stats; sklearn.metrics; sklearn.model_selection; sklearn.neural_network; sklearn.preprocessing; subprocess; time; tqdm; warnings.

Source introduction (historical text):

> # Wavelet-Based Time-Frequency Analysis of Evolving Fluids ## Comprehensive Analysis Notebook — Supervisor Meeting, April 2026 **Haemograph Pty Ltd x Master of Data Science — Capstone Project 2026** **Team:** Ria Mishra, Jianhao Zhang, Xuan Zhang, Xingcan Wang, Rohan Roy Mathew **Supervisors:** Ian Gallagher, Saumya Karunadhika **Host:** Dr Ragil Krishna, Haemograph Pty Ltd --- ### Notebook Structure | Part | Topic | Key References | |------|-------|---------------| | 1 | Rheology fundamentals and clinical motivation | Winter & Chambon 1986; Mours & Winter 1994 | | 2 | Fourier baseline and why it fails | Geri et al. 2018; Holly et al. 1988 | 

Referenced file strings (inputs and outputs mixed; inspect configuration):

`gel_dataset4_laos.xlsx; gel_dataset4_saos.xlsx; owchirp_tcs.xlsx; owchirp_tts.xlsx; part10_entropy_gels.png; part10_significance.png; part11_ann.png; part12_summary.png; part1_fundamentals.png; part2_fourier.png; part2_fourier_failure.png; part3_owch.png; part4_stft.png; part5_cwt_scalograms.png; part5_cwt_vs_fourier.png; part5_wavelets.png; part6_dataset3.png; part6_synthetic_gels.png; part6_tts_aT.png; part7_n_scales.png; part7_omega0_sensitivity.png; part8_features.png; part9_benchmark.png`

### mitmaps_multitone_pipeline__b775e819bd.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/final_data/Data6/Data6_master_pipeline.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: matplotlib; matplotlib.gridspec; matplotlib.pyplot; numpy; os; pandas; pywt; scipy; scipy.fft; scipy.signal; scipy.stats; statsmodels.tsa.stattools; sys; warnings.

Source introduction (historical text):

> # Data 6 — MITMAPS Multi-tone MAPS Rheological Data: Master Analysis Pipeline ## Phases A through W | Two Files (Maps + SAOS) | Complete Analysis **Dataset:** Multi-tone Medium Amplitude Parallel Superposition (MAPS) rheological data **Source:** github.com/krlennon/mitmaps | Lennon et al. 2020 | MIT Hydrodynamics Lab **Instrument:** TA Instruments Discovery HR-3 | Date: 3/6/2020 **Material:** Viscoelastic fluid **Project:** Wavelet-Based Time-Frequency Analysis Pipeline — Haemograph Pty Ltd ### Files - **Data6_maps.xlsx** — 24 steps (Arbitrary Wave 1-24), each ~26,366 rows at 488, 244, 122, or 61 Hz - **Data6_saos.xlsx** — 16 frequency points

Referenced file strings (inputs and outputs mixed; inspect configuration):

`Data6_maps.xlsx; Data6_saos.xlsx`

### code_checkpoint__b703da460a.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/syn_code/.ipynb_checkpoints/code-checkpoint.ipynb`

Status: checkpoint snapshot. Not rerun for this handover.

Imports: math; matplotlib.colors; matplotlib.patches; matplotlib.pyplot; numpy; pandas; pywt; scipy; scipy.signal; ssqueezepy; subprocess; sys.

Source introduction (historical text):

> ## Engineering Criteria (EC) Definitions The following evaluation criteria are used to score each algorithm's performance against ground truth. Each criterion has a defined threshold for pass/fail classification. **EC-01: Gel-point timing accuracy** Measures how accurately the algorithm detects the gel point (the moment G' crosses G''). Computed as the percentage error between estimated and true gel-point time. Threshold: error must be below 5%. **EC-02: Total harmonic distortion (THD)** Measures how much harmonic content the algorithm introduces or fails to suppress. Computed from the ratio of harmonic energy to fundamental energy in the rec

Referenced file strings (inputs and outputs mixed; inspect configuration):

`plot1_clotting_scenarios.png; plot2_fourier_vs_wavelet.png; plot3_wavelet_zoo.png; plot4_scoreboard.png; plot5_dwt_vs_cwt.png; plot6_final_verdict_fixed.png`

### synthetic_engineering_criteria_benchmark__f6986827c7.ipynb

Source: `90_Archives/Previous_Semester_MAST90106/syn_code/code.ipynb`

Status: Archived development and external reference. Not rerun for this handover.

Imports: math; matplotlib.colors; matplotlib.patches; matplotlib.pyplot; numpy; pandas; pywt; scipy; scipy.signal; ssqueezepy; subprocess; sys.

Source introduction (historical text):

> ## Engineering Criteria (EC) Definitions The following evaluation criteria are used to score each algorithm's performance against ground truth. Each criterion has a defined threshold for pass/fail classification. **EC-01: Gel-point timing accuracy** Measures how accurately the algorithm detects the gel point (the moment G' crosses G''). Computed as the percentage error between estimated and true gel-point time. Threshold: error must be below 5%. **EC-02: Total harmonic distortion (THD)** Measures how much harmonic content the algorithm introduces or fails to suppress. Computed from the ratio of harmonic energy to fundamental energy in the rec

Referenced file strings (inputs and outputs mixed; inspect configuration):

`fourier_vs_wavelet.png; mape_scoreboard.png; plot1_clotting_scenarios.png; plot2_fourier_vs_wavelet.png; plot3_wavelet_zoo.png; plot4_scoreboard.png; plot5_dwt_vs_cwt.png; plot6_final_verdict_fixed.png`

## Early Gel Detection

Early gel-point research inputs and notebooks: validation materials, chirp recordings and contextual clot data. Exact duplicates may point to files in another collection.

### gel_detection_research_notebook__676b2b620d.ipynb

Source: `90_Archives/Previous_Versions/proj_ver1/code.ipynb`

Status: Archived exploratory work. Not rerun for this handover.

Imports: PyEMD; ewtpy; fcwt; importlib; itertools; math; matplotlib.pyplot; numpy; os; pandas; pywt; ruptures; scipy.optimize; scipy.signal; scipy.special; ssqueezepy; sys; time; warnings.

Source introduction (historical text):

> # Gel Point Detection in Evolving Fluids Haemograph industry project, Master of Data Science. This notebook answers two questions. **Can we detect the gel point accurately?** The gel point is the moment a liquid becomes a solid. In blood that moment is the clot point, and finding it quickly and reliably is the reason the Haemograph rheometer exists. **Is clotting the same kind of event as gelling?** Polymer gelation and blood coagulation look similar on a plot. Whether they are the same physics, and therefore whether methods developed on gels transfer to blood, is a separate question that Part 7 addresses directly using measured values rather

Referenced file strings (inputs and outputs mixed; inspect configuration):

`DOE.xlsx; app_sheepblood_clot.xlsx; app_teg_paired.xlsx; app_teg_trauma24.xlsx; dev_curing_chirp.xlsx; val_hydrogel_laos.xlsx; val_hydrogel_saos.xlsx; val_micelle_maps.xlsx; val_micelle_saos.xlsx`

### gel_point_detection__5a0a15284e.ipynb

Source: `90_Archives/Previous_Versions/proj_ver1/gel_point_detection.ipynb`

Status: Archived exploratory work. Not rerun for this handover.

Imports: matplotlib.pyplot; numpy; os; pandas; ruptures.

Source introduction (historical text):

> # Gel point and clot onset detection A working pipeline for detecting when an evolving fluid stops being a liquid, extracted from a research notebook of 100 cells and reduced to what survived contact with real data. **What this does.** Takes a time series of rheological measurements, checks whether the data can support a detection at all, runs only the detectors the data supports, and reports each answer with a verdict on whether it is a measurement or an artefact. **What it deliberately does not do.** It does not always return an answer. Where the data cannot support a detection it says so and returns nothing, because a detector that always 

Referenced file strings (inputs and outputs mixed; inspect configuration):

`app_sheepblood_clot.xlsx`

## Synthetic Clot Event Benchmarks

v1: ten scenario designs; v2: twenty designs with three replicates each. Signal CSVs, manifest, separate ground-truth labels, quality summaries, event scores and result tables. Model-defined events are not clinical labels.

### synthetic_clot_time_benchmark__aa8b221a75.ipynb

Source: `Syn_code_new/Synthetic_Clot_Time_Benchmark.ipynb`

Status: Synthetic; model-defined events. Not rerun for this handover.

Imports: fcwt; json; matplotlib.pyplot; numpy; pandas; pathlib; pywt; ruptures; scipy; scipy.integrate; scipy.ndimage; scipy.special; scipy.stats; sklearn.metrics; time; warnings.

Source introduction (historical text):

> # Synthetic clot-time benchmark ## Goal Generating ten synthetic, instrument-style clotting datasets with known gel times, then comparing time-domain, Fourier, STFT, CWT, DWT, fast-CWT, and change-point methods against those labels. Each scenario has three noise realizations and at least 10,000 rows per realization. Observations and ground-truth labels are saved separately. This is a controlled algorithm benchmark, not clinical data or a validated Haemograph digital twin. The methods all receive the same measurements, preprocessing, windows, and event labels. The analysis does not presume that wavelets will outperform Fourier methods.

Referenced file strings (inputs and outputs mixed; inspect configuration):

`01_observed_signals.png; 02_timing_and_tolerance.png; 03_error_heatmap.png; 04_event_window_curves.png; 05_critical_difference.png; 06_quality_robustness.png; SYN*.csv; ]}.csv; dataset_manifest.csv; feature_dictionary.csv; ground_truth_labels.csv; method_performance_by_run.csv; method_performance_by_scenario.csv; method_performance_summary.csv; reporting_table.csv; signal_quality_summary.csv; statistical_tests.csv; transform_parameter_table.csv; validation_checks.csv; window_event_scores.csv`

### synthetic_clot_time_benchmark_v2__48dbc18380.ipynb

Source: `Syn_code_new/Synthetic_Clot_Time_Benchmark_v2.ipynb`

Status: Synthetic; model-defined events. Not rerun for this handover.

Imports: fcwt; json; matplotlib.pyplot; numpy; pandas; pathlib; pywt; ruptures; scipy; scipy.ndimage; scipy.special; scipy.stats; sklearn.metrics; time; warnings.

Source introduction (historical text):

> # Synthetic clot-time benchmark — Version 2 ## Goal Comparing shared-window time-domain, Fourier, STFT, CWT, DWT, fast-CWT, and change-point methods for detecting known synthetic gel times. This version evaluates twenty distinct signal scenarios with three independent noise realizations per scenario. Each measurement contains at least 10,000 rows, and ground-truth labels remain in a separate output table. Version 2 addresses specific limitations found in the first benchmark: fixed CWT frequencies that did not match the imposed tones, collapsing all CWT scales and DWT levels into one value, and using a signed slope for most methods but an abso

Referenced file strings (inputs and outputs mixed; inspect configuration):

`*.xlsx; 01_observed_signals.png; 02_timing_and_tolerance.png; 03_error_heatmap.png; 04_event_window_curves.png; 05_critical_difference.png; 06_quality_robustness.png; 07_window_length_sensitivity.png; 08_instrument_scale_reference.png; ]}.csv; dataset_manifest.csv; feature_dictionary.csv; ground_truth_labels.csv; instrument_scale_comparison_by_record.csv; instrument_scale_comparison_summary.csv; method_performance_by_run.csv; method_performance_by_scenario.csv; method_performance_summary.csv; reporting_table.csv; signal_quality_summary.csv; statistical_tests.csv; transform_parameter_table.csv; validation_checks.csv; window_event_scores.csv; window_length_sensitivity_by_run.csv; window_length_sensitivity_summary.csv`
