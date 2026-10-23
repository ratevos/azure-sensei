# privilegedAccessGroupEligibilitySchedule: filterByCurrentUser

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroupeligibilityschedule-filterbycurrentuser?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Retrieve schedules of membership and ownership eligibility requests for the calling principal.

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
GET /identityGovernance/privilegedAccess/group/eligibilitySchedules/filterByCurrentUser(on='parameterValue')
```

## Function parameters
In the request URL, provide the following query parameters with values.
The following table shows the parameters that must be used with this function.

|Parameter|Type|Description|
|:---|:---|:---|
|on|eligibilityScheduleFilterByCurrentUserOptions|Filter used to query eligibilitySchedules. The possible values are `principal`, `unknownFutureValue`. Required.|

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this function returns a `200 OK` response code and a [privilegedAccessGroupEligibilitySchedule](../resources/privilegedaccessgroupeligibilityschedule.md) collection in the response body.

## Examples
Note: this method requires either the principalId or groupId filter property.

### Example 1: Retrieve eligibility schedules for the calling principal

#### Request
The following example shows a request.
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilitySchedules/filterByCurrentUser(on='principal')
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Invoke-MgFilterIdentityGovernancePrivilegedAccessGroupEligibilityScheduleByCurrentUser -On $onId 

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(privilegedAccessGroupEligibilitySchedule)",
  "value": [
    {
      "@odata.type": "#microsoft.graph.privilegedAccessGroupEligibilitySchedule",
      "id": "14b9e371-5c2c-4ee5-a4a5-2980060d4f4e_member_f9003cf6-8905-4c69-a9f8-fd6d04caec69",
      "createdDateTime": "2022-03-14T19:26:07.06Z",
      "modifiedDateTime": "0001-01-01T08:00:00Z",
      "createdUsing": "f9003cf6-8905-4c69-a9f8-fd6d04caec69",
      "status": "Provisioned",
      "scheduleInfo": {
          "startDateTime": "2022-04-11T19:31:50.5613964Z",
          "recurrence": null,
          "expiration": {
              "type": "noExpiration",
              "endDateTime": null,
              "duration": null
          }
      },
      "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
      "accessId": "member",
      "groupId": "14b9e371-5c2c-4ee5-a4a5-2980060d4f4e",
      "memberType": "direct"
    }
  ]
}
```

### Example 2: Retrieve eligibility schedules for the principal and filter by a group and accessId

#### Request
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilitySchedules/filterByCurrentUser(on='principal')?$filter=groupId eq 'd5f0ad2e-6b34-401b-b6da-0c8fc2c5a3fc' and accessId eq 'member'
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Invoke-MgFilterIdentityGovernancePrivilegedAccessGroupEligibilityScheduleByCurrentUser -Filter "groupId eq 'd5f0ad2e-6b34-401b-b6da-0c8fc2c5a3fc' and accessId eq 'member'"  -On $onId 

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(privilegedAccessGroupEligibilitySchedule)",
  "value": [
  {
    "@odata.type": "#microsoft.graph.privilegedAccessGroupEligibilitySchedule",
    "id": "14b9e371-5c2c-4ee5-a4a5-2980060d4f4e_member_f9003cf6-8905-4c69-a9f8-fd6d04caec69",
    "createdDateTime": "2022-03-14T19:26:07.06Z",
    "modifiedDateTime": "0001-01-01T08:00:00Z",
    "createdUsing": "f9003cf6-8905-4c69-a9f8-fd6d04caec69",
    "status": "Provisioned",
    "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
    "accessId": "member",
    "groupId": "14b9e371-5c2c-4ee5-a4a5-2980060d4f4e",
    "memberType": "direct",
    "scheduleInfo": {
      "startDateTime": "2022-03-14T19:26:07.06Z",
      "recurrence": null,
      "expiration": {
        "type": "afterDateTime",
        "endDateTime": "2023-03-14T19:25:46.4Z",
        "duration": null
      }
    }
  }
  ]
}
```
