# SchedulePeriod

How often the person is investigated again: daily, weekly or monthly, counted from when the schedule was set; off runs no scheduled investigation.

## Example Usage

```python
from noresponse.models.shared import SchedulePeriod

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SchedulePeriod = "daily"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"daily"`
- `"weekly"`
- `"monthly"`
- `"off"`
