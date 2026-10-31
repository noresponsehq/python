from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Country = Union[
    Literal[
        "consistent",
        "mismatch",
        "unknown",
    ],
    UnrecognizedStr,
]
r"""IP country, phone country, breach countries and policy_context.region together. When the breach records give a country, the timezone and locale countries count too. The IP country of a proxy or hosting network does not count."""
