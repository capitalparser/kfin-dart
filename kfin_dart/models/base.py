"""Base data models with audit traceability."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

ExtractionMethod = Literal["rule", "xbrl", "llm"]
OpinionType = Literal["적정", "한정", "부적정", "의견거절"]


class SourceRef(BaseModel):
    """Origin of an extracted value."""

    page: int = Field(ge=1)
    bbox: tuple[float, float, float, float] | None = None
    extraction_method: ExtractionMethod
    confidence: float = Field(ge=0.0, le=1.0)


class ExtractedField(BaseModel):
    """A field carrying its provenance."""

    value: Any
    source: SourceRef
    raw_text: str | None = None


class KAMItem(BaseModel):
    """Key Audit Matter entry."""

    title: ExtractedField
    body: ExtractedField


class AuditOpinion(BaseModel):
    """Independent auditor's report opinion block."""

    opinion_type: OpinionType
    auditor_firm: ExtractedField
    sign_date: ExtractedField
    kam_items: list[KAMItem] = Field(default_factory=list)
    emphasis_paragraphs: list[ExtractedField] = Field(default_factory=list)
    going_concern: bool = False
