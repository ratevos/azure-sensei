# authenticationStrengthRoot resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/authenticationstrengthroot?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

The **authenticationStrengthRoot** resource is the entry point for the authentication strengths object model.

## Methods

None.

## Properties
|Property|Type|Description|
|:---|:---|:---|
|authenticationCombinations|[authenticationMethodModes](../resources/authenticationmethodmodes.md) collection|A collection of all valid authentication method combinations in the system.|
|id|String|A system-generated identifier.|

## Relationships
|Relationship|Type|Description|
|:---|:---|:---|
|authenticationMethodModes|[authenticationMethodModeDetail](../resources/authenticationmethodmodedetail.md) collection|Names and descriptions of all valid authentication method modes in the system.|
|policies|[authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) collection|A collection of [authentication strength policies](authenticationStrengthPolicy.md) that exist for this tenant, including both built-in and custom policies.|

## JSON representation
The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.authenticationStrengthRoot",
  "id": "String (identifier)",
  "authenticationCombinations": [
    "String"
  ]
}
```
