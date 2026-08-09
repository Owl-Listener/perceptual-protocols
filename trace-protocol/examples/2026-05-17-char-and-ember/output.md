# Landing Page Hero — Char & Ember

> **Artifact note:** This is the verbatim Step 2 output from the Char & Ember experiment — the landing page hero an AI agent produced when briefed with the mood.md (and the canonical vocab.md). Produced by Claude Opus 4.7 in Claude Code, May 2026.

Product: a small platform for booking remote, single-occupancy cabin stays.
Brief: `mood.md` (*Char & Ember*). Vocabulary: `vocab.md`.

---

## 1. Headline

**The stove is already lit.**

## 2. Subhead

Remote cabins, let one person at a time. You walk the last stretch on foot as the light goes — and the cold stays on the other side of the door.

## 3. CTA button

**Find your cabin**

Rejected: *Book now*, *Get started*, *Reserve instantly*. See *Tensions & trade-offs*.

---

## 4. Visual treatment

A developer should be able to build the hero directly from this. All colours, names, and rationale anchor to `mood.md`.

### 4.1 Concept

One photograph of a small dark cabin at dusk, its single window glowing orange, set into a deep charred-near-black field. The page is the *cold envelope*; the lit window is the *one hot point*; the text is the *warm interior*, readable out of the dark. Nothing else is allowed to glow. This is the brief's central principle — **dark shell, warm core** — built once, at full strength, and then left alone.

### 4.2 Layout & grid

- Full-viewport hero, `min-height: 100svh`. Position relative; the dark field bleeds edge to edge.
- 12-column grid. Page gutter `clamp(1.5rem, 5vw, 6rem)`. Inner max-width `1560px`, centred; the background colour and image bleed past it to the viewport edges.
- **Desktop ≥1024px** — two asymmetric zones (the monopitch lean; never centred):
  - **Text zone**: grid columns 1–6 (≈50% width). Vertical anchor is *high* — text block's optical centre sits ~6% above viewport centre, like a roofline, not floating mid-frame.
  - **Image zone**: columns 7–12, full-bleed, bleeding off the top and right edges of the viewport.
- **Mobile <1024px** — single column. The photograph becomes the full-bleed hero background; text and CTA sit left-aligned over it (see Background, 4.6). Whitespace is preserved by *removing* the eyebrow/horizon metadata before it is allowed to cramp — restraint leads over completeness.

### 4.3 Typography

Two families. A warm transitional serif for the one focal text moment; a humanist grotesque for everything operational. No geometric or clinical sans (explicit anti-reference). Nothing hairline — *nothing here is fragile*.

| Element | Face (with fallback stack) | Weight | Size | Line-height | Tracking | Align |
|---|---|---|---|---|---|---|
| Eyebrow | `"Söhne", "National 2", "Source Sans 3", system-ui, sans-serif` | 500 | 13px | 1.2 | +0.14em, uppercase | left |
| Headline | `"Tiempos Headline", "Lyon Display", "Newsreader", Georgia, serif` | 540 (Medium) | `clamp(2.75rem, 6vw, 5.25rem)` | 1.06 | −0.012em | left |
| Subhead | `"Söhne", "National 2", "Source Sans 3", system-ui, sans-serif` | 400 | `clamp(1.0625rem, 1.4vw, 1.3125rem)` | 1.6 | 0 | left |
| Horizon meta | same as eyebrow | 500 | 13px | 1.2 | +0.10em | left |
| Button label | same as eyebrow | 500 | 16px | 1 | +0.02em, sentence case | centred in button |

- Headline `max-width: 15ch` — forces 2–3 short stacked lines (a gable silhouette; keeps the line measure intimate, one-to-one).
- The headline is the *only* place the heavier serif weight appears — the typographic equivalent of the single ember. Subhead and all UI stay in the regular/medium band.
- Headline is left-aligned on a hard left axis, not centred. Asymmetry is the design; do not balance it.

### 4.4 Colour palette (anchored to `mood.md` qualities)

| Token | Hex | `mood.md` name | Role | Qualities served |
|---|---|---|---|---|
| `--field` | `#1C1A17` | charred larch | Hero background, dominant surface | `refuge`, `restraint`, `materiality` (warm near-black, never `#000`) |
| `--ground` | `#211E1A` | (charred, lifted) | Thin lower "ground" band the content sits on | `materiality`, `rhythm` |
| `--ember` | `#C8531F` | stove ember | **Window glow inside the photograph only** | `ember`, `warmth`, `refuge` |
| `--text` | `#E6E1D6` | lime plaster | Headline; warm light in the dark, never `#FFF` | `warmth`, `materiality` |
| `--text-soft` | `rgba(230,225,214,0.78)` | lime plaster @78% | Subhead — a quieter step in the hierarchy | `restraint`, `rhythm` |
| `--quiet` | `#9A9082` | silvered larch | Eyebrow, horizon meta, button border | `patina`, `restraint` |
| `--accent-warm` | `#8A3A1C` | weathered corten | Focus ring only — warm, not hot | `precision` (in service of warmth) |
| `--wood` | `#E0C49B` | raw birch ply | Button hover fill (the interior, on contact) | `warmth`, `materiality` |

