# HookPoint

The provider event a provider_hook context was sent for; absent for any other transport.

## Example Usage

```python
from noresponse.models.shared import HookPoint

# Open enum: unrecognized values are captured as UnrecognizedStr
value: HookPoint = "pre_registration"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"pre_registration"`
- `"post_registration"`
- `"pre_login"`
- `"post_login"`
- `"token_issuance"`
