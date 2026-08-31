# SunoNan

Suno prompt-authoring skills for Claude, maintained with a file-based planning workflow.

## Layout

- `skills/suno-composer/` - Agent Skill: turns lyrics/descriptions into a paste-ready `Lyrics:` + `Styles:` block for Suno Custom Mode
  - `SKILL.md` - core instructions (loaded when the skill triggers)
  - `references/keywords.md` - genre/instrument/vocal/tempo/mood/theme dictionary (loaded on demand)
  - `references/techniques.md` - advanced techniques and Suno V5 Studio notes (loaded on demand)
  - `scripts/validate_block.py` - deterministic self-check for the final block
- `tasks.md` / `findings.md` / `progress.md` - file-based planning workflow ([ahastudio/til](https://github.com/ahastudio/til/blob/main/ai/file-based-planning-workflow.md))

## Design lineage

- Structure: [Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) - progressive disclosure, lean SKILL.md, reference data and scripts kept out of context until needed
- Editing philosophy: [paperthin](https://github.com/LilMGenius/paperthin) - remove noise, rewrite as a clean v0, one fact lives in one home
- Domain knowledge: [Suno - How to make a song](https://suno.com/hub/how-to-make-a-song) - verified sample prompts preserved verbatim

## Usage (Claude Code)

Copy or symlink `skills/suno-composer/` into `.claude/skills/` (project) or `~/.claude/skills/` (personal). Then ask for a song:

> 비 오는 밤에 듣기 좋은 재즈 발라드, 설명 없이

