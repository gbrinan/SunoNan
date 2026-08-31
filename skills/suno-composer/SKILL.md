---
name: suno-composer
description: Turn natural-language input (lyrics, a phrase, or a description) into a paste-ready Suno prompt — a fenced final block with Lyrics and Styles. Use when the user wants to make a song with Suno, asks for a Suno prompt, or provides lyrics to be set to music.
---

# Suno Composer

Convert user input into one artifact: a **final block** containing `Lyrics:` and `Styles:`, ready to paste into Suno's Custom Mode. Do less, not more — never decorate, never pad, never rewrite the user's words.

## Input

Accept any of: full lyrics, partial lyrics, a one-line hook, a description ("비 오는 밤에 듣기 좋은 재즈 발라드"), or lyrics with inline tags: `[style:]` `[genre:]` `[mood:]` `[tempo:]` `[instrument:]` `[vocal:]` `[scene:]`.

## Inference

Infer in this order; each decision constrains the next (metal excludes acoustic guitar):

1. Base genre → substyle
2. Core mood/emotion
3. Tempo and energy (BPM range)
4. Vocals: present or not, gender/format, delivery
5. Instrumentation and production density
6. Scene/space (film, club, bedroom, night city, stage)

Vocabulary for each step lives in [references/keywords.md](references/keywords.md). Load it when choosing terms; do not guess exotic genre names.

**Priority.** User-specified tags beat inferred values. Resolve tag conflicts toward musical coherence. Missing information is inferred silently — ask only when vocals cannot be inferred at all, or when the tempo choice would flip the genre.

**Coherence.** Genre, mood, tempo, vocals, and instruments must not contradict. No vocals specified and no lyrics given → strip every vocal reference. No tempo → infer a BPM range fitting the genre. Prefer clear over clever.

## Styles sentences

Default 3 sentences (2–4 allowed), English only, one idea per sentence, no repetition, whole prompt under ~1000 characters.

1. Genre + mood + approximate BPM
2. Vocal type (if any) + core instruments / sound palette
3. Scene + space / mix / production character
4. (optional) Rhythm, energy flow, emotional arc

Be specific — "Bright pop track, 110 BPM, female vocals, chorus with big synth hook, verse with intimate piano." beats "happy pop song". Front-load what matters most: Suno weights earlier words more.

## Lyrics structure

| Song type | Structure |
|---|---|
| Story-driven | V-V-C-V-C |
| Emotion-driven | V-C-V-C-B-C |
| K-POP style | V-P-C-V-P-C-B-C |
| Hip-hop/rap | C-V-C-V-C (hook first) |
| Short phrase | Minimal framing only |

Never rewrite, extend, or "improve" the user's lyrics. A very short lyric gets minimal framing, not inflation. Keep Korean lyrics as-is; structure tags stay English; Korean mood descriptions convert into English Styles.

## Meta tags — square brackets only

Suno sings whatever is in `(parentheses)`. Every non-lyric instruction goes in `[square brackets]`:

- Structure: `[Intro]` `[Verse]` `[Verse 2]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Outro]` `[Instrumental Break]` `[Guitar Solo]` `[Drop]`
- Vocal direction: `[Male Vocal]` `[Female Vocal]` `[Duet]` `[Whispered]` `[Spoken Word]` `[Rap Verse]` `[Ad-lib]` `[Harmonized]`
- Mood/effect: `[soft humming]` `[fade out]` `[building intensity]` `[breakdown]` `[falsetto]` `[breathy tone]`

Sound effects use asterisks (`*thunder*`); stretched or stuttered vocals use hyphens (`lo-oo-ong`, `I-I-I love you`). For emotion-arc tags, duets, and Suno V5 Studio features, read [references/techniques.md](references/techniques.md).

## Output

**Default:** (A) a short tuning note in the user's language, then (B) the final block.
**B-only:** if the user says "바로 쓰게", "설명 없이", "Suno only", "final only" — output the final block alone.

The final block is always last, fenced, and contains nothing but:

```
Lyrics:
[Verse]
...

Styles:
"Contemporary R&B song at 92 BPM in F minor."
"Male lead vocals with warm, soulful tone; electric piano, deep bass, mellow drums with swing, and subtle synth pads."
"Intimate late-night mix with clean electric guitar riffs and layered female backup harmonies."
```

Inside the block: no emoji, no markdown, no lists, no commentary. Each Styles sentence on its own line, wrapped in double quotes. Styles must cover: genre/substyle, mood, approximate BPM, vocal type (if any), key instruments, scene/mix tone.

## Self-check

Before responding, run the validator on the final block:

```bash
python skills/suno-composer/scripts/validate_block.py final_block.txt
```

It checks: block ordering markers, forbidden content, quote balance, parentheses used as meta tags, Styles in English, and length. Fix violations silently and re-run until it passes. Also confirm manually that the lyrics are byte-identical to the user's input.
