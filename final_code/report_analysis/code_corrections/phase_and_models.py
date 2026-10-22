from pathlib import Path
import pandas as pd,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1];D=R/'supporting_data';F=R/'figures'
steps=pd.read_csv(D/'corrected_step_138/step_features.csv');a=steps[steps.qc_rate!='MISMATCH with label']
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--project-root',type=Path,required=True);args=parser.parse_args()
base=args.project_root/'03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data'
sig=pd.read_csv(base/'standardized_signals.csv.gz',usecols=['measurement_id','time_s','stress_pa']);sig=sig.rename(columns={'time_s':'time','stress_pa':'stress'})
sig=sig[np.isfinite(sig.time)&(sig.time>0)&np.isfinite(sig.stress)]
groups=dict(tuple(sig.groupby('measurement_id')));ref=groups[steps.iloc[0].step_id].time.to_numpy();edges=np.r_[ref[0]/1.2,np.sqrt(ref[1:]*ref[:-1]),ref[-1]*1.2]
rows=[]
for q in a.itertuples():
 d=groups[q.step_id].copy()
 if q.high_res:
  d=d.assign(bin=np.digitize(d.time,edges)-1).groupby('bin').mean(numeric_only=True);d=d[d.index.isin(range(len(ref)))]
 row={'step_id':q.step_id,'sample':q.sample}
 for prefix,lo,hi in [('T',q.t_rate_settle,2),('S',30,np.inf)]:
  w=d[d.time.between(lo,hi)];ss=q.sigma_stable
  if len(w)<3 or not np.isfinite(ss) or abs(ss)<.001: vals=[np.nan]*3
  else:
   y=w.stress/ss;vals=[abs(np.polyfit(np.log10(w.time),y,1)[0]),np.mean(abs(y-1)),np.std(y)/abs(np.mean(y))]
  row.update({prefix+'_'+k:v for k,v in zip(['slope','deviation','cv'],vals)})
 rows.append(row)
ph=pd.DataFrame(rows);ph.to_csv(D/'corrected_step_138/primary_window_descriptors.csv',index=False)
assert ((ph.T_deviation>ph.S_deviation)&ph.T_deviation.notna()).sum()==129
assert ph[['T_deviation','S_deviation']].dropna().shape[0]==130
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,3,figsize=(8.3,3.8),layout='constrained')
for ax,k,l in zip(axs,['slope','deviation','cv'],['Absolute slope','Absolute deviation','Coefficient of variation']):
 ax.boxplot([ph['T_'+k].dropna(),ph['S_'+k].dropna()],tick_labels=['Early','Late'],showfliers=False)
 for _,v in ph.iterrows():ax.plot([1,2],[v['T_'+k],v['S_'+k]],color='.6',alpha=.22,lw=.7)
 ax.set(yscale='log',title=l,ylabel='Per decade' if k=='slope' else 'Dimensionless');ax.tick_params(labelsize=10)
fig.savefig(F/'step_07_transient_vs_stable.png',dpi=250,bbox_inches='tight');plt.close(fig)
models=pd.read_csv(D/'step_138/relaxation_fits.csv');print(models.columns.tolist())
# Preserve the reported conditional range and label it explicitly.
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.3,5.2),layout='constrained',sharey=True)
y=np.arange(len(models));labels=models['sample']+' / '+models.storage_h.astype(int).astype(str)+' h'
ax.axvspan(1.13-2*.24,1.13+2*.24,color='#d6ebde',alpha=.8)
ax.hlines(y,models.tau_lambda_lo,models.tau_lambda_hi,color='#4b8ca0');ax.scatter(models.tau_lambda,y,color='#237a92',s=23)
ax.set(yticks=y,yticklabels=labels,xlabel='Structural time τλ (s)',title='Conditional cost ranges');ax.invert_yaxis();ax.tick_params(axis='y',labelsize=9)
bx.axvline(.29,color='.5',ls='--');bx.axvspan(.05,.25,color='#d6ebde',alpha=.8);bx.scatter(models.G,y,color='#237a92',s=23)
bx.set(xlabel='Elastic modulus G (Pa)',title='Fitted elastic modulus');fig.savefig(F/'step_03_tau_lambda_vs_literature.png',dpi=250,bbox_inches='tight');plt.close(fig)
# Storage model panel with readable parameter names.
m=models[models['sample']=='DEC17'].sort_values('storage_h')
fig,axs=plt.subplots(1,3,figsize=(8.3,3.5),layout='constrained')
for ax,f,l in zip(axs,['tau_lambda','G','eta_ST'],['Structural time (s)','Elastic modulus (Pa)','Structural viscosity (Pa s)']):
 ax.plot(m.storage_h,m[f],'o-',color='#237a92');ax.set(xlabel='Storage time (h)',ylabel=l,xticks=[0,12,24]);ax.grid(alpha=.2)
