# OwnerType

The credential namespace of the creator. An external user ID equal to an API-key label does not grant ownership of that key's private view.

## Example Usage

```python
from noresponse.models.shared import OwnerType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: OwnerType = "user"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"user"`
- `"api_key"`
