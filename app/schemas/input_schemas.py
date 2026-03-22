from pydantic import BaseModel
from typing import Optional, Dict, Any


class FormInputSchema(BaseModel):
    title: str
    description: Optional[str] = None
    audience: Optional[str] = None
    context: Optional[str] = None
    assessment_type: Optional[str] = None
    evidence_type: Optional[str] = None
    pathway_position: Optional[str] = None


class FreeTextInputSchema(BaseModel):
    title: Optional[str] = None
    description_text: str


class OBv3InputSchema(BaseModel):
    badge_json: Dict[str, Any]