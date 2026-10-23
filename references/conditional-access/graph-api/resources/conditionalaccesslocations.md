# conditionalAccessLocations resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesslocations?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents locations included in and excluded from the scope of a [conditional access policy](../resources/conditionalaccesspolicy.md). Locations can be [countries and regions](../resources/countrynamedlocation.md) or [IP addresses](../resources/ipnamedlocation.md).

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
| excludeLocations | String collection | Location IDs excluded from scope of policy. |
| includeLocations | String collection | Location IDs in scope of policy unless explicitly excluded, `All`, or `AllTrusted`. |

## JSON representation

The following JSON representation shows the resource type.

## Relationships

None.

```json
{
  "excludeLocations": ["String"],
  "includeLocations": ["String"]
}
```
