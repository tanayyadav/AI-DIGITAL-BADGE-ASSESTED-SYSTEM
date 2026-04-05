from typing import Dict, List


def classify_badge(signals: Dict) -> Dict:
    scores = {
        "achievement": 0,
        "skill": 0,
        "competency": 0,
    }
    reasons: List[str] = []

    phrase_matches = signals.get("phrase_matches", {})
    regex_signals = signals.get("regex_signals", [])
    bloom_level = signals.get("bloom_level")
    level_hints = signals.get("level_hints", [])

    if phrase_matches.get("achievement"):
        scores["achievement"] += 2 * len(phrase_matches["achievement"])
        reasons.append("Achievement-oriented phrases were detected in the badge text.")

    if phrase_matches.get("skill"):
        scores["skill"] += 2 * len(phrase_matches["skill"])
        reasons.append("Skill-oriented phrases were detected in the badge text.")

    if phrase_matches.get("competency"):
        scores["competency"] += 2 * len(phrase_matches["competency"])
        reasons.append("Competency-oriented phrases were detected in the badge text.")

    if "project" in regex_signals:
        scores["competency"] += 2
        reasons.append("Project-based evidence suggests demonstrated performance.")

    if "assessment" in regex_signals:
        scores["skill"] += 1
        reasons.append("Assessment language supports measurable skill validation.")

    if bloom_level in {"analyze", "evaluate", "create"}:
        scores["competency"] += 2
        reasons.append(f"Bloom level '{bloom_level}' indicates higher-order application.")
    elif bloom_level == "apply":
        scores["skill"] += 1
        reasons.append("Bloom level 'apply' aligns with practical skill use.")

    category = max(scores, key=scores.get)

    if "advanced" in level_hints:
        level = "advanced"
    elif "foundational" in level_hints:
        level = "foundational"
    elif bloom_level in {"create", "evaluate"}:
        level = "advanced"
    elif bloom_level in {"apply", "analyze"}:
        level = "intermediate"
    else:
        level = "foundational"

    return {
        "category": category,
        "level": level,
        "scores": scores,
        "reasons": reasons,
    }
