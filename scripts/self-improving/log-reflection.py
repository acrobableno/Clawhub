#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

ROOT = Path('/Users/admin/.openclaw/workspace')
BASE = ROOT / 'self-improving'
JOURNAL = BASE / 'journal'


def sgt_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        if path.exists() and path.stat().st_size > 0:
            f.write('\n')
        f.write(text.rstrip() + '\n')


def main() -> None:
    p = argparse.ArgumentParser(description='Append a structured reflection entry')
    p.add_argument('--task', required=True)
    p.add_argument('--context', required=True)
    p.add_argument('--signal', required=True, choices=['win', 'mistake', 'correction'])
    p.add_argument('--lesson', required=True)
    p.add_argument('--next-move', required=True)
    p.add_argument('--also', nargs='*', choices=['wins', 'mistakes'])
    args = p.parse_args()

    now = sgt_now()
    day = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M')

    journal_file = JOURNAL / f'{day}.md'
    entry = (
        f"## {time_str} SGT - {args.task}\n"
        f"- Context: {args.context}\n"
        f"- Signal: {args.signal}\n"
        f"- Lesson: {args.lesson}\n"
        f"- Next move: {args.next_move}\n"
    )
    append(journal_file, entry)

    tag_line = f"- [{day}] {args.task}: {args.lesson}"
    for target in (args.also or []):
        append(BASE / f'{target}.md', tag_line)

    print(f'Logged reflection to {journal_file}')


if __name__ == '__main__':
    main()
