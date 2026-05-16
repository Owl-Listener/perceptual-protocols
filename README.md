# Perceptual Protocols

> There's no protocol for how things should feel.

We've spent the last two years building increasingly sophisticated ways to give AI agents procedural knowledge. How to write CSS. How to follow a design system. How to obey our rules. All text. All procedural. All blind to the visual.

That work is necessary. It is also half the job.

The other half, the half that designers, musicians, writers, architects, and every creative human spend their career cultivating, is **perceptual**. Taste. Judgement. The ability to look at something and know it is wrong before you can articulate why. We've been encoding the **how** and ignoring the **what it should feel like**.

This is a family of protocols for the other half.

---

## What's in here

Each protocol does one thing and stops. Each one outputs a plain markdown file that any agent — Claude, Gemini, ChatGPT, Cursor, Copilot — can read. They work alone or together.

| Protocol | What it does | Output | Status |
|---|---|---|---|
| [mood-protocol](./mood-protocol) | Turn a moodboard into structured aesthetic intent | `mood.md` | Released (v0.1) |
| [vocab-protocol](./vocab-protocol) | Build a shared vocabulary for aesthetic qualities | `vocab.md` | Released (v0.1) |
| [trace-protocol](./trace-protocol) | Capture the implicit mood of an existing UI | `trace.md` | Released (v0.1) |
| [critique-protocol](./critique-protocol) | Critique agent output against a mood | `critique.md` | Planned |
| [taste-protocol](./taste-protocol) | Capture a persistent preferences across projects | `taste.md` | Planned |

More will be added. Some won't survive. That's the point of building this way.

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

From that moment on, any agent that can read your project can read your mood.

---

## What makes these a family

Six principles. All six apply to every protocol in here.

**Human-curated, not AI-generated.** These are not tools that generate taste for you. They are tools that capture and share the taste you already have, so an agent can apply it.

**Markdown, always.** The output is plain `.md`. Portable, versionable, agent-readable, human-readable. No proprietary formats. No lock-in. Git can diff your taste.

**Model-agnostic.** Anything that can read text can use these. Claude, Gemini, ChatGPT, Cursor, Copilot, the model you'll be using in two years.

**Single-purpose.** Each protocol does one thing and stops. mood-protocol is not vocab-protocol is not trace-protocol. They compose. They do not bloat.

**No setup is the default.** If a designer can't use a protocol in sixty seconds with the AI they already have, the protocol has failed. There can be a script for power users, but the prompt and the format spec are the canonical path.

**Anti-references are first-class.** Knowing what to avoid carries as much information as knowing what to pursue. "NOT corporate dashboard" closes off an entire territory of bad decisions. Every protocol that handles taste handles its opposite.

---

## The argument behind this

You can use these without reading this section. But it is the reason they exist.

For most of computing history, the interface had to be designed for reuse. A design system was an artifact of scarcity. You couldn't afford to make a different interface for every person at every moment, so you built one carefully and shipped it to everyone. Polish was the proof of care.

That world is ending. Generative interfaces are arriving. Fluid, personalised, regenerated for each user in the moment of use. When the interface is made on the fly, the design system stops being a library and starts being something more like a vocabulary. The agent needs to know not just what to build, but what the result should feel like.

Designers already know how to communicate this. We have moodboards. We have anti-references. We have private vocabularies for the qualities of a thing. The problem is that all of this lives in our heads, in Figma files, on pinned walls. In places agents cannot see.

These protocols are bridges. Each one takes something designers already do, and turns it into a file an agent can read.

If `SKILL.md` is the protocol for craft knowledge, this family is the beginning of a protocol for aesthetic intent. We are going to need a lot more of these before agents can collaborate with creative humans rather than just execute their instructions.

---

## How the protocols relate

```
                 PROCEDURAL                          PERCEPTUAL
              (how to do things)            (what it should feel like)

              SKILL.md                            mood.md
              CLAUDE.md                           vocab.md
              cursor rules                        trace.md
              agent-ready                         critique.md
              design tokens                       taste.md
                  │                                  │
                  └──────────── agent reads ─────────┘
                                  both halves
```

Procedural protocols tell the agent **how to do the work**. Perceptual protocols tell the agent **what the work should feel like when it's done**. An agent with only one half builds competently and wrongly. An agent with both starts to feel like a collaborator.

---

## Roadmap

**Now (v0.1):** mood-protocol, vocab-protocol, and trace-protocol are all live and usable. The family has three working members covering intent (mood), shared language (vocab), and decoded reading of existing work (trace).

**Next:** Real-world use of the three protocols on actual projects, surfacing the vocabulary gaps that need new terms and the integration patterns between them. Cross-references between mood, vocab, and trace files used together in real workflows.

**After that:** critique-protocol and taste-protocol. Sequenced based on what real use of the first three teaches us about the gaps that remain.

This list is a hypothesis, not a contract. The discipline is too young to plan with confidence. Build what's needed, ship it small, learn, keep going.

---

## Contributing

The most useful contributions are:

- **New vocabulary terms** for vocab-protocol. The taxonomy is open and growing. Send a pull request with the term, a one-line definition, two example references, and two anti-references.
- **Worked examples** for any protocol. A moodboard input and the `mood.md` it produces is more useful than any spec. A traced UI and its `trace.md` is the same.
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
