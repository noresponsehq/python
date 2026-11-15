from __future__ import annotations
from .recorddistinctive import RecordDistinctive, RecordDistinctiveTypedDict
from .recordkind import RecordKind
from .recordrole import RecordRole
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
    kind: NotRequired[RecordKind]
    r"""What sort of value a field holds, which decides how it is cleaned, compared and searched again. It comes from the value itself where its shape is certain (an email, an IP, a URL, an international phone number), else from the answer stored for the source's column, else text. A value of any kind is returned. Each kind's description says what it holds and the form value takes."""
    role: NotRequired[RecordRole]
    r"""Which common field a value is, where many sources share it: a join date and a birth date are both dates, with the roles joined and born. A platform account's field and a breach row's column with the same meaning carry the same kind and role. A linked_account field is named by its network. Absent for a field only its source returns. Each role's description names the kinds its values have."""
    value: NotRequired[str]
    r"""The value cleaned to its kind's one form: an email in lower case, a phone number in international form when its country is known, a date in ISO form, a country as its two-letter code, a flag as true or false. Absent when the value cannot be cleaned as its kind, or when the source masked it or cut it short, with a run of asterisks or bullets or a trailing ellipsis, in a kind that links people or is searched again; original still holds it."""
    detail: NotRequired[str]
    r"""What the value shows of itself beyond its kind: the likely algorithm of a hash, the likely coin of a crypto address or the currency of an amount."""
    distinctive: NotRequired[RecordDistinctiveTypedDict]
    r"""How distinctive a searchable value is: an email, phone, username, password, hash, person name or IP. Absent for other values, and when its rating could not be worked out, such as when a count failed."""


class RecordField(BaseModel):
    r"""One value a source returned."""

    field: str
    r"""The source's own name for the field. A nested value's name is dotted, and a list element's carries its index."""

    original: str
    r"""The value as the source wrote it. A count is written in decimal and a time in RFC 3339; a breach column's value is as the leak holds it."""

    kind: Optional[RecordKind] = None
    r"""What sort of value a field holds, which decides how it is cleaned, compared and searched again. It comes from the value itself where its shape is certain (an email, an IP, a URL, an international phone number), else from the answer stored for the source's column, else text. A value of any kind is returned. Each kind's description says what it holds and the form value takes."""

    role: Optional[RecordRole] = None
    r"""Which common field a value is, where many sources share it: a join date and a birth date are both dates, with the roles joined and born. A platform account's field and a breach row's column with the same meaning carry the same kind and role. A linked_account field is named by its network. Absent for a field only its source returns. Each role's description names the kinds its values have."""

    value: Optional[str] = None
    r"""The value cleaned to its kind's one form: an email in lower case, a phone number in international form when its country is known, a date in ISO form, a country as its two-letter code, a flag as true or false. Absent when the value cannot be cleaned as its kind, or when the source masked it or cut it short, with a run of asterisks or bullets or a trailing ellipsis, in a kind that links people or is searched again; original still holds it."""

    detail: Optional[str] = None
    r"""What the value shows of itself beyond its kind: the likely algorithm of a hash, the likely coin of a crypto address or the currency of an amount."""

    distinctive: Optional[RecordDistinctive] = None
    r"""How distinctive a searchable value is: an email, phone, username, password, hash, person name or IP. Absent for other values, and when its rating could not be worked out, such as when a count failed."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["kind", "role", "value", "detail", "distinctive"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
