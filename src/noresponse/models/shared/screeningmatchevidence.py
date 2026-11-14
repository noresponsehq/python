from __future__ import annotations
from .screeningmatchevidencekind import ScreeningMatchEvidenceKind
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningMatchEvidenceTypedDict(TypedDict):
    r"""One identifier that ties a profile to the person."""

    kind: ScreeningMatchEvidenceKind
    r"""What matched. email, phone, supplied_handle and source_fact are hard identifiers; company, city and school are soft. supplied_handle is a handle on the person row; source_fact is an account a profile found by the person's lookups lists."""
    resolver: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""
    detail: NotRequired[str]
    r"""Where the match was seen, such as the profile field that carried it."""


class ScreeningMatchEvidence(BaseModel):
    r"""One identifier that ties a profile to the person."""

    kind: ScreeningMatchEvidenceKind
    r"""What matched. email, phone, supplied_handle and source_fact are hard identifiers; company, city and school are soft. supplied_handle is a handle on the person row; source_fact is an account a profile found by the person's lookups lists."""

    resolver: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""

    detail: Optional[str] = None
    r"""Where the match was seen, such as the profile field that carried it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["detail"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
