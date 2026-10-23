from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


SELECTED_STATUSES = {"Retain", "Provisional"}


def build_candidate_set(decisions: pd.DataFrame) -> pd.DataFrame:
    required = {"feature", "protocol", "role", "decision", "evidence", "limitation"}
    if missing := required - set(decisions.columns):
        raise ValueError(f"decision table is missing: {sorted(missing)}")
    if decisions["feature"].duplicated().any():
        raise ValueError("feature names must be unique")

    selected = decisions.loc[decisions["decision"].isin(SELECTED_STATUSES)].copy()
    if len(selected) != 6:
        raise ValueError(f"expected six candidate features, found {len(selected)}")
    if set(selected["protocol"]) != {"LAOS", "Transform", "Step"}:
        raise ValueError("candidate set must cover LAOS, transform and step protocols")
    return selected.reset_index(drop=True)


def validate_redundancy(redundancy: pd.DataFrame) -> None:
    required = {"feature_1", "feature_2", "groups", "median_spearman_rho", "decision"}
    if missing := required - set(redundancy.columns):
        raise ValueError(f"redundancy table is missing: {sorted(missing)}")
    if redundancy["groups"].lt(1).any():
        raise ValueError("redundancy checks need at least one eligible group")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--decisions", type=Path, required=True)
    parser.add_argument("--redundancy", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    decisions = pd.read_csv(args.decisions)
    redundancy = pd.read_csv(args.redundancy)
    validate_redundancy(redundancy)
    selected = build_candidate_set(decisions)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    selected.to_csv(args.output_dir / "candidate_features.csv", index=False)
    decisions.to_csv(args.output_dir / "all_feature_decisions.csv", index=False)
    redundancy.to_csv(args.output_dir / "redundancy_checks.csv", index=False)
    print(selected[["protocol", "feature", "decision"]].to_string(index=False))


if __name__ == "__main__":
    main()

