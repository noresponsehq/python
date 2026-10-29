from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Provenance = Union[Literal["submitted",], UnrecognizedStr]
r"""Customer-submitted input. It does not mean the customer or NoResponse verified ownership."""
