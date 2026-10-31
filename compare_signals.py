#!/usr/bin/env python3
"""
Run both signals over the same test pieces, side by side.

    python compare_signals.py                  # every file in samples/
    python compare_signals.py samples/a.json   # just the files you name

Each file is JSON with a "text" field — the same files submit.sh sends.
Both scores run the same way: higher means more likely AI.
"""

import json
import sys
from pathlib import Path

import detector
import scoring
import stylometry


def main():
    paths = [Path(p) for p in sys.argv[1:]] or sorted(Path("samples").glob("*.json"))
    if not paths:
        print("No sample files found in samples/.")
        return

    print(f"weights: {stylometry._WEIGHTS}")
    print()
    print(f"{'sample':<20} {'model':>7} {'style':>7} {'gap':>7} {'combined':>9}  guess")
    print("-" * 66)
    for path in paths:
        text = json.loads(path.read_text(encoding="utf-8"))["text"]
        model = detector.model_signal(text)
        style = stylometry.style_signal(text)
        combined = scoring.combine_signals(model, style)
        guess, _ = scoring.score_to_label(combined)
        # A big gap means the two signals disagree — Milestone 4 asks for one.
        print(
            f"{path.stem:<20} {model:>7.4f} {style:>7.4f} {abs(model - style):>7.4f}"
            f" {combined:>9.4f}  {guess}"
        )


if __name__ == "__main__":
    main()
