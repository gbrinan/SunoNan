#!/usr/bin/env python3
"""Validate a Suno Composer final block.

Usage:
    python validate_block.py final_block.txt
    cat final_block.txt | python validate_block.py

Input: the raw final block text (the content that goes inside the fenced
code block), starting with "Lyrics:" and containing a "Styles:" section.

Exit 0 with "PASS" when clean; exit 1 with one line per violation.
"""
import re
import sys

MAX_TOTAL_CHARS = 1000  # Suno-safe length for the Styles prompt
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F000-\U0001F0FF"
    "\U00002600-\U000026FF\U0001F900-\U0001F9FF]"
)
# Meta-ish words that must never appear inside (parentheses): Suno sings them.
META_WORDS_RE = re.compile(
    r"\((?:[^)]*\b(intro|verse|chorus|bridge|outro|vocal|tempo|bpm|mood|style|genre|instrumental|whisper|fade)\b[^)]*)\)",
    re.IGNORECASE,
)
MD_RE = re.compile(r"(^#|\*\*|^- |^\d+\. |```)", re.MULTILINE)


def main() -> int:
    text = (
        open(sys.argv[1], encoding="utf-8").read()
        if len(sys.argv) > 1
        else sys.stdin.read()
    )
    errors = []

    if not text.lstrip().startswith("Lyrics:"):
        errors.append("Block must start with 'Lyrics:'")
    if "Styles:" not in text:
        errors.append("Block must contain a 'Styles:' section")

    lyrics, _, styles = text.partition("Styles:")

    if EMOJI_RE.search(text):
        errors.append("Emoji found inside the final block")
    if MD_RE.search(text):
        errors.append("Markdown formatting found inside the final block")

    m = META_WORDS_RE.search(lyrics)
    if m:
        errors.append(
            f"Parentheses used for meta info in lyrics: ({m.group(0)[1:-1]}) "
            "- use [square brackets]; Suno sings parenthesized text"
        )

    style_lines = [ln.strip() for ln in styles.strip().splitlines() if ln.strip()]
    if not 2 <= len(style_lines) <= 4:
        errors.append(f"Styles has {len(style_lines)} sentences; allowed range is 2-4")
    for i, line in enumerate(style_lines, 1):
        if not (line.startswith('"') and line.endswith('"')):
            errors.append(f"Styles line {i} is not wrapped in double quotes: {line[:50]}")
        if re.search(r"[가-힣぀-ヿ一-鿿]", line):
            errors.append(f"Styles line {i} contains non-English text")
    if len(styles) > MAX_TOTAL_CHARS:
        errors.append(f"Styles section is {len(styles)} chars; keep under {MAX_TOTAL_CHARS}")
    if text.count('"') % 2 != 0:
        errors.append("Unbalanced double quotes in block")
    for ch, name in (("[", "square"), ("(", "round")):
        close = {"[": "]", "(": ")"}[ch]
        if text.count(ch) != text.count(close):
            errors.append(f"Unbalanced {name} brackets")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"- {e}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
