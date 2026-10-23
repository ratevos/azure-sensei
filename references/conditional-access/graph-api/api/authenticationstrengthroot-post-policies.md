# Create authenticationStrengthPolicy

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthroot-post-policies?view=graph-rest-1.0  
> Microsoft doc last updated: 07/24/2024

Namespace: microsoft.graph

Create a new custom [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object.

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
POST /policies/authenticationStrengthPolicies
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body
In the request body, supply a JSON representation of the [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object.

You can specify the following properties when creating an **authenticationStrengthPolicy**.

|Property|Type|Description|
|:---|:---|:---|
|displayName|String|The display name of the policy to be created. Required.|
|description|String|The description of the policy to be created. Optional.|
|allowedCombinations|authenticationMethodModes collection|The authentication method combinations allowed by this authentication strength policy. The possible values of this flagged enum are: `password`, `voice`, `hardwareOath`, `softwareOath`, `sms`, `fido2`, `windowsHelloForBusiness`, `microsoftAuthenticatorPush`, `deviceBasedPush`, `temporaryAccessPassOneTime`, `temporaryAccessPassMultiUse`, `email`, `x509CertificateSingleFactor`, `x509CertificateMultiFactor`, `federatedSingleFactor`, `federatedMultiFactor`, `unknownFutureValue`. For the list of allowed combinations, call the [List authenticationMethodModes](../api/authenticationstrengthroot-list-authenticationmethodmodes.md) API. Required.|

## Response

If successful, this method returns a `201 Created` response code and an [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object in the response body.

## Examples

### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
POST https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies
Content-Type: application/json

{
    "displayName": "Example",
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

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	displayName = "Example"
	requirementsSatisfied = "mfa"
	allowedCombinations = @(
	"fido2"
)
"combinationConfigurations@odata.context" = "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies('5790842a-5bab-44c2-9cf1-b38d675b70ea')/combinationConfigurations"
combinationConfigurations = @(
	@{
		"@odata.type" = "#microsoft.graph.fido2CombinationConfiguration"
		id = "42235320-c8db-4d8c-9344-8f1ce87f734b"
		appliesToCombinations = @(
		"fido2"
	)
	allowedAAGUIDs = @(
	"de1e552d-db1d-4423-a619-566b625cdc84"
"90a3ccdf-635c-4729-a248-9b709135078f"
)
}
)
}

New-MgPolicyAuthenticationStrengthPolicy -BodyParameter $params

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies/$entity",
    "id": "7daf2132-6a2d-4e78-a699-b823babf4436",
    "createdDateTime": "2024-07-23T17:10:58.1492045Z",
    "modifiedDateTime": "2024-07-23T17:10:58.1492045Z",
    "displayName": "Example",
    "description": "",
    "policyType": "custom",
    "requirementsSatisfied": "mfa",
    "allowedCombinations": [
        "fido2"
    ],
    "combinationConfigurations@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/authenticationStrengthPolicies('7daf2132-6a2d-4e78-a699-b823babf4436')/combinationConfigurations",
    "combinationConfigurations": [
        {
            "@odata.type": "#microsoft.graph.fido2CombinationConfiguration",
            "id": "c0fdf2f9-3b3f-4bbf-988c-17606ea4b4e4",
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
