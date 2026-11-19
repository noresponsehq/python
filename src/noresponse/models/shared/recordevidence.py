from __future__ import annotations
from .recordevidencesignal import RecordEvidenceSignal
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RecordEvidenceTypedDict(TypedDict):
    r"""One item of evidence behind a record's likelihood."""

    signal: RecordEvidenceSignal
    r"""found_by: what found the record, which sets where its likelihood starts. agrees: a value the record shares with what the investigator gave or with a joined record. clashes: a birth date, full name, gender or country that differs from theirs."""
    bits: float
    r"""The item's weight in bits, to two places: log2 of how much likelier the evidence is for the same person than for a stranger. Positive raises the likelihood and negative lowers it."""
    kind: NotRequired[str]
    r"""For found_by, what the search looked up (email, phone, username, handle, name). Otherwise the kind of value compared, such as email, username, person_name, born, city or crypto_address."""
    field: NotRequired[str]
    r"""The record's own field that agreed or clashed, or for found_by the field the search matched."""
    with_: NotRequired[str]
    r"""given for what the investigator gave, or the id of the person's record it agreed or clashed with, or for found_by the record whose value the search looked up."""
    with_field: NotRequired[str]
    r"""The field on the other side: the field of the given identity or of the record named by with."""


class RecordEvidence(BaseModel):
    r"""One item of evidence behind a record's likelihood."""

    signal: RecordEvidenceSignal
    r"""found_by: what found the record, which sets where its likelihood starts. agrees: a value the record shares with what the investigator gave or with a joined record. clashes: a birth date, full name, gender or country that differs from theirs."""

    bits: float
    r"""The item's weight in bits, to two places: log2 of how much likelier the evidence is for the same person than for a stranger. Positive raises the likelihood and negative lowers it."""

    kind: Optional[str] = None
    r"""For found_by, what the search looked up (email, phone, username, handle, name). Otherwise the kind of value compared, such as email, username, person_name, born, city or crypto_address."""

    field: Optional[str] = None
    r"""The record's own field that agreed or clashed, or for found_by the field the search matched."""

    with_: Annotated[Optional[str], pydantic.Field(alias="with")] = None
    r"""given for what the investigator gave, or the id of the person's record it agreed or clashed with, or for found_by the record whose value the search looked up."""

    with_field: Optional[str] = None
    r"""The field on the other side: the field of the given identity or of the record named by with."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["kind", "field", "with", "with_field"])
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
    RecordEvidence.model_rebuild()
except NameError:
    pass
