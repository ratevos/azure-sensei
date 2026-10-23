# List history of riskyUser

> Source: https://learn.microsoft.com/en-us/graph/api/riskyuser-list-history?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024

Namespace: microsoft.graph

Get the riskyUserHistoryItems from the history navigation property.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|IdentityRiskyUser.Read.All|IdentityRiskyUser.ReadWrite.All|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|IdentityRiskyUser.Read.All|IdentityRiskyUser.ReadWrite.All|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Global Reader
> - Security Operator
> - Security Reader
> - Security Administrator

## HTTP request

```http
GET /identityProtection/riskyUsers/{riskyUserId}/history
```

## Optional query parameters
This method supports the `$select` OData query parameter to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [riskyUserHistoryItem](../resources/riskyuserhistoryitem.md) objects in the response body.

## Examples

### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityProtection/riskyUsers/{riskyUserId}/history
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgRiskyUserHistory -RiskyUserId $riskyUserId

```

---

### Response
**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": [
    {
      "@odata.type": "#microsoft.graph.riskyUserHistoryItem",
      "id": "5e1d812e-812e-5e1d-2e81-1d5e2e811d5e",
      "isDeleted": "Boolean",
      "isProcessing": "Boolean",
      "riskLastUpdatedDateTime": "String (timestamp)",
      "riskLevel": "String",
      "riskState": "String",
      "riskDetail": "String",
      "userDisplayName": "String",
      "userPrincipalName": "String",
      "userId": "String",
      "initiatedBy": "String",
      "activity": {
          "riskEventTypes": [],
          "detail": "userPerformedSecuredPasswordReset"
      }
    }
  ]
}
```
