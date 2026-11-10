from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
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

    screenshot_sha256: Optional[str] = None
    r"""SHA-256 of the screenshot taken of a flagged item."""

    captured_at: Optional[str] = None
    r"""When the screenshot was taken."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["reply_to", "screenshot_sha256", "captured_at"])
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
