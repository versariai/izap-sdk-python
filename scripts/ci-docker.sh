#!/usr/bin/env bash
# Run scripts/ci.sh inside the pinned uv image. Buildkite agents are containers driving the
# host Docker daemon, so a bind mount would be an empty host dir: copy the SDK in instead.
set -euo pipefail

repo="$(cd "$(dirname "$0")/../../.." && pwd)"
# uv publishes no versioned bookworm tags, so pin the floating tag by digest.
image="${SDK_PYTHON_UV_IMAGE:-ghcr.io/astral-sh/uv:python3.13-bookworm@sha256:47965cdc9d53a515f68f78241161c901e70051ce428f12e791bd7fe19f6a631a}"

cid="$(docker create -w /sdk/python "$image" bash scripts/ci.sh)"
trap 'docker rm -f "$cid" >/dev/null 2>&1 || true' EXIT

echo "--- :python: Copying sdk/python into $image"
# The committed tree, as CI checks it out. git builds the tar, so the agent's (busybox) tar never runs.
git -C "$repo" archive --format=tar HEAD sdk/python | docker cp - "$cid:/"

echo "--- :python: Python SDK gate"
docker start -a "$cid"
