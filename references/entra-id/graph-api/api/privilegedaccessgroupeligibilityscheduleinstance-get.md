# Get privilegedAccessGroupEligibilityScheduleInstance

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroupeligibilityscheduleinstance-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Read the properties and relationships of a [privilegedAccessGroupEligibilityScheduleInstance](../resources/privilegedaccessgroupeligibilityscheduleinstance.md) object.

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
GET /identityGovernance/privilegedAccess/group/eligibilityScheduleInstances/{privilegedAccessGroupEligibilityScheduleInstanceId}
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

If successful, this method returns a `200 OK` response code and a [privilegedAccessGroupEligibilityScheduleInstance](../resources/privilegedaccessgroupeligibilityscheduleinstance.md) object in the response body.

## Examples

### Example 1: Get all eligibility schedule instances

#### Request
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilityScheduleInstances/d5f0ad2e-6b34-401b-b6da-0c8fc2c5a3fc
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgIdentityGovernancePrivilegedAccessGroupEligibilityScheduleInstance -PrivilegedAccessGroupEligibilityScheduleInstanceId $privilegedAccessGroupEligibilityScheduleInstanceId

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": {
    "@odata.type": "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance",
    "id": "b88fc7b0-a4ff-45fc-82c4-1d31a807315e",
    "accessId": "member",
    "principalId": "c277c8cb-6bb7-42e5-a17f-0add9a718151",
    "groupId": "d5f0ad2e-6b34-401b-b6da-0c8fc2c5a3fc",
    "startDateTime": "2020-08-27T18:58:35.967Z",
    "endDateTime": "2020-08-29T18:57:38Z",
    "memberType": "Direct",
    "memberEligibilityScheduleId": "04e755d8-488a-4abb-a27f-19091d73c970"
  }
}
```
