from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


EnrichmentMode = Union[
    Literal[
        "off",
        "suggest",
        "automatic",
    ],
    UnrecognizedStr,
]
r"""off: enrichment starts no search. suggest: enrichment starts no search by itself. automatic: after a workspace person's own investigation, and each time a search on that person finishes, enrichment starts searches by itself."""
