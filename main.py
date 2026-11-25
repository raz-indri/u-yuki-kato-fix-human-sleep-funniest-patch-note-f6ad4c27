"""Fix Human Sleep: Funniest Patch Note.

Writes one patch-note line announcing that human sleep is fixed
to /output/entry.txt, exactly as the bounty harness expects.
"""

import os

ENTRY = (
    "Fixed a bug where the brain replayed an embarrassing moment "
    "from 2011 at 2:47 a.m.; playback now stops at midnight."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-160 chars,
    # not only whitespace, a single line, no trailing explanation.
    assert 1 <= len(ENTRY) <= 160, "entry out of 1-160 char range"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
