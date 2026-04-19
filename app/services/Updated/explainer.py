from typing import Dict, List


def build_explanation(text: str, signals: Dict, classification: Dict) -> List[str]:
    explanation: List[str] = []

    phrase_matches = signals.get("phrase_matches", {})
    regex_signals = signals.get("regex_signals", [])
    bloom_level = signals.get("bloom_level")

    if phrase_matches.get("achievement"):
        explanation.append(
            f"Matched achievement phrases: {', '.join(phrase_matches['achievement'])}."
        )

    if phrase_matches.get("skill"):
        explanation.append(
            f"Matched skill phrases: {', '.join(phrase_matches['skill'])}."
        )

    if phrase_matches.get("competency"):
        explanation.append(
            f"Matched competency phrases: {', '.join(phrase_matches['competency'])}."
        )

    if regex_signals:
        explanation.append(
            f"Additional rule-based signals found: {', '.join(regex_signals)}."
        )

    if bloom_level:
        explanation.append(
            f"The detected Bloom level was '{bloom_level}', which influenced the final decision."
        )

    explanation.append(
        f"Final classification: {classification['category']} at the {classification['level']} level."
    )

    return explanation