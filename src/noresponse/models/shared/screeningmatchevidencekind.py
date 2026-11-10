from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ScreeningMatchEvidenceKind = Union[
    Literal[
        "email",
        "phone",
        "supplied_handle",
        "source_fact",
        "name",
        "company",
        "city",
        "school",
    ],
    UnrecognizedStr,
]
r"""What matched. email, phone, supplied_handle and source_fact are hard identifiers; company, city and school are soft."""
