from __future__ import annotations
from .policyevaluation import PolicyEvaluation, PolicyEvaluationTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PolicyEvaluationListTypedDict(TypedDict):
    r"""Retained jobs, newest first. Follow next_before for another page."""

    items: List[PolicyEvaluationTypedDict]
    next_before: NotRequired[str]


class PolicyEvaluationList(BaseModel):
    r"""Retained jobs, newest first. Follow next_before for another page."""

    items: List[PolicyEvaluation]

    next_before: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_before"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
