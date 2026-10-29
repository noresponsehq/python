from __future__ import annotations
from .priority import Priority
from .reviewupdaterequeststatus import ReviewUpdateRequestStatus
from noresponse.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ReviewUpdateRequestTypedDict(TypedDict):
    expected_version: int
    status: NotRequired[ReviewUpdateRequestStatus]
    priority: NotRequired[Priority]
    assignee: NotRequired[Nullable[str]]


class ReviewUpdateRequest(BaseModel):
    expected_version: int

    status: Optional[ReviewUpdateRequestStatus] = None

    priority: Optional[Priority] = None

    assignee: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["status", "priority", "assignee"])
        nullable_fields = set(["assignee"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
