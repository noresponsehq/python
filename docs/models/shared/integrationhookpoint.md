# IntegrationHookPoint

pre_registration runs before the user exists; post_login runs after a successful sign-in.

## Example Usage

```python
from noresponse.models.shared import IntegrationHookPoint

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IntegrationHookPoint = "pre_registration"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"pre_registration"`
- `"post_login"`
