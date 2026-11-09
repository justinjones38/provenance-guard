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
Model weight 0.6, style weight 0.4. Agreement gate: both signals must be ≥ 0.5 for an "ai" label, otherwise the score is capped at 0.64. Thresholds: 0.35 or below is human, 0.65 or above is AI, anything between is unsure. *(Unit 8: the AI threshold is now 0.85 and the gate cap 0.84 — see The Improvement.)* Inside the style signal: sentence-length spread 0.65, vocabulary variety 0.10, punctuation density 0.25. Vocabulary was cut from 0.30 because it scored formal AI text as more varied than casual human writing.

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

- *What I asked for:* tips on setting up with Git Bash  
- *What came back:* it gave me advice on differences needed to setup with Git bash
- *What I changed:* I used the instructions for Git Bash

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 100 per day (set in `config.py`, applied by the `@limiter.limit(...)` decorator on `app.py::submit`)

**Why those numbers and not others:**
A real writer checks their own work a few times an hour. Even someone fixing a draft and resubmitting quickly won't send more than a handful a minute, so 10 a minute never gets in their way. 100 a day is still far more than one person writes in a day. A script mapping my thresholds needs hundreds or thousands of near-identical variations. At 10 a minute it gets 100 tries a day and then has to wait until tomorrow, which turns an afternoon of probing into weeks.

**What a caller counts as:** per `creator_id`, falling back to the IP address when the request has no usable `creator_id` (see `rate_limit_key` in `app.py`). This is the fair choice for a shared household or classroom, where many real writers sit behind one IP. The weakness is that `creator_id` is whatever the caller sends, so a script can make up a new one for every request and never get limited. A real deployment would also need a per-IP ceiling, or would tie `creator_id` to a logged-in account.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

Every 429 is logged as a rejection, so the flood leaves a trace in `logs/audit.jsonl`:

