# Certainty

confirmed: a linked record or the searched identifier states it directly. likely: a strong inference. possible: a weak inference.

## Example Usage

```python
from noresponse.models.shared import Certainty

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Certainty = "confirmed"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"confirmed"`
- `"likely"`
- `"possible"`
