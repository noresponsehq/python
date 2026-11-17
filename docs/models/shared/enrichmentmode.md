# EnrichmentMode

off: enrichment starts no search and suggests none. suggest: enrichment starts no search by itself, and the person report lists the searches it would start in suggested_searches. automatic: after a workspace person's own investigation or a group's screening, and each time a search on that person finishes, enrichment starts searches by itself. A group takes suggest while the workspace has not set a mode.

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
