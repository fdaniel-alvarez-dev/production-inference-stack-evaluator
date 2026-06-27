class EvaluationError(Exception):
    """Base exception for evaluator errors."""


class InputFormatError(EvaluationError):
    """Raised when an input file is missing required fields or values."""
