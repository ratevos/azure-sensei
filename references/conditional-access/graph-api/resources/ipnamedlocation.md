# ipNamedLocation resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/ipnamedlocation?view=graph-rest-1.0  
> Microsoft doc last updated: 05/23/2024


Namespace: microsoft.graph

Represents a Microsoft Entra ID named location defined by IP ranges. Named locations are custom rules that define network locations that can then be used in a Conditional Access policy.

Inherits from [namedLocation](../resources/namedLocation.md)

## Methods

| Method       | Return Type | Description |
|:-------------|:------------|:------------|
| [List](../api/conditionalaccessroot-list-namedlocations.md) | [ipNamedLocation](ipNamedLocation.md) collection | Get all the **ipNamedLocation** objects in the organization. |
| [Create](../api/conditionalaccessroot-post-namedlocations.md) | [ipNamedLocation](ipNamedLocation.md) | Create a new **ipNamedLocation** object. |
| [Get](../api/ipnamedlocation-get.md) | [ipNamedLocation](ipnamedlocation.md) | Read the properties and relationships of an **ipNamedLocation** object. |
| [Update](../api/ipnamedlocation-update.md) | [ipNamedLocation](ipnamedlocation.md) | Update an **ipNamedLocation** object. |
| [Delete](../api/ipnamedlocation-delete.md) | None | Delete an **ipNamedLocation** object. |

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|createdDateTime|DateTimeOffset|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. Inherited from [namedLocation](../resources/namedLocation.md).|
|displayName|String|Human-readable name of the location. Required.|
|id|String|Identifier of a namedLocation object. Read-only. Inherited from [namedLocation](../resources/namedLocation.md).|
|ipRanges|[ipRange](iprange.md) collection|List of IP address ranges in IPv4 CIDR format (for example, 1.2.3.4/32) or any allowable IPv6 format from IETF RFC5969. Required.|
|isTrusted|Boolean|`true` if this location is explicitly trusted. Optional. Default value is `false`.|
|modifiedDateTime|DateTimeOffset|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. Inherited from [namedLocation](../resources/namedLocation.md).|

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "createdDateTime": "String (timestamp)",
  "displayName": "String",
  "id": "String (identifier)",
  "ipRanges": [{"@odata.type": "microsoft.graph.ipRange"}],
  "isTrusted": true,
  "modifiedDateTime": "String (timestamp)"
}
```

## Related content

+ [What is Conditional Access?](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
+ [Using the location condition in a Conditional Access policy](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/location-condition)
