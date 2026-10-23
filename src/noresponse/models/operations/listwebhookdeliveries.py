from __future__ import annotations
from noresponse.models.shared import webhookdeliverylist as shared_webhookdeliverylist
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Awaitable, Callable, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListWebhookDeliveriesRequestTypedDict(TypedDict):
    endpoint_id: str
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another workspace's answers 404."""
    limit: NotRequired[int]
    r"""Attempts per page."""
    cursor: NotRequired[str]
    r"""next_cursor from the previous page, unchanged."""


class ListWebhookDeliveriesRequest(BaseModel):
    endpoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The endpoint's whe_ id. An id that is unknown, malformed or another workspace's answers 404."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Attempts per page."""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""next_cursor from the previous page, unchanged."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListWebhookDeliveriesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_webhookdeliverylist.WebhookDeliveryListTypedDict


class ListWebhookDeliveriesResponse(BaseModel):
    next: Union[
        Callable[[], Optional[ListWebhookDeliveriesResponse]],
        Callable[[], Awaitable[Optional[ListWebhookDeliveriesResponse]]],
    ]

    headers: Dict[str, List[str]]

    result: shared_webhookdeliverylist.WebhookDeliveryList
