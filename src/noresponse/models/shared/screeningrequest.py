from __future__ import annotations
from .handleplatform import HandlePlatform
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ScreeningRequestTypedDict(TypedDict):
    r"""Screens the event's attendees no screening has reached and everyone on watch or escalated."""

    depth: ScreeningDepth
    platforms: List[HandlePlatform]


class ScreeningRequest(BaseModel):
    r"""Screens the event's attendees no screening has reached and everyone on watch or escalated."""

    depth: ScreeningDepth

    platforms: List[HandlePlatform]
