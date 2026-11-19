from __future__ import annotations
from .stagetime import StageTime, StageTimeTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ScreeningCoverageTimingTypedDict(TypedDict):
    r"""How long this search's latest attempt took, stage by stage. started_at minus the investigation's creation is the time spent queued or retrying."""

    started_at: str
    r"""When the attempt that wrote this result started."""
    total_ms: int
    r"""Milliseconds from started_at to the end of the last stage listed."""
    stages: List[StageTimeTypedDict]
    r"""Stages finished so far, in order. The result first written lists stages up to written; the settled result lists them all."""


class ScreeningCoverageTiming(BaseModel):
    r"""How long this search's latest attempt took, stage by stage. started_at minus the investigation's creation is the time spent queued or retrying."""

    started_at: str
    r"""When the attempt that wrote this result started."""

    total_ms: int
    r"""Milliseconds from started_at to the end of the last stage listed."""

    stages: List[StageTime]
    r"""Stages finished so far, in order. The result first written lists stages up to written; the settled result lists them all."""
