# tokens.md

> Place this file at the root of your project. Reference it in your agent context, system prompt, or workflow brief.

---

## Source

Where your token values live. Agents should read this file for intent and the source for values.

| Format | Location |
|---|---|
| [e.g. Figma variables] | [e.g. link to Figma file] |
| [e.g. CSS custom properties] | [e.g. src/styles/tokens.css] |
| [e.g. Tailwind config] | [e.g. tailwind.config.ts] |
| [e.g. JSON tokens] | [e.g. tokens/tokens.json] |

---

## Color

Semantic color roles. Use the semantic name when generating UI — not the primitive value.

### Surface

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `color.surface.default` | [e.g. #ffffff] | Page and panel backgrounds | Interactive elements |
| `color.surface.subtle` | [e.g. #f9fafb] | Secondary backgrounds, zebra rows | Primary content areas |
| `color.surface.raised` | [e.g. #ffffff + shadow] | Cards, dropdowns, modals | Flat page sections |

### Content

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `color.content.primary` | [e.g. #111827] | Body text, headings | Disabled states |
| `color.content.secondary` | [e.g. #6b7280] | Supporting text, labels, captions | Primary actions |
| `color.content.disabled` | [e.g. #d1d5db] | Disabled text | Any active state |
| `color.content.inverse` | [e.g. #ffffff] | Text on dark/filled surfaces | Light backgrounds |

### Interactive

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `color.interactive.primary` | [e.g. #2563eb] | Primary buttons, key links, focus rings | Backgrounds |
| `color.interactive.primary.hover` | [e.g. #1d4ed8] | Hover state of primary interactive | Default state |
| `color.interactive.secondary` | [e.g. #e5e7eb] | Secondary buttons, ghost fills | Primary actions |

### Semantic

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `color.semantic.danger` | [e.g. #dc2626] | Destructive actions, error states | Warnings |
| `color.semantic.warning` | [e.g. #d97706] | Cautionary states, non-critical alerts | Errors |
| `color.semantic.success` | [e.g. #16a34a] | Completion, confirmation, positive states | Neutral info |
| `color.semantic.info` | [e.g. #2563eb] | Neutral informational states | Actions |

### Dark mode

| Light token | Dark equivalent | Notes |
|---|---|---|
| `color.surface.default` | [e.g. #111827] | [e.g. Invert surface hierarchy in dark] |
| `color.content.primary` | [e.g. #f9fafb] | |

*If your token system handles dark mode automatically (e.g. via CSS variables or Figma modes), note that here and omit the table.*

---

## Typography

Type scale with semantic labels. Use the label when specifying text styles — not the raw size.

| Token | Size | Weight | Line height | Use for | Do not use for |
|---|---|---|---|---|---|
| `type.display` | [e.g. 48px] | [e.g. 700] | [e.g. 1.1] | Hero headings, large feature text | Body content |
| `type.heading.1` | [e.g. 32px] | [e.g. 700] | [e.g. 1.2] | Page titles | Section subheadings |
| `type.heading.2` | [e.g. 24px] | [e.g. 600] | [e.g. 1.3] | Section headings | Page titles |
| `type.heading.3` | [e.g. 20px] | [e.g. 600] | [e.g. 1.4] | Card titles, subsections | Primary headings |
| `type.body.default` | [e.g. 16px] | [e.g. 400] | [e.g. 1.5] | Body text, descriptions | Headings, labels |
| `type.body.small` | [e.g. 14px] | [e.g. 400] | [e.g. 1.5] | Secondary body, supporting text | Primary body content |
| `type.label` | [e.g. 12px] | [e.g. 500] | [e.g. 1.4] | Form labels, tags, badges | Body text |
| `type.code` | [e.g. 14px mono] | [e.g. 400] | [e.g. 1.6] | Code blocks, technical strings | UI labels |

**Typefaces**

| Role | Family | Fallback |
|---|---|---|
| [e.g. Display / heading] | [e.g. Inter] | [e.g. system-ui, sans-serif] |
| [e.g. Body] | [e.g. Inter] | [e.g. system-ui, sans-serif] |
| [e.g. Monospace] | [e.g. JetBrains Mono] | [e.g. monospace] |

---

## Spacing

Spacing scale with intent. Match the scale level to the relationship being expressed.

| Token | Value | Use for |
|---|---|---|
| `space.1` | [e.g. 4px] | Icon internal padding, tight inline gaps |
| `space.2` | [e.g. 8px] | Component internal padding (compact) |
| `space.3` | [e.g. 12px] | Component internal padding (default) |
| `space.4` | [e.g. 16px] | Default component padding, gap between related elements |
| `space.5` | [e.g. 20px] | Generous component padding |
| `space.6` | [e.g. 24px] | Gap between components in a group |
| `space.8` | [e.g. 32px] | Section internal spacing |
| `space.10` | [e.g. 40px] | Gap between sections |
| `space.12` | [e.g. 48px] | Large section padding |
| `space.16` | [e.g. 64px] | Page-level vertical rhythm |

**Rules**
- Use smaller values (1–4) within a component
- Use mid values (4–8) between components in a group
- Use larger values (8–16) between sections and page regions
- [e.g. Never use arbitrary values — always pick the nearest scale step]

---

## Elevation

Shadow levels and what they communicate. Elevation signals layering and interaction state.

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `elevation.0` | none | Flat elements, inline content | Interactive surfaces |
| `elevation.1` | [e.g. 0 1px 2px rgba(0,0,0,0.05)] | Cards, subtle raised surfaces | Overlays |
| `elevation.2` | [e.g. 0 4px 6px rgba(0,0,0,0.07)] | Dropdowns, popovers | Page-level elements |
| `elevation.3` | [e.g. 0 10px 15px rgba(0,0,0,0.1)] | Modals, dialogs | Inline components |
| `elevation.4` | [e.g. 0 20px 25px rgba(0,0,0,0.15)] | Toasts, floating action elements | Standard cards |

---

## Motion

Duration and easing values with usage context. Match the motion to the weight of the interaction.

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `motion.duration.instant` | [e.g. 80ms] | Hover states, focus rings | Layout shifts |
| `motion.duration.fast` | [e.g. 150ms] | Button feedback, toggles, small reveals | Page transitions |
| `motion.duration.default` | [e.g. 200ms] | Most UI transitions | Decorative animation |
| `motion.duration.slow` | [e.g. 300ms] | Modals, drawers, page-level transitions | Micro-interactions |
| `motion.duration.deliberate` | [e.g. 500ms] | Onboarding, celebratory moments | Functional UI |

| Token | Value | Use for |
|---|---|---|
| `motion.easing.default` | [e.g. cubic-bezier(0.4, 0, 0.2, 1)] | Most transitions |
| `motion.easing.enter` | [e.g. cubic-bezier(0, 0, 0.2, 1)] | Elements entering the screen |
| `motion.easing.exit` | [e.g. cubic-bezier(0.4, 0, 1, 1)] | Elements leaving the screen |
| `motion.easing.spring` | [e.g. cubic-bezier(0.34, 1.56, 0.64, 1)] | Playful or expressive moments only |

**Rules**
- [e.g. Respect prefers-reduced-motion — all transitions should fall back to instant]
- [e.g. Never animate layout properties (width, height, top, left) — use transform instead]

---

## Radius

Border radius scale with component-level guidance.

| Token | Value | Use for |
|---|---|---|
| `radius.none` | 0px | Sharp-edged elements, data tables, code blocks |
| `radius.sm` | [e.g. 4px] | Badges, tags, compact chips |
| `radius.default` | [e.g. 6px] | Buttons, inputs, cards (default) |
| `radius.md` | [e.g. 8px] | Cards, panels, larger containers |
| `radius.lg` | [e.g. 12px] | Modals, dialogs, sheets |
| `radius.xl` | [e.g. 16px] | Large feature cards, hero elements |
| `radius.full` | [e.g. 9999px] | Pills, avatars, circular buttons |

*[e.g. Default to `radius.default` for interactive elements unless the component has a specific rule.]*
