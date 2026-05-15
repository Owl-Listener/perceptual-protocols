# mood.md Protocol Specification

**Version:** 0.1.0

## Overview

`mood.md` is a structured markdown file that encodes visual design direction 
in a format any AI agent can consume. It is the perceptual counterpart to 
procedural skill files (`SKILL.md`), providing aesthetic intent alongside 
craft knowledge.

## Filename & Location

- **Filename:** `mood.md`
- **Location:** Project root, or within a named subdirectory for multi-mood projects
- **Encoding:** UTF-8

## Required Sections

A conformant `mood.md` MUST include these sections:

### `# Mood: [Name]`
Top-level heading with the mood's name.

### `## Essence`
2-3 sentences capturing the overall feeling. Must be specific and evocative — 
actionable creative direction, not generic descriptors.

### `## Colour`
Must include:
- **Temperature** (warm / cool / neutral + nuance)
- **Palette** (hex values with semantic names)
- **Contrast** (high / medium / low + usage)
- **Saturation** (vivid / muted / desaturated + character)

### `## Typography`
Must include:
- **Character** (the typographic personality)
- **Weight distribution** (how weight creates hierarchy)
- **Density** (airy / balanced / compact)

### `## Space & Layout`
Must include:
- **Rhythm** (spatial pattern)
- **Scale relationships** (how size creates hierarchy)

### `## Emotional Register`
A short paragraph describing how someone should *feel* when experiencing 
the designed thing. Cultural touchpoints encouraged.

### `## Agent Instructions`
A concise, actionable paragraph written directly to an AI agent, explaining 
how to apply this mood when generating code, choosing colours, writing CSS, 
or making any design decision.

## Optional Sections

### `## Texture & Material`
Surface quality, material references, finish.

### `## Design Principles`
3-5 short principles extracted from the mood, formatted as:
**Principle name** — one-sentence explanation.

### `## References`
Per-image notes on what each source image contributes.

### `## Anti-References`
Things this mood explicitly is NOT. Equally important as positive direction.

### `## Motion` (future)
Reserved for animation, transition, and interaction mood.

### `## Sound` (future)
Reserved for sonic/audio mood direction.

## Conventions

- Hex colour values should be lowercase: `#1a1a2e` not `#1A1A2E`
- Colour names should be semantic: `"deep night"` not `"dark blue"`
- Anti-references may be signalled in source material by filenames 
  prefixed with `not-` or `anti-`
- Designer annotations from source material (visible sticky notes, 
  handwritten labels) should be preserved as direct quotes

## Multi-Mood Projects

Projects may contain multiple mood files:

```
moods/
  brand/mood.md
  dark-mode/mood.md
  onboarding/mood.md
```

Each mood file is self-contained and independently valid.

## Versioning

This spec follows semver. The version is declared at the top of this document.
Generator tools should include the spec version in a comment at the end 
of generated files:

```markdown
<!-- mood-protocol v0.1.0 -->
```

## Relationship to Other Protocols

| Protocol | Purpose | Domain |
|----------|---------|--------|
| `SKILL.md` | Procedural knowledge — how to build | Craft |
| `mood.md` | Perceptual direction — how it should feel | Aesthetics |
| `.cursorrules` / `CLAUDE.md` | Agent behaviour configuration | Process |

`mood.md` is complementary to all of the above. It provides the aesthetic 
layer that procedural and behavioural files cannot express.
