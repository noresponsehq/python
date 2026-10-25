from __future__ import annotations
from noresponse.models.shared import key as shared_key
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RevokeKeyRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    key_id: str
    r"""The key's id. A key of another workspace answers 404, as does a key of the other environment to an API key."""


class RevokeKeyRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    key_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The key's id. A key of another workspace answers 404, as does a key of the other environment to an API key."""


class RevokeKeyResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_key.KeyTypedDict


class RevokeKeyResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_key.Key
