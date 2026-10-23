# Get template

> Source: https://learn.microsoft.com/en-us/graph/api/conditionalaccesstemplate-get?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024

Namespace: microsoft.graph

Read the properties and relationships of a [conditionalAccessTemplate](../resources/conditionalaccesstemplate.md) object.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|Policy.Read.All|Not available.|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|Policy.Read.All|Not available.|

> [!IMPORTANT]
> For delegated access using work or school accounts where the signed-in user is acting on another user, they must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Global Secure Access Administrator - read standard properties
> - Security Reader - read standard properties
> - Security Administrator - read standard properties
> - Global Reader
> - Conditional Access Administrator

## HTTP request

``` http
GET /identity/conditionalAccess/templates/{id}
```

## Optional query parameters
This method supports the `$select` OData query parameter to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
| Name            |Description|
|:----------------|:----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
| Accept-Language | Language. Optional. |

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a [conditionalAccessTemplate](../resources/conditionalaccesstemplate.md) object in the response body.

## Examples

### Example 1: Get the properties a template by ID

#### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/identity/conditionalAccess/templates/c7503427-338e-4c5e-902d-abe252abfb43
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgIdentityConditionalAccessTemplate -ConditionalAccessTemplateId $conditionalAccessTemplateId

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identity/conditionalAccess/templates/$entity",
    "name": "Require multifactor authentication for admins",
    "description": "Require multifactor authentication for privileged administrative accounts to reduce risk of compromise. This policy will target the same roles as Security Default.",
    "id": "c7503427-338e-4c5e-902d-abe252abfb43",
    "scenarios": "secureFoundation,zeroTrust,protectAdmins",
    "details": {
        "sessionControls": null,
        "conditions": {
            "userRiskLevels": [],
            "signInRiskLevels": [],
            "clientAppTypes": [
                "all"
            ],
            "servicePrincipalRiskLevels": [],
            "platforms": null,
            "locations": null,
            "signInRiskDetections": null,
            "times": null,
            "deviceStates": null,
            "devices": null,
            "clientApplications": null,
            "applications": {
                "includeApplications": [
                    "All"
                ],
                "excludeApplications": [],
                "includeUserActions": [],
                "includeAuthenticationContextClassReferences": [],
                "applicationFilter": null,
                "networkAccess": null
            },
            "users": {
                "includeUsers": [],
                "excludeUsers": [
                    "Current administrator will be excluded"
                ],
                "includeGroups": [],
                "excludeGroups": [],
                "includeRoles": [
                    "62e90394-69f5-4237-9190-012177145e10",
                    "194ae4cb-b126-40b2-bd5b-6091b380977d"
                ],
                "excludeRoles": [],
                "includeGuestsOrExternalUsers": null,
                "excludeGuestsOrExternalUsers": null
            }
        },
        "grantControls": {
            "operator": "OR",
            "builtInControls": [
                "mfa"
            ],
            "customAuthenticationFactors": [],
            "termsOfUse": [],
            "authenticationStrength": null
        }
    }
}
```

### Example 2: Select details of a template

#### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/identity/conditionalAccess/templates/c7503427-338e-4c5e-902d-abe252abfb43?$select=details
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgIdentityConditionalAccessTemplate -ConditionalAccessTemplateId $conditionalAccessTemplateId -Property "details" 

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identity/conditionalAccess/templates(details)/$entity",
    "details": {
        "sessionControls": null,
        "conditions": {
            "userRiskLevels": [],
            "signInRiskLevels": [],
            "clientAppTypes": [
                "all"
            ],
            "servicePrincipalRiskLevels": [],
            "platforms": null,
            "locations": null,
            "signInRiskDetections": null,
            "times": null,
            "deviceStates": null,
            "devices": null,
            "clientApplications": null,
            "applications": {
                "includeApplications": [
                    "All"
                ],
                "excludeApplications": [],
                "includeUserActions": [],
                "includeAuthenticationContextClassReferences": [],
                "applicationFilter": null,
                "networkAccess": null
            },
            "users": {
                "includeUsers": [],
                "excludeUsers": [
                    "Current administrator will be excluded"
                ],
                "includeGroups": [],
                "excludeGroups": [],
                "includeRoles": [
                    "62e90394-69f5-4237-9190-012177145e10",
                    "194ae4cb-b126-40b2-bd5b-6091b380977d"
                ],
                "excludeRoles": [],
                "includeGuestsOrExternalUsers": null,
                "excludeGuestsOrExternalUsers": null
            }
        },
        "grantControls": {
            "operator": "OR",
            "builtInControls": [
                "mfa"
            ],
            "customAuthenticationFactors": [],
            "termsOfUse": [],
            "authenticationStrength": null
        }
    }
}
```
