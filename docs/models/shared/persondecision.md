# PersonDecision

## Example Usage

```python
from noresponse.models.shared import PersonDecision

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PersonDecision = "cleared"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"cleared"`
- `"watch"`
- `"escalated"`
