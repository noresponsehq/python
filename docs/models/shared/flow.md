# Flow

The provider flow the assessment gates. Use the top-level flow instead; this member is ignored when the top-level flow is present. Absent means signup.

## Example Usage

```python
from noresponse.models.shared import Flow
value: Flow = "signup"
```


## Values

- `"signup"`
- `"login"`
- `"recovery"`
- `"profile_change"`
