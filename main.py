#!/usr/bin/env python3
"""The Funniest Toaster Error Message — rebuilt.

The toaster reports a missing ingredient under a bureaucratic error
code, then confesses it has unionised and is declining breakfast.
Deadpan first, absurd second, punch on the last word.

This rebuild assembles the message from labelled parts instead of one
long literal, so each clause can be checked on its own. Same words
reach the output file; only the plumbing changed.

Writes the message to /output/entry.txt. Stdlib only, no network.
"""

import os

CODE = "ERROR 410"
MISSING = "Bread not found."
REFUSAL = "The toaster has unionised and declines to participate in breakfast."

GATE = 120


def assemble_message() -> str:
    """Join the error code, the missing item and the refusal."""
    return " ".join((CODE + ":", MISSING, REFUSAL))


def check_error_message(text: str) -> None:
    """Check the message reads as a toaster error, not a generic joke."""
    assert text.startswith("ERROR "), "message must open with an error code"
    assert "Bread not found" in text, "message must name the missing item"
    assert text.endswith("breakfast."), "punch must land on the last word"


def main() -> None:
    text = assemble_message()
    check_error_message(text)
    assert 1 <= len(text) <= GATE, "message must fit the 1-120 gate"
    assert "\n" not in text, "message must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
