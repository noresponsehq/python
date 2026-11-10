# HandlePlatform

A platform a screening can cover. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network.

## Example Usage

```python
from noresponse.models.shared import HandlePlatform

# Open enum: unrecognized values are captured as UnrecognizedStr
value: HandlePlatform = "instagram"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"instagram"`
- `"x"`
- `"bluesky"`
- `"youtube"`
- `"tiktok"`
- `"facebook"`
- `"threads"`
- `"reddit"`
- `"telegram"`
- `"linkedin"`
- `"synthetic"`
