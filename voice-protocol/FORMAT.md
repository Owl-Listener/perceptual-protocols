# voice.md format spec

A `voice.md` is a structured description of how a brand writes. It has five sections, in this order. Any agent that can read text can use it.

## Top-level structure

```markdown
# voice.md

[Optional: one line naming the brand or product this voice belongs to.]

## Personality

- **[Descriptor]** — but never [boundary]. [One line on what the descriptor buys you.]
- **[Descriptor]** — but never [boundary]. [One line.]

## Tonal range

| Context | Register | Notes |
|---|---|---|
| [Surface] | [How the voice sits here] | [What to optimise for] |

## Mechanics

**Person and address**
- [Rule]

**Sentence structure**
- [Rule]

**Punctuation and formatting**
- [Rule]

**Grammar**
- [Rule]

## Vocabulary

**Use**

| Word / phrase | Why |
|---|---|
| [Term] | [Reason] |

**Avoid**

| Word / phrase | Why |
|---|---|
| [Term] | [Reason] |

**Brand-specific terms**

| Term | Usage |
|---|---|
| [Term] | [How to use it] |

## Reference

**This is the voice:**

> [A real sample, two to four sentences.]

**This is not the voice:**

> [A counter-example that is technically correct and tonally wrong.]

*[One line naming what is wrong with the second version.]*
```

## Rules

**Every personality descriptor carries a contrast.** `**Direct** — but never blunt` is a constraint. `Direct` on its own is a mood ring. The contrast is the half that does the work, and a descriptor without one should be cut. This is the verbal equivalent of the family's anti-reference rule: a quality is defined by the boundary it doesn't cross.

**Three to five descriptors, not ten.** A voice with ten personality traits has no personality. If two descriptors are near-synonyms, keep the more specific one.

**Tonal range covers the surfaces you actually ship.** Add and remove rows to match your product. A marketing site and a CLI have almost no surfaces in common; neither should carry the other's rows. If a surface exists in your product and isn't in the table, an agent will guess at it.

**Mechanics are enforceable or they are not mechanics.** "Write clearly" is not a mechanic. "No sentence over 20 words in UI copy" is. The test: could a reviewer decide whether a given string breaks the rule without consulting you? If not, it belongs in Personality, not Mechanics.

**Every avoid-word has a reason.** The reason is what lets an agent generalise. "Avoid *seamless*" bans one word; "Avoid *seamless* — empty" teaches the agent to distrust the whole register.

**The reference pair is not optional.** It is the fastest calibration in the file, and it is the section agents lean on hardest. Use real copy for the positive example. Generic AI copy works well as the counter-example, because it is the exact failure mode the file exists to prevent.

**Name what's wrong with the counter-example.** "This is not the voice" tells an agent the sample is bad. The line underneath tells it *why*, which is the part it can apply to copy it hasn't seen yet.

## What makes a good descriptor

1. **Recognisable** — a word people already use about the brand, not one invented for the document.
2. **Contrastable** — it has a plausible failure mode on the other side. "Warm" fails into "gushing." "Professional" fails into nothing in particular, which is why it's a weak descriptor.
3. **Visible in sentences** — you can point at a line of real copy and say *there, that's the warmth*. If you can't, the descriptor is aspirational rather than descriptive.
4. **Agent-actionable** — asking for more or less of it produces different copy.

## Relationship to the other modality vocabularies

`voice.md` is the verbal sibling of `vocab.md` (static), `motion.md` (temporal), and `sound.md` (sonic). The four are designed to be present in the same project without collision — they describe different perceptual layers and never define the same term twice.

Where a term genuinely spans layers, define it once in `vocab.md` and refer to it from `voice.md` rather than restating it. `restraint` means something coherent in both a layout and a sentence; the definition belongs in the shared vocabulary, and `voice.md` should say how restraint shows up in punctuation and sentence length specifically.

## Deliberate contradiction

The vocabularies do not enforce coherence. A brand can look precise and write loose, and some do it on purpose. The format's job is to make that visible and discussable, not to prevent it. If the contradiction is intentional, say so in the file — otherwise the next agent to read it will treat it as a bug and quietly resolve it.
