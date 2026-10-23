# Get privilegedAccessGroupEligibilityScheduleRequest

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroupeligibilityschedulerequest-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Read the properties and relationships of a [privilegedAccessGroupEligibilityScheduleRequest](../resources/privilegedaccessgroupeligibilityschedulerequest.md) object.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|PrivilegedEligibilitySchedule.Read.AzureADGroup|PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|PrivilegedEligibilitySchedule.Read.AzureADGroup|PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be an owner or member of the group or be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
>
> - For role-assignable groups: *Global Reader* or *Privileged Role Administrator*
> - For non-role-assignable groups: *Global Reader*, *Directory Writer*, *Groups Administrator*, *Identity Governance Administrator*, or *User Administrator*
>
> The role assignments for the calling user should be scoped at the directory level.
> 
> Other roles with permissions to manage groups (such as Exchange Administrators for non-role-assignable Microsoft 365 groups) and administrators with assignments scoped at administrative unit level can manage groups through groups API and override changes made in Microsoft Entra PIM through PIM for Groups APIs.

## HTTP request

```http
GET /identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/{privilegedAccessGroupEligibilityScheduleRequestId}
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

If successful, this method returns a `200 OK` response code and a [privilegedAccessGroupEligibilityScheduleRequest](../resources/privilegedaccessgroupeligibilityschedulerequest.md) object in the response body.

## Examples

### Example 1: Get all eligibility schedule requests

#### Request
The following example shows a request.
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/534b3d4d-3ba0-8429-3568-5e9cce6c2cbd
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgIdentityGovernancePrivilegedAccessGroupEligibilityScheduleRequest -PrivilegedAccessGroupEligibilityScheduleRequestId $privilegedAccessGroupEligibilityScheduleRequestId

```

---

#### Response
The following example shows the response.

>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/$entity",
    "id": "534b3d4d-3ba0-8429-3568-5e9cce6c2cbd",
    "status": "Revoked",
    "completedDateTime": null,
    "createdDateTime": "2022-04-12T09:12:18.187Z",
    "approvalId": null,
    "customData": null,
    "createdBy": {
        "user": {
            "displayName": null,
            "id": "3fbd929d-8c56-4462-851e-0eb9a7b3a2a5"
        }
    },
    "action": "adminRemove",
    "isValidationOnly": false,
    "justification": null,
    "scheduleInfo": null,
    "ticketInfo": {
        "ticketNumber": null,
        "ticketSystem": null
    },
    "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
    "accessId": "member",
    "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
    "targetScheduleId": null
}
```

### Example 2: Get specific properties of all eligibility schedule requests

#### Request
The following example shows a request.
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/534b3d4d-3ba0-8429-3568-5e9cce6c2cbd?$select=principalId,action,groupId
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgIdentityGovernancePrivilegedAccessGroupEligibilityScheduleRequest -PrivilegedAccessGroupEligibilityScheduleRequestId $privilegedAccessGroupEligibilityScheduleRequestId -Property "principalId,action,groupId" 

```

---

#### Response
The following example shows the response.

>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/$entity",
    "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
    "action": "adminRemove",
    "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d"
}
```
