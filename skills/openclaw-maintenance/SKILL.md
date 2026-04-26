---
name: openclaw-maintenance
description: Run post-upgrade, health, maintenance, or drift checks for OpenClaw itself. Use when asked to verify an OpenClaw upgrade, audit OpenClaw status, review cron/task/memory health, inspect release notes for useful new features, or propose safe maintenance improvements.
---

# OpenClaw Maintenance

Use this for OpenClaw post-upgrade checks and routine platform maintenance.

## Rules

- Default to read-only checks first.
- Ask before state-changing actions: config edits, cron updates, task cleanup, service restarts, installs, firewall changes, file writes, or skill edits.
- Prefer OpenClaw first-class tools and CLI commands over ad hoc filesystem edits.
- Redact tokens, personal details, channel secrets, and host identifiers in user-facing output.
- In group chats, avoid surfacing private memory or personal data.
- Keep user reports concise: good, needs attention, actions taken, approvals needed.

## Read-only baseline

Run the smallest useful set, expanding only when needed:

```bash
openclaw --version
openclaw status
openclaw status --deep
openclaw security audit --deep
openclaw update status
openclaw health --json
openclaw memory status
openclaw tasks audit
```

Also inspect cron with the `cron` tool:

- `status`
- `list` with disabled jobs included
- `runs` for any failed jobs

For host posture, use the healthcheck skill if the user asks for hardening or host security. Otherwise only note obvious signals from OpenClaw audit.

## Post-upgrade review

Check local release notes before recommending changes:

```bash
grep -n "^## " "$OPENCLAW_PACKAGE/CHANGELOG.md" | head
```

If `$OPENCLAW_PACKAGE` is unknown, resolve the installed package path from the `openclaw` binary or `npm root -g`.

Focus on changes that affect current operations:

- cron and heartbeat behavior
- session and subagent behavior
- ACP/Codex routing
- memory/search/dreaming
- browser automation
- messaging delivery
- security audit findings
- image/media generation
- plugin startup and runtime deps

## Common safe fixes

Require approval, then apply one step at a time:

- Memory dirty: `openclaw memory index --force --agent main`
- Task maintenance preview says apply: `openclaw tasks maintenance --apply`
- Cron timeout after one isolated failure: increase that job's `payload.timeoutSeconds`, do not rerun unless asked.
- Stale failed cron state after a known fixed config: leave state until next run unless user asks to run now.
- Security audit `--fix`: only with explicit approval, and explain it changes OpenClaw defaults/file permissions only, not host firewall or SSH.

## Escalate instead of editing manually

Do not directly edit OpenClaw internal stores unless the user explicitly asks and there is a backup/rollback plan. This includes task databases, cron JSON, auth stores, and session stores.

## Final report format

Use short bullets:

- Version/update status
- Health/channel status
- Security summary
- Cron/task/memory status
- Changes made
- Remaining recommendations
- Next approval, if any
