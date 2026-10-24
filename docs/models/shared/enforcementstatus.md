# EnforcementStatus

applied when the identity provider accepted the action, failed when it refused it or could not be reached. Only applied counts as enforced.

## Example Usage

```python
from noresponse.models.shared import EnforcementStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EnforcementStatus = "applied"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"applied"`
- `"failed"`
