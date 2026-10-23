# Get authenticationStrengthPolicy

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthpolicy-get?view=graph-rest-1.0  
> Microsoft doc last updated: 07/24/2024

Namespace: microsoft.graph

Read the properties and relationships of an [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object.

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
GET /policies/authenticationStrengthPolicies/{authenticationStrengthPolicyId}
```

## Optional query parameters
This method doesn't support OData query parameters.

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and an [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object in the response body.

## Examples

### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies/00000000-0000-0000-0000-000000000004
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyAuthenticationStrengthPolicy -AuthenticationStrengthPolicyId $authenticationStrengthPolicyId

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies/$entity",
    "@microsoft.graph.tips": "Use $select to choose only the properties your app needs, as this can lead to performance improvements. For example: GET policies/authenticationStrengthPolicies('<guid>')?$select=allowedCombinations,createdDateTime",
    "id": "5790842a-5bab-44c2-9cf1-b38d675b70ea",
    "createdDateTime": "2024-07-10T20:27:42.5264618Z",
    "modifiedDateTime": "2024-07-10T23:49:43.883679Z",
    "displayName": "Auth Strength policy name",
    "description": "",
    "policyType": "custom",
    "requirementsSatisfied": "mfa",
    "allowedCombinations": [
        "fido2"
    ],
    "combinationConfigurations@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies('5790842a-5bab-44c2-9cf1-b38d675b70ea')/combinationConfigurations",
    "combinationConfigurations": [
        {
            "@odata.type": "#microsoft.graph.fido2CombinationConfiguration",
            "id": "42235320-c8db-4d8c-9344-8f1ce87f734b",
            "appliesToCombinations": [
                "fido2"
            ],
            "allowedAAGUIDs": [
                "de1e552d-db1d-4423-a619-566b625cdc84",
                "90a3ccdf-635c-4729-a248-9b709135078f"
            ]
        }
    ]
}
```
