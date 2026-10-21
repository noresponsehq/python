from __future__ import annotations
from noresponse.models.shared import keyrotation as shared_keyrotation
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class RotateAPIKeyResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_keyrotation.KeyRotationTypedDict


class RotateAPIKeyResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_keyrotation.KeyRotation
