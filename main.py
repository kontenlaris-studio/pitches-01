#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single one-line pitch to /output/entry.txt. Stdlib only,
deterministic, no network.
"""

import os

PITCH = (
    "Small clinics lose $12,000 a year to empty chairs - "
    "NoShowGuard texts each patient at the hour they're most likely "
    "to confirm, then backfills the slot before the visit is lost."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")
    print(f"wrote /output/entry.txt ({len(PITCH)} characters)")


if __name__ == "__main__":
    main()
