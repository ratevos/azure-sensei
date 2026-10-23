# Update ipnamedlocation

> Source: https://learn.microsoft.com/en-us/graph/api/ipnamedlocation-update?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024


Namespace: microsoft.graph

Update the properties of an [ipNamedLocation](../resources/ipNamedLocation.md) object.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|Policy.Read.All and Policy.ReadWrite.ConditionalAccess|Not available.|
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
| Content-type | application/json. Required. |

## Request body

In the request body, supply the values for relevant fields that should be updated. Existing properties that aren't included in the request body maintains their previous values or are recalculated based on changes to other property values. For best performance, don't include existing values that haven't changed.

You must specify the **@odata.type** as `#microsoft.graph.ipNamedLocation`.

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|displayName|String|Human-readable name of the location.|
|ipRanges|[ipRange](../resources/iprange.md) collection|List of IP address ranges in IPv4 CIDR format (1.2.3.4/32) or any allowable IPv6 format from IETF RFC5962. To retain any existing **ipRange** objects, you must add them to this object in addition to any new objects; to remove any **ipRange** objects, exclude them from this object.|
|isTrusted|Boolean|The value is `true` if this location is explicitly trusted.|

## Response

If successful, this method returns a `204 No Content` response code. It doesn't return anything in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/identity/conditionalAccess/namedLocations/0854951d-5fc0-4eb1-b392-9b2c9d7949c2
Content-type: application/json

{
    "@odata.type": "#microsoft.graph.ipNamedLocation",
    "displayName": "Untrusted named location with only IPv4 address",
    "isTrusted": false,
    "ipRanges": [
        {
            "@odata.type": "#microsoft.graph.iPv4CidrRange",
            "cidrAddress": "6.5.4.3/18"
        }

    ]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	"@odata.type" = "#microsoft.graph.ipNamedLocation"
	displayName = "Untrusted named location with only IPv4 address"
	isTrusted = $false
	ipRanges = @(
		@{
			"@odata.type" = "#microsoft.graph.iPv4CidrRange"
			cidrAddress = "6.5.4.3/18"
		}
	)
}

Update-MgIdentityConditionalAccessNamedLocation -NamedLocationId $namedLocationId -BodyParameter $params

```

---

### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 204 No Content
```
