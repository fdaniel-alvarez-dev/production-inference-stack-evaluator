# ADR-0002: Core Design Tradeoffs

## Status

Accepted

## Decision

Use CSV metrics and JSON weights for version 0.1.0.

## Rationale

This keeps the repository dependency-light and easy to review. Direct adapters for benchmark tools can be added later after the metric schema stabilizes.

## Tradeoff

The first version is less automated, but more transparent.
