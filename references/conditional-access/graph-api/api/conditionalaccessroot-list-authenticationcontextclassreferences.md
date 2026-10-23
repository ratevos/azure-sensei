# List authenticationContextClassReferences

> Source: https://learn.microsoft.com/en-us/graph/api/conditionalaccessroot-list-authenticationcontextclassreferences?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024


Namespace: microsoft.graph

Retrieve a list of [authenticationContextClassReference](../resources/authenticationcontextclassreference.md) objects.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|AuthenticationContext.Read.All|AuthenticationContext.ReadWrite.All, Policy.Read.ConditionalAccess, Policy.ReadWrite.ConditionalAccess|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|AuthenticationContext.Read.All|AuthenticationContext.ReadWrite.All, Policy.Read.ConditionalAccess, Policy.ReadWrite.ConditionalAccess|

> [!IMPORTANT]
> For delegated access using work or school accounts where the signed-in user is acting on another user, they must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Global Secure Access Administrator - read standard properties
> - Security Reader - read standard properties
> - Security Administrator - read standard properties
> - Global Reader
> - Conditional Access Administrator

## HTTP request

```http
GET /identity/conditionalAccess/authenticationContextClassReferences
```
## Optional query parameters

This method supports the `$filter` OData query parameter to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers

| Name      |Description|
|:----------|:----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [authenticationContextClassReference](..\resources\authenticationcontextclassreference.md) objects in the response body.

## Examples

### Request

The following example shows a request.

# [HTTP](#tab/http)

```msgraph-interactive
GET /identity/conditionalAccess/authenticationContextClassReferences
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgIdentityConditionalAccessAuthenticationContextClassReference

```

---

### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#/conditionalAccess/authenticationContextClassReferences",
  "value": [
    {
      "id": "c1",
      "displayName": "Contoso trusted locations",
      "description": "Access is only allowed from trusted locations",
      "isAvailable": true
    }
  ]
}
```
