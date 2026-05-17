# Comparison: mood.md vs trace.md

A quality-by-quality alignment of the brief against the blind reading of the output. This is Step 4 of the trace-triangulation workflow — what survived translation, what didn't, and what the divergences suggest.

## Per-quality alignment (canonical vocabulary)

| Quality (mood.md) | Weight | Present in trace.md? | Trace confidence | Notes |
|---|---|---|---|---|
| `materiality` | primary | partial — token names + one photograph only | **low (unverifiable)** | UI as literally specified is flat colour fields, hairline borders, and a 2px radius. The trace explicitly does not claim materiality as a felt quality, noting it "rides entirely on token names and one unseen photograph, neither of which a flat hex spec can guarantee." |
| `warmth` | primary | partial — rationed | **medium (deferred)** | The trace calls warmth "a promise the design makes, not an ambient condition it delivers." Confined to text colour, one photograph, and one hover state. Static page reads cool. |
| `restraint` | primary | yes | **high** | "The artifact is defined by subtraction. Nearly every spec clause is a prohibition." Anchored to multiple specific spec clauses. |
| `intimacy` | primary | yes | **high** | "Every scale and voice decision narrows the address from a crowd to one reader." Anchored to `max-width: 15ch`, second-person voice, refusal of social proof. |
| `friction` | supporting | partial — rhetorical only | **medium** | "Tonal and verbal, performed, not slowness imposed." Still a single click to "Find your cabin." Friction is the *texture* of slowness, not its imposition. |
| `rhythm` | supporting | partial — inferred | **low–medium** | A defined spatial metre exists in the spacing table, "but a single above-the-fold hero shows only one beat." Vocab frames rhythm as cadence through composition, not present at this scale. |
| `precision` | held in tension | yes — but as joinery only | **medium** | Specification is exacting; the visible page is modest. The trace accepts the artifact's own resolution: "precision is the joinery, never the finish." |
| `density` | anti-anchor | yes (absent, as intended) | **high** | The trace independently identified the artifact as "uncrowded by design" and listed dense dashboards in its anti-references. The anti-anchor held. |
| `irreverence` | anti-anchor | yes (absent, as intended) | **high** | The trace characterised the work as "earnest, not promotional" and listed hype in its anti-references. The anti-anchor held. |

## Per-quality alignment (project-specific terms proposed in mood.md)

| Term | Trace identified? | Notes |
|---|---|---|
| `refuge` | **yes — high confidence** | The trace identified refuge as "the structural spine" of the design, *independently* — calling it out as a quality the canonical vocab.md lacks a word for, and naming it on the artifact's own evidence. This is the strongest result of the experiment: a proposed canonical term that survived translation and was picked up cold by the trace. |
| `patina` | not claimed as embodied | The trace explicitly grouped patina with materiality and declined to claim either as embodied qualities in the rendered page. Both "ride entirely on token names and one unseen photograph." |
| `ember` | yes — as colour discipline | The trace anchored the "one hot point" rule to the photographed window. Ember survived as a structural composition rule, even though the trace called the colour itself `--ember` and treated it as an instance of the broader composition principle rather than its own named quality. |

## Qualities the trace named that mood.md did not ask for

The trace introduced one quality beyond the provided vocab.md — *refuge / enclosure* — and it anchored to the artifact's mechanisms, not to the brief. This was already anticipated by mood.md as a proposed new term, so it counts as a convergent finding rather than a divergence.

No other qualities appeared in the trace that the brief hadn't named or anticipated.

## Tensions the output explicitly resolved

The output.md's "Tensions & trade-offs" section named four tensions and committed on which value led:

| Tension | Which led | Trace observation |
|---|---|---|
| friction vs. conversion convention | friction | The trace accepts this as deliberate; the entire CTA section, button padding, and copy register support it. |
| ember (one hot point) vs. CTA affordance | ember | The trace independently identified the single-hot-point discipline as a structurally encoded choice. |
| precision vs. patina / materiality | patina | The trace verifies precision as joinery only; patina/materiality not embodied in the spec, only named. |
| intimacy vs. crowd-facing hero | intimacy | Verified at multiple levels (scale, voice, refusal of plurality). |

The fact that the output named its own tensions was itself a methodological observation in the trace — it noted that this contaminates the trace's ability to detect those qualities independently. The trace handled this by anchoring every reading to a concrete described *mechanism* rather than to the author's prose claims.

## Summary

Of the ten qualities the brief named (seven canonical, three proposed):

- **Three transferred at high confidence:** `restraint`, `intimacy`, `refuge`. These were structurally encoded in the output's mechanisms, not just asserted in its prose.
- **Three transferred partially or rhetorically:** `warmth`, `friction`, `precision`. Present as language, hover states, or specification rigour — but rationed against the dominant cool surface or limited to non-felt levels.
- **Two were not embodied in the visible UI:** `materiality`, `patina`. They lived in token naming and one photograph, not in the renderable spec.
- **Two were correctly held as anti-anchors:** `density`, `irreverence` — both absent, as intended.
- **One (rhythm) was insufficient signal:** A single hero is too thin a surface to show cadence; the trace flagged this honestly rather than claiming what wasn't there.

The asymmetry is the most important finding. **Not every quality the brief named survived specification into a flat-UI hero.** The brief's primary quality (`materiality`) was its weakest carrier in the output — because flat hex tokens and hairline borders cannot embody materiality on their own; that quality requires assets (the photograph) and implementation (texture, grain, weight) the spec couldn't supply.

The strongest single-quality finding was the validation of `refuge` — proposed by mood-protocol, structurally encoded in output, picked up independently by trace. That's three independent runs converging on the same term. It's the closest thing to canonical-vocabulary validation evidence the family has produced.

See [LEARNINGS.md](./LEARNINGS.md) for what these findings suggest for the family — proposed updates to canonical vocab.md, a documented translation gap for `materiality`, a methodological recommendation about brief-execution prompts, and an open epistemological question about the trace step's contamination risk.
