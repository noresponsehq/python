from __future__ import annotations
from .postplace import PostPlace, PostPlaceTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Any, Dict, List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ScreeningPostTypedDict(TypedDict):
    r"""One post a collector read, with its permalink and time."""

    id: str
    text: str
    profile_id: str
    permalink: str
    posted_at: str
    kind: Literal["post"]
    reply_to: NotRequired[str]
    repost_of: NotRequired[str]
    r"""The permalink of the post this one reposts. text then holds that post's author's words, not the person's."""
    quote_of: NotRequired[str]
    r"""The permalink of the post this one quotes. text holds the person's own words alone."""
    place: NotRequired[PostPlaceTypedDict]
    r"""A place a post names, as the platform shows it."""
    tagged: NotRequired[List[str]]
    r"""The handles of the accounts the post tags, on its own platform."""
    likes: NotRequired[int]
    r"""How many likes the platform shows for the post."""
    comments: NotRequired[int]
    r"""How many comments the platform shows for the post."""
    views: NotRequired[int]
    r"""How many views or plays the platform shows for the post."""
    shares: NotRequired[int]
    r"""How many times the platform shows the post was shared or reposted."""
    language: NotRequired[str]
    r"""The language the platform says the post is in, as the platform codes it, such as en or pt-BR."""
    edited: NotRequired[bool]
    r"""true when the platform marks the post as edited after it went up. Absent when it does not mark it."""
    sponsored: NotRequired[bool]
    r"""true when the platform marks the post as a paid partnership or an ad. Absent when it does not mark it."""
    ai_generated: NotRequired[bool]
    r"""true when the platform labels the post as made or changed with AI. Absent when it does not label it."""
    posted_with: NotRequired[str]
    r"""The app or device the platform says the post was made with."""
    stated: NotRequired[Dict[str, Any]]
    r"""Everything else the platform sent about the post, under the platform's own names and as it typed them: counts, ids of linked posts and accounts, links, media details, labels and notices. The fields above are not repeated here. Nothing that describes the account the screening read with, such as whether it liked or saved the post, is ever here."""
    screenshot_sha256: NotRequired[str]
    r"""SHA-256 of the screenshot taken of a flagged item."""
    captured_at: NotRequired[str]
    r"""When the screenshot was taken."""


class ScreeningPost(BaseModel):
    r"""One post a collector read, with its permalink and time."""

    id: str

    text: str

    profile_id: str

    permalink: str

    posted_at: str

    kind: Annotated[
        Annotated[Literal["post"], AfterValidator(validate_const("post"))],
        pydantic.Field(alias="kind"),
    ] = "post"

    reply_to: Optional[str] = None

    repost_of: Optional[str] = None
    r"""The permalink of the post this one reposts. text then holds that post's author's words, not the person's."""

    quote_of: Optional[str] = None
    r"""The permalink of the post this one quotes. text holds the person's own words alone."""

    place: Optional[PostPlace] = None
    r"""A place a post names, as the platform shows it."""

    tagged: Optional[List[str]] = None
    r"""The handles of the accounts the post tags, on its own platform."""

    likes: Optional[int] = None
    r"""How many likes the platform shows for the post."""

    comments: Optional[int] = None
    r"""How many comments the platform shows for the post."""

    views: Optional[int] = None
    r"""How many views or plays the platform shows for the post."""

    shares: Optional[int] = None
    r"""How many times the platform shows the post was shared or reposted."""

    language: Optional[str] = None
    r"""The language the platform says the post is in, as the platform codes it, such as en or pt-BR."""

    edited: Optional[bool] = None
    r"""true when the platform marks the post as edited after it went up. Absent when it does not mark it."""

    sponsored: Optional[bool] = None
    r"""true when the platform marks the post as a paid partnership or an ad. Absent when it does not mark it."""

    ai_generated: Optional[bool] = None
    r"""true when the platform labels the post as made or changed with AI. Absent when it does not label it."""

    posted_with: Optional[str] = None
    r"""The app or device the platform says the post was made with."""

    stated: Optional[Dict[str, Any]] = None
    r"""Everything else the platform sent about the post, under the platform's own names and as it typed them: counts, ids of linked posts and accounts, links, media details, labels and notices. The fields above are not repeated here. Nothing that describes the account the screening read with, such as whether it liked or saved the post, is ever here."""

    screenshot_sha256: Optional[str] = None
    r"""SHA-256 of the screenshot taken of a flagged item."""

    captured_at: Optional[str] = None
    r"""When the screenshot was taken."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "reply_to",
                "repost_of",
                "quote_of",
                "place",
                "tagged",
                "likes",
                "comments",
                "views",
                "shares",
                "language",
                "edited",
                "sponsored",
                "ai_generated",
                "posted_with",
                "stated",
                "screenshot_sha256",
                "captured_at",
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


try:
    ScreeningPost.model_rebuild()
except NameError:
    pass
