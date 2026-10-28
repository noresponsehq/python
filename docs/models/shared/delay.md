# Delay

How long after the assessment's creation the change was made.

## Example Usage

```python
from noresponse.models.shared import Delay

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Delay = "under_10s"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"under_10s"`
- `"under_1m"`
- `"under_10m"`
- `"under_1h"`
- `"under_1d"`
- `"over_1d"`