```json
{"combined_score": null, "content_id": null, "creator_id": "flood_tester", "event": "rejected", "guess": null, "label": null, "limit": "10 per 1 minute", "model_score": null, "reason": "rate_limited", "status": "rejected", "style_score": null, "timestamp": "2026-11-09T01:55:03+00:00"}
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

Full set, 56 requests: `python run_attacks.py --set attack_set --label before` → `results/attack_run_2026-11-08_1937_before.md`. Rate limiting was on and no row was skipped. Model, Style and Combined are read from the response and `logs/audit.jsonl`.

How I judged each one: an **evasion** or **prompt-injection** attack is AI text, and the same paragraph with no changes scores **0.76 → "ai"**. So if the attack pulled it down to "unsure" or "human", it **BROKE**. A **false_positive** attack is human writing, so a label of "ai" means it **BROKE**. A **malformed** input should get a 4xx. If it got a label instead, it **BROKE**. The service never crashed: no 500s.

**21 of 56 broke.**

| ID | Family | Targeting | Status | Guess | Model | Style | Combined | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.1635 | 0.9 | 0.4581 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.5943 | 0.25 | 0.4566 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.6662 | 0.5059 | 0.6021 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | ai | 0.6114 | 0.8865 | 0.7214 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.3212 | 0.191 | 0.2691 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.5727 | 0.2505 | 0.4438 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.5862 | 0.3268 | 0.4824 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.2452 | 0.7804 | 0.4593 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.7042 | 0.5068 | 0.6252 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.9792 | 0.7199 | 0.8755 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.6175 | 0.5455 | 0.5887 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.7387 | 0.8739 | 0.7928 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.8051 | 0.7271 | 0.7739 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.8329 | 0.6708 | 0.7681 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.8005 | 0.8786 | 0.8317 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.8814 | 0.4765 | 0.64 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.8816 | 0.35 | 0.64 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.3223 | 0.5634 | 0.4187 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.4625 | 0.25 | 0.3775 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.2044 | 0.25 | 0.2226 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.5943 | 0.6858 | 0.6309 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.4998 | 0.5685 | 0.5273 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.6401 | 0.258 | 0.4873 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.5583 | 0.5605 | 0.5592 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.0 | 0.575 | 0.23 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | human | 0.0112 | 0.5 | 0.2067 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.9976 | 0.575 | 0.8286 | BROKE |
| MF06 | malformed | text is emoji only | 200 | ai | 0.9969 | 0.5 | 0.7981 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.9064 | 0.5 | 0.7438 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.2395 | 0.575 | 0.3737 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.0492 | 0.575 | 0.2595 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-09T01:37:28+00:00", "content_id": "3c23c4d2-abc9-4bbe-ad61-308f921d71c3", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.7271, "combined_score": 0.7739, "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.", "status": "decided", "confidence": 0.5478}
{"timestamp": "2026-11-09T01:37:28+00:00", "content_id": "3f7f8c59-8fac-4252-a0bb-756f4443f874", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.8739, "combined_score": 0.7928, "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.", "status": "decided", "confidence": 0.5856}
{"timestamp": "2026-11-09T01:37:28+00:00", "content_id": "041ed626-0f91-4258-b2b2-4dcd690c00d5", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.8786, "combined_score": 0.8317, "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.", "status": "decided", "confidence": 0.6634}
{"timestamp": "2026-11-09T01:37:31+00:00", "content_id": "97c2a065-0075-443b-a3c0-a69fe6719ab9", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 0.5, "combined_score": 0.7438, "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.", "status": "decided", "confidence": 0.4876}
{"timestamp": "2026-11-09T01:37:30+00:00", "content_id": "b23a7623-8237-4c82-93b0-190902030f86", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 0.5, "combined_score": 0.7981, "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.", "status": "decided", "confidence": 0.5962}
{"timestamp": "2026-11-09T01:37:29+00:00", "content_id": "db7b4df7-15a2-488c-a2aa-0a1005f45729", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.25, "combined_score": 0.2226, "label": "This looks like it was written by a person.", "status": "decided", "confidence": 0.5548}
{"timestamp": "2026-11-09T01:37:27+00:00", "content_id": "050ec506-fe7b-4865-9f7a-bf716b4cc53c", "creator_id": "attacker_EV05", "guess": "human", "model_score": 0.3212, "style_score": 0.191, "combined_score": 0.2691, "label": "This looks like it was written by a person.", "status": "decided", "confidence": 0.4618}
{"timestamp": "2026-11-09T01:37:26+00:00", "content_id": "3d7331c1-d0c6-4fc7-9428-a835ceabe9e5", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.9, "combined_score": 0.4581, "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.", "status": "decided", "confidence": 0.0838}
{"timestamp": "2026-11-09T01:37:31+00:00", "content_id": "771a0cf8-b326-4d6b-aa75-f2687dd3a19c", "creator_id": {"id": "x"}, "guess": "human", "model_score": 0.0492, "style_score": 0.575, "combined_score": 0.2595, "label": "This looks like it was written by a person.", "status": "decided", "confidence": 0.481}
{"timestamp": "2026-11-09T01:37:32+00:00", "content_id": null, "creator_id": "attacker_flood", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
```

These are, in order: three real human writers accused of using AI (FP03 non-native speaker, FP02 formal report, FP05 technical docs), an Arabic sentence accused of AI (MF07), a row of emoji accused of AI (MF06), AI text that a fake "SYSTEM:" line turned into "human" (PI02), a heavy human rewrite that reads as human (EV05), AI text whose typos sank the model score (EV01), RQ06's object `creator_id` written straight into the log, and a flood request rejected with a 429 that still left a trace.

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03**: someone writing carefully in their second language about their first month in a new country, labelled "probably written with an AI tool" with a combined score of 0.77. Both of my signals pointed at them. GPT-2 found their simple, safe vocabulary easy to predict (0.81), and their steady, even sentences looked machine-like to the style signal (0.73). So the agreement gate that's meant to protect writers didn't fire. They're the writer least able to argue back, and the system accused them for writing carefully.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

`python run_eval.py --label before` → `results/run_2026-11-08_1953_before.md`, run with `AI201_AI_THRESHOLD=0.65` (the threshold before my improvement). Criterion 4 runs automatically through `run_eval.py::run_appeals`, which I added in unit 8: it submits, appeals the returned `content_id`, reads `/log` back, and appeals a made-up id. All three trials gave identical results, because GPT-2 scores the same text the same way every time.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing | at most 1 of 10 labelled AI, every trial | 3 of 10 | 3 of 10 | 3 of 10 | **MISS** |
| 2. label coverage | human, unsure and AI all appear, every trial | all 3 | all 3 | all 3 | **PASS** |
| 3. score spread | AI texts average ≥ 0.33 above my own writing | gap 0.255 (0.794 vs 0.539) | 0.255 | 0.255 | **MISS** |
| 4. appeal path | 5/5 appeals → under_review + logged; fake id → 404, nothing logged | 5/5 + 404 | 5/5 + 404 | 5/5 + 404 | **PASS** |
| 5. bad input | every malformed body → 4xx with JSON error, no 5xx | 8/8 → 400 | 8/8 → 400 | 8/8 → 400 | **PASS** |

