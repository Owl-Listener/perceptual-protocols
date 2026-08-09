# Perceptual Protocols

> This project is all about how things should feel.

We've spent the last two years building increasingly sophisticated ways to give AI agents procedural knowledge. How to write CSS. How to follow a design system. How to obey our rules. Owl-Listener contains a lot of procedural design skills and methods that are all machine readbale and made for producing great design with LLMs. This collection is more about telling the LLM how things should feel with great accuracy so you can get rich and meaningful outcomes.

Designers, musicians, writers, architects, and every creative human spend their career cultivating, is **perceptual**. Taste. Judgement. The ability to look at something and know it is wrong before you can articulate why. We've been encoding the **how** and ignoring the **what it should feel like**.

This is a family of protocols for this.

---

## What's in here

Each protocol does one thing and stops. Each one outputs a plain markdown file that any agent — Claude, Gemini, ChatGPT, Cursor, Copilot — can read. They work alone, but they compose into a complete workflow when used together.

| Protocol | What it does | Output | Status |
|---|---|---|---|
| [mood-protocol](./mood-protocol) | Declare what the product should feel like, from visual references | `mood.md` | Released (v0.1) |
| [vocab-protocol](./vocab-protocol) | Share a vocabulary for the static qualities you mean | `vocab.md` | Released (v0.1) |
| [motion-protocol](./motion-protocol) | Share a vocabulary for how the product should move | `motion.md` | Released (v0.1) |
| [voice-protocol](./voice-protocol) | Specify how the brand writes — personality, register, mechanics | `voice.md` | Released (v0.1) |
| [listen-protocol](./listen-protocol) | Author a brief from audio references; share sound vocabulary | `listen.md` + `sound.md` | Released (v0.1) |
| [situation-protocol](./situation-protocol) | Weight the qualities differently by context | `situation.md` | Released (v0.1) |
| [tokens-protocol](./tokens-protocol) | Annotate the design system you already have with intent | `tokens.md` | Released (v0.1) |
| [trace-protocol](./trace-protocol) | Read an existing UI and capture its implicit mood | `trace.md` | Released (v0.1) |
| [critique-protocol](./critique-protocol) | Critique agent output against the brief | `critique.md` | Released (v0.1) |
| `taste-protocol` | Capture a designer's persistent preferences across projects | `taste.md` | Planned |

The order tells the story of how the system runs. Declare intent (visual, then sonic). Share vocabulary across static, motion, verbal, and sound modalities. Encode conditional weighting. Annotate the system once one exists. Read existing work. Close the feedback loop.

**One repo.** `mood-protocol`, `voice-protocol`, and `tokens-protocol` used to live in separate repositories. They don't any more — they're folders in here, alongside the rest of the family. The old repositories are archived and still resolve, so existing links keep working, but this is the only place any of them are maintained.

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

From that moment on, any agent that can read your project can read your mood. As you adopt the other protocols, they read alongside it. If you also work with audio — a soundtrack, a recorded place — `listen-protocol` produces a parallel brief from sound that the agent reads together with mood.md.

---

## Install

There is one install, and it is copying markdown files into your project. Pick whichever of these you prefer; they do the same thing.

**By hand.** Open the folder for the protocol you want, copy its template file into your project root, and rename it to lowercase — `vocab-protocol/VOCAB.md` becomes `vocab.md`, `voice-protocol/VOICE.md` becomes `voice.md`, and so on. This is the canonical path and it will always work.

**With the script.** For the case where you want several at once:

```bash
git clone https://github.com/Owl-Listener/perceptual-protocols
cd perceptual-protocols
./install.sh --into ~/projects/my-app vocab voice tokens
```

Run `./install.sh --list` to see what's available, or `./install.sh --into <dir> all` to take everything. It is POSIX shell, it copies files and nothing else, it never overwrites without `--force`, and it makes no network calls. If it ever does more than that, it has become a dependency and should be deleted.

**What you end up with**, in your project root:

```
my-app/
├── mood.md         ← what it should feel like
├── vocab.md        ← what the words in mood.md mean
├── voice.md        ← how it writes
├── tokens.md       ← what the design system means
└── ...
```

Then point your agent at them: add them to `CLAUDE.md`, your Cursor rules, your system prompt, or just say *"read mood.md and voice.md before you start"*. There is no build step, no schema, no validator, and nothing to keep running.

---

## What makes these a family

