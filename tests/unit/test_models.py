import unittest

from inference_stack_eval.core.models import MetricRow


class ModelTests(unittest.TestCase):
    def test_metric_row_from_mapping(self):
        row = MetricRow.from_mapping({
            "stack": "vLLM",
            "workload": "short_chat",
            "p50_ms": "100",
            "p95_ms": "200",
            "p99_ms": "300",
            "ttft_ms": "80",
            "output_tokens_per_sec": "1000",
            "requests_per_sec": "20",
            "gpu_memory_gb": "40",
            "prefix_cache_hit_rate_pct": "50",
            "cost_per_1m_tokens_usd": "1.0",
            "error_rate_pct": "0.1",
            "observability_score": "4",
            "deployment_score": "4",
            "documentation_score": "5",
        })
        self.assertEqual(row.stack, "vLLM")
        self.assertEqual(row.p95_ms, 200)


if __name__ == "__main__":
    unittest.main()
