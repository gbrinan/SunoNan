# Tasks

## Project Goal

Rewrite the "Suno Composer" Notion guide as a proper Claude Agent Skill
(`skills/suno-composer/`), following:

- Anthropic Agent Skills spec (SKILL.md + progressive disclosure)
- paperthin philosophy (remove noise, clean v0 rewrite, single source of truth)
- suno.com "How to make a song" guide (preserve verified good samples)

## Phases

### Phase 1: Repository setup ✅
- [x] Set up file-based planning workflow (tasks.md / findings.md / progress.md)
- [x] Create skill directory skeleton

### Phase 2: Skill rewrite ✅
- [x] Rewrite SKILL.md as lean instructions (English, <5k tokens body)
- [x] Move keyword dictionary to references/keywords.md (Level 3)
- [x] Move advanced techniques to references/techniques.md (Level 3)
- [x] Implement self-check as scripts/validate_block.py

### Phase 3: Ship 🔄
- [ ] Push branch, open PR
- [ ] Review feedback

## Decisions

| Decision | Rationale |
|---|---|
| Self-check as a script, not prose | Deterministic checks (brackets, quotes, length) belong in code; only output enters context |
| Notion keyword tables → references/ | Reference data is Level 3: zero token cost until needed |
| Preserve Suno hub sample prompts verbatim | Verified-good samples must survive the rewrite |
| SKILL.md in English | Skill instruction documents are English; Suno Styles are English-only anyway |

## Errors

| Error | Cause | Resolution |
|---|---|---|
| (none yet) | | |
