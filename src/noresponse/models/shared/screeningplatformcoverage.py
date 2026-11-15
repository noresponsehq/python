from __future__ import annotations
from .screeningplatformcoveragestatus import ScreeningPlatformCoverageStatus
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningPlatformCoverageTypedDict(TypedDict):
    r"""What a screening read on one platform."""

    platform: str
    r"""A platform a screening can cover, such as instagram, x, bluesky, youtube, tiktok or github. The screening registry owns the set: a request that names a platform it does not cover answers 422. A new platform adds an id without changing this contract, so read a platform you do not know in a response as one you have not seen before, not as an error. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
    status: ScreeningPlatformCoverageStatus
    r"""covered read at least one profile; none_found looked and found no account; inaccessible found accounts that are private or locked; failed could not finish looking; unavailable has no resolver or collector enabled."""
    accounts_found: int
    items_read: int


class ScreeningPlatformCoverage(BaseModel):
    r"""What a screening read on one platform."""

    platform: str
    r"""A platform a screening can cover, such as instagram, x, bluesky, youtube, tiktok or github. The screening registry owns the set: a request that names a platform it does not cover answers 422. A new platform adds an id without changing this contract, so read a platform you do not know in a response as one you have not seen before, not as an error. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""

    status: ScreeningPlatformCoverageStatus
    r"""covered read at least one profile; none_found looked and found no account; inaccessible found accounts that are private or locked; failed could not finish looking; unavailable has no resolver or collector enabled."""

    accounts_found: int

    items_read: int
