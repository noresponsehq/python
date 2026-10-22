# Transport

Where the context was derived: backend (also when the request named no transport), browser, or provider_hook for a hosted provider hook.

## Example Usage

```python
from noresponse.models.shared import Transport

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Transport = "backend"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"backend"`
- `"browser"`
- `"provider_hook"`
