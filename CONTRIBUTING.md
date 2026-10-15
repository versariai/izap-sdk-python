# Contributing

This repository is the public mirror of `izap` (PyPI). The package is developed in
iZap's internal monorepo; each release replaces `main` here with that copy and tags
`v<version>`, which publishes to PyPI.

- **Issues are welcome.** Bugs, generated-client mismatches, missing endpoints.
- **Pull requests are welcome too.** We review them here, then port the change into
  the monorepo, so it reaches this repo with the next release instead of as a merge.

## Develop

Requires Python 3.11 or newer, and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run pytest
uv run ruff check
uv run python scripts/generate.py --check   # generated-client drift check
```
