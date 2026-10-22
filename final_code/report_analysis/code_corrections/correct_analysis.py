from pathlib import Path
import json, shutil, itertools
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1] if Path(__file__).parent.name=='code_corrections' else Path('output/latex/Group_24_Blood_Clotting_Updated').resolve()
D=ROOT/'supporting_data'; F=ROOT/'figures'; OUT=D/'corrected_step_138'; OUT.mkdir(exist_ok=True)
nb=json.loads((ROOT/'analysis_sources/Step_UpDown_Analysis.ipynb').read_text())
steps=pd.read_csv(D/'step_138/step_features.csv')
invalid=(~np.isfinite(steps.sigma_stable)) | (steps.n_stable<3) | (steps.sigma_stable.abs()<=.001)
audit=steps.loc[invalid,['step_id','workbook','n_stable','sigma_stable','settling_time']].copy()
audit.rename(columns={'settling_time':'previous_settling_time_s'},inplace=True)
audit['corrected_settling_time_s']=np.nan
audit['reason']='Missing or ineligible late reference stress'
audit.to_csv(OUT/'settling_corrections.csv',index=False)
steps.loc[invalid,'settling_time']=np.nan
steps.to_csv(OUT/'step_features.csv',index=False)
FEATURES=['jump_signed','overshoot','undershoot','init_slope','settling_time','t_peak','t_min','area_log','relax_amp','visc_ratio']
# Re-execute the original paired analysis on the corrected saved feature table.
for i in [34,36,40]: exec(''.join(nb['cells'][i]['source']))
def holm(x):
 x=np.asarray(x,float); order=np.argsort(x); out=np.empty(len(x));out[order]=np.minimum(1,np.maximum.accumulate(x[order]*np.arange(len(x),0,-1)));return out
for name,df in [('result_magnitude',res_mag),('result_direction',res_dir)]:
 df['sign_test_p_holm']=holm(df.sign_test_p)
 if 'wilcoxon_p' in df: df['wilcoxon_p_holm']=holm(df.wilcoxon_p)
 df.to_csv(OUT/(name+'_holm.csv'),index=False)
 df.to_csv(D/(name+'_138_holm.csv'),index=False)
pairs.to_csv(OUT/'matched_pairs.csv',index=False)
mag.to_csv(OUT/'magnitude_family_correlations.csv',index=False)
summary=[]
for direction,g in steps.groupby('direction'):
 for f in FEATURES:
  a=g[f].dropna();summary.append(dict(direction=direction,feature=f,n=len(a),median=a.median(),q25=a.quantile(.25),q75=a.quantile(.75)))
pd.DataFrame(summary).to_csv(OUT/'feature_summary.csv',index=False)
coverage=pd.DataFrame([dict(feature=f,valid=int(A[f].notna().sum()),eligible=len(A),fraction=A[f].notna().mean()) for f in FEATURES])
coverage.to_csv(OUT/'feature_coverage.csv',index=False)
counts={'corrected_records':audit.step_id.tolist(),'settling_valid_all':int(steps.settling_time.notna().sum()),'settling_valid_down':int(steps[steps.direction=='down'].settling_time.notna().sum()),'settling_missing_down_to_01':int(steps[(steps.direction=='down')&np.isclose(steps.rate_to,.1)].settling_time.isna().sum()),'settling_down_summary':pd.DataFrame(summary).query("direction=='down' and feature=='settling_time'").to_dict('records')}
(OUT/'correction_summary.json').write_text(json.dumps(counts,indent=2))
# Store a guarded extraction function for future execution without changing the archived notebook.
src=''.join(nb['cells'][20]['source']); start=src.index('    outside ='); end=src.index('    f["area_log"]',start)
old=src[start:end].replace('f["settling_time"] = tm[0]', 'f["settling_time"] = tm[0] if tm[0] < STABLE_START else np.nan'); guarded='    if not np.isfinite(ss) or e.n_stable < 3 or abs(ss) <= NOISE_PA or len(tm) == 0:\n        f["settling_time"] = np.nan\n    else:\n'+''.join('    '+line+'\n' for line in old.rstrip().splitlines())
src=src[:start]+guarded+src[end:]
(ROOT/'code_corrections/guarded_step_features.py').write_text('# Requires the original step notebook preprocessing and constants.\n# Corrected 23 October 2026: missing late reference cannot imply settling.\n'+src)
# Preserve the original notebook as a source snapshot; provide a clearly labelled guarded copy.
nb['cells'][20]['source']=src.splitlines(keepends=True)
for c in nb['cells']:
 if c['cell_type']=='code': c['outputs']=[];c['execution_count']=None
