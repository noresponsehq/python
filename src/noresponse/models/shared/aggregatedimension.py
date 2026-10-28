from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AggregateDimension = Union[
    Literal[
        "decision",
        "flow",
        "recommendation",
        "band",
        "reason",
        "lane",
        "country",
        "asn",
        "list_match",
    ],
    UnrecognizedStr,
]
r"""decision, recommendation and band: the first answer's. flow: the assessment's. list_match: the action of the list entry that decided the account when it was first answered. reason: a reason the first answer fired, with its impact band. lane: an evidence lane the first answer listed in incomplete_sources. country and asn: the submitted IP's, from the IP data."""
