from __future__ import annotations
from noresponse.models.shared import keylist as shared_keylist
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ListKeysRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""


class ListKeysRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""


class ListKeysResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_keylist.KeyListTypedDict


class ListKeysResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_keylist.KeyList
