from pprint import pprint

from extractor import extract_signals
from classifier import classify_badge
from explainer import build_explanation



def run_pipeline(text: str) -> dict:
    signals = extract_signals(text)
    classification = classify_badge(signals)
    explanation = build_explanation(text, signals, classification)

    return {
        "input_text": text,
        "signals": signals,
        "classification": classification,
        "explanation": explanation,
    }


if __name__ == "__main__":
    sample_text = (
        "Learners successfully completed a real-world project and passed an assessment "
        "to demonstrate advanced Python skills and design solutions."
    )

    result = run_pipeline(sample_text)
    pprint(result)
