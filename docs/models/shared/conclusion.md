# Conclusion

## Example Usage

```python
from noresponse.models.shared import Conclusion

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Conclusion = "benign"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"benign"`
- `"abuse"`
- `"inconclusive"`
