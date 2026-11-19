from __future__ import annotations
from .enrichmentchange import EnrichmentChange, EnrichmentChangeTypedDict
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InvestigationRequestTypedDict(TypedDict):
    r"""Runs a new investigation against one retained workspace person."""

    depth: ScreeningDepth
    person_id: str
    platforms: NotRequired[List[str]]
    r"""Deprecated: leave it out. Without it the investigation is a full search: every platform a connector serves in the environment when the investigation starts, which the investigation then lists, each searched only with the identifiers its connector takes. A list sent here still limits the investigation until a later contract release removes the field."""
    enrichment: NotRequired[EnrichmentChangeTypedDict]
    r"""A change to enrichment. A field left out keeps the value in force; max_spend or deadline null removes the bound."""


class InvestigationRequest(BaseModel):
    r"""Runs a new investigation against one retained workspace person."""

    depth: ScreeningDepth

    person_id: str

    platforms: Annotated[
        Optional[List[str]],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Deprecated: leave it out. Without it the investigation is a full search: every platform a connector serves in the environment when the investigation starts, which the investigation then lists, each searched only with the identifiers its connector takes. A list sent here still limits the investigation until a later contract release removes the field."""

    enrichment: Optional[EnrichmentChange] = None
    r"""A change to enrichment. A field left out keeps the value in force; max_spend or deadline null removes the bound."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["platforms", "enrichment"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
