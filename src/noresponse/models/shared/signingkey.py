from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SigningKeyTypedDict(TypedDict):
    r"""One signing key, by id. The secret is not included."""

    key_id: str
    r"""The signing key id, sent as NR-Webhook-Key-Id on every delivery it signs."""
    created_at: str
    expires_at: NotRequired[str]
    r"""Present on a key a rotation replaced: it stops verifying at this instant, 7 days after the rotation. Absent on the key that signs."""


class SigningKey(BaseModel):
    r"""One signing key, by id. The secret is not included."""

    key_id: str
    r"""The signing key id, sent as NR-Webhook-Key-Id on every delivery it signs."""

    created_at: str

    expires_at: Optional[str] = None
    r"""Present on a key a rotation replaced: it stops verifying at this instant, 7 days after the rotation. Absent on the key that signs."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["expires_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
