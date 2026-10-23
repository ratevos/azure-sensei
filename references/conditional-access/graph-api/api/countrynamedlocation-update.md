# Update countryNamedlocation

> Source: https://learn.microsoft.com/en-us/graph/api/countrynamedlocation-update?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024


Namespace: microsoft.graph

Update the properties of a [countryNamedLocation](../resources/countryNamedLocation.md) object.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|Policy.Read.All and Policy.ReadWrite.ConditionalAccess| Not available.|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|Policy.Read.All and Policy.ReadWrite.ConditionalAccess|Not available.|

> [!IMPORTANT]
> For delegated access using work or school accounts where the signed-in user is acting on another user, they must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Security Administrator
> - Conditional Access Administrator

## HTTP request

```http
PATCH /identity/conditionalAccess/namedLocations/{id}
```

## Request headers

| Name       | Description|
|:-----------|:-----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
| Content-type  | application/json. Required. |

## Request body

In the request body, supply the values for relevant fields that should be updated. Existing properties that aren't included in the request body maintain their previous values or are recalculated based on changes to other property values. For best performance, don't include existing values that haven't changed.

You must specify the **@odata.type** as `#microsoft.graph.countryNamedLocation`.

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|countriesAndRegions|String collection|List of countries and/or regions in two-letter format specified by ISO 3166-2.|
|displayName|String|Human-readable name of the location.|
|includeUnknownCountriesAndRegions|Boolean|The value is `true` if IP addresses that don't map to a country or region should be included in the named location.|

## Response

If successful, this method returns a `204 No Content` response code. It doesn't return anything in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/identity/conditionalAccess/namedLocations/1c4427fd-0885-4a3d-8b23-09a899ffa959
Content-type: application/json

{
    "@odata.type": "#microsoft.graph.countryNamedLocation",
    "displayName": "Updated named location without unknown countries and regions",
    "countriesAndRegions": [
        "CA",
        "IN"
    ],
    "includeUnknownCountriesAndRegions": false
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	"@odata.type" = "#microsoft.graph.countryNamedLocation"
	displayName = "Updated named location without unknown countries and regions"
	countriesAndRegions = @(
	"CA"
"IN"
)
includeUnknownCountriesAndRegions = $false
}

Update-MgIdentityConditionalAccessNamedLocation -NamedLocationId $namedLocationId -BodyParameter $params

```

---

### Response

The following example shows the response.

```http
HTTP/1.1 204 No Content
```
