# AttendeeDecision

## Example Usage

```python
from noresponse.models.shared import AttendeeDecision

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AttendeeDecision = "cleared"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"cleared"`
- `"watch"`
- `"escalated"`
