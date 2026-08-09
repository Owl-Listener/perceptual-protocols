# tokens.md format spec

A `tokens.md` is a semantic annotation layer over a design system that already exists. It has seven sections. `## Source` is required; the rest are included only where your product has something to say.

## Top-level structure

```markdown
# tokens.md

## Source

| Format | Location |
|---|---|
| [Token format] | [Path or link to the real values] |

[Optional: one line on how theming/dark mode is resolved.]

## Color

### [Group]

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `color.group.role` | [value] | [where it belongs] | [where it doesn't] |

## Typography

| Token | Size | Weight | Line height | Use for | Do not use for |
|---|---|---|---|---|---|
| `type.role` | [size] | [weight] | [line height] | [where it belongs] | [where it doesn't] |

## Spacing

| Token | Value | Use for |
|---|---|---|
| `space.n` | [value] | [what relationship this expresses] |

**Rules**
- [Scale-level rule]

## Elevation

| Token | Value | Use for | Do not use for |
|---|---|---|---|

## Motion

| Token | Value | Use for | Do not use for |
|---|---|---|---|

**Rules**
- [Accessibility and performance rules]

## Radius

| Token | Value | Use for |
|---|---|---|
```

## Rules

**`## Source` comes first and is never omitted.** It is the section that keeps the file honest. An agent reading `tokens.md` should know immediately that this file carries intent and the linked source carries truth. Without it, `tokens.md` reads as a second source of values and starts competing with the real one.

**Token names are semantic, not descriptive.** `color.semantic.danger`, not `color.red.600`. If your system only has primitives, the mapping from primitive to semantic *is* the useful content of the file — write it down here even if it lives nowhere else yet.

**Every table row that can carry a "Do not use for" carries one.** This is the highest-value column in the file. `color.semantic.warning` used for errors is exactly the kind of plausible, confident, wrong choice an agent makes when it has values but no boundaries.

**"Do not use for" names a real temptation.** `color.surface.subtle` → *"Do not use for: primary content areas"* is useful, because that is a mistake someone would actually make. *"Do not use for: typography"* is filler. If you can't name a plausible misuse, leave the cell empty rather than padding it.

**Values may be elided, and often should be.** If your source of truth is linked and stable, `[from tokens.json]` in the value column is legitimate. The rules are the point. The more values you copy in, the faster the file rots.

**Delete sections you don't have.** A product with no elevation system should not ship a `## Elevation` section full of placeholders. Empty scaffolding reads to an agent as a system it should be using.

**Scale rules belong under the scale.** The `## Spacing` and `## Motion` sections each end with a short rules block, because the individual rows can't express the relationships — *use 1–4 within a component, 8–16 between sections* is the actual grammar, and no per-token row carries it.

## Handling dark mode and theming

Two options, and the choice depends on your system.

**If theming resolves automatically** — CSS custom properties, Figma modes, a `data-theme` attribute — say so once in `## Source` and give a single value column. The agent writes semantic token names and the platform handles the rest. This is the better path when it's available, because it keeps the file thin.

**If it doesn't**, add a `Dark` column beside the light values in the `## Color` tables, or a small light-to-dark mapping table at the end of the section. Note anything that inverts rather than translating — elevation and surface hierarchy usually behave differently in dark mode, and an agent that doesn't know will produce a light-mode layout with dark colours in it.

## Keeping it in sync

`tokens.md` is a derived document, and derived documents drift. Three habits that help:

1. **Point, don't copy.** Every value you duplicate is a value that can go stale.
2. **Put it next to the source.** If `tokens.md` lives in the same repository as `tokens.css`, a change to one is visible in review alongside the other.
3. **Treat a wrong value as a bug.** A stale hex in `tokens.md` will be propagated into generated UI with total confidence. That is a worse failure than a missing file, and it's the main argument for keeping the file thin.

## Relationship to motion-protocol

`tokens.md` and `motion.md` both describe motion, and the split is deliberate.

- `tokens.md` carries the **values**: `motion.duration.fast` is 150ms, the easing curve is `cubic-bezier(0.4, 0, 0.2, 1)`.
- `motion.md` carries the **character**: this product moves snappily, mechanically, invisibly.

An agent generating a transition needs both — the character to pick the right token, the value to write the CSS. Where the two disagree, that's a finding: either the brief moved on or the system did.
