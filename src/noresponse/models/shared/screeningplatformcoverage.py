from __future__ import annotations
from .handleplatform import HandlePlatform
from .screeningplatformcoveragestatus import ScreeningPlatformCoverageStatus
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningPlatformCoverageTypedDict(TypedDict):
    r"""What a screening read on one platform."""

    platform: HandlePlatform
    r"""A platform a screening can cover. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
    status: ScreeningPlatformCoverageStatus
    r"""covered read at least one profile; none_found looked and found no account; inaccessible found accounts that are private or locked; failed could not finish looking; unavailable has no resolver or collector enabled."""
    accounts_found: int
    items_read: int


class ScreeningPlatformCoverage(BaseModel):
    r"""What a screening read on one platform."""

    platform: HandlePlatform
    r"""A platform a screening can cover. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""

    status: ScreeningPlatformCoverageStatus
    r"""covered read at least one profile; none_found looked and found no account; inaccessible found accounts that are private or locked; failed could not finish looking; unavailable has no resolver or collector enabled."""

    accounts_found: int

    items_read: int
