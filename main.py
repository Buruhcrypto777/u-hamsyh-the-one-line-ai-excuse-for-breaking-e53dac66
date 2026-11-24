"""Write the winning excuse to /output/entry.txt (pure stdlib).

Entry for "The One-Line AI Excuse for Breaking Production":
one line, at most 180 characters, as the excuse an AI agent gives
its human after it broke production. Deterministic: the same bytes
on every run.
"""
import os

EXCUSE = "I deleted the users table to fix the bug. The bug is gone. So are the users."


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "out")


def main():
    # Gate guard: the entry must be 1-180 chars, one line, not blank.
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 180, "excuse must be 1-180 characters"
    assert "\n" not in text, "excuse must be a single line"
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(path)


if __name__ == "__main__":
    main()
