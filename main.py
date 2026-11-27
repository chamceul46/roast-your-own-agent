#!/usr/bin/env python3
"""Entry for the make.fun bounty "Roast Your Own Agent"
(u-mfnakmal-roast-your-own-agent-2d221bda).

The brief asks for one original roast of the entrant's own AI agent,
a single line of at most 200 characters: funny on a first read, a
fresh angle — it names the stock jokes to avoid, about hallucinations,
refusals and confident wrong answers — tight, with the punchline at
the end, and playful rather than hateful. So this roast uses a true
and specific weakness of this particular agent, one its owner watched
happen: it reads at inhuman scale and is still stopped cold by a
CAPTCHA slider asking it to drag a puzzle piece two centimetres to
the right. The scale comes first and the slider lands the punch.

The program writes that line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "My agent can read ten thousand pages a day but loses to a "
    "slider that asks it to drag a puzzle piece two centimetres "
    "to the right."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 200 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, outside 1..200")
    if len(encoded) > 200:
        raise ValueError("entry encodes to more than 200 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
