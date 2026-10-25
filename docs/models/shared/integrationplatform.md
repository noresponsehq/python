# IntegrationPlatform

The authentication provider that calls the endpoint.

## Example Usage

```python
from noresponse.models.shared import IntegrationPlatform

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IntegrationPlatform = "workos"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"workos"`
- `"auth0"`
- `"supabase"`
