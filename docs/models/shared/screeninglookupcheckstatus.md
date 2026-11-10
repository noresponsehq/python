# ScreeningLookupCheckStatus

found: a source found the identifier. not_found: every source answered and none found it. partial: the sources that answered found nothing and the others did not answer. not_covered: no source answered. A lookup that failed reads partial or not_covered, not not_found.

## Example Usage

```python
from noresponse.models.shared import ScreeningLookupCheckStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScreeningLookupCheckStatus = "found"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"found"`
- `"not_found"`
- `"partial"`
- `"not_covered"`
