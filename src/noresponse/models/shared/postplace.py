from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PostPlaceTypedDict(TypedDict):
    r"""A place a post names, as the platform shows it."""

    name: str
    id: NotRequired[str]
    r"""The platform's own id of the place."""
    address: NotRequired[str]
    city: NotRequired[str]
    latitude: NotRequired[float]
    longitude: NotRequired[float]


class PostPlace(BaseModel):
    r"""A place a post names, as the platform shows it."""

    name: str

    id: Optional[str] = None
    r"""The platform's own id of the place."""

    address: Optional[str] = None

    city: Optional[str] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["id", "address", "city", "latitude", "longitude"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
