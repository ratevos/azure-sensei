# Create authenticationCombinationConfiguration

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthpolicy-post-combinationconfigurations?view=graph-rest-1.0  
> Microsoft doc last updated: 06/25/2024

Namespace: microsoft.graph

Create a new authenticationCombinationConfiguration object which can be of one of the following derived types:
* [fido2combinationConfiguration](../resources/fido2combinationconfiguration.md)
* [x509certificatecombinationconfiguration](../resources/x509certificatecombinationconfiguration.md)

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
POST /identity/conditionalAccess/authenticationStrength/policies/{authenticationStrengthPolicyId}/combinationConfigurations
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body
In the request body, supply a JSON representation of the [authenticationCombinationConfiguration](../resources/authenticationcombinationconfiguration.md) object.

You can specify the following properties when creating an **authenticationCombinationConfiguration**. Additionally, you must supply the @odata.type and required properties of the derived type of [authenticationCombinationConfiguration](../resources/authenticationcombinationconfiguration.md) that you're creating. For example, `"@odata.type" : "#microsoft.graph.fido2CombinationConfiguration"`.

|Property|Type|Description|
|:---|:---|:---|
|appliesToCombinations|authenticationMethodModes collection|The combinations where this configuration applies. For **fido2combinationConfigurations** use `"fido2"`, for **x509certificatecombinationconfiguration** use `"x509CertificateSingleFactor"` or `"x509CertificateMultiFactor"`. Required.|

## Response

If successful, this method returns a `201 Created` response code and an [authenticationCombinationConfiguration](../resources/authenticationcombinationconfiguration.md) object which can be a [fido2combinationConfigurations](../resources/fido2combinationconfiguration.md) or an [x509certificatecombinationconfiguration](../resources/x509certificatecombinationconfiguration.md) object in the response body.

## Examples

### Example 1: Create a fido2combinationConfiguration object

#### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
POST https://graph.microsoft.com/v1.0/identity/conditionalAccess/authenticationStrength/policies/{authenticationStrengthPolicyId}/combinationConfigurations
Content-Type: application/json
Content-length: 130

{
  "@odata.type" : "#microsoft.graph.fido2CombinationConfiguration",
  "allowedAAGUIDs": [
    "486c3b50-889c-480a-abc5-c04ef7c873e0",
    "c042882f-a621-40c8-94d3-9cde3a826fed",
    "ec454c08-4c77-4012-9d48-45f7f0fccdfb"
  ],
  "appliesToCombinations": ["fido2"]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	"@odata.type" = "#microsoft.graph.fido2CombinationConfiguration"
	allowedAAGUIDs = @(
	"486c3b50-889c-480a-abc5-c04ef7c873e0"
"c042882f-a621-40c8-94d3-9cde3a826fed"
"ec454c08-4c77-4012-9d48-45f7f0fccdfb"
)
appliesToCombinations = @(
"fido2"
)
}

New-MgIdentityConditionalAccessAuthenticationStrengthPolicyCombinationConfiguration -AuthenticationStrengthPolicyId $authenticationStrengthPolicyId -BodyParameter $params

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.type" : "#microsoft.graph.fido2CombinationConfiguration",
  "id": "96cb1a17-e45e-4b4f-8b4b-4a9490d63d66",
  "allowedAAGUIDs": [
    "486c3b50-889c-480a-abc5-c04ef7c873e0",
    "c042882f-a621-40c8-94d3-9cde3a826fed",
    "ec454c08-4c77-4012-9d48-45f7f0fccdfb"
  ],
  "appliesToCombinations": ["fido2"]
}
```

### Example 2: Create a x509CertificateCombinationConfiguration object

#### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
POST https://graph.microsoft.com/v1.0/identity/conditionalAccess/authenticationStrength/policies/{authenticationStrengthPolicyId}/combinationConfigurations 
 
{ 
    "@odata.type": "#microsoft.graph.x509CertificateCombinationConfiguration", 
    "allowedIssuerSkis": [ 
        "9A4248C6AC8C2931AB2A86537818E92E7B6C97B6" 
    ], 
    "allowedPolicyOIDs": [], 
    "appliesToCombinations": [ 
        "x509CertificateSingleFactor " 
    ] 
} 
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	"@odata.type" = "#microsoft.graph.x509CertificateCombinationConfiguration"
	allowedIssuerSkis = @(
	"9A4248C6AC8C2931AB2A86537818E92E7B6C97B6"
)
allowedPolicyOIDs = @(
)
appliesToCombinations = @(
"x509CertificateSingleFactor "
)
}

New-MgIdentityConditionalAccessAuthenticationStrengthPolicyCombinationConfiguration -AuthenticationStrengthPolicyId $authenticationStrengthPolicyId -BodyParameter $params

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 201 Created
Content-Type: application/json

{ 
    "@odata.type": "#microsoft.graph.x509CertificateCombinationConfiguration", 
    "id" : "96cb1a17-e45e-4b4f-8b4b-4a9490d63d66",
    "allowedIssuerSkis": [ 
        "9A4248C6AC8C2931AB2A86537818E92E7B6C97B6" 
    ], 
    "allowedPolicyOIDs": [], 
    "appliesToCombinations": [ 
        "x509CertificateSingleFactor " 
    ] 
} 
```
