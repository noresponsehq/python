from __future__ import annotations
from .action import Action
from .listimpactkind import ListImpactKind
from .listimpacttransition import ListImpactTransition, ListImpactTransitionTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListImpactTypedDict(TypedDict):
    r"""List override changes among the newest 5000 matching accounts. These counts describe override inputs. Customer enforcement and eventual outcomes remain separate. The response reports whether the matching population was truncated."""

    kind: ListImpactKind
    value: str
    action: Action
    matched_accounts: int
    changed_overrides: int
    truncated: bool
    transitions: List[ListImpactTransitionTypedDict]
    scope: Literal["current_list_override_inputs"]
    remove: NotRequired[str]
    historical_population_known: Literal[False]


class ListImpact(BaseModel):
    r"""List override changes among the newest 5000 matching accounts. These counts describe override inputs. Customer enforcement and eventual outcomes remain separate. The response reports whether the matching population was truncated."""

    kind: ListImpactKind

    value: str

    action: Action

    matched_accounts: int

    changed_overrides: int

    truncated: bool

    transitions: List[ListImpactTransition]

    scope: Annotated[
        Annotated[
            Literal["current_list_override_inputs"],
            AfterValidator(validate_const("current_list_override_inputs")),
        ],
        pydantic.Field(alias="scope"),
    ] = "current_list_override_inputs"

    remove: Optional[str] = None

    historical_population_known: Annotated[
        Annotated[Literal[False], AfterValidator(validate_const(False))],
        pydantic.Field(alias="historical_population_known"),
    ] = False

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["remove"])
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
    ListImpact.model_rebuild()
except NameError:
    pass
