# List eligibilitySchedules

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroup-list-eligibilityschedules?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Get a list of the [privilegedAccessGroupEligibilitySchedule](../resources/privilegedaccessgroupeligibilityschedule.md) objects and their properties.

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
GET /identityGovernance/privilegedAccess/group/eligibilitySchedules?$filter=groupId eq '{groupId}'
GET /identityGovernance/privilegedAccess/group/eligibilitySchedules?filter=principalId eq '{principalId}'
```

## Query parameters
This method requires the `$filter` (`eq`) query parameter to scope the request to a **principalId** or a **groupId**.

This method supports the `$select`, `$filter`, and `$expand` OData query parameters to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [privilegedAccessGroupEligibilitySchedule](../resources/privilegedaccessgroupeligibilityschedule.md) objects in the response body.

## Examples

### Example 1: Retrieve all eligibility schedules scoped to a group and a principal

#### Request
The following example shows a request.
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilitySchedules?$filter=groupId eq '2b5ed229-4072-478d-9504-a047ebd4b07d' and principalId eq '3cce9d87-3986-4f19-8335-7ed075408ca2'
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgIdentityGovernancePrivilegedAccessGroupEligibilitySchedule -Filter "groupId eq '2b5ed229-4072-478d-9504-a047ebd4b07d' and principalId eq '3cce9d87-3986-4f19-8335-7ed075408ca2'" 

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/eligibilitySchedules",
  "value": [
    {
      "id": "2b5ed229-4072-478d-9504-a047ebd4b07d_member_4cc1a00f-3e44-48ae-9bb5-fba55c9a7a5c",
      "scheduleInfo": {
          "startDateTime": "2022-04-12T14:44:50.287Z",
          "recurrence": null,
          "expiration": {
              "type": "afterDateTime",
              "endDateTime": "2024-04-10T00:00:00Z",
              "duration": null
          }
      },
      "createdUsing": "77f71919-62f3-4d0c-9f88-0a0391b665cd",
      "createdDateTime": "2022-04-12T14:44:50.287Z",
      "modifiedDateTime": "0001-01-01T08:00:00Z",
      "status": "Provisioned",
      "memberType": "Direct",
      "accessId": "member",
      "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
      "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
    }
  ]
}
```

### Example 2: Retrieve specific properties of all eligibility schedules scoped to a group and a principal

#### Request
The following example shows a request.
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilitySchedules?$filter=groupId eq '2b5ed229-4072-478d-9504-a047ebd4b07d' and principalId eq '3cce9d87-3986-4f19-8335-7ed075408ca2'&$select=accessId,principalId,groupId
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgIdentityGovernancePrivilegedAccessGroupEligibilitySchedule -Filter "groupId eq '2b5ed229-4072-478d-9504-a047ebd4b07d' and principalId eq '3cce9d87-3986-4f19-8335-7ed075408ca2'" -Property "accessId,principalId,groupId" 

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/eligibilitySchedules(accessId,principalId,groupId)",
  "value": [
    {
      "accessId": "member",
      "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
      "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
    }
  ]
}
```
