from __future__ import annotations
from .identifiersearch import IdentifierSearch, IdentifierSearchTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AccountDirectorySearchRequestTypedDict(TypedDict):
    r"""Bounded distinct-account search for one authenticated workspace/environment. identifier matches any retained admitted assessment of an account, including historical submitted values. email preserves the legacy canonical-mailbox filter. identifier and email cannot be combined. All other filters combine using AND. Typed identifier search uses stable opaque account order; ordinary and legacy email searches retain newest-seen ordering. Pages are live, not a cross-page snapshot. Requires history or investigate authority and identifier-read permission for identifier or email filtering."""

    needs_action: NotRequired[bool]
    r"""Select accounts with a retained open or in-progress review, or a current review/block account decision with no retained effective account outcome. The server applies this filter before counting and pagination. Requires reviews.read as well as history.read for console members; API keys additionally require management."""
    account_id: NotRequired[str]
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    email: NotRequired[str]
    r"""Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400."""
    limit: NotRequired[int]
    cursor: NotRequired[str]
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""
    identifier: NotRequired[IdentifierSearchTypedDict]
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""


class AccountDirectorySearchRequest(BaseModel):
    r"""Bounded distinct-account search for one authenticated workspace/environment. identifier matches any retained admitted assessment of an account, including historical submitted values. email preserves the legacy canonical-mailbox filter. identifier and email cannot be combined. All other filters combine using AND. Typed identifier search uses stable opaque account order; ordinary and legacy email searches retain newest-seen ordering. Pages are live, not a cross-page snapshot. Requires history or investigate authority and identifier-read permission for identifier or email filtering."""

    needs_action: Optional[bool] = False
    r"""Select accounts with a retained open or in-progress review, or a current review/block account decision with no retained effective account outcome. The server applies this filter before counting and pagination. Requires reviews.read as well as history.read for console members; API keys additionally require management."""

    account_id: Optional[str] = None
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    email: Optional[str] = None
    r"""Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400."""

    limit: Optional[int] = 25

    cursor: Optional[str] = None
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""

    identifier: Optional[IdentifierSearch] = None
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["needs_action", "account_id", "email", "limit", "cursor", "identifier"]
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
