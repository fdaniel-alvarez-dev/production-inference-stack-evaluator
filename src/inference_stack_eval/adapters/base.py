from __future__ import annotations

from abc import ABC, abstractmethod

from inference_stack_eval.core.models import MetricRow


class MetricsReader(ABC):
    @abstractmethod
    def read(self) -> list[MetricRow]:
        """Return normalized metric rows."""
