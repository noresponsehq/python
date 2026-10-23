from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class KeyUsageEventTypedDict(TypedDict):
    r"""One request made with an issued key. An event whose ip is not a public address, or whose occurred_at is more than 24 hours old or more than 5 minutes ahead, is counted in ignored and adds nothing."""

    key_sha256: str
    r"""SHA-256 of the issued key's UTF-8 bytes, as 64 lower-case hex characters: the value sent as issued_credential.sha256 when the account was assessed. Each SDK's issued-credential helper computes it."""
    ip: str
    r"""The client IP address the request came from, IPv4 or IPv6, as your server saw it. Stored only as a keyed digest and its country."""
    occurred_at: str
    r"""When the request was made."""
    user_agent: NotRequired[str]
    r"""The request's User-Agent header, at most 512 characters. Stored only as a keyed digest."""
    model: NotRequired[str]
    r"""The model or product the request used, such as gpt-4o-mini. Stored only as a keyed digest."""
    input_tokens: NotRequired[int]
    r"""Input tokens the request consumed."""
    output_tokens: NotRequired[int]
    r"""Output tokens the request produced."""
    sample_rate: NotRequired[float]
    r"""The share of requests your sampler records, when it records only some: 0.1 means this event stands for 10 requests. Request and token totals are weighted by its inverse. Distinct IP and country counts see only the events sent."""


class KeyUsageEvent(BaseModel):
    r"""One request made with an issued key. An event whose ip is not a public address, or whose occurred_at is more than 24 hours old or more than 5 minutes ahead, is counted in ignored and adds nothing."""

    key_sha256: str
    r"""SHA-256 of the issued key's UTF-8 bytes, as 64 lower-case hex characters: the value sent as issued_credential.sha256 when the account was assessed. Each SDK's issued-credential helper computes it."""

    ip: str
    r"""The client IP address the request came from, IPv4 or IPv6, as your server saw it. Stored only as a keyed digest and its country."""

    occurred_at: str
    r"""When the request was made."""

    user_agent: Optional[str] = None
    r"""The request's User-Agent header, at most 512 characters. Stored only as a keyed digest."""

    model: Optional[str] = None
    r"""The model or product the request used, such as gpt-4o-mini. Stored only as a keyed digest."""

    input_tokens: Optional[int] = None
    r"""Input tokens the request consumed."""

    output_tokens: Optional[int] = None
    r"""Output tokens the request produced."""

    sample_rate: Optional[float] = 1.0
    r"""The share of requests your sampler records, when it records only some: 0.1 means this event stands for 10 requests. Request and token totals are weighted by its inverse. Distinct IP and country counts see only the events sent."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["user_agent", "model", "input_tokens", "output_tokens", "sample_rate"]
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
