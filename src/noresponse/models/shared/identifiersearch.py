from __future__ import annotations
from .identifiersearchkind import IdentifierSearchKind
from .match import Match
from .namespace import Namespace
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IdentifierSearchTypedDict(TypedDict):
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""

    kind: IdentifierSearchKind
    value: str
    r"""The comparison value. Stored original identifiers remain unchanged. An invalid identifier is refused instead of returning an empty result."""
    match: NotRequired[Match]
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""
    namespace: NotRequired[Namespace]
    r"""Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone."""


class IdentifierSearch(BaseModel):
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""

    kind: IdentifierSearchKind

    value: str
    r"""The comparison value. Stored original identifiers remain unchanged. An invalid identifier is refused instead of returning an empty result."""

    match: Optional[Match] = None
    r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""

    namespace: Optional[Namespace] = None
    r"""Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["match", "namespace"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
