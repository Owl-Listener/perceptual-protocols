# tokens.md — example

> A filled-in example for a fictional fintech product called Clearline. Use it as a reference when completing your own `tokens.md`.
>
> Clearline is also the subject of [`voice-protocol/example-clearline.md`](../voice-protocol/example-clearline.md). Read the two together to see how one brand's systematic grammar and verbal identity line up — the reserved spring easing in this file is the same restraint as that file's ban on exclamation marks.

---

## Source

| Format | Location |
|---|---|
| Figma variables | [Clearline Design System — Figma](https://figma.com) |
| CSS custom properties | `src/styles/tokens.css` |
| Tailwind config | `tailwind.config.ts` |

Dark mode is handled via CSS `prefers-color-scheme` and a `data-theme` attribute. The dark values below are applied automatically — no manual switching needed in generated code.

---

## Color

### Surface

| Token | Light | Dark | Use for | Do not use for |
|---|---|---|---|---|
| `color.surface.default` | #ffffff | #0f172a | Page and panel backgrounds | Interactive elements |
| `color.surface.subtle` | #f8fafc | #1e293b | Secondary backgrounds, zebra rows | Primary content areas |
| `color.surface.raised` | #ffffff | #1e293b | Cards, dropdowns, modals | Flat page sections |

### Content

| Token | Light | Dark | Use for | Do not use for |
|---|---|---|---|---|
| `color.content.primary` | #0f172a | #f1f5f9 | Body text, headings | Disabled states |
| `color.content.secondary` | #64748b | #94a3b8 | Supporting text, labels, captions | Primary actions |
| `color.content.disabled` | #cbd5e1 | #334155 | Disabled text | Any active state |
| `color.content.inverse` | #ffffff | #0f172a | Text on filled surfaces | Standard backgrounds |

### Interactive

| Token | Light | Dark | Use for | Do not use for |
|---|---|---|---|---|
| `color.interactive.primary` | #2563eb | #3b82f6 | Primary buttons, key links | Backgrounds |
| `color.interactive.primary.hover` | #1d4ed8 | #2563eb | Hover state only | Default state |
| `color.interactive.secondary` | #f1f5f9 | #1e293b | Secondary buttons, ghost fills | Primary actions |

### Semantic

| Token | Light | Dark | Use for | Do not use for |
|---|---|---|---|---|
| `color.semantic.danger` | #dc2626 | #ef4444 | Destructive actions, errors, failed states | Warnings or neutral alerts |
| `color.semantic.warning` | #d97706 | #f59e0b | Cautionary states, pending | Errors or success |
| `color.semantic.success` | #16a34a | #22c55e | Completion, confirmed transactions | Neutral info |
| `color.semantic.info` | #2563eb | #3b82f6 | Informational states, tips | Actions or CTAs |

---

## Typography

| Token | Size | Weight | Line height | Use for | Do not use for |
|---|---|---|---|---|---|
| `type.display` | 48px | 700 | 1.1 | Hero headings only | Any body or UI content |
| `type.heading.1` | 32px | 700 | 1.2 | Page titles | Section headings |
| `type.heading.2` | 24px | 600 | 1.3 | Section headings | Page titles |
| `type.heading.3` | 20px | 600 | 1.4 | Card titles, subsections | Primary headings |
| `type.body.default` | 16px | 400 | 1.5 | Body text, descriptions | Headings, UI labels |
| `type.body.small` | 14px | 400 | 1.5 | Secondary body, supporting copy | Primary body content |
| `type.label` | 12px | 500 | 1.4 | Form labels, tags, status badges | Body text |
| `type.code` | 14px mono | 400 | 1.6 | Account numbers, sort codes, reference IDs | UI labels |

**Typefaces**

| Role | Family | Fallback |
|---|---|---|
| All UI text | Inter | system-ui, -apple-system, sans-serif |
| Monospace | JetBrains Mono | ui-monospace, monospace |

---

## Spacing

| Token | Value | Use for |
|---|---|---|
| `space.1` | 4px | Icon padding, tight inline gaps |
| `space.2` | 8px | Compact component padding, icon-to-label gap |
| `space.3` | 12px | Default input and button padding (vertical) |
| `space.4` | 16px | Default component padding, gap between related items |
| `space.5` | 20px | Generous component padding |
| `space.6` | 24px | Gap between components in a group |
| `space.8` | 32px | Section internal spacing |
| `space.10` | 40px | Gap between page sections |
| `space.12` | 48px | Large section padding |
| `space.16` | 64px | Page-level vertical rhythm |

**Rules**
- Use space.1–4 within a component
- Use space.4–8 between components in a group
- Use space.8–16 between page sections
- Never use arbitrary values — always pick the nearest scale step
- Prefer space.4 (16px) as the default when unsure

---

## Elevation

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `elevation.0` | none | Flat elements, table rows, inline content | Anything interactive or floating |
| `elevation.1` | 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04) | Transaction cards, list items | Overlays |
| `elevation.2` | 0 4px 6px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.04) | Dropdowns, account selector, date picker | Modals |
| `elevation.3` | 0 10px 15px rgba(0,0,0,0.08), 0 4px 6px rgba(0,0,0,0.04) | Modals, confirmation dialogs | Inline cards |
| `elevation.4` | 0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04) | Toasts, notifications, critical alerts | Standard UI |

---

## Motion

| Token | Value | Use for | Do not use for |
|---|---|---|---|
| `motion.duration.instant` | 80ms | Focus rings, hover background fills | Layout changes |
| `motion.duration.fast` | 150ms | Button press, toggle, checkbox | Page transitions |
| `motion.duration.default` | 200ms | Most UI transitions — accordions, reveals | Decorative moments |
| `motion.duration.slow` | 300ms | Modals entering, drawer sliding in | Micro-interactions |
| `motion.duration.deliberate` | 500ms | Onboarding steps, transaction confirmed state | Functional UI |

| Token | Value | Use for |
|---|---|---|
| `motion.easing.default` | cubic-bezier(0.4, 0, 0.2, 1) | Most transitions |
| `motion.easing.enter` | cubic-bezier(0, 0, 0.2, 1) | Modals, drawers, panels entering |
| `motion.easing.exit` | cubic-bezier(0.4, 0, 1, 1) | Elements leaving the screen |
| `motion.easing.spring` | cubic-bezier(0.34, 1.56, 0.64, 1) | Transaction confirmed celebration only |

**Rules**
- All transitions must respect `prefers-reduced-motion` — fall back to instant (0ms)
- Never animate `width`, `height`, `top`, `left` — use `transform` and `opacity` only
- The spring easing is reserved for the transaction confirmed moment; do not use elsewhere

---

## Radius

| Token | Value | Use for |
|---|---|---|
| `radius.none` | 0px | Data tables, dividers, code blocks |
| `radius.sm` | 4px | Status badges, inline tags |
| `radius.default` | 6px | Buttons, inputs, small cards |
| `radius.md` | 8px | Standard cards, panels |
| `radius.lg` | 12px | Modals, bottom sheets |
| `radius.xl` | 16px | Feature cards, onboarding panels |
| `radius.full` | 9999px | Avatar circles, pill buttons, amount chips |

Default to `radius.default` for all interactive elements unless there is a specific rule above. Do not mix radius scales within a single component.
