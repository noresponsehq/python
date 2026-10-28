# RequestDiagnosticPage

Authenticated attempts in a bounded interval, newest first. Keep the same filters when paging.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `items`                                                                    | List[[shared.RequestDiagnostic](../../models/shared/requestdiagnostic.md)] | :heavy_check_mark:                                                         | N/A                                                                        |                                                                            |
| `next_cursor`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        | eyJ0IjoxNzY3MjI1NjAwMDAwMDAwLCJpIjoiYXNtX2V4YW1wbGUiLCJlIjoxNzY3MjI5MjAwfQ |