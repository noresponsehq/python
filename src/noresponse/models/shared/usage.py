from __future__ import annotations
from .usagecount import UsageCount, UsageCountTypedDict
from noresponse.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class UsageTypedDict(TypedDict):
    r"""Body of the 200 answer to GET /v1/workspaces/{workspace_id}/usage: what the workspace's environments were metered for on each UTC day from from through to. Each billable unit is counted once, where it becomes final: an assessment when it is admitted (by flow and depth), a webhook delivery once per event per endpoint (retries and replays add nothing), and a key-usage event once when the ingest accepts it. A count does not change when the assessment, account or workspace is later deleted. A day, environment or metric with nothing counted has no item. No prices, limits or billing."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    from_: str
    r"""The first UTC day covered."""
    to: str
    r"""The last UTC day covered, included."""
    items: List[UsageCountTypedDict]
    r"""Ordered by environment (live first), then day, metric, flow and depth."""


class Usage(BaseModel):
    r"""Body of the 200 answer to GET /v1/workspaces/{workspace_id}/usage: what the workspace's environments were metered for on each UTC day from from through to. Each billable unit is counted once, where it becomes final: an assessment when it is admitted (by flow and depth), a webhook delivery once per event per endpoint (retries and replays add nothing), and a key-usage event once when the ingest accepts it. A count does not change when the assessment, account or workspace is later deleted. A day, environment or metric with nothing counted has no item. No prices, limits or billing."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    from_: Annotated[str, pydantic.Field(alias="from")]
    r"""The first UTC day covered."""

    to: str
    r"""The last UTC day covered, included."""

    items: List[UsageCount]
    r"""Ordered by environment (live first), then day, metric, flow and depth."""


try:
    Usage.model_rebuild()
except NameError:
    pass
