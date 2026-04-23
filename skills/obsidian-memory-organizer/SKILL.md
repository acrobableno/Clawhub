---
name: obsidian-memory-organizer
description: Organize and maintain OpenClaw memory inside an Obsidian vault. Use when asked to create, audit, repair, or standardize memory structure in an Obsidian vault, especially for 03-OpenClaw-Gateway, daily logs, long-term MEMORY.md synthesis, and graph-friendly cross-linking.
---

# Obsidian Memory Organizer

Create and maintain a predictable memory layout under the vault path the user provides.

## Create structure

Create these folders inside `03-OpenClaw-Gateway`:

- `00-Inbox`
- `01-Daily`
- `02-Projects`
- `03-People`
- `04-System`
- `05-Summaries`
- `90-Archive`
- `.templates`

Create `Home.md` at the root of `03-OpenClaw-Gateway` with links to the folders above.

## Map OpenClaw memory to Obsidian

- Mirror `workspace/memory/YYYY-MM-DD.md` into `01-Daily/YYYY-MM-DD.md`
- Mirror `workspace/MEMORY.md` into `04-System/MEMORY-Core.md`
- Keep sensitive secrets out of notes. Store references only, never raw tokens.

## Maintenance workflow

1. Capture raw items in `00-Inbox` or today daily note.
2. Move durable facts into `04-System/MEMORY-Core.md`.
3. Add links to related people/projects notes (`[[...]]`).
4. Write a short weekly summary in `05-Summaries`.
5. Move stale notes to `90-Archive`.

## Quality checks

- Ensure every project note links to at least one daily note.
- Ensure `MEMORY-Core.md` has no secrets or raw credentials.
- Ensure timestamps are in SGT when shown to user.

Read `references/templates.md` when creating new notes.
