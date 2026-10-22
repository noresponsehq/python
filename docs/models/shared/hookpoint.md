# HookPoint

The provider event a provider_hook context was sent for. pre_registration runs before the user exists, so subject and the request's account_id may be absent there. Sent only with transport provider_hook.

## Example Usage

```python
from noresponse.models.shared import HookPoint
value: HookPoint = "pre_registration"
```


## Values

- `"pre_registration"`
- `"post_registration"`
- `"pre_login"`
- `"post_login"`
- `"token_issuance"`
