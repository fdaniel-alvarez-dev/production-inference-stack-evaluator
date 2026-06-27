#!/usr/bin/env bash
set -euo pipefail

# Basic repository hygiene scan. This intentionally avoids matching generic words
# such as "token" because this project legitimately discusses output tokens/sec.
if grep -RInE '(api[_-]?key[[:space:]]*=|secret[[:space:]]*=|password[[:space:]]*=|private[_-]?key[[:space:]]*=|BEGIN RSA|BEGIN OPENSSH|kubeconfig)' . \
  --exclude-dir=.git \
  --exclude-dir=.venv \
  --exclude-dir=__pycache__ \
  --exclude-dir=reports \
  --exclude='.env.example' \
  --exclude='.gitignore' \
  --exclude='basic_secret_scan.sh' \
  --exclude='*.md'; then
  echo "Potential secret-like string found. Review manually." >&2
  exit 1
fi

echo "No obvious secret-like strings found by the basic scan."
