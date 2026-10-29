from __future__ import annotations
from .filter_ import Filter, FilterTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ReviewViewRequestTypedDict(TypedDict):
    name: str
    shared: bool
    filter_: FilterTypedDict
    expected_version: NotRequired[int]


class ReviewViewRequest(BaseModel):
    name: str

    shared: bool

    filter_: Annotated[Filter, pydantic.Field(alias="filter")]

    expected_version: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["expected_version"])
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
    ReviewViewRequest.model_rebuild()
except NameError:
    pass
