# Update authenticationCombinationConfiguration

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationcombinationconfiguration-update?view=graph-rest-1.0  
> Microsoft doc last updated: 06/18/2024

Namespace: microsoft.graph

Update the properties of an [authenticationCombinationConfiguration](../resources/authenticationcombinationconfiguration.md) object. 
The properties can be for one of the following derived types:
* [fido2combinationConfigurations](../resources/fido2combinationconfiguration.md)
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
PATCH /identity/conditionalAccess/authenticationStrength/policies/{authenticationStrengthPolicyId}/combinationConfigurations/{authenticationCombinationConfigurationId}
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body

|Property|Type|Description|
|:---|:---|:---|
|appliesToCombinations|authenticationMethodModes collection|The combinations where this configuration applies. For **fido2combinationConfigurations** use `"fido2"`, for **x509certificatecombinationconfiguration** use `"x509CertificateSingleFactor"` or `"x509CertificateMultiFactor"`. Required.|

## Response

If successful, this method returns a `204 No Content` response code.
## Examples

### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
PATCH https://graph.microsoft.com/v1.0/identity/conditionalAccess/authenticationStrength/policies/0e371351-6419-4c8a-8047-61eef0212ffb/combinationConfigurations/4643f174-fe85-42b8-8b84-516775750a30
Content-Type: application/json
Content-length: 130

{
  "appliesToCombinations": ["fido2"]
}
```

---

### Response
The following example shows the response.

``` http
HTTP/1.1 204 No Content
```
