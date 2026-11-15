from __future__ import annotations
from noresponse.models.shared import (
    group as shared_group,
    grouprequest as shared_grouprequest,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateGroupRequestTypedDict(TypedDict):
    body: shared_grouprequest.GroupRequestTypedDict
    idempotency_key: NotRequired[str]
    r"""Opaque request key, 16 to 128 characters. Repeating the key and request returns the same resource in its current state while it is retained. A different request with the same key answers 409. Use a new key for a deliberate new operation. Keys are scoped to the environment and operation; person searches also scope them to the group and person."""


class CreateGroupRequest(BaseModel):
    body: Annotated[
        shared_grouprequest.GroupRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Opaque request key, 16 to 128 characters. Repeating the key and request returns the same resource in its current state while it is retained. A different request with the same key answers 409. Use a new key for a deliberate new operation. Keys are scoped to the environment and operation; person searches also scope them to the group and person."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["Idempotency-Key"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class CreateGroupResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_group.GroupTypedDict


class CreateGroupResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_group.Group
