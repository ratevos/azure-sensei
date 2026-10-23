# countryNamedLocation resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/countrynamedlocation?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents a Microsoft Entra ID named location defined by countries and regions. Named locations are custom rules that define network locations which can then be used in a Conditional Access policy.

Inherits from [namedLocation](../resources/namedLocation.md)

## Methods

| Method       | Return Type | Description |
|:-------------|:------------|:------------|
| [List](../api/conditionalaccessroot-list-namedlocations.md) | [countryNamedLocation](countryNamedLocation.md) collection | Get all the **countryNamedLocation** objects in the organization. |
| [Create](../api/conditionalaccessroot-post-namedlocations.md) | [countryNamedLocation](countryNamedLocation.md) | Create a new **countryNamedLocation** object. |
| [Get](../api/countrynamedlocation-get.md) | [countryNamedLocation](countrynamedlocation.md) | Read the properties and relationships of a **countryNamedLocation** object. |
| [Update](../api/countrynamedlocation-update.md) | [countryNamedLocation](countrynamedlocation.md) | Update a **countryNamedLocation** object. |
| [Delete](../api/countrynamedlocation-delete.md) | None | Delete a **countryNamedLocation** object. |

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|countriesAndRegions|String collection|List of countries and/or regions in two-letter format specified by ISO 3166-2. Required.|
|countryLookupMethod|countryLookupMethodType|Determines what method is used to decide which country the user is located in. Possible values are `clientIpAddress`(default) and `authenticatorAppGps`. Note: `authenticatorAppGps` is not yet supported in the Microsoft Cloud for US Government.|
|createdDateTime|DateTimeOffset|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. Inherited from [namedLocation](../resources/namedLocation.md).|
|displayName|String|Human-readable name of the location. Required. Inherited from [namedLocation](../resources/namedLocation.md).|
|id|String|Identifier of a namedLocation object. Read-only. Inherited from [namedLocation](../resources/namedLocation.md).|
|includeUnknownCountriesAndRegions|Boolean|`true` if IP addresses that don't map to a country or region should be included in the named location. Optional. Default value is `false`.|
|modifiedDateTime|DateTimeOffset|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. Inherited from [namedLocation](../resources/namedLocation.md).|

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "countriesAndRegions": ["String"],
  "countryLookupMethod": "String",
  "createdDateTime": "String (timestamp)",
  "displayName": "String",
  "id": "String (identifier)",
  "includeUnknownCountriesAndRegions": true,
  "modifiedDateTime": "String (timestamp)"
}
```

## Related content

+ [What is Conditional Access?](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
+ [Using the location condition in a Conditional Access policy](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/location-condition)
