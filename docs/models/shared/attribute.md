# Attribute

name_gender is the records' gender against the submitted first name's usual one.

## Example Usage

```python
from noresponse.models.shared import Attribute

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Attribute = "birth_date"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"birth_date"`
- `"gender"`
- `"nationality"`
- `"name_gender"`
