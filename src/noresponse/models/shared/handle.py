from __future__ import annotations
from .handleplatform import HandlePlatform
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class HandleTypedDict(TypedDict):
    r"""An account the person is known to hold."""

    platform: HandlePlatform
    r"""A platform a screening can cover. github and scratch through flickr are each one read of the public profile a handle names, with no posts. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
    handle: str
    r"""The account's handle, without a leading @."""


class Handle(BaseModel):
    r"""An account the person is known to hold."""

    platform: HandlePlatform
    r"""A platform a screening can cover. github and scratch through flickr are each one read of the public profile a handle names, with no posts. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""

    handle: str
    r"""The account's handle, without a leading @."""