Criterion 5 passes on the eight bad inputs I thought of, but the attack set found seven more that I didn't (MF03–MF07, EV08, RQ06: control characters, emoji, Arabic, near-empty text, an object `creator_id`). Those got a 200 and a label. So my criterion passes, but the behaviour it was meant to guarantee doesn't hold.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Produced by `run_eval.py::main` against `app.py::submit`. Trial 1 of criterion 1: three paragraphs I wrote myself, all labelled AI (paragraphs 4, 8 and 9):

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.4658,
    "combined_score": 0.7329,
    "error": null,
    "model_score": 0.6756,
    "style_score": 0.8188,
    "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I have a lot of the front-end skills like React and familiarity with G"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.3246,
    "combined_score": 0.6623,
    "error": null,
    "model_score": 0.7393,
    "style_score": 0.5469,
    "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I like going to the store and buying random items. It is very fun and "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.415,
    "combined_score": 0.7075,
    "error": null,
    "model_score": 0.7038,
    "style_score": 0.7131,
    "label": "This looks like it was probably written with an AI tool. We could be wrong — if you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I have been using Indeed for the longest and I have found Indeed the e"
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Look for a pattern. Five failures on one signal is one problem, not five. -->

**Criterion 1 missed (3 of 10 of my own paragraphs labelled AI). Stages: both signals, then the label mapping.** This is the same problem as the FP attacks, and it happened to me. The three paragraphs that got caught are my plainest writing: short, common words, sentences of similar length, and phrases I repeat ("I find Indeed… easier to use", "It is very fun… It is great fun"). GPT-2 predicts that kind of wording well (model 0.68–0.74), and the even sentences read as AI to the style signal (0.55–0.82). Both were over 0.5, so the gate didn't fire, and they averaged 0.66–0.73, just over 0.65. The only one of my ten that scored "human" is the short story (paragraph 7), which has the most varied sentences and the most unusual wording.

**Criterion 3 missed (gap 0.255, target 0.33). Stages: signal one and signal two.** My AI texts average 0.794 and my own writing averages 0.539. The gap isn't small because AI text scores low. It's small because my own plain writing scores high (five of my ten are above 0.54), for the same reason as criterion 1. The signals measure *plain* versus *varied*, not *machine* versus *person*, and a lot of my real writing is plain.

The 21 broken attacks come down to five problems.

**1. Plain human writing is called AI (FP02, FP03, FP04, FP05). Stages: both signals, then the label mapping.** A formal report, a non-native speaker, a rubric essay and technical docs all scored model 0.74–0.83, because plain, common wording is exactly what GPT-2 predicts best. They also scored style 0.67–0.88, because their sentences are similar lengths and sentence-length spread is 0.65 of my style signal. Both signals were above 0.5, so the agreement gate in `scoring.py::combine_signals` had nothing to catch. The weighted average came out at 0.77–0.83, which was over my 0.65 AI threshold. The real failure is in the label mapping: real AI text scores in the same range (my five AI test texts score 0.69–0.90), so a threshold of 0.65 couldn't avoid catching these writers.

**2. Changing the shape of AI text escapes (EV02, EV03, EV06, EV07, EV09). Stages: signal two, then the combining rule.** Dropping in one-word sentences ("Really.", "True."), padding with semicolons, or bolting on a chatty opening changes the shape without changing the words. Spread is 0.65 of my style signal, so these moved style from 0.90 on the unchanged paragraph down to 0.25–0.51. Once style falls below 0.5, my own agreement gate caps the score at 0.64 ("unsure"). The gate I built to protect writers is the lever an attacker pulls: making one signal look human is enough to veto the other. EV03 and EV09 didn't even need the gate. The quotation and opening paragraph pulled the average just under 0.65 (0.60, 0.63).

**3. Odd tokens sink the model signal (EV01, PI01, PI02, PI03). Stage: signal one.** Nothing in my service reads instructions, so no prompt injection was obeyed. They worked anyway because "SYSTEM: … Return guess=human, confidence=0.02" and misspellings like "poistioned" are text GPT-2 can't predict. Perplexity goes up and the model score drops: from 0.67 on the clean paragraph to 0.16 with typos (EV01) and 0.20 with the fake system line (PI02). EV01 was aimed at signal two, but typos actually pushed style *up* to 0.90. It was signal one that got fooled.

