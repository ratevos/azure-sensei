# riskyUser: confirmCompromised

> Source: https://learn.microsoft.com/en-us/graph/api/riskyuser-confirmcompromised?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024

Namespace: microsoft.graph

>**Note:** The riskyUsers API requires a Microsoft Entra ID P2 license.

Confirm one or more [riskyUser](../resources/riskyuser.md) objects as compromised. This action sets the targeted user's risk level to high.

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
POST /identityProtection/riskyUsers/confirmCompromised
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body
In the request body, supply JSON representation of the parameters.

The following table shows the parameters that can be used with this action.

|Parameter|Type|Description|
|:---|:---|:---|
|userIds|String collection|Specify the risky user IDs to mark as high risk.|

## Response

If successful, this action returns a `204 No Content` response code.

## Examples

### Request

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/identityProtection/riskyUsers/confirmCompromised
Content-Type: application/json

{
  "userIds": [
    "29f270bb-4d23-4f68-8a57-dc73dc0d4caf",
    "20f91ec9-d140-4d90-9cd9-f618587a1471"
  ]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	userIds = @(
	"29f270bb-4d23-4f68-8a57-dc73dc0d4caf"
"20f91ec9-d140-4d90-9cd9-f618587a1471"
)
}

Confirm-MgRiskyUserCompromised -BodyParameter $params

```

---

### Response

```http
HTTP/1.1 204 No Content
```
