from extractor import extract_signals
from classifier import classify_badge
from explainer import build_explanation


def test_end_to_end_pipeline_with_project_and_assessment():
    text = (
        "Learners successfully completed a real-world project and passed an assessment "
        "to demonstrate advanced Python skills and design solutions."
    )

    signals = extract_signals(text)
    classification = classify_badge(signals)
    explanation = build_explanation(text, signals, classification)

    assert "project" in signals["regex_signals"]
    assert "assessment" in signals["regex_signals"]
    assert classification["category"] in {"achievement", "skill", "competency"}
    assert classification["level"] in {"foundational", "intermediate", "advanced"}
    assert len(explanation) > 0


def test_end_to_end_pipeline_with_foundational_badge():
    text = (
        "Students attended the program and completed an introductory course "
        "with beginner-level assessment in web development."
    )

    signals = extract_signals(text)
    classification = classify_badge(signals)
    explanation = build_explanation(text, signals, classification)

    assert "assessment" in signals["regex_signals"]
    assert "beginner_level" in signals["regex_signals"]
    assert classification["level"] == "foundational"
    assert len(explanation) > 0


def test_end_to_end_pipeline_with_skill_focused_badge():
    text = (
        "Participants applied knowledge through hands-on practice and technical skill "
        "development in data analytics."
    )

    signals = extract_signals(text)
    classification = classify_badge(signals)
    explanation = build_explanation(text, signals, classification)

    assert classification["category"] in {"skill", "competency", "achievement"}
    assert isinstance(explanation, list)
    assert len(explanation) > 0