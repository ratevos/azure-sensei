# privilegedAccessGroupAssignmentScheduleRequest: updateRequest

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroupassignmentschedulerequest-updaterequest?view=graph-rest-1.0  
> Microsoft doc last updated: 09/16/2026


Namespace: microsoft.graph

Update a privilegedAccessGroupAssignmentScheduleRequest object with the result of a custom extension evaluation. This action is used to submit the result of a custom extension evaluation for a role assignment request.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup|Not available.|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup|Not available.|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be an owner or member of the group or be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
>
> - For role-assignable groups: *Privileged Role Administrator*
> - For non-role-assignable groups: *Directory Writer*, *Groups Administrator*, *Identity Governance Administrator*, or *User Administrator*
>
> The role assignments for the calling user should be scoped at the directory level.
>
> Other roles with permissions to manage groups (such as Exchange Administrators for non-role-assignable Microsoft 365 groups) and administrators with assignments scoped at administrative unit level can manage groups through groups API and override changes made in Microsoft Entra PIM through PIM for Groups APIs.

## HTTP request

```http
POST /identityGovernance/privilegedAccess/group/assignmentScheduleRequests/{privilegedAccessGroupAssignmentScheduleRequestId}/updateRequest
```

## Request headers

|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body

In the request body, provide a JSON object with the following parameters.

|Parameter|Type|Description|
|:---|:---|:---|
|evaluationId|String|The unique identifier of the custom extension evaluation. Optional.|
|evaluationOutcome|[evaluationOutcome](../resources/enums.md#evaluationoutcome-values)|The result of the custom extension evaluation. The possible values are: `approved`, `denied`, `unknownFutureValue`. Optional.|
|reason|String|The reason for the evaluation outcome. Optional.|
|scheduleInfo|[requestSchedule](../resources/requestschedule.md)|The updated schedule for the role assignment. Optional.|

## Response

If successful, this action returns a `200 OK` response code and a [privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) object in the response body.

## Example

### Request

The following example shows a request.

```http
POST https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/assignmentScheduleRequests/f4b57a8c-da56-4ae0-8aef-65c3a043dab4/updateRequest
Content-Type: application/json

{
  "evaluationId": "d4e5f6a7-b8c9-4d0e-9f1a-2b3c4d5e6f7a",
  "evaluationOutcome": "approved",
  "reason": "The ticket information is valid.",
  "scheduleInfo": {
    "startDateTime": "2026-09-16T19:00:00Z",
    "expiration": {
      "type": "afterDuration",
      "duration": "PT8H"
    }
  }
}
```

### Response

The following example shows the response. The response shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.type": "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest",
  "id": "f4b57a8c-da56-4ae0-8aef-65c3a043dab4",
  "status": "Granted",
  "action": "selfActivate",
  "principalId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
  "accessId": "member",
  "groupId": "55aa55aa-bb66-cc77-dd88-99ee99ee99ee",
  "justification": "Respond to the service incident"
}
```
