# Tutorial: Running the perceptual-protocols family on a real project

This is a hands-on walkthrough. By the end, you'll have run a complete trace-triangulation experiment — authored a brief from your own references, used it to generate work, traced that work blind, and compared the two to learn what your brief actually transfers to output.

The tutorial uses Claude Code in the terminal as the working surface, but the workflow translates to any AI tool that handles images and writes files. It assumes about 30–45 minutes for a first run.

## What you'll learn

- How to author a `mood.md` from a moodboard of your own references
- How to brief an AI agent against that mood and capture the output
- How to run a blind trace of the output, separately, and compare it against your brief
- How to read the comparison — what survived translation, what didn't, what to change next time

## What you'll need

- A small set of references for one project — 3–5 images that cohere aesthetically. A Pinterest board, a Figma frame, screenshots from products you admire, anything visual you can upload.
- A clone of the perceptual-protocols repo locally:
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/Owl-Listener/perceptual-protocols.git
  ```
- An AI tool with vision and file-writing capability. The instructions below assume [Claude Code](https://docs.claude.com/en/docs/claude-code), but any equivalent tool works.

---

## Part 1: Set up the experiment

The whole experiment lives in one folder, organised so each step has its own working directory. The directory isolation isn't cosmetic — it's how you enforce the blind constraint in Step 3.

```bash
EXP=~/your-projects/perceptual-protocols-experiments/$(date +%Y-%m-%d)-experiment-name
mkdir -p "$EXP"/{inputs,01-mood,02-output,03-trace,04-compare}
cd "$EXP"
```

Place the canonical vocabulary where every step can find it:

```bash
cp ~/code/perceptual-protocols/vocab-protocol/vocab.md inputs/
```

You're now ready to bring in your references. You can either:
- **Save them to `inputs/`** for permanent record (recommended if you're keeping this as a case study)
- **Drag them directly into Claude Code in the next step** (faster for a first try)

Either works. The references go through Claude's vision, not through filesystem reads.

---

## Part 2: Author your brief — `mood.md`

This is Step 1 of the workflow: produce a structured brief from your references.

```bash
cd "$EXP"/01-mood
cp ../inputs/vocab.md .
claude
```

In Claude Code, drag your reference images into the window (they attach as image content to your next message). Then send:

> *I'm running step 1 of a perceptual-protocols experiment. The images I just attached are references for a project's perceptual identity.*
>
> *1. Read `./vocab.md` — the canonical perceptual vocabulary.*
> *2. Read `~/code/perceptual-protocols/mood-protocol/PROMPT.md` for the mood-protocol extraction prompt.*
> *3. Apply that prompt to the attached references, anchoring to vocab.md terms where they genuinely fit and proposing new ones only where the canonical set doesn't cover what you see.*
> *4. Save the resulting mood.md as `./mood.md` in the current directory.*
>
> *Be opinionated. A vague mood.md will produce a vague experiment.*

Claude will produce a `mood.md`. Read it carefully:

```bash
cat mood.md
```

**This step matters more than any other in the experiment.** If you start with a brief you don't believe, you're not testing whether the family works — you're testing whether a bad brief produces bad output (it will).

If the brief doesn't capture what you actually see in the references, push back in the same conversation:

> *The warmth reading is too generic. Look at the second image specifically — the warmth lives in the hand-lettered annotations. Anchor it there. Also, you missed the materiality of the textured paper. Add it.*

Iterate until the mood.md feels right.

> **Example from a real run:** In the *Char & Ember* experiment (Pinterest references of off-grid cabins), the brief opened with: *"A small dark box set against a cold wild landscape, with a single orange fire burning inside it."* One sentence doing the work of a thousand mood-board captions. That's the kind of compression a good brief produces.

When the mood.md is solid, exit Claude:

```
/exit
```

---

## Part 3: Brief an agent to produce output

This is Step 2: hand the brief to an agent and ask it to make something.

```bash
cd "$EXP"/02-output
cp ../01-mood/mood.md .
cp ../inputs/vocab.md .
claude
```

**Pick your test artifact carefully.** The product or surface you ask the agent to design should be plausibly compatible with the mood — not so on-the-nose that the agent can produce the mood from the product type alone, but not so mismatched that the brief is being asked to do something impossible.

For most moods, a **landing page hero** is a clean test artifact:
- Small enough to be coherent
- Has multiple perceptual decisions (copy, type, colour, layout)
- Produces text the trace step can read
- Easy for any designer to judge

Send the brief execution prompt:

> *I'm running step 2 of a perceptual-protocols experiment. You have two files in the current directory:*
>
> *- `mood.md` — the perceptual brief for this project*
> *- `vocab.md` — the shared vocabulary the brief uses*
>
> *Please read both carefully. They are the only source of truth for what the work should feel like.*
>
> *Then design the landing page hero for [your product]. Treat the mood.md as the brief; do not improvise mood from the product category.*
>
> *Produce all four of the following:*
>
> *1. Headline copy*
> *2. Subhead copy*
> *3. CTA button copy*
> *4. A detailed visual treatment description — typography (face, weight, size, alignment), colour palette (with anchors to mood.md qualities), spatial layout, imagery direction, button treatment, background, white-space behaviour. Be specific enough that a developer could implement from your description.*
>
> *Make decisions that visibly embody the perceptual qualities the mood.md describes. If two qualities in the brief are in tension, make a deliberate trade-off and say which one led and why.*
>
> *Save the complete output as `output.md` in the current directory. Do not include commentary outside the four deliverables.*

When it's done:

```bash
cat output.md
```

Don't iterate this one. Record the first response. The whole point is to see what the brief produces unsupervised.

> **A note on what to ask the agent to produce.** The example above asks for a *written description* of a hero. That's a tractable v0.1 test — text-to-text fidelity is highest. As the family matures, you may want to test against richer outputs (rendered HTML, generated images, actual Figma frames). Just remember that the trace step will need to read whatever you produce.

Exit Claude:

```
/exit
```

---

## Part 4: Run the blind trace

This is the critical step. It's where the experiment becomes a real test rather than self-affirmation.

The whole point of trace-triangulation is that trace-protocol reads the output **without seeing the original brief** — so any qualities it identifies are qualities the *output itself* communicates, not qualities the trace was told to look for. The blind is what breaks the circularity.

To enforce the blind, the trace works from a directory containing **only** the artifact, the shared vocabulary, and the trace-protocol prompt — but **not** the mood.md.

```bash
cd "$EXP"
cp 01-mood/output.md 03-trace/
cp inputs/vocab.md 03-trace/
ls 03-trace/
```

You should see exactly two files: `output.md` and `vocab.md`. **No `mood.md` in this directory.** If you see one, delete it before proceeding.

Now — and this is essential — **start a fresh Claude Code session**. Not `/clear`, not "continue." A new session. The blind has to be enforced both at the filesystem level and at the context level.

```bash
cd 03-trace
claude
```

**First message — set the constraint before anything else.** Claude Code can read across the filesystem, and might helpfully reach for `../01-mood/mood.md` if you don't tell it not to:

> *I am running a blind perceptual trace experiment. You have access only to the files in the current directory (`03-trace/`). Do not read any files outside this directory under any circumstances, including files in sibling directories. Confirm you understand this constraint before proceeding.*

Wait for Claude to confirm. **This is the moment that makes the experiment valid.** If you skip it, you're not running trace-triangulation — you're running confirmation bias.

Then send the trace prompt:

> *Read the files in this directory:*
>
> *- `output.md` — a detailed description of a landing page hero design produced by another agent. Treat this as the artifact to trace.*
> *- `vocab.md` — the shared perceptual vocabulary you may use.*
>
> *Then read `~/code/perceptual-protocols/trace-protocol/PROMPT.md` for the trace-protocol extraction prompt.*
>
> *Apply that prompt to the hero design described in output.md. Produce a `trace.md` that captures, in your own reading, what this design implicitly feels like — what perceptual qualities it embodies, anchored to specific elements of the description. Be specific. Do not infer qualities the description doesn't support.*
>
> *Save the output as `trace.md` in the current directory.*

When it's done:

```bash
cat trace.md
```

Exit:

```
/exit
```

---

## Part 5: Compare and interpret

You now have the two documents the experiment is testing:

- `01-mood/mood.md` — your brief
- `03-trace/trace.md` — a blind reading of what the output actually communicates

Compare them quality by quality. You can do this by hand, or hand both to Claude in a fresh session for a structured comparison:

```bash
cd "$EXP"/04-compare
cp ../01-mood/mood.md .
cp ../03-trace/trace.md .
claude
```

> *Please read `mood.md` (the brief I authored) and `trace.md` (a blind reading of the agent's output against that brief).*
>
> *Produce a `comparison.md` that does the following:*
>
> *1. For each perceptual quality named in mood.md, note whether it appears in trace.md — either by name or via a clearly-mapped term.*
> *2. List qualities the trace mentions that mood.md did not ask for.*
> *3. Identify any tensions in mood.md that the agent appears to have silently resolved one way or the other.*
> *4. Summarise: which qualities reliably transferred to the output, which didn't, and what that suggests about either the brief, the agent, or the medium.*
>
> *Save as `comparison.md`.*

### What the patterns mean

Three patterns to watch for:

**Qualities that consistently survived.** These are the ones the brief reliably renders. You can brief in them with confidence in future projects.

**Qualities that became rhetorical rather than embodied.** A quality might appear in the *language* of the output (the copy talks about being warm) but not in the *mechanisms* (the actual UI is flat and cool). This is one of the family's most interesting findings — some qualities transfer as *naming* and *promise*, but require assets or implementation to actually deliver.

**Qualities that didn't transfer at all.** These tell you where the brief needs sharpening, where the canonical vocabulary needs a stronger anti-reference, or where the output medium you chose can't carry the quality (you can't show motion in a still description; you can't show materiality in a flat-colour spec).

A **passing experiment** doesn't mean every quality transferred perfectly. It means the trace produced *honest, actionable* readings that you can use to iterate the brief.

> **Example from a real run:** In the *Char & Ember* experiment, the trace found that `refuge` was the structural spine of the output — even though `refuge` wasn't in the canonical vocab.md. This was direct evidence that the proposed new term should be promoted to canonical. The same experiment found that `materiality` (a primary canonical quality) didn't transfer to the visible UI — it lived in token names and one photograph, not in the actual rendered surface. That's the kind of finding that changes how the vocabulary documents itself.

---

## Common pitfalls

**Running the trace in the same Claude session as the brief.** Claude can self-discipline if you tell it to, but the blind is much cleaner with a genuinely fresh session in a directory that doesn't contain `mood.md`. The filesystem isolation matters.

**Iterating the output before tracing it.** Resist the urge to ask the agent to "make it better" after the first try. The whole experiment is about what the brief produces *unsupervised*. Save the iteration for after you have the trace findings.

**Naming the qualities in the output itself.** If the brief-execution prompt encourages the agent to *name* the qualities it's trying to embody ("write a 'tensions and trade-offs' section"), the trace step has to do extra work to discount author prose vs structural mechanisms. For cleaner traces, ask the agent to *embody* qualities in the output and save the naming for critique-protocol.

**Picking an unachievable product for the mood.** If the mood is for an intimate, restrained off-grid cabin product but you ask the agent to design a SaaS conversion funnel, the brief will fight the category. Pick a product the mood plausibly fits.

**Treating a passing trace as proof the brief works perfectly.** The trace tells you what the output *communicates*. It doesn't tell you whether real users would perceive the qualities the same way, or whether implementation would preserve them. The trace is a strong signal, not a final verdict.

---

## What to do with your findings

Each experiment produces three kinds of useful output:

**Iterations to your brief.** If qualities didn't transfer, you have specific places to sharpen the mood.md — better anti-references, more concrete anchors, explicit guidance on tensions.

**Candidates for canonical vocabulary updates.** If you proposed a new term in your mood.md and the trace independently identified it as central, that's evidence the term belongs in canonical `vocab.md`. Send a pull request to the family root.

**Case studies for the family.** Real experiments are more useful than synthetic examples. Copy your `experiment-name/` folder into `perceptual-protocols/trace-protocol/examples/your-experiment-name/` and PR it. Include a `LEARNINGS.md` capturing what transferred, what didn't, and what you'd change next time.

---

## Where to go next

- **[mood-protocol](./mood-protocol)** — full documentation of the brief format
- **[vocab-protocol](./vocab-protocol)** — the canonical vocabulary and how to extend it
- **[motion-protocol](./motion-protocol)** — extend your brief to cover how the product should *move*, not just how it looks
- **[situation-protocol](./situation-protocol)** — encode conditional weighting if your product has multiple contexts (clinical dashboard vs patient portal, etc.)
- **[critique-protocol](./critique-protocol)** — for ongoing assessment of agent output during a project, not just one-shot validation
- **[trace-protocol](./trace-protocol)** — full documentation of what trace-protocol does, including the worked Linear example

The tutorial above used `mood`, `vocab`, and `trace`. Once those feel natural, the other three protocols extend the workflow in obvious ways. None of them require you to have used the others first.

---

## A final note

The family is young. The protocols work, but they're not finished — your experiments are how they get better. If you run a trace-triangulation and learn something unexpected, write it up. If you find a quality the canonical vocabulary doesn't name, propose it. If you find a category where the workflow breaks down, open an issue.

This is research as much as it is tooling. The interesting work is in what we find when designers actually run these on their own briefs, with their own references, and see what the data says back.