Six principles. All six apply to every protocol in here.

**Human-curated, not AI-generated.** These are not tools that generate taste for you. They are tools that capture and share the taste you already have, so an agent can apply it.

**Markdown, always.** The output is plain `.md`. Portable, versionable, agent-readable, human-readable. No proprietary formats. No lock-in. Git can diff your taste.

**Model-agnostic.** Anything that can read text can use these. Claude, Gemini, ChatGPT, Cursor, Copilot, the model you'll be using in two years.

**Single-purpose.** Each protocol does one thing and stops. mood-protocol is not vocab-protocol is not voice-protocol is not tokens-protocol. They compose. They do not bloat.

**No setup is the default.** If a designer can't use a protocol in sixty seconds with the AI they already have, the protocol has failed. There can be a script for power users, but the prompt and the format spec are the canonical path.

**Anti-references are first-class.** Knowing what to avoid carries as much information as knowing what to pursue. "NOT corporate dashboard" closes off an entire territory of bad decisions. Every protocol that handles taste handles its opposite — including the ones that look like specifications. `voice.md` pairs every descriptor with the line it doesn't cross; `tokens.md` gives every token a "do not use for."

---

## The argument behind this

You can use these without reading this section. But it is the reason they exist.

For most of computing history, the interface had to be designed for reuse. A design system was an artifact of scarcity. You couldn't afford to make a different interface for every person at every moment, so you built one carefully and shipped it to everyone. Polish was the proof of care.

That world is ending. Generative interfaces are arriving. Fluid, personalised, regenerated for each user in the moment of use. When the interface is made on the fly, the design system stops being a library and starts being something more like a vocabulary. The agent needs to know not just what to build, but what the result should feel like, how it should move, how it should sound, how it should talk, and how that feeling should adapt to who is looking and when.

Designers already know how to communicate this. We have moodboards. We have anti-references. We have playlists. We have private vocabularies for the qualities of a thing. We have tone-of-voice decks and token libraries. We have implicit knowledge about how a clinical dashboard should feel different from a patient portal, and how a snappy product moves differently from a calm one, and how a bossa nova playlist shapes the design differently from a punk one. The problem is that all of this lives in our heads, in Figma files, on pinned walls, in PDFs, in personal Spotify libraries. In places agents cannot see.

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
              cursor rules                        motion.md
              agent-ready                         sound.md
              design tokens                       listen.md
                    │                             voice.md
                    │                             situation.md
                    │                             trace.md
                    │                             critique.md
                    │                                  │
                    └──────────► tokens.md ◄───────────┘
                              values from the left,
                              intent from the right
                                       │
                                       ▼
                            agent reads all of it
```

Procedural protocols tell the agent **how to do the work**. Perceptual protocols tell the agent **what the work should feel like when it's done** — visually, temporally, sonically, and verbally. An agent with only the procedural half builds competently and wrongly. An agent with both starts to feel like a collaborator.

`tokens.md` is the one file that sits in the join. Your design tokens are procedural — they're values a machine can already read. `tokens.md` annotates them with the intent that never made it into the JSON. It is the handoff point between the two halves, which is why it arrives late in a project and why it is the protocol most likely to drift.

---

## The design.md story

Google Labs published [`DESIGN.md`](https://github.com/google-labs-code/design.md) in April 2026 — a single manifest for brand and system, with YAML tokens, components, and established visual identity in one file. It's a good idea, and the obvious question is why this family isn't just that file.

The answer is that `DESIGN.md` bundles three jobs that have different lifecycles.

| The job | When it's true | This family |
|---|---|---|
| What should this feel like? | Week one, before a system exists | `mood.md`, `vocab.md` |
| How does the brand talk? | Once, then slowly drifts | `voice.md` |
| What does the system mean? | Only once there is a system | `tokens.md` |

Bundling them means the file can't be written until the slowest part is ready — you can't fill in the tokens section in week one, so the intent doesn't get written down either, so the system gets built without it. That's the failure this family is designed around. `mood.md` exists precisely so there is something to write before there is anything to specify.

So a typical project runs the arc rather than the file. Generate `mood.md` from moodboards in week one. Write `voice.md` as soon as there's copy worth describing. Derive tokens in week three and annotate them with `tokens.md`. Run all of it alongside `CLAUDE.md` for the rest of the build.

If you already have a mature design system and a settled brand, `DESIGN.md` is a reasonable single file and you should use it. This family is for the part of a project where the system doesn't exist yet, and for the fact that intent keeps mattering after it does.

---

## Composing as a system

The nine released protocols are not nine discrete tools. They compose into a workflow with three input layers, a system layer, a synthesis step, a feedback loop, and an analytical channel.

```
    AUTHORING LAYER          SHARED VOCABULARY         CONDITIONAL LOGIC
   from your own sources      vocab.md  (static)         situation.md
   mood.md   (visual)         motion.md (temporal)            │
   listen.md (audio)          sound.md  (sonic)               │
                              voice.md  (verbal)              │
                                                              │
                          ┌───────► agent reads any ◄─────────┤
                          │       combination of these
                          │           ↓
                          │       tokens.md
                          │    (the system layer — present
                          │     once a system exists)
                          │           ↓
                          │     generates the work
                          │           ↓
                          │       critique.md ──► feeds back
                          │                       into the brief
                          ↓
                   (trace.md reads existing
                    work into the same formats —
                    an analytical inverse)
