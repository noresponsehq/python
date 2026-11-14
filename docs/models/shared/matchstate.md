# MatchState

How sure the latest screening is that it found the person's accounts. unscreened until a screening reaches the person, and after one that had no profile to check (no_profile_to_check).

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
