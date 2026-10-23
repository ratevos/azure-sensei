# Azure built-in roles for Monitor - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/monitor  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the Monitor category.

## Application Insights Component Contributor

Can manage Application Insights components

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/app/resources-roles-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage classic alert rules |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/generateLiveToken/read | Live Metrics get token |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricAlerts/* | Create and manage new alert rules |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/components/* | Create and manage Insights components |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/scheduledqueryrules/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/topology/read | Read Topology |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/transactions/read | Read Transactions |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/webtests/* | Create and manage Insights web tests |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
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
  "description": "Can manage Application Insights components",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/ae349356-3a1b-4a5e-921d-050484c6347e",
  "name": "ae349356-3a1b-4a5e-921d-050484c6347e",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Insights/generateLiveToken/read",
        "Microsoft.Insights/metricAlerts/*",
        "Microsoft.Insights/components/*",
        "Microsoft.Insights/scheduledqueryrules/*",
        "Microsoft.Insights/topology/read",
        "Microsoft.Insights/transactions/read",
        "Microsoft.Insights/webtests/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Application Insights Component Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Application Insights Snapshot Debugger

Gives user permission to view and download debug snapshots collected with the Application Insights Snapshot Debugger. Note that these permissions are not included in the [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor) roles. When giving users the Application Insights Snapshot Debugger role, you must grant the role directly to the user. The role is not recognized when it is added to a custom role.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/app/snapshot-debugger)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/components/*/read |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/snapshots/read | Read snapshots generated by Snapshot Debugger |
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
  "description": "Gives user permission to use Application Insights Snapshot Debugger features",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/08954f03-6346-4c2e-81c0-ec3a5cfae23b",
  "name": "08954f03-6346-4c2e-81c0-ec3a5cfae23b",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Insights/components/*/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "Microsoft.Insights/snapshots/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Application Insights Snapshot Debugger",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Managed Grafana Workspace Contributor

Can manage Azure Managed Grafana resources, without providing access to the workspaces themselves.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/write | Write grafana |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/delete | Delete grafana |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/PrivateEndpointConnectionsApproval/action | Approve PrivateEndpointConnection |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/managedPrivateEndpoints/action | Operations on Private Endpoints |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/locations/operationStatuses/write | Write operation statuses |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/privateEndpointConnectionProxies/validate/action | Validate PrivateEndpointConnectionProxy |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/privateEndpointConnectionProxies/write | Create/Update PrivateEndpointConnectionProxy |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/privateEndpointConnectionProxies/delete | Delete PrivateEndpointConnectionProxy |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/privateEndpointConnections/write | Update PrivateEndpointConnection |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/privateEndpointConnections/delete | Delete PrivateEndpointConnection |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/managedPrivateEndpoints/write | Write Managed Private Endpoints |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/managedPrivateEndpoints/delete | Delete Managed Private Endpoints |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/integrationFabrics/write | Write Integration Fabrics |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/integrationFabrics/delete | Delete Integration Fabrics |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/grafanaDefinitions/read | Read Grafana Definitions |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/grafanaDefinitions/write | Write Grafana Definitions |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/grafanaDefinitions/delete | Delete Grafana Definitions |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Write | Create or update a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Delete | Delete a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Activated/Action | Classic metric alert activated |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Resolved/Action | Classic metric alert resolved |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Throttled/Action | Classic metric alert rule throttled |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Incidents/Read | Read a classic metric alert incident |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/delete | Deletes a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/cancel/action | Cancels a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/validate/action | Validates a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/whatIf/action | Predicts template deployment changes. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/exportTemplate/action | Export template for a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
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
  "description": "Can manage Azure Managed Grafana resources, without providing access to the workspaces themselves.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5c2d7e57-b7c2-4d8a-be4f-82afa42c6e95",
  "name": "5c2d7e57-b7c2-4d8a-be4f-82afa42c6e95",
  "permissions": [
    {
      "actions": [
        "Microsoft.Dashboard/grafana/write",
        "Microsoft.Dashboard/grafana/delete",
        "Microsoft.Dashboard/grafana/PrivateEndpointConnectionsApproval/action",
        "Microsoft.Dashboard/grafana/managedPrivateEndpoints/action",
        "Microsoft.Dashboard/locations/operationStatuses/write",
        "Microsoft.Dashboard/grafana/privateEndpointConnectionProxies/validate/action",
        "Microsoft.Dashboard/grafana/privateEndpointConnectionProxies/write",
        "Microsoft.Dashboard/grafana/privateEndpointConnectionProxies/delete",
        "Microsoft.Dashboard/grafana/privateEndpointConnections/write",
        "Microsoft.Dashboard/grafana/privateEndpointConnections/delete",
        "Microsoft.Dashboard/grafana/managedPrivateEndpoints/write",
        "Microsoft.Dashboard/grafana/managedPrivateEndpoints/delete",
        "Microsoft.Dashboard/grafana/integrationFabrics/write",
        "Microsoft.Dashboard/grafana/integrationFabrics/delete",
        "Microsoft.Dashboard/grafana/grafanaDefinitions/read",
        "Microsoft.Dashboard/grafana/grafanaDefinitions/write",
        "Microsoft.Dashboard/grafana/grafanaDefinitions/delete",
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/AlertRules/Write",
        "Microsoft.Insights/AlertRules/Delete",
        "Microsoft.Insights/AlertRules/Read",
        "Microsoft.Insights/AlertRules/Activated/Action",
        "Microsoft.Insights/AlertRules/Resolved/Action",
        "Microsoft.Insights/AlertRules/Throttled/Action",
        "Microsoft.Insights/AlertRules/Incidents/Read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Resources/deployments/write",
        "Microsoft.Resources/deployments/delete",
        "Microsoft.Resources/deployments/cancel/action",
        "Microsoft.Resources/deployments/validate/action",
        "Microsoft.Resources/deployments/whatIf/action",
        "Microsoft.Resources/deployments/exportTemplate/action",
        "Microsoft.Resources/deployments/operations/read",
        "Microsoft.Resources/deployments/operationstatuses/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Managed Grafana Workspace Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Data Purger

Delete private data from a Log Analytics workspace.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/personal-data-mgmt)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/components/*/read |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/components/purge/action | Purging data from Application Insights |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/*/read | View log analytics data |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/purge/action | Delete specified data by query from workspace. |
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
  "description": "Can purge analytics data",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/150f5e0c-0603-4f03-8c7f-cf70034c4e90",
  "name": "150f5e0c-0603-4f03-8c7f-cf70034c4e90",
  "permissions": [
    {
      "actions": [
        "Microsoft.Insights/components/*/read",
        "Microsoft.Insights/components/purge/action",
        "Microsoft.OperationalInsights/workspaces/*/read",
        "Microsoft.OperationalInsights/workspaces/purge/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Data Purger",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Grafana Admin

