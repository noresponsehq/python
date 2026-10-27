from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ListEntryKind = Union[
    Literal[
        "email",
        "email_domain",
    ],
    UnrecognizedStr,
]
r"""email matches one address, whatever the case of its local part. email_domain matches every address of the registrable domain and of its subdomains."""
