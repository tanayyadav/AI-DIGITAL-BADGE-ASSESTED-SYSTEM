from app.schemas.fact_sheet_schema import BadgeFactSheet


AUDIENCE_MAP = {
    "students": "student",
    "student": "student",
    "learners": "student",
    "learner": "student",
    "faculty members": "faculty",
    "faculty": "faculty",
    "staff": "staff",
    "employees": "staff",
    "employee": "staff"
}

ASSESSMENT_MAP = {
    "quiz": "quiz",
    "exam": "exam",
    "test": "exam",
    "rubric-based evaluation": "rubric",
    "graded project": "project",
    "project": "project"
}

EVIDENCE_MAP = {
    "portfolio submission": "portfolio",
    "portfolio": "portfolio",
    "artifact upload": "artifact",
    "artifact": "artifact",
    "project submission": "project",
    "project": "project",
    "reflection": "reflection",
    "presentation": "presentation"
}


def normalize_value(value, mapping):
    if not value:
        return None
    value = value.strip().lower()
    return mapping.get(value, value)


def normalize_raw_input(raw_data: dict) -> BadgeFactSheet:
    normalized_audience = normalize_value(raw_data.get("audience"), AUDIENCE_MAP)
    normalized_assessment = normalize_value(raw_data.get("assessment_type"), ASSESSMENT_MAP)
    normalized_pathway = raw_data.get("pathway_position")

    normalized_evidence_list = []
    raw_evidence = raw_data.get("evidence_type")

    if raw_evidence:
        normalized_evidence = normalize_value(raw_evidence, EVIDENCE_MAP)
        normalized_evidence_list.append(normalized_evidence)

    return BadgeFactSheet(
        source_type=raw_data.get("source_type", "unknown"),
        title=raw_data.get("title"),
        description=raw_data.get("description"),
        issuer=raw_data.get("issuer"),

        audience=normalized_audience,
        context=raw_data.get("context"),

        assessment_present=bool(normalized_assessment),
        assessment_type=normalized_assessment,

        evidence_present=len(normalized_evidence_list) > 0,
        evidence_type=normalized_evidence_list,

        bloom_level_indicators=[],
        pathway_position=normalized_pathway,

        extracted_keywords=[]
    )