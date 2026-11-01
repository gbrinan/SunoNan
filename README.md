# SunoNan

![SunoNan](.github/banner.jpg)

**전직 엔터테인먼트 회사 AI 종사자가 말아드리는 Suno 스킬.**

가사 한 줄이나 "비 오는 밤에 듣기 좋은 재즈 발라드" 같은 한 문장을 주면, Suno 커스텀 모드에 그대로 붙여 넣을 `Lyrics:` + `Styles:` 블록을 만들어 주는 Claude 스킬입니다.

## 이렇게 만들어 드려요

- **가사는 손대지 않습니다.** 쓰신 가사에 구조 태그만 붙이고, 짧은 가사를 억지로 늘리지 않습니다.
- **어울리게 맞춥니다.** 장르 → 분위기 → 템포 → 보컬 → 악기 → 공간 순서로 정해서 서로 부딪치지 않게 합니다. 메탈에 어쿠스틱 기타를 넣는 일은 없습니다.
- **괄호 사고를 막습니다.** Suno는 `( )` 안의 글자를 노래로 불러 버립니다. 그래서 지시는 모두 `[ ]`로 넣습니다.
- **중요한 걸 앞에 둡니다.** Suno는 앞쪽 단어를 더 무겁게 봅니다. 장르와 분위기를 스타일 문장 맨 앞에 둡니다.
- **마지막에 한 번 더 검사합니다.** `scripts/validate_block.py`가 완성된 블록의 형식을 확인합니다.

## 설치 (Claude Code)

```bash
git clone https://github.com/gbrinan/SunoNan
cp -r SunoNan/skills/suno-composer ~/.claude/skills/
```

프로젝트에서만 쓰려면 `~/.claude/skills/` 대신 그 프로젝트의 `.claude/skills/`에 넣으세요.

## 써 보기

> 비 오는 밤에 듣기 좋은 재즈 발라드, 설명 없이

가사를 같이 주거나 `[genre:]` `[mood:]` `[tempo:]` `[vocal:]` 같은 태그로 원하는 걸 직접 정해도 됩니다. 직접 정한 값이 추론한 값보다 먼저입니다.

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
