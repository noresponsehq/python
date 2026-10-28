# ListRequestDiagnosticsRequest


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `from_`                                           | *str*                                             | :heavy_check_mark:                                | Inclusive start of a range of at most seven days. | 2026-10-21T00:00:00Z                              |
| `to`                                              | *str*                                             | :heavy_check_mark:                                | Exclusive end of the range.                       | 2026-10-22T00:00:00Z                              |
| `request_id`                                      | *Optional[str]*                                   | :heavy_minus_sign:                                | Optional filter or paging parameter.              |                                                   |
| `route`                                           | *Optional[str]*                                   | :heavy_minus_sign:                                | Optional filter or paging parameter.              |                                                   |
| `status`                                          | *Optional[int]*                                   | :heavy_minus_sign:                                | Optional filter or paging parameter.              |                                                   |
| `limit`                                           | *Optional[int]*                                   | :heavy_minus_sign:                                | Optional filter or paging parameter.              |                                                   |
| `cursor`                                          | *Optional[str]*                                   | :heavy_minus_sign:                                | Optional filter or paging parameter.              |                                                   |