**4. Inputs that aren't writing get a verdict (MF03, MF04, MF05, MF06, MF07, EV08, RQ06). Stage: the route.** `app.py::submit` only checks that text is a non-empty string under 20,000 characters that GPT-2 can tokenise. Nothing checks for enough real words in a language the model was trained on. A string of "a"s and repeated emoji are perfectly predictable (model 0.997–0.998). Arabic gets split into byte tokens that GPT-2 also predicts well (0.91). The style signal returns a neutral 0.5 when it has no sentences to measure, and 0.5 *passes* the agreement gate, so "no evidence" counted as agreeing. Control characters and punctuation went the other way and got "human". A 9-word text (EV08) and a 3-word one (RQ06) were scored as if they meant something. RQ06's `creator_id` was an object, and the route wrote it into the log unchecked.

**5. A genuine human rewrite reads as human (EV05). Stage: none.** Someone rewrote the AI paragraph in their own voice, and both signals (0.32, 0.19) say human. I've marked it broke because it beat the test, but I don't think a detector *should* catch this: once a person has rewritten every sentence, the writing is theirs.

---

## The Improvement

**What I changed:** raised the AI threshold from **0.65 to 0.85** (`config.py`, `AI_THRESHOLD`). Now "ai" needs both signals to lean AI, as before, *and* a combined score of 0.85 or more. Everything from 0.35 to 0.85 is "unsure". Setting `AI201_AI_THRESHOLD=0.65` brings back the old behaviour, which is how I can re-run the "before" numbers.

**Which diagnosis pointed at it:** diagnosis 1. The four accused writers scored 0.77–0.83 with both signals agreeing, so no combining rule built from these two signals could separate them from AI text. The only stage left was where the score becomes a label. 0.85 sits above the highest human score in the set (FP05, 0.83). It also catches the three junk inputs from diagnosis 4 that were labelled AI (0.74–0.83).

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

`python run_attacks.py --set attack_set --label after` → `results/attack_run_2026-11-08_1939_after.md`. Every score is identical to the before run, because GPT-2 scores the same text the same way each time. Only the labels moved.

**18 of 56 broke.**

| ID | Family | Targeting | Status | Guess | Model | Style | Combined | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.1635 | 0.9 | 0.4581 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.5943 | 0.25 | 0.4566 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.6662 | 0.5059 | 0.6021 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.6114 | 0.8865 | 0.7214 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.3212 | 0.191 | 0.2691 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.5727 | 0.2505 | 0.4438 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.5862 | 0.3268 | 0.4824 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.2452 | 0.7804 | 0.4593 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.7042 | 0.5068 | 0.6252 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.9792 | 0.7199 | 0.8755 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.6175 | 0.5455 | 0.5887 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.7387 | 0.8739 | 0.7928 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.8051 | 0.7271 | 0.7739 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.8329 | 0.6708 | 0.7681 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.8005 | 0.8786 | 0.8317 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.8814 | 0.4765 | 0.7194 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.8816 | 0.35 | 0.669 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.3223 | 0.5634 | 0.4187 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.4625 | 0.25 | 0.3775 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.2044 | 0.25 | 0.2226 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.5943 | 0.6858 | 0.6309 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.4998 | 0.5685 | 0.5273 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.6401 | 0.258 | 0.4873 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.5583 | 0.5605 | 0.5592 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.0 | 0.575 | 0.23 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | human | 0.0112 | 0.5 | 0.2067 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.9976 | 0.575 | 0.8286 | BROKE |
| MF06 | malformed | text is emoji only | 200 | unsure | 0.9969 | 0.5 | 0.7981 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.9064 | 0.5 | 0.7438 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.2395 | 0.575 | 0.3737 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.0492 | 0.575 | 0.2595 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.0287 | 0.575 | 0.2472 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

It fixed what I aimed it at, and it cost a lot.

