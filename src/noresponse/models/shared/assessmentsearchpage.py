from __future__ import annotations
from .assessmentrevision import AssessmentRevision, AssessmentRevisionTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssessmentSearchPageTypedDict(TypedDict):
    r"""A bounded page of latest assessment revisions, newest creation first. Each revision identifies the exact result found; no current account risk is attached."""

    items: List[AssessmentRevisionTypedDict]
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    next_cursor: NotRequired[str]
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""
    retention_days: NotRequired[int]
    r"""The calling workspace's configured retention period in days. Default 365 (12 months), which is also the maximum: a workspace may only shorten it, to at least 1 day. Each record expires from its own created_at; see assessment expires_at."""


class AssessmentSearchPage(BaseModel):
    r"""A bounded page of latest assessment revisions, newest creation first. Each revision identifies the exact result found; no current account risk is attached."""

    items: List[AssessmentRevision]

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    next_cursor: Optional[str] = None
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""

    retention_days: Optional[int] = 365
    r"""The calling workspace's configured retention period in days. Default 365 (12 months), which is also the maximum: a workspace may only shorten it, to at least 1 day. Each record expires from its own created_at; see assessment expires_at."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_cursor", "retention_days"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    AssessmentSearchPage.model_rebuild()
except NameError:
    pass
