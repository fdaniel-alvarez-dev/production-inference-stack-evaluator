#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "ARTICLE.md",
    "EDITORIAL_BRIEF.md",
    "QUALITY_CHECKLIST.md",
    "HUMANIZATION_NOTES.md",
    "docs/research_notes.md",
    "docs/structure.md",
    "docs/assumptions.md",
    "assets/diagrams",
    "assets/images",
    ".github/workflows",
    "manifest.json",
]
FORBIDDEN_NAMES = {"article_prompt_rewritten.txt", "temporary_notes", "private_build_log", "draft_output"}

def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).exists()]
    forbidden = []
    for path in ROOT.rglob("*"):
        if any(part in {".git", "__pycache__", ".pytest_cache", "node_modules", ".venv"} for part in path.parts):
            forbidden.append(str(path.relative_to(ROOT)))
        if path.name.lower() in FORBIDDEN_NAMES:
            forbidden.append(str(path.relative_to(ROOT)))
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    if not manifest.get("github_ready"):
        missing.append("manifest.github_ready=true")
    if missing or forbidden:
        print(json.dumps({"status": "FAIL", "missing": missing, "forbidden": forbidden}, indent=2))
        return 1
    print(json.dumps({"status": "PASS", "repo": ROOT.name}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
