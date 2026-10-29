# Provenance

Customer-submitted input. It does not mean the customer or NoResponse verified ownership.

## Example Usage

```python
from noresponse.models.shared import Provenance

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Provenance = "submitted"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"submitted"`
