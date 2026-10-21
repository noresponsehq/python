# SignalOutcome

Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence.

## Example Usage

```python
from noresponse.models.shared import SignalOutcome

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SignalOutcome = "found"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"found"`
- `"not_found"`
- `"inconclusive"`
- `"blocked"`
- `"unavailable"`
