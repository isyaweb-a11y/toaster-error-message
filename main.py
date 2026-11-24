#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

The entry is the error message a kitchen toaster shows its owner when
something goes wrong. The judge wants a real error message, fresh
surprise, tight wording and one clear appliance voice that lands on a
single read.

The joke avoids the obvious burnt-toast puns entirely: the toaster
reports a missing ingredient with a bureaucratic error code, then
confesses it has unionised and is declining breakfast. Deadpan first,
absurd second, and the punch lands on the last word.

Writes the message to /output/entry.txt. Stdlib only, no network.
"""

import os

TEXT = (
    "ERROR 410: Bread not found. "
    "The toaster has unionised and declines to participate in breakfast."
)

# The gate allows 1 to 120 characters.
MAX_CHARS = 120


def entry_text() -> str:
    """Return the error message, checked against the bounty's own rules."""
    text = TEXT.strip()
    assert text and not text.isspace(), "the entry must not be blank"
    assert len(text) <= MAX_CHARS, "the entry must fit the gate"
    assert "\n" not in text, "the entry must be a single line"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
