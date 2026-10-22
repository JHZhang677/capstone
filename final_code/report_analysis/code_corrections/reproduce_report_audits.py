from pathlib import Path
import ast, json, shutil, argparse
import numpy as numpy
import pandas as pandas
from scipy import signal as scipy_signal
from scipy.stats import spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
argument_parser = argparse.ArgumentParser(description = 'Reproducing targeted report audits without running the full notebooks.')
argument_parser.add_argument('--project-root', type = Path, required = True)
arguments = argument_parser.parse_args()
project_directory = arguments.project_root.resolve()
report_directory = Path(__file__).resolve().parent.parent
evidence_directory = report_directory / 'supporting_data'
evidence_directory.mkdir(exist_ok = True)
part1_directory = project_directory / '03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data'
part2_directory = next((project_directory / '03_Team_Contributions/Part2_Conventional_LAOS/Extracted_Contents').iterdir())
step_directory = part1_directory / 'step_analysis_outputs_main'

def adjust_holm(probability_values):
    probabilities = numpy.asarray(probability_values, dtype = float)
    order = numpy.argsort(probabilities)
    adjusted = numpy.empty(len(probabilities))
    adjusted[order] = numpy.minimum(1, numpy.maximum.accumulate(probabilities[order] * numpy.arange(len(probabilities), 0, -1)))
    return adjusted

for result_name in ['result_magnitude', 'result_direction', 'result_transient_vs_stable']:
    result_dataframe = pandas.read_csv(step_directory / (result_name + '.csv'))
    result_dataframe['sign_test_p_holm'] = adjust_holm(result_dataframe['sign_test_p'])
    if 'wilcoxon_p' in result_dataframe:
        result_dataframe['wilcoxon_p_holm'] = adjust_holm(result_dataframe['wilcoxon_p'])
    result_dataframe.to_csv(evidence_directory / (result_name + '_138_holm.csv'), index = False)
    print(result_name, result_dataframe.to_string(index = False))

# Recomputing the retained Fourier ratio using only the saved notebook functions
notebook = json.loads((report_directory / 'code_corrections/00_feature_integration_Final.ipynb').read_text())
function_source = ''.join(notebook['cells'][94]['source'])
syntax_tree = ast.parse(function_source)
required_names = {'prepare_uniform_transform_signal', 'calculate_normalised_spectral_entropy', 'calculate_band_energy', 'calculate_fft_features'}
selected_definitions = [node for node in syntax_tree.body if isinstance(node, ast.FunctionDef) and node.name in required_names]
TRANSFORM_MINIMUM_WINDOW_SAMPLE_COUNT = 16
exec(compile(ast.Module(body = selected_definitions, type_ignores = []), '<saved notebook functions>', 'exec'))
signal_dataframe = pandas.read_csv(part1_directory / 'standardized_signals.csv.gz', usecols = ['measurement_id', 'time_s', 'stress_pa'])
feature_dataframe = pandas.read_csv(part2_directory / 'laos_features.csv')
signal_groups = dict(tuple(signal_dataframe.groupby('measurement_id')))
sensitivity_rows = []
for measurement_row in feature_dataframe.itertuples(index = False):
    frequency_hz = float(measurement_row.omega_label_rad_s) / (2 * numpy.pi)
    selected_signal = signal_groups[measurement_row.measurement_id]
    end_seconds = selected_signal['time_s'].max()
    selected_signal = selected_signal.loc[selected_signal['time_s'].between(end_seconds - 2 / frequency_hz, end_seconds)]
    sensitivity_record = {'measurement_id': measurement_row.measurement_id, 'source_file': measurement_row.source_file}
    for sampling_frequency_hz in [25.0, 50.0]:
        prepared_signal = prepare_uniform_transform_signal(selected_signal, sampling_frequency_hz, True)
        features, diagnostics = calculate_fft_features(prepared_signal['normalised_stress_values'], sampling_frequency_hz, fundamental_frequency_hz = frequency_hz, high_frequency_split_hz = 3 * frequency_hz, effective_nyquist_hz = prepared_signal['effective_nyquist_from_p90_hz'])
        sensitivity_record[f'ratio_{int(sampling_frequency_hz)}_hz'] = features['high_to_low_frequency_energy_ratio']
    sensitivity_rows.append(sensitivity_record)
