from __future__ import annotations
from noresponse.models.shared import operationalaggregate as shared_operationalaggregate
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class AggregateWebhooksResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_operationalaggregate.OperationalAggregateTypedDict


class AggregateWebhooksResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_operationalaggregate.OperationalAggregate
