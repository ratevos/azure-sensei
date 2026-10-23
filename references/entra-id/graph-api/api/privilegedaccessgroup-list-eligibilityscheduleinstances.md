# List eligibilityScheduleInstances

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroup-list-eligibilityscheduleinstances?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Get a list of the [privilegedAccessGroupEligibilityScheduleInstance](../resources/privilegedaccessgroupeligibilityscheduleinstance.md) objects and their properties.

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
GET /identityGovernance/privilegedAccess/group/eligibilityScheduleInstances?$filter=groupId eq '{groupId}'
GET /identityGovernance/privilegedAccess/group/eligibilityScheduleInstances?filter=principalId eq '{principalId}'
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

If successful, this method returns a `200 OK` response code and a collection of [privilegedAccessGroupEligibilityScheduleInstance](../resources/privilegedaccessgroupeligibilityscheduleinstance.md) objects in the response body.

## Examples

### Request
The following example shows a request.
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilityScheduleInstances?$filter=groupId eq '2b5ed229-4072-478d-9504-a047ebd4b07d'
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgIdentityGovernancePrivilegedAccessGroupEligibilityScheduleInstance -Filter "groupId eq '2b5ed229-4072-478d-9504-a047ebd4b07d'" 

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/eligibilityScheduleInstances",
  "value": [
    {
      "id": "2b5ed229-4072-478d-9504-a047ebd4b07d_member_326a4063-93c5-4998-9537-969b8cd50297",
      "startDateTime": "2023-08-18T00:33:48.8Z",
      "endDateTime": null,
      "accessId": "member",
      "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
      "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
      "memberType": "Direct",
    },
    {
      "id": "2b5ed229-4072-478d-9504-a047ebd4b07d_owner_d663bb72-3781-4af0-b69b-01f2f0283a96",
      "startDateTime": "2023-09-06T18:18:03.917Z",
      "endDateTime": null,
      "accessId": "owner",
      "principalId": "56f2d212-e49c-42e3-8298-0188e5bef094",
      "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
      "memberType": "Direct",
    }
  ]
}
```
