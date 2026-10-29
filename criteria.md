# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->
Of 10 paragpghs that I wrote myself, at most 1 is labelled as high-confidence AI in every one of 3 trials.


**Why this target:**
As seen in school, a wrong accusation is far more damaging than a missed detection, So, that is the goal of this target.


---

## 2.

<!-- Your criterion. -->
All 3 labels (human, unsure, AI) is producted by at least one of the test inputs.


**Why this target:**
A label that nothing can reach is a broken range. I want to test for all possible labels, so each label need to be included.


---

## 3.

<!-- Your criterion. -->
Clearly-AI text averages at least 0.33 higher on combined score than obvious human-text.


**Why this target:**
I want there to be a large gap between text that is clearly AI and human. If two text score close together, then run-to-run variation can change the label.


---

## 4.

<!-- Your criterion. -->
All appeals (5 our of 5) appeals on real_content_ids change the status to under_review and write an appeal entry to the log, and an appeal on a made-up content_id returns 404 and changes nothing


**Why this target:**
The appeal is the only thing standing between a wrong accusation and nothing. So, it must every time.


---

## 5.

<!-- Your criterion. -->

Every incorrect request (such as missing or empty text, null, or over the word limit) returns a 400 level error with a JSON message. 

**Why this target:**
A crash on bad input causes a lot of real faulures, so I am trying to prevent that.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
