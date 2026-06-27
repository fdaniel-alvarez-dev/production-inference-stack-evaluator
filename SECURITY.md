# Security Policy

## Reporting a vulnerability

Please report vulnerabilities privately through the repository maintainer contact path. Do not open a public issue for secrets, exploit details, or sensitive benchmark data.

## Scope

This repository contains a scoring and reporting helper. It does not run model servers or manage credentials. Still, benchmark data may contain sensitive workload names, prompt shapes, model choices, or infrastructure details.

## Data-handling rule

Never commit production prompts, customer data, private logs, API keys, cloud account identifiers, kubeconfigs, or raw traces from internal systems.
