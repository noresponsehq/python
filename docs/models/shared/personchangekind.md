# PersonChangeKind

account_added and account_removed: an account or profile appeared or disappeared. breach_added and breach_removed: a breach record appeared or disappeared. identifier_added and identifier_removed: an email, phone, username, name or account id on an account the person already held. field_changed: another field on such an account. finding_added: a new finding. posts_added: new posts, counted in count.

## Example Usage

```python
from noresponse.models.shared import PersonChangeKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PersonChangeKind = "account_added"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"account_added"`
- `"account_removed"`
- `"breach_added"`
- `"breach_removed"`
- `"identifier_added"`
- `"identifier_removed"`
- `"field_changed"`
- `"finding_added"`
- `"posts_added"`
