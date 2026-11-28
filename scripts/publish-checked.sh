#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 scripts/publication-title-gate.py
git diff --check
git push "$@"
