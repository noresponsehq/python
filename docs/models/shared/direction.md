# Direction

## Example Usage

```python
from noresponse.models.shared import Direction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Direction = "raises"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"raises"`
- `"lowers"`
- `"neutral"`
