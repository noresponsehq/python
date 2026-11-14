# PostsStopped

Why fewer posts were read than the screening's depth asks for while the account holds more. platform_limit: the platform shows the screening no more of them. page_limit: the pages a screening reads ran out first. rate_limited or unavailable: a later page was held back or failed; the posts before it are kept and the person is partial. Absent when the account was read to its end or to the depth.

## Example Usage

```python
from noresponse.models.shared import PostsStopped

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PostsStopped = "platform_limit"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"platform_limit"`
- `"page_limit"`
- `"rate_limited"`
- `"unavailable"`
