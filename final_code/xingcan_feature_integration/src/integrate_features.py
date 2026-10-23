from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def prefixed(frame: pd.DataFrame, id_column: str, prefix: str) -> pd.DataFrame:
    if id_column not in frame.columns:
        raise ValueError(f"missing identifier column: {id_column}")
    if frame[id_column].duplicated().any():
        raise ValueError(f"duplicate identifiers in {prefix.rstrip('_')} table")
    renamed = frame.rename(columns={id_column: "measurement_id"}).copy()
    renamed.columns = [
        column if column == "measurement_id" else f"{prefix}{column}"
        for column in renamed.columns
    ]
    return renamed


def integrate(
    measurement_index: pd.DataFrame,
    laos_features: pd.DataFrame,
    step_features: pd.DataFrame,
    step_id_column: str,
) -> pd.DataFrame:
    if measurement_index["measurement_id"].duplicated().any():
        raise ValueError("measurement index contains duplicate identifiers")

    combined = measurement_index.merge(
        prefixed(laos_features, "measurement_id", "laos__"),
        on="measurement_id",
        how="left",
        validate="one_to_one",
    )
    combined = combined.merge(
        prefixed(step_features, step_id_column, "step__"),
        on="measurement_id",
        how="left",
        validate="one_to_one",
    )
    combined["has_laos_features"] = combined.filter(like="laos__").notna().any(axis=1)
    combined["has_step_features"] = combined.filter(like="step__").notna().any(axis=1)
    return combined


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--measurement-index", type=Path, required=True)
    parser.add_argument("--laos-features", type=Path, required=True)
    parser.add_argument("--step-features", type=Path, required=True)
    parser.add_argument("--step-id-column", default="step_id")
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    combined = integrate(
        pd.read_csv(args.measurement_index),
        pd.read_csv(args.laos_features),
        pd.read_csv(args.step_features),
        args.step_id_column,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(args.output, index=False)
    print(f"rows: {len(combined)}")
    print(f"LAOS features: {int(combined['has_laos_features'].sum())}")
    print(f"step features: {int(combined['has_step_features'].sum())}")


if __name__ == "__main__":
    main()
