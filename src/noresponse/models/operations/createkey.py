from __future__ import annotations
from noresponse.models.shared import key as shared_key, keyrequest as shared_keyrequest
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CreateKeyRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    body: shared_keyrequest.KeyRequestTypedDict


class CreateKeyRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    body: Annotated[
        shared_keyrequest.KeyRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreateKeyResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_key.KeyTypedDict


class CreateKeyResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_key.Key
