#!/usr/bin/env bash
set -euo pipefail

SRC_ROOT="/Users/admin/.openclaw/workspace"
DST_ROOT="/Users/admin/Documents/Clawhub/03-OpenClaw-Gateway"

mkdir -p "$DST_ROOT"/{00-Inbox,01-Daily,02-Projects,03-People,04-System,05-Summaries,90-Archive,.templates}

# Core profile/system files
[ -f "$SRC_ROOT/MEMORY.md" ] && cp "$SRC_ROOT/MEMORY.md" "$DST_ROOT/04-System/MEMORY-Core.md"
[ -f "$SRC_ROOT/USER.md" ] && cp "$SRC_ROOT/USER.md" "$DST_ROOT/04-System/USER-Profile.md"
[ -f "$SRC_ROOT/IDENTITY.md" ] && cp "$SRC_ROOT/IDENTITY.md" "$DST_ROOT/04-System/IDENTITY.md"
[ -f "$SRC_ROOT/SOUL.md" ] && cp "$SRC_ROOT/SOUL.md" "$DST_ROOT/04-System/SOUL.md"
[ -f "$SRC_ROOT/AGENTS.md" ] && cp "$SRC_ROOT/AGENTS.md" "$DST_ROOT/04-System/AGENTS.md"

# Daily memory notes
if [ -d "$SRC_ROOT/memory" ]; then
  find "$SRC_ROOT/memory" -maxdepth 1 -type f -name "*.md" | while read -r f; do
    base="$(basename "$f")"
    cp "$f" "$DST_ROOT/01-Daily/$base"
  done
fi

# Optional heartbeat state snapshot
if [ -f "$SRC_ROOT/memory/heartbeat-state.json" ]; then
  cp "$SRC_ROOT/memory/heartbeat-state.json" "$DST_ROOT/04-System/heartbeat-state.json"
fi

# Keep a basic sync stamp for quick checks
cat > "$DST_ROOT/04-System/last-sync.md" <<EOF
# Last Sync

🦞 Clawd: Synced from workspace.

- Source: 
  - /Users/admin/.openclaw/workspace
- Synced at (UTC): $(date -u +"%Y-%m-%d %H:%M:%S")
- Synced at (SGT): $(TZ=Asia/Singapore date +"%Y-%m-%d %H:%M:%S %Z")
EOF

echo "Sync complete: $DST_ROOT"
