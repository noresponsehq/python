# ProfileCitationKind

record: a record in lookup.records or profiles[].record. post: an item in posts. check: an item in lookup.checks.

## Example Usage

```python
from noresponse.models.shared import ProfileCitationKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProfileCitationKind = "record"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"record"`
- `"post"`
- `"check"`