Manage server-wide settings and manage access to resources such as organizations, users, and licenses.

[Learn more](https://learn.microsoft.com/en-us/azure/managed-grafana/concept-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | *none* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/ActAsGrafanaAdmin/action | Act as Grafana Admin role |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Manage server-wide settings and manage access to resources such as organizations, users, and licenses.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/22926164-76b3-42b3-bc55-97df8dab3e41",
  "name": "22926164-76b3-42b3-bc55-97df8dab3e41",
  "permissions": [
    {
      "actions": [],
      "notActions": [],
      "dataActions": [
        "Microsoft.Dashboard/grafana/ActAsGrafanaAdmin/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Grafana Admin",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Grafana Editor

Create, edit, delete, or view dashboards; create, edit, or delete folders; and edit or view playlists.

[Learn more](https://learn.microsoft.com/en-us/azure/managed-grafana/concept-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | *none* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/ActAsGrafanaEditor/action | Act as Grafana Editor role |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Create, edit, delete, or view dashboards; create, edit, or delete folders; and edit or view playlists.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/a79a5197-3a5c-4973-a920-486035ffd60f",
  "name": "a79a5197-3a5c-4973-a920-486035ffd60f",
  "permissions": [
    {
      "actions": [],
      "notActions": [],
      "dataActions": [
        "Microsoft.Dashboard/grafana/ActAsGrafanaEditor/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Grafana Editor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Grafana Limited Viewer

View home page.

[Learn more](https://learn.microsoft.com/en-us/azure/managed-grafana/concept-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | *none* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/ActAsGrafanaLimitedViewer/action | Act as Grafana Limited Viewer role |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "View home page.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/41e04612-9dac-4699-a02b-c82ff2cc3fb5",
  "name": "41e04612-9dac-4699-a02b-c82ff2cc3fb5",
  "permissions": [
    {
      "actions": [],
      "notActions": [],
      "dataActions": [
        "Microsoft.Dashboard/grafana/ActAsGrafanaLimitedViewer/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Grafana Limited Viewer",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Grafana Viewer

View dashboards, playlists, and query data sources.

[Learn more](https://learn.microsoft.com/en-us/azure/managed-grafana/concept-role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | *none* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard)/grafana/ActAsGrafanaViewer/action | Act as Grafana Viewer role |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "View dashboards, playlists, and query data sources.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/60921a7e-fef1-4a43-9b16-a26c52ad4769",
  "name": "60921a7e-fef1-4a43-9b16-a26c52ad4769",
  "permissions": [
    {
      "actions": [],
      "notActions": [],
      "dataActions": [
        "Microsoft.Dashboard/grafana/ActAsGrafanaViewer/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Grafana Viewer",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Log Analytics Contributor

Log Analytics Contributor can read all monitoring data and edit monitoring settings. Editing monitoring settings includes adding the VM extension to VMs; reading storage account keys to be able to configure collection of logs from Azure Storage; adding solutions; and configuring Azure diagnostics on all Azure resources.

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | Microsoft.ClassicCompute/virtualMachines/extensions/* |  |
> | Microsoft.ClassicStorage/storageAccounts/listKeys/action |  |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/extensions/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/write | Installs or Updates an Azure Arc extensions |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/diagnosticSettings/* | Creates, updates, or reads the diagnostic setting for Analysis Server |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/* |  |
> | [Microsoft.OperationsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationsmanagement)/* |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/* |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/listKeys/action | Returns the access keys for the specified storage account. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/jobs/export/action | Lets you export data from Log Analytics workspace per query and time range |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Log Analytics Contributor can read all monitoring data and edit monitoring settings. Editing monitoring settings includes adding the VM extension to VMs; reading storage account keys to be able to configure collection of logs from Azure Storage; adding solutions; and configuring Azure diagnostics on all Azure resources.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/92aaf0da-9dab-42b6-94a3-d43ce8d16293",
  "name": "92aaf0da-9dab-42b6-94a3-d43ce8d16293",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.ClassicCompute/virtualMachines/extensions/*",
        "Microsoft.ClassicStorage/storageAccounts/listKeys/action",
        "Microsoft.Compute/virtualMachines/extensions/*",
        "Microsoft.HybridCompute/machines/extensions/write",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Insights/diagnosticSettings/*",
        "Microsoft.OperationalInsights/*",
        "Microsoft.OperationsManagement/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/*",
        "Microsoft.Storage/storageAccounts/listKeys/action",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.OperationalInsights/workspaces/jobs/export/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Log Analytics Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Log Analytics Data Reader

Log Analytics Data Reader can query and search the logs it is allowed to view over Log Analytics workspaces and tables

> | Actions | Description |
> | --- | --- |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/query/read | Run queries over the data in the workspace |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/read | Gets an existing workspace |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/tables/data/read | Allows you to provide read data access to workspaces, or more fine-grained data entities, such as specific tables or rows. |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Log Analytics Data Reader can query and search the logs it is allowed to view over Log Analytics workspaces and tables",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/3b03c2da-16b3-4a49-8834-0f8130efdd3b",
  "name": "3b03c2da-16b3-4a49-8834-0f8130efdd3b",
  "permissions": [
    {
      "actions": [
        "Microsoft.OperationalInsights/workspaces/query/read",
        "Microsoft.OperationalInsights/workspaces/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.OperationalInsights/workspaces/tables/data/read"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Log Analytics Data Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Log Analytics Reader

Log Analytics Reader can view and search all monitoring data as well as and view monitoring settings, including viewing the configuration of Azure diagnostics on all Azure resources.

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/analytics/query/action | Search using new engine. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/search/action | Executes a search query |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | **NotActions** |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedKeys/read | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | **DataActions** |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/jobs/export/action | Lets you export data from Log Analytics workspace per query and time range |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Log Analytics Reader can view and search all monitoring data as well as and view monitoring settings, including viewing the configuration of Azure diagnostics on all Azure resources.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/73c42c96-874c-492b-b04d-ab87d138a893",
  "name": "73c42c96-874c-492b-b04d-ab87d138a893",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.OperationalInsights/workspaces/analytics/query/action",
        "Microsoft.OperationalInsights/workspaces/search/action",
        "Microsoft.Support/*"
      ],
      "notActions": [
        "Microsoft.OperationalInsights/workspaces/sharedKeys/read"
      ],
      "dataActions": [
        "Microsoft.OperationalInsights/workspaces/jobs/export/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Log Analytics Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Monitoring Contributor

Can read all monitoring data and edit monitoring settings. See also [Get started with roles, permissions, and security with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/roles-permissions-security#built-in-monitoring-roles).

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/roles-permissions-security)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/alerts/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/alertsSummary/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/issues/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/actiongroups/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/activityLogAlerts/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/components/* | Create and manage Insights components |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/createNotifications/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionEndpoints/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRules/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRuleAssociations/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/DiagnosticSettings/* | Creates, updates, or reads the diagnostic setting for Analysis Server |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/eventtypes/* | List Activity Log events (management events) in a subscription. This permission is applicable to both programmatic and portal access to the Activity Log. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/LogDefinitions/* | This permission is necessary for users who need access to Activity Logs via the portal. List log categories in Activity Log. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricalerts/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/MetricDefinitions/* | Read metric definitions (list of available metric types for a resource). |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Metrics/* | Read metrics for a resource. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/notificationStatus/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Register/Action | Register the Microsoft Insights provider |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/scheduledqueryrules/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/webtests/* | Create and manage Insights web tests |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooktemplates/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/privateLinkScopes/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/privateLinkScopeOperationStatuses/* |  |
> | [Microsoft.Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor)/accounts/* |  |
> | [Microsoft.Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor)/settings/* |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/write | Creates a new workspace or links to an existing workspace by providing the customer id from the existing workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/intelligencepacks/* | Read/write/delete log analytics solution packs. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/savedSearches/* | Read/write/delete log analytics saved searches. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/search/action | Executes a search query |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedKeys/action | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedKeys/read | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/storageinsightconfigs/* | Read/write/delete log analytics storage insight configurations. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/locations/workspaces/failover/action | Initiates workspace failover to replication location. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/failback/action | Initiates workspace failback. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/smartDetectorAlertRules/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/actionRules/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/smartGroups/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/migrateFromSmartDetection/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/investigations/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/prometheusRuleGroups/* |  |
> | [Microsoft.Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor)/investigations/* |  |
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
  "description": "Can read all monitoring data and update monitoring settings.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/749f88d5-cbae-40b8-bcfc-e573ddc772fa",
  "name": "749f88d5-cbae-40b8-bcfc-e573ddc772fa",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.AlertsManagement/alerts/*",
        "Microsoft.AlertsManagement/alertsSummary/*",
        "Microsoft.AlertsManagement/issues/*",
        "Microsoft.Insights/actiongroups/*",
        "Microsoft.Insights/activityLogAlerts/*",
        "Microsoft.Insights/AlertRules/*",
        "Microsoft.Insights/components/*",
        "Microsoft.Insights/createNotifications/*",
        "Microsoft.Insights/dataCollectionEndpoints/*",
        "Microsoft.Insights/dataCollectionRules/*",
        "Microsoft.Insights/dataCollectionRuleAssociations/*",
        "Microsoft.Insights/DiagnosticSettings/*",
        "Microsoft.Insights/eventtypes/*",
        "Microsoft.Insights/LogDefinitions/*",
        "Microsoft.Insights/metricalerts/*",
        "Microsoft.Insights/MetricDefinitions/*",
        "Microsoft.Insights/Metrics/*",
        "Microsoft.Insights/notificationStatus/*",
        "Microsoft.Insights/Register/Action",
        "Microsoft.Insights/scheduledqueryrules/*",
        "Microsoft.Insights/webtests/*",
        "Microsoft.Insights/workbooks/*",
        "Microsoft.Insights/workbooktemplates/*",
        "Microsoft.Insights/privateLinkScopes/*",
        "Microsoft.Insights/privateLinkScopeOperationStatuses/*",
        "Microsoft.Monitor/accounts/*",
        "Microsoft.Monitor/settings/*",
        "Microsoft.OperationalInsights/workspaces/write",
        "Microsoft.OperationalInsights/workspaces/intelligencepacks/*",
        "Microsoft.OperationalInsights/workspaces/savedSearches/*",
        "Microsoft.OperationalInsights/workspaces/search/action",
        "Microsoft.OperationalInsights/workspaces/sharedKeys/action",
        "Microsoft.OperationalInsights/workspaces/sharedKeys/read",
        "Microsoft.OperationalInsights/workspaces/storageinsightconfigs/*",
        "Microsoft.OperationalInsights/locations/workspaces/failover/action",
        "Microsoft.OperationalInsights/workspaces/failback/action",
        "Microsoft.Support/*",
        "Microsoft.AlertsManagement/smartDetectorAlertRules/*",
        "Microsoft.AlertsManagement/actionRules/*",
        "Microsoft.AlertsManagement/smartGroups/*",
        "Microsoft.AlertsManagement/migrateFromSmartDetection/*",
        "Microsoft.AlertsManagement/investigations/*",
        "Microsoft.AlertsManagement/prometheusRuleGroups/*",
        "Microsoft.Monitor/investigations/*",
        "Microsoft.Resources/deployments/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Monitoring Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Monitoring Metrics Publisher

Enables publishing metrics against Azure resources

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/container-insights-update-metrics)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Register/Action | Register the Microsoft Insights provider |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Metrics/Write | Write metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Telemetry/Write | Write telemetry |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Enables publishing metrics against Azure resources",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/3913510d-42f4-4e42-8a64-420c390055eb",
  "name": "3913510d-42f4-4e42-8a64-420c390055eb",
  "permissions": [
    {
      "actions": [
        "Microsoft.Insights/Register/Action",
        "Microsoft.Support/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.Insights/Metrics/Write",
        "Microsoft.Insights/Telemetry/Write"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Monitoring Metrics Publisher",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Monitoring Policy Contributor

Allows read access to all monitoring data, update permissions for monitoring settings and permissions to deploy and remediate Azure Monitor alert policies.

[Learn more](https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-azure-monitor)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/alerts/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/alertsSummary/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/issues/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/actiongroups/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/activityLogAlerts/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/components/* | Create and manage Insights components |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/createNotifications/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionEndpoints/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRules/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/dataCollectionRuleAssociations/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/DiagnosticSettings/* | Creates, updates, or reads the diagnostic setting for Analysis Server |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/eventtypes/* | List Activity Log events (management events) in a subscription. This permission is applicable to both programmatic and portal access to the Activity Log. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/LogDefinitions/* | This permission is necessary for users who need access to Activity Logs via the portal. List log categories in Activity Log. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricalerts/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/MetricDefinitions/* | Read metric definitions (list of available metric types for a resource). |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Metrics/* | Read metrics for a resource. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/notificationStatus/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Register/Action | Register the Microsoft Insights provider |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/scheduledqueryrules/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/webtests/* | Create and manage Insights web tests |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooktemplates/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/privateLinkScopes/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/privateLinkScopeOperationStatuses/* |  |
> | [Microsoft.Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor)/accounts/* |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/write | Creates a new workspace or links to an existing workspace by providing the customer id from the existing workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/intelligencepacks/* |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/savedSearches/* |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/search/action | Executes a search query |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedKeys/action | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/sharedKeys/read | Retrieves the shared keys for the workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/storageinsightconfigs/* |  |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/locations/workspaces/failover/action | Initiates workspace failover to replication location. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/failback/action | Initiates workspace failback. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/smartDetectorAlertRules/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/actionRules/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/smartGroups/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/migrateFromSmartDetection/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/investigations/* |  |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement)/prometheusRuleGroups/* |  |
> | [Microsoft.Monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor)/investigations/* |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.PolicyInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftpolicyinsights)/remediations/* |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/* |  |
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
  "description": "Allows read access to all monitoring data, update permissions for monitoring settings and permissions to deploy and remediate Azure Monitor alert policies.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/47be4a87-7950-4631-9daf-b664a405f074",
  "name": "47be4a87-7950-4631-9daf-b664a405f074",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.AlertsManagement/alerts/*",
        "Microsoft.AlertsManagement/alertsSummary/*",
        "Microsoft.AlertsManagement/issues/*",
        "Microsoft.Insights/actiongroups/*",
        "Microsoft.Insights/activityLogAlerts/*",
        "Microsoft.Insights/AlertRules/*",
        "Microsoft.Insights/components/*",
        "Microsoft.Insights/createNotifications/*",
        "Microsoft.Insights/dataCollectionEndpoints/*",
        "Microsoft.Insights/dataCollectionRules/*",
        "Microsoft.Insights/dataCollectionRuleAssociations/*",
        "Microsoft.Insights/DiagnosticSettings/*",
        "Microsoft.Insights/eventtypes/*",
        "Microsoft.Insights/LogDefinitions/*",
        "Microsoft.Insights/metricalerts/*",
        "Microsoft.Insights/MetricDefinitions/*",
        "Microsoft.Insights/Metrics/*",
        "Microsoft.Insights/notificationStatus/*",
        "Microsoft.Insights/Register/Action",
        "Microsoft.Insights/scheduledqueryrules/*",
        "Microsoft.Insights/webtests/*",
        "Microsoft.Insights/workbooks/*",
        "Microsoft.Insights/workbooktemplates/*",
        "Microsoft.Insights/privateLinkScopes/*",
        "Microsoft.Insights/privateLinkScopeOperationStatuses/*",
        "Microsoft.Monitor/accounts/*",
        "Microsoft.OperationalInsights/workspaces/write",
        "Microsoft.OperationalInsights/workspaces/intelligencepacks/*",
        "Microsoft.OperationalInsights/workspaces/savedSearches/*",
        "Microsoft.OperationalInsights/workspaces/search/action",
        "Microsoft.OperationalInsights/workspaces/sharedKeys/action",
        "Microsoft.OperationalInsights/workspaces/sharedKeys/read",
        "Microsoft.OperationalInsights/workspaces/storageinsightconfigs/*",
        "Microsoft.OperationalInsights/locations/workspaces/failover/action",
        "Microsoft.OperationalInsights/workspaces/failback/action",
        "Microsoft.Support/*",
        "Microsoft.AlertsManagement/smartDetectorAlertRules/*",
        "Microsoft.AlertsManagement/actionRules/*",
        "Microsoft.AlertsManagement/smartGroups/*",
        "Microsoft.AlertsManagement/migrateFromSmartDetection/*",
        "Microsoft.AlertsManagement/investigations/*",
        "Microsoft.AlertsManagement/prometheusRuleGroups/*",
        "Microsoft.Monitor/investigations/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.PolicyInsights/remediations/*",
        "Microsoft.Resources/subscriptions/resourceGroups/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Monitoring Policy Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Monitoring Reader

Can read all monitoring data (metrics, logs, etc.). See also [Get started with roles, permissions, and security with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/roles-permissions-security#built-in-monitoring-roles).

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-monitor/roles-permissions-security)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights)/workspaces/search/action | Executes a search query |
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
  "description": "Can read all monitoring data.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/43d0d8ad-25c7-4714-9337-8ba259a9fe05",
  "name": "43d0d8ad-25c7-4714-9337-8ba259a9fe05",
  "permissions": [
    {
      "actions": [
        "*/read",
        "Microsoft.OperationalInsights/workspaces/search/action",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Monitoring Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Service Health Security Reader

Grants permissions to view sensitive security information present in service health events

[Learn more](https://learn.microsoft.com/en-us/azure/service-health/impacted-resources-security)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/events/action | Endpoint to fetch details for event |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/AvailabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/AvailabilityStatuses/current/read | Gets the availability status for the specified resource |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/Operations/read | Get the operations available for the Microsoft ResourceHealth |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/emergingissues/read | Get Azure services' emerging issues |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/events/read | Get Service Health Events for given subscription |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/events/fetchEventDetails/action | Endpoint to fetch details for event |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/events/listSecurityAdvisoryImpactedResources/action | Get Impacted Resources for a given event of type SecurityAdvisory |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/events/impactedResources/read | Get Impacted Resources for a given event |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/metadata/read | Gets Metadata |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/potentialoutages/read | Get Potential Outages for given subscription |
> | **NotActions** |  |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/events/fetchBillingCommunicationDetails/action | Get Billing details for a given subscription and tracking id |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants permissions to view sensitive security information present in service health events",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/1a928ab0-1fee-43cf-9266-f9d8c22a8ddb",
  "name": "1a928ab0-1fee-43cf-9266-f9d8c22a8ddb",
  "permissions": [
    {
      "actions": [
        "Microsoft.ResourceHealth/events/action",
        "Microsoft.ResourceHealth/AvailabilityStatuses/read",
        "Microsoft.ResourceHealth/AvailabilityStatuses/current/read",
        "Microsoft.ResourceHealth/Operations/read",
        "Microsoft.ResourceHealth/emergingissues/read",
        "Microsoft.ResourceHealth/events/read",
        "Microsoft.ResourceHealth/events/fetchEventDetails/action",
        "Microsoft.ResourceHealth/events/listSecurityAdvisoryImpactedResources/action",
        "Microsoft.ResourceHealth/events/impactedResources/read",
        "Microsoft.ResourceHealth/metadata/read",
        "Microsoft.ResourceHealth/potentialoutages/read"
      ],
      "notActions": [
        "Microsoft.ResourceHealth/events/fetchBillingCommunicationDetails/action"
      ],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Service Health Security Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Workbook Contributor

Can save shared workbooks.

[Learn more](https://learn.microsoft.com/en-us/azure/sentinel/tutorial-monitor-your-data)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/write | Create or update a workbook |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/delete | Delete a workbook |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/read | Read a workbook |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/revisions/read | Get the workbook revisions |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooktemplates/write | Create or update a workbook template |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooktemplates/delete | Delete a workbook template |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooktemplates/read | Read a workbook template |
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
  "description": "Can save shared workbooks.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/e8ddcd69-c73f-4f9f-9844-4100522f16ad",
  "name": "e8ddcd69-c73f-4f9f-9844-4100522f16ad",
  "permissions": [
    {
      "actions": [
        "Microsoft.Insights/workbooks/write",
        "Microsoft.Insights/workbooks/delete",
        "Microsoft.Insights/workbooks/read",
        "Microsoft.Insights/workbooks/revisions/read",
        "Microsoft.Insights/workbooktemplates/write",
        "Microsoft.Insights/workbooktemplates/delete",
        "Microsoft.Insights/workbooktemplates/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Workbook Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Workbook Reader

Can read workbooks.

[Learn more](https://learn.microsoft.com/en-us/azure/sentinel/tutorial-monitor-your-data)

> | Actions | Description |
> | --- | --- |
> | [microsoft.insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/read | Read a workbook |
> | [microsoft.insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooks/revisions/read | Get the workbook revisions |
> | [microsoft.insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/workbooktemplates/read | Read a workbook template |
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
  "description": "Can read workbooks.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/b279062a-9be3-42a0-92ae-8b3cf002ec4d",
  "name": "b279062a-9be3-42a0-92ae-8b3cf002ec4d",
  "permissions": [
    {
      "actions": [
        "microsoft.insights/workbooks/read",
        "microsoft.insights/workbooks/revisions/read",
        "microsoft.insights/workbooktemplates/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Workbook Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
