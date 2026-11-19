from __future__ import annotations
from .scheduleperiod import SchedulePeriod
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PersonScheduleRequestTypedDict(TypedDict):
    r"""The schedule to set."""

    period: SchedulePeriod
    r"""How often the person is investigated again: daily, weekly or monthly, counted from when the schedule was set; off runs no scheduled investigation."""


class PersonScheduleRequest(BaseModel):
    r"""The schedule to set."""

    period: SchedulePeriod
    r"""How often the person is investigated again: daily, weekly or monthly, counted from when the schedule was set; off runs no scheduled investigation."""
