# SignIn

## Example Usage

```python
from noresponse.models.shared import SignIn

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SignIn = "password"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"password"`
- `"google"`
- `"facebook"`
- `"apple"`
- `"microsoft"`
- `"sso"`
- `"other"`
