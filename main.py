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


def validate_word(text: str) -> None:
    """Enforce the bounty gate: one token, 1-30 chars, non-whitespace."""
    if not (1 <= len(text) <= 30) or text.strip() != text or len(text.split()) != 1:
        raise ValueError(f"invalid entry word: {text!r}")


def write_entry(path: Path) -> None:
    validate_word(WORD)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(WORD.encode("utf-8"))


def self_test() -> int:
    try:
        validate_word(WORD)
    except ValueError as exc:
        print(f"SELF-TEST FAILED: {exc}", file=sys.stderr)
        return 1
    print(f"SELF-TEST OK: {WORD!r} ({len(WORD.encode())} bytes)")
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
