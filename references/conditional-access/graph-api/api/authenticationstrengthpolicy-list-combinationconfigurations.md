# List combinationConfigurations

> Source: https://learn.microsoft.com/en-us/graph/api/authenticationstrengthpolicy-list-combinationconfigurations?view=graph-rest-1.0  
> Microsoft doc last updated: 06/18/2024

Namespace: microsoft.graph

Get the [authenticationCombinationConfiguration](../resources/authenticationcombinationconfiguration.md) objects for an [authentication strength policy](../resources/authenticationstrengthpolicy.md). The objects can be of one or more of the following derived types:
* [fido2combinationConfigurations](../resources/fido2combinationconfiguration.md)
* [x509certificatecombinationconfiguration](../resources/x509certificatecombinationconfiguration.md)

**authenticationCombinationConfiguration** objects are supported only for custom authentication strengths.

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
GET /identity/conditionalAccess/authenticationStrength/policies/{authenticationStrengthPolicyId}/combinationConfigurations
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

If successful, this method returns a `200 OK` response code and a collection of [authenticationCombinationConfiguration](../resources/authenticationcombinationconfiguration.md) objects in the response body.

## Examples

### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/identity/conditionalAccess/authenticationStrength/policies/0e371351-6419-4c8a-8047-61eef0212ffb/combinationConfigurations
```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": [
    {
      "@odata.type" : "#microsoft.graph.fido2CombinationConfiguration",
      "id": "133b68c4-503b-4e87-839a-6c286a27381b",
      "allowedAAGUIDs": [
        "dcf6eadd-31fd-49e5-b84e-44035a5e6295",
        "e0d9c83d-f035-45b2-8d98-345903f91e29"
      ],
      "appliesToCombinations": ["fido2"]
    }
  ]
}
```
