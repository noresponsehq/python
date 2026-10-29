from __future__ import annotations
from .aggregategroup import AggregateGroup, AggregateGroupTypedDict
from .aggregatelateflip import AggregateLateFlip, AggregateLateFlipTypedDict
from .aggregatescorecount import AggregateScoreCount, AggregateScoreCountTypedDict
from .aggregatescoreoutcome import AggregateScoreOutcome, AggregateScoreOutcomeTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AggregateBucketTypedDict(TypedDict):
    start: str
    r"""The bucket's first instant, in UTC. A day or week bucket in a time zone starts at local midnight there, so in Asia/Tokyo a day starts at 15:00Z the day before."""
    count: NotRequired[int]
    r"""Assessments first answered whose creation falls in the bucket. With metric count."""
    groups: NotRequired[List[AggregateGroupTypedDict]]
    r"""With metric count and group_by: the bucket's counts of the groups answered, largest group first."""
    score_histogram: NotRequired[List[AggregateScoreCountTypedDict]]
    score_outcomes: NotRequired[List[AggregateScoreOutcomeTypedDict]]
    r"""With metric score_outcomes: the score_histogram's first answers whose assessment has a reported outcome, by its latest. A bin's count less its score_outcomes is the first answers with none reported."""
    late_flips: NotRequired[List[AggregateLateFlipTypedDict]]


class AggregateBucket(BaseModel):
    start: str
    r"""The bucket's first instant, in UTC. A day or week bucket in a time zone starts at local midnight there, so in Asia/Tokyo a day starts at 15:00Z the day before."""

    count: Optional[int] = None
    r"""Assessments first answered whose creation falls in the bucket. With metric count."""

    groups: Optional[List[AggregateGroup]] = None
    r"""With metric count and group_by: the bucket's counts of the groups answered, largest group first."""

    score_histogram: Optional[List[AggregateScoreCount]] = None

    score_outcomes: Optional[List[AggregateScoreOutcome]] = None
    r"""With metric score_outcomes: the score_histogram's first answers whose assessment has a reported outcome, by its latest. A bin's count less its score_outcomes is the first answers with none reported."""

    late_flips: Optional[List[AggregateLateFlip]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["count", "groups", "score_histogram", "score_outcomes", "late_flips"]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
