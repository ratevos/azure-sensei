# Update conditionalaccesspolicy

> Source: https://learn.microsoft.com/en-us/graph/api/conditionalaccesspolicy-update?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024


Namespace: microsoft.graph

Update the properties of a [conditionalAccessPolicy](../resources/conditionalaccesspolicy.md) object.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|Policy.Read.All and Policy.ReadWrite.ConditionalAccess|Application.Read.All and Policy.ReadWrite.ConditionalAccess|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|Policy.Read.All and Policy.ReadWrite.ConditionalAccess|Application.Read.All and Policy.ReadWrite.ConditionalAccess|

> [!IMPORTANT]
> For delegated access using work or school accounts where the signed-in user is acting on another user, they must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Security Administrator
> - Conditional Access Administrator

> [!NOTE]
> This method has a [known permissions issue](https://learn.microsoft.com/en-us/graph/known-issues#conditional-access-policy-requires-consent-to-additional-permission) and may require consent to multiple permissions.

## HTTP request

```http
PATCH /identity/conditionalAccess/policies/{id}
```

## Request headers

| Name          | Description      |
|:--------------|:-----------------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
| Content-Type  | application/json. Required. |

## Request body

In the request body, supply the values for relevant fields that should be updated. Existing properties that aren't included in the request body maintain their previous values or are recalculated based on changes to other property values. For best performance, don't include existing values that haven't changed.

For the list of properties, see [conditionalAccessPolicy](../resources/conditionalaccesspolicy.md).

## Response

If successful, this method returns a `204 No Content` response code. It doesn't return anything in the response body.

## Example

### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies/{id}
Content-type: application/json

{
    "conditions": {
        "signInRiskLevels": [
            "high",
            "medium",
            "low"
        ]
    }
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	conditions = @{
		signInRiskLevels = @(
		"high"
	"medium"
"low"
)
}
}

Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId $conditionalAccessPolicyId -BodyParameter $params

```

---

### Response

The following example shows the response.

```http
HTTP/1.1 204 No Content
```
