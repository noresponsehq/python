# MatchState

How sure the latest screening is that it found the attendee's accounts. unscreened until a screening reaches the attendee.

## Example Usage

```python
from noresponse.models.shared import MatchState

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MatchState = "unscreened"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"unscreened"`
- `"confirmed"`
- `"probable"`
- `"possible"`
- `"none_found"`
- `"inaccessible"`
