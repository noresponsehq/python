from __future__ import annotations
from .identifiersearchkind import IdentifierSearchKind
from .match import Match
from .namespace import Namespace
from .provenance import Provenance
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IdentifierMatchTypedDict(TypedDict):
    r"""Why this result matched a typed identifier search. value is the original value submitted in assessment_id. Provenance records a customer submission, not a source discovery or verified ownership. Equality is deterministic and has no inferred confidence score. An account result names its newest retained matching assessment, which can differ from latest."""

    kind: IdentifierSearchKind
    value: str
    match_basis: Match
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""
    provenance: Provenance
    r"""Customer-submitted input. It does not mean the customer or NoResponse verified ownership."""
    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""
    namespace: NotRequired[Namespace]
    r"""Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone."""


class IdentifierMatch(BaseModel):
    r"""Why this result matched a typed identifier search. value is the original value submitted in assessment_id. Provenance records a customer submission, not a source discovery or verified ownership. Equality is deterministic and has no inferred confidence score. An account result names its newest retained matching assessment, which can differ from latest."""

    kind: IdentifierSearchKind

    value: str

    match_basis: Match
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""

    provenance: Provenance
    r"""Customer-submitted input. It does not mean the customer or NoResponse verified ownership."""

    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""

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
