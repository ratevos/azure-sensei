# conditionalAccessExternalTenants resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessexternaltenants?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

An abstract type that represents external tenants in a policy scope.

Base type of [conditionalAccessAllExternalTenants](../resources/conditionalaccessallexternaltenants.md) and [conditionalAccessEnumeratedExternalTenants](conditionalaccessenumeratedexternaltenants.md).

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
| membershipKind |conditionalAccessExternalTenantsMembershipKind | The membership kind. The possible values are: `all`, `enumerated`, `unknownFutureValue`. The `enumerated` member references an [conditionalAccessEnumeratedExternalTenants](conditionalaccessenumeratedexternaltenants.md) object.|

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.conditionalAccessExternalTenants",
  "membershipKind": "String"
}
```