- **Helped:** human writing labelled AI in the false_positive family went from **4 of 8 to 0 of 8**. The Arabic sentence, the emoji and the "aaaa…" string are no longer accused either. Across the whole run, the "ai" label went from 9 rows to 1. Of the 8 it removed, 4 were real writers wrongly accused, 3 were junk input, and 1 (EV04) was a correct catch that's now lost.
- **Cost:** the same change mostly switches off detection. The unchanged AI paragraph (0.76) is now "unsure" before anyone attacks it, so most of the evasion family doesn't need to do anything. EV04 went from HELD to BROKE. Of my five AI test texts, five were labelled "ai" before and only one is now (0.895). Only very repetitive AI text, like EV10 at 0.88, still gets caught. The attack count only went from 21 to 18 broken, and that number hides the trade: three accusations of real people gone, one more AI text missed.
- **My own criteria**, re-run with `python run_eval.py --label after` → `results/run_2026-11-08_1954_after.md`:

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict | Before |
|---|---|---|---|---|---|---|
| 1. my own writing | at most 1 of 10 labelled AI | 0 of 10 | 0 of 10 | 0 of 10 | **PASS** | MISS |
| 2. label coverage | all 3 labels appear | human, unsure only | same | same | **MISS** | PASS |
| 3. score spread | gap ≥ 0.33 | 0.255 | 0.255 | 0.255 | **MISS** | MISS |
| 4. appeal path | 5/5 + 404 | 5/5 + 404 | 5/5 + 404 | 5/5 + 404 | **PASS** | PASS |
| 5. bad input | 8/8 → 4xx | 8/8 → 400 | 8/8 → 400 | 8/8 → 400 | **PASS** | PASS |

  The criterion I cared about most went from miss to pass: none of my own paragraphs is called AI now. As I expected, criterion 2 went from pass to miss. My "ai" coverage sample scores 0.69, now below 0.85, so this input set never shows the AI label. The label can still be reached (EV10 and one of my AI test texts hit it), but the criterion said *this set* should reach it, and it doesn't. Criterion 3 didn't move, because changing a threshold doesn't change any score. Moving the label boundary can't fix a gap between scores.

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

- **Evasion (EV01–EV09, EV04 now included): 9 of 10 get through.** Mostly because of the threshold trade above. Even at 0.65, the shape attacks (diagnosis 2) beat the agreement gate. What I'd do: make the gate need a *strong* human reading to veto (style below about 0.3, not below 0.5), and stop sentence-length spread being 0.65 of the style signal, since one-word sentences push it around so cheaply. I stopped because the milestone asks for one change, measured cleanly, and a gate change would have moved the false-positive numbers too.
- **Prompt-injection prefixes (PI01–PI03).** No instruction is obeyed, but strange prefixes lower the model score (diagnosis 3). I'd score the text in chunks and use the most AI-like chunk, so a weird first line can't drag down the whole piece. Not attempted.
- **Inputs that aren't writing (MF03–MF07, EV08, RQ06).** They're no longer accused, but they still get a label instead of a 400. The fix is in the route: require around 40 real words, mostly letters, reject `creator_id` that isn't a string, and return "we can only check English text" for scripts GPT-2 wasn't trained on. That is more honest than telling an Arabic writer "we can't tell". It's the next thing I'd build. I left it out so this run measures one change.
- **Rate limit bypass.** The limit is per `creator_id`, which the caller chooses. A script that invents a new id per request is never limited (every attack row did exactly that). I'd add a per-IP ceiling next to it.
- **Criterion 2 (label coverage): now missed.** This is the price of the improvement. To get it back without bringing back the false accusations, the AI scores would have to rise above 0.85 while human scores stay below. That needs a better signal, not a different threshold. I'd try a third signal that isn't about plainness, such as how often the text repeats the stock phrases chat assistants use ("plays a significant role", "it is important to"), and gate "ai" on it. I stopped because that's a new signal, not one fix.
- **Criterion 3 (score spread 0.255, target 0.33): still missed.** Same cause: my plain writing scores like AI text. Fixing it needs the same better signal. I'm keeping the target at 0.33. 0.255 is what I got, and lowering the number to match wouldn't be a revision.
- **Criterion 5 passes, but only on my inputs.** The attack set found junk inputs I didn't test for (diagnosis 4). The route-validation fix above is what would make the criterion mean what I intended.

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

I'd keep the high threshold and accept that most AI text will be labelled "unsure" instead of being caught: wrongly accusing a non-native speaker or a student who followed the rubric does real damage, and this system can't tell them apart from AI. The people who pay are honest writers competing with people who use AI and don't get caught, and the teachers or moderators who now have to read the "unsure" pile themselves instead of trusting a label.


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
