# Architecture

The repository separates three concerns:

1. **Metric ingestion** from a manual CSV file.
2. **Transparent scoring** using weighted normalized metrics.
3. **Report generation** in Markdown.

```text
CSV metrics + JSON weights
          |
          v
CsvMetricsReader
          |
          v
MetricRow objects
          |
          v
score_rows()
          |
          v
Markdown report
```

The implementation intentionally avoids hidden benchmark logic. A senior reviewer should be able to inspect the weights, the raw metrics, and the scoring output without trusting a black box.

## Why CSV first

CSV is not glamorous, but it keeps the first version easy to audit. Most load-test tools, dashboards, and notebooks can export to CSV. Teams can add direct adapters later when they have a stable source of metrics.

## Non-goal

This project does not run inference servers. It is a decision-support companion for benchmark data produced elsewhere.
