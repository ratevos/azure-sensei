# Delete authenticationStrengthPolicy

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthroot-delete-policies?view=graph-rest-1.0  
> Microsoft doc last updated: 05/28/2024

Namespace: microsoft.graph

Delete a custom [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|Policy.ReadWrite.ConditionalAccess|Policy.ReadWrite.AuthenticationMethod|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|Policy.ReadWrite.ConditionalAccess|Policy.ReadWrite.AuthenticationMethod|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Conditional Access administrator
> - Security Administrator

## HTTP request

``` http
DELETE /policies/authenticationStrengthPolicies/{authenticationStrengthPolicyId}
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `204 No Content` response code.

## Examples

### Request
The following example shows a request.
# [HTTP](#tab/http)

``` http
DELETE https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies/6e7d7469-07c5-4bb2-a801-5eaef8fb7c1e/$ref
```

---

### Response
The following example shows the response.

``` http
HTTP/1.1 204 No Content
```
