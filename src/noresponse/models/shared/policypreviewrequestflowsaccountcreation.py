from __future__ import annotations
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


class PolicyPreviewRequestFlowsAccountCreationTypedDict(TypedDict):
    step_up: NotRequired[int]
    review: NotRequired[int]
    block: NotRequired[Nullable[int]]


class PolicyPreviewRequestFlowsAccountCreation(BaseModel):
    step_up: Optional[int] = None

    review: Optional[int] = None

    block: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["step_up", "review", "block"])
        nullable_fields = set(["block"])
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
