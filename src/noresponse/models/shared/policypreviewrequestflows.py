from __future__ import annotations
from .policypreviewrequestflowsaccountcreation import (
    PolicyPreviewRequestFlowsAccountCreation,
    PolicyPreviewRequestFlowsAccountCreationTypedDict,
)
from .policypreviewrequestflowslogin import (
    PolicyPreviewRequestFlowsLogin,
    PolicyPreviewRequestFlowsLoginTypedDict,
)
from .policypreviewrequestflowspurchase import (
    PolicyPreviewRequestFlowsPurchase,
    PolicyPreviewRequestFlowsPurchaseTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PolicyPreviewRequestFlowsTypedDict(TypedDict):
    account_creation: NotRequired[PolicyPreviewRequestFlowsAccountCreationTypedDict]
    login: NotRequired[PolicyPreviewRequestFlowsLoginTypedDict]
    purchase: NotRequired[PolicyPreviewRequestFlowsPurchaseTypedDict]


class PolicyPreviewRequestFlows(BaseModel):
    account_creation: Optional[PolicyPreviewRequestFlowsAccountCreation] = None

    login: Optional[PolicyPreviewRequestFlowsLogin] = None

    purchase: Optional[PolicyPreviewRequestFlowsPurchase] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["account_creation", "login", "purchase"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
