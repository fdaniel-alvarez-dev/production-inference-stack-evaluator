# ADR-0001: Context and Scope

## Status

Accepted

## Context

Teams comparing vLLM, SGLang, and TensorRT-LLM often need a repeatable way to turn raw metrics into an adoption discussion.

## Decision

Build a small scorecard tool instead of a benchmark runner.

## Consequences

- The tool stays simple and auditable.
- Users must still run real benchmarks elsewhere.
- The repo avoids fake or non-reproducible performance claims.
