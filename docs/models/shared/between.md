# Between

## Example Usage

```python
from noresponse.models.shared import Between

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Between = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"phone"`
