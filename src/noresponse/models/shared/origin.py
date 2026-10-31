from __future__ import annotations
from typing import Literal


Origin = Literal[
    "api",
    "lookup",
]
r"""api (the default) searches the assessments your integration sent. lookup searches the assessments your team ran by hand on the console's Lookup page. The API sets an assessment's origin from the credential that sent it. A lookup is not in any other list, count, webhook event or account."""
