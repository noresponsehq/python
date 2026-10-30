# AccountType

personal, or business: an account a company or school manages.

## Example Usage

```python
from noresponse.models.shared import AccountType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AccountType = "personal"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"personal"`
- `"business"`
