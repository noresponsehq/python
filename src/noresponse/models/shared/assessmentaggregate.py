from __future__ import annotations
from .aggregatebucket import AggregateBucket, AggregateBucketTypedDict
from .aggregatedimension import AggregateDimension
from .bucket import Bucket
from noresponse.types import BaseModel, UNSET_SENTINEL, UnrecognizedStr
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


AssessmentAggregateMetric = Union[
    Literal[
        "count",
        "score_histogram",
        "late_flips",
    ],
    UnrecognizedStr,
]


class AssessmentAggregateTypedDict(TypedDict):
    r"""Body of the 200 answer to POST /v1/assessments/aggregate: one entry per bucket of [from,to), empty buckets included. Counts are of first answers and stay when an assessment or account is deleted or erased; search returns only assessments still retained."""

    from_: str
    to: str
    bucket: Bucket
    r"""The period each count covers, in UTC; a week starts on Monday."""
    group_by: List[AggregateDimension]
    metrics: List[AssessmentAggregateMetric]
    groups_truncated: bool
    r"""true when more groups had counts than limit allowed."""
    buckets: List[AggregateBucketTypedDict]
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    retention_days: NotRequired[int]
    r"""The calling workspace's configured retention period in days. Default 365 (12 months), which is also the maximum: a workspace may only shorten it, to at least 1 day. Each record expires from its own created_at; see assessment expires_at."""


class AssessmentAggregate(BaseModel):
    r"""Body of the 200 answer to POST /v1/assessments/aggregate: one entry per bucket of [from,to), empty buckets included. Counts are of first answers and stay when an assessment or account is deleted or erased; search returns only assessments still retained."""

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    bucket: Bucket
    r"""The period each count covers, in UTC; a week starts on Monday."""

    group_by: List[AggregateDimension]

    metrics: List[AssessmentAggregateMetric]

    groups_truncated: bool
    r"""true when more groups had counts than limit allowed."""

    buckets: List[AggregateBucket]

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    retention_days: Optional[int] = 365
    r"""The calling workspace's configured retention period in days. Default 365 (12 months), which is also the maximum: a workspace may only shorten it, to at least 1 day. Each record expires from its own created_at; see assessment expires_at."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["retention_days"])
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
    AssessmentAggregate.model_rebuild()
except NameError:
    pass
