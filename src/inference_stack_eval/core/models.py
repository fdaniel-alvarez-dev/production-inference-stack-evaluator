from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


LOWER_IS_BETTER = {
    "p50_ms",
    "p95_ms",
    "p99_ms",
    "ttft_ms",
    "gpu_memory_gb",
    "cost_per_1m_tokens_usd",
    "error_rate_pct",
}

HIGHER_IS_BETTER = {
    "output_tokens_per_sec",
    "requests_per_sec",
    "prefix_cache_hit_rate_pct",
    "observability_score",
    "deployment_score",
    "documentation_score",
}

REQUIRED_METRICS = LOWER_IS_BETTER | HIGHER_IS_BETTER


@dataclass(frozen=True)
class MetricRow:
    stack: str
    workload: str
    p50_ms: float
    p95_ms: float
    p99_ms: float
    ttft_ms: float
    output_tokens_per_sec: float
    requests_per_sec: float
    gpu_memory_gb: float
    prefix_cache_hit_rate_pct: float
    cost_per_1m_tokens_usd: float
    error_rate_pct: float
    observability_score: float
    deployment_score: float
    documentation_score: float

    @classmethod
    def from_mapping(cls, row: dict[str, str]) -> "MetricRow":
        values: dict[str, object] = {
            "stack": row.get("stack", "").strip(),
            "workload": row.get("workload", "").strip(),
        }
        if not values["stack"] or not values["workload"]:
            raise ValueError("Each row must include non-empty stack and workload values.")
        for name in REQUIRED_METRICS:
            raw = row.get(name)
            if raw is None or raw == "":
                raise ValueError(f"Missing required metric: {name}")
            values[name] = float(raw)
        return cls(**values)  # type: ignore[arg-type]

    def metric_value(self, metric: str) -> float:
        return float(getattr(self, metric))


def known_metrics() -> Iterable[str]:
    return sorted(REQUIRED_METRICS)
