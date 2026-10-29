# Environment

## Example Usage

```python
from noresponse.models.shared import Environment

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Environment = "live"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"live"`
- `"test"`
- `"workspace"`
