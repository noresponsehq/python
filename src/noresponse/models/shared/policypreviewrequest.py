from __future__ import annotations
from .policypreviewrequestflows import (
    PolicyPreviewRequestFlows,
    PolicyPreviewRequestFlowsTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PolicyPreviewRequestTypedDict(TypedDict):
    r"""Side-effect-free threshold preview for at most 31 days. Retained first answers are evaluated at their exact frozen scores using the production threshold and hold rules. Changes to admission, source selection, depth or retention are not simulated."""

    expected_policy_version: int
    from_: str
    to: str
    flows: PolicyPreviewRequestFlowsTypedDict
    limit: NotRequired[int]


class PolicyPreviewRequest(BaseModel):
    r"""Side-effect-free threshold preview for at most 31 days. Retained first answers are evaluated at their exact frozen scores using the production threshold and hold rules. Changes to admission, source selection, depth or retention are not simulated."""

    expected_policy_version: int

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    flows: PolicyPreviewRequestFlows

    limit: Optional[int] = 1000

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit"])
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
    PolicyPreviewRequest.model_rebuild()
except NameError:
    pass
