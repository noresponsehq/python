from __future__ import annotations
from .credentialassociationactor import (
    CredentialAssociationActor,
    CredentialAssociationActorTypedDict,
)
from .credentialassociationretiredby import (
    CredentialAssociationRetiredBy,
    CredentialAssociationRetiredByTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CredentialAssociationTypedDict(TypedDict):
    r"""An association between an account and an issued key. The response excludes the key and its hash. Retirement removes this association from risk calculations; revoke the actual key through your own service."""

    id: str
    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    created_at: str
    actor: CredentialAssociationActorTypedDict
    retired_at: NotRequired[str]
    retired_by: NotRequired[CredentialAssociationRetiredByTypedDict]


class CredentialAssociation(BaseModel):
    r"""An association between an account and an issued key. The response excludes the key and its hash. Retirement removes this association from risk calculations; revoke the actual key through your own service."""

    id: str

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    created_at: str

    actor: CredentialAssociationActor

    retired_at: Optional[str] = None

    retired_by: Optional[CredentialAssociationRetiredBy] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["retired_at", "retired_by"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
