from __future__ import annotations
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningRequestTypedDict(TypedDict):
    r"""Screens the group's people no screening has reached."""

    depth: ScreeningDepth


class ScreeningRequest(BaseModel):
    r"""Screens the group's people no screening has reached."""

    depth: ScreeningDepth
