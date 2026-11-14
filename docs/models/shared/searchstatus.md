# SearchStatus

A password or hash search is counting, then counted: rows says how many breach rows hold the value, and nothing runs until a person runs it (POST .../searches/{search_id}/run). Any other search is queued, then running. completed: every source it asked answered. partial: some did not. failed: none answered or none could be asked, which says nothing about whether the value is held anywhere.

## Example Usage

```python
from noresponse.models.shared import SearchStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SearchStatus = "counting"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"counting"`
- `"counted"`
- `"queued"`
- `"running"`
- `"completed"`
- `"partial"`
- `"failed"`
