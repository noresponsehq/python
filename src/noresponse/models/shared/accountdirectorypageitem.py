from __future__ import annotations
from .account import Account, AccountTypedDict
from .assessmentrevision import AssessmentRevision, AssessmentRevisionTypedDict
from .identifiermatch import IdentifierMatch, IdentifierMatchTypedDict
from .identifiertermmatch import IdentifierTermMatch, IdentifierTermMatchTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL, UnrecognizedStr
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


WaitingFor = Union[
    Literal[
        "outcome",
        "review",
    ],
    UnrecognizedStr,
]


class AccountDirectoryPageItemTypedDict(TypedDict):
    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    latest: AssessmentRevisionTypedDict
    r"""Retrieve a retained assessment version with its original decision, policy, flow and depth. This response excludes the current account decision. Current retention and response-mode permissions still apply."""
    assessments: int
    r"""Count of admitted retained assessments belonging to this account, not just the returned page."""
    waiting_for: NotRequired[List[WaitingFor]]
    r"""Present for needs_action searches. outcome means a current review/block decision lacks a retained effective outcome; review means a retained open or in-progress review. Both can apply."""
    current: NotRequired[AccountTypedDict]
    r"""Body of the 200 answer to GET /v1/accounts/{account_id}: the one current risk of one of the calling workspace's accounts. It is the risk of the account's latest assessment that has a decision (status complete or partial), by created_at and then assessment_id, scored exactly as GET /v1/assessments/{assessment_id} scores that assessment, plus the account's own reason shared_api_key when a key issued to the account was used from many IP addresses or countries (POST /v1/key_usage/batches). Its assessments are the account's history (GET /v1/accounts/{account_id}/assessments)."""
    matched_identifier: NotRequired[IdentifierMatchTypedDict]
    r"""Why this result matched a typed identifier search. value is the original value submitted in assessment_id. Provenance records a customer submission, not a source discovery or verified ownership. Equality is deterministic and has no inferred confidence score. An account result names its newest retained matching assessment, which can differ from latest."""
    matched_identifiers: NotRequired[List[IdentifierTermMatchTypedDict]]
    r"""Present only for identifier_expression. All satisfied unique terms, ordered by term_index, with original submitted values and retained assessment witnesses. A duplicate normalized term appears once at its first raw leaf index. The legacy single identifier filter instead returns matched_identifier."""


class AccountDirectoryPageItem(BaseModel):
    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    latest: AssessmentRevision
    r"""Retrieve a retained assessment version with its original decision, policy, flow and depth. This response excludes the current account decision. Current retention and response-mode permissions still apply."""

    assessments: int
    r"""Count of admitted retained assessments belonging to this account, not just the returned page."""

    waiting_for: Optional[List[WaitingFor]] = None
    r"""Present for needs_action searches. outcome means a current review/block decision lacks a retained effective outcome; review means a retained open or in-progress review. Both can apply."""

    current: Optional[Account] = None
    r"""Body of the 200 answer to GET /v1/accounts/{account_id}: the one current risk of one of the calling workspace's accounts. It is the risk of the account's latest assessment that has a decision (status complete or partial), by created_at and then assessment_id, scored exactly as GET /v1/assessments/{assessment_id} scores that assessment, plus the account's own reason shared_api_key when a key issued to the account was used from many IP addresses or countries (POST /v1/key_usage/batches). Its assessments are the account's history (GET /v1/accounts/{account_id}/assessments)."""

    matched_identifier: Optional[IdentifierMatch] = None
    r"""Why this result matched a typed identifier search. value is the original value submitted in assessment_id. Provenance records a customer submission, not a source discovery or verified ownership. Equality is deterministic and has no inferred confidence score. An account result names its newest retained matching assessment, which can differ from latest."""

    matched_identifiers: Optional[List[IdentifierTermMatch]] = None
    r"""Present only for identifier_expression. All satisfied unique terms, ordered by term_index, with original submitted values and retained assessment witnesses. A duplicate normalized term appears once at its first raw leaf index. The legacy single identifier filter instead returns matched_identifier."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["waiting_for", "current", "matched_identifier", "matched_identifiers"]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
