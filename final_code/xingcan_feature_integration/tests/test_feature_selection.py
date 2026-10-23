from pathlib import Path
import sys
import unittest

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from select_features import build_candidate_set, validate_redundancy
from integrate_features import integrate


class FeatureSelectionTests(unittest.TestCase):
    def test_candidate_set_has_six_features(self):
        decisions = pd.read_csv(ROOT / "data" / "feature_decisions.csv")
        selected = build_candidate_set(decisions)
        self.assertEqual(len(selected), 6)
        self.assertEqual(set(selected["protocol"]), {"LAOS", "Transform", "Step"})

    def test_redundancy_table_is_valid(self):
        redundancy = pd.read_csv(ROOT / "data" / "redundancy_checks.csv")
        validate_redundancy(redundancy)

    def test_feature_tables_join_by_measurement(self):
        index = pd.DataFrame({"measurement_id": ["M1", "M2", "M3"]})
        laos = pd.DataFrame({"measurement_id": ["M1"], "Gpp": [2.0]})
        steps = pd.DataFrame({"step_id": ["M2"], "undershoot": [0.2]})
        combined = integrate(index, laos, steps, "step_id")
        self.assertEqual(len(combined), 3)
        self.assertEqual(int(combined["has_laos_features"].sum()), 1)
        self.assertEqual(int(combined["has_step_features"].sum()), 1)


if __name__ == "__main__":
    unittest.main()
