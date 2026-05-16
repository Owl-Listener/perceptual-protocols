# critique-protocol

> Did we land it?

A protocol for closing the loop. Take an actual piece of agent output — a generated draft, a screenshot, a Figma frame, copy, code, whatever — and structure a critique of it against the `mood.md` and `vocab.md` you briefed the work with. The output is a `critique.md`: an anchored, two-sided, actionable aesthetic review that the human and the agent can both read.

Part of the [Perceptual Protocols](../) family.

## What this is for

mood-protocol declares intent. vocab-protocol gives the intent shared language. trace-protocol reads existing work. critique-protocol is the feedback loop that closes the cycle — it asks whether the output actually embodies the intent, and if not, what specifically to change next.

Without it, the family is half-open. You declare a mood, the agent generates, and you just look at the result and feel something. critique-protocol formalises that feeling into a record. Repeatable. Anchored. Improvable.

Four common uses:

**Review your own iteration.** You briefed an agent. It produced something. You see what's off but can't quite say why. The protocol gives you the structure to say it — and a file you can hand back to the agent for the next pass.

**Team critique without the room.** Your collaborator is in another time zone. They can read a `critique.md` and engage with it the way they'd engage with a comment thread on a Figma file. The critique is the meeting.

**Auditing a long-running project.** Run critique-protocol on a year-old surface against a year-old mood. The gap is where the project drifted. The same gap is often the most useful thing in the audit.

**Refining your own intent.** Sometimes the output is fine and the mood was unclear. A good critique surfaces that — and what you thought you wanted gets sharper because of the encounter with what you got.

## How to use it

1. Gather your inputs:
   - The `mood.md` (or `trace.md`) the work was briefed against
   - The `vocab.md` whose terms you used in the brief
   - The output being critiqued — screenshots, copy, links, the actual artifact in whatever form
2. Open Claude, Gemini, or ChatGPT. Upload all of the above.
3. Paste the prompt from [`PROMPT.md`](./PROMPT.md).
4. Save the output as a `critique.md` in your project.
5. Pass the critique back to the next iteration of the work — either to a human collaborator or to the agent itself.

## Output format

The output is a `critique.md`, defined in [`FORMAT.md`](./FORMAT.md). It's a different format from `mood.md` and `vocab.md` because it does a different job — it's a record of a specific assessment moment, not a long-lived intent or vocabulary file.

## How it composes with the family

```
mood.md   ──┐
            ├──► agent generates ──► output ──► critique.md
vocab.md  ──┘                                       │
                                                    ▼
                                          feeds back into
                                          mood.md or vocab.md
                                          (refine for next pass)
```

The interesting thing is that critique.md often feeds *back* into mood.md or vocab.md. A good critique sharpens not just the next iteration of the output, but the next iteration of the intent itself. You discover what you actually meant by encountering the gap between what you said and what came back.

## What this is not

critique-protocol is not a usability audit. It does not score for accessibility, conversion, or affordances. Those are valid concerns and they live in other tools.

This protocol is for the perceptual layer specifically — whether the work feels the way it was meant to feel. Whether the qualities the brief called for actually show up in the output, and where they don't, and what to do about it.

A piece of work can pass critique-protocol with flying colours and still fail a usability test. The two are different jobs.

## A worked example

See [`examples/example-critique.md`](./examples/example-critique.md) for a full `critique.md` of a synthetic AI-generated landing page hero, critiqued against a sample mood and the canonical vocab. Useful as a calibration reference when reading your own first drafts.

## License

MIT — see the family root.
