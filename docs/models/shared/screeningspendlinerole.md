# ScreeningSpendLineRole

What the implementation did. analyser appears only on spend recorded before the engine stopped analysing posts.

## Example Usage

```python
from noresponse.models.shared import ScreeningSpendLineRole

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScreeningSpendLineRole = "resolver"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"resolver"`
- `"collector"`
- `"analyser"`
