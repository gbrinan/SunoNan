# Advanced Prompt Techniques

Load when the task needs emotion arcs, duets, special vocal effects, or Suno V5/V5.5 platform features.

## Emotion-arc tags (verified)

`[Sad Verse]` `[Angry Verse]` `[Triumphant Chorus]` - contrasting emotions per section create a dramatic arc.

## Parentheses - the one legitimate use

- Chorus/ad-lib lyrics in `(parentheses)` are sung 100% of the time.
- Vocal-tone directions in parentheses are recognized only ~30% of the time; if used, place them alone directly under `[Intro]`.
- Everything else non-lyric: square brackets. No exceptions.

## Special vocal effects

- Stutter: `I-I-I love you` - vocal-chop effect
- Stretch: `lo-oo-ong vowels`, `Ooo-ooo-ooh` - dramatic holds
- Intensity: CAPS + exclamation (`NEVER GIVE UP!`)
- Sound effects: `*gunshots*`, `*thunder*`, `*rain falling*`
- Melodic spelling: `L-O-V-E`

## Prompt engineering

**Three-element formula:** `[Genre: House] [Influence: Afrobeat percussion] [Signature: call-and-response hook]`

**Specific beats vague:**
- "make a chill song" becomes "create an ambient electronic track for an introspective moment in a short film"
- "old song" becomes "1950s doo-wop"
- "electronic music" becomes "80s synth pop"

**Duets:** tag lyrics with `[Male Voice]` / `[Female Singer]`; add "male and female voices", "emotional duet" to Styles.

**Order matters:** Suno reflects earlier requests first.

## Space & production phrases

- Space: "Add subtle room reverb", "Create a small jazz club atmosphere", "Let the sound feel close and personal"
- Dynamics: "Let the mix breathe", "Build intensity gradually toward the end"
- Separation: "Keep clear separation between instruments", "Focus on clarity rather than loudness"
- Structure/length: "Make the intro longer", "Let the outro fade slowly and emotionally"

## Suno V5.5 platform features (as of 2026-08)

v5.5 (released 2026-03-26) added creation features on top of V5; prompt syntax (structure tags, Styles limits) is unchanged.

- Voices: record or upload your own audio to sing on your creations (Pro/Premier; voice is private to the uploader)
- Custom Models: upload 6+ of your tracks to train a personalized v5.5 that knows your sound
- My Taste: learns your go-to genres/moods/references and applies them via the Magic Wand
- Duration slider: pick song length in the Create form (web, v5.5 model)
- Lyricist: save lyrical style examples, natural-language lyric editing, full-screen editor

## Suno V5 Studio

- Stem export: drums/bass/vocals/synth as separate WAVs
- Remove FX: export dry stems without reverb
- Warp Markers: fix timing on the waveform without pitch shift
- Alternates: preview multiple generations, pick one
- Time Signature: 3/4, 7/8, 5/4 and other non-standard meters
- Remix: change genre while keeping melody/lyrics
- Extend: lengthen from a timestamp
- V4.5+ tools: Add Vocals, Add Instrumentals, Inspire

## Mistakes to avoid

1. Staying in Simple Mode - Custom Mode is required for direct control
2. Vague prompts - see "specific beats vague" above
3. Commercial-rights timing - a Premier plan applies from generation time onward
4. Changing many things at once - iterate one element per regeneration
5. Skipping structure tags - untagged songs get random structure
6. Putting mood in [brackets] inside lyrics - mood belongs in the Styles field
