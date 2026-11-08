from __future__ import annotations
from .screeningdepth import ScreeningDepth
from noresponse.types import BaseModel
from typing import List, Literal
from typing_extensions import TypedDict


ScreeningRequestPlatform = Literal[
    "instagram",
    "x",
    "bluesky",
    "youtube",
    "tiktok",
    "facebook",
    "threads",
    "reddit",
    "telegram",
    "linkedin",
]


class ScreeningRequestTypedDict(TypedDict):
    r"""Screens the event's attendees no screening has reached and everyone on watch or escalated."""

    depth: ScreeningDepth
    platforms: List[ScreeningRequestPlatform]


class ScreeningRequest(BaseModel):
    r"""Screens the event's attendees no screening has reached and everyone on watch or escalated."""

    depth: ScreeningDepth

    platforms: List[ScreeningRequestPlatform]
