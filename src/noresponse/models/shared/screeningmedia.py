from __future__ import annotations
from .mediatype import MediaType
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ScreeningMediaTypedDict(TypedDict):
    r"""One image or video a collector read, with the post that carried it."""

    id: str
    media_type: MediaType
    media_url: str
    r"""Where the platform serves the image or video."""
    profile_id: str
    permalink: str
    posted_at: str
    kind: Literal["media"]
    post_id: NotRequired[str]
    text: NotRequired[str]
    r"""The caption or alt text."""
    screenshot_sha256: NotRequired[str]
    r"""SHA-256 of the screenshot taken of a flagged item."""
    captured_at: NotRequired[str]
    r"""When the screenshot was taken."""


class ScreeningMedia(BaseModel):
    r"""One image or video a collector read, with the post that carried it."""

    id: str

    media_type: MediaType

    media_url: str
    r"""Where the platform serves the image or video."""

    profile_id: str

    permalink: str

    posted_at: str

    kind: Annotated[
        Annotated[Literal["media"], AfterValidator(validate_const("media"))],
        pydantic.Field(alias="kind"),
    ] = "media"

    post_id: Optional[str] = None

    text: Optional[str] = None
    r"""The caption or alt text."""

    screenshot_sha256: Optional[str] = None
    r"""SHA-256 of the screenshot taken of a flagged item."""

    captured_at: Optional[str] = None
    r"""When the screenshot was taken."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["post_id", "text", "screenshot_sha256", "captured_at"])
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
    ScreeningMedia.model_rebuild()
except NameError:
    pass