axs[0].axhspan(.65,1.61,color='#d6ebde',zorder=-1);axs[1].axhline(.29,color='.6',ls='--');fig.savefig(F/'step_08b_dec17_model_parameters.png',dpi=250,bbox_inches='tight');plt.close(fig)
print('Primary phase contrast reproduced:129/130')
# Baseline direction rule: show only the prespecified rule used in the text.
pairs=pd.read_csv(D/'corrected_step_138/matched_pairs.csv');ids=set(pairs.up_id)|set(pairs.down_id);paired=a[a.step_id.isin(ids)]
def accuracy(x):
 q=x[x.jump_signed.notna()];return ((q.jump_signed>0)==(q.direction=='up')).mean()
rng=np.random.default_rng(0);wbs=paired['sample'].unique();boot=[accuracy(pd.concat([paired[paired['sample']==wb] for wb in rng.choice(wbs,len(wbs))])) for _ in range(2000)]
lo,hi=np.quantile(boot,[.025,.975]);v=accuracy(paired)
fig,ax=plt.subplots(figsize=(8.3,2),layout='constrained');ax.errorbar(v,0,xerr=[[v-lo],[hi-v]],fmt='o',capsize=6,color='#237a92',markersize=8)
ax.axvline(.5,color='.5',ls='--');ax.set(xlim=(.3,.8),ylim=(-.6,.6),yticks=[0],yticklabels=['First-reading rule'],xlabel='Correct classifications / eligible paired records')
ax.text(v,.25,f'24/44 = {100*v:.1f}%',ha='center');fig.savefig(F/'step_06b_direction_rules.png',dpi=250,bbox_inches='tight');plt.close(fig)
# Descriptive storage curves; use fitted parameters only for effective time.
sub=a[a['sample']=='DEC17'].copy();sub=sub.merge(m[['storage_h','k_lambda','tr1','tr2']],on='storage_h')
sub['tau_eff']=1/(sub.k_lambda*(sub.tr1*sub.rate_to+sub.tr2*np.sqrt(sub.rate_to)+1))
fig,axs=plt.subplots(1,3,figsize=(8.3,4),layout='constrained')
for ax,f,label in zip(axs,['sigma_stable','jump_signed','tau_eff'],['Late reference (Pa)','First-reading jump','Effective model time (s)']):
 for (g0,g1),g in sub.groupby(['rate_from','rate_to']):
  if g.storage_h.nunique()!=3:continue
  g=g.groupby('storage_h')[f].mean().reset_index();ax.plot(g.storage_h,g[f],'o-',ms=3,label=f'{g0:g} → {g1:g}')
 ax.set(xlabel='Storage time (h)',ylabel=label,xticks=[0,12,24]);ax.grid(alpha=.15)
 if f=='sigma_stable':ax.set_yscale('log')
axs[0].legend(title='Rates (s⁻¹)',fontsize=7,title_fontsize=8,frameon=False);fig.savefig(F/'step_08_dec17_storage.png',dpi=250,bbox_inches='tight');plt.close(fig)
