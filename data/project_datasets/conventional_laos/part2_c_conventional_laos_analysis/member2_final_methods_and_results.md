# Member 2 — Conventional LAOS Methods and Results

## Methods

### Dataset and analysis freeze
Conventional LAOS analysis used the common Member 1 standardized signal table and measurement index. The earlier exploratory inventory reported 184 usable LAOS blocks, but this was not the final analysis-ready count. The Member 1 standardized index contains 200 LAOS-classified blocks. For the final Member 2 freeze, 17 LAOS blocks from **9MAY19** were removed because the supplied dataset review identifies them as duplicates of **27FEB19**; one **NOV18** trace (ω = 1 rad/s, γ₀ = 100) was removed because Member 1 flags it as an exact duplicate of the γ₀ = 50 trace; and one **JUN18** block was removed because it has no frequency or strain-amplitude label. This leaves **181 analysis-ready LAOS measurements from 10 source workbooks**. The raw JUN18 workbook also contains an ω = 1, γ₀ = 10 block whose middle signal lacks the expected Stress header; because this block was not standardized by the shared pipeline, it was not manually reintroduced in Member 2. This preserves a common dataset across members. The 181-measurement freeze is therefore used throughout this section.

### Conventional LAOS feature extraction
For each measurement, strain was represented as γ(t)=γ₀ sin(ωt). Following the Fourier representation used for blood LAOS by Armstrong et al. (2021), stress over the analysis window was represented by first-to-fifth sine/cosine harmonic terms. The strain fundamental was first fitted to establish phase and measured strain amplitude. The in-phase and quadrature first-harmonic stress components were divided by the measured strain fundamental to obtain **G′** and **G″**, and phase angle was calculated as δ = atan2(G″,G′). Harmonic intensity ratios were calculated as **I3/I1** and **I5/I1**, where each harmonic intensity is the magnitude of its sine/cosine pair. THD was calculated from harmonics 2–5 relative to I1. A normalized stress–strain Lissajous loop area was also calculated from the final cycle.

The primary estimate used the **last two nominal oscillation periods** for every measurement. This gives a common rule at ω = 0.5, 1 and 5 rad/s while avoiding the very short-run problem at ω = 0.5 rad/s, where only about three cycles are available. No window-wise z-score normalization was used because stress amplitude is part of the strain-amplitude response. An intercept was included in the harmonic regression; linear detrending was retained only as a sensitivity analysis because it materially changes some higher-harmonic ratios.

### Implementation and instrument cross-validation
Implementation was first checked with synthetic signals having known G′, G″, I3/I1 and I5/I1; all target values were recovered to numerical precision. A second validation used the rheometer-generated values stored in the Armstrong SS/SAOS summary sheets. Frequency-sweep rows were matched to the corresponding raw LAOS condition by workbook, storage condition (where applicable), angular frequency, and strain amplitude. This produced **26 matched pairs for G′/G″** and **12 matched pairs with third-harmonic components**. Instrument third-harmonic values were converted to I3/I1 using the same magnitude-ratio definition reported by Armstrong et al. (2021) and Pincot et al. (2023).

### Strain-amplitude comparison and uncertainty
The independent analysis unit was the **source workbook**, not individual cycles. For workbooks containing repeated conditions (notably DEC17 at 0/12/24 h), repeated values at the same strain amplitude and frequency were first collapsed by their median. Within each workbook and frequency, Spearman correlation was then calculated between log10 strain amplitude and each conventional feature. The final result for each frequency is the median workbook-level Spearman coefficient with a 95% bootstrap interval. A two-sided sign test summarises whether the direction of the within-workbook relationship is consistent. Because the number of independent workbooks is small, these results are treated as exploratory.

## Results

### Instrument agreement
The direct rheometer cross-validation supported the harmonic implementation. **G″ showed the closest agreement**, with median absolute percentage error (MdAPE) of **1.6%** and Pearson r = **0.999** across 26 matched points. **I3/I1** also agreed closely (MdAPE **6.5%**, Pearson r = **0.987**, n = 12). **G′** retained strong linear agreement (Pearson r = **0.987**) but had a larger MdAPE of **19.4%** because G′ becomes very small at high strain and relative error is therefore amplified. The agreement of G″ and I3/I1 provides the strongest direct check that the phase convention and harmonic-amplitude calculation are consistent with the instrument output.

