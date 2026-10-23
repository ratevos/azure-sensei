# authenticationStrengthPolicy: usage

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthpolicy-usage?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Allows the caller to see which Conditional Access policies reference a specified authentication strength policy. The policies are returned in two collections, one containing Conditional Access policies that require an MFA claim and the other containing Conditional Access policies that don't require such a claim. Policies in the former category are restricted in what kinds of changes may be made to them to prevent undermining the MFA requirement of those policies.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|Policy.Read.AuthenticationMethod|Policy.Read.All, Policy.ReadWrite.AuthenticationMethod, Policy.ReadWrite.ConditionalAccess|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|Policy.Read.AuthenticationMethod|Policy.Read.All, Policy.ReadWrite.AuthenticationMethod, Policy.ReadWrite.ConditionalAccess|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Conditional Access administrator
> - Security Administrator
> - Security Reader

## HTTP request

``` http
GET /policies/authenticationStrengthPolicies/{authenticationStrengthPolicyId}/usage
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this function returns a `200 OK` response code and an [authenticationStrengthUsage](../resources/authenticationstrengthusage.md) complex type in the response body.

## Examples

### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies/{authenticationStrengthPolicyId}/usage
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Invoke-MgUsagePolicyAuthenticationStrengthPolicy -AuthenticationStrengthPolicyId $authenticationStrengthPolicyId

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "mfa": [
        {
            "displayName": "Conditional Access Policy 1",
            "id": "a26dbede-a6c0-4156-92e1-6c86dd7bc561",
            "grantControls": {
                "authenticationStrength": {
                    "id": "00000000-0000-0000-0000-000000000003"
                },
                "controls": [
                    "MfaAndChangePassword"
                ]
            }
        }
    ],
    "none": [
        {
            "displayName": "Conditional Access Policy 2",
            "id": "5d7d5a7f-dd35-412b-a18d-5411d8eafe8f",
            "grantControls": {
                "authenticationStrength": {
                    "id": "00000000-0000-0000-0000-000000000003"
                },
                "controls": [
                    "RequireCompliantDevice"
                ]
            }
        }
    ]
}
```
