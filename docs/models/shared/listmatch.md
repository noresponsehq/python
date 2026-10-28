# ListMatch

The action of the list entry that decided the account.

## Example Usage

```python
from noresponse.models.shared import ListMatch

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ListMatch = "block"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"block"`
- `"allow"`
