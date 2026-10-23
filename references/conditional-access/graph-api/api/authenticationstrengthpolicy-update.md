# Update authenticationStrengthPolicy

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthpolicy-update?view=graph-rest-1.0  
> Microsoft doc last updated: 05/28/2024

Namespace: microsoft.graph

Update the properties of an [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object. You cannot update the allowed auth method combinations using this request. To do so, use the [Update allowed combinations](authenticationstrengthpolicy-updateallowedcombinations.md) action.

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
PATCH /policies/authenticationStrengthPolicies/{authenticationStrengthPolicyId}
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body

|Property|Type|Description|
|:---|:---|:---|
|displayName|String|The display name of the policy to be created. Optional.|
|description|String|The description of the policy to be created. Optional.|

## Response

If successful, this method returns a `204 No Content` response code.
## Examples

### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
PATCH https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies/a34a4c89-c5bf-4c0b-927d-adc396bf1f19
Content-Type: application/json
Content-length: 239

{
  "@odata.type": "#microsoft.graph.authenticationStrengthPolicy",
  "displayName": "FIDO2 only",
  "description": "An auth strength allowing only FIDO2 security keys."
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	"@odata.type" = "#microsoft.graph.authenticationStrengthPolicy"
	displayName = "FIDO2 only"
	description = "An auth strength allowing only FIDO2 security keys."
}

Update-MgPolicyAuthenticationStrengthPolicy -AuthenticationStrengthPolicyId $authenticationStrengthPolicyId -BodyParameter $params

```

---

### Response
The following example shows the response.

``` http
HTTP/1.1 204 No Content
```
