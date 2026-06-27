import unittest

from inference_stack_eval.core.models import MetricRow
from inference_stack_eval.core.scoring import normalize_metric, score_rows
from inference_stack_eval.errors import InputFormatError


class ScoringTests(unittest.TestCase):
    def test_normalize_lower_is_better(self):
        self.assertEqual(normalize_metric(10, [10, 20], higher_is_better=False), 1.0)
        self.assertEqual(normalize_metric(20, [10, 20], higher_is_better=False), 0.0)

    def test_normalize_higher_is_better(self):
        self.assertEqual(normalize_metric(20, [10, 20], higher_is_better=True), 1.0)
        self.assertEqual(normalize_metric(10, [10, 20], higher_is_better=True), 0.0)

    def test_score_rows_prefers_better_latency_and_throughput(self):
        rows = [
            MetricRow("vLLM", "short_chat", 100, 200, 300, 80, 1000, 20, 40, 50, 1.0, 0.1, 4, 4, 5),
            MetricRow("SGLang", "short_chat", 120, 240, 350, 90, 900, 18, 42, 60, 1.2, 0.2, 4, 3, 4),
        ]
        scores = score_rows(rows, {"p95_ms": 1, "output_tokens_per_sec": 1})
        self.assertGreater(scores["vLLM"], scores["SGLang"])

    def test_unknown_weight_is_rejected(self):
        rows = [MetricRow("vLLM", "short_chat", 100, 200, 300, 80, 1000, 20, 40, 50, 1.0, 0.1, 4, 4, 5)]
        with self.assertRaises(InputFormatError):
            score_rows(rows, {"unknown_metric": 1})


if __name__ == "__main__":
    unittest.main()
