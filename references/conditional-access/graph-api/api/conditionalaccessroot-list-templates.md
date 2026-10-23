# List conditionalAccessTemplates

> Source: https://learn.microsoft.com/en-us/graph/api/conditionalaccessroot-list-templates?view=graph-rest-1.0  
> Microsoft doc last updated: 10/17/2024

Namespace: microsoft.graph

Get a list of the [conditionalAccessTemplate](../resources/conditionalaccesstemplate.md) objects and their properties.

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
GET /identity/conditionalAccess/templates
```

## Optional query parameters
This method supports the `$filter` and `$select` OData query parameters to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
| Name            |Description|
|:----------------|:----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
| Accept-Language | Language. Optional. |

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [conditionalAccessTemplate](../resources/conditionalaccesstemplate.md) objects in the response body.

## Examples

### Example 1: List all conditional access policy templates

#### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/identity/conditionalAccess/templates
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgIdentityConditionalAccessTemplate

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identity/conditionalAccess/templates",
    "value": [
        {
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
    ]
}
```

### Example 2: List name, description, id, scenarios of templates whose scenarios contain "secureFoundation"

#### Request
The following example shows a request.

# [HTTP](#tab/http)

``` http
GET https://graph.microsoft.com/v1.0/identity/conditionalAccess/templates?$select=name,description,id,scenarios&$filter=scenarios has 'secureFoundation'
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgIdentityConditionalAccessTemplate -Property "name,description,id,scenarios" -Filter "scenarios has 'secureFoundation'" 

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

``` http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identity/conditionalAccess/templates(name,description,id,scenarios)",
    "value": [
        {
            "name": "Require multifactor authentication for admins",
            "description": "Require multifactor authentication for privileged administrative accounts to reduce risk of compromise. This policy will target the same roles as Security Default.",
            "id": "c7503427-338e-4c5e-902d-abe252abfb43",
            "scenarios": "secureFoundation,zeroTrust,protectAdmins"
        },
        {
            "name": "Securing security info registration",
            "description": "Secure when and how users register for Azure AD multifactor authentication and self-service password.",
            "id": "b8bda7f8-6584-4446-bce9-d871480e53fa",
            "scenarios": "secureFoundation,zeroTrust,remoteWork"
        },
        {
            "name": "Block legacy authentication",
            "description": "Block legacy authentication endpoints that can be used to bypass multifactor authentication.",
            "id": "0b2282f9-2862-4178-88b5-d79340b36cb8",
            "scenarios": "secureFoundation,zeroTrust,remoteWork,protectAdmins"
        },
        {
            "name": "Require multifactor authentication for all users",
            "description": "Require multifactor authentication for all user accounts to reduce risk of compromise.",
            "id": "a3d0a415-b068-4326-9251-f9cdf9feeb64",
            "scenarios": "secureFoundation,zeroTrust,remoteWork"
        }
    ]
}
```
