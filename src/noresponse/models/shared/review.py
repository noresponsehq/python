from __future__ import annotations
from .priority import Priority
from .resolution import Resolution, ResolutionTypedDict
from .reviewstatus import ReviewStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ReviewTypedDict(TypedDict):
    id: str
    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    status: ReviewStatus
    priority: Priority
    version: int
    opened_risk_version: int
    current_risk_version: int
    created_by: str
    updated_by: str
    created_at: str
    updated_at: str
    expires_at: str
    assignee: NotRequired[str]
    resolution: NotRequired[ResolutionTypedDict]
    assignee_principal_id: NotRequired[str]
    r"""Immutable workspace member ID. assignee is the historical display identity captured at assignment."""


class Review(BaseModel):
    id: str

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    status: ReviewStatus

    priority: Priority

    version: int

    opened_risk_version: int

    current_risk_version: int

    created_by: str

    updated_by: str

    created_at: str

    updated_at: str

    expires_at: str

    assignee: Optional[str] = None

    resolution: Optional[Resolution] = None

    assignee_principal_id: Optional[str] = None
    r"""Immutable workspace member ID. assignee is the historical display identity captured at assignment."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["assignee", "resolution", "assignee_principal_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
