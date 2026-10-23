# Delete ipNamedLocation

> Source: https://learn.microsoft.com/en-us/graph/api/ipnamedlocation-delete?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024


Namespace: microsoft.graph

Delete an [ipNamedLocation](../resources/ipNamedLocation.md) object.

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
DELETE /identity/conditionalAccess/namedLocations/{id}
```

## Request headers

| Name          | Description   |
|:--------------|:--------------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `204 No Content` response code. It doesn't return anything in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
DELETE https://graph.microsoft.com/v1.0/identity/conditionalAccess/namedLocations/0854951d-5fc0-4eb1-b392-9b2c9d7949c2
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Remove-MgIdentityConditionalAccessNamedLocation -NamedLocationId $namedLocationId

```

---

### Response

The following example shows the response.

```http
HTTP/1.1 204 No Content
```
