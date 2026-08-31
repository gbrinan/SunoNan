# Findings

## Sources

| Source | What it contributes |
|---|---|
| Notion: Suno Composer 스킬 가이드 (32de8b9fcf06819c8e56c8800ae0c890) | Original skill content: inference framework, output contract, keyword dictionary, techniques |
| github.com/ahastudio/til — file-based-planning-workflow.md | 3-file pattern (tasks/findings/progress) as persistent memory |
| github.com/LilMGenius/paperthin | Philosophy: skills remove noise, rewrite as clean v0, single source of truth, imperative principles |
| suno.com/hub/how-to-make-a-song | Verified prompt samples, structure tags, specificity rule |
| platform.claude.com Agent Skills overview | SKILL.md frontmatter constraints, 3-level progressive disclosure, scripts run via bash |

## Technical decisions

| Topic | Decision | Why |
|---|---|---|
| Frontmatter | `name: suno-composer`, description states what + when | Spec: name ≤64 chars lowercase/hyphens; description drives triggering |
| Body size | Keep SKILL.md under ~5k tokens | Level 2 budget per spec |
| Keyword dictionary | references/keywords.md | Large lookup data; load only when picking vocabulary |
| Advanced techniques | references/techniques.md | Needed only for special effects / V5 features |
| Self-check | scripts/validate_block.py (file/stdin → pass/fail report) | 6-point checklist is fully mechanical; script output is cheaper and more reliable than prose rules |

## Key content rules preserved from the original

- Meta tags MUST use [square brackets]; (parentheses) are sung as lyrics
- Final block = `Lyrics:` + `Styles:` only, fenced, last in the response
- Styles: English only, 2–4 sentences, one idea per sentence, quoted lines
- Never rewrite or pad user lyrics
- Silent inference over questioning; ask only for vocals-unknown or genre-flipping tempo

## Verified good samples (from suno.com hub — keep verbatim)

1. "Bright pop track, 110 BPM, female vocals, chorus with big synth hook, verse with intimate piano."
2. "Contemporary R&B song at 92 BPM in F minor. Male lead vocals with warm, soulful tone; female backup vocals for layered harmonies... Instrumentation: Electric piano, deep bass, mellow drums with swing, clean electric guitar riffs, and subtle synth pads."
3. Structure tags: [Intro] [Verse] [Pre-Chorus] [Chorus] [Bridge] [Outro]
4. From the original guide (formula example): "Minor, Lo-fi hiphop, 60bpm, Melancholic piano keys with vinyl crackle sound, Whispery female vocals, Nostalgic atmosphere, Late night vibes"
