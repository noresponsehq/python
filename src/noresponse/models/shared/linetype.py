from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


LineType = Union[
    Literal[
        "mobile",
        "voip",
        "landline",
        "toll_free",
        "other",
    ],
    UnrecognizedStr,
]
