# Build notes

- Read the kit's RULES.txt and competition.yaml first; the judge weighs, in order: office subject, earned laugh (turn/payoff at the end), specific office detail, freshness, tightness.
- v1: "think outside the box / moved my desk into the hallway" joke. Ran clean locally (90 chars, valid) but the setup is a cliché, weak on the freshness criterion.
- Revision: rewrote the joke around the reply-all thread — a specific office detail with a self-inflicted twist that pays off in the last few words ("one email at a time").
- Final test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py` — `out/entry.txt` holds one line, 115 characters (116 bytes incl. trailing newline), within 1–200, not whitespace-only, valid UTF-8.
- `main.py` is Python stdlib only, honours `MAKEFUN_OUTPUT_DIR`, asserts the 1–200 character gate before writing.
- Not submitted; no repo created; no contact with make.fun.
