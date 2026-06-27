from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone

from inference_stack_eval.core.models import MetricRow


def render_markdown_report(rows: list[MetricRow], scores: dict[str, float], weights: dict[str, float]) -> str:
    by_stack: dict[str, list[MetricRow]] = defaultdict(list)
    for row in rows:
        by_stack[row.stack].append(row)

    lines = [
        "# LLM Inference Stack Evaluation Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
        "This report is a decision aid, not a universal benchmark claim. Interpret the scores only in the context of the workload, hardware, model, framework versions, and measurement method used to generate the input metrics.",
        "",
        "## Overall score",
        "",
        "| Stack | Score |",
        "| --- | ---: |",
    ]
    for stack, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"| {stack} | {score:.4f} |")

    lines.extend(["", "## Weights", "", "| Metric | Weight |", "| --- | ---: |"])
    for metric, weight in sorted(weights.items()):
        lines.append(f"| {metric} | {weight} |")

    lines.extend(["", "## Workload details", ""])
    for stack, stack_rows in sorted(by_stack.items()):
        lines.extend([f"### {stack}", "", "| Workload | p95 ms | TTFT ms | tok/s | req/s | VRAM GB | cost / 1M | errors % |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"])
        for row in stack_rows:
            lines.append(
                f"| {row.workload} | {row.p95_ms:.1f} | {row.ttft_ms:.1f} | {row.output_tokens_per_sec:.1f} | {row.requests_per_sec:.1f} | {row.gpu_memory_gb:.1f} | {row.cost_per_1m_tokens_usd:.2f} | {row.error_rate_pct:.2f} |"
            )
        lines.append("")

    lines.extend([
        "## Review notes",
        "",
        "- Confirm that all stacks used the same model family, quantization policy, sampling parameters, and prompt set.",
        "- Review failed and retried requests before treating throughput as a win.",
        "- Re-run the benchmark when driver, CUDA, container, model, or framework versions change.",
        "- Keep raw metrics with the release artifact if publishing benchmark claims.",
        "",
    ])
    return "\n".join(lines)
