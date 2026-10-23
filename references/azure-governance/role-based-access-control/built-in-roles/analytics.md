# Azure built-in roles for Analytics - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/analytics  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the Analytics category.

## Azure Event Hubs Data Owner

Allows for full access to Azure Event Hubs resources.

[Learn more](https://learn.microsoft.com/en-us/azure/event-hubs/authenticate-application)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows for full access to Azure Event Hubs resources.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/f526a384-b230-433a-b45c-95f59c4a2dec",
  "name": "f526a384-b230-433a-b45c-95f59c4a2dec",
  "permissions": [
    {
      "actions": [
        "Microsoft.EventHub/*"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.EventHub/*"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Event Hubs Data Owner",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Event Hubs Data Receiver

Allows receive access to Azure Event Hubs resources.

[Learn more](https://learn.microsoft.com/en-us/azure/event-hubs/authenticate-application)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/*/eventhubs/consumergroups/read |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/*/receive/action |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows receive access to Azure Event Hubs resources.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/a638d3c7-ab3a-418d-83e6-5f17a39d4fde",
  "name": "a638d3c7-ab3a-418d-83e6-5f17a39d4fde",
  "permissions": [
    {
      "actions": [
        "Microsoft.EventHub/*/eventhubs/consumergroups/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.EventHub/*/receive/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Event Hubs Data Receiver",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Event Hubs Data Sender

Allows send access to Azure Event Hubs resources.

[Learn more](https://learn.microsoft.com/en-us/azure/event-hubs/authenticate-application)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/*/eventhubs/read |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/*/send/action |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Allows send access to Azure Event Hubs resources.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/2b629674-e913-4c01-ae53-ef4638d8f975",
  "name": "2b629674-e913-4c01-ae53-ef4638d8f975",
  "permissions": [
    {
      "actions": [
        "Microsoft.EventHub/*/eventhubs/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.EventHub/*/send/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Event Hubs Data Sender",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Data Factory Contributor

Create and manage data factories, as well as child resources within them.

[Learn more](https://learn.microsoft.com/en-us/azure/data-factory/concepts-roles-permissions)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.DataFactory](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftdatafactory)/dataFactories/* | Create and manage data factories, and child resources within them. |
> | [Microsoft.DataFactory](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftdatafactory)/factories/* | Create and manage data factories, and child resources within them. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.EventGrid](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventgrid)/eventSubscriptions/write | Create or update an eventSubscription |
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
  "description": "Create and manage data factories, as well as child resources within them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/673868aa-7521-48a0-acc6-0f60742d39f5",
  "name": "673868aa-7521-48a0-acc6-0f60742d39f5",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.DataFactory/dataFactories/*",
        "Microsoft.DataFactory/factories/*",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "Microsoft.EventGrid/eventSubscriptions/write"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Data Factory Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## HDInsight Cluster Operator

Lets you read and modify HDInsight cluster configurations.

[Learn more](https://learn.microsoft.com/en-us/azure/hdinsight/hdinsight-migrate-granular-access-cluster-configurations)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/*/read |  |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusters/getGatewaySettings/action | Get gateway settings for HDInsight Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusters/updateGatewaySettings/action | Update gateway settings for HDInsight Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusters/configurations/* |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
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
  "description": "Lets you read and modify HDInsight cluster configurations.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/61ed4efc-fab3-44fd-b111-e24485cc132a",
  "name": "61ed4efc-fab3-44fd-b111-e24485cc132a",
  "permissions": [
    {
      "actions": [
        "Microsoft.HDInsight/*/read",
        "Microsoft.HDInsight/clusters/getGatewaySettings/action",
        "Microsoft.HDInsight/clusters/updateGatewaySettings/action",
        "Microsoft.HDInsight/clusters/configurations/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/operations/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Authorization/*/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "HDInsight Cluster Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## HDInsight Domain Services Contributor

Can Read, Create, Modify and Delete Domain Services related operations needed for HDInsight Enterprise Security Package

[Learn more](https://learn.microsoft.com/en-us/azure/hdinsight/domain-joined/apache-domain-joined-configure-using-azure-adds)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad)/*/read |  |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad)/domainServices/*/read |  |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad)/domainServices/oucontainer/* |  |
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
  "description": "Can Read, Create, Modify and Delete Domain Services related operations needed for HDInsight Enterprise Security Package",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/8d8d5a11-05d3-4bda-a417-a08778121c7c",
  "name": "8d8d5a11-05d3-4bda-a417-a08778121c7c",
  "permissions": [
    {
      "actions": [
        "Microsoft.AAD/*/read",
        "Microsoft.AAD/domainServices/*/read",
        "Microsoft.AAD/domainServices/oucontainer/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "HDInsight Domain Services Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## HDInsight on AKS Cluster Admin

Grants a user/group the ability to create, delete and manage clusters within a given cluster pool. Cluster Admin can also run workloads, monitor, and manage all user activity on these clusters.

[Learn more](https://learn.microsoft.com/en-us/azure/hdinsight-aks/hdinsight-on-aks-manage-authorization-profile)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/read | Get details about HDInsight on AKS Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/write | Create or Update HDInsight on AKS Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/delete | Delete a HDInsight on AKS cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/resize/action | Resize a HDInsight on AKS Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterpools/clusters/instanceviews/read | Get details about HDInsight on AKS Cluster Instance View |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/jobs/read | List HDInsight on AKS Cluster Jobs |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/runjob/action | Run HDInsight on AKS Cluster Job |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterpools/clusters/serviceconfigs/read | Get details about HDInsight on AKS Cluster Service Configurations |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/availableupgrades/read | Get Available Upgrades for HDInsight on AKS Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/upgrade/action | Upgrade HDInsight on AKS Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/rollback/action | Rollback HDInsight on AKS Cluster Upgrade |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/upgradehistories/read | Read HDInsight on AKS Cluster Upgrade Histories |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/libraries/read | Read HDInsight on AKS Cluster Libraries |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/managelibraries/action | Manage HDInsight on AKS Cluster Libraries |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/*/read |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/validate/action | Validates a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/exportTemplate/action | Export template for a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Write | Create or update a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Delete | Delete a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Activated/Action | Classic metric alert activated |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Resolved/Action | Classic metric alert resolved |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Throttled/Action | Classic metric alert rule throttled |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Incidents/Read | Read a classic metric alert incident |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/logs/read | Reading data from all your logs |
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
  "description": "Grants a user/group the ability to create, delete and manage clusters within a given cluster pool. Cluster Admin can also run workloads, monitor, and manage all user activity on these clusters.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/fd036e6b-1266-47a0-b0bb-a05d04831731",
  "name": "fd036e6b-1266-47a0-b0bb-a05d04831731",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.HDInsight/clusterPools/clusters/read",
        "Microsoft.HDInsight/clusterPools/clusters/write",
        "Microsoft.HDInsight/clusterPools/clusters/delete",
        "Microsoft.HDInsight/clusterPools/clusters/resize/action",
        "Microsoft.HDInsight/clusterpools/clusters/instanceviews/read",
        "Microsoft.HDInsight/clusterPools/clusters/jobs/read",
        "Microsoft.HDInsight/clusterPools/clusters/runjob/action",
        "Microsoft.HDInsight/clusterpools/clusters/serviceconfigs/read",
        "Microsoft.HDInsight/clusterPools/clusters/availableupgrades/read",
        "Microsoft.HDInsight/clusterPools/clusters/upgrade/action",
        "Microsoft.HDInsight/clusterPools/clusters/rollback/action",
        "Microsoft.HDInsight/clusterPools/clusters/upgradehistories/read",
        "Microsoft.HDInsight/clusterPools/clusters/libraries/read",
        "Microsoft.HDInsight/clusterPools/clusters/managelibraries/action",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/operations/read",
        "Microsoft.Resources/deployments/*/read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Resources/deployments/validate/action",
        "Microsoft.Resources/deployments/write",
        "Microsoft.Resources/deployments/exportTemplate/action",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "Microsoft.Insights/AlertRules/Write",
        "Microsoft.Insights/AlertRules/Delete",
        "Microsoft.Insights/AlertRules/Read",
        "Microsoft.Insights/AlertRules/Activated/Action",
        "Microsoft.Insights/AlertRules/Resolved/Action",
        "Microsoft.Insights/AlertRules/Throttled/Action",
        "Microsoft.Insights/AlertRules/Incidents/Read",
        "Microsoft.Insights/metrics/read",
        "Microsoft.Insights/logs/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "HDInsight on AKS Cluster Admin",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## HDInsight on AKS Cluster Pool Admin

Can read, create, modify and delete HDInsight on AKS cluster pools and create clusters

[Learn more](https://learn.microsoft.com/en-us/azure/hdinsight-aks/hdinsight-on-aks-manage-authorization-profile)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/read | Get details about HDInsight on AKS Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/clusters/write | Create or Update HDInsight on AKS Cluster |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/delete | Delete a HDInsight on AKS Cluster Pool |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/read | Get details about HDInsight on AKS Cluster Pool |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/write | Create or Update HDInsight on AKS Cluster Pool |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterpools/availableupgrades/read | Get Available Upgrades for HDInsight on AKS Cluster Pool |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterpools/upgrade/action | Upgrade HDInsight on AKS Cluster Pool |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight)/clusterPools/upgradehistories/read | Read HDInsight on AKS Cluster Pool Upgrade Histories |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/validate/action | Validates a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/*/read |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/exportTemplate/action | Export template for a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/validate/action | Validates a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Write | Create or update a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Delete | Delete a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Activated/Action | Classic metric alert activated |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Resolved/Action | Classic metric alert resolved |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Throttled/Action | Classic metric alert rule throttled |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Incidents/Read | Read a classic metric alert incident |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/logs/read | Reading data from all your logs |
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
  "description": "Can read, create, modify and delete HDInsight on AKS cluster pools and create clusters",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/7656b436-37d4-490a-a4ab-d39f838f0042",
  "name": "7656b436-37d4-490a-a4ab-d39f838f0042",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.HDInsight/clusterPools/clusters/read",
        "Microsoft.HDInsight/clusterPools/clusters/write",
        "Microsoft.HDInsight/clusterPools/delete",
        "Microsoft.HDInsight/clusterPools/read",
        "Microsoft.HDInsight/clusterPools/write",
        "Microsoft.HDInsight/clusterpools/availableupgrades/read",
        "Microsoft.HDInsight/clusterpools/upgrade/action",
        "Microsoft.HDInsight/clusterPools/upgradehistories/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/operations/read",
        "Microsoft.Resources/deployments/validate/action",
        "Microsoft.Resources/deployments/*/read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Resources/deployments/write",
        "Microsoft.Resources/deployments/exportTemplate/action",
        "Microsoft.Resources/deployments/validate/action",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "Microsoft.Insights/AlertRules/Write",
        "Microsoft.Insights/AlertRules/Delete",
        "Microsoft.Insights/AlertRules/Read",
        "Microsoft.Insights/AlertRules/Activated/Action",
        "Microsoft.Insights/AlertRules/Resolved/Action",
        "Microsoft.Insights/AlertRules/Throttled/Action",
        "Microsoft.Insights/AlertRules/Incidents/Read",
        "Microsoft.Insights/metrics/read",
        "Microsoft.Insights/logs/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "HDInsight on AKS Cluster Pool Admin",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Schema Registry Contributor

Read, write, and delete Schema Registry groups and schemas.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/namespaces/schemagroups/* |  |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/namespaces/schemas/* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Read, write, and delete Schema Registry groups and schemas.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5dffeca3-4936-4216-b2bc-10343a5abb25",
  "name": "5dffeca3-4936-4216-b2bc-10343a5abb25",
  "permissions": [
    {
      "actions": [
        "Microsoft.EventHub/namespaces/schemagroups/*"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.EventHub/namespaces/schemas/*"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Schema Registry Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Schema Registry Reader

Read and list Schema Registry groups and schemas.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/namespaces/schemagroups/read | Get list of SchemaGroup Resource Descriptions |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub)/namespaces/schemas/read | Retrieve schemas |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Read and list Schema Registry groups and schemas.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/2c56ea50-c6b3-40a6-83c0-9d98858bc7d2",
  "name": "2c56ea50-c6b3-40a6-83c0-9d98858bc7d2",
  "permissions": [
    {
      "actions": [
        "Microsoft.EventHub/namespaces/schemagroups/read"
      ],
      "notActions": [],
      "dataActions": [
        "Microsoft.EventHub/namespaces/schemas/read"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Schema Registry Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Stream Analytics Query Tester

Lets you perform query testing without creating a stream analytics job first

> | Actions | Description |
> | --- | --- |
> | [Microsoft.StreamAnalytics](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftstreamanalytics)/locations/TestQuery/action | Test Query for Stream Analytics Resource Provider |
> | [Microsoft.StreamAnalytics](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftstreamanalytics)/locations/OperationResults/read | Read Stream Analytics Operation Result |
> | [Microsoft.StreamAnalytics](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftstreamanalytics)/locations/SampleInput/action | Sample Input for Stream Analytics Resource Provider |
> | [Microsoft.StreamAnalytics](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftstreamanalytics)/locations/CompileQuery/action | Compile Query for Stream Analytics Resource Provider |
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
  "description": "Lets you perform query testing without creating a stream analytics job first",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/1ec5b3c1-b17e-4e25-8312-2acb3c3c5abf",
  "name": "1ec5b3c1-b17e-4e25-8312-2acb3c3c5abf",
  "permissions": [
    {
      "actions": [
        "Microsoft.StreamAnalytics/locations/TestQuery/action",
        "Microsoft.StreamAnalytics/locations/OperationResults/read",
        "Microsoft.StreamAnalytics/locations/SampleInput/action",
        "Microsoft.StreamAnalytics/locations/CompileQuery/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Stream Analytics Query Tester",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
