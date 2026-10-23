# conditionalAccessRoot resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessroot?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

The **conditionalAccessRoot** resource is the entry point for the Conditional Access (CA) object model. It doesn't contain any usable properties.

For more information on Conditional Access in Microsoft Entra ID, see [What is Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)?

## Methods

None.

## Properties

None.

## Relationships

| Relationship | Type	|Description|
|:---------------|:--------|:----------|
|authenticationContextClassReferences|[authenticationContextClassReference](authenticationcontextclassreference.md) collection|Read-only. Nullable. Returns a collection of the specified authentication context class references.|
|namedLocations|[namedLocation](namedlocation.md) collection| Read-only. Nullable. Returns a collection of the specified named locations.|
|policies|[conditionalAccessPolicy](conditionalaccesspolicy.md) collection| Read-only. Nullable. Returns a collection of the specified Conditional Access (CA) policies.|
|templates|[conditionalAccessTemplate](../resources/conditionalaccesstemplate.md) collection| Read-only. Nullable. Returns a collection of the specified Conditional Access templates.|

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.conditionalAccessRoot"
}
```
