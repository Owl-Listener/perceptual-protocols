# Char & Ember — a real-world trace-triangulation experiment

A worked example of running the full trace-triangulation workflow on a real designer's references. This is the first non-synthetic case study in trace-protocol's examples folder.

## What this example shows

A complete experimental loop, end to end:

1. A designer (MC Dean) loaded a Pinterest moodboard of off-grid cabin references into Claude Code.
2. The mood-protocol prompt was used to extract a structured `mood.md` from those references — anchored to the canonical perceptual vocabulary, proposing three new project-specific terms (`refuge`, `patina`, `ember`).
3. The mood.md was used as the brief for an AI agent designing a landing page hero for a single-occupancy cabin booking platform. The agent produced a detailed `output.md`.
4. A trace was run on the output (with the methodological caveats noted below) to read what perceptual qualities the output actually communicated, blind to the original brief.
5. The two documents were compared. The findings are documented in the summary at the end of `comparison.md`.

## Files in this folder

- `README.md` — this file
- `mood.md` — the brief extracted from the Pinterest moodboard (Step 1 output)
- `output.md` — the landing page hero design produced from the brief (Step 2 output)
- `trace.md` — the blind reading of the output (Step 3 output)
- `comparison.md` — a quality-by-quality alignment between mood.md and trace.md, and the findings (Step 4 output)
- `moodboard-01.png`, `moodboard-02.png` — the Pinterest references the brief was extracted from

## Why this example matters

Before this run, the trace-protocol family had only one worked example — a synthetic decoding of Linear's interface. That example demonstrated the *format* but not the *epistemology*: nobody had actually used the family to test whether a brief authored from a moodboard transfers to agent output.

This experiment is the first evidence we have. It validated one proposed canonical term (`refuge`), identified a translation gap for the family's most-used term (`materiality`), and surfaced a methodological recommendation about how to structure brief-execution prompts. All three findings are documented in the summary at the end of `comparison.md`.

It also failed in a useful way: the trace step was not fully blind. The implications of that partial failure are part of what makes the example instructive.

## Methodological caveats (read these before drawing conclusions)

**The trace was run in the same Claude Code session as the brief authoring and brief execution.** This means the model had the full conversation history available — including the original mood.md and Pinterest references — when producing the trace. The model self-disciplined explicitly (*"anchored only to lines in output.md, not imported from mood.md"*) and the trace.md is rigorous about distinguishing the artifact's mechanisms from the author's prose. But for a fully clean trace-triangulation, the next iteration of this experiment would use a genuinely separate session, ideally with no filesystem access to the mood.md from any sibling directory.

**The trace is of a written specification, not of a rendered page.** The output.md is a detailed visual treatment document, not actual rendered HTML or CSS. This means we're testing whether the brief transferred to a specification, which is one step removed from whether it transferred to actual implementation. The trace flags this caveat repeatedly: *"this is a trace of a specification, not of pixels."*

**The output.md included a "Tensions & trade-offs" section that named the very qualities the trace was meant to detect.** This required the trace to discount claims supported only by author prose and anchor every reading to a concrete described mechanism. The trace did this carefully — but the methodological lesson is that future brief-execution prompts may want to ask the agent to *embody* qualities without *naming* them in the output.

These caveats do not invalidate the findings — they bound them.

## How to read this example

Recommended order:

1. **Start with this README** — for context.
2. **Read `mood.md`** — to see what a substantive brief looks like when extracted from a real moodboard.
3. **Read `output.md`** — to see what the agent produced from the brief.
4. **Read `trace.md`** — to see what an honest, anchored, confidence-graded blind reading looks like.
5. **End with `comparison.md`** — for the quality-by-quality alignment between brief and trace, and the findings in its closing summary.

If you only have time for two files, read `mood.md` and the summary at the end of `comparison.md`. The brief shows what good looks like; the summary shows what the experiment proved.

## Reproducing this experiment

The directory structure used was:

```
2026-05-17-pinterest-test/
├── inputs/             (Pinterest screenshots + canonical vocab.md)
├── 01-mood/            (mood.md produced here)
├── 02-output/          (intended location; the agent saved output.md in 01-mood/)
├── 03-trace/           (output.md + vocab.md + trace.md, blind setup)
└── 04-compare/         (comparison.md)
```

See [TUTORIAL.md](../../../TUTORIAL.md) at the family root for step-by-step instructions on running your own version. If you do, please contribute the result back as another worked example.

## Contributing

This example is intentionally imperfect — the methodological caveats are part of its value. If you run a cleaner version (genuinely blind trace, different model for the trace step, a rendered output rather than a specification), please contribute it as another folder in this directory. Several variations would teach us more than one perfect example.
