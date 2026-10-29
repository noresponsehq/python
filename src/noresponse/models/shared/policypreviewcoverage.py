from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class PolicyPreviewCoverageTypedDict(TypedDict):
    scanned: int
    eligible: int
    missing_score: int
    unsupported: int
    truncated: bool
    complete_retained_window: bool
    historical_population_known: Literal[False]
    r"""Deleted, expired and uncaptured records cannot be reconstructed. Counts describe retained evidence and provide no causal estimate of fraud prevented."""


class PolicyPreviewCoverage(BaseModel):
    scanned: int

    eligible: int

    missing_score: int

    unsupported: int

    truncated: bool

    complete_retained_window: bool

    historical_population_known: Annotated[
        Annotated[Literal[False], AfterValidator(validate_const(False))],
        pydantic.Field(alias="historical_population_known"),
    ] = False
    r"""Deleted, expired and uncaptured records cannot be reconstructed. Counts describe retained evidence and provide no causal estimate of fraud prevented."""


try:
    PolicyPreviewCoverage.model_rebuild()
except NameError:
    pass
