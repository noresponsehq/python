# WrittenProfileStatus

queued: the profile is being written. written: summary, statements and leads hold it. failed: it could not be written; error_code says why and no content is returned.

## Example Usage

```python
from noresponse.models.shared import WrittenProfileStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WrittenProfileStatus = "queued"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"queued"`
- `"written"`
- `"failed"`
