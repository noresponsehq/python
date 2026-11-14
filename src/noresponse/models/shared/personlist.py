from __future__ import annotations
from .person import Person, PersonTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PersonListTypedDict(TypedDict):
    r"""People in upload order."""

    items: List[PersonTypedDict]
    next_after: NotRequired[str]
    r"""Pass as after to read the next page."""


class PersonList(BaseModel):
    r"""People in upload order."""

    items: List[Person]

    next_after: Optional[str] = None
    r"""Pass as after to read the next page."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_after"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
