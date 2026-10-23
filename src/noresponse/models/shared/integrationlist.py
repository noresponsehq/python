from __future__ import annotations
from .integration import Integration, IntegrationTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class IntegrationListTypedDict(TypedDict):
    r"""GET /v1/integrations: every integration of the workspace, oldest first, at most 10. No secret is ever listed."""

    items: List[IntegrationTypedDict]


class IntegrationList(BaseModel):
    r"""GET /v1/integrations: every integration of the workspace, oldest first, at most 10. No secret is ever listed."""

    items: List[Integration]
