#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
from pathlib import Path
import re

ROOT = Path('/Users/admin/.openclaw/workspace')
BASE = ROOT / 'self-improving'
JOURNAL = BASE / 'journal'


def sgt_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))


def read_text(path: Path) -> str:
    if not path.exists():
        return ''
    return path.read_text(encoding='utf-8')


def parse_today_entries(day: str) -> list[dict[str, str]]:
    f = JOURNAL / f'{day}.md'
    text = read_text(f)
    if not text.strip():
        return []

    blocks = [b.strip() for b in re.split(r'\n(?=## )', text) if b.strip().startswith('## ')]
    out: list[dict[str, str]] = []
    for b in blocks:
        lines = b.splitlines()
        title = lines[0].replace('## ', '', 1).strip()
        item = {'title': title, 'lesson': '', 'next': '', 'signal': ''}
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('- Signal:'):
                item['signal'] = line.replace('- Signal:', '', 1).strip()
            elif line.startswith('- Lesson:'):
                item['lesson'] = line.replace('- Lesson:', '', 1).strip()
            elif line.startswith('- Next move:'):
                item['next'] = line.replace('- Next move:', '', 1).strip()
        out.append(item)
    return out


def tail_lines(path: Path, n: int = 3) -> list[str]:
    text = read_text(path)
    lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith('- ')]
    return lines[-n:]


def main() -> None:
    now = sgt_now()
    day = now.strftime('%Y-%m-%d')
    entries = parse_today_entries(day)

    print(f"🦞 Clawd Daily Self-Reflection ({day}, SGT)")

    if not entries:
        print('- No reflection entries logged yet today.')
    else:
        print('- Today\'s reflection highlights:')
        for e in entries[-5:]:
            lesson = e['lesson'] or 'No lesson captured.'
            signal = e['signal'] or 'signal-unknown'
            print(f"  - [{signal}] {e['title']}: {lesson}")

    hot = tail_lines(BASE / 'HOT.md', 4)
    if hot:
        print('- Current HOT rules:')
        for h in hot:
            print(f'  {h}')

    recent_patterns = tail_lines(BASE / 'patterns.md', 3)
    if recent_patterns:
        print('- Recent promoted patterns:')
        for p in recent_patterns:
            print(f'  {p}')

    print('- How to work with me better:')
    print('  - Give explicit corrections when something is off, I log and adapt faster.')
    print('  - State durable preferences as "always/never" so I can promote them safely.')
    print('  - For multi-step tasks, tell me your preferred output format up front.')


if __name__ == '__main__':
    main()
