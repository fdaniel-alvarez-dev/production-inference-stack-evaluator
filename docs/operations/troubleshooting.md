# Troubleshooting

## The score looks wrong

Check whether one metric dominates the weights. Then inspect whether the input values use the same units across all rows.

## The report favors a stack with bad failures

Increase the weight for `error_rate_pct` or add a hard gate before scoring. In production evaluations, a stack with unacceptable failure behavior should not win on throughput alone.

## Scores changed after a version bump

That is expected. Re-run the benchmark when CUDA, driver, container, model, or framework versions change.
