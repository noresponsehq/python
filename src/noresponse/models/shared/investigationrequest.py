from __future__ import annotations
from .enrichmentchange import EnrichmentChange, EnrichmentChangeTypedDict
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class InvestigationRequestTypedDict(TypedDict):
    r"""Runs a new investigation against one retained workspace person."""

    depth: ScreeningDepth
    platforms: List[str]
    person_id: str
    enrichment: NotRequired[EnrichmentChangeTypedDict]
    r"""A change to enrichment. A field left out keeps the value in force; max_spend or deadline null removes the bound."""


class InvestigationRequest(BaseModel):
    r"""Runs a new investigation against one retained workspace person."""

    depth: ScreeningDepth

    platforms: List[str]

    person_id: str

    enrichment: Optional[EnrichmentChange] = None
    r"""A change to enrichment. A field left out keeps the value in force; max_spend or deadline null removes the bound."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["enrichment"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
