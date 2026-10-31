# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
The file goes from the writer's request (POST /submit with text and creator_id).
It then goes to the route in app.py, which parses and validates the input. Then it creates a content_id. Then it goes to the following files:
1. detector.model_signal - GPT-2 runs on your machine and measures how predictable the text is 
2. stylometry.style_signal - it measures variation in sentence length, vocabulary variety, and punctuation.
3. scoring.combine_signals - it combines your 2 scores into one score
4. scoring.score_to_label - it turns your score into words that say whether the text is human, unsure, or AI
5. audit.log_decision - everything is written to logs/audit.jsonl
Then it brings the JSON response, which the reader sees.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** the perplexity, to see how predictable the text is to GPT-2, which is then converted to a 0-1 score.

**Why that might differ between human and AI writing:**
AI writes by choosing the most likely next words, so a model finds text by AI easy to predict.

**What it can't see:**
Some humans (like me) write very plain text. So, people who write plain may come across as AI.

### Signal two — the style signal

**What it measures:** the shape without meaning, such as the difference in sentence length, the variety of vocabulary, and the punctuation used.

**Why that might differ between human and AI writing:** 
AI writes even, mid-length sentences with a simple vocabulary. Humans typically vary in sentence length, can have typos, and often vary widely with vocabulary.

**What it can't see:**
It will struggle with typos, grammatically incorrect sentences, which can change the score without changing who wrote the text.

### Endpoints
The two endpoints are POST /submit and POST /appeal

**POST/submit**
Input => It takes in text and the creator_id.
Output => It returns the content_id, guess, confidence, label, model_score, style_score, and combined_score. Missing, too-short, or too-long text gets a 400 and is logged as a rejection.

**POST/appeal**
Input => It takes in content_id and reasoning
Output => It returns a confirmation and the status of the item changed to under_review. An unknown content_id gets a 404.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
The combined score is a weighted average: 0.6 × model score + 0.4 × style score. A text can only be labelled AI if both signals lean AI (each at 0.5 or above); if either one leans human, the result is capped at "unsure". When the signals disagree, the system doesn't accuse — a false accusation costs a writer more than a missed AI text costs anyone.

**The numbers:**
Model weight 0.6, style weight 0.4. Agreement gate: both signals must be ≥ 0.5 for an "ai" label, otherwise the score is capped at 0.64. Thresholds: 0.35 or below is human, 0.65 or above is AI, anything between is unsure. Inside the style signal: sentence-length spread 0.65, vocabulary variety 0.10, punctuation density 0.25. Vocabulary was cut from 0.30 because it scored formal AI text as more varied than casual human writing.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
When my two signals split on my own short story (model 0.445, a coin flip, against style 0.16, clearly human), my rule averages them 60/40 to about 0.33, just under the 0.35 human threshold, so it's labelled human without the agreement gate needing to step in.

The agreement gate fires on `samples/ai_edited.json`, AI-style text with a few very short sentences dropped in: model 0.908 (confidently AI) against style 0.301 (leans human). The plain average is 0.665, which would be labelled AI, but because the style signal leans human the rule caps it at 0.64 and the writer sees "unsure" instead of an accusation.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | "This looks like it was written by a person." |
| unsure | above 0.35 and below 0.65 (and any score where the two signals disagree) | "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work." |
| high-confidence AI | 0.65 – 1.00, and only if both signals lean AI | "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it." |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
It says the system couldn't decide, not that the writer did anything wrong. My own plain writing lands in this band, so I wrote it as something I'd be fine reading about my own work: it names the cause (some styles are hard to call) and says outright that it isn't a judgment about the writer.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit   -H "Content-Type: application/json"   --data-binary @samples/ai_listy.json
```

```json
{
  "combined_score": 0.6866,
  "confidence": 0.3732,
  "content_id": "05302ec6-e981-4db0-a99c-c1414d070cc9",
  "creator_id": "test-ai",
  "guess": "ai",
  "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.",
  "model_score": 0.7544,
  "style_score": 0.585
}
```

The other two labels, from the same run:

```json
{"content_id": "5acf1a44-5275-4cdd-ae74-483db40100a4", "creator_id": "test-borderline", "guess": "unsure", "combined_score": 0.3919, "model_score": 0.3489, "style_score": 0.4565}
{"content_id": "5591674e-5bb0-49ed-ac8a-dbed204d7742", "creator_id": "test-human", "guess": "human", "combined_score": 0.3287, "model_score": 0.4445, "style_score": 0.1551}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal   -H "Content-Type: application/json"   -d '{"content_id": "05302ec6-e981-4db0-a99c-c1414d070cc9", "reasoning": "I wrote this myself for a workplace training handout. It is formal because the handout had to be."}'
```

```json
{
  "content_id": "05302ec6-e981-4db0-a99c-c1414d070cc9",
  "message": "Thanks — your appeal has been recorded and a person will review this result. Nothing changes until they do.",
  "original_guess": "ai",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ grep 05302ec6-e981-4db0-a99c-c1414d070cc9 logs/audit.jsonl
```

```json
{"timestamp": "2026-10-31T03:38:13+00:00", "content_id": "05302ec6-e981-4db0-a99c-c1414d070cc9", "creator_id": "test-ai", "guess": "ai", "model_score": 0.7544, "style_score": 0.585, "combined_score": 0.6866, "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.", "status": "decided", "confidence": 0.3732}
{"timestamp": "2026-10-31T03:38:13+00:00", "content_id": "05302ec6-e981-4db0-a99c-c1414d070cc9", "creator_id": "test-ai", "event": "appeal", "status": "under_review", "reasoning": "I wrote this myself for a workplace training handout. It is formal because the handout had to be."}
```

The original decision stays in the log and the appeal is added after it, so the history shows what was decided and that it was challenged.

---

## How I Used AI

**Moment 1**

- *What I asked for:* help me complete the submit function in app.py
- *What came back:* it offered tips how to complete the submit function
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
