# PolicyRestoreRequest

Publish a captured configuration as a new version. Version checks and publication are atomic. Longer retention does not revive expired records, and restored policy does not undo customer enforcement.


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `version`                                           | *int*                                               | :heavy_check_mark:                                  | N/A                                                 |                                                     |
| `expected_policy_version`                           | *int*                                               | :heavy_check_mark:                                  | N/A                                                 |                                                     |
| `change_reason`                                     | *str*                                               | :heavy_check_mark:                                  | N/A                                                 | Adjust thresholds after reviewing retained evidence |