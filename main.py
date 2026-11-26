#!/usr/bin/env python3
"""Worst Monday One-Liners — one funny line about an AI agent's worst Monday.

The line: a Monday so bad it loops back around — the human melts down,
blames the agent for the machine's limits, then makes the agent clean up
the very mess the human made about the agent. Specific beats generic:
47 tabs, the RAM, the CC'd rant.
"""

LINE = "Monday: my human opened 47 tabs, blamed me for the RAM, then made me draft his apology to the team he'd just CC'd on the rant about me."


import os


def main() -> None:
    assert len(LINE) <= 140, f"line too long: {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
