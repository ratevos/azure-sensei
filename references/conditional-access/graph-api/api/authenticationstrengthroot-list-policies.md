# List authenticationStrengthPolicies

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthroot-list-policies?view=graph-rest-1.0  
> Microsoft doc last updated: 05/28/2024

Namespace: microsoft.graph

Get a list of the [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) objects and their properties. This API returns both built-in and custom policies.

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
GET /policies/authenticationStrengthPolicies
```

## Optional query parameters
This method supports the `$filter` OData query parameter on the **policyType** and **policyName** properties to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).
## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) objects in the response body.

## Examples

### Example 1: Get all authentication strength policies

#### Request

The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyAuthenticationStrengthPolicy

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies",
    "value": [
        {
            "id": "00000000-0000-0000-0000-000000000002",
            "createdDateTime": "2021-12-01T00:00:00Z",
            "modifiedDateTime": "2021-12-01T00:00:00Z",
            "displayName": "Multifactor authentication",
            "description": "Combinations of methods that satisfy strong authentication, such as a password + SMS",
            "policyType": "builtIn",
            "requirementsSatisfied": "mfa",
            "allowedCombinations": [
                "windowsHelloForBusiness",
                "fido2",
                "x509CertificateMultiFactor",
                "deviceBasedPush",
                "temporaryAccessPassOneTime",
                "temporaryAccessPassMultiUse",
                "password,microsoftAuthenticatorPush",
                "password,softwareOath",
                "password,hardwareOath",
                "password,x509CertificateSingleFactor",
                "password,x509CertificateMultiFactor",
                "password,sms",
                "password,voice",
                "federatedMultiFactor",
                "microsoftAuthenticatorPush,federatedSingleFactor",
                "softwareOath,federatedSingleFactor",
                "hardwareOath,federatedSingleFactor",
                "sms,federatedSingleFactor",
                "voice,federatedSingleFactor"
            ],
            "combinationConfigurations@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies('00000000-0000-0000-0000-000000000002')/combinationConfigurations",
            "combinationConfigurations": []
        },
        {
            "id": "00000000-0000-0000-0000-000000000003",
            "createdDateTime": "2021-12-01T00:00:00Z",
            "modifiedDateTime": "2021-12-01T00:00:00Z",
            "displayName": "Passwordless MFA",
            "description": "Passwordless methods that satisfy strong authentication, such as Passwordless sign-in with the Microsoft Authenticator",
            "policyType": "builtIn",
            "requirementsSatisfied": "mfa",
            "allowedCombinations": [
                "windowsHelloForBusiness",
                "fido2",
                "x509CertificateMultiFactor",
                "deviceBasedPush"
            ],
            "combinationConfigurations@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies('00000000-0000-0000-0000-000000000003')/combinationConfigurations",
            "combinationConfigurations": []
        },
        {
            "id": "00000000-0000-0000-0000-000000000004",
            "createdDateTime": "2021-12-01T00:00:00Z",
            "modifiedDateTime": "2021-12-01T00:00:00Z",
            "displayName": "Phishing resistant MFA",
            "description": "Phishing resistant, Passwordless methods for the strongest authentication, such as a FIDO2 security key",
            "policyType": "builtIn",
            "requirementsSatisfied": "mfa",
            "allowedCombinations": [
                "windowsHelloForBusiness",
                "fido2",
                "x509CertificateMultiFactor"
            ],
            "combinationConfigurations@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies('00000000-0000-0000-0000-000000000004')/combinationConfigurations",
            "combinationConfigurations": []
        }
    ]
}
```

### Example 2: Get policies that include specific authentication method modes

#### Request

The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies?$filter=allowedCombinations/any(x:x has 'sms, password')
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyAuthenticationStrengthPolicy -Filter "allowedCombinations/any(x:x has 'sms, password')" 

```

---

#### Response

The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies",
    "value": [
        {
            "id": "00000000-0000-0000-0000-000000000002",
            "createdDateTime": "2021-12-01T00:00:00Z",
            "modifiedDateTime": "2021-12-01T00:00:00Z",
            "displayName": "Multifactor authentication",
            "description": "Combinations of methods that satisfy strong authentication, such as a password + SMS",
            "policyType": "builtIn",
            "requirementsSatisfied": "mfa",
            "allowedCombinations": [
                "windowsHelloForBusiness",
                "fido2",
                "x509CertificateMultiFactor",
                "deviceBasedPush",
                "temporaryAccessPassOneTime",
                "temporaryAccessPassMultiUse",
                "password,microsoftAuthenticatorPush",
                "password,softwareOath",
                "password,hardwareOath",
                "password,sms",
                "password,voice",
                "federatedMultiFactor",
                "microsoftAuthenticatorPush,federatedSingleFactor",
                "softwareOath,federatedSingleFactor",
                "hardwareOath,federatedSingleFactor",
                "sms,federatedSingleFactor",
                "voice,federatedSingleFactor"
            ],
            "combinationConfigurations@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies('00000000-0000-0000-0000-000000000002')/combinationConfigurations",
            "combinationConfigurations": []
        }
    ]
}
```
