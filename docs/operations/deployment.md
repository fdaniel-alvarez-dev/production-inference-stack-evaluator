# Deployment

This repository is designed to run locally or in CI.

## Local

```bash
make setup
make test
make example
```

## Container

```bash
docker compose run --rm evaluator
```

## Operational boundary

The evaluator does not connect to GPUs, model servers, or cloud APIs. Keep raw production benchmark collection in a separate, access-controlled environment.
