from __future__ import annotations
from .handleplatform import HandlePlatform
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class HandleTypedDict(TypedDict):
    r"""An account the attendee is known to hold."""

    platform: HandlePlatform
    handle: str
    r"""The account's handle, without a leading @."""


class Handle(BaseModel):
    r"""An account the attendee is known to hold."""

    platform: HandlePlatform

    handle: str
    r"""The account's handle, without a leading @."""
