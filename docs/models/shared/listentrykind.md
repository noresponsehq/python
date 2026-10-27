# ListEntryKind

email matches one address, whatever the case of its local part. email_domain matches every address of the registrable domain and of its subdomains.

## Example Usage

```python
from noresponse.models.shared import ListEntryKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ListEntryKind = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"email_domain"`
