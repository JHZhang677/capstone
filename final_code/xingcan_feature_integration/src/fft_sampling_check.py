from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.signal import detrend, periodogram
from scipy.stats import spearmanr


def prepare_signal(frame: pd.DataFrame, sampling_rate: float) -> tuple[np.ndarray, np.ndarray, float]:
    data = (
        frame[["time_s", "stress_pa"]]
        .dropna()
        .groupby("time_s", as_index=False)["stress_pa"]
        .mean()
        .sort_values("time_s")
    )
    time = data["time_s"].to_numpy(float)
    stress = data["stress_pa"].to_numpy(float)
    if len(time) < 20:
        raise ValueError("not enough observations")

    sample_count = int(np.floor((time[-1] - time[0]) * sampling_rate)) + 1
    uniform_time = time[0] + np.arange(sample_count) / sampling_rate
    uniform_stress = np.interp(uniform_time, time, stress)
    uniform_stress = detrend(uniform_stress, type="linear")
    rms = np.sqrt(np.mean(uniform_stress**2))
    if not np.isfinite(rms) or rms == 0:
        raise ValueError("zero stress variation")

    dt90 = float(np.quantile(np.diff(time), 0.9))
    return uniform_time, uniform_stress / rms, 1.0 / (2.0 * dt90)


def high_low_ratio(
    frame: pd.DataFrame,
    angular_frequency: float,
    sampling_rate: float,
) -> float:
    period = 2.0 * np.pi / angular_frequency
    end_time = frame["time_s"].max()
    window = frame.loc[frame["time_s"] >= end_time - 2.0 * period]
    _, stress, support_limit = prepare_signal(window, sampling_rate)

    frequency, density = periodogram(
        stress,
        fs=sampling_rate,
        window="hann",
        detrend=False,
        scaling="density",
    )
    split_frequency = 3.0 * angular_frequency / (2.0 * np.pi)
    keep = (frequency > 0) & (frequency <= min(sampling_rate / 2.0, support_limit))
    frequency = frequency[keep]
    density = density[keep]
    low = density[frequency < split_frequency].sum()
    high = density[frequency >= split_frequency].sum()
    return float(high / low) if low > 0 else np.nan


def run_check(signals: pd.DataFrame, features: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    required = {"measurement_id", "time_s", "stress_pa"}
    if missing := required - set(signals.columns):
        raise ValueError(f"signal table is missing: {sorted(missing)}")
    if "omega_label_rad_s" not in features.columns:
        raise ValueError("LAOS feature table is missing omega_label_rad_s")

    metadata = features.set_index("measurement_id")
    signals = signals.loc[signals["measurement_id"].isin(metadata.index)].copy()
    records = []
    for measurement_id, frame in signals.groupby("measurement_id", sort=True):
        omega = float(metadata.loc[measurement_id, "omega_label_rad_s"])
        try:
            ratio_25 = high_low_ratio(frame, omega, 25.0)
            ratio_50 = high_low_ratio(frame, omega, 50.0)
        except ValueError:
            ratio_25 = ratio_50 = np.nan
        relative_difference = (
            abs(ratio_25 - ratio_50) / abs(ratio_50)
            if np.isfinite(ratio_50) and ratio_50 != 0
            else np.nan
        )
        records.append(
            {
                "measurement_id": measurement_id,
                "fft_ratio_25_hz": ratio_25,
                "fft_ratio_50_hz": ratio_50,
                "relative_absolute_difference": relative_difference,
            }
        )

    results = pd.DataFrame(records)
    complete = results.dropna()
    rho = spearmanr(complete["fft_ratio_25_hz"], complete["fft_ratio_50_hz"]).statistic
    summary = {
        "complete_measurements": int(len(complete)),
        "spearman_rho": float(rho),
        "median_relative_absolute_difference_percent": float(
            100.0 * complete["relative_absolute_difference"].median()
        ),
    }
    return results, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--signals", type=Path, required=True)
    parser.add_argument("--laos-features", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results, summary = run_check(
        pd.read_csv(args.signals),
        pd.read_csv(args.laos_features),
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results.to_csv(args.output_dir / "fft_sampling_measurements.csv", index=False)
    with (args.output_dir / "fft_sampling_summary.json").open("w", encoding="utf-8") as stream:
        json.dump(summary, stream, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
