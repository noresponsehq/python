from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Namespace = Union[Literal["customer",], UnrecognizedStr]
r"""Required for username: the username submitted by this customer in this workspace/environment. It does not name or join a source platform. Omit for email and phone."""