nb['cells'].insert(0,{'cell_type':'markdown','metadata':{},'source':['# Guarded step analysis source\n','This copy adds a late-reference guard to settling time. Outputs are cleared. The report uses the targeted recalculation in `correct_analysis.py`; model fitting was not rerun. Original exploratory markdown is retained as development history and does not replace the report\'s corrected statistics.']})
(ROOT/'code_corrections/Step_UpDown_Analysis_Guarded.ipynb').write_text(json.dumps(nb,indent=1))
# Small-sample null distribution: permute method assignments independently within each workbook.
scores=pd.read_csv(D/'measured/transform_method_workbook_association_scores.csv')
v=scores[[m+'_absolute_spearman_rho' for m in ['FFT','STFT','CWT','DWT']]].to_numpy()
ranks=stats.rankdata(v,axis=1); N,k=ranks.shape
base=12/(N*k*(k+1)); observed=base*np.sum(ranks.sum(0)**2)-3*N*(k+1)
rng=np.random.default_rng(20261023); B=1000000; extreme=0
perms=np.array(list(itertools.permutations(range(k))))
for _ in range(B//10000):
 idx=perms[rng.integers(len(perms),size=(10000,N))]
 sim=np.take_along_axis(np.broadcast_to(ranks,(10000,N,k)),idx,axis=2)
 qs=base*np.sum(sim.sum(1)**2,axis=1)-3*N*(k+1)
 extreme+=int(np.sum(qs>=observed-1e-10))
p=(extreme+1)/(B+1)
_ci=stats.binomtest(extreme,B).proportion_ci();ci=(_ci.low,_ci.high)
perm={'replicates':B,'seed':20261023,'extreme_count':extreme,'p_plus_one':p,'binomial_interval_95':list(ci),'friedman_tie_corrected':float(stats.friedmanchisquare(*v.T).statistic),'asymptotic_p':float(stats.friedmanchisquare(*v.T).pvalue),'tie_handling':'Average ranks retained; within-row permutation preserves tie correction.'}
(D/'measured/friedman_permutation_check.json').write_text(json.dumps(perm,indent=2))
# Inspect overlap of two retained LAOS descriptors using matched measurement IDs.
laos=pd.read_csv(D/'laos_features.csv');fft=pd.read_csv(D/'transforms/fft_features.csv')
join=laos[['measurement_id','source_file','I3_I1']].merge(fft[['measurement_id','high_to_low_frequency_energy_ratio']],on='measurement_id')
red=[]
for wb,g in join.groupby('source_file'):
 g=g.dropna();red.append(dict(source_file=wb,n=len(g),spearman_rho=stats.spearmanr(g.I3_I1,g.high_to_low_frequency_energy_ratio).statistic))
pd.DataFrame(red).to_csv(D/'retained_laos_feature_overlap.csv',index=False)
# Readable figures from final corrected tables.
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':False})
labels={'jump_signed':'First-reading jump','overshoot':'Overshoot','undershoot':'Undershoot','init_slope':'Initial slope','settling_time':'Settling time','t_peak':'Time of peak','t_min':'Time of minimum','area_log':'Log-time area','relax_amp':'Relaxation amplitude','visc_ratio':'Viscosity ratio'}
units={f:'dimensionless' for f in FEATURES};units.update(init_slope='per decade of time',settling_time='s',t_peak='s',t_min='s',relax_amp='Pa',area_log='normalised stress × ln(time)')
colors={'down':'#237a92','up':'#b56336'}
def save(fig,name):
 fig.savefig(F/name,dpi=250,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(2,5,figsize=(14,6.5),layout='constrained')
for a,f in zip(ax.flat,FEATURES):
 for j,d in enumerate(['down','up']):
  vals=steps.loc[steps.direction==d,f].dropna().to_numpy(); jitter=np.random.default_rng(2).uniform(-.17,.17,len(vals))
  a.scatter(j+jitter,vals,s=9,color=colors[d],alpha=.5);a.plot([j-.22,j+.22],[np.median(vals)]*2,color='black',lw=2)
 a.set(title=labels[f],ylabel=units[f],xticks=[0,1],xticklabels=['Down','Up']);a.tick_params(labelsize=9);a.grid(axis='y',alpha=.15)
save(fig,'step_02d_feature_distributions.png')
fig,axes=plt.subplots(2,3,figsize=(11,6.4),layout='constrained')
for row,d in enumerate(['down','up']):
 for a,f in zip(axes[row],['undershoot','init_slope','settling_time']):
  for (unit,g0),g in A[A.direction==d].groupby(['unit','rate_from']):
   if len(g)<3:continue
   g=g.assign(size=g.log10_ratio.abs()).sort_values('size');a.plot(g['size'],g[f],'o-',ms=3,lw=.8,alpha=.6)
  a.set(title=f'{labels[f]}: step {d}',xlabel='Absolute log₁₀(final / initial rate)',ylabel=units[f]);a.grid(alpha=.15)
save(fig,'step_05_magnitude.png')
order=['undershoot','init_slope','overshoot','settling_time','area_log','t_peak','t_min','jump_signed','relax_amp','visc_ratio']
fig,(a,b)=plt.subplots(1,2,figsize=(11,5.6),layout='constrained',sharey=True)
for i,f in enumerate(order):
 for d,offset in [('down',-.12),('up',.12)]:
  q=res_mag[(res_mag.feature==f)&(res_mag.direction==d)].iloc[0];a.scatter(q.median_rho,i+offset,edgecolors=colors[d],facecolors='none',s=55,marker='o' if d=='down' else 's')
 q=res_dir[res_dir.feature==f].iloc[0];num,den=map(int,q.pairs_up_gt_down.split('/'));b.scatter(num/den,i,c='#247e65' if q.sign_test_p_holm<.05 else '#aaaaaa',s=60);b.text(1.05,i,f'p = {q.sign_test_p_holm:.3f}',va='center',fontsize=9)
a.set(yticks=range(len(order)),yticklabels=[labels[x] for x in order],xlim=(-1.1,1.1),xlabel='Median within-workbook Spearman ρ',title='Step magnitude');a.invert_yaxis();a.axvline(0,color='.7',lw=.8)
a.scatter([],[],edgecolors=colors['down'],facecolors='none',label='Down');a.scatter([],[],edgecolors=colors['up'],facecolors='none',marker='s',label='Up');a.legend(loc='lower right',fontsize=9)
b.set(xlim=(-.05,1.7),xticks=[0,.5,1],xlabel='Fraction of pairs with up > down',title='Matched direction');b.axvline(.5,color='.6',ls='--',lw=.8)
save(fig,'step_05b_evidence_summary.png')
fig,a=plt.subplots(figsize=(11,5.4),layout='constrained');a.set_xlim(0,4);a.set_ylim(len(order)-.5,-1)
for i,f in enumerate(order):
 c=coverage[coverage.feature==f].iloc[0];a.text(.05,i,labels[f],va='center');a.text(1.55,i,f'{c.valid}/{c.eligible} ({100*c.fraction:.1f}%)',ha='center',va='center')
 for x,d in [(2.45,'down'),(3.05,'up')]:
  pval=res_mag[(res_mag.feature==f)&(res_mag.direction==d)].sign_test_p_holm.iloc[0];a.text(x,i,f'{pval:.3f}',ha='center',va='center',color='#247e65' if pval<.05 else '#555555')
 pval=res_dir[res_dir.feature==f].sign_test_p_holm.iloc[0];a.text(3.7,i,f'{pval:.3f}',ha='center',va='center',fontweight='bold' if pval<.05 else 'normal',color='#247e65' if pval<.05 else '#555555');a.axhline(i+.5,color='#dddddd',lw=.6)
for x,label in [(.05,'Feature'),(1.55,'Finite / eligible'),(2.45,'Size: down'),(3.05,'Size: up'),(3.7,'Direction')]:a.text(x,-.7,label,ha='left' if x<1 else 'center',weight='bold')
a.axis('off');save(fig,'step_09_metric_reliability.png')
# Replot matched pairs with formal labels.
p=pairs.sort_values('down_undershoot');fig,a=plt.subplots(figsize=(8,6),layout='constrained')
y=np.arange(len(p))
a.hlines(y,p.up_undershoot,p.down_undershoot,color='.75',lw=1)
a.scatter(p.up_undershoot,y,label='Step-up',color=colors['up']);a.scatter(p.down_undershoot,y,label='Step-down',color=colors['down'])
a.set(yticks=y,yticklabels=p['sample']+' · '+p['pair'],xlabel='Undershoot / late reference stress',ylabel='Workbook and matched rates (s⁻¹)');a.tick_params(axis='y',labelsize=9);a.legend(frameon=False);save(fig,'step_matched_pairs.png')
print('CORRECTION',counts);print('PERMUTATION',perm);print('RETAINED OVERLAP',pd.DataFrame(red).spearman_rho.median())
