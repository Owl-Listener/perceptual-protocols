# Motion Vocabulary

A starter perceptual vocabulary for motion. Eight qualities, chosen because they cover distinct motion territory, are immediately recognisable to designers, and produce different agent output when asked for more or less of them.

This file is intended to be included in a project alongside `mood.md`, `vocab.md`, and (optionally) `situation.md`. Each entry includes both perceptual descriptions and technical anchors so an agent can translate the perceptual claim into actual animation choices.

Format spec: see `FORMAT.md`. To extend the vocabulary for your project, see `PROMPT.md`.

---

## snappy

**One line:** Decisive, fast, no waiting between intent and response.

**When it applies:** When the user is a power user, or when the task is one they will repeat many times in a session, or when speed itself is part of the brand promise. Snappy motion communicates competence and respect for the user's time.

**References:**
- Linear's command palette — opens in roughly 120ms, no springiness
- Notion's keyboard navigation — most transitions cut, very few fade
- Vercel's hover states — under 100ms, the response feels instant

**Technical anchors:**
- Duration: ≤200ms
- Easing: ease-out, or none
- Gesture response: under 100ms to first frame
- Avoids: springs, overshoots, secondary motion

**Anti-references:**
- iOS sheet drag — springy, not snappy
- Headspace's breathing animations — calm, not snappy
- A consumer app with bouncy button feedback — playful, not snappy

**Pairs well with:** mechanical, invisible
**Tensions with:** springy, playful (when overdone), theatrical

---

## springy

**One line:** Physical, weighted, alive — the interface has bones.

**When it applies:** When the work should feel like real objects responding to touch, when the brand has warmth, when the interface is consumer-facing and the small joy of physical-feeling motion is part of the experience.

**References:**
- iOS sheet drag — the classic spring-physics gesture response
- Apple Mail swipe-to-archive — over-and-back, with weight
- Stripe's "Atlas" form fields — subtle but real spring on focus

**Technical anchors:**
- Easing: spring physics (mass, stiffness, damping) or cubic-bezier with overshoot
- Duration: 300–600ms typical
- Often includes secondary motion (one element settles while another adjusts)
- Permits a small overshoot before settling

**Anti-references:**
- A bank dashboard with bouncy modal — wrong category, undermines trust
- Linear's command palette — snappy and mechanical, deliberately not springy
- A government form — should be precise, not playful

**Pairs well with:** playful, warm-feeling brands
**Tensions with:** snappy, mechanical, invisible

---

## glassy

**One line:** Smooth, frictionless, continuous — motion that slides rather than steps.

**When it applies:** When the work needs to feel premium, when transitions cover distance, when the user should feel they're moving through a single continuous space rather than between discrete states.

**References:**
- Apple's keynote interface transitions — long, smooth, never abrupt
- Apple Music's now-playing card expansion — continuous transformation, not a swap
- Stripe Press article reader — the page flow has no edges

**Technical anchors:**
- Duration: 300–500ms typical
- Easing: smooth s-curves (ease-in-out, or custom cubic-bezier with no sharp transitions)
- Avoids: cuts, hard endings, anything that feels like a snap
- Often pairs with subtle parallax or layered motion

**Anti-references:**
- Linear's command palette — snappy by design, no glide
- A power-user dashboard — efficiency over smoothness
- A jump-cut transition — the opposite of glassy

**Pairs well with:** calm, theatrical (when slow), premium brand qualities
**Tensions with:** snappy, mechanical, invisible

---

## calm

**One line:** Slow, patient, gives breath — motion that respects the user's attention.

**When it applies:** When the user is in a vulnerable, contemplative, or considered state. When the content deserves attention rather than action. When the brand is one of restraint rather than urgency.

**References:**
- Headspace's breathing animations — slow, looping, no rush
- Stripe Press reading interface — fades and reveals at the pace of reading
- Calm app — every animation choice favours the slower option

**Technical anchors:**
- Duration: typically >400ms, often >800ms for hero transitions
- Easing: gentle, often ease-in-out
- Avoids: short durations, snappy responses, anything that hurries
- Often pairs with reduced motion options for accessibility

