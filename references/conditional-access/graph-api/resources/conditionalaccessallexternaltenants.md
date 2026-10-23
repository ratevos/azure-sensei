# conditionalAccessAllExternalTenants resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessallexternaltenants?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents all external tenants in a policy scope.

Inherits from [conditionalAccessExternalTenants](conditionalaccessexternaltenants.md).

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
| membershipKind |conditionalAccessExternalTenantsMembershipKind | The membership kind. The possible values are: `all`, `enumerated`, `unknownFutureValue`. The `enumerated` member references an [conditionalAccessEnumeratedExternalTenants](conditionalaccessenumeratedexternaltenants.md) object. Inherited from [conditionalAccessExternalTenants](conditionalaccessexternaltenants.md). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.conditionalAccessAllExternalTenants",
  "membershipKind": "String"
}
```
