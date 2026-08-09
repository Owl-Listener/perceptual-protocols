# Situations: Synthetic hospital product

**Source:** Worked example for situation-protocol v0.1. A synthetic hospital product, designed to demonstrate how a single brand identity should weight its qualities differently across distinct situations.

**Baseline:** This product's `mood.md` describes a hospital that is warm, precise, restrained, authoritative, and intimate. Across every situation, the brand never abandons any of these qualities entirely — what changes is which ones lead.

**Vocabulary used:** Canonical [`vocab.md`](../../vocab-protocol/VOCAB.md) from the perceptual-protocols family.

This is a worked example of a `situation.md`. Useful as a calibration reference when reading your own first drafts. The file below shows what good output looks like — opinionated, anchored, and willing to name tensions.

---

## Patient portal

**When this applies:** The user is a patient, a family member, or a caregiver. The surfaces are public or post-login consumer pages — login, appointment scheduling, secure messaging, billing-as-patient, health records browsing, education content. The user is often in a vulnerable or anxious state and is using a consumer device, often on a phone, sometimes one-handed.

**Weighted qualities:**
- warmth: HEAVY
- intimacy: HEAVY
- restraint: MODERATE
- precision: LIGHT
- authority: MODERATE
- density: LIGHT

**Situation-specific qualities:**
- patience — the interface never rushes the user. No countdown timers. No "session expires in 30 seconds" without a recovery path. No interactive elements that disappear under the finger.
- forgiveness — every action is recoverable, every error message uses kind language, every form pre-fills what the system already knows.

**Why this weighting:** A person scheduling chemotherapy is not a power user with a Bloomberg Terminal. They are a frightened human looking for help. Warmth and intimacy lead because the medium is the message — the interface itself is part of the care. Precision still matters (this is a hospital, not a lifestyle app), but precision in this context shows up as *clarity*, not density. Authority is present but quiet — the user already knows the hospital is authoritative; the interface doesn't need to perform it.

---

## Clinical dashboard

**When this applies:** The user is a clinician — nurse, doctor, technician, pharmacist. The surfaces are professional, post-authentication tools — patient charts, order entry, decision support, lab results, imaging review. The user is at work, often standing, frequently switching contexts, and has been trained on the software.

**Weighted qualities:**
- precision: HEAVY
- density: HEAVY
- authority: HEAVY
- restraint: MODERATE
- warmth: LIGHT
- intimacy: LIGHT

**Situation-specific qualities:**
- legibility under motion — typography that reads at a glance, in motion, at arm's length, from a moving cart or a desk lamp at 2am.
- glanceability — critical information visible without scrolling, scanning, or hovering.

**Why this weighting:** A clinician at the bedside does not have time for the warmth that a patient needs. Performative friendliness here is not just misplaced — it is in the way. Precision and density lead because every misread metric has consequences. Authority leads because the interface is being acted on, not just looked at. Warmth and intimacy drop to LIGHT, not OFF, because clinicians are people too — but the warmth of a clinical tool is the warmth of a well-machined instrument, not the warmth of a personal note.

---

## Alert state

**When this applies:** Any moment when the interface needs to interrupt the user with something urgent — an abnormal lab value, a medication conflict, a crash cart call, a security incident. Applies across both patient and clinician contexts, but the visual treatment differs.

**Weighted qualities:**
- precision: HEAVY
- authority: HEAVY
- restraint: HEAVY
- warmth: LIGHT
- intimacy: LIGHT
- density: LIGHT

**Situation-specific qualities:**
- urgency — the alert reads as urgent without screaming. Colour is used decisively (one accent, no rainbow). Motion is used minimally (one transition, no decoration). Sound is used only when the medium permits.
- recoverability — every alert has a clear next action and a clear dismiss path. Alerts that the user cannot act on are alerts that should not exist.

**Why this weighting:** An alert is the moment the interface stops being a tool and becomes an event. The qualities that matter are the ones that help the user *act*: precision (so they know what's happening), authority (so they trust the alert is real), and a paradoxical restraint (because urgency that is also visually noisy reads as panic, which is worse than calm urgency). Density drops because the alert is a single thing, not a dashboard. Warmth and intimacy recede — this is not the moment for a hug.

The visual treatment of an alert differs between patient and clinician contexts. A patient-facing alert ("we noticed an issue with your prescription, please call your pharmacy") inherits some warmth from the patient portal situation. A clinical alert ("PT/INR critical high") inherits the density-tolerance of the clinical dashboard situation. The agent should combine the alert state weighting with the underlying surface situation, taking the heavier weight for each quality.

---

## Tensions to hold

A few cross-cutting tensions worth naming, because the agent will encounter them whenever it produces work for this product:

**Warmth and precision.** These are not opposites. A warm, precise interface is one of the hardest things to design — and one of the most valuable in healthcare. The hospital brand asks for both, always. The situations weight them differently, but neither is ever absent.

**Authority and intimacy.** The clinician needs to trust the tool; the patient needs to feel met as a person. Both are forms of trust. Authority earns trust through competence; intimacy earns it through care. The situation determines which form leads.

**Urgency and restraint.** Counter-intuitively, the most urgent alert is the most restrained one. A flashing red banner with five exclamation points reads as advertising. A quiet, precise, decisively-coloured single line reads as serious. Restraint is part of how urgency is communicated, not a contradiction of it.

---

## What to take from this example

A few moves worth noting when you read your own `situation.md` first drafts:

**Every situation made actual calls.** Patient portal weights warmth HEAVY and precision LIGHT. Clinical dashboard weights precision HEAVY and warmth LIGHT. The protocol is useful precisely because it forces these calls. A `situation.md` that weights everything MODERATE everywhere has done none of the work.

**The "Why this weighting" rationales did real work.** They named the user, the context, and the consequence. Not "patients need warmth" but "a person scheduling chemotherapy is not a power user."

**Situation-specific qualities were used sparingly and justified.** Patience and forgiveness in the patient portal. Legibility-under-motion and glanceability in the clinical dashboard. Urgency and recoverability in the alert state. Each one was earned by the situation; none was smuggled in.

**Tensions were named, not hidden.** The cross-cutting tensions section at the end did the work of an experienced designer in the room — anticipating the contradictions the agent will encounter and giving guidance on how to hold them.

**The alert state explicitly handles composition.** A patient-portal alert is not the same as a clinical alert. The file said so, and gave guidance on how the agent should combine weights when situations overlap. This is the kind of detail that prevents the protocol from breaking down at edge cases.