```

The architecture has three input layers:

- **Authoring layer** — `mood.md` (from your visual references) and `listen.md` (from your audio references). Both are briefs you author from sources that mean something to you.
- **Shared vocabulary** — `vocab.md`, `motion.md`, `sound.md`, `voice.md`. Four perceptual modalities (static, temporal, sonic, verbal), four vocabularies the briefs use to anchor their language. Designed to compose.
- **Conditional logic** — `situation.md`. Weights the vocabulary differently by context.

Then a system layer (`tokens.md`) once there is a system to annotate. Then a generation step. Then a feedback loop (`critique.md`) that can sharpen any of the input layers for the next iteration. And `trace.md` as a parallel channel that reads existing artifacts into the same formats — useful for competitive analysis, brand archaeology, and self-audit.

The point of building it this way is that no protocol has to do all the work. Each one is small. Together they are sufficient.

## Four vocabularies, one identity

`vocab-protocol`, `motion-protocol`, `voice-protocol`, and `sound.md` (which lives inside listen-protocol) are sibling vocabularies. They produce different files because they describe different perceptual layers — what the product looks like still, how it moves, how it sounds, and how it talks. Each can be present in the same project brief.

A coherent identity uses all four to reinforce each other. Linear's static identity (precise, restrained, dense) and motion identity (snappy, mechanical, invisible) reinforce each other — the same brand expressed in two registers, and its writing is recognisably the third. A brand briefed from Brian Eno's *Music for Airports* would inherit a sound identity (spacious, pulseless, long-decayed) that implies a static identity (warmth, restraint, generous whitespace), a motion identity (calm, glassy, invisible), and a verbal identity that would never use an exclamation mark — four modalities composing into one perceptual posture.

Some products deliberately contradict themselves between the layers. That's a design choice too, and the protocols let you specify it explicitly. The vocabularies don't enforce coherence; they make coherence (or its deliberate absence) visible and discussable.

---

## Closing the loop: does the brief actually work?

The honest open question with any perceptual brief is whether the agent's output actually embodies the intent. critique-protocol is a partial answer — it gives you a structured way to read the output against the brief. But critique-protocol has a circularity: it uses the brief's own vocabulary to assess the output, so a passing critique might just mean *the output is self-consistent with the brief*, not that it *actually feels the way the brief asked for*.

The exit is **trace-protocol triangulation.**

The workflow:

1. Author your `mood.md` (and/or `listen.md`, plus `vocab.md`, optionally `motion.md`, `sound.md`, `voice.md`, and `situation.md`).
2. Brief the agent with these files. Generate the output.
3. Run **`trace-protocol` on the output — without giving the trace agent your `mood.md`.** Let it read the output cold.
4. Compare the resulting `trace.md` to your original `mood.md`, quality by quality.

Where the two documents agree, the brief survived translation to output. Where they diverge, the diverging qualities are exactly the ones the agent didn't deliver — and those gaps are immediately actionable for the next iteration.

The reason this breaks the circularity is that the trace doesn't read the brief. It reaches for vocabulary based on what it sees in the output, not on what was asked for. Even though both protocols share the same `vocab.md`, the evaluation happens through cross-document comparison, not self-affirmation. The two documents have to meet in the middle on their own.

For stronger validation, run the trace with a **human** in the place of the agent — a designer who hasn't seen your `mood.md`. If their unprompted reading of the output matches the brief, the work landed. If their reading diverges in interesting ways, you've learned something about either the output, the brief, or both.

This is a workflow, not a protocol. It composes existing parts of the family. If the manual diff between `mood.md` and `trace.md` gets tedious enough in real use, we'll consider a small `alignment-protocol` that automates the comparison. For now, the README is the spec.

See [TUTORIAL.md](./TUTORIAL.md) for a hands-on walkthrough of running the trace-triangulation workflow on a real project. The first real-world worked example lives at [trace-protocol/examples/2026-05-17-char-and-ember](./trace-protocol/examples/2026-05-17-char-and-ember).

---

## Roadmap

**Now (v0.1):** Nine working protocols cover the project-level perceptual workflow end to end, in one repository. Declare intent from visual references (mood) or audio references (listen). Share vocabulary for static (vocab), temporal (motion), sonic (sound), and verbal (voice) qualities. Weight by context (situation). Annotate the design system once it exists (tokens). Read existing work (trace). Close the loop on output (critique). And: a documented validation workflow that uses the family's own pieces to test whether the brief is actually working.

**Next:** Real-world use of the nine protocols on actual projects. Surfacing the vocabulary gaps that need new terms across all four modalities, the situation patterns that recur across products, the cross-modal translation patterns that hold up under iteration, and the integration moves that make the family work together. Worked examples for each protocol drawn from real (not synthetic) projects. Empirical testing of the trace-triangulation workflow. Evidence on whether `tokens.md` actually stays in sync in practice, or whether the drift problem needs tooling rather than discipline.

**After that:** taste-protocol, a designer-personal cross-project preferences layer that sits above the project-scoped protocols. Sequenced for after the project-level protocols have been road-tested. Possibly `alignment-protocol`, if the manual trace-diff workflow proves valuable enough to formalise. Possibly cross-modal validation tooling — the trace-triangulation workflow needs extension for cases where the brief is sonic but the output is visual.

This list is a hypothesis, not a contract. The discipline is too young to plan with confidence. Build what's needed, ship it small, learn, keep going.

---

## Contributing

The most useful contributions are:

- **New vocabulary terms** for `vocab-protocol`. The taxonomy is open and growing. Send a pull request with the term, a one-line definition, two example references, and two anti-references.
- **New motion terms** for `motion-protocol`. Same bar as vocab terms, with the additional requirement of technical anchors (durations, easing, gesture response).
- **New sound terms** for `sound.md` inside listen-protocol. Same bar, with technical anchors where applicable (frequency range, dynamic range, reverberation time).
- **Voice mechanics that generalise** for `voice-protocol`. Rules that are enforceable across brands rather than specific to one — the kind a reviewer could apply without asking the author.
- **Token usage rules that recur** for `tokens-protocol`. The "do not use for" column is where the value is, and the common misuses are common across products.
- **Situation patterns** for `situation-protocol`. Common context families that recur across products (healthcare, finance, government, education) are especially valuable.
- **Worked examples** for any protocol. A real `mood.md`, `vocab.md`, `motion.md`, `voice.md`, `listen.md`, `situation.md`, `tokens.md`, `trace.md`, or `critique.md` from your own work is more useful than any spec.
- **Trace-triangulation case studies.** If you've run the validation workflow on a real project, write up what you found — which qualities transferred to output, which didn't, and what you learned about either the brief or the agent.
- **Cross-modal case studies.** If you've used `listen-protocol` to brief a visual project (or vice versa), write up how the cross-modal translation actually held up. We have very little empirical data here yet.
- **New protocols.** If you've found a gap, something designers do that agents can't yet see, open an issue. Sketch the format. We'll figure out together whether it belongs in this family or somewhere else.

Each sub-protocol's `FORMAT.md` is the spec its contributions are held to.

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
- Brian Eno — A Year With Swollen Appendices and the *Music for Airports* liner notes. 

The longer reading list with notes lives in `READING.md`.

---

## License

MIT. See [LICENSE](./LICENSE).

---

## About

Built by [MC Dean](https://marieclairedean.substack.com), part of the [Owl-Listener](https://github.com/Owl-Listener) collection. Small, opinionated protocols for designers building with AI.

We are still in the early days of teaching machines to see what we see, hear what we hear, and feel what we feel. The interesting work is in the translation.

If you make something with these, I want to hear what happens.
