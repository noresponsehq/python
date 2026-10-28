from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SentIdentifiersTypedDict(TypedDict):
    r"""The identifiers an assessment was sent: each member of the request's identifiers object exactly as received, before the server normalised it (the email domain keeps its case, the name its Unicode form). A member the request did not send is absent. NoResponse keeps them encrypted under the workspace's own key, does not index or log them, and deletes them with the assessment: on DELETE of the assessment or its account, at its expires_at, and with the workspace."""

    email: NotRequired[str]
    r"""identifiers.email as the request sent it."""
    username: NotRequired[str]
    r"""identifiers.username as the request sent it."""
    phone: NotRequired[str]
    r"""identifiers.phone as the request sent it."""
    name: NotRequired[str]
    r"""identifiers.name as the request sent it, before NFC normalisation."""
    ip: NotRequired[str]
    r"""identifiers.ip as the request sent it."""


class SentIdentifiers(BaseModel):
    r"""The identifiers an assessment was sent: each member of the request's identifiers object exactly as received, before the server normalised it (the email domain keeps its case, the name its Unicode form). A member the request did not send is absent. NoResponse keeps them encrypted under the workspace's own key, does not index or log them, and deletes them with the assessment: on DELETE of the assessment or its account, at its expires_at, and with the workspace."""

    email: Optional[str] = None
    r"""identifiers.email as the request sent it."""

    username: Optional[str] = None
    r"""identifiers.username as the request sent it."""

    phone: Optional[str] = None
    r"""identifiers.phone as the request sent it."""

    name: Optional[str] = None
    r"""identifiers.name as the request sent it, before NFC normalisation."""

    ip: Optional[str] = None
    r"""identifiers.ip as the request sent it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["email", "username", "phone", "name", "ip"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
