# voice.md

> Place this file at the root of your project. Reference it in your agent context, system prompt, or workflow brief.

---

## Personality

What this brand sounds like at its core. Each descriptor is followed by a contrast — the line it doesn't cross.

- **[e.g. Direct]** — but never blunt. Gets to the point without losing the person.
- **[e.g. Warm]** — but never gushing. Caring without performance.
- **[e.g. Confident]** — but never arrogant. Assured without needing to prove it.
- **[e.g. Curious]** — but never exhausting. Brings people in, doesn't lecture.

*3 to 5 descriptors. The contrast is as important as the descriptor.*

---

## Tonal range

The same brand writes differently depending on context. Define the register for each.

| Context | Register | Notes |
|---|---|---|
| Marketing / campaign | [e.g. Bold, energetic, a little playful] | Can afford to be unexpected |
| Product UI / labels | [e.g. Clear, neutral, functional] | Clarity over character |
| Onboarding | [e.g. Warm, encouraging, calm] | Reduce anxiety, build confidence |
| Error messages | [e.g. Direct, calm, never apologetic] | Say what happened and what to do |
| Support / help content | [e.g. Patient, precise, human] | Assumes good faith |
| Empty states | [e.g. Light, useful, not cute] | Give people somewhere to go |

*Add or remove rows to match your product surface area.*

---

## Mechanics

Specific, enforceable writing rules. These apply unless a tonal register above says otherwise.

**Person and address**
- [ ] First person singular (I / me)
- [ ] First person plural (we / our)
- [x] Second person (you / your) — *default: address the reader directly*
- [ ] Third person

**Sentence structure**
- Prefer short sentences. One idea per sentence.
- [e.g. Vary rhythm — short declarative followed by a longer one if needed]
- [e.g. No sentences over 25 words in UI copy]

**Punctuation and formatting**
- [e.g. No exclamation marks in product UI]
- [e.g. Oxford comma always]
- [e.g. Em dash for parenthetical — not brackets]
- [e.g. Sentence case for headings, not title case]

**Grammar**
- [e.g. Active voice by default]
- [e.g. Contractions are fine — "you're" not "you are"]
- [e.g. Don't start sentences with "We" — it centers the brand, not the user]

*These are defaults. Override them intentionally, not by accident.*

---

## Vocabulary

**Use**

| Word / phrase | Why |
|---|---|
| [e.g. "get started"] | Friendlier than "begin" or "initiate" |
| [e.g. "here's how"] | Signals useful, direct guidance |
| [e.g. brand-specific term] | Owned language — use consistently |

**Avoid**

| Word / phrase | Why |
|---|---|
| [e.g. "leverage"] | Corporate filler |
| [e.g. "seamless"] | Overused, meaningless |
| [e.g. "just"] | Minimises the user's effort |
| [e.g. "easy"] | Presumptuous |
| [e.g. "solution"] | Vague, jargon |

**Brand-specific terms**

| Term | Usage |
|---|---|
| [e.g. Product name] | Always capitalised, never abbreviated |
| [e.g. Feature name] | Refer to as X, not Y |

---

## Reference

A before/after pair. The fastest way to calibrate an agent on your voice.

**This is the voice:**

> [Paste a real example — a headline, onboarding message, or UI string that sounds exactly right. Two to four sentences is enough.]

**This is not the voice:**

> [Paste a counter-example — something that's technically correct but tonally wrong. Generic AI copy works well here. Name what's off about it.]
