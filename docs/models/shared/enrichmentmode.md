# EnrichmentMode

off: enrichment starts no search. suggest: enrichment starts no search by itself. automatic: after a workspace person's own investigation, and each time a search on that person finishes, enrichment starts searches by itself.

## Example Usage

```python
from noresponse.models.shared import EnrichmentMode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EnrichmentMode = "off"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"off"`
- `"suggest"`
- `"automatic"`
