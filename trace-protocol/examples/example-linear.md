# Linear, traced

**Source:** trace-protocol extraction from [Linear](https://linear.app) product interface, May 2026.
**Surfaces analysed:** Issue list, board view, project page, settings, command palette, marketing site landing.
**Vocabulary used:** Canonical [vocab.md](../../vocab-protocol/vocab.md) from the perceptual-protocols family.

This is a worked example of trace-protocol output. Useful as a calibration reference when reading your own first drafts. The `trace.md` below is the kind of file trace-protocol should produce: anchored, specific, two-sided, honest about uncertainty.

---

## Mood summary

A tool that has earned its restraint. Linear feels like an interface designed by someone who has been frustrated by every other project management tool and decided to remove every element that did not pay rent. The mood is quiet, fast, exact — the digital equivalent of a well-machined precision instrument. There is care in every detail, and the care is invisible by design.

## Implied vocabulary

### precision
- **Anchored to:** The keyboard shortcut overlay (every action has a memorable mnemonic). The 1px borders on issue rows. The exact alignment of meta-fields. The 0.16s ease curve on hover transitions.
- **Why:** These are not aesthetic flourishes. They are decisions about how the interface should feel under the hand, and every one of them has been made with intent.

### restraint
- **Anchored to:** The choice to render the entire issue list at near-monochrome, reserving colour for status pills and the priority dot. The omission of avatar-heavy visual noise. The absence of a sidebar that's trying to look "rich."
- **Why:** What's missing carries the meaning. Linear refuses ornament in places where competitors lean in.

### density
- **Anchored to:** The issue row that fits identifier, title, status, priority, assignee, labels, and date in a single ~32px row, all readable, none crowded.
- **Why:** This is information density tuned for power users who would resent being patronised with breathing room.

### authority
- **Anchored to:** The command palette as the primary interaction model. The willingness to make the user learn the shortcuts. The marketing copy that doesn't try to charm.
- **Why:** Linear acts like a tool that knows its audience already wants what it offers. It refuses to perform friendliness.

### materiality (subtle)
- **Anchored to:** The animation curves. The way panels slide in with weight. The subtle drop-shadow gradient that gives the modal physical authority.
- **Why:** Linear is not flat. It has subtle materiality, but only in motion. Static screenshots underrepresent it.

## Implied anti-references

What Linear is deliberately not doing:

- **A playful card-stacking interface.** Linear's audience does not want their work product to look like a cheerful organisational toy.
- **Labyrinthine settings menus.** Settings in Linear are flat, named, alphabetised, and findable. There is a refusal of menu-tree depth.
- **Pastel optimism.** No watercolour banners. No motivational illustrations. No "let's get organised!" microcopy.
- **A consumer task app's draggable-everything maximalism.** Linear allows drag where drag is the right move. It does not make everything draggable for the joy of it.
- **A typical SaaS dashboard's metric-soup landing screen.** Linear opens to the work, not to the analytics about the work.

## Choices that produced this mood

- **Monospace numerals throughout.** Issue IDs, dates, durations — anything numeric reads as tabular.
- **A near-monochrome palette with extreme selectivity on hue.** Colour appears where it carries meaning (priority, status) and is otherwise absent.
- **Custom sans-serif geometry that reads as both modern and slightly cool.** Reminiscent of Inter but proprietary, signalling care without shouting.
- **Type sizes that are unusually small for a 2020s product.** This is a power-user reading distance.
- **Keyboard-first interaction model.** The command palette is the hero, not the sidebar.
- **Animation curves that suggest weight and bias toward fast.** Nothing bounces. Nothing waits to be admired.

## Cultural or temporal context

Linear sits in the lineage of post-2018 productivity tools that explicitly rejected the consumer-friendly visual language of the prior generation. It draws aesthetically on terminal applications, on Notion's restraint without Notion's blank-page passivity, and on the design culture around Stripe, Vercel, and the early-2020s "developer-tools-as-design-object" movement.

## Confidence and uncertainty

- **High confidence** on the precision, restraint, and density readings. These are observable in every surface.
- **Medium confidence** on materiality. Some of the effects I'm reading as deliberate weight could be standard CSS transitions. Worth looking at the source in browser dev tools to confirm.
- **Lower confidence** on authority. Linear could be authoritative because it has earned the right, or because it doesn't yet have to perform friendliness to win over a wider audience. The marketing site tone may shift if they move down-market. Watch for that.

---

## What to take from this example

A few moves worth noting when you read your own trace-protocol output:

**Every quality is anchored to specific elements.** Not "feels precise" but "1px borders, 0.16s ease curves, monospace numerals." The anchoring is most of the work.

**Anti-references describe categories, not competitors.** Saying "labyrinthine settings menus" is more useful and more honest than naming a specific product. It points to the shape Linear is not, without making the document about anyone else.

**Confidence is graded.** Some claims are high-confidence, some are middling, some are speculative. A `trace.md` that pretends to be certain about everything is suspect. Honesty about uncertainty makes the rest of the document more trustworthy.

**The cultural context section is short, optional, but earns its place.** It anchors the work in a moment and a lineage, which is useful when you go to make something different (or similar).

If your own first pass doesn't have these properties, push back on the model. "Anchor more specifically." "Drop the brand names from anti-references." "Tell me which of these claims you're least sure about."
