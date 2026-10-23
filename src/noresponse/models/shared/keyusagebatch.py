from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class KeyUsageBatchTypedDict(TypedDict):
    r"""The 202 answer of POST /v1/key_usage/batches. A replay with the same Idempotency-Key and body answers the same record and counts nothing again."""

    id: str
    r"""Opaque, server-assigned id of the batch: 'kub_' and a 26-character Crockford base32 ULID."""
    received_at: str
    r"""When NoResponse first recorded the batch."""
    accepted: int
    r"""Events counted."""
    ignored: int
    r"""Events that added nothing: a private, reserved or unreadable ip, or an occurred_at more than 24 hours old or more than 5 minutes ahead."""


class KeyUsageBatch(BaseModel):
    r"""The 202 answer of POST /v1/key_usage/batches. A replay with the same Idempotency-Key and body answers the same record and counts nothing again."""

    id: str
    r"""Opaque, server-assigned id of the batch: 'kub_' and a 26-character Crockford base32 ULID."""

    received_at: str
    r"""When NoResponse first recorded the batch."""

    accepted: int
    r"""Events counted."""

    ignored: int
    r"""Events that added nothing: a private, reserved or unreadable ip, or an occurred_at more than 24 hours old or more than 5 minutes ahead."""
