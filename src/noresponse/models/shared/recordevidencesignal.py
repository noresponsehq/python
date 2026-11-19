from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RecordEvidenceSignal = Union[
    Literal[
        "found_by",
        "agrees",
        "clashes",
    ],
    UnrecognizedStr,
]
r"""found_by: what found the record, which sets where its likelihood starts. agrees: a value the record shares with what the investigator gave or with a joined record. clashes: a birth date, full name, gender or country that differs from theirs."""
