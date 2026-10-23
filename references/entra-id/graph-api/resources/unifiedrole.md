# unifiedRole resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/unifiedrole?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024

Namespace: microsoft.graph

The directory roles that can be assigned to a Microsoft partner through a delegated admin relationship.

## Properties
|Property|Type|Description|
|:---|:---|:---|
|roleDefinitionId|String|The unified role definition ID of the directory role. Refer to [unifiedRoleDefinition](../resources/unifiedRoleDefinition.md) resource.|

## Relationships
None.

## JSON representation
The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.unifiedRole",
  "roleDefinitionId": "String"
}
```
