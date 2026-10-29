# PolicyHistory

Immutable settings snapshots, newest first. history_complete is false when earlier versions predate capture. A restored version is published with a fresh version number. History is removed with the tenant.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `items`                                                                    | List[[shared.PolicyHistoryItem](../../models/shared/policyhistoryitem.md)] | :heavy_check_mark:                                                         | N/A                                                                        |
| `has_more`                                                                 | *bool*                                                                     | :heavy_check_mark:                                                         | N/A                                                                        |
| `next_before_version`                                                      | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `history_complete`                                                         | *bool*                                                                     | :heavy_check_mark:                                                         | N/A                                                                        |