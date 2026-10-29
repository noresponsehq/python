# KeyScope

## Example Usage

```python
from noresponse.models.shared import KeyScope

# Open enum: unrecognized values are captured as UnrecognizedStr
value: KeyScope = "assess"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"assess"`
- `"history"`
- `"delete"`
- `"webhooks"`
- `"detailed"`
- `"integrations"`
- `"management"`
- `"audit"`
- `"usage"`
- `"investigate"`
- `"evidence"`
- `"exports"`
- `"audit_manage"`
- `"settings"`
- `"policy_publish"`
- `"members"`
- `"members_manage"`
