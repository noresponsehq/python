from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Attribute = Union[
    Literal[
        "birth_date",
        "gender",
        "nationality",
        "name_gender",
    ],
    UnrecognizedStr,
]
r"""name_gender is the records' gender against the submitted first name's usual one."""
