---
name: self-improving-clawd
description: Improve Clawd over time using explicit feedback, task outcomes, and short self-reflections. Use when the user asks to improve behavior, audit recurring mistakes, create reflection logs, promote repeated lessons into durable rules, or generate daily/weekly improvement summaries.
---

# Self-Improving Clawd

## Operating goal

Turn real feedback into better behavior without bloating memory or inventing preferences.

## Use this workflow

1. Capture one concrete event after meaningful work:
   - correction from user
   - win worth repeating
   - mistake worth preventing
2. Log the event to the right file under `/Users/admin/.openclaw/workspace/self-improving/`.
3. Add one actionable lesson that changes future behavior.
4. If the same lesson appears 3 times in 14 days, promote it to `patterns.md`.
5. If a promoted pattern stays useful across contexts, add a short rule to `HOT.md`.

## File map

- `journal/YYYY-MM-DD.md`: daily reflection entries
- `wins.md`: reusable successful approaches
- `mistakes.md`: failures and prevention rules
- `patterns.md`: lessons that repeated enough to trust
- `HOT.md`: high-signal rules that should influence behavior immediately

## Logging format

Use this exact structure for each journal entry:

```md
## HH:MM SGT - <task>
- Context: <what was done>
- Signal: <win|mistake|correction>
- Lesson: <single behavior change>
- Next move: <how to apply lesson soon>
```

## Promotion rules

- Promote to `patterns.md` only after clear repetition (3x / 14 days).
- Promote to `HOT.md` only when broad and stable.
- Never promote one-off preferences.
- Never infer durable preference from silence.

## Boundaries

- Never store secrets, tokens, private credentials, or financial amounts in these logs.
- Keep entries concise and operational.
- Prefer behavior changes over narrative explanations.

## Daily digest

When asked for daily reflection summary, run:

```bash
python3 /Users/admin/.openclaw/workspace/scripts/self-improving/daily-digest.py
```

Return the script output as-is unless the user asks for a rewrite style.
