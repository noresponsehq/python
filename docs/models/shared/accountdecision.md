# AccountDecision

block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it.

## Example Usage

```python
from noresponse.models.shared import AccountDecision

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AccountDecision = "allow"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"allow"`
- `"step_up"`
- `"review"`
- `"block"`
