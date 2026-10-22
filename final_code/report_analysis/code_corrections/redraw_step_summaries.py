from pathlib import Path
import shutil
import pandas as pandas
import numpy as numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
report_directory = Path(__file__).resolve().parent.parent
source = (report_directory / 'main.tex').read_text()
evidence_directory = report_directory / 'supporting_data'
feature_labels = {'init_slope':'Initial slope','undershoot':'Undershoot','visc_ratio':'Viscosity ratio','overshoot':'Overshoot','area_log':'Log-time area','t_min':'Time of minimum','settling_time':'Settling time','t_peak':'Time of peak','relax_amp':'Relaxation amplitude','jump_signed':'First-reading jump'}
magnitude = pandas.read_csv(evidence_directory / 'result_magnitude_138_holm.csv')
direction = pandas.read_csv(evidence_directory / 'result_direction_138_holm.csv')

# Redrawing exploratory evidence graphics with the final Holm decision rule
pyplot.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
feature_order = list(feature_labels)
figure, axes = pyplot.subplots(1,2,figsize=(11.5,4.8),layout='constrained',gridspec_kw={'width_ratios':[1.2,1]})
for direction_name, colour, offset in [('down','#236a9d',-.13),('up','#c17230',.13)]:
    for index, feature_name in enumerate(feature_order):
        values=magnitude.loc[magnitude['direction'].eq(direction_name)&magnitude['feature'].eq(feature_name)].iloc[0]
        axes[0].scatter(values.median_rho,index+offset,color=colour,s=40,facecolors='none',label=direction_name.title() if index==0 else None)
axes[0].set_yticks(range(len(feature_order)),[feature_labels[name] for name in feature_order])
axes[0].invert_yaxis()
axes[0].set_xlim(-1.12,1.12)
axes[0].axvline(0,color='#999999',lw=.7)
axes[0].set_xlabel('Median within-family Spearman correlation')
axes[0].set_title('Step magnitude: no test survives Holm correction',fontsize=11)
axes[0].legend(frameon=False,loc='lower left')
for index,feature_name in enumerate(feature_order):
    values=direction.loc[direction['feature'].eq(feature_name)].iloc[0]
    successes,total=map(int,values.pairs_up_gt_down.split('/'))
    supported=values.sign_test_p_holm<.05
    axes[1].scatter(successes/total,index,color='#227b6a' if supported else '#aab3b8',s=45,marker='o')
axes[1].set_yticks(range(len(feature_order)),['']*len(feature_order))
axes[1].invert_yaxis()
axes[1].axvline(.5,color='#999999',lw=.7,ls='--')
axes[1].set_xlim(-.08,1.08)
axes[1].set_xlabel('Fraction of matched pairs with up > down')
axes[1].set_title('Direction: green = Holm sign-test p < 0.05',fontsize=11)
for axis in axes: axis.grid(axis='x',alpha=.15)
figure.savefig(report_directory/'figures/step_05b_evidence_summary.png',dpi=220)
pyplot.close(figure)

reliability=pandas.read_csv(evidence_directory/'step_138/metric_reliability.csv')
figure,axes=pyplot.subplots(1,2,figsize=(10.5,4.8),layout='constrained',gridspec_kw={'width_ratios':[1.3,1]})
for index,feature_name in enumerate(feature_order):
    coverage=float(reliability.loc[reliability.feature.eq(feature_name),'computable'].iloc[0])
    axes[0].barh(index,coverage,color='#8ab4c3',height=.65)
    axes[0].text(coverage+.025,index,f'{coverage:.0%}',va='center',fontsize=9)
axes[0].set_yticks(range(len(feature_order)),[feature_labels[name] for name in feature_order])
axes[0].invert_yaxis()
axes[0].set_xlim(0,1.18)
axes[0].set_xlabel('Fraction with a computable value (saved, rounded)')
axes[0].set_title('Coverage is different from statistical evidence',fontsize=11)
status_matrix=numpy.zeros((len(feature_order),3),dtype=int)
for index,feature_name in enumerate(feature_order):
    for column,direction_name in enumerate(['down','up']):
        status_matrix[index,column]=int(magnitude.loc[magnitude.feature.eq(feature_name)&magnitude.direction.eq(direction_name),'sign_test_p_holm'].iloc[0]<.05)
    status_matrix[index,2]=int(direction.loc[direction.feature.eq(feature_name),'sign_test_p_holm'].iloc[0]<.05)
from matplotlib.colors import ListedColormap
axes[1].imshow(status_matrix,cmap=ListedColormap(['#e9edf0','#267c69']),vmin=0,vmax=1,aspect='auto')
axes[1].set_xticks([0,1,2],['Size: down','Size: up','Direction'],fontsize=9)
axes[1].set_yticks([])
axes[1].set_title('Holm-adjusted sign tests',fontsize=11)
for index in range(len(feature_order)):
    for column in range(3):
        axes[1].text(column,index,'< 0.05' if status_matrix[index,column] else '≥ 0.05',ha='center',va='center',color='white' if status_matrix[index,column] else '#59646f',fontsize=9)
figure.savefig(report_directory/'figures/step_09_metric_reliability.png',dpi=220)
pyplot.close(figure)
