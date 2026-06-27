from __future__ import annotations

from collections import defaultdict

from inference_stack_eval.core.models import HIGHER_IS_BETTER, LOWER_IS_BETTER, MetricRow
from inference_stack_eval.errors import InputFormatError


def normalize_metric(value: float, values: list[float], higher_is_better: bool) -> float:
    """Normalize a metric to the [0, 1] range.

    The function is intentionally simple and transparent. It is not a statistical benchmark.
    """
    if not values:
        raise InputFormatError("Cannot normalize an empty metric list.")
    low = min(values)
    high = max(values)
    if high == low:
        return 1.0
    raw = (value - low) / (high - low)
    return raw if higher_is_better else 1.0 - raw


def validate_weights(weights: dict[str, float]) -> None:
    known = HIGHER_IS_BETTER | LOWER_IS_BETTER
    unknown = set(weights) - known
    if unknown:
        raise InputFormatError(f"Unknown weight metrics: {', '.join(sorted(unknown))}")
    total = sum(weights.values())
    if total <= 0:
        raise InputFormatError("At least one weight must be positive.")
    if any(value < 0 for value in weights.values()):
        raise InputFormatError("Weights cannot be negative.")


def score_rows(rows: list[MetricRow], weights: dict[str, float]) -> dict[str, float]:
    validate_weights(weights)
    values_by_metric: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        for metric in weights:
            values_by_metric[metric].append(row.metric_value(metric))

    score_by_stack: dict[str, float] = defaultdict(float)
    weight_total = sum(weights.values())
    for row in rows:
        row_score = 0.0
        for metric, weight in weights.items():
            higher = metric in HIGHER_IS_BETTER
            row_score += normalize_metric(row.metric_value(metric), values_by_metric[metric], higher) * weight
        score_by_stack[row.stack] += row_score / weight_total

    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row.stack] += 1
    return {stack: round(score / counts[stack], 4) for stack, score in score_by_stack.items()}
