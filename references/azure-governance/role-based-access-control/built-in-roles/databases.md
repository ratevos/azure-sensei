# Azure built-in roles for Databases - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/databases  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the Databases category.

## Azure Connected SQL Server Onboarding

Allows for read and write access to Azure resources for SQL Server on Arc-enabled servers.

[Learn more](https://learn.microsoft.com/en-us/sql/sql-server/azure-arc/connect)

> | Actions | Description |
> | --- | --- |
> | Microsoft.AzureArcData/sqlServerInstances/read | Retrieves a SQL Server Instance resource |
> | Microsoft.AzureArcData/sqlServerInstances/write | Updates a SQL Server Instance resource |
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
  "description": "Microsoft.AzureArcData service role to access the resources of Microsoft.AzureArcData stored with RPSAAS.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/e8113dce-c529-4d33-91fa-e9b972617508",
  "name": "e8113dce-c529-4d33-91fa-e9b972617508",
  "permissions": [
    {
      "actions": [
        "Microsoft.AzureArcData/sqlServerInstances/read",
        "Microsoft.AzureArcData/sqlServerInstances/write"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Connected SQL Server Onboarding",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Managed Redis Contributor

Create and manage Azure Managed Redis resources. Cannot read or write data stored in the cache.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/locations/operationsStatus/read | View the status of a long running operation for which the 'AzureAsync' header was previously returned to the client |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/locations/checknameavailability/action | Checks if a name is available for use with a new Redis Enterprise cache |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/operations/read | Lists the operations that 'Microsoft.Cache' provider supports. |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/redisEnterprise/* | Create and manage Azure Managed Redis resources |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
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
  "description": "Lets you manage Azure Managed Redis resources, but not access the data stored in them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/3015e5ed-6856-4ab3-b2f0-b8492aa30ca6",
  "name": "3015e5ed-6856-4ab3-b2f0-b8492aa30ca6",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Cache/locations/operationsStatus/read",
        "Microsoft.Cache/locations/checknameavailability/action",
        "Microsoft.Cache/operations/read",
        "Microsoft.Cache/redisEnterprise/*",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Managed Redis Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Managed Redis Reader

Read Azure Managed Redis resources and their configuration. Cannot modify resources, retrieve access keys, or read data stored in the cache.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/locations/operationsStatus/read | View the status of a long running operation for which the 'AzureAsync' header was previously returned to the client |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/operations/read | Lists the operations that 'Microsoft.Cache' provider supports. |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/redisEnterprise/read | View Azure Managed Redis resource's settings and configurations |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/redisEnterprise/*/read | Gets or lists Azure Managed Redis resources |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/read | Read a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/read | Gets or lists deployments. |
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
  "description": "Read Azure Managed Redis resources and their configuration. Cannot modify resources, retrieve access keys, or read data stored in the cache.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/f287ba2f-f923-4464-a5bd-721c3951d32d",
  "name": "f287ba2f-f923-4464-a5bd-721c3951d32d",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Cache/locations/operationsStatus/read",
        "Microsoft.Cache/operations/read",
        "Microsoft.Cache/redisEnterprise/read",
        "Microsoft.Cache/redisEnterprise/*/read",
        "Microsoft.Insights/alertRules/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Managed Redis Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Cosmos DB Account Reader Role

Can read Azure Cosmos DB account data. See [DocumentDB Account Contributor](#documentdb-account-contributor) for managing Azure Cosmos DB accounts.

[Learn more](https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/*/read | Read any collection |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/readonlykeys/action | Reads the database account readonly keys. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/MetricDefinitions/read | Read metric definitions |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Metrics/read | Read metrics |
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
  "description": "Can read Azure Cosmos DB Accounts data",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/fbdf93bf-df7d-467e-a4d2-9458aa1360c8",
  "name": "fbdf93bf-df7d-467e-a4d2-9458aa1360c8",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.DocumentDB/*/read",
        "Microsoft.DocumentDB/databaseAccounts/readonlykeys/action",
        "Microsoft.Insights/MetricDefinitions/read",
        "Microsoft.Insights/Metrics/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Cosmos DB Account Reader Role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Cosmos DB Operator

Lets you manage Azure Cosmos DB accounts, but not access data in them. Prevents access to account keys and connection strings.

[Learn more](https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.DocumentDb](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/joinViaServiceEndpoint/action | Joins resource such as storage account or SQL database to a subnet. Not alertable. |
> | **NotActions** |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/copyJobs/* |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/dataTransferJobs/* |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/readonlyKeys/* |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/regenerateKey/* |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/listKeys/* |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/listConnectionStrings/* |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/sqlRoleDefinitions/write | Create or update a SQL Role Definition |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/sqlRoleDefinitions/delete | Delete a SQL Role Definition |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/sqlRoleAssignments/write | Create or update a SQL Role Assignment |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/sqlRoleAssignments/delete | Delete a SQL Role Assignment |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongodbRoleDefinitions/write | Create or update a Mongo Role Definition |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongodbRoleDefinitions/delete | Delete a MongoDB Role Definition |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongodbUserDefinitions/write | Create or update a MongoDB User Definition |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongodbUserDefinitions/delete | Delete a MongoDB User Definition |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/tableRoleAssignments/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/tableRoleAssignments/delete |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/tableRoleDefinitions/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/tableRoleDefinitions/delete |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/gremlinRoleAssignments/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/gremlinRoleAssignments/delete |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/gremlinRoleDefinitions/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/gremlinRoleDefinitions/delete |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/cassandraRoleAssignments/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/cassandraRoleAssignments/delete |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/cassandraRoleDefinitions/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/cassandraRoleDefinitions/delete |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongoMIRoleAssignments/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongoMIRoleAssignments/delete |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongoMIRoleDefinitions/write |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/mongoMIRoleDefinitions/delete |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you manage Azure Cosmos DB accounts, but not access data in them. Prevents access to account keys and connection strings.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/230815da-be43-4aae-9cb4-875f7bd000aa",
  "name": "230815da-be43-4aae-9cb4-875f7bd000aa",
  "permissions": [
    {
      "actions": [
        "Microsoft.DocumentDb/databaseAccounts/*",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Authorization/*/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "Microsoft.Network/virtualNetworks/subnets/joinViaServiceEndpoint/action"
      ],
      "notActions": [
        "Microsoft.DocumentDB/databaseAccounts/copyJobs/*",
        "Microsoft.DocumentDB/databaseAccounts/dataTransferJobs/*",
        "Microsoft.DocumentDB/databaseAccounts/readonlyKeys/*",
        "Microsoft.DocumentDB/databaseAccounts/regenerateKey/*",
        "Microsoft.DocumentDB/databaseAccounts/listKeys/*",
        "Microsoft.DocumentDB/databaseAccounts/listConnectionStrings/*",
        "Microsoft.DocumentDB/databaseAccounts/sqlRoleDefinitions/write",
        "Microsoft.DocumentDB/databaseAccounts/sqlRoleDefinitions/delete",
        "Microsoft.DocumentDB/databaseAccounts/sqlRoleAssignments/write",
        "Microsoft.DocumentDB/databaseAccounts/sqlRoleAssignments/delete",
        "Microsoft.DocumentDB/databaseAccounts/mongodbRoleDefinitions/write",
        "Microsoft.DocumentDB/databaseAccounts/mongodbRoleDefinitions/delete",
        "Microsoft.DocumentDB/databaseAccounts/mongodbUserDefinitions/write",
        "Microsoft.DocumentDB/databaseAccounts/mongodbUserDefinitions/delete",
        "Microsoft.DocumentDB/databaseAccounts/tableRoleAssignments/write",
        "Microsoft.DocumentDB/databaseAccounts/tableRoleAssignments/delete",
        "Microsoft.DocumentDB/databaseAccounts/tableRoleDefinitions/write",
        "Microsoft.DocumentDB/databaseAccounts/tableRoleDefinitions/delete",
        "Microsoft.DocumentDB/databaseAccounts/gremlinRoleAssignments/write",
        "Microsoft.DocumentDB/databaseAccounts/gremlinRoleAssignments/delete",
        "Microsoft.DocumentDB/databaseAccounts/gremlinRoleDefinitions/write",
        "Microsoft.DocumentDB/databaseAccounts/gremlinRoleDefinitions/delete",
        "Microsoft.DocumentDB/databaseAccounts/cassandraRoleAssignments/write",
        "Microsoft.DocumentDB/databaseAccounts/cassandraRoleAssignments/delete",
        "Microsoft.DocumentDB/databaseAccounts/cassandraRoleDefinitions/write",
        "Microsoft.DocumentDB/databaseAccounts/cassandraRoleDefinitions/delete",
        "Microsoft.DocumentDB/databaseAccounts/mongoMIRoleAssignments/write",
        "Microsoft.DocumentDB/databaseAccounts/mongoMIRoleAssignments/delete",
        "Microsoft.DocumentDB/databaseAccounts/mongoMIRoleDefinitions/write",
        "Microsoft.DocumentDB/databaseAccounts/mongoMIRoleDefinitions/delete"
      ],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Cosmos DB Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## CosmosBackupOperator

Can submit restore request for a Cosmos DB database or a container for an account

[Learn more](https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/backup/action | Submit a request to trigger external backup operation |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/restore/action | Submit a request to trigger external restore operation |
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
  "description": "Can submit restore request for a Cosmos DB database or a container for an account",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/db7b14f2-5adf-42da-9f96-f2ee17bab5cb",
  "name": "db7b14f2-5adf-42da-9f96-f2ee17bab5cb",
  "permissions": [
    {
      "actions": [
        "Microsoft.DocumentDB/databaseAccounts/backup/action",
        "Microsoft.DocumentDB/databaseAccounts/restore/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "CosmosBackupOperator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## CosmosRestoreOperator

Can perform restore action for Cosmos DB database account with continuous backup mode

> | Actions | Description |
> | --- | --- |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/locations/restorableDatabaseAccounts/restore/action | Submit a restore request |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/locations/restorableDatabaseAccounts/*/read |  |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/locations/restorableDatabaseAccounts/read | Read a restorable database account or List all the restorable database accounts |
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
  "description": "Can perform restore action for Cosmos DB database account with continuous backup mode",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5432c526-bc82-444a-b7ba-57c5b0b5b34f",
  "name": "5432c526-bc82-444a-b7ba-57c5b0b5b34f",
  "permissions": [
    {
      "actions": [
        "Microsoft.DocumentDB/locations/restorableDatabaseAccounts/restore/action",
        "Microsoft.DocumentDB/locations/restorableDatabaseAccounts/*/read",
        "Microsoft.DocumentDB/locations/restorableDatabaseAccounts/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "CosmosRestoreOperator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## DocumentDB Account Contributor

Can manage Azure Cosmos DB accounts. Azure Cosmos DB is formerly known as DocumentDB.

[Learn more](https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.DocumentDb](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb)/databaseAccounts/* | Create and manage Azure Cosmos DB accounts |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/joinViaServiceEndpoint/action | Joins resource such as storage account or SQL database to a subnet. Not alertable. |
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
  "description": "Lets you manage DocumentDB accounts, but not access to them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5bd9cd88-fe45-4216-938b-f97437e15450",
  "name": "5bd9cd88-fe45-4216-938b-f97437e15450",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.DocumentDb/databaseAccounts/*",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Support/*",
        "Microsoft.Network/virtualNetworks/subnets/joinViaServiceEndpoint/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "DocumentDB Account Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## PostgreSQL Flexible Server Long Term Retention Backup Role

Role to allow backup vault to access PostgreSQL Flexible Server Resource APIs for Long Term Retention Backup.

[Learn more](https://learn.microsoft.com/en-us/azure/backup/backup-azure-database-postgresql-flex-overview)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrBackup/action | Start LTR backup operation for a server |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrBackupAccess/action | Start LTR backup access operation for a server |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrBackupOperations/read | Returns the list of  PostgreSQL server long term backup operation tracking. |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrBackupPreCheck/action | Start LTR backup pre-check operation for a server |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrPreBackup/action | Checks if a server is ready for a long term backup |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrRestoreFinalize/action | Start LTR restore finalize operation for a server |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrRestoreInitialize/action | Start LTR restore initialize operation for a server |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/ltrRestorePreCheck/action | Start LTR restore pre-check operation for a server |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/read | Return the list of servers or gets the properties for the specified server. |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/flexibleServers/startLtrBackup/action | Start long term backup for a server |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/locations/azureAsyncOperation/read | Return PostgreSQL Server Operation Results |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql)/locations/operationResults/read | Return PostgreSQL Server Operation Results |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
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
  "description": "Role to allow backup vault to access PostgreSQL Flexible Server Resource APIs for Long Term Retention Backup.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/c088a766-074b-43ba-90d4-1fb21feae531",
  "name": "c088a766-074b-43ba-90d4-1fb21feae531",
  "permissions": [
    {
      "actions": [
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrBackup/action",
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrBackupAccess/action",
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrBackupOperations/read",
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrBackupPreCheck/action",
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrPreBackup/action",
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrRestoreFinalize/action",
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrRestoreInitialize/action",
        "Microsoft.DBforPostgreSQL/flexibleServers/ltrRestorePreCheck/action",
        "Microsoft.DBforPostgreSQL/flexibleServers/read",
        "Microsoft.DBforPostgreSQL/flexibleServers/startLtrBackup/action",
        "Microsoft.DBforPostgreSQL/locations/azureAsyncOperation/read",
        "Microsoft.DBforPostgreSQL/locations/operationResults/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "PostgreSQL Flexible Server Long Term Retention Backup Role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Redis Cache Contributor

Create and manage Azure Cache for Redis resources. Cannot read or write data stored in the cache.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/register/action | Registers the 'Microsoft.Cache' resource provider with a subscription |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache)/redis/* | Create and manage Azure Cache for Redis resources |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
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
  "description": "Create and manage Azure Cache for Redis resources. Cannot read or write data stored in the cache.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/e0f68234-74aa-48ed-b826-c38b57376e17",
  "name": "e0f68234-74aa-48ed-b826-c38b57376e17",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Cache/register/action",
        "Microsoft.Cache/redis/*",
        "Microsoft.Insights/alertRules/*",
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
  "roleName": "Redis Cache Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Semantic Reranker User

Execute semantic reranking operations against registered inference accounts. This role should be assigned to users who need to run semantic reranking workloads but do not need to manage the accounts themselves.

[Learn more](https://learn.microsoft.com/en-us/azure/cosmos-db/gen-ai/semantic-reranker)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.InferenceService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftinferenceservice)/inferenceAccounts/read | Reads an inference service. |
> | **NotActions** |  |
> | [Microsoft.InferenceService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftinferenceservice)/inferenceAccounts/write | Creates or updates an inference service. |
> | [Microsoft.InferenceService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftinferenceservice)/inferenceAccounts/delete | Deletes an inference service. |
> | **DataActions** |  |
> | [Microsoft.InferenceService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftinferenceservice)/inferenceAccounts/invoke/semanticReranker/action | Invokes the semantic reranker on an inference account. |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Execute semantic reranking operations against registered inference accounts. This role should be assigned to users who need to run semantic reranking workloads but do not need to manage the accounts themselves.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/6c74a7c5-4a87-40f9-bb03-61e49aecbc78",
  "name": "6c74a7c5-4a87-40f9-bb03-61e49aecbc78",
  "permissions": [
    {
      "actions": [
        "Microsoft.InferenceService/inferenceAccounts/read"
      ],
      "notActions": [
        "Microsoft.InferenceService/inferenceAccounts/write",
        "Microsoft.InferenceService/inferenceAccounts/delete"
      ],
      "dataActions": [
        "Microsoft.InferenceService/inferenceAccounts/invoke/semanticReranker/action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "Semantic Reranker User",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## SQL DB Contributor

Lets you manage SQL databases, including copying, restoring, exporting, deleting, and configuring certain database-level security settings such as identities, encryption protectors, and enclaves. Although it grants no SQL query permissions directly, its data-movement capabilities can enable access to or exfiltration of database data. It cannot manage parent SQL servers and excludes the security-related operations listed in NotActions.

[Learn more](https://learn.microsoft.com/en-us/azure/data-share/concepts-roles-permissions)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/*/read |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/* | Create and manage SQL databases |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/read | Return the list of servers or gets the properties for the specified server. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricDefinitions/read | Read metric definitions |
> | **NotActions** |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/ledgerDigestUploads/write | Enable uploading ledger digests  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/ledgerDigestUploads/disable/action | Disable uploading ledger digests |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/currentSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/recommendedSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/schemas/tables/columns/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/securityAlertPolicies/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/securityAlertPolicies/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/auditingSettings/* | Edit audit settings |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/auditRecords/read | Retrieve the database blob audit records |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/currentSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/dataMaskingPolicies/* | Edit data masking policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/extendedAuditingSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/recommendedSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/schemas/tables/columns/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/securityAlertPolicies/* | Edit security alert policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/securityMetrics/* | Edit security metrics |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessmentScans/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessmentSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/vulnerabilityAssessments/* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you manage SQL databases, but not access to them. Also, you can't manage their security-related policies or their parent SQL servers.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/9b7fa17d-e63e-47b0-bb0a-15c516ac86ec",
  "name": "9b7fa17d-e63e-47b0-bb0a-15c516ac86ec",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Sql/locations/*/read",
        "Microsoft.Sql/servers/databases/*",
        "Microsoft.Sql/servers/read",
        "Microsoft.Support/*",
        "Microsoft.Insights/metrics/read",
        "Microsoft.Insights/metricDefinitions/read"
      ],
      "notActions": [
        "Microsoft.Sql/servers/databases/ledgerDigestUploads/write",
        "Microsoft.Sql/servers/databases/ledgerDigestUploads/disable/action",
        "Microsoft.Sql/managedInstances/databases/currentSensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/recommendedSensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/schemas/tables/columns/sensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/securityAlertPolicies/*",
        "Microsoft.Sql/managedInstances/databases/sensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/vulnerabilityAssessments/*",
        "Microsoft.Sql/managedInstances/securityAlertPolicies/*",
        "Microsoft.Sql/managedInstances/vulnerabilityAssessments/*",
        "Microsoft.Sql/servers/databases/auditingSettings/*",
        "Microsoft.Sql/servers/databases/auditRecords/read",
        "Microsoft.Sql/servers/databases/currentSensitivityLabels/*",
        "Microsoft.Sql/servers/databases/dataMaskingPolicies/*",
        "Microsoft.Sql/servers/databases/extendedAuditingSettings/*",
        "Microsoft.Sql/servers/databases/recommendedSensitivityLabels/*",
        "Microsoft.Sql/servers/databases/schemas/tables/columns/sensitivityLabels/*",
        "Microsoft.Sql/servers/databases/securityAlertPolicies/*",
        "Microsoft.Sql/servers/databases/securityMetrics/*",
        "Microsoft.Sql/servers/databases/sensitivityLabels/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessments/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessmentScans/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessmentSettings/*",
        "Microsoft.Sql/servers/vulnerabilityAssessments/*"
      ],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "SQL DB Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## SQL Managed Instance Contributor

Lets you manage SQL Managed Instances and required network configuration, but can't give access to others.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/* |  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/*/read |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/instanceFailoverGroups/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/* |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/* |  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/* |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricDefinitions/read | Read metric definitions |
> | **NotActions** |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/azureADOnlyAuthentications/delete | Deletes a specific managed server Azure Active Directory only authentication object |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/azureADOnlyAuthentications/write | Adds or updates a specific managed server Azure Active Directory only authentication object |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you manage SQL Managed Instances and required network configuration, but can't give access to others.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/4939a1f6-9ae0-4e48-a1e0-f2cbe897382d",
  "name": "4939a1f6-9ae0-4e48-a1e0-f2cbe897382d",
  "permissions": [
    {
      "actions": [
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Network/networkSecurityGroups/*",
        "Microsoft.Network/routeTables/*",
        "Microsoft.Sql/locations/*/read",
        "Microsoft.Sql/locations/instanceFailoverGroups/*",
        "Microsoft.Sql/managedInstances/*",
        "Microsoft.Support/*",
        "Microsoft.Network/virtualNetworks/subnets/*",
        "Microsoft.Network/virtualNetworks/*",
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Insights/metrics/read",
        "Microsoft.Insights/metricDefinitions/read"
      ],
      "notActions": [
        "Microsoft.Sql/managedInstances/azureADOnlyAuthentications/delete",
        "Microsoft.Sql/managedInstances/azureADOnlyAuthentications/write"
      ],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "SQL Managed Instance Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## SQL Security Manager

Lets you manage the security-related policies of SQL servers and databases, but not access to them.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-sql/database/azure-defender-for-sql)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/joinViaServiceEndpoint/action | Joins resource such as storage account or SQL database to a subnet. Not alertable. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/administratorAzureAsyncOperation/read | Gets the Managed instance azure async administrator operations result. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/advancedThreatProtectionSettings/read | Retrieve a list of managed instance Advanced Threat Protection settings configured for a given instance |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/advancedThreatProtectionSettings/write | Change the managed instance Advanced Threat Protection settings for a given managed instance |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/advancedThreatProtectionSettings/read | Retrieve a list of the managed database Advanced Threat Protection settings configured for a given managed database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/advancedThreatProtectionSettings/write | Change the database Advanced Threat Protection settings for a given managed database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/advancedThreatProtectionSettings/read | Retrieve a list of managed instance Advanced Threat Protection settings configured for a given instance |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/advancedThreatProtectionSettings/write | Change the managed instance Advanced Threat Protection settings for a given managed instance |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/advancedThreatProtectionSettings/read | Retrieve a list of the managed database Advanced Threat Protection settings configured for a given managed database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/advancedThreatProtectionSettings/write | Change the database Advanced Threat Protection settings for a given managed database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/currentSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/recommendedSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/schemas/tables/columns/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/securityAlertPolicies/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/advancedThreatProtectionSettings/read | Retrieve a list of server Advanced Threat Protection settings configured for a given server |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/advancedThreatProtectionSettings/write | Change the server Advanced Threat Protection settings for a given server |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/securityAlertPolicies/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/transparentDataEncryption/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/serverConfigurationOptions/read | Gets properties for the specified Azure SQL Managed Instance Server Configuration Option. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/serverConfigurationOptions/write | Updates Azure SQL Managed Instance's Server Configuration Option properties for the specified instance. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/serverConfigurationOptionAzureAsyncOperation/read | Gets the status of Azure SQL Managed Instance Server Configuration Option Azure async operation. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/advancedThreatProtectionSettings/read | Retrieve a list of server Advanced Threat Protection settings configured for a given server |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/advancedThreatProtectionSettings/write | Change the server Advanced Threat Protection settings for a given server |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/auditingSettings/* | Create and manage SQL server auditing setting |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/extendedAuditingSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/advancedThreatProtectionSettings/read | Retrieve a list of database Advanced Threat Protection settings configured for a given database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/advancedThreatProtectionSettings/write | Change the database Advanced Threat Protection settings for a given database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/advancedThreatProtectionSettings/read | Retrieve a list of database Advanced Threat Protection settings configured for a given database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/advancedThreatProtectionSettings/write | Change the database Advanced Threat Protection settings for a given database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/auditingSettings/* | Create and manage SQL server database auditing settings |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/auditRecords/read | Retrieve the database blob audit records |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/currentSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/dataMaskingPolicies/* | Create and manage SQL server database data masking policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/extendedAuditingSettings/read | Retrieve details of the extended blob auditing policy configured on a given database |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/read | Return the list of databases or gets the properties for the specified database. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/recommendedSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/schemas/read | Get a database schema. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/schemas/tables/columns/read | Get a database column. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/schemas/tables/columns/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/schemas/tables/read | Get a database table. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/securityAlertPolicies/* | Create and manage SQL server database security alert policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/securityMetrics/* | Create and manage SQL server database security metrics |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/transparentDataEncryption/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/sqlvulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessmentScans/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessmentSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/devOpsAuditingSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/firewallRules/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/read | Return the list of servers or gets the properties for the specified server. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/securityAlertPolicies/* | Create and manage SQL server security alert policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/sqlvulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/vulnerabilityAssessments/* |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/azureADOnlyAuthentications/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/read | Return the list of managed instances or gets the properties for the specified managed instance. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/azureADOnlyAuthentications/* |  |
> | [Microsoft.Security](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftsecurity)/sqlVulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/administrators/read | Gets a list of managed instance administrators. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/administrators/read | Gets a specific Azure Active Directory administrator object |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/ledgerDigestUploads/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/ledgerDigestUploadsAzureAsyncOperation/read | Gets in-progress operations of ledger digest upload settings |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/ledgerDigestUploadsOperationResults/read | Gets in-progress operations of ledger digest upload settings |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/externalPolicyBasedAuthorizations/* |  |
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
  "description": "Lets you manage the security-related policies of SQL servers and databases, but not access to them.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/056cd41c-7e88-42e1-933e-88ba6a50c9c3",
  "name": "056cd41c-7e88-42e1-933e-88ba6a50c9c3",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Network/virtualNetworks/subnets/joinViaServiceEndpoint/action",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Sql/locations/administratorAzureAsyncOperation/read",
        "Microsoft.Sql/managedInstances/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/managedInstances/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/managedInstances/databases/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/managedInstances/databases/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/managedInstances/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/managedInstances/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/managedInstances/databases/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/managedInstances/databases/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/managedInstances/databases/currentSensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/recommendedSensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/schemas/tables/columns/sensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/securityAlertPolicies/*",
        "Microsoft.Sql/managedInstances/databases/sensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/vulnerabilityAssessments/*",
        "Microsoft.Sql/servers/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/servers/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/managedInstances/securityAlertPolicies/*",
        "Microsoft.Sql/managedInstances/databases/transparentDataEncryption/*",
        "Microsoft.Sql/managedInstances/vulnerabilityAssessments/*",
        "Microsoft.Sql/managedInstances/serverConfigurationOptions/read",
        "Microsoft.Sql/managedInstances/serverConfigurationOptions/write",
        "Microsoft.Sql/locations/serverConfigurationOptionAzureAsyncOperation/read",
        "Microsoft.Sql/servers/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/servers/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/servers/auditingSettings/*",
        "Microsoft.Sql/servers/extendedAuditingSettings/*",
        "Microsoft.Sql/servers/databases/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/servers/databases/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/servers/databases/advancedThreatProtectionSettings/read",
        "Microsoft.Sql/servers/databases/advancedThreatProtectionSettings/write",
        "Microsoft.Sql/servers/databases/auditingSettings/*",
        "Microsoft.Sql/servers/databases/auditRecords/read",
        "Microsoft.Sql/servers/databases/currentSensitivityLabels/*",
        "Microsoft.Sql/servers/databases/dataMaskingPolicies/*",
        "Microsoft.Sql/servers/databases/extendedAuditingSettings/read",
        "Microsoft.Sql/servers/databases/read",
        "Microsoft.Sql/servers/databases/recommendedSensitivityLabels/*",
        "Microsoft.Sql/servers/databases/schemas/read",
        "Microsoft.Sql/servers/databases/schemas/tables/columns/read",
        "Microsoft.Sql/servers/databases/schemas/tables/columns/sensitivityLabels/*",
        "Microsoft.Sql/servers/databases/schemas/tables/read",
        "Microsoft.Sql/servers/databases/securityAlertPolicies/*",
        "Microsoft.Sql/servers/databases/securityMetrics/*",
        "Microsoft.Sql/servers/databases/sensitivityLabels/*",
        "Microsoft.Sql/servers/databases/transparentDataEncryption/*",
        "Microsoft.Sql/servers/databases/sqlvulnerabilityAssessments/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessments/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessmentScans/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessmentSettings/*",
        "Microsoft.Sql/servers/devOpsAuditingSettings/*",
        "Microsoft.Sql/servers/firewallRules/*",
        "Microsoft.Sql/servers/read",
        "Microsoft.Sql/servers/securityAlertPolicies/*",
        "Microsoft.Sql/servers/sqlvulnerabilityAssessments/*",
        "Microsoft.Sql/servers/vulnerabilityAssessments/*",
        "Microsoft.Support/*",
        "Microsoft.Sql/servers/azureADOnlyAuthentications/*",
        "Microsoft.Sql/managedInstances/read",
        "Microsoft.Sql/managedInstances/azureADOnlyAuthentications/*",
        "Microsoft.Security/sqlVulnerabilityAssessments/*",
        "Microsoft.Sql/managedInstances/administrators/read",
        "Microsoft.Sql/servers/administrators/read",
        "Microsoft.Sql/servers/databases/ledgerDigestUploads/*",
        "Microsoft.Sql/locations/ledgerDigestUploadsAzureAsyncOperation/read",
        "Microsoft.Sql/locations/ledgerDigestUploadsOperationResults/read",
        "Microsoft.Sql/servers/externalPolicyBasedAuthorizations/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "SQL Security Manager",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## SQL Server Contributor

Lets you manage SQL servers and databases, including server administrator credentials and certain server security and network settings. Although it grants no SQL data-plane permissions directly, control of administrator credentials can enable data-plane access. It excludes the security-related policies listed in NotActions.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-configure)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/locations/*/read |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/* | Create and manage SQL servers |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/metricDefinitions/read | Read metric definitions |
> | **NotActions** |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/currentSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/recommendedSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/schemas/tables/columns/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/securityAlertPolicies/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/databases/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/securityAlertPolicies/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/managedInstances/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/auditingSettings/* | Edit SQL server auditing settings |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/auditingSettings/* | Edit SQL server database auditing settings |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/auditRecords/read | Retrieve the database blob audit records |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/currentSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/dataMaskingPolicies/* | Edit SQL server database data masking policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/extendedAuditingSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/recommendedSensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/schemas/tables/columns/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/securityAlertPolicies/* | Edit SQL server database security alert policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/securityMetrics/* | Edit SQL server database security metrics |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/sensitivityLabels/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessmentScans/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/databases/vulnerabilityAssessmentSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/devOpsAuditingSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/extendedAuditingSettings/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/securityAlertPolicies/* | Edit SQL server security alert policies |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/vulnerabilityAssessments/* |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/azureADOnlyAuthentications/delete | Deletes a specific server Azure Active Directory only authentication object |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/azureADOnlyAuthentications/write | Adds or updates a specific server Azure Active Directory only authentication object |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/externalPolicyBasedAuthorizations/delete | Deletes a specific server external policy based authorization property |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql)/servers/externalPolicyBasedAuthorizations/write | Adds or updates a specific server external policy based authorization property |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Lets you manage SQL servers and databases, but not access to them, and not their security -related policies.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/6d8ee4ec-f05a-4a1d-8b00-a9b17e38b437",
  "name": "6d8ee4ec-f05a-4a1d-8b00-a9b17e38b437",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Sql/locations/*/read",
        "Microsoft.Sql/servers/*",
        "Microsoft.Support/*",
        "Microsoft.Insights/metrics/read",
        "Microsoft.Insights/metricDefinitions/read"
      ],
      "notActions": [
        "Microsoft.Sql/managedInstances/databases/currentSensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/recommendedSensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/schemas/tables/columns/sensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/securityAlertPolicies/*",
        "Microsoft.Sql/managedInstances/databases/sensitivityLabels/*",
        "Microsoft.Sql/managedInstances/databases/vulnerabilityAssessments/*",
        "Microsoft.Sql/managedInstances/securityAlertPolicies/*",
        "Microsoft.Sql/managedInstances/vulnerabilityAssessments/*",
        "Microsoft.Sql/servers/auditingSettings/*",
        "Microsoft.Sql/servers/databases/auditingSettings/*",
        "Microsoft.Sql/servers/databases/auditRecords/read",
        "Microsoft.Sql/servers/databases/currentSensitivityLabels/*",
        "Microsoft.Sql/servers/databases/dataMaskingPolicies/*",
        "Microsoft.Sql/servers/databases/extendedAuditingSettings/*",
        "Microsoft.Sql/servers/databases/recommendedSensitivityLabels/*",
        "Microsoft.Sql/servers/databases/schemas/tables/columns/sensitivityLabels/*",
        "Microsoft.Sql/servers/databases/securityAlertPolicies/*",
        "Microsoft.Sql/servers/databases/securityMetrics/*",
        "Microsoft.Sql/servers/databases/sensitivityLabels/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessments/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessmentScans/*",
        "Microsoft.Sql/servers/databases/vulnerabilityAssessmentSettings/*",
        "Microsoft.Sql/servers/devOpsAuditingSettings/*",
        "Microsoft.Sql/servers/extendedAuditingSettings/*",
        "Microsoft.Sql/servers/securityAlertPolicies/*",
        "Microsoft.Sql/servers/vulnerabilityAssessments/*",
        "Microsoft.Sql/servers/azureADOnlyAuthentications/delete",
        "Microsoft.Sql/servers/azureADOnlyAuthentications/write",
        "Microsoft.Sql/servers/externalPolicyBasedAuthorizations/delete",
        "Microsoft.Sql/servers/externalPolicyBasedAuthorizations/write"
      ],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "SQL Server Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
