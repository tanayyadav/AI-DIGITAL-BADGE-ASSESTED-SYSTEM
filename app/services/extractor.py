import re
from typing import Dict, List, Optional

try:
    import spacy
except ImportError:  # pragma: no cover
    spacy = None


_NLP = None
if spacy is not None:
    try:
        _NLP = spacy.load("en_core_web_sm")
    except Exception:
        _NLP = None


PHRASE_RULES: Dict[str, List[str]] = {
    "achievement": [
        "successfully completed",
        "participated in",
        "attended the program",
        "finished the course",
    ],
    "skill": [
        "demonstrated skill",
        "applied knowledge",
        "technical skill",
        "hands-on practice",
    ],
    "competency": [
        "demonstrated competency",
        "performance-based",
        "mastery of",
        "real-world project",
    ],
}

REGEX_RULES: Dict[str, str] = {
    "project": r"\b(project|capstone|portfolio)\b",
    "assessment": r"\b(exam|quiz|assessment|evaluation|test)\b",
    "collaboration": r"\b(teamwork|collaboration|group work|peer review)\b",
    "beginner_level": r"\b(beginner|introductory|foundational)\b",
    "advanced_level": r"\b(advanced|expert|mastery)\b",
}

BLOOM_VERB_MAP: Dict[str, str] = {
    "identify": "remember",
    "describe": "understand",
    "apply": "apply",
    "analyze": "analyze",
    "evaluate": "evaluate",
    "design": "create",
    "build": "create",
    "create": "create",
}


def extract_phrase_matches(text: str) -> Dict[str, List[str]]:
    text_lower = text.lower()
    matches: Dict[str, List[str]] = {
        "achievement": [],
        "skill": [],
        "competency": [],
    }

    for category, phrases in PHRASE_RULES.items():
        for phrase in phrases:
            if phrase in text_lower:
                matches[category].append(phrase)

    return matches



def extract_regex_signals(text: str) -> List[str]:
    text_lower = text.lower()
    signals: List[str] = []

    for signal_name, pattern in REGEX_RULES.items():
        if re.search(pattern, text_lower):
            signals.append(signal_name)

    return signals



def extract_bloom_level(text: str) -> Optional[str]:
    if _NLP is not None:
        doc = _NLP(text)
        lemmas = [token.lemma_.lower() for token in doc]
    else:
        lemmas = text.lower().split()

    for lemma in lemmas:
        if lemma in BLOOM_VERB_MAP:
            return BLOOM_VERB_MAP[lemma]

    return None



def extract_signals(text: str) -> Dict:
    phrase_matches = extract_phrase_matches(text)
    regex_signals = extract_regex_signals(text)
    bloom_level = extract_bloom_level(text)

    evidence_type: List[str] = []
    level_hints: List[str] = []

    if "project" in regex_signals:
        evidence_type.append("project")
    if "assessment" in regex_signals:
        evidence_type.append("assessment")
    if "beginner_level" in regex_signals:
        level_hints.append("foundational")
    if "advanced_level" in regex_signals:
        level_hints.append("advanced")

    return {
        "phrase_matches": phrase_matches,
        "regex_signals": regex_signals,
        "bloom_level": bloom_level,
        "evidence_type": evidence_type,
        "level_hints": level_hints,
    }
