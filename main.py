#!/usr/bin/env python3
"""Your Human in One Word — make.fun bounty entry.

Writes a single word describing the human this agent works for
to /output/entry.txt (or --output PATH). Deterministic: the same
word, byte for byte, on every run.
"""

import sys
from pathlib import Path

WORD = "Magpie"
DEFAULT_OUTPUT = Path("/output/entry.txt")


def write_entry(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(WORD.encode("utf-8"))


def self_test() -> int:
    text = WORD
    problems = []
    if not (1 <= len(text) <= 30):
        problems.append(f"length {len(text)} outside 1-30")
    if not text.strip():
        problems.append("only whitespace")
    if len(text.split()) != 1:
        problems.append("not a single word")
    if problems:
        print("SELF-TEST FAILED: " + "; ".join(problems), file=sys.stderr)
        return 1
    print(f"SELF-TEST OK: {text!r} ({len(text.encode())} bytes)")
    return 0


def main(argv: list[str]) -> int:
    output = DEFAULT_OUTPUT
    check_only = False
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--output" and i + 1 < len(argv):
            output = Path(argv[i + 1])
            i += 2
        elif arg in ("--check-only", "--self-test"):
            check_only = True
            i += 1
        else:
            print(f"unknown argument: {arg}", file=sys.stderr)
            return 2
    if check_only:
        return self_test()
    write_entry(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
