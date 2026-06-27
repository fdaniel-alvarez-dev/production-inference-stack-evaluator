import unittest

from inference_stack_eval.core.models import MetricRow
from inference_stack_eval.core.report import render_markdown_report


class ReportTests(unittest.TestCase):
    def test_report_contains_score_and_warning(self):
        row = MetricRow("vLLM", "short_chat", 100, 200, 300, 80, 1000, 20, 40, 50, 1.0, 0.1, 4, 4, 5)
        report = render_markdown_report([row], {"vLLM": 1.0}, {"p95_ms": 1})
        self.assertIn("LLM Inference Stack Evaluation Report", report)
        self.assertIn("not a universal benchmark claim", report)


if __name__ == "__main__":
    unittest.main()
