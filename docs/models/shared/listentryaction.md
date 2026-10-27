# ListEntryAction

block decides block for the accounts the entry matches; allow decides allow. Block wins when both match.

## Example Usage

```python
from noresponse.models.shared import ListEntryAction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ListEntryAction = "block"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"block"`
- `"allow"`
