from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RecordSourceTypedDict(TypedDict):
    r"""Where a record came from."""

    connector: str
    r"""The id of the connector that read the record: breach for a breach row."""
    kind: str
    r"""The kind of source: platform for an account read off a live platform; for a breach row, the kind of leak its table is: site_breach, credential_list, stealer_log, scrape, hacking_forum, abuse_service or darkweb_site."""
    site: NotRequired[str]
    r"""The host a person knows the source's site by."""
    table: NotRequired[str]
    r"""The table a leaked row came from."""
    date_: NotRequired[str]
    r"""When the source's data dates from, at the precision it is known: YYYY or YYYY-MM for a breach table."""


class RecordSource(BaseModel):
    r"""Where a record came from."""

    connector: str
    r"""The id of the connector that read the record: breach for a breach row."""

    kind: str
    r"""The kind of source: platform for an account read off a live platform; for a breach row, the kind of leak its table is: site_breach, credential_list, stealer_log, scrape, hacking_forum, abuse_service or darkweb_site."""

    site: Optional[str] = None
    r"""The host a person knows the source's site by."""

    table: Optional[str] = None
    r"""The table a leaked row came from."""

    date_: Annotated[Optional[str], pydantic.Field(alias="date")] = None
    r"""When the source's data dates from, at the precision it is known: YYYY or YYYY-MM for a breach table."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["site", "table", "date"])
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
    RecordSource.model_rebuild()
except NameError:
    pass
