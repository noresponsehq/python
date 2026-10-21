from __future__ import annotations
from .breachexposed import BreachExposed
from .breachkind import BreachKind
from .breachselector import BreachSelector
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class BreachTypedDict(TypedDict):
    r"""One breach table that matched, detailed view only. name is the catalogue's display name for the table's site, not the upstream provider. No member carries a record, value, password or hash."""

    name: str
    kind: BreachKind
    r"""Who is in the table: site_breach, a site's own users; credential_list, a combolist or compilation; stealer_log, malware or botnet victims; scrape; hacking_forum, a criminal hacking, cracking or carding community; abuse_service, the customers of DDoS-for-hire, account generators, dump or card shops, darknet markets, stalkerware or breach-lookup services; darkweb_site, an onion site of unknown purpose."""
    matched_on: BreachSelector
    r"""The submitted identifier a breach table matched on: email or username. Phone and name are not breach selectors."""
    domain: NotRequired[str]
    r"""The breached site's domain, lower case. Absent when the table has none (a credential list, for example)."""
    category: NotRequired[str]
    r"""The table's category from its name, lower case (social, gaming, combolist, ...)."""
    year: NotRequired[int]
    r"""A breach table's date year."""
    month: NotRequired[int]
    r"""Absent when only the year is known."""
    exposed: NotRequired[List[BreachExposed]]


class Breach(BaseModel):
    r"""One breach table that matched, detailed view only. name is the catalogue's display name for the table's site, not the upstream provider. No member carries a record, value, password or hash."""

    name: str

    kind: BreachKind
    r"""Who is in the table: site_breach, a site's own users; credential_list, a combolist or compilation; stealer_log, malware or botnet victims; scrape; hacking_forum, a criminal hacking, cracking or carding community; abuse_service, the customers of DDoS-for-hire, account generators, dump or card shops, darknet markets, stalkerware or breach-lookup services; darkweb_site, an onion site of unknown purpose."""

    matched_on: BreachSelector
    r"""The submitted identifier a breach table matched on: email or username. Phone and name are not breach selectors."""

    domain: Optional[str] = None
    r"""The breached site's domain, lower case. Absent when the table has none (a credential list, for example)."""

    category: Optional[str] = None
    r"""The table's category from its name, lower case (social, gaming, combolist, ...)."""

    year: Optional[int] = None
    r"""A breach table's date year."""

    month: Optional[int] = None
    r"""Absent when only the year is known."""

    exposed: Optional[List[BreachExposed]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["domain", "category", "year", "month", "exposed"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
