# LineType

## Example Usage

```python
from noresponse.models.shared import LineType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: LineType = "mobile"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"mobile"`
- `"voip"`
- `"landline"`
- `"toll_free"`
- `"other"`
