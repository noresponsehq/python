# Failure

Why the attempt failed: the URL is no longer valid, the host did not resolve, it resolved to an address that is not public, no answer within 5 seconds, the connection failed, a 3xx (redirects are not followed) or another non-2xx status. Absent for a delivered attempt.

## Example Usage

```python
from noresponse.models.shared import Failure

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Failure = "invalid_url"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invalid_url"`
- `"resolve_failed"`
- `"address_refused"`
- `"timeout"`
- `"connection_failed"`
- `"redirect"`
- `"non_2xx"`
