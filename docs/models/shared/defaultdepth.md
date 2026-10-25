# DefaultDepth

The depth a request for this flow that names none is served at. Defaults: full for account_creation and purchase, quick for login.

## Example Usage

```python
from noresponse.models.shared import DefaultDepth

# Open enum: unrecognized values are captured as UnrecognizedStr
value: DefaultDepth = "quick"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"quick"`
- `"full"`
