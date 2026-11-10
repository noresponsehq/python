# Access

public profiles were read; a private or locked one exists but could not be read.

## Example Usage

```python
from noresponse.models.shared import Access

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Access = "public"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"public"`
- `"private"`
- `"locked"`
