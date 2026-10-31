"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Decision: coefficient of variation (stdev / mean) of words per sentence.
    0.0 means every sentence is the same length; human prose usually lands
    around 0.4–0.8. **Higher means more human.** Fewer than two sentences
    returns 0.0 here, and style_signal treats that case as "no evidence"
    rather than "perfectly even".
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return round(statistics.stdev(lengths) / mean, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    Decision: to blunt the length effect, this is a moving-average ratio —
    the plain ratio inside every 50-word window, averaged. Texts shorter than
    one window get the plain ratio. **Higher means more human.**
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    window = 50
    if len(tokens) <= window:
        return round(len(set(tokens)) / len(tokens), 4)
    ratios = [
        len(set(tokens[i:i + window])) / window
        for i in range(len(tokens) - window + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Decision: count only the "expressive" marks — commas, semicolons, colons,
    dashes, brackets, quotes, ! and ? — and skip full stops, which mostly
    track sentence count. Returned per word, so typically 0.0–0.3.
    **Higher means more human** — a guess to check against the calibration
    inputs, since some models lean hard on commas and em dashes.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    marks = re.findall(r"[,;:!?()\"“”‘’\-–—]", text)
    return round(len(marks) / len(tokens), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    Decisions:
      1. All three measures run "higher = more human", so each is flipped.
      2. Each is scaled to 0–1 "human-ness" by a linear ramp between an
         AI-ish anchor (0) and a human-ish anchor (1), clamped. The anchors
         in _ANCHORS are starting guesses — tune them on the calibration set.
      3. Weighted average: spread 0.65, vocabulary 0.10, punctuation 0.25.
         Vocabulary started at 0.30 and was cut after calibration: formal AI
         prose uses many distinct long words, so it scored as *more* varied
         than casual human writing — pointing the wrong way.
      4. A one-sentence text has no spread, so that measure scores a neutral
         0.5 instead of "perfectly even".
    """
    if not words(text):
        return 0.5

    if len(sentences(text)) < 2:
        spread_h = 0.5
    else:
        spread_h = _ramp(sentence_length_spread(text), *_ANCHORS["spread"])
    vocab_h = _ramp(type_token_ratio(text), *_ANCHORS["vocab"])
    punct_h = _ramp(punctuation_density(text), *_ANCHORS["punct"])

    human_ness = (
        _WEIGHTS["spread"] * spread_h
        + _WEIGHTS["vocab"] * vocab_h
        + _WEIGHTS["punct"] * punct_h
    )
    return round(1.0 - human_ness, 4)


# (AI-ish value, human-ish value) for each measure.
_ANCHORS = {
    "spread": (0.20, 0.65),
    "vocab": (0.60, 0.85),
    "punct": (0.05, 0.20),
}
_WEIGHTS = {"spread": 0.65, "vocab": 0.10, "punct": 0.25}


def _ramp(value: float, low: float, high: float) -> float:
    """Map value onto 0–1: low -> 0, high -> 1, clamped either side."""
    return min(max((value - low) / (high - low), 0.0), 1.0)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
