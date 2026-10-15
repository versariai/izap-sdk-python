#!/usr/bin/env bash
# CI gate for the Python SDK: locked deps, generated-code drift, lint, types, and the
# tests on the default interpreter (.python-version) plus the oldest supported one (3.11).
set -euo pipefail
cd "$(dirname "$0")/.."

uv sync --locked
uv run --no-sync python scripts/generate.py --check
uv run --no-sync ruff check
uv run --no-sync ruff format --check
uv run --no-sync ty check
uv run --no-sync pytest
UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-.venv}-py311" uv run --locked --python 3.11 pytest
