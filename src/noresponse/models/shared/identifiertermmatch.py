from __future__ import annotations
from .identifiersearchkind import IdentifierSearchKind
from .match import Match
from .namespace import Namespace
from .provenance import Provenance
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IdentifierTermMatchTypedDict(TypedDict):
    r"""One satisfied unique term in an identifier expression. term_index is the zero-based depth-first raw leaf position of its first occurrence. Duplicate normalized terms produce one witness. All satisfied unique terms are returned, ordered by term_index, including satisfied terms in an OR branch that was not needed. value preserves the original submitted value in assessment_id. In assessment scope all witnesses belong to the same matching assessment; account search chooses the newest such assessment. In account scope each term uses its newest retained matching assessment, so witnesses may have different assessment IDs. This evidence does not assert ownership or equality between accounts."""

    kind: IdentifierSearchKind
    value: str
    match_basis: Match
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""
    provenance: Provenance
    r"""Customer-submitted input. It does not mean the customer or NoResponse verified ownership."""
    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""
    term_index: int
    r"""Zero-based depth-first position of the first occurrence of this normalized term in the submitted expression."""
    namespace: NotRequired[Namespace]
    r"""Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone."""


class IdentifierTermMatch(BaseModel):
    r"""One satisfied unique term in an identifier expression. term_index is the zero-based depth-first raw leaf position of its first occurrence. Duplicate normalized terms produce one witness. All satisfied unique terms are returned, ordered by term_index, including satisfied terms in an OR branch that was not needed. value preserves the original submitted value in assessment_id. In assessment scope all witnesses belong to the same matching assessment; account search chooses the newest such assessment. In account scope each term uses its newest retained matching assessment, so witnesses may have different assessment IDs. This evidence does not assert ownership or equality between accounts."""

    kind: IdentifierSearchKind

    value: str

    match_basis: Match
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""

    provenance: Provenance
    r"""Customer-submitted input. It does not mean the customer or NoResponse verified ownership."""

    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the workspace; another workspace's assessment id answers 404."""

    term_index: int
    r"""Zero-based depth-first position of the first occurrence of this normalized term in the submitted expression."""

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
