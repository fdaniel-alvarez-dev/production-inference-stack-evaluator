from __future__ import annotations

import argparse
import json
from pathlib import Path

from inference_stack_eval.adapters.manual_csv import CsvMetricsReader
from inference_stack_eval.core.report import render_markdown_report
from inference_stack_eval.core.scoring import score_rows
from inference_stack_eval.observability.logging import configure_logging


def load_weights(path: Path) -> dict[str, float]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Weights file must contain a JSON object.")
    return {str(key): float(value) for key, value in data.items()}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate inference-stack fit from benchmark metrics.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    evaluate = subparsers.add_parser("evaluate", help="Generate a Markdown scorecard report.")
    evaluate.add_argument("--metrics", required=True, type=Path, help="CSV file with benchmark metrics.")
    evaluate.add_argument("--weights", required=True, type=Path, help="JSON file with metric weights.")
    evaluate.add_argument("--out", required=True, type=Path, help="Output Markdown report path.")
    return parser


def main(argv: list[str] | None = None) -> int:
    configure_logging()
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "evaluate":
        rows = CsvMetricsReader(args.metrics).read()
        weights = load_weights(args.weights)
        scores = score_rows(rows, weights)
        report = render_markdown_report(rows, scores, weights)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
        print(f"Wrote {args.out}")
        return 0
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
