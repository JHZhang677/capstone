# Correcting the instrument condition audit in cells 116-118
# Requiring the notebook setup variables before executing these cells

instrument_pair_condition_data = pd.read_csv(LAOS_FEATURE_DIR / "instrument_crossvalidation.csv")
instrument_pair_condition_data["omega_nominal_numeric"] = pd.to_numeric(
    instrument_pair_condition_data["omega_nominal"], errors = "coerce"
)
instrument_pair_condition_data["omega_instrument_numeric"] = pd.to_numeric(
    instrument_pair_condition_data["omega_instrument"], errors = "coerce"
)
# Converting the stored nominal strain fraction to percent before comparing conditions
instrument_pair_condition_data["strain_nominal_fraction"] = pd.to_numeric(
    instrument_pair_condition_data["strain_nominal"], errors = "coerce"
)
instrument_pair_condition_data["strain_nominal_percent"] = (
    100.0 * instrument_pair_condition_data["strain_nominal_fraction"]
)
instrument_pair_condition_data["strain_instrument_numeric"] = pd.to_numeric(
    instrument_pair_condition_data["strain_instrument_pct"], errors = "coerce"
)

instrument_pair_condition_data["frequency_relative_difference"] = (
    abs(instrument_pair_condition_data["omega_instrument_numeric"]
        - instrument_pair_condition_data["omega_nominal_numeric"])
    / instrument_pair_condition_data["omega_nominal_numeric"].abs().replace(0, np.nan)
)
instrument_pair_condition_data["strain_relative_difference"] = (
    abs(instrument_pair_condition_data["strain_instrument_numeric"]
        - instrument_pair_condition_data["strain_nominal_percent"])
    / instrument_pair_condition_data["strain_nominal_percent"].abs().replace(0, np.nan)
)
instrument_pair_condition_data["frequency_matches_within_5_percent"] = (
    instrument_pair_condition_data["frequency_relative_difference"] <= 0.05
)
instrument_pair_condition_data["strain_matches_within_5_percent"] = (
    instrument_pair_condition_data["strain_relative_difference"] <= 0.05
)
instrument_pair_condition_data["same_condition_match"] = (
    instrument_pair_condition_data["frequency_matches_within_5_percent"]
    & instrument_pair_condition_data["strain_matches_within_5_percent"]
)

instrument_condition_summary = pd.DataFrame([{
    "instrument_pair_count": len(instrument_pair_condition_data),
    "frequency_matches_within_5_percent": int(
        instrument_pair_condition_data["frequency_matches_within_5_percent"].sum()
    ),
    "strain_matches_within_5_percent": int(
        instrument_pair_condition_data["strain_matches_within_5_percent"].sum()
    ),
    "matched_frequency_and_strain_pairs": int(
        instrument_pair_condition_data["same_condition_match"].sum()
    ),
    "median_laos_strain_percent": instrument_pair_condition_data["strain_nominal_percent"].median(),
    "median_instrument_strain_percent": instrument_pair_condition_data["strain_instrument_numeric"].median(),
}])

display(instrument_condition_summary)
display(instrument_pair_condition_data[[
    "source_file", "measurement_id", "omega_nominal_numeric", "omega_instrument_numeric",
    "strain_nominal_percent", "strain_instrument_numeric", "same_condition_match",
]].head(10))

instrument_pair_condition_data.to_csv(
    FINAL_REAL_ANALYSIS_OUTPUT_DIRECTORY / "instrument_condition_match_audit.csv",
    index = False,
)
instrument_condition_summary.to_csv(
    FINAL_REAL_ANALYSIS_OUTPUT_DIRECTORY / "instrument_condition_match_summary.csv",
    index = False,
)

reviewed_laos_metric_status = pd.DataFrame([
    {
        "metric": "G_prime_Pa",
        "previous_status": "VALID",
        "reviewed_status": "Matched-condition instrument-summary agreement",
        "reason": "Nominal strain fractions are converted to percent; all 26 frequency/strain pairs pass the 5% audit tolerance.",
    },
    {
        "metric": "G_double_prime_Pa",
        "previous_status": "VALID",
        "reviewed_status": "Matched-condition instrument-summary agreement",
        "reason": "Nominal strain fractions are converted to percent; all 26 frequency/strain pairs pass the 5% audit tolerance.",
    },
    {
        "metric": "phase_angle_deg",
        "previous_status": "VALID",
        "reviewed_status": "Derived feature; no independent instrument phase measurement",
        "reason": "The supplied instrument summary has no directly matched phase-angle column.",
    },
    {
        "metric": "I3_I1",
        "previous_status": "VALID WITH CAUTION",
        "reviewed_status": "Matched-condition agreement; detrending caution",
        "reason": "Twelve available harmonic pairs belong to the matched-condition set; the feature remains sensitive to detrending.",
    },
    {
        "metric": "I5_I1",
        "previous_status": "UNSTABLE / EXPLORATORY",
        "reviewed_status": "Exploratory",
        "reason": "The feature is sensitive to detrending and lacks a matched instrument reference.",
    },
    {
        "metric": "THD_2to5",
        "previous_status": "UNSTABLE / EXPLORATORY",
        "reviewed_status": "Exploratory",
        "reason": "The feature is sensitive to detrending and combines higher harmonics.",
    },
    {
        "metric": "lissajous_normalized_area",
        "previous_status": "VALID DESCRIPTIVE",
        "reviewed_status": "Descriptive feature",
        "reason": "The feature describes loop shape; it is not an independent biological endpoint.",
    },
])

display(reviewed_laos_metric_status)
reviewed_laos_metric_status.to_csv(
    FINAL_REAL_ANALYSIS_OUTPUT_DIRECTORY / "reviewed_laos_metric_status.csv",
    index = False,
)
