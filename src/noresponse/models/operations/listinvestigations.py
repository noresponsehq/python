from __future__ import annotations
from noresponse.models.shared import investigationslist as shared_investigationslist
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListInvestigationsRequestTypedDict(TypedDict):
    person_id: NotRequired[str]
    before: NotRequired[str]
    limit: NotRequired[int]


class ListInvestigationsRequest(BaseModel):
    person_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    before: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["person_id", "before", "limit"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListInvestigationsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_investigationslist.InvestigationsListTypedDict


class ListInvestigationsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_investigationslist.InvestigationsList
