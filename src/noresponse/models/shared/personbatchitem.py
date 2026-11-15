from __future__ import annotations
from .personbatchitemoutcome import PersonBatchItemOutcome
from .personmatch import PersonMatch, PersonMatchTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PersonBatchItemTypedDict(TypedDict):
    index: int
    r"""The row's position in the request."""
    id: str
    outcome: PersonBatchItemOutcome
    r"""unchanged: the row matched a person with the same details."""
    suggested_matches: NotRequired[List[PersonMatchTypedDict]]


class PersonBatchItem(BaseModel):
    index: int
    r"""The row's position in the request."""

    id: str

    outcome: PersonBatchItemOutcome
    r"""unchanged: the row matched a person with the same details."""

    suggested_matches: Optional[List[PersonMatch]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["suggested_matches"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
