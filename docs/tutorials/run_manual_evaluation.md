# Tutorial: Run a Manual Evaluation

1. Benchmark each stack with the same model, prompt set, sampling settings, and hardware.
2. Export the results to the required CSV format.
3. Adjust `weights.json` to match your adoption goal.
4. Run:

```bash
PYTHONPATH=src python -m inference_stack_eval.cli evaluate   --metrics examples/minimal/metrics.csv   --weights examples/minimal/weights.json   --out reports/manual_report.md
```

5. Review the report with an engineer who understands the runtime configuration.

Do not treat the final score as a replacement for engineering judgment.
