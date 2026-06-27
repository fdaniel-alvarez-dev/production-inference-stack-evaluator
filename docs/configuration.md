# Configuration

## Metrics CSV

Required columns:

- stack
- workload
- p50_ms
- p95_ms
- p99_ms
- ttft_ms
- output_tokens_per_sec
- requests_per_sec
- gpu_memory_gb
- prefix_cache_hit_rate_pct
- cost_per_1m_tokens_usd
- error_rate_pct
- observability_score
- deployment_score
- documentation_score

## Weights JSON

The weights file maps metric names to numeric weights. Higher weights make the metric more important in the final score.

Do not use the same weights for every adoption decision. A batch-processing team and a user-facing chat team should not value the same metrics equally.
