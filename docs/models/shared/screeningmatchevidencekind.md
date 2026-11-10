# ScreeningMatchEvidenceKind

What matched. email, phone, supplied_handle and source_fact are hard identifiers; company, city and school are soft.

## Example Usage

```python
from noresponse.models.shared import ScreeningMatchEvidenceKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScreeningMatchEvidenceKind = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"phone"`
- `"supplied_handle"`
- `"source_fact"`
- `"name"`
- `"company"`
- `"city"`
- `"school"`
