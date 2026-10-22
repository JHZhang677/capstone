# Requires the original step notebook preprocessing and constants.
# Corrected 23 October 2026: missing late reference cannot imply settling.
def features(b, e):
    d = b["an"]; t = d.time.values; s = d.stress.values
    fc = flow_curve_for(b["workbook"], b["storage_h"])
    ss = e.sigma_stable
    m = t >= e.t_rate_settle
    tm, sm = t[m], s[m]
    pre = s[t < 0.5 * e.t_step] if e.has_pre_step else np.array([])
    f = dict(step_id=b["step_id"])
    f["sigma_pre"] = np.median(pre) if len(pre) else np.nan
    f["sigma_pre_fc"] = flow_stress(fc, e.rate_from)
    f["sigma_final_fc"] = flow_stress(fc, e.rate_to)
    f["sigma_imm"] = sm[0]
    i_pk, i_mn = np.argmax(sm), np.argmin(sm)
    f.update(sigma_peak=sm[i_pk], t_peak=tm[i_pk], sigma_min=sm[i_mn], t_min=tm[i_mn])
    denom = abs(ss) if abs(ss) > NOISE_PA else np.nan
    f["overshoot"] = (sm[i_pk] - ss) / denom
    f["undershoot"] = (ss - sm[i_mn]) / denom
    f["jump_signed"] = (sm[0] - ss) / denom
    f["relax_amp"] = sm[0] - ss
    early = (tm <= 1.0)
    f["init_slope"] = (np.polyfit(np.log10(tm[early]), sm[early] / denom, 1)[0]
                       if early.sum() >= 3 and np.isfinite(denom) else np.nan)
    if not np.isfinite(ss) or e.n_stable < 3 or abs(ss) <= NOISE_PA or len(tm) == 0:
        f["settling_time"] = np.nan
    else:
        outside = np.where(np.abs(sm - ss) > max(SETTLE_BAND * abs(ss), NOISE_PA))[0]
        if len(outside) == 0:
            f["settling_time"] = tm[0] if tm[0] < STABLE_START else np.nan
        elif outside[-1] + 1 < len(tm) and tm[outside[-1] + 1] < STABLE_START:
            f["settling_time"] = tm[outside[-1] + 1]
        else:
            f["settling_time"] = np.nan
    f["area_log"] = trapezoid((sm - ss) / denom, np.log(tm))
    f["plateau_vs_fc"] = ss / f["sigma_final_fc"]
    f["baseline_vs_fc"] = f["sigma_pre"] / f["sigma_pre_fc"]
    f["visc_ratio"] = ((ss / e.rate_to) / (f["sigma_pre"] / e.rate_from)
                       if len(pre) and abs(f["sigma_pre"]) >= 3 * NOISE_PA else np.nan)   # baseline must exceed noise
    return f

evs = ev.set_index("step_id")
feat = pd.DataFrame([features(b, evs.loc[b["step_id"]]) for b in blocks])
steps = ev.merge(feat, on="step_id")
FEATURES = ["jump_signed", "overshoot", "undershoot", "init_slope", "settling_time", "t_peak", "t_min",
            "area_log", "relax_amp", "visc_ratio"]
steps.to_csv(OUT / "step_features.csv", index=False)
steps[["step_id", "sample", "label", "direction", "sigma_pre", "sigma_imm", "sigma_stable"] + FEATURES].head(10).round(4)