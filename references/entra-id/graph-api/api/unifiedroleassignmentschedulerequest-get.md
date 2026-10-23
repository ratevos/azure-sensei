# Get unifiedRoleAssignmentScheduleRequest

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleassignmentschedulerequest-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

In PIM, read the details of a request for an active and persistent role assignment made through the [unifiedRoleAssignmentScheduleRequest](../resources/unifiedroleassignmentschedulerequest.md) object.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|RoleAssignmentSchedule.ReadWrite.Directory|RoleManagement.ReadWrite.Directory|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|RoleAssignmentSchedule.ReadWrite.Directory|RoleManagement.ReadWrite.Directory|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - For read operations: *Global Reader*, *Security Operator*, *Security Reader*, *Security Administrator*, or *Privileged Role Administrator*
> - For write operations: *Privileged Role Administrator*

## HTTP request

```http
GET /roleManagement/directory/roleAssignmentScheduleRequests/{unifiedRoleAssignmentScheduleRequestId}
```

## Optional query parameters
This method supports the `$select` and `$expand` OData query parameters to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and an [unifiedRoleAssignmentScheduleRequest](../resources/unifiedroleassignmentschedulerequest.md) object in the response body.

## Examples

### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleRequests/95c690fb-3eb3-4942-a03f-4524aed6f31e
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleAssignmentScheduleRequest -UnifiedRoleAssignmentScheduleRequestId $unifiedRoleAssignmentScheduleRequestId

```

---

### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignmentScheduleRequests/$entity",
    "id": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
    "status": "Provisioned",
    "createdDateTime": "2022-04-11T11:50:05.95Z",
    "completedDateTime": "2022-04-11T11:50:06Z",
    "approvalId": null,
    "customData": null,
    "action": "adminAssign",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "roleDefinitionId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
    "directoryScopeId": "/",
    "appScopeId": null,
    "isValidationOnly": false,
    "targetScheduleId": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
    "justification": "Assign Groups Admin to IT Helpdesk group",
    "createdBy": {
        "application": null,
        "device": null,
        "user": {
            "displayName": null,
            "id": "3fbd929d-8c56-4462-851e-0eb9a7b3a2a5"
        }
    },
    "scheduleInfo": {
        "startDateTime": "2022-04-11T11:50:05.9999343Z",
        "recurrence": null,
        "expiration": {
            "type": "noExpiration",
            "endDateTime": null,
            "duration": null
        }
    },
    "ticketInfo": {
        "ticketNumber": null,
        "ticketSystem": null
    }
}
```

### Example 2: Retrieve specified properties of a role assignment request and expand the relationships

#### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleRequests/95c690fb-3eb3-4942-a03f-4524aed6f31e?$select=principalId,action,roleDefinitionId&$expand=roleDefinition,activatedUsing,principal,targetSchedule
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleAssignmentScheduleRequest -UnifiedRoleAssignmentScheduleRequestId $unifiedRoleAssignmentScheduleRequestId -Property "principalId,action,roleDefinitionId" -ExpandProperty "roleDefinition,activatedUsing,principal,targetSchedule" 

```

---

#### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignmentScheduleRequests(principalId,action,roleDefinitionId,roleDefinition(),activatedUsing(),principal(),targetSchedule())/$entity",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "action": "adminAssign",
    "roleDefinitionId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
    "roleDefinition": {
        "id": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
        "description": "",
        "displayName": "Groups Administrator",
        "isBuiltIn": true,
        "isEnabled": true,
        "templateId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
        "version": null,
        "resourceScopes": [],
        "rolePermissions": []
    },
    "activatedUsing": null,
    "principal": {
        "@odata.type": "#microsoft.graph.user",
        "id": "071cc716-8147-4397-a5ba-b2105951cc0b",
        "displayName": "Conf Room Adams",
        "userPrincipalName": "Adams@Contoso.com",
        "mail": "Adams@Contoso.com",
        "businessPhones": [],
        "givenName": null,
        "jobTitle": null,
        "mobilePhone": null,
        "officeLocation": null,
        "preferredLanguage": null,
        "surname": null
    },
    "targetSchedule": {
        "id": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
        "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
        "roleDefinitionId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
        "directoryScopeId": "/",
        "appScopeId": null,
        "createdUsing": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
        "createdDateTime": "2022-04-11T11:50:05.95Z",
        "modifiedDateTime": "2022-04-11T11:50:05.95Z",
        "status": "Provisioned",
        "assignmentType": "Assigned",
        "memberType": "Direct",
        "scheduleInfo": {
            "startDateTime": "2022-04-11T11:50:05.9999343Z",
            "recurrence": null,
            "expiration": {
                "type": "noExpiration",
                "endDateTime": null,
                "duration": null
            }
        }
    }
}
```
