from __future__ import annotations
from .access import Access
from .handleplatform import HandlePlatform
from .screeningmatch import ScreeningMatch, ScreeningMatchTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningProfileTypedDict(TypedDict):
    r"""An account the screening matched to the attendee, how it was matched, and how much of it was read."""

    id: str
    platform: HandlePlatform
    r"""A platform a screening can cover. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
    handle: str
    url: str
    access: Access
    r"""public profiles were read; a private or locked one exists but could not be read."""
    match: ScreeningMatchTypedDict
    r"""How a profile was matched to the attendee: the state its evidence earns, and the evidence."""
    collector: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""
    items_read: int
    collected_at: str
    display_name: NotRequired[str]
    bio: NotRequired[str]
    avatar_url: NotRequired[str]
    followers: NotRequired[int]
    account_created_at: NotRequired[str]
    period_from: NotRequired[str]
    r"""The oldest item read."""
    period_to: NotRequired[str]
    r"""The newest item read."""


class ScreeningProfile(BaseModel):
    r"""An account the screening matched to the attendee, how it was matched, and how much of it was read."""

    id: str

    platform: HandlePlatform
    r"""A platform a screening can cover. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""

    handle: str

    url: str

    access: Access
    r"""public profiles were read; a private or locked one exists but could not be read."""

    match: ScreeningMatch
    r"""How a profile was matched to the attendee: the state its evidence earns, and the evidence."""

    collector: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""

    items_read: int

    collected_at: str

    display_name: Optional[str] = None

    bio: Optional[str] = None

    avatar_url: Optional[str] = None

    followers: Optional[int] = None

    account_created_at: Optional[str] = None

    period_from: Optional[str] = None
    r"""The oldest item read."""

    period_to: Optional[str] = None
    r"""The newest item read."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "display_name",
                "bio",
                "avatar_url",
                "followers",
                "account_created_at",
                "period_from",
                "period_to",
            ]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
