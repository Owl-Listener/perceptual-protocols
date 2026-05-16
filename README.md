# Perceptual Protocols

> There's no protocol for how things should feel.

We've spent the last two years building increasingly sophisticated ways to give AI agents procedural knowledge. How to write CSS. How to follow a design system. How to obey our rules. All text. All procedural. All blind to the visual.

That work is necessary. It is also half the job.

The other half, the half that designers, musicians, writers, architects, and every creative human spend their career cultivating, is **perceptual**. Taste. Judgement. The ability to look at something and know it is wrong before you can articulate why. We've been encoding the **how** and ignoring the **what it should feel like**.

This is a family of protocols for the other half.

---

## What's in here

Each protocol does one thing and stops. Each one outputs a plain markdown file that any agent — Claude, Gemini, ChatGPT, Cursor, Copilot — can read. They work alone, but they compose into a complete workflow when used together.

| Protocol | What it does | Output | Status |
|---|---|---|---|
| [mood-protocol](./mood-protocol) | Declare what the product should feel like | `mood.md` | Released (v0.1) |
| [vocab-protocol](./vocab-protocol) | Share a vocabulary for the qualities you mean | `vocab.md` | Released (v0.1) |
| [situation-protocol](./situation-protocol) | Weight the qualities differently by context | `situation.md` | Released (v0.1) |
| [trace-protocol](./trace-protocol) | Read an existing UI and capture its implicit mood | `trace.md` | Released (v0.1) |
| [critique-protocol](./critique-protocol) | Critique agent output against the brief | `critique.md` | Released (v0.1) |
| [taste-protocol](./taste-protocol) | Capture a designer's persistent preferences across projects | `taste.md` | Planned |

The order tells the story of how the system runs. Declare intent, share language, encode conditional weighting, read existing work, close the feedback loop.

---

## Quick start

The fastest way in is mood-protocol. You need a moodboard, the AI subscription you already pay for, and sixty seconds.

```
1. Make a moodboard. Figma, Pinterest, a wall of printouts. Any moodboard.
2. Screenshot it. Annotations and sticky notes included — the vision model reads everything visible.
3. Open Claude, Gemini, or ChatGPT. Upload your image.
4. Paste the prompt from mood-protocol/PROMPT.md.
5. Save the output as mood.md in your project.
```

That's it. No setup. No API keys. No terminal. The protocol is the format, the tooling is just convenience.

From that moment on, any agent that can read your project can read your mood. As you adopt the other protocols, they read alongside it.

---

## What makes these a family

Six principles. All six apply to every protocol in here.

**Human-curated, not AI-generated.** These are not tools that generate taste for you. They are tools that capture and share the taste you already have, so an agent can apply it.

**Markdown, always.** The output is plain `.md`. Portable, versionable, agent-readable, human-readable. No proprietary formats. No lock-in. Git can diff your taste.

**Model-agnostic.** Anything that can read text can use these. Claude, Gemini, ChatGPT, Cursor, Copilot, the model you'll be using in two years.

**Single-purpose.** Each protocol does one thing and stops. mood-protocol is not vocab-protocol is not situation-protocol. They compose. They do not bloat.

**No setup is the default.** If a designer can't use a protocol in sixty seconds with the AI they already have, the protocol has failed. There can be a script for power users, but the prompt and the format spec are the canonical path.

**Anti-references are first-class.** Knowing what to avoid carries as much information as knowing what to pursue. "NOT corporate dashboard" closes off an entire territory of bad decisions. Every protocol that handles taste handles its opposite.

---

## The argument behind this

You can use these without reading this section. But it is the reason they exist.

For most of computing history, the interface had to be designed for reuse. A design system was an artifact of scarcity. You couldn't afford to make a different interface for every person at every moment, so you built one carefully and shipped it to everyone. Polish was the proof of care.

That world is ending. Generative interfaces are arriving. Fluid, personalised, regenerated for each user in the moment of use. When the interface is made on the fly, the design system stops being a library and starts being something more like a vocabulary. The agent needs to know not just what to build, but what the result should feel like, and how that feeling should adapt to who is looking and when.

Designers already know how to communicate this. We have moodboards. We have anti-references. We have private vocabularies for the qualities of a thing. We have implicit knowledge about how a clinical dashboard should feel different from a patient portal. The problem is that all of this lives in our heads, in Figma files, on pinned walls. In places agents cannot see.

These protocols are bridges. Each one takes something designers already do, and turns it into a file an agent can read.

If `SKILL.md` is the protocol for craft knowledge, this family is the beginning of a protocol for aesthetic intent.

