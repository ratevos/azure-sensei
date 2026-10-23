# conditionalAccessDevices resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessdevices?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents devices in the scope of a [conditionalAccessTemplate](../resources/conditionalaccesstemplate.md) object. This resource is configured in the **conditionalAccessTemplate** resource > **details** property > **conditions** property > **devices** property.

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
| deviceFilter | [conditionalAccessFilter](conditionalaccessfilter.md) | Filter that defines the dynamic-device-syntax rule to include/exclude devices. A filter can use device properties (such as extension attributes) to include/exclude them. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "deviceFilter": {"@odata.type": "microsoft.graph.conditionalAccessFilter"}
}
```
