# LLM Inference Stack Evaluator

A small, reproducible companion repository for evaluating **vLLM**, **SGLang**, and **TensorRT-LLM** as production inference stacks.

The repository does not claim that one stack is universally better. It helps teams compare stacks against their own workload shape, hardware envelope, and operating constraints.

## Who this is for

- ML platform engineers comparing open-weight serving stacks.
- SREs who need p95/p99 latency and failure-mode visibility before adoption.
- Staff engineers creating an evidence-based adoption scorecard.
- Technical writers building a reproducible companion for an inference-stack article.

## What is included

- A benchmark matrix model for short chat, long-context RAG, structured JSON, tool-calling/agentic requests, batch generation, and repeated-prefix workloads.
- A deterministic scoring engine over CSV metrics.
- Example metrics and weights.
- A Markdown report generator.
- Documentation for benchmark fairness, operations, security, and adoption decisions.

## What is intentionally out of scope

- This repo does not run vLLM, SGLang, or TensorRT-LLM servers for you.
- It does not publish benchmark numbers.
- It does not simulate GPU behavior.
- It does not replace a real load test on your hardware, models, drivers, and framework versions.

## 5-minute quickstart

```bash
python -m venv .venv
source .venv/bin/activate
make setup
make test
make example
```

The example writes a Markdown report to `reports/minimal_report.md`.

## Example command

```bash
PYTHONPATH=src python -m inference_stack_eval.cli evaluate   --metrics examples/minimal/metrics.csv   --weights examples/minimal/weights.json   --out reports/minimal_report.md
```

## Core idea

The right serving stack depends on workload fit:

| Workload | Stress point | Why it matters |
| --- | --- | --- |
| Short chat | TTFT and scheduler overhead | User-facing latency dominates. |
| Long-context RAG | prefill and KV cache pressure | Context size can dominate cost and latency. |
| Structured JSON | constrained decoding and retries | Invalid output can erase throughput wins. |
| Tool-calling / agents | prefix reuse and traceability | Repeated schemas and loops change the economics. |
| Batch generation | throughput and fairness | Offline work rewards sustained tokens/sec. |
| Repeated prefix | cache hit rate | Stable system prompts and tool schemas can materially change results. |

## Repository map

```text
src/inference_stack_eval/   scoring and report generation
tests/                      unit tests for scoring and report behavior
examples/minimal/           runnable sample input
examples/realistic/         guidance for real benchmark inputs
docs/                       architecture, operations, security, and decisions
.github/workflows/          CI and basic security checks
```

## Companion article thesis

Start with workload characterization, not tool selection.

## License

MIT.