sensitivity_dataframe = pandas.DataFrame(sensitivity_rows)
sensitivity_dataframe['relative_difference_percent_vs_50_hz'] = 100 * abs(sensitivity_dataframe['ratio_25_hz'] - sensitivity_dataframe['ratio_50_hz']) / abs(sensitivity_dataframe['ratio_50_hz'])
sensitivity_dataframe.to_csv(evidence_directory / 'fft_ratio_sampling_25_50_report_audit.csv', index = False)
saved_fft = pandas.read_csv(project_directory / '01_Active_Blood_Project/04_Results/Fourier_Wavelet_Feature_Development/fft_features.csv')
comparison = sensitivity_dataframe.merge(saved_fft[['measurement_id','high_to_low_frequency_energy_ratio']], on = 'measurement_id')
summary = {'records': len(sensitivity_dataframe), 'spearman_rho': float(spearmanr(sensitivity_dataframe['ratio_25_hz'], sensitivity_dataframe['ratio_50_hz']).statistic), 'median_relative_difference_percent': float(sensitivity_dataframe['relative_difference_percent_vs_50_hz'].median()), 'maximum_difference_from_saved_50_hz': float(abs(comparison['ratio_50_hz'] - comparison['high_to_low_frequency_energy_ratio']).max())}
(evidence_directory / 'fft_ratio_sampling_summary.json').write_text(json.dumps(summary, indent = 2))
print('FFT ratio audit:', summary)

# Redrawing the conventional plots with explicit workbook aggregation and IQR bars
pyplot.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
for feature_name, filename, axis_label in [('G_double_prime_Pa','laos_gdouble_vs_strain.png',"Loss modulus G″ (Pa)"),('I3_I1','laos_i3i1_vs_strain.png','Third / first harmonic amplitude')]:
    grouped = feature_dataframe.groupby(['source_file','omega_label_rad_s','strain_amplitude_label_fraction'])[feature_name].median().reset_index()
    figure, axes = pyplot.subplots(figsize = (6.2, 4.1), layout = 'constrained')
    for angular_frequency, colour in zip([0.5,1,5], ['#147d92','#b75e35','#635c9d']):
        subset = grouped.loc[grouped['omega_label_rad_s'].eq(angular_frequency)]
        aggregated = subset.groupby('strain_amplitude_label_fraction')[feature_name].agg(['median',lambda values: values.quantile(.25),lambda values: values.quantile(.75)])
        aggregated.columns = ['median','q25','q75']
        axes.errorbar(aggregated.index,aggregated['median'],yerr = [aggregated['median'] - aggregated['q25'],aggregated['q75'] - aggregated['median']],fmt = 'o-',capsize = 3,label = f'{angular_frequency:g} rad/s',color = colour)
    axes.set_xscale('log')
    axes.set_xlabel('Strain amplitude (fraction)')
    axes.set_ylabel(axis_label)
    axes.grid(alpha = .16)
    axes.legend(frameon = False, fontsize = 9)
    figure.savefig(report_directory / 'figures' / filename, dpi = 230)
    pyplot.close(figure)

# Copying the exact saved tables behind the report without copying raw blood recordings
source_directories = {
    'measured': project_directory / '01_Active_Blood_Project/04_Results/Final_Real_Data_Analysis',
    'transforms': project_directory / '01_Active_Blood_Project/04_Results/Fourier_Wavelet_Feature_Development',
    'synthetic': project_directory / 'Syn_code_new/v2_outputs',
}
for collection_name, collection_directory in source_directories.items():
    destination_directory = evidence_directory / collection_name
    destination_directory.mkdir(exist_ok = True)
    for table_path in collection_directory.glob('*.csv'):
        if table_path.stat().st_size < 3000000 and table_path.name not in ['instrument_condition_match_audit.csv','instrument_condition_match_summary.csv','reviewed_laos_metric_status.csv']:
            shutil.copy2(table_path, destination_directory / table_path.name)
for table_name in ['instrument_crossvalidation.csv','instrument_crossvalidation_summary.csv','workbook_level_strain_correlations.csv','sensitivity_summary.csv','laos_features.csv']:
    shutil.copy2(part2_directory / table_name, evidence_directory / table_name)
shutil.copy2(part1_directory / 'processing_summary.json', evidence_directory / 'processing_summary.json')
