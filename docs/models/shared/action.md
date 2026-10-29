# Action

## Example Usage

```python
from noresponse.models.shared import Action

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Action = "allow"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"allow"`
- `"block"`
