from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningMediaObservationTypedDict(TypedDict):
    r"""What an analyser saw in one image that a finding rests on."""

    media_id: str
    r"""The image, one of the finding's evidence."""
    description: str
    r"""What the analyser saw in the image that supports the finding."""
    read_text: NotRequired[str]
    r"""Words the analyser read in the image, as it read them. They come from the image's pixels, not from a post's text, so they are not a quote and were not checked against the record."""


class ScreeningMediaObservation(BaseModel):
    r"""What an analyser saw in one image that a finding rests on."""

    media_id: str
    r"""The image, one of the finding's evidence."""

    description: str
    r"""What the analyser saw in the image that supports the finding."""

    read_text: Optional[str] = None
    r"""Words the analyser read in the image, as it read them. They come from the image's pixels, not from a post's text, so they are not a quote and were not checked against the record."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["read_text"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
