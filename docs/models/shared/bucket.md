# Bucket

The period each count covers: an hour, or a day or a week (from Monday) in time_zone. Hour buckets are whole UTC hours in any time zone.

## Example Usage

```python
from noresponse.models.shared import Bucket

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Bucket = "hour"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"hour"`
- `"day"`
- `"week"`
