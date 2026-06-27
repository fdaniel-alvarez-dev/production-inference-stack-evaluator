from __future__ import annotations

import csv
from pathlib import Path

from inference_stack_eval.adapters.base import MetricsReader
from inference_stack_eval.core.models import MetricRow
from inference_stack_eval.errors import InputFormatError


class CsvMetricsReader(MetricsReader):
    def __init__(self, path: Path):
        self.path = path

    def read(self) -> list[MetricRow]:
        if not self.path.exists():
            raise InputFormatError(f"Metrics file not found: {self.path}")
        with self.path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = []
            for line_number, raw_row in enumerate(reader, start=2):
                try:
                    rows.append(MetricRow.from_mapping(raw_row))
                except Exception as exc:  # pragma: no cover - message clarity matters more than class here
                    raise InputFormatError(f"Invalid metrics row at line {line_number}: {exc}") from exc
        if not rows:
            raise InputFormatError("Metrics file contains no data rows.")
        return rows
