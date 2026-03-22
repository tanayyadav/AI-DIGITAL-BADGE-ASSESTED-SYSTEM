from pydantic import BaseModel
from typing import List, Optional


class BadgeFactSheet(BaseModel):
    source_type: str
    title: Optional[str] = None
    description: Optional[str] = None
    issuer: Optional[str] = None

    audience: Optional[str] = None
    context: Optional[str] = None

    assessment_present: bool = False
    assessment_type: Optional[str] = None

    evidence_present: bool = False
    evidence_type: List[str] = []

    bloom_level_indicators: List[str] = []
    pathway_position: Optional[str] = None

    extracted_keywords: List[str] = []