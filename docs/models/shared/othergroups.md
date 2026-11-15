# OtherGroups

Where else in the environment the person appears, read live from those groups: deleting one removes it here.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `total`                                                                             | *int*                                                                               | :heavy_check_mark:                                                                  | How many other groups include this person, of which items lists the 20 most recent. |
| `items`                                                                             | List[[shared.OtherGroup](../../models/shared/othergroup.md)]                        | :heavy_check_mark:                                                                  | This person's memberships in the 20 most recent other groups, newest group first.   |