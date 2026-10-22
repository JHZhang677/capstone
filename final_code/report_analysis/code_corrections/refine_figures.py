from pathlib import Path
import pandas as pd,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1];D=R/'supporting_data';F=R/'figures'
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
steps=pd.read_csv(D/'corrected_step_138/step_features.csv')
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--project-root',type=Path,required=True);args=parser.parse_args()
base=args.project_root/'03_Team_Contributions/Part1_Data_Processing/Extracted_Contents/main-data'
signals=pd.read_csv(base/'standardized_signals.csv.gz',usecols=['measurement_id','time_s','stress_pa'])
selected=[]
for dr,g0,g1 in [('up',.25,5),('down',5,.1)]:
 q=steps[(steps['sample']=='JUN18')&np.isclose(steps.rate_from,g0)&np.isclose(steps.rate_to,g1)].iloc[0];selected.append(q)
fig,axs=plt.subplots(1,2,figsize=(8.2,4.3),layout='constrained')
for a,q in zip(axs,selected):
 d=signals[signals.measurement_id==q.step_id].sort_values('time_s');ss=q.sigma_stable;band=max(.1*abs(ss),.001)
 a.axvspan(d.time_s.min(),q.t_rate_settle,color='#dddddd',label='Instrument exclusion')
 a.axhspan(1-band/ss,1+band/ss,color='#b8dec7',alpha=.65,label='Settling band')
 a.plot(d.time_s,d.stress_pa/ss,'o-',color='#237a92',ms=3,lw=1)
 a.axhline(1,color='#247e65',ls='--',lw=1)
 a.axvline(q.settling_time,color='#a65328',ls=':',lw=1.5)
 a.text(.97,.96,f'Settling: {q.settling_time:.2f} s',ha='right',va='top',transform=a.transAxes,fontsize=10)
 a.set(xscale='log',xlabel='Elapsed time (s)',ylabel='Stress / late reference',title=f'{q.rate_from:g} → {q.rate_to:g} s⁻¹')
 a.set_xlim(.03,70)
axs[0].legend(fontsize=8,loc='lower right');fig.savefig(F/'annotated_step_responses.png',dpi=250);plt.close(fig)
pd.DataFrame(selected).to_csv(D/'corrected_step_138/illustrated_jun18_records.csv',index=False)
# Readable two-column feature distributions.
features=['jump_signed','overshoot','undershoot','init_slope','settling_time','t_peak','t_min','area_log','relax_amp','visc_ratio']
labels=['First-reading jump','Overshoot','Undershoot','Initial slope','Settling time','Time of peak','Time of minimum','Log-time area','Relaxation amplitude','Viscosity ratio']
units=['dimensionless','dimensionless','dimensionless','per decade','s','s','s','dimensionless','Pa','dimensionless']
fig,axs=plt.subplots(5,2,figsize=(8.1,10),layout='constrained')
for a,f,l,u in zip(axs.flat,features,labels,units):
 for j,dr,color in [(0,'down','#237a92'),(1,'up','#b56336')]:
  v=steps.loc[steps.direction==dr,f].dropna();jitter=np.random.default_rng(2).uniform(-.18,.18,len(v))
  a.scatter(j+jitter,v,s=7,alpha=.5,color=color);a.plot([j-.22,j+.22],[v.median()]*2,color='black',lw=2)
 a.set(title=l,ylabel=u,xticks=[0,1],xticklabels=['Down','Up']);a.tick_params(labelsize=9);a.grid(axis='y',alpha=.15)
fig.savefig(F/'step_02d_feature_distributions.png',dpi=250);plt.close(fig)
# Larger type in the two half-page LAOS panels.
laos=pd.read_csv(D/'laos_features.csv')
plt.rcParams.update({'font.size':16})
for f,name,yl in [('G_double_prime_Pa','laos_gdouble_vs_strain.png','Loss modulus G″ (Pa)'),('I3_I1','laos_i3i1_vs_strain.png','Third / first harmonic amplitude')]:
 g=laos.groupby(['source_file','omega_label_rad_s','strain_amplitude_label_fraction'])[f].median().reset_index();fig,a=plt.subplots(figsize=(6.2,4.5),layout='constrained')
 for w,c in zip([.5,1,5],['#147d92','#b75e35','#635c9d']):
  q=g[g.omega_label_rad_s==w].groupby('strain_amplitude_label_fraction')[f].agg(['median',lambda x:x.quantile(.25),lambda x:x.quantile(.75)]);q.columns=['m','l','u']
  a.errorbar(q.index,q.m,yerr=[q.m-q.l,q.u-q.m],fmt='o-',capsize=3,label=f'{w:g} rad/s',color=c)
 a.set(xscale='log',xlabel='Strain amplitude (fraction)',ylabel=yl);a.legend(fontsize=12,frameon=False);a.grid(alpha=.15);fig.savefig(F/name,dpi=250);plt.close(fig)
print(pd.DataFrame(selected)[['step_id','overshoot','undershoot','settling_time','t_peak','t_min']].to_string(index=False))
