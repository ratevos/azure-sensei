# authenticationStrengthPolicy: updateAllowedCombinations

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthpolicy-updateallowedcombinations?view=graph-rest-1.0  
> Microsoft doc last updated: 05/28/2024

Namespace: microsoft.graph

Update the allowedCombinations property of an [authenticationStrengthPolicy](../resources/authenticationstrengthpolicy.md) object. To update other properties of an authenticationStrengthPolicy object, use the [Update authenticationStrengthPolicy](authenticationstrengthpolicy-update.md) method.

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
POST /policies/authenticationStrengthPolicies/{authenticationStrengthPolicyId}/updateAllowedCombinations
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body
In the request body, supply a JSON representation of the parameters.

The following table shows the parameters that can be used with this action.

|Parameter|Type|Description|
|:---|:---|:---|
|allowedCombinations|authenticationMethodModes collection|The authentication method combinations allowed by this authentication strength policy. The possible values of this flagged enum are: `password`, `voice`, `hardwareOath`, `softwareOath`, `sms`, `fido2`, `windowsHelloForBusiness`, `microsoftAuthenticatorPush`, `deviceBasedPush`, `temporaryAccessPassOneTime`, `temporaryAccessPassMultiUse`, `email`, `x509CertificateSingleFactor`, `x509CertificateMultiFactor`, `federatedSingleFactor`, `federatedMultiFactor`, `unknownFutureValue`. For the list of allowed combinations, call the [List authenticationMethodModes](../api/authenticationstrengthroot-list-authenticationmethodmodes.md) API. Required.|

## Response

If successful, this action returns a `200 OK` response code and a [updateAllowedCombinationsResult](../resources/updateallowedcombinationsresult.md) in the response body.

## Examples

### Request
The following example shows a request.
# [HTTP](#tab/http)

``` http
POST https://graph.microsoft.com/v1.0/policies/authenticationStrengthPolicies/33c5d2c0-884e-4b5d-a5b8-5395082b092c/updateAllowedCombinations
Content-Type: application/json
Content-length: 51

{
  "allowedCombinations": [
      "password, voice"
  ]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	allowedCombinations = @(
	"password, voice"
)
}

Update-MgPolicyAuthenticationStrengthPolicyAllowedCombination -AuthenticationStrengthPolicyId $authenticationStrengthPolicyId -BodyParameter $params

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.type" : "#microsoft.graph.updateAllowedCombinationsResult",
  "previousCombinations": [
    "fido2",
    "password, voice"
  ],
  "currentCombinations": [
    "password, voice"
  ],
  "conditionalAccessReferences": [
    "53a3968a-ae2c-4b82-a313-091d10c52bfa"
  ],
  "additionalInformation": "You have lowered the security of the My Custom Strength authentication strength by adding a lower security combination. This Authentication Strength is referenced by one or more Conditional Access policies. Review conditionalAccessReferences to understand which Conditional Access policies were impacted by this change. To reverse your changes back, use updateAllowedCombinations action with the previousCombinations values."
}
```