---

## How the protocols relate

The family sits on the perceptual side of a bigger gap in how we talk to agents.

```
                 PROCEDURAL                          PERCEPTUAL
              (how to do things)            (what it should feel like)

              SKILL.md                            mood.md
              CLAUDE.md                           vocab.md
              cursor rules                        situation.md
              agent-ready                         trace.md
              design tokens                       critique.md
                  │                                  │
                  └──────────── agent reads ─────────┘
                                  both halves
```

Procedural protocols tell the agent **how to do the work**. Perceptual protocols tell the agent **what the work should feel like when it's done**. An agent with only one half builds competently and wrongly. An agent with both starts to feel like a collaborator.

---

## Composing as a system

The five released protocols are not five discrete tools. They compose into a workflow.

```
            STATIC IDENTITY                    CONDITIONAL LOGIC
              mood.md   ──┐                     situation.md
              vocab.md  ──┤                         │
                          │                         │
                          ├─────► agent reads ◄─────┤
                          │       all of these
                          │           ↓
                          │     generates work
                          │           ↓
                          │       critique.md ──► feeds back
                          │                       into mood / vocab /
                          │                       situation
                          ↓
                   (trace.md reads
                    existing work
                    in the same format)
```

Two layers describe what the brand is and how it adapts. A generation step turns the brief into output. A feedback loop assesses the output and sharpens the brief. A parallel analytical channel reads existing work — yours, a competitor's, a piece of inspiration — into the same format.

The point of building it this way is that no protocol has to do all the work. Each one is small. Together they are sufficient.

---

## Roadmap

**Now (v0.1):** Five working protocols cover the project-level perceptual workflow end to end. Declare intent (mood). Share language (vocab). Weight by context (situation). Read existing work (trace). Close the loop on output (critique).

**Next:** Real-world use of the five protocols on actual projects. Surfacing the vocabulary gaps that need new terms, the situation patterns that recur across products, and the integration moves that make the family work together. Worked examples for each protocol drawn from real (not synthetic) projects.

**After that:** taste-protocol, a designer-personal cross-project preferences layer that sits above the project-scoped protocols. Sequenced for after the project-level protocols have been road-tested.

This list is a hypothesis, not a contract. The discipline is too young to plan with confidence. Build what's needed, ship it small, learn, keep going.

---

## Contributing

The most useful contributions are:

- **New vocabulary terms** for `vocab-protocol`. The taxonomy is open and growing. Send a pull request with the term, a one-line definition, two example references, and two anti-references.
- **Situation patterns** for `situation-protocol`. Common context families that recur across products (healthcare, finance, government, education) are especially valuable. Send a pull request with a worked situation entry and the kind of product it applies to.
- **Worked examples** for any protocol. A real mood.md / vocab.md / situation.md / trace.md / critique.md from your own work is more useful than any spec.
- **New protocols.** If you've found a gap, something designers do that agents can't yet see, open an issue. Sketch the format. We'll figure out together whether it belongs in this family or somewhere else.

See `CONTRIBUTING.md` inside each sub-protocol for the specifics.

---

## Background reading

A short, opinionated list. The work this builds on.

- Lucero, Hegemann and Oulasvirta — Mood Boards (CHI '19). Empirical work on how designers actually use moodboards.
- Jeffrey Bardzell — Interaction Criticism: An Introduction to the Practice. Foundational paper for aesthetic interaction in HCI.
- UC Berkeley iSchool (2026) — Aesthetic Taste and Its Limits: Breakdowns in Prompt-Mediated Design of User Interfaces. The most current academic work on the exact problem these protocols address.
- Sianne Ngai — Our Aesthetic Categories: Zany, Cute, Interesting. Philosophy of aesthetic experience. The category of the **interesting** especially is essential for AI-era design.
- Richard Shusterman — Somaesthetics. Bodily aesthetics, for when the work needs to consider what design feels like in a body, not just on a screen.
- Donald Norman — Emotional Design. The visceral, behavioural, reflective trio.
- Marc Hassenzahl — hedonic vs pragmatic UX. Two-axis model that makes feeling arguments legible to PMs.

The longer reading list with notes lives in `READING.md`.

---

## License

MIT. See `LICENSE`.

---

## About

Built by [MC Dean](https://marieclairedean.substack.com), part of the [Owl-Listener](https://github.com/Owl-Listener) collection. Small, opinionated protocols for designers building with AI.

We are still in the early days of teaching machines to see what we see. The interesting work is in the translation.

If you make something with these, I want to hear what happens.
