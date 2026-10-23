# conditionalAccessAuthenticationFlows resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessauthenticationflows?view=graph-rest-1.0  
> Microsoft doc last updated: 11/08/2024


Namespace: microsoft.graph

Represents the authentication flows in scope for the policy.

## Properties

|Property|Type|Description|
|:---|:---|:---|
|transferMethods|conditionalAccessTransferMethods|Represents the transfer methods in scope for the policy. The possible values are: `none`, `deviceCodeFlow`, `authenticationTransfer`, `unknownFutureValue`.|

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

``` json
{
  "transferMethods": "String",
}
```
