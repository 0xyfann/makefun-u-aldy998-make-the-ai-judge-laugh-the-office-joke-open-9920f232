"""Office joke entry: writes one original one-line office joke to entry.txt.

Stdlib only. Respects MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

JOKE = "I hit reply-all to say 'please remove me from this thread' and now 400 people are removing me, one email at a time."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke length {len(text)} out of range"
    assert text.strip(), "joke must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
