#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/Users/admin/.openclaw/workspace"
cd "$REPO_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "not-a-git-repo"
  exit 0
fi

git add -A
if git diff --cached --quiet; then
  echo "no-changes"
  exit 0
fi

STAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
git commit -m "chore: heartbeat auto-git-sync ${STAMP}" >/dev/null 2>&1 || true

git push >/dev/null 2>&1

echo "pushed"
