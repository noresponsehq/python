# Match

exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists.

## Example Usage

```python
from noresponse.models.shared import Match

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Match = "exact"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"exact"`
- `"canonical"`
- `"mailbox"`
