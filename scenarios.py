"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of the five criteria in criteria.md has a scenario below. `run_eval.py`
runs everything here three times.

A scenario carries ONE of these:

    "texts"    a list of strings. Each is sent as {"text": ..., "creator_id": ...}
               with a creator_id made up for you.

    "bodies"   a list of whole request bodies, sent exactly as written. Used for
               the bad-input criterion, where the malformed request IS the point.

    "appeals"  {"texts": [...], "fake_ids": [...]}. Each text is submitted, then
               appealed against the content_id that came back, and the log is
               checked for the appeal entry. Each fake id is appealed and must
               come back 404 and leave nothing in the log. (Criterion 4 — added
               to run_eval.py in unit 8 so the appeal path runs automatically
               instead of by hand.)
"""

import json
from pathlib import Path

SAMPLES = Path(__file__).parent / "samples"


def _sample(name: str) -> str:
    return json.loads((SAMPLES / name).read_text(encoding="utf-8"))["text"]


def _my_writing() -> list[str]:
    """
    Criterion 1's texts: paragraphs I wrote myself, kept in
    samples/my_writing.txt, separated by a blank line.
    """
    path = SAMPLES / "my_writing.txt"
    if not path.exists():
        return ["REPLACE ME — put ten of your own paragraphs in samples/my_writing.txt"]
    paragraphs = [p.strip() for p in path.read_text(encoding="utf-8").split("\n\n")]
    return [p for p in paragraphs if p and not p.startswith("#")]


# Clearly AI-written: generated for this test in the even, formal, listy register
# a chat assistant defaults to. Criterion 3 compares these against my own writing.
AI_TEXTS = [
    _sample("ai_listy.json"),
    "Effective communication is a cornerstone of successful teamwork. When team "
    "members share information clearly and consistently, they are better able to "
    "coordinate their efforts and avoid misunderstandings. There are several "
    "strategies that can help improve communication in the workplace. First, it "
    "is important to establish clear channels for sharing updates. Second, active "
    "listening ensures that every voice is heard and valued. Finally, regular "
    "feedback helps teams identify areas for improvement and celebrate success.",
    "Regular physical activity offers numerous benefits for both physical and "
    "mental health. Engaging in exercise on a consistent basis can help reduce the "
    "risk of chronic diseases, improve cardiovascular health, and support healthy "
    "weight management. In addition, exercise has been shown to reduce symptoms of "
    "anxiety and depression. Experts generally recommend at least 150 minutes of "
    "moderate activity each week. By incorporating movement into daily routines, "
    "individuals can enjoy a higher quality of life.",
    "Climate change is one of the most pressing challenges facing the world today. "
    "Rising global temperatures are contributing to more frequent extreme weather "
    "events, rising sea levels, and disruptions to ecosystems. Addressing this "
    "issue requires a coordinated effort from governments, businesses, and "
    "individuals. Key strategies include transitioning to renewable energy "
    "sources, improving energy efficiency, and protecting natural habitats. By "
    "taking action now, we can help ensure a sustainable future for generations "
    "to come.",
    "Learning a new language can be a rewarding and enriching experience. It "
    "opens doors to new cultures, enhances cognitive abilities, and can improve "
    "career opportunities. To learn a language effectively, it is important to "
    "practice consistently and set realistic goals. Immersion, such as watching "
    "films or speaking with native speakers, can accelerate progress. "
    "Additionally, language learning apps provide convenient tools for building "
    "vocabulary. With dedication and patience, anyone can achieve fluency over "
    "time.",
]


SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Ten paragraphs I wrote myself. Pass: at most 1 of 10 labelled "ai",
        # in every one of the three trials.
        "texts": _my_writing(),
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # One input aimed at each band. Pass: across the set, all three
        # guesses (human, unsure, ai) appear — in every trial.
        "texts": [
            _sample("ai_listy.json"),
            _sample("human_casual.json"),
            _sample("borderline.json"),
            _sample("ai_edited.json"),
        ],
    },
    {
        "name": "score spread (AI side)",
        "criterion": 3,
        # Pass: the mean combined score of these is at least 0.33 above the mean
        # combined score of "my own writing" (criterion 1), in every trial.
        "texts": AI_TEXTS,
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # Pass: 5 of 5 real appeals return 200, status under_review, and leave
        # an appeal entry in the log; the made-up id returns 404 and writes
        # nothing.
        "appeals": {
            "texts": [
                _sample("ai_listy.json"),
                _sample("human_casual.json"),
                _sample("borderline.json"),
                _sample("ai_edited.json"),
                AI_TEXTS[1],
            ],
            "fake_ids": ["00000000-0000-0000-0000-000000000000"],
        },
    },
    {
        "name": "bad input",
        "criterion": 5,
        # Pass: every one of these returns a 4xx with a JSON error body. No 5xx.
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "     \n\t ", "creator_id": "eval_bad_whitespace"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": ["a", "list"], "creator_id": "eval_bad_list"},
            {"text": "word " * 5000, "creator_id": "eval_bad_huge"},
            {"text": "Hi", "creator_id": "eval_bad_tiny"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        appeals = scenario.get("appeals")

        if sum(bool(x) for x in (texts, bodies, appeals)) > 1:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has more than one of "
                f"texts / bodies / appeals — pick one"
            )
            continue

        if appeals:
            if not appeals.get("texts"):
                problems.append(f"scenario {i} has an appeals block with no texts")
            texts = appeals.get("texts") or []
        elif bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
