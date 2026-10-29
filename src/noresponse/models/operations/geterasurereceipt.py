from __future__ import annotations
from noresponse.models.shared import erasurereceipt as shared_erasurereceipt
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetErasureReceiptRequestTypedDict(TypedDict):
    erasure_id: str


class GetErasureReceiptRequest(BaseModel):
    erasure_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetErasureReceiptResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_erasurereceipt.ErasureReceiptTypedDict


class GetErasureReceiptResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_erasurereceipt.ErasureReceipt
