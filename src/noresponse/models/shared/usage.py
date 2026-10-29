from __future__ import annotations
from .consolelookups import ConsoleLookups, ConsoleLookupsTypedDict
from .usagecount import UsageCount, UsageCountTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UsageTypedDict(TypedDict):
    r"""Body of the 200 answer to GET /v1/workspaces/{workspace_id}/usage: what the workspace's environments were metered for on each UTC day from from through to. Each billable unit is counted once, where it becomes final: an assessment when it is admitted (by flow and depth), a webhook delivery once per event per endpoint (retries and replays add nothing), and a key-usage event once when the ingest accepts it. A count does not change when the assessment, account or workspace is later deleted. A day, environment or metric with nothing counted has no item. No prices or billing. console_lookups is the one limit: the live environment's daily cap on console lookups, as spent today."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    from_: str
    r"""The first UTC day covered."""
    to: str
    r"""The last UTC day covered, included."""
    items: List[UsageCountTypedDict]
    r"""Ordered by environment (live first), then day, metric, flow and depth."""
    console_lookups: NotRequired[ConsoleLookupsTypedDict]
    r"""The live environment's daily cap on assessments members make through the console (the playground), as spent on the current UTC day. Each console submission with a new Idempotency-Key spends one lookup; a replay spends nothing, and API keys and the test environment spend none. When used reaches limit, the next lookup answers 429 lookup_limit_reached until resets_at. The count is the one the cap enforces."""


class Usage(BaseModel):
    r"""Body of the 200 answer to GET /v1/workspaces/{workspace_id}/usage: what the workspace's environments were metered for on each UTC day from from through to. Each billable unit is counted once, where it becomes final: an assessment when it is admitted (by flow and depth), a webhook delivery once per event per endpoint (retries and replays add nothing), and a key-usage event once when the ingest accepts it. A count does not change when the assessment, account or workspace is later deleted. A day, environment or metric with nothing counted has no item. No prices or billing. console_lookups is the one limit: the live environment's daily cap on console lookups, as spent today."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    from_: Annotated[str, pydantic.Field(alias="from")]
    r"""The first UTC day covered."""

    to: str
    r"""The last UTC day covered, included."""

    items: List[UsageCount]
    r"""Ordered by environment (live first), then day, metric, flow and depth."""

    console_lookups: Optional[ConsoleLookups] = None
    r"""The live environment's daily cap on assessments members make through the console (the playground), as spent on the current UTC day. Each console submission with a new Idempotency-Key spends one lookup; a replay spends nothing, and API keys and the test environment spend none. When used reaches limit, the next lookup answers 429 lookup_limit_reached until resets_at. The count is the one the cap enforces."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["console_lookups"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    Usage.model_rebuild()
except NameError:
    pass
