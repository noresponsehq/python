from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RecordFieldTypedDict(TypedDict):
    r"""One value a source returned."""

    field: str
    r"""The source's own name for the field. A nested value's name is dotted, and a list element's carries its index."""
    original: str
    r"""The value as the source wrote it. A count is written in decimal and a time in RFC 3339; a breach column's value is as the leak holds it."""
    kind: NotRequired[str]
    r"""What sort of value the field holds. Absent until the field's kind is known."""
    role: NotRequired[str]
    r"""Which common field it is, where many sources share it, such as handle, display_name, account_id, profile_link, picture, bio, website, linked_account (named by its network), account_status, joined, last_updated, organisation, location, followers, following or posts. Absent for a field only this source returns."""
    value: NotRequired[str]
    r"""The cleaned value. Absent when it cannot be cleaned, or until the field's kind is known."""


class RecordField(BaseModel):
    r"""One value a source returned."""

    field: str
    r"""The source's own name for the field. A nested value's name is dotted, and a list element's carries its index."""

    original: str
    r"""The value as the source wrote it. A count is written in decimal and a time in RFC 3339; a breach column's value is as the leak holds it."""

    kind: Optional[str] = None
    r"""What sort of value the field holds. Absent until the field's kind is known."""

    role: Optional[str] = None
    r"""Which common field it is, where many sources share it, such as handle, display_name, account_id, profile_link, picture, bio, website, linked_account (named by its network), account_status, joined, last_updated, organisation, location, followers, following or posts. Absent for a field only this source returns."""

    value: Optional[str] = None
    r"""The cleaned value. Absent when it cannot be cleaned, or until the field's kind is known."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["kind", "role", "value"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
