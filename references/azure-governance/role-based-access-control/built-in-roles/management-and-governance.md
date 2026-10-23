# Azure built-in roles for Management and governance - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/management-and-governance  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the Management and governance category.

## Advisor Recommendations Contributor (Assessments and Reviews)

View assessment recommendations, accepted review recommendations, and manage the recommendations lifecycle (mark recommendations as completed, postponed or dismissed, in progress, or not started).

[Learn more](https://learn.microsoft.com/en-us/azure/advisor/permissions)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/recommendations/read | Reads recommendations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/recommendations/write | Writes recommendations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/recommendations/available/action | New recommendation is available in Microsoft Advisor |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/conversations/* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "View assessment recommendations, accepted review recommendations, and manage the recommendations lifecycle (mark recommendations as completed, postponed or dismissed, in progress, or not started).",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/6b534d80-e337-47c4-864f-140f5c7f593d",
  "name": "6b534d80-e337-47c4-864f-140f5c7f593d",
  "permissions": [
    {
      "actions": [
        "Microsoft.Advisor/recommendations/read",
        "Microsoft.Advisor/recommendations/write",
        "Microsoft.Advisor/recommendations/available/action",
        "Microsoft.Advisor/conversations/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Advisor Recommendations Contributor (Assessments and Reviews)",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Advisor Reviews Contributor

View reviews for a workload and triage recommendations linked to them.

[Learn more](https://learn.microsoft.com/en-us/azure/advisor/permissions)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/resiliencyReviews/read | Read resiliencyReviews |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/triageRecommendations/read | Read triageRecommendations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/triageRecommendations/approve/action | Approve triageRecommendations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/triageRecommendations/reject/action | Reject triageRecommendations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/triageRecommendations/reset/action | Reset triageRecommendations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/triageResources/read | Read triageResources |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "View reviews for a workload and triage recommendations linked to them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/8aac15f0-d885-4138-8afa-bfb5872f7d13",
  "name": "8aac15f0-d885-4138-8afa-bfb5872f7d13",
  "permissions": [
    {
      "actions": [
        "Microsoft.Advisor/resiliencyReviews/read",
        "Microsoft.Advisor/triageRecommendations/read",
        "Microsoft.Advisor/triageRecommendations/approve/action",
        "Microsoft.Advisor/triageRecommendations/reject/action",
        "Microsoft.Advisor/triageRecommendations/reset/action",
        "Microsoft.Advisor/triageResources/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Advisor Reviews Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Advisor Reviews Reader

View reviews for a workload and recommendations linked to them.

[Learn more](https://learn.microsoft.com/en-us/azure/advisor/permissions)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/resiliencyReviews/read | Read resiliencyReviews |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/triageRecommendations/read | Read triageRecommendations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/triageResources/read | Read triageResources |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "View reviews for a workload and recommendations linked to them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/c64499e0-74c3-47ad-921c-13865957895c",
  "name": "c64499e0-74c3-47ad-921c-13865957895c",
  "permissions": [
    {
      "actions": [
        "Microsoft.Advisor/resiliencyReviews/read",
        "Microsoft.Advisor/triageRecommendations/read",
        "Microsoft.Advisor/triageResources/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Advisor Reviews Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Automation Contributor

Manage Azure Automation resources and other resources using Azure Automation.

[Learn more](https://learn.microsoft.com/en-us/azure/automation/automation-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/* |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/ActionGroups/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/ActivityLogAlerts/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/MetricAlerts/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/ScheduledQueryRules/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/diagnosticSettings/* | Creates, updates, or reads the diagnostic setting for Analysis Server |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedKeys/action | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Manage azure automation resources and other resources using azure automation.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/f353d9bd-d4a6-484e-a77a-8050b599b867",
  "name": "f353d9bd-d4a6-484e-a77a-8050b599b867",
  "permissions": [
    {
      "actions": [
        "Microsoft.Automation/automationAccounts/*",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "Microsoft.Insights/ActionGroups/*",
        "Microsoft.Insights/ActivityLogAlerts/*",
        "Microsoft.Insights/MetricAlerts/*",
        "Microsoft.Insights/ScheduledQueryRules/*",
        "Microsoft.Insights/diagnosticSettings/*",
        "Microsoft.OperationalInsights/workspaces/sharedKeys/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Automation Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Automation Job Operator

Create and Manage Jobs using Automation Runbooks.

[Learn more](https://learn.microsoft.com/en-us/azure/automation/automation-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/hybridRunbookWorkerGroups/read | Reads a Hybrid Runbook Worker Group |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/read | Gets an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/resume/action | Resumes an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/stop/action | Stops an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/streams/read | Gets an Azure Automation job stream |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/suspend/action | Suspends an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/write | Creates an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/output/read | Gets the output of a job |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Create and Manage Jobs using Automation Runbooks.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/4fe576fe-1146-4730-92eb-48519fa6bf9f",
  "name": "4fe576fe-1146-4730-92eb-48519fa6bf9f",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Automation/automationAccounts/hybridRunbookWorkerGroups/read",
        "Microsoft.Automation/automationAccounts/jobs/read",
        "Microsoft.Automation/automationAccounts/jobs/resume/action",
        "Microsoft.Automation/automationAccounts/jobs/stop/action",
        "Microsoft.Automation/automationAccounts/jobs/streams/read",
        "Microsoft.Automation/automationAccounts/jobs/suspend/action",
        "Microsoft.Automation/automationAccounts/jobs/write",
        "Microsoft.Automation/automationAccounts/jobs/output/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Automation Job Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Automation Operator

Automation Operators are able to start, stop, suspend, and resume jobs

[Learn more](https://learn.microsoft.com/en-us/azure/automation/automation-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/hybridRunbookWorkerGroups/read | Reads a Hybrid Runbook Worker Group |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/read | Gets an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/resume/action | Resumes an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/stop/action | Stops an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/streams/read | Gets an Azure Automation job stream |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/suspend/action | Suspends an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/write | Creates an Azure Automation job |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobSchedules/read | Gets an Azure Automation job schedule |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobSchedules/write | Creates an Azure Automation job schedule |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/linkedWorkspace/read | Gets the workspace linked to the automation account |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/read | Gets an Azure Automation account |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/runbooks/read | Gets an Azure Automation runbook |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/schedules/read | Gets an Azure Automation schedule asset |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/schedules/write | Creates or updates an Azure Automation schedule asset |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/jobs/output/read | Gets the output of a job |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Automation Operators are able to start, stop, suspend, and resume jobs",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/d3881f73-407a-4167-8283-e981cbba0404",
  "name": "d3881f73-407a-4167-8283-e981cbba0404",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Automation/automationAccounts/hybridRunbookWorkerGroups/read",
        "Microsoft.Automation/automationAccounts/jobs/read",
        "Microsoft.Automation/automationAccounts/jobs/resume/action",
        "Microsoft.Automation/automationAccounts/jobs/stop/action",
        "Microsoft.Automation/automationAccounts/jobs/streams/read",
        "Microsoft.Automation/automationAccounts/jobs/suspend/action",
        "Microsoft.Automation/automationAccounts/jobs/write",
        "Microsoft.Automation/automationAccounts/jobSchedules/read",
        "Microsoft.Automation/automationAccounts/jobSchedules/write",
        "Microsoft.Automation/automationAccounts/linkedWorkspace/read",
        "Microsoft.Automation/automationAccounts/read",
        "Microsoft.Automation/automationAccounts/runbooks/read",
        "Microsoft.Automation/automationAccounts/schedules/read",
        "Microsoft.Automation/automationAccounts/schedules/write",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Automation/automationAccounts/jobs/output/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Automation Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Automation Runbook Operator

Read Runbook properties - to be able to create Jobs of the runbook.

[Learn more](https://learn.microsoft.com/en-us/azure/automation/automation-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation)/automationAccounts/runbooks/read | Gets an Azure Automation runbook |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Read Runbook properties - to be able to create Jobs of the runbook.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5fb5aef8-1081-4b8e-bb16-9d5d0385bab5",
  "name": "5fb5aef8-1081-4b8e-bb16-9d5d0385bab5",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Automation/automationAccounts/runbooks/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Automation Runbook Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Center for SAP solutions administrator

This role provides read and write access to all capabilities of Azure Center for SAP solutions.

[Learn more](https://learn.microsoft.com/en-us/azure/sap/center-sap-solutions/manage-with-azure-rbac)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/configurations/read | Get configurations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/recommendations/read | Reads recommendations |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/sapvirtualInstances/*/read |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/sapVirtualInstances/*/write |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/sapVirtualInstances/*/delete |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/Locations/*/action |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/Locations/*/read |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/sapVirtualInstances/*/start/action |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/sapVirtualInstances/*/stop/action |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/connectors/*/read |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/connectors/*/write |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/connectors/*/delete |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricDefinitions/read | Read metric definitions |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/write | Creates or updates a resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/* |  |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read | Gets available metrics for the PingMesh |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/write | Creates a virtual network subnet or updates an existing virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/virtualMachines/read | Gets references to all the virtual machines in a virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/read | Gets a network interface definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/ipconfigurations/read | Gets a network interface ip configuration definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/loadBalancers/read | Gets all the load balancers that the network interface is part of |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/providers/Microsoft.Insights/metricDefinitions/read | Gets available metrics for the Network Interface |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/read | Gets a load balancer definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/backendAddressPools/read | Gets a load balancer backend address pool definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/frontendIPConfigurations/read | Gets a load balancer frontend IP configuration definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/loadBalancingRules/read | Gets a load balancer load balancing rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/inboundNatRules/read | Gets a load balancer inbound nat rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/providers/Microsoft.Insights/logDefinitions/read | Gets the events for Load Balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/networkInterfaces/read | Gets references to all the network interfaces under a load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/outboundRules/read | Gets a load balancer outbound rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/virtualMachines/read | Gets references to all the virtual machines under a load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/providers/Microsoft.Insights/metricDefinitions/read | Gets the available metrics for Load Balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/read | Gets an private endpoint resource. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/join/action | Joins a network security group. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/join/action | Joins a route table. Not Alertable. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/read | Returns the list of storage accounts or gets the properties for the specified storage account. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/blobServices/read | Returns blob service properties or statistics |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/blobServices/containers/read | Returns list of containers |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/read | Get file service properties |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/shares/read | List file shares |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/read | Get the properties of a virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/read | Get the properties of an availability set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/sshPublicKeys/read | Get the properties of an SSH public key |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/sshPublicKeys/write | Creates a new SSH public key or updates an existing SSH public key |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/sshPublicKeys/*/generateKeyPair/action |  |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/extensions/read | Get the properties of a virtual machine extension |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/extensions/delete | Deletes the virtual machine extension |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/read | Get the properties of a Disk |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/blobServices/containers/blobs/read | Returns a blob or a list of blobs |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "This role provides read and write access to all capabilities of Azure Center for SAP solutions.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/7b0c7e81-271f-4c71-90bf-e30bdfdbc2f7",
  "name": "7b0c7e81-271f-4c71-90bf-e30bdfdbc2f7",
  "permissions": [
    {
      "actions": [
        "Microsoft.Advisor/configurations/read",
        "Microsoft.Advisor/recommendations/read",
        "Microsoft.Workloads/sapvirtualInstances/*/read",
        "Microsoft.Workloads/sapVirtualInstances/*/write",
        "Microsoft.Workloads/sapVirtualInstances/*/delete",
        "Microsoft.Workloads/Locations/*/action",
        "Microsoft.Workloads/Locations/*/read",
        "Microsoft.Workloads/sapVirtualInstances/*/start/action",
        "Microsoft.Workloads/sapVirtualInstances/*/stop/action",
        "Microsoft.Workloads/connectors/*/read",
        "Microsoft.Workloads/connectors/*/write",
        "Microsoft.Workloads/connectors/*/delete",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Insights/metrics/read",
        "Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/write",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/virtualNetworks/subnets/write",
        "Microsoft.Network/virtualNetworks/subnets/virtualMachines/read",
        "Microsoft.Network/networkInterfaces/read",
        "Microsoft.Network/networkInterfaces/ipconfigurations/read",
        "Microsoft.Network/networkInterfaces/loadBalancers/read",
        "Microsoft.Network/networkInterfaces/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/loadBalancers/read",
        "Microsoft.Network/loadBalancers/backendAddressPools/read",
        "Microsoft.Network/loadBalancers/frontendIPConfigurations/read",
        "Microsoft.Network/loadBalancers/loadBalancingRules/read",
        "Microsoft.Network/loadBalancers/inboundNatRules/read",
        "Microsoft.Network/loadBalancers/providers/Microsoft.Insights/logDefinitions/read",
        "Microsoft.Network/loadBalancers/networkInterfaces/read",
        "Microsoft.Network/loadBalancers/outboundRules/read",
        "Microsoft.Network/loadBalancers/virtualMachines/read",
        "Microsoft.Network/loadBalancers/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/privateEndpoints/read",
        "Microsoft.Network/networkSecurityGroups/join/action",
        "Microsoft.Network/routeTables/join/action",
        "Microsoft.Storage/storageAccounts/read",
        "Microsoft.Storage/storageAccounts/blobServices/read",
        "Microsoft.Storage/storageAccounts/blobServices/containers/read",
        "Microsoft.Storage/storageAccounts/fileServices/read",
        "Microsoft.Storage/storageAccounts/fileServices/shares/read",
        "Microsoft.Compute/virtualMachines/read",
        "Microsoft.Compute/availabilitySets/read",
        "Microsoft.Compute/sshPublicKeys/read",
        "Microsoft.Compute/sshPublicKeys/write",
        "Microsoft.Compute/sshPublicKeys/*/generateKeyPair/action",
        "Microsoft.Compute/virtualMachines/extensions/read",
        "Microsoft.Compute/virtualMachines/extensions/delete",
        "Microsoft.Compute/disks/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Center for SAP solutions administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Center for SAP solutions reader

This role provides read access to all capabilities of Azure Center for SAP solutions.

[Learn more](https://learn.microsoft.com/en-us/azure/sap/center-sap-solutions/manage-with-azure-rbac)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/configurations/read | Get configurations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/recommendations/read | Reads recommendations |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/sapvirtualInstances/*/read |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/Locations/*/read |  |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/Operations/read | read Operations |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads)/Locations/OperationStatuses/read | read OperationStatuses |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricDefinitions/read | Read metric definitions |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/read | Gets or lists deployments. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read | Gets available metrics for the PingMesh |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/virtualMachines/read | Gets references to all the virtual machines in a virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/read | Gets a network interface definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/ipconfigurations/read | Gets a network interface ip configuration definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/loadBalancers/read | Gets all the load balancers that the network interface is part of |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/providers/Microsoft.Insights/metricDefinitions/read | Gets available metrics for the Network Interface |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/read | Gets a load balancer definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/backendAddressPools/read | Gets a load balancer backend address pool definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/frontendIPConfigurations/read | Gets a load balancer frontend IP configuration definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/loadBalancingRules/read | Gets a load balancer load balancing rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/inboundNatRules/read | Gets a load balancer inbound nat rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/providers/Microsoft.Insights/logDefinitions/read | Gets the events for Load Balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/networkInterfaces/read | Gets references to all the network interfaces under a load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/outboundRules/read | Gets a load balancer outbound rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/virtualMachines/read | Gets references to all the virtual machines under a load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/providers/Microsoft.Insights/metricDefinitions/read | Gets the available metrics for Load Balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/read | Gets an private endpoint resource. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/read | Returns the list of storage accounts or gets the properties for the specified storage account. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/blobServices/read | Returns blob service properties or statistics |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/blobServices/containers/read | Returns list of containers |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/read | Get file service properties |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/shares/read | List file shares |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/read | Get the properties of a virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/read | Get the properties of an availability set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/extensions/read | Get the properties of a virtual machine extension |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/read | Get the properties of a Disk |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "This role provides read access to all capabilities of Azure Center for SAP solutions.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/05352d14-a920-4328-a0de-4cbe7430e26b",
  "name": "05352d14-a920-4328-a0de-4cbe7430e26b",
  "permissions": [
    {
      "actions": [
        "Microsoft.Advisor/configurations/read",
        "Microsoft.Advisor/recommendations/read",
        "Microsoft.Workloads/sapvirtualInstances/*/read",
        "Microsoft.Workloads/Locations/*/read",
        "Microsoft.Workloads/Operations/read",
        "Microsoft.Workloads/Locations/OperationStatuses/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Insights/alertRules/read",
        "Microsoft.Insights/metrics/read",
        "Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/virtualNetworks/subnets/virtualMachines/read",
        "Microsoft.Network/networkInterfaces/read",
        "Microsoft.Network/networkInterfaces/ipconfigurations/read",
        "Microsoft.Network/networkInterfaces/loadBalancers/read",
        "Microsoft.Network/networkInterfaces/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/loadBalancers/read",
        "Microsoft.Network/loadBalancers/backendAddressPools/read",
        "Microsoft.Network/loadBalancers/frontendIPConfigurations/read",
        "Microsoft.Network/loadBalancers/loadBalancingRules/read",
        "Microsoft.Network/loadBalancers/inboundNatRules/read",
        "Microsoft.Network/loadBalancers/providers/Microsoft.Insights/logDefinitions/read",
        "Microsoft.Network/loadBalancers/networkInterfaces/read",
        "Microsoft.Network/loadBalancers/outboundRules/read",
        "Microsoft.Network/loadBalancers/virtualMachines/read",
        "Microsoft.Network/loadBalancers/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/privateEndpoints/read",
        "Microsoft.Storage/storageAccounts/read",
        "Microsoft.Storage/storageAccounts/blobServices/read",
        "Microsoft.Storage/storageAccounts/blobServices/containers/read",
        "Microsoft.Storage/storageAccounts/fileServices/read",
        "Microsoft.Storage/storageAccounts/fileServices/shares/read",
        "Microsoft.Compute/virtualMachines/read",
        "Microsoft.Compute/availabilitySets/read",
        "Microsoft.Compute/virtualMachines/extensions/read",
        "Microsoft.Compute/disks/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Center for SAP solutions reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Center for SAP solutions service role

Azure Center for SAP solutions service role - This role is intended to be used for providing the permissions to user assigned managed identity. Azure Center for SAP solutions will use this identity to deploy and manage SAP systems.

[Learn more](https://learn.microsoft.com/en-us/azure/sap/center-sap-solutions/manage-with-azure-rbac)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/write | Creates or updates a resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/* |  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/read | Gets a load balancer definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/write | Creates a load balancer or updates an existing load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/backendAddressPools/read | Gets a load balancer backend address pool definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/backendAddressPools/write | Creates a load balancer backend address pool or updates an existing load balancer backend address pool |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/frontendIPConfigurations/read | Gets a load balancer frontend IP configuration definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/loadBalancingRules/read | Gets a load balancer load balancing rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/inboundNatRules/read | Gets a load balancer inbound nat rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/providers/Microsoft.Insights/logDefinitions/read | Gets the events for Load Balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/networkInterfaces/read | Gets references to all the network interfaces under a load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/outboundRules/read | Gets a load balancer outbound rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/virtualMachines/read | Gets references to all the virtual machines under a load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/providers/Microsoft.Insights/metricDefinitions/read | Gets the available metrics for Load Balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/read | Gets a network interface definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/write | Creates a network interface or updates an existing network interface.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/ipconfigurations/read | Gets a network interface ip configuration definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/loadBalancers/read | Gets all the load balancers that the network interface is part of |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/checkIpAddressAvailability/read | Check if IP Address is available at the specified virtual network |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/virtualMachines/read | Gets references to all the virtual machines in a virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/virtualMachines/read | Gets references to all the virtual machines in a virtual network |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/ipconfigurations/join/action | Joins a Network Interface IP Configuration. Not alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/read | Gets an private endpoint resource. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/write | Creates a new private endpoint, or updates an existing private endpoint. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/join/action | Joins a Virtual Machine to a network interface. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/backendAddressPools/join/action | Joins a load balancer backend address pool. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/frontendIPConfigurations/join/action | Joins a Load Balancer Frontend IP Configuration. Not alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/joinLoadBalancer/action | Joins a load balancer to virtual network subnets |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/read | Returns the list of storage accounts or gets the properties for the specified storage account. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/write | Creates a storage account with the specified parameters or update the properties or tags or adds custom domain for the specified storage account. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/PrivateEndpointConnectionsApproval/action | Approve Private Endpoint Connections |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/blobServices/read | Returns blob service properties or statistics |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/blobServices/containers/read | Returns list of containers |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/read | Get file service properties |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/write | Put file service properties |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/shares/read | List file shares |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/fileServices/shares/write | Create or update file share |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/read | Get the properties of a virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/write | Creates a new virtual machine or updates an existing virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/instanceView/read | Gets the detailed runtime status of the virtual machine and its resources |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/read | Get the properties of an availability set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/write | Creates a new availability set or updates an existing one |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/skus/read | Gets the list of Microsoft.Compute SKUs available for your Subscription |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/sshPublicKeys/read | Get the properties of an SSH public key |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/extensions/read | Get the properties of a virtual machine extension |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/extensions/write | Creates a new virtual machine extension or updates an existing one |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/extensions/delete | Deletes the virtual machine extension |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/read | Get the properties of a Disk |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/write | Creates a new Disk or updates an existing one |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Azure Center for SAP solutions service role - This role is intended to be used for providing the permissions to user assigned managed identity. Azure Center for SAP solutions will use this identity to deploy and manage SAP systems.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/aabbc5dd-1af0-458b-a942-81af88f9c138",
  "name": "aabbc5dd-1af0-458b-a942-81af88f9c138",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/write",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/*",
        "Microsoft.Network/loadBalancers/read",
        "Microsoft.Network/loadBalancers/write",
        "Microsoft.Network/loadBalancers/backendAddressPools/read",
        "Microsoft.Network/loadBalancers/backendAddressPools/write",
        "Microsoft.Network/loadBalancers/frontendIPConfigurations/read",
        "Microsoft.Network/loadBalancers/loadBalancingRules/read",
        "Microsoft.Network/loadBalancers/inboundNatRules/read",
        "Microsoft.Network/loadBalancers/providers/Microsoft.Insights/logDefinitions/read",
        "Microsoft.Network/loadBalancers/networkInterfaces/read",
        "Microsoft.Network/loadBalancers/outboundRules/read",
        "Microsoft.Network/loadBalancers/virtualMachines/read",
        "Microsoft.Network/loadBalancers/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/networkInterfaces/read",
        "Microsoft.Network/networkInterfaces/write",
        "Microsoft.Network/networkInterfaces/ipconfigurations/read",
        "Microsoft.Network/networkInterfaces/loadBalancers/read",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/checkIpAddressAvailability/read",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/virtualNetworks/subnets/virtualMachines/read",
        "Microsoft.Network/virtualNetworks/virtualMachines/read",
        "Microsoft.Network/networkInterfaces/ipconfigurations/join/action",
        "Microsoft.Network/privateEndpoints/read",
        "Microsoft.Network/privateEndpoints/write",
        "Microsoft.Network/networkInterfaces/join/action",
        "Microsoft.Network/loadBalancers/backendAddressPools/join/action",
        "Microsoft.Network/loadBalancers/frontendIPConfigurations/join/action",
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/virtualNetworks/subnets/joinLoadBalancer/action",
        "Microsoft.Storage/storageAccounts/read",
        "Microsoft.Storage/storageAccounts/write",
        "Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action",
        "Microsoft.Storage/storageAccounts/blobServices/read",
        "Microsoft.Storage/storageAccounts/blobServices/containers/read",
        "Microsoft.Storage/storageAccounts/fileServices/read",
        "Microsoft.Storage/storageAccounts/fileServices/write",
        "Microsoft.Storage/storageAccounts/fileServices/shares/read",
        "Microsoft.Storage/storageAccounts/fileServices/shares/write",
        "Microsoft.Compute/virtualMachines/read",
        "Microsoft.Compute/virtualMachines/write",
        "Microsoft.Compute/virtualMachines/instanceView/read",
        "Microsoft.Compute/availabilitySets/read",
        "Microsoft.Compute/availabilitySets/write",
        "Microsoft.Compute/skus/read",
        "Microsoft.Compute/sshPublicKeys/read",
        "Microsoft.Compute/virtualMachines/extensions/read",
        "Microsoft.Compute/virtualMachines/extensions/write",
        "Microsoft.Compute/virtualMachines/extensions/delete",
        "Microsoft.Compute/disks/read",
        "Microsoft.Compute/disks/write"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Center for SAP solutions service role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Connected Machine Onboarding

Can onboard Azure Connected Machines.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-arc/servers/onboard-service-principal)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/read | Reads any Azure Arc settings |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/write | Writes an Azure Arc settings |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/read | Reads any Azure Arc gateways |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/privateLinkScopes/read | Read any Azure Arc privateLinkScopes |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/guestConfigurationAssignments/read | Get guest configuration assignment. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRuleAssociations/write | Create or update a resource's association with a data collection rule |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRuleAssociations/delete | Delete a resource's association with a data collection rule |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRuleAssociations/read | Read a resource's association with a data collection rule |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/addExtensions/action | Setup Extensions on Azure Arc machines |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can onboard Azure Connected Machines.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/b64e21ea-ac4e-4cdf-9dc9-5b892992bee7",
  "name": "b64e21ea-ac4e-4cdf-9dc9-5b892992bee7",
  "permissions": [
    {
      "actions": [
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/settings/read",
        "Microsoft.HybridCompute/settings/write",
        "Microsoft.HybridCompute/gateways/read",
        "Microsoft.HybridCompute/privateLinkScopes/read",
        "Microsoft.GuestConfiguration/guestConfigurationAssignments/read",
        "Microsoft.Insights/dataCollectionRuleAssociations/write",
        "Microsoft.Insights/dataCollectionRuleAssociations/delete",
        "Microsoft.Insights/dataCollectionRuleAssociations/read",
        "Microsoft.HybridCompute/machines/addExtensions/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Connected Machine Onboarding",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Connected Machine Resource Administrator

Can read, write, delete and re-onboard Azure Connected Machines.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-arc/servers/security-overview)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runCommands/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/UpgradeExtensions/action | Upgrades Extensions on Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/privateLinkScopes/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/*/read |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can read, write, delete and re-onboard Azure Connected Machines.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/cd570a14-e51a-42ad-bac8-bafd67325302",
  "name": "cd570a14-e51a-42ad-bac8-bafd67325302",
  "permissions": [
    {
      "actions": [
        "Microsoft.HybridCompute/machines/*",
        "Microsoft.HybridCompute/machines/extensions/*",
        "Microsoft.HybridCompute/machines/licenseProfiles/*",
        "Microsoft.HybridCompute/machines/runCommands/*",
        "Microsoft.HybridCompute/machines/UpgradeExtensions/action",
        "Microsoft.HybridCompute/settings/*",
        "Microsoft.HybridCompute/gateways/*",
        "Microsoft.HybridCompute/privateLinkScopes/*",
        "Microsoft.HybridCompute/licenses/*",
        "Microsoft.HybridCompute/locations/*",
        "Microsoft.HybridCompute/*/read",
        "Microsoft.Resources/deployments/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Connected Machine Resource Administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Connected Machine Resource Manager

Custom role for Azure Local resource provider (Microsoft.AzureStackHCI Resource Provider) to manage hybrid compute machines and hybrid connectivity endpoints in a resource group

[Learn more](https://learn.microsoft.com/en-us/azure-stack/hci/deploy/deployment-azure-resource-manager-template)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/guestConfigurationAssignments/*/read |  |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/guestConfigurationAssignments/read | Get guest configuration assignment. |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/guestConfigurationAssignments/write | Create new guest configuration assignment. |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/*/read |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/delete | Deletes an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/write | Installs or Updates an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/delete | Deletes an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/read | Reads any Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/write | Installs or Updates an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/UpgradeExtensions/action | Upgrades Extensions on Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/endpoints/read | Gets the endpoint to the resource. |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/endpoints/serviceConfigurations/read | Gets the details about the service to the resource. |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/endpoints/serviceConfigurations/write | Update the service details in the service configurations of the target resource. |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/endpoints/write | Update the endpoint to the target resource. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.EdgeMarketplace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace)/locations/operationStatuses/read | read operationStatuses |
> | [Microsoft.EdgeMarketPlace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace)/offers/getAccessToken/action | get access token. |
> | [Microsoft.EdgeMarketPlace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace)/offers/generateAccessToken/action | A long-running resource action. |
> | [Microsoft.EdgeMarketplace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace)/publishers/read | List Publisher resources by parent |
> | [Microsoft.EdgeMarketplace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace)/offers/read | List Offer resources by parent |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/read | Gets an Custom Location resource |
> | [Microsoft.Attestation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftattestation)/attestationProviders/write | Adds attestation service. |
> | [Microsoft.Attestation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftattestation)/attestationProviders/read | Gets the attestation service status. |
> | [Microsoft.Attestation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftattestation)/attestationProviders/delete | Removes attestation service. |
> | [Microsoft.Attestation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftattestation)/attestationProviders/attestation/read | Gets the attestation service status. |
> | [Microsoft.Attestation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftattestation)/attestationProviders/attestation/write | Adds attestation service. |
> | [Microsoft.Attestation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftattestation)/attestationProviders/attestation/delete | Removes attestation service. |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/read | Reads any Azure Arc settings |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/write | Writes an Azure Arc settings |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Custom Role for AzureStackHCI RP to manage hybrid compute machines and hybrid connectivity endpoints in a resource group",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/f5819b54-e033-4d82-ac66-4fec3cbf3f4c",
  "name": "f5819b54-e033-4d82-ac66-4fec3cbf3f4c",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.GuestConfiguration/guestConfigurationAssignments/*/read",
        "Microsoft.GuestConfiguration/guestConfigurationAssignments/read",
        "Microsoft.GuestConfiguration/guestConfigurationAssignments/write",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/extensions/read",
        "Microsoft.HybridCompute/*/read",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/machines/extensions/delete",
        "Microsoft.HybridCompute/machines/extensions/write",
        "Microsoft.HybridCompute/machines/licenseProfiles/delete",
        "Microsoft.HybridCompute/machines/licenseProfiles/read",
        "Microsoft.HybridCompute/machines/licenseProfiles/write",
        "Microsoft.HybridCompute/machines/UpgradeExtensions/action",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridConnectivity/endpoints/read",
        "Microsoft.HybridConnectivity/endpoints/serviceConfigurations/read",
        "Microsoft.HybridConnectivity/endpoints/serviceConfigurations/write",
        "Microsoft.HybridConnectivity/endpoints/write",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.EdgeMarketplace/locations/operationStatuses/read",
        "Microsoft.EdgeMarketPlace/offers/getAccessToken/action",
        "Microsoft.EdgeMarketPlace/offers/generateAccessToken/action",
        "Microsoft.EdgeMarketplace/publishers/read",
        "Microsoft.EdgeMarketplace/offers/read",
        "Microsoft.ExtendedLocation/customLocations/read",
        "Microsoft.Attestation/attestationProviders/write",
        "Microsoft.Attestation/attestationProviders/read",
        "Microsoft.Attestation/attestationProviders/delete",
        "Microsoft.Attestation/attestationProviders/attestation/read",
        "Microsoft.Attestation/attestationProviders/attestation/write",
        "Microsoft.Attestation/attestationProviders/attestation/delete",
        "Microsoft.HybridCompute/settings/read",
        "Microsoft.HybridCompute/settings/write"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Connected Machine Resource Manager",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Customer Lockbox Approver for Subscription

Can approve Microsoft support requests to access specific resources contained within a subscription, or the subscription itself, when Customer Lockbox for Microsoft Azure is enabled on the tenant where the subscription resides.

[Learn more](https://learn.microsoft.com/en-us/azure/security/fundamentals/customer-lockbox-overview)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.CustomerLockbox](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcustomerlockbox)/requests/UpdateApproval/action | Update Approval Microsoft.CustomerLockbox |
> | [Microsoft.CustomerLockbox](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcustomerlockbox)/requests/read | Read Lockbox Request |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/eventtypes/values/read | Read Activity Log events |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can approve Microsoft support requests to access specific resources contained within a subscription, or the subscription itself, when Customer Lockbox for Microsoft Azure is enabled on the tenant where the subscription resides.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/4dae6930-7baf-46f5-909e-0383bc931c46",
  "name": "4dae6930-7baf-46f5-909e-0383bc931c46",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.CustomerLockbox/requests/UpdateApproval/action",
        "Microsoft.CustomerLockbox/requests/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Insights/eventtypes/values/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Customer Lockbox Approver for Subscription",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Billing Reader

Allows read access to billing data

[Learn more](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-billing-access)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Billing](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbilling)/*/read | Read Billing information |
> | [Microsoft.Commerce](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcommerce)/*/read |  |
> | [Microsoft.Consumption](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftconsumption)/*/read |  |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/read | List management groups for the authenticated user. |
> | [Microsoft.CostManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcostmanagement)/*/read |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows read access to billing data",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/fa23ad8b-c56e-40d8-ac0c-ce449e1d2c64",
  "name": "fa23ad8b-c56e-40d8-ac0c-ce449e1d2c64",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Billing/*/read",
        "Microsoft.Commerce/*/read",
        "Microsoft.Consumption/*/read",
        "Microsoft.Management/managementGroups/read",
        "Microsoft.CostManagement/*/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Billing Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Blueprint Contributor

Can manage blueprint definitions, but not assign them.

[Learn more](https://learn.microsoft.com/en-us/azure/governance/blueprints/overview)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Blueprint](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftblueprint)/blueprints/* | Create and manage blueprint definitions or blueprint artifacts. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can manage blueprint definitions, but not assign them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/41077137-e803-4205-871c-5a86e6a753b4",
  "name": "41077137-e803-4205-871c-5a86e6a753b4",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Blueprint/blueprints/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Blueprint Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Blueprint Operator

Can assign existing published blueprints, but cannot create new blueprints. Note that this only works if the assignment is done with a user-assigned managed identity.

[Learn more](https://learn.microsoft.com/en-us/azure/governance/blueprints/overview)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Blueprint](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftblueprint)/blueprintAssignments/* | Create and manage blueprint assignments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can assign existing published blueprints, but cannot create new blueprints. NOTE: this only works if the assignment is done with a user-assigned managed identity.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/437d2ced-4a38-4302-8479-ed2bcb43d090",
  "name": "437d2ced-4a38-4302-8479-ed2bcb43d090",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Blueprint/blueprintAssignments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Blueprint Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Carbon Optimization Reader

Allow read access to Azure Carbon Optimization data

[Learn more](https://learn.microsoft.com/en-us/azure/carbon-optimization/permissions)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Carbon](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcarbon)/carbonEmissionReports/action | API for Carbon Emissions Reports |
> | [Microsoft.Carbon](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcarbon)/carbonEmissionReports/read | API for Carbon Emissions Reports |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allow read access to Azure Carbon Optimization data",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/fa0d39e6-28e5-40cf-8521-1eb320653a4c",
  "name": "fa0d39e6-28e5-40cf-8521-1eb320653a4c",
  "permissions": [
    {
      "actions": [
        "Microsoft.Carbon/carbonEmissionReports/action",
        "Microsoft.Carbon/carbonEmissionReports/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Carbon Optimization Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Cost Management Contributor

Can view costs and manage cost configuration (e.g. budgets, exports)

[Learn more](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Consumption](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftconsumption)/* |  |
> | [Microsoft.CostManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcostmanagement)/* |  |
> | [Microsoft.Billing](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbilling)/billingPeriods/read |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/configurations/read | Get configurations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/recommendations/read | Reads recommendations |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/read | List management groups for the authenticated user. |
> | [Microsoft.Billing](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbilling)/billingProperty/read | Gets the billing properties for a subscription |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can view costs and manage cost configuration (e.g. budgets, exports)",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/434105ed-43f6-45c7-a02f-909b2ba83430",
  "name": "434105ed-43f6-45c7-a02f-909b2ba83430",
  "permissions": [
    {
      "actions": [
        "Microsoft.Consumption/*",
        "Microsoft.CostManagement/*",
        "Microsoft.Billing/billingPeriods/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "Microsoft.Advisor/configurations/read",
        "Microsoft.Advisor/recommendations/read",
        "Microsoft.Management/managementGroups/read",
        "Microsoft.Billing/billingProperty/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Cost Management Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Cost Management Reader

Can view cost data and configuration (e.g. budgets, exports)

[Learn more](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Consumption](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftconsumption)/*/read |  |
> | [Microsoft.CostManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcostmanagement)/*/read |  |
> | [Microsoft.Billing](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbilling)/billingPeriods/read |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/configurations/read | Get configurations |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor)/recommendations/read | Reads recommendations |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/read | List management groups for the authenticated user. |
> | [Microsoft.Billing](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbilling)/billingProperty/read | Gets the billing properties for a subscription |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can view cost data and configuration (e.g. budgets, exports)",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/72fafb9e-0641-4937-9268-a91bfd8191a3",
  "name": "72fafb9e-0641-4937-9268-a91bfd8191a3",
  "permissions": [
    {
      "actions": [
        "Microsoft.Consumption/*/read",
        "Microsoft.CostManagement/*/read",
        "Microsoft.Billing/billingPeriods/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "Microsoft.Advisor/configurations/read",
        "Microsoft.Advisor/recommendations/read",
        "Microsoft.Management/managementGroups/read",
        "Microsoft.Billing/billingProperty/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Cost Management Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Essential Machine Management Administrator

Can managed Essential Machine Management resources for subscriptions

[Learn more](https://learn.microsoft.com/en-us/azure/operations/configuration-enrollment)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRules/read | Read a data collection rule |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRules/write | Create or update a data collection rule |
> | [Microsoft.Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor)/accounts/write | Create or Update any Monitoring Account |
> | [Microsoft.Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor)/accounts/read | Read any Monitoring Account |
> | [Microsoft.ManagedOps](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedops)/managedOps/read | List all ManagedOps instances in the subscription. |
> | [Microsoft.ManagedOps](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedops)/managedOps/write | Creates or updates the ManagedOps instance. |
> | [Microsoft.ManagedOps](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedops)/managedOps/delete | Deletes the ManagedOps instance. |
> | [Microsoft.OperationsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationsmanagement)/solutions/read | Get existing OMS solution |
> | [Microsoft.OperationsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationsmanagement)/solutions/write | Create new OMS solution |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/read | Gets an existing workspace |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedkeys/action | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedkeys/read | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/listKeys/action | Retrieves the list keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricAlerts/write | Create or update a metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricAlerts/read | Read a metric alert |
> | [Microsoft.Security](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftsecurity)/pricings/write | Updates the pricing settings for the scope |
> | [Microsoft.Security](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftsecurity)/pricings/read | Gets the pricing settings for the scope |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Can managed Essential Machine Management resources for subscriptions",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/34013b0a-565b-43aa-8755-1b7c286f6cf7",
  "name": "34013b0a-565b-43aa-8755-1b7c286f6cf7",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/deployments/*",
        "Microsoft.Insights/dataCollectionRules/read",
        "Microsoft.Insights/dataCollectionRules/write",
        "Microsoft.Monitor/accounts/write",
        "Microsoft.Monitor/accounts/read",
        "Microsoft.ManagedOps/managedOps/read",
        "Microsoft.ManagedOps/managedOps/write",
        "Microsoft.ManagedOps/managedOps/delete",
        "Microsoft.OperationsManagement/solutions/read",
        "Microsoft.OperationsManagement/solutions/write",
        "Microsoft.OperationalInsights/workspaces/read",
        "Microsoft.OperationalInsights/workspaces/sharedkeys/action",
        "Microsoft.OperationalInsights/workspaces/sharedkeys/read",
        "Microsoft.OperationalInsights/workspaces/listKeys/action",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Insights/metricAlerts/write",
        "Microsoft.Insights/metricAlerts/read",
        "Microsoft.Security/pricings/write",
        "Microsoft.Security/pricings/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Essential Machine Management Administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Hierarchy Settings Administrator

Allows users to edit and delete Hierarchy Settings

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/settings/write | Creates or updates management group hierarchy settings. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/settings/delete | Deletes management group hierarchy settings. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows users to edit and delete Hierarchy Settings",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/350f8d15-c687-4448-8ae1-157740a3936d",
  "name": "350f8d15-c687-4448-8ae1-157740a3936d",
  "permissions": [
    {
      "actions": [
        "Microsoft.Management/managementGroups/settings/write",
        "Microsoft.Management/managementGroups/settings/delete"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Hierarchy Settings Administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Managed Application Contributor Role

Allows for creating managed application resources.

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.Solutions](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftsolutions)/applications/* |  |
> | [Microsoft.Solutions](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftsolutions)/register/action | Register the subscription for Microsoft.Solutions |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/* |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows for creating managed application resources.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/641177b8-a67a-45b9-a033-47bc880bb21e",
  "name": "641177b8-a67a-45b9-a033-47bc880bb21e",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.Solutions/applications/*",
        "Microsoft.Solutions/register/action",
        "Microsoft.Resources/subscriptions/resourceGroups/*",
        "Microsoft.Resources/deployments/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Managed Application Contributor Role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Managed Application Operator Role

Lets you read and perform actions on Managed Application resources

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.Solutions](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftsolutions)/applications/read | Lists all the applications within a subscription. |
> | [Microsoft.Solutions](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftsolutions)/*/action |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you read and perform actions on Managed Application resources",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/c7393b34-138c-406f-901b-d8cf2b17e6ae",
  "name": "c7393b34-138c-406f-901b-d8cf2b17e6ae",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.Solutions/applications/read",
        "Microsoft.Solutions/*/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Managed Application Operator Role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Managed Application Publisher Operator

Allows the publisher to read resources in the managed resource group for Managed Application and request JIT access for additional operations. This role is only used by the Managed Application service to provide access to publishers.

This role was previously named Managed Applications Reader.

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Solutions](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftsolutions)/jitRequests/* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows the publisher to read resources in the managed resource group for Managed Application and request JIT access for additional operations. This role is only used by the Managed Application service to provide access to publishers.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/b9331d33-8a36-4f8c-b097-4f54124fdb44",
  "name": "b9331d33-8a36-4f8c-b097-4f54124fdb44",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Solutions/jitRequests/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Managed Application Publisher Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Managed Services Registration assignment Delete Role

Managed Services Registration Assignment Delete Role allows the managing tenant users to delete the registration assignment assigned to their tenant.

[Learn more](https://learn.microsoft.com/en-us/azure/lighthouse/how-to/remove-delegation)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.ManagedServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedservices)/registrationAssignments/read | Retrieves a list of Managed Services registration assignments. |
> | [Microsoft.ManagedServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedservices)/registrationAssignments/delete | Removes Managed Services registration assignment. |
> | [Microsoft.ManagedServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedservices)/operationStatuses/read | Reads the operation status for the resource. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Managed Services Registration Assignment Delete Role allows the managing tenant users to delete the registration assignment assigned to their tenant.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/91c1777a-f3dc-4fae-b103-61d183457e46",
  "name": "91c1777a-f3dc-4fae-b103-61d183457e46",
  "permissions": [
    {
      "actions": [
        "Microsoft.ManagedServices/registrationAssignments/read",
        "Microsoft.ManagedServices/registrationAssignments/delete",
        "Microsoft.ManagedServices/operationStatuses/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Managed Services Registration assignment Delete Role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Management Group Contributor

Management Group Contributor Role

[Learn more](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/delete | Delete management group. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/read | List management groups for the authenticated user. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/subscriptions/delete | De-associates subscription from the management group. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/subscriptions/write | Associates existing subscription with the management group. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/write | Create or update a management group. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/subscriptions/read | Lists subscription under the given management group. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Management Group Contributor Role",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5d58bcaf-24a5-4b20-bdb6-eed9f69fbe4c",
  "name": "5d58bcaf-24a5-4b20-bdb6-eed9f69fbe4c",
  "permissions": [
    {
      "actions": [
        "Microsoft.Management/managementGroups/delete",
        "Microsoft.Management/managementGroups/read",
        "Microsoft.Management/managementGroups/subscriptions/delete",
        "Microsoft.Management/managementGroups/subscriptions/write",
        "Microsoft.Management/managementGroups/write",
        "Microsoft.Management/managementGroups/subscriptions/read",
        "Microsoft.Authorization/*/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Management Group Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Management Group Reader

Management Group Reader Role

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/read | List management groups for the authenticated user. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/subscriptions/read | Lists subscription under the given management group. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Management Group Reader Role",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/ac63b705-f282-497d-ac71-919bf39d939d",
  "name": "ac63b705-f282-497d-ac71-919bf39d939d",
  "permissions": [
    {
      "actions": [
        "Microsoft.Management/managementGroups/read",
        "Microsoft.Management/managementGroups/subscriptions/read",
        "Microsoft.Authorization/*/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Management Group Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## New Relic APM Account Contributor

Lets you manage New Relic Application Performance Management accounts and applications, but not access to them.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | NewRelic.APM/accounts/* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you manage New Relic Application Performance Management accounts and applications, but not access to them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5d28c62d-5b37-4476-8438-e587778df237",
  "name": "5d28c62d-5b37-4476-8438-e587778df237",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "NewRelic.APM/accounts/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "New Relic APM Account Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Policy Insights Data Writer (Preview)

Allows read access to resource policies and write access to resource component policy events.

[Learn more](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policyassignments/read | Get information about a policy assignment. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policydefinitions/read | Get information about a policy definition. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policyexemptions/read | Get information about a policy exemption. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policysetdefinitions/read | Get information about a policy set definition. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.PolicyInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftpolicyinsights)/checkDataPolicyCompliance/action | Check the compliance status of a given component against data policies. |
> | [Microsoft.PolicyInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftpolicyinsights)/policyEvents/logDataEvents/action | Log the resource component policy events. |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows read access to resource policies and write access to resource component policy events.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/66bb4e9e-b016-4a94-8249-4c0511c2be84",
  "name": "66bb4e9e-b016-4a94-8249-4c0511c2be84",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/policyassignments/read",
        "Microsoft.Authorization/policydefinitions/read",
        "Microsoft.Authorization/policyexemptions/read",
        "Microsoft.Authorization/policysetdefinitions/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.PolicyInsights/checkDataPolicyCompliance/action",
        "Microsoft.PolicyInsights/policyEvents/logDataEvents/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Policy Insights Data Writer (Preview)",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Quota Request Operator

Read and create quota requests, get quota request status, and create support tickets.

[Learn more](https://learn.microsoft.com/en-us/rest/api/reserved-vm-instances/quotaapi)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/resourceProviders/locations/serviceLimits/read | Get the current service limit or quota of the specified resource and location |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/resourceProviders/locations/serviceLimits/write | Create service limit or quota for the specified resource and location |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/resourceProviders/locations/serviceLimitsRequests/read | Get any service limit request for the specified resource and location |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/register/action | Registers the Capacity resource provider and enables the creation of Capacity resources. |
> | [Microsoft.Quota](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftquota)/usages/read | Get the usages for resource providers |
> | [Microsoft.Quota](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftquota)/quotas/read | Get the current Service limit or quota of the specified resource |
> | [Microsoft.Quota](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftquota)/quotas/write | Creates the service limit or quota request for the specified resource |
> | [Microsoft.Quota](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftquota)/quotaRequests/read | Get any service limit request for the specified resource |
> | [Microsoft.Quota](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftquota)/register/action | Register the subscription with Microsoft.Quota Resource Provider |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Read and create quota requests, get quota request status, and create support tickets.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/0e5f05e5-9ab9-446b-b98d-1e2157c94125",
  "name": "0e5f05e5-9ab9-446b-b98d-1e2157c94125",
  "permissions": [
    {
      "actions": [
        "Microsoft.Capacity/resourceProviders/locations/serviceLimits/read",
        "Microsoft.Capacity/resourceProviders/locations/serviceLimits/write",
        "Microsoft.Capacity/resourceProviders/locations/serviceLimitsRequests/read",
        "Microsoft.Capacity/register/action",
        "Microsoft.Quota/usages/read",
        "Microsoft.Quota/quotas/read",
        "Microsoft.Quota/quotas/write",
        "Microsoft.Quota/quotaRequests/read",
        "Microsoft.Quota/register/action",
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Quota Request Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Reservation Purchaser

Lets you purchase reservations

[Learn more](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/prepare-buy-reservation)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/read | Get information about a role assignment. |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/catalogs/read | Read catalog of Reservation |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/register/action | Registers the Capacity resource provider and enables the creation of Capacity resources. |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/register/action | Registers Subscription with Microsoft.Compute resource provider |
> | [Microsoft.Consumption](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftconsumption)/register/action | Register to Consumption RP |
> | [Microsoft.Consumption](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftconsumption)/reservationRecommendationDetails/read | List Reservation Recommendation Details |
> | [Microsoft.Consumption](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftconsumption)/reservationRecommendations/read | List single or shared recommendations for Reserved instances for a subscription. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.SQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/register/action | Registers the subscription for the Microsoft SQL Database resource provider and enables the creation of Microsoft SQL Databases. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/supporttickets/write | Allows creating and updating a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you purchase reservations",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/f7b75c60-3036-4b75-91c3-6b41c27c1689",
  "name": "f7b75c60-3036-4b75-91c3-6b41c27c1689",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/roleAssignments/read",
        "Microsoft.Capacity/catalogs/read",
        "Microsoft.Capacity/register/action",
        "Microsoft.Compute/register/action",
        "Microsoft.Consumption/register/action",
        "Microsoft.Consumption/reservationRecommendationDetails/read",
        "Microsoft.Consumption/reservationRecommendations/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.SQL/register/action",
        "Microsoft.Support/supporttickets/write"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Reservation Purchaser",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Reservations Reader

Lets one read all the reservations in a tenant

[Learn more](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-reservations)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/*/read |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/read | Get information about a role assignment. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/providers/Microsoft.Capacity"
  ],
  "description": "Lets one read all the reservations in a tenant",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/582fc458-8989-419f-a480-75249bc5db7e",
  "name": "582fc458-8989-419f-a480-75249bc5db7e",
  "permissions": [
    {
      "actions": [
        "Microsoft.Capacity/*/read",
        "Microsoft.Authorization/roleAssignments/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Reservations Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Resource Policy Contributor

Users with rights to create/modify resource policy, create support ticket and read resources/hierarchy.

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

[Learn more](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policyassignments/* | Create and manage policy assignments |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policydefinitions/* | Create and manage policy definitions |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policyexemptions/* | Create and manage policy exemptions |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policyenrollments/* |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/policysetdefinitions/* | Create and manage policy sets |
> | [Microsoft.PolicyInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftpolicyinsights)/* |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Users with rights to create/modify resource policy, create support ticket and read resources/hierarchy.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/36243c78-bf99-498c-9df9-86d9f8d28608",
  "name": "36243c78-bf99-498c-9df9-86d9f8d28608",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.Authorization/policyassignments/*",
        "Microsoft.Authorization/policydefinitions/*",
        "Microsoft.Authorization/policyexemptions/*",
        "Microsoft.Authorization/policyenrollments/*",
        "Microsoft.Authorization/policysetdefinitions/*",
        "Microsoft.PolicyInsights/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Resource Policy Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Savings plan Purchaser

Lets you purchase savings plans

[Learn more](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/permission-view-manage)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/register/action | Registers the Capacity resource provider and enables the creation of Capacity resources. |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity)/catalogs/read | Read catalog of Reservation |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/read | Get information about a role assignment. |
> | [Microsoft.BillingBenefits](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbillingbenefits)/savingsPlanOrders/write | Create a savings plan orders |
> | [Microsoft.BIllingBenefits](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbillingbenefits)/register/action | Registers the BillingBenefits resource provider and enables the creation of BillingBenefits resources. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/supporttickets/write | Allows creating and updating a support ticket |
> | [Microsoft.Billing](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbilling)/billingProperty/read | Gets the billing properties for a subscription |
> | [Microsoft.CostManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcostmanagement)/benefitRecommendations/read | List  single or shared recommendations for Microsoft benefits. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you purchase savings plans",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/3d24a3a0-c154-4f6f-a5ed-adc8e01ddb74",
  "name": "3d24a3a0-c154-4f6f-a5ed-adc8e01ddb74",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Capacity/register/action",
        "Microsoft.Capacity/catalogs/read",
        "Microsoft.Authorization/roleAssignments/read",
        "Microsoft.BillingBenefits/savingsPlanOrders/write",
        "Microsoft.BIllingBenefits/register/action",
        "Microsoft.Support/supporttickets/write",
        "Microsoft.Billing/billingProperty/read",
        "Microsoft.CostManagement/benefitRecommendations/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Savings plan Purchaser",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Scheduled Patching Contributor

Provides access to manage maintenance configurations with maintenance scope InGuestPatch and corresponding configuration assignments

[Learn more](https://learn.microsoft.com/en-us/azure/update-manager/scheduled-patching)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/maintenanceConfigurations/read | Read maintenance configuration. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/maintenanceConfigurations/write | Create or update maintenance configuration. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/maintenanceConfigurations/delete | Delete maintenance configuration. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/configurationAssignments/read | Read maintenance configuration assignment. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/configurationAssignments/write | Create or update maintenance configuration assignment. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/configurationAssignments/delete | Delete maintenance configuration assignment. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/configurationAssignments/maintenanceScope/InGuestPatch/read | Read maintenance configuration assignment for InGuestPatch maintenance scope. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/configurationAssignments/maintenanceScope/InGuestPatch/write | Create or update a maintenance configuration assignment for InGuestPatch maintenance scope. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/configurationAssignments/maintenanceScope/InGuestPatch/delete | Delete maintenance configuration assignment for InGuestPatch maintenance scope. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/maintenanceConfigurations/maintenanceScope/InGuestPatch/read | Read maintenance configuration for InGuestPatch maintenance scope. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/maintenanceConfigurations/maintenanceScope/InGuestPatch/write | Create or update a maintenance configuration for InGuestPatch maintenance scope. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/maintenanceConfigurations/maintenanceScope/InGuestPatch/delete | Delete maintenance configuration for InGuestPatch maintenance scope. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/applyUpdates/read | Read apply updates to a resource. |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance)/updates/read | Read updates to a resource. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Provides access to manage maintenance configurations with maintenance scope InGuestPatch and corresponding configuration assignments",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/cd08ab90-6b14-449c-ad9a-8f8e549482c6",
  "name": "cd08ab90-6b14-449c-ad9a-8f8e549482c6",
  "permissions": [
    {
      "actions": [
        "Microsoft.Maintenance/maintenanceConfigurations/read",
        "Microsoft.Maintenance/maintenanceConfigurations/write",
        "Microsoft.Maintenance/maintenanceConfigurations/delete",
        "Microsoft.Maintenance/configurationAssignments/read",
        "Microsoft.Maintenance/configurationAssignments/write",
        "Microsoft.Maintenance/configurationAssignments/delete",
        "Microsoft.Maintenance/configurationAssignments/maintenanceScope/InGuestPatch/read",
        "Microsoft.Maintenance/configurationAssignments/maintenanceScope/InGuestPatch/write",
        "Microsoft.Maintenance/configurationAssignments/maintenanceScope/InGuestPatch/delete",
        "Microsoft.Maintenance/maintenanceConfigurations/maintenanceScope/InGuestPatch/read",
        "Microsoft.Maintenance/maintenanceConfigurations/maintenanceScope/InGuestPatch/write",
        "Microsoft.Maintenance/maintenanceConfigurations/maintenanceScope/InGuestPatch/delete",
        "Microsoft.Maintenance/applyUpdates/read",
        "Microsoft.Maintenance/updates/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Scheduled Patching Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```
## Service Group Administrator

Manage all aspects of service groups and relationships. The default role assigned to users when they create a service group. Includes an ABAC condition to constrain role assignments.

[Learn more](https://learn.microsoft.com/en-us/azure/governance/service-groups/overview)

> | Actions | Description |
> | --- | --- |
> | * |  |
> | **NotActions** |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/write | Create a role assignment at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/delete | Delete a role assignment at the specified scope. |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |
> | **Actions** |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/write | Create a role assignment at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/delete | Delete a role assignment at the specified scope. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |
> | **Condition** |  |
> | ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{4e50c84cc78e4e37b47ee60ffea0a775,32e6a4ec60954e37b54b12aa350ba81f,de754d53652d4c75a67f1e48d8b49c97})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{4e50c84cc78e4e37b47ee60ffea0a775,32e6a4ec60954e37b54b12aa350ba81f,de754d53652d4c75a67f1e48d8b49c97})) | Add or remove role assignments for the following roles:<br/>Service Group Administrator<br/>Service Group Contributor<br/>Service Group Reader |

```json
{
  "assignableScopes": [
    "/providers/Microsoft.Management/serviceGroups"
  ],
  "description": "Role Definition for administrator of a Service Group",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/4e50c84c-c78e-4e37-b47e-e60ffea0a775",
  "name": "4e50c84c-c78e-4e37-b47e-e60ffea0a775",
  "permissions": [
    {
      "actions": [
        "*"
      ],
      "notActions": [
        "Microsoft.Authorization/roleAssignments/write",
        "Microsoft.Authorization/roleAssignments/delete"
      ],
      "dataActions": [],
      "notDataActions": []
    },
    {
      "actions": [
        "Microsoft.Authorization/roleAssignments/write",
        "Microsoft.Authorization/roleAssignments/delete"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": [],
      "conditionVersion": "2.0",
      "condition": "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{4e50c84cc78e4e37b47ee60ffea0a775,32e6a4ec60954e37b54b12aa350ba81f,de754d53652d4c75a67f1e48d8b49c97})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{4e50c84cc78e4e37b47ee60ffea0a775,32e6a4ec60954e37b54b12aa350ba81f,de754d53652d4c75a67f1e48d8b49c97}))"
    }
  ],
  "roleName": "Service Group Administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Service Group Contributor

Manage all aspects of service groups and relationships, but does not allow you to assign roles.

[Learn more](https://learn.microsoft.com/en-us/azure/governance/service-groups/overview)

> | Actions | Description |
> | --- | --- |
> | * |  |
> | **NotActions** |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/write | Create a role assignment at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/delete | Delete a role assignment at the specified scope. |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/providers/Microsoft.Management/serviceGroups"
  ],
  "description": "Role Definition for contributor of a Service Group",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/32e6a4ec-6095-4e37-b54b-12aa350ba81f",
  "name": "32e6a4ec-6095-4e37-b54b-12aa350ba81f",
  "permissions": [
    {
      "actions": [
        "*"
      ],
      "notActions": [
        "Microsoft.Authorization/roleAssignments/write",
        "Microsoft.Authorization/roleAssignments/delete"
      ],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Service Group Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Service Group Reader

Read service groups and view the connected relationships.

[Learn more](https://learn.microsoft.com/en-us/azure/governance/service-groups/overview)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/providers/Microsoft.Management/serviceGroups"
  ],
  "description": "Role Definition for reader of a Service Group",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/de754d53-652d-4c75-a67f-1e48d8b49c97",
  "name": "de754d53-652d-4c75-a67f-1e48d8b49c97",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.Authorization/*/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Service Group Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Site Recovery Contributor

Lets you manage Site Recovery service except vault creation and role assignment

[Learn more](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-role-based-linked-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/locations/allocatedStamp/read | GetAllocatedStamp is internal operation used by service |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/locations/allocateStamp/action | AllocateStamp is internal operation used by service |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/certificates/write | The Update Resource Certificate operation updates the resource/vault credential certificate. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/extendedInformation/* | Create and manage extended info related to vault |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/read | The Get Vault operation gets an object representing the Azure resource of type 'vault' |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/refreshContainers/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/registeredIdentities/* | Create and manage registered identities |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationAlertSettings/* | Create or Update replication alert settings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationEvents/read | Read any Events |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/* | Create and manage replication fabrics |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationJobs/* | Create and manage replication jobs |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationPolicies/* | Create and manage replication policies |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/* | Create and manage recovery plans |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationVaultSettings/* |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/storageConfig/* | Create and manage storage configuration of Recovery Services vault |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/tokenInfo/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/usages/read | Returns usage details for a Recovery Services Vault. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/vaultTokens/read | The Vault Token operation can be used to get Vault Token for vault level backend operations. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/monitoringAlerts/* | Read alerts for the Recovery services vault |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/monitoringConfigurations/notificationConfiguration/read |  |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/read | Returns the list of storage accounts or gets the properties for the specified storage account. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationOperationStatus/read | Read any Vault Replication Operation Status |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you manage Site Recovery service except vault creation and role assignment",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/6670b86e-a3f7-4917-ac9b-5d6ab1be4567",
  "name": "6670b86e-a3f7-4917-ac9b-5d6ab1be4567",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.RecoveryServices/locations/allocatedStamp/read",
        "Microsoft.RecoveryServices/locations/allocateStamp/action",
        "Microsoft.RecoveryServices/Vaults/certificates/write",
        "Microsoft.RecoveryServices/Vaults/extendedInformation/*",
        "Microsoft.RecoveryServices/Vaults/read",
        "Microsoft.RecoveryServices/Vaults/refreshContainers/read",
        "Microsoft.RecoveryServices/Vaults/registeredIdentities/*",
        "Microsoft.RecoveryServices/vaults/replicationAlertSettings/*",
        "Microsoft.RecoveryServices/vaults/replicationEvents/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/*",
        "Microsoft.RecoveryServices/vaults/replicationJobs/*",
        "Microsoft.RecoveryServices/vaults/replicationPolicies/*",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/*",
        "Microsoft.RecoveryServices/vaults/replicationVaultSettings/*",
        "Microsoft.RecoveryServices/Vaults/storageConfig/*",
        "Microsoft.RecoveryServices/Vaults/tokenInfo/read",
        "Microsoft.RecoveryServices/Vaults/usages/read",
        "Microsoft.RecoveryServices/Vaults/vaultTokens/read",
        "Microsoft.RecoveryServices/Vaults/monitoringAlerts/*",
        "Microsoft.RecoveryServices/Vaults/monitoringConfigurations/notificationConfiguration/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Storage/storageAccounts/read",
        "Microsoft.RecoveryServices/vaults/replicationOperationStatus/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Site Recovery Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Site Recovery Operator

Lets you failover and failback but not perform other Site Recovery management operations

[Learn more](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-role-based-linked-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/locations/allocatedStamp/read | GetAllocatedStamp is internal operation used by service |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/locations/allocateStamp/action | AllocateStamp is internal operation used by service |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/extendedInformation/read | The Get Extended Info operation gets an object's Extended Info representing the Azure resource of type ?vault? |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/read | The Get Vault operation gets an object representing the Azure resource of type 'vault' |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/refreshContainers/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/registeredIdentities/operationResults/read | The Get Operation Results operation can be used get the operation status and result for the asynchronously submitted operation |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/registeredIdentities/read | The Get Containers operation can be used get the containers registered for a resource. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationAlertSettings/read | Read any Alerts Settings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationEvents/read | Read any Events |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/checkConsistency/action | Checks Consistency of the Fabric |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/read | Read any Fabrics |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/reassociateGateway/action | Reassociate Gateway |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/renewcertificate/action | Renew Certificate for Fabric |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationNetworks/read | Read any Networks |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationNetworks/replicationNetworkMappings/read | Read any Network Mappings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/read | Read any Protection Containers |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectableItems/read | Read any Protectable Items |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/applyRecoveryPoint/action | Apply Recovery Point |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/failoverCommit/action | Failover Commit |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/plannedFailover/action | Planned Failover |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/read | Read any Protected Items |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/recoveryPoints/read | Read any Replication Recovery Points |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/repairReplication/action | Repair replication |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/reProtect/action | ReProtect Protected Item |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/switchprotection/action | Switch Protection Container |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/testFailover/action | Test Failover |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/testFailoverCleanup/action | Test Failover Cleanup |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/unplannedFailover/action | Failover |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/updateMobilityService/action | Update Mobility Service |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectionContainerMappings/read | Read any Protection Container Mappings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationRecoveryServicesProviders/read | Read any Recovery Services Providers |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationRecoveryServicesProviders/refreshProvider/action | Refresh Provider |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationStorageClassifications/read | Read any Storage Classifications |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationStorageClassifications/replicationStorageClassificationMappings/read | Read any Storage Classification Mappings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationvCenters/read | Read any vCenters |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationJobs/* | Create and manage replication jobs |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationPolicies/read | Read any Policies |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/failoverCommit/action | Failover Commit Recovery Plan |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/plannedFailover/action | Planned Failover Recovery Plan |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/read | Read any Recovery Plans |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/reProtect/action | ReProtect Recovery Plan |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/testFailover/action | Test Failover Recovery Plan |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/testFailoverCleanup/action | Test Failover Cleanup Recovery Plan |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/unplannedFailover/action | Failover Recovery Plan |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationVaultSettings/read | Read any  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/monitoringAlerts/* | Read alerts for the Recovery services vault |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/monitoringConfigurations/notificationConfiguration/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/storageConfig/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/tokenInfo/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/usages/read | Returns usage details for a Recovery Services Vault. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/vaultTokens/read | The Vault Token operation can be used to get Vault Token for vault level backend operations. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/read | Returns the list of storage accounts or gets the properties for the specified storage account. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you failover and failback but not perform other Site Recovery management operations",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/494ae006-db33-4328-bf46-533a6560a3ca",
  "name": "494ae006-db33-4328-bf46-533a6560a3ca",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.RecoveryServices/locations/allocatedStamp/read",
        "Microsoft.RecoveryServices/locations/allocateStamp/action",
        "Microsoft.RecoveryServices/Vaults/extendedInformation/read",
        "Microsoft.RecoveryServices/Vaults/read",
        "Microsoft.RecoveryServices/Vaults/refreshContainers/read",
        "Microsoft.RecoveryServices/Vaults/registeredIdentities/operationResults/read",
        "Microsoft.RecoveryServices/Vaults/registeredIdentities/read",
        "Microsoft.RecoveryServices/vaults/replicationAlertSettings/read",
        "Microsoft.RecoveryServices/vaults/replicationEvents/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/checkConsistency/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/reassociateGateway/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/renewcertificate/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationNetworks/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationNetworks/replicationNetworkMappings/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectableItems/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/applyRecoveryPoint/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/failoverCommit/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/plannedFailover/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/recoveryPoints/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/repairReplication/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/reProtect/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/switchprotection/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/testFailover/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/testFailoverCleanup/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/unplannedFailover/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/updateMobilityService/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectionContainerMappings/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationRecoveryServicesProviders/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationRecoveryServicesProviders/refreshProvider/action",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationStorageClassifications/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationStorageClassifications/replicationStorageClassificationMappings/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationvCenters/read",
        "Microsoft.RecoveryServices/vaults/replicationJobs/*",
        "Microsoft.RecoveryServices/vaults/replicationPolicies/read",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/failoverCommit/action",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/plannedFailover/action",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/read",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/reProtect/action",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/testFailover/action",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/testFailoverCleanup/action",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/unplannedFailover/action",
        "Microsoft.RecoveryServices/vaults/replicationVaultSettings/read",
        "Microsoft.RecoveryServices/Vaults/monitoringAlerts/*",
        "Microsoft.RecoveryServices/Vaults/monitoringConfigurations/notificationConfiguration/read",
        "Microsoft.RecoveryServices/Vaults/storageConfig/read",
        "Microsoft.RecoveryServices/Vaults/tokenInfo/read",
        "Microsoft.RecoveryServices/Vaults/usages/read",
        "Microsoft.RecoveryServices/Vaults/vaultTokens/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Storage/storageAccounts/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Site Recovery Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Site Recovery Reader

Lets you view Site Recovery status but not perform other management operations

[Learn more](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-role-based-linked-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/locations/allocatedStamp/read | GetAllocatedStamp is internal operation used by service |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/extendedInformation/read | The Get Extended Info operation gets an object's Extended Info representing the Azure resource of type ?vault? |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/monitoringAlerts/read | Gets the alerts for the Recovery services vault. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/monitoringConfigurations/notificationConfiguration/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/read | The Get Vault operation gets an object representing the Azure resource of type 'vault' |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/refreshContainers/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/registeredIdentities/operationResults/read | The Get Operation Results operation can be used get the operation status and result for the asynchronously submitted operation |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/registeredIdentities/read | The Get Containers operation can be used get the containers registered for a resource. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationAlertSettings/read | Read any Alerts Settings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationEvents/read | Read any Events |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/read | Read any Fabrics |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationNetworks/read | Read any Networks |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationNetworks/replicationNetworkMappings/read | Read any Network Mappings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/read | Read any Protection Containers |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectableItems/read | Read any Protectable Items |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/read | Read any Protected Items |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/recoveryPoints/read | Read any Replication Recovery Points |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectionContainerMappings/read | Read any Protection Container Mappings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationRecoveryServicesProviders/read | Read any Recovery Services Providers |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationStorageClassifications/read | Read any Storage Classifications |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationStorageClassifications/replicationStorageClassificationMappings/read | Read any Storage Classification Mappings |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationvCenters/read | Read any vCenters |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationJobs/read | Read any Jobs |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationPolicies/read | Read any Policies |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationRecoveryPlans/read | Read any Recovery Plans |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationVaultSettings/read | Read any  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/storageConfig/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/tokenInfo/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/usages/read | Returns usage details for a Recovery Services Vault. |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/Vaults/vaultTokens/read | The Vault Token operation can be used to get Vault Token for vault level backend operations. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you view Site Recovery status but not perform other management operations",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/dbaa88c4-0c30-4179-9fb3-46319faa6149",
  "name": "dbaa88c4-0c30-4179-9fb3-46319faa6149",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.RecoveryServices/locations/allocatedStamp/read",
        "Microsoft.RecoveryServices/Vaults/extendedInformation/read",
        "Microsoft.RecoveryServices/Vaults/monitoringAlerts/read",
        "Microsoft.RecoveryServices/Vaults/monitoringConfigurations/notificationConfiguration/read",
        "Microsoft.RecoveryServices/Vaults/read",
        "Microsoft.RecoveryServices/Vaults/refreshContainers/read",
        "Microsoft.RecoveryServices/Vaults/registeredIdentities/operationResults/read",
        "Microsoft.RecoveryServices/Vaults/registeredIdentities/read",
        "Microsoft.RecoveryServices/vaults/replicationAlertSettings/read",
        "Microsoft.RecoveryServices/vaults/replicationEvents/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationNetworks/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationNetworks/replicationNetworkMappings/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectableItems/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/recoveryPoints/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectionContainerMappings/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationRecoveryServicesProviders/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationStorageClassifications/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationStorageClassifications/replicationStorageClassificationMappings/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationvCenters/read",
        "Microsoft.RecoveryServices/vaults/replicationJobs/read",
        "Microsoft.RecoveryServices/vaults/replicationPolicies/read",
        "Microsoft.RecoveryServices/vaults/replicationRecoveryPlans/read",
        "Microsoft.RecoveryServices/vaults/replicationVaultSettings/read",
        "Microsoft.RecoveryServices/Vaults/storageConfig/read",
        "Microsoft.RecoveryServices/Vaults/tokenInfo/read",
        "Microsoft.RecoveryServices/Vaults/usages/read",
        "Microsoft.RecoveryServices/Vaults/vaultTokens/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Site Recovery Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## SRE Agent Administrator

Full control of the agent—manage chats, incident response plans, and agent run modes; approve and execute commands.

[Learn more](https://learn.microsoft.com/en-us/azure/sre-agent/user-access-roles)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/read | Read a classic metric alert |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/read | Read SRE Agent properties |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/*/read |  |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/write | Create or Update a SRE Agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/*/write |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/*/read |  |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/*/write |  |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/*/delete |  |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/threads/approve/action | Approve action executions in conversation threads |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Full control of the agent—manage chats, incident response plans, and agent run modes; approve and execute commands.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/e79298df-d852-4c6d-84f9-5d13249d1e55",
  "name": "e79298df-d852-4c6d-84f9-5d13249d1e55",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/read",
        "Microsoft.App/agents/read",
        "Microsoft.App/agents/*/read",
        "Microsoft.App/agents/write",
        "Microsoft.App/agents/*/write"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.App/agents/*/read",
        "Microsoft.App/agents/*/write",
        "Microsoft.App/agents/*/delete",
        "Microsoft.App/agents/threads/approve/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "SRE Agent Administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## SRE Agent Reader

Grants read-only access to all SRE Agent data, including chats, incidents, logs, and configurations. Does not permit interaction with the agent.

[Learn more](https://learn.microsoft.com/en-us/azure/sre-agent/user-access-roles)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/read | Read SRE Agent properties |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/threads/read | Read all the conversation threads with an SRE Agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/graph/read | Read resource graph in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/memory/read | Read agent memory in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/incidentManagement/read | Read incident management configurations in an SRE agent |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants read-only access to all SRE Agent data, including chats, incidents, logs, and configurations. Does not permit interaction with the agent.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/a4b156ac-253f-4a1a-9851-96d62b71b047",
  "name": "a4b156ac-253f-4a1a-9851-96d62b71b047",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.App/agents/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.App/agents/threads/read",
        "Microsoft.App/agents/graph/read",
        "Microsoft.App/agents/memory/read",
        "Microsoft.App/agents/incidentManagement/read"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "SRE Agent Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## SRE Agent Standard User

Grants access to interact with the SRE Agent to triage incidents and run diagnostics.

[Learn more](https://learn.microsoft.com/en-us/azure/sre-agent/user-access-roles)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/read | Read a classic metric alert |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/read | Read SRE Agent properties |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/threads/read | Read all the conversation threads with an SRE Agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/graph/read | Read resource graph in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/memory/read | Read agent memory in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/incidentManagement/read | Read incident management configurations in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/threads/write | Create new conversation threads with an SRE Agent and reply to existing threads |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/graph/write | Update nodes in resource graph in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/memory/write | Update agent memory in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/scheduledtasks/read | Read scheduled tasks in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/scheduledtasks/write | Update scheduled tasks in an SRE agent |
> | [Microsoft.App](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp)/agents/scheduledtasks/delete | Delete existing scheduled tasks in an SRE agent |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants access to interact with the SRE Agent to triage incidents and run diagnostics.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/2d84a65a-63b2-4343-bbb6-31105d857bc1",
  "name": "2d84a65a-63b2-4343-bbb6-31105d857bc1",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/read",
        "Microsoft.App/agents/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.App/agents/threads/read",
        "Microsoft.App/agents/graph/read",
        "Microsoft.App/agents/memory/read",
        "Microsoft.App/agents/incidentManagement/read",
        "Microsoft.App/agents/threads/write",
        "Microsoft.App/agents/graph/write",
        "Microsoft.App/agents/memory/write",
        "Microsoft.App/agents/scheduledtasks/read",
        "Microsoft.App/agents/scheduledtasks/write",
        "Microsoft.App/agents/scheduledtasks/delete"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "SRE Agent Standard User",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Support Request Contributor

Lets you create and manage Support requests

[Learn more](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-create-azure-support-request)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you create and manage Support requests",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/cfd33db0-3dd1-45e3-aa9d-cdbdf3b6f24e",
  "name": "cfd33db0-3dd1-45e3-aa9d-cdbdf3b6f24e",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Support Request Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Tag Contributor

Lets you manage tags on entities, without providing access to the entities themselves.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/resources/read | Gets the resources for the resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resources/read | Gets resources of a subscription. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/tags/* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you manage tags on entities, without providing access to the entities themselves.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/4a9ae827-6dc8-4573-8ac7-8239d42aa03f",
  "name": "4a9ae827-6dc8-4573-8ac7-8239d42aa03f",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/resourceGroups/resources/read",
        "Microsoft.Resources/subscriptions/resources/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Support/*",
        "Microsoft.Resources/tags/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Tag Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Template Spec Contributor

Allows full access to Template Spec operations at the assigned scope.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/templateSpecs/* | Create and manage template specs and template spec versions |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows full access to Template Spec operations at the assigned scope.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/1c9b6475-caf0-4164-b5a1-2142a7116f4b",
  "name": "1c9b6475-caf0-4164-b5a1-2142a7116f4b",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/templateSpecs/*",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Template Spec Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Template Spec Reader

Allows read access to Template Specs at the assigned scope.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/templateSpecs/*/read | Get or list template specs and template spec versions |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows read access to Template Specs at the assigned scope.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/392ae280-861d-42bd-9ea5-08ee6d83b80e",
  "name": "392ae280-861d-42bd-9ea5-08ee6d83b80e",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/templateSpecs/*/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Template Spec Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
