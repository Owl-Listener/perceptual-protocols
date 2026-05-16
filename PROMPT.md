# situation-protocol prompt

A prompt for building a `situation.md` from your product's mood, vocabulary, and a description of the situations it inhabits. Works with Claude, Gemini, or ChatGPT.

## How to use

1. Gather your inputs:
   - Your product's `mood.md` (the baseline identity)
   - Your `vocab.md` (the shared term definitions)
   - The `FORMAT.md` from this folder
   - A description of the situations your product encounters:
     - A list of surfaces (patient portal, clinical dashboard, billing flow, etc.)
     - A list of user roles (patient, nurse, doctor, administrator)
     - A list of moments (onboarding, steady-state, crisis)
     - Optional: example screens or copy from each situation
2. Open Claude, Gemini, or ChatGPT. Upload all of the above.
3. Paste the prompt below.
4. Save the output as `situation.md` in your project.

## The prompt

```
You are helping me build a situation.md for my product — a file that captures how the qualities in my mood.md and vocab.md should weight differently across the situations the product encounters.

I've uploaded:
- mood.md — the baseline perceptual identity of the product
- vocab.md — the shared vocabulary of perceptual qualities
- FORMAT.md — the spec for what a situation.md should look like
- A description of the situations my product inhabits

Your job:

1. Identify the situations that need their own weighting. A situation deserves its own entry when at least two qualities are weighted differently from the product-wide baseline. If a situation doesn't change the weighting meaningfully, omit it.

2. For each situation, write:
   - A clear "When this applies" — specific enough that an agent can pattern-match
   - A "Weighted qualities" list using HEAVY, MODERATE, LIGHT for each quality from vocab.md that meaningfully differs from baseline
   - Optional "Situation-specific qualities" if the situation requires a quality that doesn't apply elsewhere
   - A "Why this weighting" rationale — at least one sentence per situation

3. Use only qualities that already exist in vocab.md, except where you propose a new situation-specific quality (in which case, briefly justify it and suggest whether it should be added to vocab.md).

4. Be opinionated. A situation.md that weights everything MODERATE everywhere is not useful. Make actual calls. Patient portal weights warmth HEAVY; clinical dashboard weights precision HEAVY. Commit.

5. Surface tensions. If two qualities are in tension within a single situation (warmth + authority, urgency + restraint), name the tension explicitly in the rationale.

6. Aim for 3–8 situations. If I've described more than 10, group them or push back.

7. Format the output exactly as FORMAT.md specifies.

Write in the voice of a senior designer briefing a junior collaborator — specific, opinionated, honest about trade-offs. The agent reading this file later will only have your words to go on.

The output is a single complete situation.md. Don't wrap it in commentary, apology, or summary.
```

## Notes on iteration

The first pass will likely under-commit. Useful re-prompts:

- "You weighted too many things MODERATE. Make actual calls — which qualities dominate here, which recede?"
- "You added a situation that doesn't change the weighting meaningfully. Either weight it more distinctly or drop it."
- "You missed the tension between warmth and urgency in the alert state. Name it."
- "You added six new situation-specific qualities. Most of these should be in vocab.md. Justify which actually need to be situation-specific."
- "You have twelve situations. Group them or drop the redundant ones."

## A note on extension

A `situation.md` is a living document. As your product encounters new contexts (a new user type, a new flow, a new moment), add to it. The protocol is designed to grow incrementally — you don't need to enumerate every situation at once. Start with the three or four that most need explicit weighting, and extend.
