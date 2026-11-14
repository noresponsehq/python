from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PrincipalTypedDict(TypedDict):
    r"""A person the group protects."""

    name: str
    r"""The principal's name."""
    aliases: NotRequired[List[str]]
    r"""Other names the principal goes by, at most 10."""


class Principal(BaseModel):
    r"""A person the group protects."""

    name: str
    r"""The principal's name."""

    aliases: Optional[List[str]] = None
    r"""Other names the principal goes by, at most 10."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["aliases"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
