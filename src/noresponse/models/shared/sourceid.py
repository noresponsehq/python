from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


SourceID = Union[
    Literal[
        "github",
        "phone",
        "breach",
        "rdap",
        "mx",
        "ipintel",
    ],
    UnrecognizedStr,
]
r"""A NoResponse source: github (GitHub accounts), phone (the phone lookup), breach (breach exposure), rdap (the email domain's registration), mx (the email domain's mail servers) or ipintel (IP intelligence)."""
