from __future__ import annotations
from .access import Access
from .postsstopped import PostsStopped
from .record import Record, RecordTypedDict
from .screeningmatch import ScreeningMatch, ScreeningMatchTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningProfileTypedDict(TypedDict):
    r"""An account the screening matched to the person, how it was matched, and how much of it was read."""

    id: str
    platform: str
    r"""A platform a screening can cover, such as instagram, x, bluesky, youtube, tiktok or github. The screening registry owns the set: a request that names a platform it does not cover answers 422. A new platform adds an id without changing this contract, so read a platform you do not know in a response as one you have not seen before, not as an error. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
    handle: str
    url: str
    access: Access
    r"""public profiles were read; a private or locked one exists but could not be read."""
    match: ScreeningMatchTypedDict
    r"""How a profile was matched to the person: the state its evidence earns, and the evidence."""
    collector: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""
    items_read: int
    collected_at: str
    display_name: NotRequired[str]
    bio: NotRequired[str]
    avatar_url: NotRequired[str]
    followers: NotRequired[int]
    account_created_at: NotRequired[str]
    posts_stopped: NotRequired[PostsStopped]
    r"""Why fewer posts were read than the screening's depth asks for while the account holds more. platform_limit: the platform shows the screening no more of them. page_limit: the pages a screening reads ran out first. rate_limited or unavailable: a later page was held back or failed; the posts before it are kept and the person is partial. Absent when the account was read to its end or to the depth."""
    period_from: NotRequired[str]
    r"""The oldest item read."""
    period_to: NotRequired[str]
    r"""The newest item read."""
    record: NotRequired[RecordTypedDict]
    r"""One answer from one source: where it came from, what found it and every field it holds. A person's lookup records also say how likely each is the person."""


class ScreeningProfile(BaseModel):
    r"""An account the screening matched to the person, how it was matched, and how much of it was read."""

    id: str

    platform: str
    r"""A platform a screening can cover, such as instagram, x, bluesky, youtube, tiktok or github. The screening registry owns the set: a request that names a platform it does not cover answers 422. A new platform adds an id without changing this contract, so read a platform you do not know in a response as one you have not seen before, not as an error. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""

    handle: str

    url: str

    access: Access
    r"""public profiles were read; a private or locked one exists but could not be read."""

    match: ScreeningMatch
    r"""How a profile was matched to the person: the state its evidence earns, and the evidence."""

    collector: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""

    items_read: int

    collected_at: str

    display_name: Optional[str] = None

    bio: Optional[str] = None

    avatar_url: Optional[str] = None

    followers: Optional[int] = None

    account_created_at: Optional[str] = None

    posts_stopped: Optional[PostsStopped] = None
    r"""Why fewer posts were read than the screening's depth asks for while the account holds more. platform_limit: the platform shows the screening no more of them. page_limit: the pages a screening reads ran out first. rate_limited or unavailable: a later page was held back or failed; the posts before it are kept and the person is partial. Absent when the account was read to its end or to the depth."""

    period_from: Optional[str] = None
    r"""The oldest item read."""

    period_to: Optional[str] = None
    r"""The newest item read."""

    record: Optional[Record] = None
    r"""One answer from one source: where it came from, what found it and every field it holds. A person's lookup records also say how likely each is the person."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "display_name",
                "bio",
                "avatar_url",
                "followers",
                "account_created_at",
                "posts_stopped",
                "period_from",
                "period_to",
                "record",
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
