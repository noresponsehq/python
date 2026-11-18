from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ScreeningMatchEvidenceKind = Union[
    Literal[
        "email",
        "phone",
        "supplied_handle",
        "supplied_username",
        "source_fact",
        "name",
        "company",
        "city",
        "school",
    ],
    UnrecognizedStr,
]
r"""What matched. email, phone, supplied_handle and source_fact are hard identifiers; company, city and school are soft. supplied_handle is a handle on the person row; supplied_username is an account at the person's platform-free username, which alone makes a possible match; source_fact is an account a profile found by the person's lookups lists."""
