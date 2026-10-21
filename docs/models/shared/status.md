# Status

complete: final; nothing is still running. A lane that failed or missed its 10 s deadline stays listed in incomplete_sources, and confidence is lower. partial: a recommendation exists and at least one lane is still running or did not settle (see incomplete_sources). pending: nothing usable before the deadline; no recommendation yet, poll or wait for the webhook.

## Example Usage

```python
from noresponse.models.shared import Status

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Status = "complete"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"complete"`
- `"partial"`
- `"pending"`
