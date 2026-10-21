# NotFoundErrorCode

Machine codes an HTTP 404 answer can carry.

## Example Usage

```python
from noresponse.models.shared import NotFoundErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: NotFoundErrorCode = "not_found"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"not_found"`
