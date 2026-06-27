# Contributing

Thank you for improving this repository.

## Local checks

```bash
make setup
make lint
make test
make security
make docs
```

## Contribution guidelines

- Do not add private prompts, `.input/`, model logs, worklogs, or benchmark outputs that reveal customer or internal data.
- Do not add benchmark claims unless the model, hardware, framework version, configuration, workload, and raw measurements are documented.
- Prefer small, reviewable changes.
- Keep documentation aligned with implemented behavior.

## Benchmark contribution rules

A benchmark contribution must include:

- model name and exact version or revision
- GPU model, count, memory, driver, CUDA, and container/runtime versions
- inference-stack version and command line
- sampling parameters
- warmup procedure
- concurrency sweep
- raw metrics or reproducible collection method
- failure/retry accounting
