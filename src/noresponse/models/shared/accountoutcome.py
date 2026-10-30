from __future__ import annotations
from .accountoutcomeactor import AccountOutcomeActor, AccountOutcomeActorTypedDict
from .outcome import Outcome
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AccountOutcomeTypedDict(TypedDict):
    r"""Immutable acceptance receipt. risk_version is the account version after this report committed, not the version when a retry reads it. effective_outcome_id names the effective head at that write. The effective expiration may shorten under retention changes. A legitimate report or correction removes only the account-feedback contribution, not unrelated risk."""

    id: str
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""
    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    outcome: Outcome
    r"""What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins."""
    observed_at: str
    received_at: str
    expires_at: str
    actor: AccountOutcomeActorTypedDict
    risk_version_before: int
    risk_version: int
    supersedes: NotRequired[str]
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""
    external_ref: NotRequired[str]
    r"""Your own opaque reference for the outcome, such as a case or ticket id. Stored as given and not interpreted; keep direct identifiers out of it."""
    effective_outcome_id: NotRequired[str]
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""


class AccountOutcome(BaseModel):
    r"""Immutable acceptance receipt. risk_version is the account version after this report committed, not the version when a retry reads it. effective_outcome_id names the effective head at that write. The effective expiration may shorten under retention changes. A legitimate report or correction removes only the account-feedback contribution, not unrelated risk."""

    id: str
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    outcome: Outcome
    r"""What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins."""

    observed_at: str

    received_at: str

    expires_at: str

    actor: AccountOutcomeActor

    risk_version_before: int

    risk_version: int

    supersedes: Optional[str] = None
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""

    external_ref: Optional[str] = None
    r"""Your own opaque reference for the outcome, such as a case or ticket id. Stored as given and not interpreted; keep direct identifiers out of it."""

    effective_outcome_id: Optional[str] = None
    r"""Opaque, server-assigned id of one recorded outcome: 'out_' and a 26-character Crockford base32 ULID. Unique within the workspace."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["supersedes", "external_ref", "effective_outcome_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
