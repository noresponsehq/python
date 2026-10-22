from __future__ import annotations
from noresponse.models.shared import integrationlist as shared_integrationlist
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class ListIntegrationsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_integrationlist.IntegrationListTypedDict


class ListIntegrationsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_integrationlist.IntegrationList
