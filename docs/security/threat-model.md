# Threat Model

## Assets

- benchmark datasets
- production-like prompts
- latency and throughput results
- model and infrastructure metadata
- generated reports

## Risks

- accidental commit of private prompts or traces
- leaking cloud or infrastructure identifiers
- publishing benchmark claims without enough context
- treating illustrative sample data as measured production data

## Controls

- `.gitignore` excludes private workspaces and common secret files
- `scripts/basic_secret_scan.sh` performs a basic local scan
- documentation requires benchmark context before publishing claims
- sample data is explicitly labeled illustrative
