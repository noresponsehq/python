from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class HandleTypedDict(TypedDict):
    r"""An account the person is known to hold."""

    platform: str
    r"""A platform a screening can cover, such as instagram, x, bluesky, youtube, tiktok or github. The screening registry owns the set: a request that names a platform it does not cover answers 422. A new platform adds an id without changing this contract, so read a platform you do not know in a response as one you have not seen before, not as an error. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
    handle: str
    r"""The account's handle, without a leading @."""


class Handle(BaseModel):
    r"""An account the person is known to hold."""

    platform: str
    r"""A platform a screening can cover, such as instagram, x, bluesky, youtube, tiktok or github. The screening registry owns the set: a request that names a platform it does not cover answers 422. A new platform adds an id without changing this contract, so read a platform you do not know in a response as one you have not seen before, not as an error. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""

    handle: str
    r"""The account's handle, without a leading @."""
