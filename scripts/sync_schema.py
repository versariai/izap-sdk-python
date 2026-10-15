"""Copy the monorepo's canonical public schema into the SDK's vendored snapshot.

    uv run python scripts/sync_schema.py                                   # from the devdocs schema
    IZAP_OPENAPI_INPUT=path/to/openapi.json uv run python scripts/sync_schema.py

Run ``scripts/generate.py`` afterwards and commit both. ``generate.py`` and CI read the
snapshot, not the canonical file, so the SDK still regenerates once it is mirrored out
of the monorepo.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "openapi" / "izap-public.json"
CANONICAL = ROOT.parent.parent / "doc" / "external" / "devdocs" / "api-reference" / "openapi.json"


def main() -> int:
    source = Path(os.environ.get("IZAP_OPENAPI_INPUT") or CANONICAL)
    if not source.is_file():
        sys.exit(f"schema not found: {source}")
    if source.resolve() == SNAPSHOT.resolve():
        print(f"{source} is already the snapshot; nothing to copy")
        return 0
    try:
        json.loads(source.read_text())
    except ValueError as exc:
        sys.exit(f"{source} is not valid JSON: {exc}")
    shutil.copyfile(source, SNAPSHOT)
    print(f"copied {source} to {SNAPSHOT.relative_to(ROOT)}; now run scripts/generate.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