### Strain-dependent conventional response
The first-harmonic measures showed the most consistent strain dependence. **G′ and G″ decreased with increasing strain amplitude at every tested frequency**, with median workbook-level ρ = -1.00/-1.00 at 0.5 rad/s, -1.00/-1.00 at 1 rad/s, and -0.94/-1.00 at 5 rad/s. **Phase angle increased** with strain amplitude (median ρ = 1.00, 1.00, and 0.94), indicating an increasingly loss-dominated response over the tested strain range. Normalized Lissajous area also increased consistently, with median ρ = 1.00, 0.94, and 0.60.

Higher-harmonic metrics were more frequency-dependent. **I3/I1 increased modestly at 0.5 rad/s (ρ = 0.10) and more clearly at 1 rad/s (ρ = 0.49), but decreased at 5 rad/s (ρ = -0.37)**. I5/I1 showed strong positive monotonic relationships at 0.5 and 1 rad/s (ρ = 0.90 and 0.94) but was inconsistent at 5 rad/s (ρ = 0.37; bootstrap interval includes zero). THD followed a similar frequency-dependent pattern. These results mean that the higher-harmonic response should not be summarised as a single universal “increases with strain” rule; the direction depends on oscillation frequency.

### Reliability and interpretation
The conventional first-harmonic metrics **G′, G″ and phase angle** are retained as valid baseline features. I3/I1 is retained as **valid with caution** because it has direct instrument support but changes materially when linear detrending is imposed. I5/I1 and THD are retained as **exploratory/unstable** rather than primary features because no matching fifth-harmonic instrument summary was available and both are more preprocessing-sensitive. Normalized Lissajous area is retained as a robust descriptive feature of loop shape. These labels are documented in `metric_reliability_final.csv` rather than selecting metrics only by apparent differentiation performance.

Overall, the conventional LAOS baseline answers the Member 2 question: the Armstrong blood data show clear strain-dependent changes in first-harmonic viscoelasticity and loop geometry, while higher-harmonic nonlinearity adds information that is strongly frequency-dependent. These features provide the conventional baseline against which the FFT/STFT/CWT/DWT features should be compared in the later project stages.

## Figure captions

**Figure 1.** Median storage modulus G′ versus nominal strain amplitude. Error bars show the interquartile range across available measurements/workbooks at each condition.

**Figure 2.** Median loss modulus G″ versus nominal strain amplitude. G″ decreases monotonically with strain amplitude at all three frequencies.

**Figure 3.** Phase angle versus nominal strain amplitude. The phase angle moves toward 90° as strain increases, consistent with a more loss-dominated first-harmonic response.

**Figure 4.** Third-harmonic intensity ratio I3/I1 versus nominal strain amplitude. The relationship is positive at 0.5–1 rad/s but reverses at 5 rad/s.

**Figure 7–9.** Cross-validation of recomputed values against Armstrong rheometer summary values. The dashed line denotes identity.

**Figure 10.** Representative stress–strain Lissajous loop from DEC17 t0, ω = 1 rad/s, γ₀ = 10.

**Figure 11.** Corresponding first, third and fifth stress-harmonic amplitudes for the representative DEC17 measurement.

## References
Armstrong, M., Scully, M., Clark, M., Corrigan, T., & James, C. (2021). A simple approach for adding thixotropy to an elasto-visco-plastic rheological model to facilitate structural interrogation of human blood. *Journal of Non-Newtonian Fluid Mechanics, 290*, 104503. https://doi.org/10.1016/j.jnnfm.2021.104503

Armstrong, M., Pincot, A., Rogers, S., Knight, T., & Bailey, D. (2022). Recent advances in biofluid mechanics and bio- and hemorheology collating recent advances in predicting complex behavior of human blood with thixo-elasto-visco-plastic models and sequence of physical process. *Frontiers in Physics, 10*, 889065. https://doi.org/10.3389/fphy.2022.889065

Pincot, A., Burpo, F. J., Javadi, E., Jamali, S., Farrington, S., & Armstrong, M. J. (2023). Characterizing blood hysteresis via tensorial thixo-elasto-viscoplastic modeling. *Physics of Fluids, 35*(11), 113104. https://doi.org/10.1063/5.0169051
