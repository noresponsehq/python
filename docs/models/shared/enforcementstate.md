# EnforcementState

The account's state in the workspace's identity provider just before the action: onboarding, provisional (created, not yet activated), active, restricted or rejected.

## Example Usage

```python
from noresponse.models.shared import EnforcementState

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EnforcementState = "onboarding"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"onboarding"`
- `"provisional"`
- `"active"`
- `"restricted"`
- `"rejected"`
