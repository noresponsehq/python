from __future__ import annotations
from .identifierexpressionnodelevelone import (
    IdentifierExpressionNodeLevelOne,
    IdentifierExpressionNodeLevelOneTypedDict,
)
from .identifiersearch import IdentifierSearch, IdentifierSearchTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IdentifierExpressionNodeLevelTwoTypedDict(TypedDict):
    term: NotRequired[IdentifierSearchTypedDict]
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""
    and_: NotRequired[List[IdentifierExpressionNodeLevelOneTypedDict]]
    or_: NotRequired[List[IdentifierExpressionNodeLevelOneTypedDict]]


class IdentifierExpressionNodeLevelTwo(BaseModel):
    term: Optional[IdentifierSearch] = None
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""

    and_: Annotated[
        Optional[List[IdentifierExpressionNodeLevelOne]], pydantic.Field(alias="and")
    ] = None

    or_: Annotated[
        Optional[List[IdentifierExpressionNodeLevelOne]], pydantic.Field(alias="or")
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["term", "and", "or"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    IdentifierExpressionNodeLevelTwo.model_rebuild()
except NameError:
    pass
