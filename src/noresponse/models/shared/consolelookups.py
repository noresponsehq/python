from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ConsoleLookupsTypedDict(TypedDict):
    r"""The live environment's daily cap on assessments members make through the console (the playground), as spent on the current UTC day. Each console submission with a new Idempotency-Key spends one lookup; a replay spends nothing, and API keys and the test environment spend none. When used reaches limit, the next lookup answers 429 lookup_limit_reached until resets_at. The count is the one the cap enforces."""

    used: int
    r"""Lookups spent since the last reset."""
    limit: int
    r"""Lookups allowed per UTC day."""
    resets_at: str
    r"""The next reset: the coming midnight UTC, when used returns to 0."""


class ConsoleLookups(BaseModel):
    r"""The live environment's daily cap on assessments members make through the console (the playground), as spent on the current UTC day. Each console submission with a new Idempotency-Key spends one lookup; a replay spends nothing, and API keys and the test environment spend none. When used reaches limit, the next lookup answers 429 lookup_limit_reached until resets_at. The count is the one the cap enforces."""

    used: int
    r"""Lookups spent since the last reset."""

    limit: int
    r"""Lookups allowed per UTC day."""

    resets_at: str
    r"""The next reset: the coming midnight UTC, when used returns to 0."""
