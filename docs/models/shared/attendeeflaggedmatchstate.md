# AttendeeFlaggedMatchState

How sure the screening is that the accounts it read are the attendee's. A finding on a possible match is at most moderate, on a probable match at most high.

## Example Usage

```python
from noresponse.models.shared import AttendeeFlaggedMatchState
value: AttendeeFlaggedMatchState = "confirmed"
```


## Values

- `"confirmed"`
- `"probable"`
- `"possible"`
- `"none_found"`
- `"inaccessible"`
