from __future__ import annotations
from .assessmentdetail import AssessmentDetail, AssessmentDetailTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssessmentListTypedDict(TypedDict):
    r"""Body of the 200 answer to POST /v1/assessments/query: one page of the calling workspace's unexpired assessments for one account, newest first, each at its latest assessment_version, as its detail; the account's current risk is GET /v1/accounts/{account_id}. Every item's account_id equals the page's. An assessment past its expires_at is not listed. next_cursor is present only when another page exists."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    items: List[AssessmentDetailTypedDict]
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    next_cursor: NotRequired[str]
    r"""Opaque cursor for the next page, bound to your workspace and the account_id it was issued for. Pass it back unchanged in the next query; a tampered, foreign or expired cursor answers 400 invalid_cursor."""
    retention_days: NotRequired[int]
    r"""Your current retention period, so a consumer knows how far back history reaches. Every item expires no later than its created_at plus this many days."""


class AssessmentList(BaseModel):
    r"""Body of the 200 answer to POST /v1/assessments/query: one page of the calling workspace's unexpired assessments for one account, newest first, each at its latest assessment_version, as its detail; the account's current risk is GET /v1/accounts/{account_id}. Every item's account_id equals the page's. An assessment past its expires_at is not listed. next_cursor is present only when another page exists."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    items: List[AssessmentDetail]

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    next_cursor: Optional[str] = None
    r"""Opaque cursor for the next page, bound to your workspace and the account_id it was issued for. Pass it back unchanged in the next query; a tampered, foreign or expired cursor answers 400 invalid_cursor."""

    retention_days: Optional[int] = 365
    r"""Your current retention period, so a consumer knows how far back history reaches. Every item expires no later than its created_at plus this many days."""

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
    AssessmentList.model_rebuild()
except NameError:
    pass
