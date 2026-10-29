# From

## Example Usage

```python
from noresponse.models.shared import From

# Open enum: unrecognized values are captured as UnrecognizedStr
value: From = "allow"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"allow"`
- `"step_up"`
- `"review"`
- `"block"`
- `"held"`