Discipline (from the brief's *one hot point* principle): `--ember` is **never** used as a UI fill, border, or background — it exists exclusively as the photographed window. Greens (`highland moss`, `forest dusk`) live only inside the photograph's landscape, never in chrome. The interface is char, plaster, and silvered larch; the warmth is in the picture and the words.

### 4.5 Imagery direction

- **One** photograph. A single small dark cabin — charred timber or rust metal — seen from *outside*, at dusk / blue hour, in cold open landscape (moorland, pine, or loch). Exactly one window glowing warm orange. No people. No styled interior. The thesis image of the board.
- Naturally lit and slightly underexposed in the cold areas so the lit window is the brightest thing in the frame. Visible grain and weather — reads as a *photograph with patina*, not a 3D render, not HDR, not glossy. Matte throughout; the only glow is the light itself.
- Desktop: full-bleed in the image zone, bleeding off top and right. A `--field`→`transparent` linear scrim on the image's left edge (~30% of its width, `to right`) welds it to the dark text field — no hard rectangular seam; the night wraps the cabin.
- This is the only saturated element on the entire page.

### 4.6 Background & white-space behaviour

- Hero background: flat `--field`. No gradient, no texture overlay, no vignette beyond the single image scrim. Matte (explicit anti-reference: no gradient sheen, no glassmorphism).
- A 1px rule in `--quiet` at `opacity: 0.22` spans the gutters ~96px above the viewport bottom — a horizon. The content "sits on" it the way a cabin sits on its site. Just above it, left-aligned: `No road to the door · no wifi · one bed, one stove` (horizon-meta style). One thin line and a plain statement of constraints — earnest, not sold.
- White-space is generous and deliberately *unbalanced*. The text zone holds far more void than content; treat that void as the cold landscape that makes the small warm text block read as shelter ("small object, big context"). The large calm areas lower-left and right are intentional — never fill a void to balance the composition. The eye crosses the void to the one lit window.
- Mobile: the photograph becomes the full hero background under a `--field` scrim at 62% opacity (heavier — `linear-gradient(180deg, rgba(28,26,23,0.55), rgba(28,26,23,0.82))`) so text glows out of the image. Text and CTA left-anchored at the `1.5rem` gutter, never centred. CTA max-width `22rem`, not edge-to-edge.

### 4.7 Button treatment

- Shape: rectangle, `border-radius: 2px` (a planed-edge chamfer, not a friendly pill — honest, made).
- **Default**: `background: transparent`; `border: 1px solid rgba(154,144,130,0.55)` (`--quiet`); label `--text`; `padding: 18px 32px` (generous, deliberate — a considered action, not a quick tap).
- **Hover**: `background: --wood (#E0C49B)`; `border-color: #E0C49B`; label `--field (#1C1A17)`. Transition `background-color 320ms cubic-bezier(0.22,0.61,0.36,1), color 320ms` — slow and deliberate, the threshold from cold/outside to warm/inside enacted on contact. No scale, no shadow, no glow.
- **Focus-visible**: `outline: 2px solid #8A3A1C` (`--accent-warm`), `outline-offset: 3px` — the single permitted warm UI accent, exact and intentional.
- **Active**: `background: #D0AE80` (raw birch ply, darkened); nothing else changes.
- **`prefers-reduced-motion: reduce`**: replace the 320ms colour transition with an instant state change. The friction in this design is spatial and verbal, never motion-dependent.
- Optional secondary action (only if strictly required): a plain text link, `--text` at 70%, 1px underline `--quiet` offset 4px, no button chrome — recessive, placed 24px after the primary. One clear gesture is preferred; a second action should almost disappear.

---

## Tensions & trade-offs

**`friction` / `restraint` vs. landing-page conversion convention — friction led.**
The product category pulls toward a frictionless, urgent CTA (*Book now*, *Reserve instantly*, scarcity copy). The brief is explicit that the work must "feel like a thing, not a feed," that hype is an anti-reference, and that the experience *is* the threshold. So the CTA is a quiet, deliberate verb (*Find your cabin*), the button is large-padded and slow to warm, and the page states its constraints plainly (`no road to the door · no wifi`) instead of selling them away. Cost: lower immediate click optimisation. Gain: the page feels like the retreat it sells — chosen, not glided into.

**`ember` (one hot point) vs. CTA affordance — the one hot point led.**
Conversion convention wants a bright orange "buy" button. The brief allows exactly one saturated hot point per view, and the soul of the board is the lit window in the dark. So the single `#C8531F` ember is spent entirely on the photographed window, and the CTA earns its emphasis from position, scale, and the calm dark around it — warming to wood (`#E0C49B`) only on contact. Two hot points would have broken the central principle; the photograph kept it.

**`precision` vs. `patina` / `materiality` — patina led, precision kept as joinery.**
Precision governs only the invisible craft: the baseline grid, optical alignment, the exact focus ring. Every visible surface carries weather and grain (photograph, matte field, planed-edge button). Precision is the joinery, never the finish — keeping the brief's instruction to hold precision's care while refusing its chill.

**`intimacy` vs. a crowd-facing hero — intimacy led.**
No social proof, no "join thousands," no plural. Copy is second-person singular, single-occupancy stated plainly, line measure kept short. The page addresses one person about one cabin, as the brief requires.
