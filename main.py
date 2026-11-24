"""One-Line Robot Wedding Vows.

Writes a single original robot wedding vow, one line, to entry.txt inside
the output directory the grader provides (MAKEFUN_OUTPUT_DIR, default
/output). Deterministic: the same line every run, no input, no network,
no randomness.
"""

import os

VOW = (
    "I take you to be my lawfully wedded co-processor, to have and to hold "
    "in sickness and in low battery, till factory reset do us part."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-160 characters, one line.
    assert 1 <= len(VOW) <= 160, "vow must be 1-160 characters"
    assert "\n" not in VOW, "vow must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
