# Motion: Linear (extracted)

**Source:** motion-protocol extraction from [Linear](https://linear.app) product interface, May 2026.
**Surfaces analysed:** Issue list, command palette, board view, side panel transitions, hover states, modal sheets, page navigation.
**Vocabulary used:** Canonical [`motion.md`](./MOTION.md) from the perceptual-protocols family.

This is a worked example of motion-protocol output. Read alongside the [Linear static trace](../trace-protocol/examples/example-linear.md) — together they describe how Linear's identity expresses across both spatial and temporal dimensions. The same product. Two layers of perception.

---

## Motion summary

Linear moves like a precision instrument that has decided not to draw attention to itself. The motion identity is unusually consistent — the same easing curve and similar durations appear across surfaces, transitions are short and decisive, and almost nothing waits to be admired. The interface is in service of operation, not of delight. When motion is present, it carries information; when it isn't required, it isn't there.

## Implied vocabulary

### snappy
- **Anchored to:** Command palette opens in roughly 120ms with a single ease-out curve. Hover states resolve in 160ms. Page navigation between issue and project views feels under 250ms.
- **Why:** Linear's audience is operating the tool repeatedly throughout the day. Snappy motion is a form of respect — the interface does not waste the user's time waiting for itself to be ready.

### mechanical
- **Anchored to:** The same easing curve appears on hover states, menu opens, modal reveals, and panel transitions. The duration sometimes varies but the curve does not.
- **Why:** Linear behaves like a precision instrument. The user develops muscle memory because the same gesture produces the same response every time. There are no surprises and the absence of surprise is the point.

### invisible
- **Anchored to:** Page navigation, scroll behaviour, the cross-fade between similar issue states. You complete the task and never think about the motion.
- **Why:** The most common motion in the Linear interface is one you don't notice. Invisible is the baseline — the qualities below are the exceptions.

### materiality (subtle, motion-specific)
- **Anchored to:** Modal sheets that slide in with a faint sense of weight. The drop-shadow gradient that gives the side panel a sense of physical thickness as it animates.
- **Why:** Linear is not flat-dead. There's a quiet materiality to the way panels enter and leave — they feel like objects with bones, even though no spring physics are involved. This is what distinguishes Linear's motion from the truly invisible motion of a terminal application.

## Implied anti-references

What Linear's motion deliberately is not:

- **Springy.** No bounce, no overshoot, no settle. Sheets do not wobble into place. Buttons do not over-and-back on press.
- **Theatrical.** No staged reveals, no choreographed sequences, no hero animations on app launch. The dashboard arrives instantly.
- **Glassy.** No long, smooth transitions covering distance. Linear cuts and resolves where a glassier product would slide.
- **Playful.** No confetti. No celebratory animations on task completion. No personality in the easing curves.
- **Calm.** Linear is not slow. Calm motion would feel like the tool was failing to keep up.

## Technical anchors observable

- **Standard ease:** A single ease-out curve applied across the product. Likely cubic-bezier(0.16, 1, 0.3, 1) or similar — a curve that decelerates fast at the end with no overshoot.
- **Standard durations:** 120ms (hover, instant feedback), 160ms (state changes), 240ms (panel transitions). Three durations cover the vast majority of motion.
- **Gesture response:** First frame appears under 100ms across keyboard and pointer interactions.
- **What is absent:** Spring physics, secondary motion, anticipation curves, staggered timing across elements.

## Choices that produced this motion identity

- **One easing curve, used everywhere.** The deliberate consistency is what produces the mechanical feel. Most products vary their easing across components; Linear does not.
- **A small set of standardised durations.** The user is not subjected to 200ms here and 600ms there. The temporal scale is one of the things being held constant.
- **No staggered animations.** When multiple elements need to change, they change together. Sequencing would introduce theatricality.
- **No secondary motion.** A pressed button does not affect the elements around it. The motion of any one element is contained.
- **Absent reveals.** The app does not animate in on launch. There is no hero. The interface is already there when you arrive.

## Cultural or temporal context

Linear's motion identity sits in the post-2018 productivity tool lineage that explicitly rejected the playful consumer motion language of the prior generation (Slack's reactions and confetti, Asana's celebrations, mid-period GitHub's bouncy buttons). It draws on terminal applications, on the deliberate restraint of macOS native motion at its most invisible, and on the design culture that emerged around developer tools positioning themselves as serious instruments rather than friendly companions.

## Confidence and uncertainty

- **High confidence** on snappy, mechanical, invisible. These are observable everywhere.
- **Medium confidence** on the exact easing curve. The visual signature is consistent, but I'm inferring the bezier from the feel; the source CSS would confirm.
- **Lower confidence** on whether the subtle materiality is deliberate or a side effect of CSS defaults. A future review could distinguish by looking at the source or asking a designer at Linear directly.

---

## What to take from this example

A few moves worth noting when you read your own `motion.md` first drafts:

**Every quality is anchored to specific timing or behaviour.** Not "feels snappy" but "command palette opens in roughly 120ms." Anchoring is most of the work.

**The technical anchors section did real work.** Naming the three standard durations and the single easing curve is what would let an agent actually reproduce the motion identity. Without that, the perceptual claim is just a vibe.

**Anti-references closed off entire territories.** Linear is not springy. Not theatrical. Not glassy. Not playful. Not calm. Naming what the motion *is not* was as informative as naming what it is.

**Confidence is graded.** Some claims are observable, some are inferred, some need source-code confirmation. A motion.md that pretends certainty about easing curves it can only see in animation is suspect.

**The summary and the per-quality entries reinforce each other.** The opening paragraph names the identity in one breath. The per-quality entries anchor it. The composition holds.

**Read this alongside the static [Linear trace](../trace-protocol/examples/example-linear.md).** The same product. Static identity: precise, restrained, dense, authoritative, subtly material. Motion identity: snappy, mechanical, invisible, subtly material. The two profiles reinforce each other — Linear is the rare product whose motion and stillness are saying the same thing.
