from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def check_unique(frame: pd.DataFrame, column: str, label: str) -> None:
    if column not in frame.columns:
        raise ValueError(f"{label} is missing the {column} column")
    if frame[column].isna().any():
        raise ValueError(f"{label} contains missing {column} values")
    if frame[column].duplicated().any():
        raise ValueError(f"{label} contains duplicate {column} values")


def build_audit(index: pd.DataFrame, laos: pd.DataFrame) -> pd.DataFrame:
    check_unique(index, "measurement_id", "measurement index")
    check_unique(laos, "measurement_id", "LAOS feature table")

    index_ids = set(index["measurement_id"].astype(str))
    laos_ids = set(laos["measurement_id"].astype(str))
    rows = [
        {
            "table": "measurement_index",
            "rows": len(index),
            "unique_measurements": len(index_ids),
            "ids_in_measurement_index": len(index_ids),
        },
        {
            "table": "laos_features",
            "rows": len(laos),
            "unique_measurements": len(laos_ids),
            "ids_in_measurement_index": len(laos_ids & index_ids),
        },
    ]
    return pd.DataFrame(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--measurement-index", type=Path, required=True)
    parser.add_argument("--laos-features", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    audit = build_audit(
        pd.read_csv(args.measurement_index),
        pd.read_csv(args.laos_features),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    audit.to_csv(args.output, index=False)
    print(audit.to_string(index=False))


if __name__ == "__main__":
    main()

