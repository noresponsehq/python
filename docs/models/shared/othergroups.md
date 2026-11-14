# OtherGroups

Where else in the environment the person appears, read live from those groups: deleting one removes it here.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `total`                                                                         | *int*                                                                           | :heavy_check_mark:                                                              | How many people of other groups match, of which items lists the 20 most recent. |
| `items`                                                                         | List[[shared.OtherGroup](../../models/shared/othergroup.md)]                    | :heavy_check_mark:                                                              | The 20 people of the most recent other groups, newest group first.              |