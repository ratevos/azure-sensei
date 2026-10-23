# riskyUser: confirmSafe

> Source: https://learn.microsoft.com/en-us/graph/api/riskyuser-confirmsafe?view=graph-rest-1.0  
> Microsoft doc last updated: 05/14/2025


Namespace: microsoft.graph

Confirm one or more [riskyUser](../resources/riskyuser.md) objects as safe. This action sets the targeted user's risk level to none.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|IdentityRiskyUser.ReadWrite.All|Not available.|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|IdentityRiskyUser.ReadWrite.All|Not available.|
> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. *Security Administrator* is the least privileged role supported for this operation.

## HTTP request

```http
POST /identityProtection/riskyUsers/confirmSafe
```

## Request headers

|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body

In the request body, supply a JSON representation of the parameters.

The following table lists the parameters that are required when you call this action.

|Parameter|Type|Description|
|:---|:---|:---|
|userIds|String collection|Specify the risky user IDs to mark as safe.|

## Response

If successful, this action returns a `204 No Content` response code.

## Examples

### Request

The following example shows a request.
# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/identityProtection/riskyUsers/confirmSafe
Content-Type: application/json

{
  "userIds": [
    "5a0c76d2-cb57-4ece-9bc1-c323178f116a",
    "96609214-09ef-4f80-9d4a-ace5fceecaec",
    "05020696-4eb8-45a3-918f-8f8bb7ad6015"
  ]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	userIds = @(
	"5a0c76d2-cb57-4ece-9bc1-c323178f116a"
"96609214-09ef-4f80-9d4a-ace5fceecaec"
"05020696-4eb8-45a3-918f-8f8bb7ad6015"
)
}

Confirm-MgRiskyUserSafe -BodyParameter $params

```

---

### Response

The following example shows the response.

```http
HTTP/1.1 204 No Content
```
