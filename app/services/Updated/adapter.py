from dataclasses import dataclass, field
from typing import List, Optional

from app.schemas.fact_sheet_schema import BadgeFactSheet


@dataclass
class ExternalBadgeInput:
    source_type: str
    title: Optional[str] = None
    description: Optional[str] = None
    issuer: Optional[str] = None
    audience: Optional[str] = None
    context: Optional[str] = None
    assessment_present: bool = False
    assessment_type: Optional[str] = None
    evidence_present: bool = False
    evidence_type: List[str] = field(default_factory=list)
    bloom_level_indicators: List[str] = field(default_factory=list)
    pathway_position: Optional[str] = None
    extracted_keywords: List[str] = field(default_factory=list)


def fact_sheet_to_external_input(fact_sheet: BadgeFactSheet) -> ExternalBadgeInput:
    """
    Adapter function to convert internal Pydantic BadgeFactSheet
    into external dataclass format expected by classification engine.
    """
    return ExternalBadgeInput(
        source_type=fact_sheet.source_type,
        title=fact_sheet.title,
        description=fact_sheet.description,
        issuer=fact_sheet.issuer,
        audience=fact_sheet.audience,
        context=fact_sheet.context,
        assessment_present=fact_sheet.assessment_present,
        assessment_type=fact_sheet.assessment_type,
        evidence_present=fact_sheet.evidence_present,
        evidence_type=list(fact_sheet.evidence_type),
        bloom_level_indicators=list(fact_sheet.bloom_level_indicators),
        pathway_position=fact_sheet.pathway_position,
        extracted_keywords=list(fact_sheet.extracted_keywords),
    )