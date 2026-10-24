# EnforcementProvider

The identity provider the action ran in; custom for the workspace's own user store.

## Example Usage

```python
from noresponse.models.shared import EnforcementProvider

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EnforcementProvider = "clerk"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"clerk"`
- `"workos"`
- `"auth0"`
- `"custom"`
