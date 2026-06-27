# Observability

The report is only as useful as the metrics collected before scoring.

Recommended measurements:

- p50, p95, and p99 latency
- TTFT for streaming workloads
- output tokens/sec
- requests/sec
- GPU memory usage
- cache hit rate
- failed and retried requests
- queue time where available
- framework/server logs during saturation

Always keep framework version, driver, CUDA, container, model, and sampling parameters with the metrics.
