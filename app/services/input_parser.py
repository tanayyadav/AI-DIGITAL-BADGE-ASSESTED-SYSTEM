def parse_form_input(data):
    return {
        "source_type": "form",
        "title": data.title,
        "description": data.description,
        "audience": data.audience,
        "context": data.context,
        "assessment_type": data.assessment_type,
        "evidence_type": data.evidence_type,
        "pathway_position": data.pathway_position
    }


def parse_text_input(data):
    return {
        "source_type": "text",
        "title": data.title,
        "description": data.description_text,
        "audience": None,
        "context": None,
        "assessment_type": None,
        "evidence_type": None,
        "pathway_position": None
    }


def parse_obv3_input(data):
    badge_json = data.badge_json

    return {
        "source_type": "obv3",
        "title": badge_json.get("name"),
        "description": badge_json.get("description"),
        "issuer": badge_json.get("issuer"),
        "criteria": badge_json.get("criteria"),
        "alignment": badge_json.get("alignment"),
        "audience": None,
        "context": None,
        "assessment_type": None,
        "evidence_type": None,
        "pathway_position": None
    }