**Anti-references:**
- A trading interface — calm motion would undermine urgency
- Linear's command palette — efficiency requires snap, not calm
- A high-conversion landing page — calm reads as slow loading

**Pairs well with:** glassy, intimate brand qualities, warm brand qualities
**Tensions with:** snappy, mechanical, theatrical (when fast)

---

## mechanical

**One line:** Exact, predictable, repeats identically — motion that behaves like a precision instrument.

**When it applies:** When the brand asks to be trusted as a tool. When the user is a professional who needs to know that the same gesture will produce the same result every time. When motion is in service of operation, not delight.

**References:**
- Linear's hover states — same duration, same easing, every time
- A keyboard shortcut overlay sliding in — single transition, no variation
- A well-designed terminal application — motion present only when it carries information

**Technical anchors:**
- Easing: linear, or a single consistent ease applied everywhere
- Duration: consistent across element types (don't mix 200ms and 600ms motions without reason)
- Avoids: spring physics (too variable), staggered animations, randomness
- Repeatable: the same trigger produces the same motion identically every time

**Anti-references:**
- A consumer app with celebratory confetti — playful, not mechanical
- iOS sheet physics — springy, deliberately variable in feel
- A motion design reel — theatrical, character-driven

**Pairs well with:** snappy, invisible, precise brand qualities
**Tensions with:** springy, playful, theatrical, organic

---

## playful

**One line:** Surprising, characterful, slightly disobedient — motion that has personality.

**When it applies:** When the brand carries irreverence or warmth, when the moment is celebratory or low-stakes, when delight is the goal and the user is in a frame of mind to enjoy it.

**References:**
- Notion's confetti on task completion
- A loading spinner with character — eyes, expression, secondary motion
- A toggle that overshoots and bounces on first activation

**Technical anchors:**
- Easing: custom curves, anticipation (pull-back-before-go), overshoots
- Often: secondary motion (one thing moves and another responds in sympathy)
- Permits: brief moments of unpredictability or surprise
- Duration: variable; the unpredictability is part of the character

**Anti-references:**
- A medical interface — playful motion would be inappropriate
- A government form — every motion should be functional and earned
- A clinical dashboard — character would undermine trust

**Pairs well with:** springy, warm and irreverent brand qualities
**Tensions with:** mechanical, invisible, authoritative

---

## theatrical

**One line:** Sequenced, choreographed, narrative — motion that tells a story over time.

**When it applies:** When the moment is significant (onboarding, a major reveal, a hero animation), when there is time for the user to attend to the sequence, when the brand benefits from a sense of staging and craft.

**References:**
- Apple keynote intros — staged reveals, dependent timing, choreographed motion
- A well-designed loading sequence for a major product launch
- Stripe's Press product pages — elements arrive in considered order

**Technical anchors:**
- Sequencing: dependent timing (element B starts when element A ends or reaches a threshold)
- Duration: total sequence often >1s
- Easing: varied across elements, each chosen for its role
- Often: pauses (stillness as part of the sequence)

**Anti-references:**
- A search results page — theatrical motion would obstruct the task
- Linear's command palette — single transition, no sequence
- A keyboard shortcut response — should be immediate, not staged

**Pairs well with:** glassy, calm, premium brand qualities
**Tensions with:** snappy, mechanical, invisible

---

## invisible

**One line:** Present without announcement — motion you notice only by its absence.

**When it applies:** Almost everywhere by default. The most common motion in a good interface is invisible — it does its job, the user moves on, the motion is forgotten. Invisible motion is the baseline; the other qualities are deviations earned for specific reasons.

**References:**
- A native macOS scroll position transition — there, but you never think about it
- The cross-fade between similar states in Linear — present, but doesn't draw the eye
- A well-implemented loading skeleton fading to content

**Technical anchors:**
- Duration: 150–250ms typical
- Easing: ease-out, the curve that feels least like animation
- Avoids: anything that says "look at me"
- The success criterion: the user completes their task without being conscious of the motion

**Anti-references:**
- A celebratory checkmark animation — earned visibility
- A theatrical hero reveal — deliberately the opposite of invisible
- A playful loading character — visible by choice

**Pairs well with:** snappy, mechanical, restrained brand qualities
**Tensions with:** theatrical, playful, springy (when overdone)
