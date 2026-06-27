#!/usr/bin/env bash
set -euo pipefail

echo "== Public release gate =="

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: not inside a Git repository." >&2
  exit 1
fi

ROOT="$(git rev-parse --show-toplevel)"
echo "Git root: $ROOT"
cd "$ROOT"

echo "-- Tracked private workflow artifacts --"
if git ls-files | grep -Ei '(^|/)\.input/|humanizer|worklog|scratch|session|transcript|private-notes|prompts/' ; then
  echo "ERROR: private workflow artifacts appear in tracked files." >&2
  exit 1
else
  echo "OK: no matching private workflow artifacts tracked."
fi

echo "-- Git status --"
git status --short

for target in setup lint test security docs; do
  if grep -qE "^${target}:" Makefile 2>/dev/null; then
    make "$target"
  else
    echo "Skipping make ${target}: target not found"
  fi
done

echo "Release gate completed. Manual review is still required."
