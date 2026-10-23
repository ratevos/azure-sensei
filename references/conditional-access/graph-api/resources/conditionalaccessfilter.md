# conditionalAccessFilter resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessfilter?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents filter in the policy scope.

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
| mode | filterMode | Mode to use for the filter. Possible values are `include` or `exclude`. |
| rule | String | Rule syntax is similar to that used for membership rules for groups in Microsoft Entra ID. For details, see [rules with multiple expressions](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-dynamic-membership#rules-with-multiple-expressions) |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "mode": "String",
  "rule": "String"
}
```
