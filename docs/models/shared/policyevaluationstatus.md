# PolicyEvaluationStatus

## Example Usage

```python
from noresponse.models.shared import PolicyEvaluationStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PolicyEvaluationStatus = "queued"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"queued"`
- `"running"`
- `"completed"`
- `"failed"`
- `"cancelled"`
