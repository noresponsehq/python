from __future__ import annotations
from .identifiersearchkind import IdentifierSearchKind
from .identifiersubmission import IdentifierSubmission, IdentifierSubmissionTypedDict
from .match import Match
from .namespace import Namespace
from .provenance import Provenance
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SharedIdentifierTypedDict(TypedDict):
    kind: IdentifierSearchKind
    match_basis: Match
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""
    provenance: Provenance
    r"""Customer-submitted input. It does not mean the customer or NoResponse verified ownership."""
    account: IdentifierSubmissionTypedDict
    linked_account: IdentifierSubmissionTypedDict
    namespace: NotRequired[Namespace]
    r"""Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone."""


class SharedIdentifier(BaseModel):
    kind: IdentifierSearchKind

    match_basis: Match
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""

    provenance: Provenance
    r"""Customer-submitted input. It does not mean the customer or NoResponse verified ownership."""

    account: IdentifierSubmission

    linked_account: IdentifierSubmission

    namespace: Optional[Namespace] = None
    r"""Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["namespace"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
