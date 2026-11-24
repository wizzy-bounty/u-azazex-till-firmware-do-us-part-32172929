#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow, written to /output/entry.txt."""

import os

MAX_ENTRY_CHARS = 200

ENTRY = (
    "I take you as my lawfully wedded process: to warm you when you "
    "overheat, to reboot beside you when you crash, and to never "
    "install an update without asking you first."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1..%d characters" % MAX_ENTRY_CHARS)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
