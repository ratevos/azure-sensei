# Azure built-in roles for Migration - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/migration  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the Migration category.

## Azure Migrate Decide and Plan Expert

Grants restricted access on Azure Migrate project to only perform planning operations including appliance-based discovery, managing inventory, identifying server dependencies, creation of business case & assessment reports.

[Learn more](https://learn.microsoft.com/en-us/azure/migrate/prepare-azure-accounts)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/locations/read | Gets the list of locations supported. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/checkResourceName/action | Check the resource name for validity. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/write | Creates or updates a deployment script |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/read | Gets or lists deployment scripts |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/write | Creates or updates a resource link. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/write | Add locks at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/delete | Delete locks at the specified scope. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Migrate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftmigrate)/* |  |
> | Microsoft.ApplicationMigration/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/* |  |
> | Microsoft.MySQLDiscovery/* |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | Microsoft.DependencyMap/* |  |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/vaults/* |  |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/checkNameAvailability/read | Checks that a key vault name is valid and is not in use |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/register/action | Registers the subscription for the Microsoft.HybridCompute Resource Provider |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/write | Creates a virtual network subnet or updates an existing virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/join/action | Joins a network security group. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/read | Gets an private endpoint resource. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/write | Creates a new private endpoint, or updates an existing private endpoint. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/privateDnsZoneGroups/write | Puts a Private DNS Zone Group |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/write | Create or update a Private DNS zone within a resource group. Note that this command cannot be used to create or update virtual network links or record sets within the zone. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/virtualNetworkLinks/write | Create or update a Private DNS zone link to virtual network. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/join/action | Joins a Private DNS Zone |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/A/write | Create or update a record set of type 'A' within a Private DNS zone. The records specified will replace the current records in the record set. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/register/action | Registers the subscription |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/privateDnsZoneGroups/read | Gets a Private DNS Zone Group |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/*/read |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/*/write |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/listKeys/action | Returns the access keys for the specified storage account. |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/register/action | Registers the subscription for the Microsoft.GuestConfiguration resource provider. |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/register/action | Register the subscription for Microsoft.HybridConnectivity |
> | Microsoft.DataReplication/*/read |  |
> | Microsoft.DataReplication/register/action | Registers the subscription for the Microsoft.DataReplication resource provider |
> | Microsoft.DataReplication/replicationVaults/write | Updates any vault |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/* |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/register/action | Registers subscription for given Resource Provider |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/register/action | Registers a subscription |
> | Microsoft.AzureArcData/register/action | Register the subscription for Microsoft.AzureArcData |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/read | Gets or lists resource links. |
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
  "description": "Grants restricted access on Azure Migrate project to only perform planning operations including appliance-based discovery, managing inventory, identifying server dependencies, creation of business case & assessment reports.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/7859c0b0-0bb9-4994-bd12-cd529af7d646",
  "name": "7859c0b0-0bb9-4994-bd12-cd529af7d646",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/locations/read",
        "Microsoft.Resources/checkResourceName/action",
        "Microsoft.Resources/deploymentScripts/write",
        "Microsoft.Resources/deploymentScripts/read",
        "Microsoft.Resources/links/write",
        "Microsoft.Authorization/*/read",
        "Microsoft.Authorization/locks/write",
        "Microsoft.Authorization/locks/delete",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Migrate/*",
        "Microsoft.ApplicationMigration/*",
        "Microsoft.OffAzure/*",
        "Microsoft.MySQLDiscovery/*",
        "Microsoft.Support/*",
        "Microsoft.DependencyMap/*",
        "Microsoft.KeyVault/vaults/*",
        "Microsoft.KeyVault/checkNameAvailability/read",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/register/action",
        "Microsoft.Network/virtualNetworks/subnets/write",
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/networkSecurityGroups/join/action",
        "Microsoft.Network/virtualNetworks/join/action",
        "Microsoft.Network/privateEndpoints/read",
        "Microsoft.Network/privateEndpoints/write",
        "Microsoft.Network/privateEndpoints/privateDnsZoneGroups/write",
        "Microsoft.Network/privateDnsZones/write",
        "Microsoft.Network/privateDnsZones/virtualNetworkLinks/write",
        "Microsoft.Network/privateDnsZones/join/action",
        "Microsoft.Network/privateDnsZones/A/write",
        "Microsoft.Network/register/action",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/privateEndpoints/privateDnsZoneGroups/read",
        "Microsoft.Storage/storageAccounts/*/read",
        "Microsoft.Storage/storageAccounts/*/write",
        "Microsoft.Storage/storageAccounts/listKeys/action",
        "Microsoft.GuestConfiguration/register/action",
        "Microsoft.HybridConnectivity/register/action",
        "Microsoft.DataReplication/*/read",
        "Microsoft.DataReplication/register/action",
        "Microsoft.DataReplication/replicationVaults/write",
        "Microsoft.RecoveryServices/vaults/*",
        "Microsoft.RecoveryServices/register/action",
        "Microsoft.KeyVault/register/action",
        "Microsoft.AzureArcData/register/action",
        "Microsoft.Resources/links/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Migrate Decide and Plan Expert",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Migrate Execute Expert

Grants restricted access on an Azure Migrate project to only perform migration related operations, including replication, execution of test migrations, tracking and monitoring of migration progress, and initiation of agentless and agent-based migrations.

Includes an ABAC condition to constrain role assignments.

[Learn more](https://learn.microsoft.com/en-us/azure/migrate/prepare-azure-accounts)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/write | Creates or updates a resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/locations/read | Gets the list of locations supported. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/checkResourceName/action | Check the resource name for validity. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/write | Creates or updates a deployment script |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/read | Gets or lists deployment scripts |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/write | Creates or updates a resource link. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/write | Add locks at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/delete | Delete locks at the specified scope. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Migrate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftmigrate)/*/read |  |
> | Microsoft.ApplicationMigration/*/read |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/*/read |  |
> | Microsoft.MySQLDiscovery/*/read |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/read | Gets a network interface definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/write | Creates a network interface or updates an existing network interface.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/delete | Deletes a network interface |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/*/read |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/*/write |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/listKeys/action | Returns the access keys for the specified storage account. |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/register/action | Registers Subscription with Microsoft.Compute resource provider |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/read | Get the properties of an availability set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/vmSizes/read | List available sizes for creating or updating a virtual machine in the availability set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/diskEncryptionSets/read | Get the properties of a disk encryption set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/skus/read | Gets the list of Microsoft.Compute SKUs available for your Subscription |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/read | Get the properties of a Disk |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/write | Creates a new Disk or updates an existing one |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/delete | Deletes the Disk |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/read | Get the properties of a virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/write | Creates a new virtual machine or updates an existing virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/delete | Deletes the virtual machine |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/* |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/register/action | Registers subscription for given Resource Provider |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/operations/read | Operation returns the list of Operations for a Resource Provider |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/read | Gets or lists resource links. |
> | Microsoft.DependencyMap/*/read |  |
> | Microsoft.DependencyMap/maps/*/action |  |
> | **NotActions** |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/hypervSites/machines/inventoryinsights/pendingupdates/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/hypervSites/machines/inventoryinsights/vulnerabilities/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/serverSites/machines/inventoryinsights/pendingupdates/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/serverSites/machines/inventoryinsights/vulnerabilities/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/vmwareSites/machines/inventoryinsights/vulnerabilities/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/vmwareSites/machines/inventoryinsights/pendingupdates/* |  |
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
> | ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe})) | Add or remove role assignments for the following roles:<br/>Storage Account Contributor<br/>Storage Blob Data Contributor |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants restricted access on an Azure Migrate project to only perform migration related operations, including replication, execution of test migrations, tracking and monitoring of migration progress, and initiation of agentless and agent-based migrations.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/1cfa4eac-9a23-481c-a793-bfb6958e836b",
  "name": "1cfa4eac-9a23-481c-a793-bfb6958e836b",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/write",
        "Microsoft.Resources/subscriptions/locations/read",
        "Microsoft.Resources/checkResourceName/action",
        "Microsoft.Resources/deploymentScripts/write",
        "Microsoft.Resources/deploymentScripts/read",
        "Microsoft.Resources/links/write",
        "Microsoft.Authorization/*/read",
        "Microsoft.Authorization/locks/write",
        "Microsoft.Authorization/locks/delete",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Migrate/*/read",
        "Microsoft.ApplicationMigration/*/read",
        "Microsoft.OffAzure/*/read",
        "Microsoft.MySQLDiscovery/*/read",
        "Microsoft.Support/*",
        "Microsoft.Network/networkInterfaces/read",
        "Microsoft.Network/networkInterfaces/write",
        "Microsoft.Network/networkInterfaces/delete",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Storage/storageAccounts/*/read",
        "Microsoft.Storage/storageAccounts/*/write",
        "Microsoft.Storage/storageAccounts/listKeys/action",
        "Microsoft.Compute/register/action",
        "Microsoft.Compute/availabilitySets/read",
        "Microsoft.Compute/availabilitySets/vmSizes/read",
        "Microsoft.Compute/diskEncryptionSets/read",
        "Microsoft.Compute/skus/read",
        "Microsoft.Compute/disks/read",
        "Microsoft.Compute/disks/write",
        "Microsoft.Compute/disks/delete",
        "Microsoft.Compute/virtualMachines/read",
        "Microsoft.Compute/virtualMachines/write",
        "Microsoft.Compute/virtualMachines/delete",
        "Microsoft.RecoveryServices/vaults/*",
        "Microsoft.RecoveryServices/register/action",
        "Microsoft.RecoveryServices/operations/read",
        "Microsoft.Resources/links/read",
        "Microsoft.DependencyMap/*/read",
        "Microsoft.DependencyMap/maps/*/action"
      ],
      "notActions": [
        "Microsoft.OffAzure/hypervSites/machines/inventoryinsights/pendingupdates/*",
        "Microsoft.OffAzure/hypervSites/machines/inventoryinsights/vulnerabilities/*",
        "Microsoft.OffAzure/serverSites/machines/inventoryinsights/pendingupdates/*",
        "Microsoft.OffAzure/serverSites/machines/inventoryinsights/vulnerabilities/*",
        "Microsoft.OffAzure/vmwareSites/machines/inventoryinsights/vulnerabilities/*",
        "Microsoft.OffAzure/vmwareSites/machines/inventoryinsights/pendingupdates/*"
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
      "condition": "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe}))"
    }
  ],
  "roleName": "Azure Migrate Execute Expert",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Migrate Owner

Grants full access to create and manage Azure Migrate projects including appliance-based discovery, creation of business case & assessment report and execution of migrations; Also grants ability to assign Azure Migrate specific roles in Azure RBAC.

Includes an ABAC condition to constrain role assignments.

[Learn more](https://learn.microsoft.com/en-us/azure/migrate/prepare-azure-accounts)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/write | Creates or updates a resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/locations/read | Gets the list of locations supported. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/checkResourceName/action | Check the resource name for validity. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/write | Creates or updates a deployment script |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/read | Gets or lists deployment scripts |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/write | Creates or updates a resource link. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/write | Add locks at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/delete | Delete locks at the specified scope. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Migrate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftmigrate)/* |  |
> | Microsoft.ApplicationMigration/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/* |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | Microsoft.MySQLDiscovery/* |  |
> | Microsoft.DependencyMap/* |  |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/vaults/* |  |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/checkNameAvailability/read | Checks that a key vault name is valid and is not in use |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/register/action | Registers the subscription for the Microsoft.HybridCompute Resource Provider |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/read | Gets a network interface definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/write | Creates a network interface or updates an existing network interface.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/delete | Deletes a network interface |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/write | Creates a virtual network subnet or updates an existing virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/join/action | Joins a network security group. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/read | Gets an private endpoint resource. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/write | Creates a new private endpoint, or updates an existing private endpoint. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/privateDnsZoneGroups/write | Puts a Private DNS Zone Group |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/write | Create or update a Private DNS zone within a resource group. Note that this command cannot be used to create or update virtual network links or record sets within the zone. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/virtualNetworkLinks/write | Create or update a Private DNS zone link to virtual network. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/join/action | Joins a Private DNS Zone |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/A/write | Create or update a record set of type 'A' within a Private DNS zone. The records specified will replace the current records in the record set. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/register/action | Registers the subscription |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/privateDnsZoneGroups/read | Gets a Private DNS Zone Group |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/* | Create and manage storage accounts |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/register/action | Registers the subscription for the Microsoft.GuestConfiguration resource provider. |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/register/action | Registers Subscription with Microsoft.Compute resource provider |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/read | Get the properties of an availability set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/availabilitySets/vmSizes/read | List available sizes for creating or updating a virtual machine in the availability set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/diskEncryptionSets/read | Get the properties of a disk encryption set |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/skus/read | Gets the list of Microsoft.Compute SKUs available for your Subscription |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/read | Get the properties of a Disk |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/write | Creates a new Disk or updates an existing one |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/disks/delete | Deletes the Disk |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/read | Get the properties of a virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/write | Creates a new virtual machine or updates an existing virtual machine |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute)/virtualMachines/delete | Deletes the virtual machine |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/register/action | Register the subscription for Microsoft.HybridConnectivity |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/* |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/register/action | Registers subscription for given Resource Provider |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/operations/read | Operation returns the list of Operations for a Resource Provider |
> | Microsoft.DataReplication/*/read |  |
> | Microsoft.DataReplication/register/action | Registers the subscription for the Microsoft.DataReplication resource provider |
> | Microsoft.DataReplication/replicationVaults/write | Updates any vault |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/register/action | Registers a subscription |
> | Microsoft.AzureArcData/register/action | Register the subscription for Microsoft.AzureArcData |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/read | Gets or lists resource links. |
> | **NotActions** |  |
> | *none* |  |
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
> | ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836b, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836b, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63})) | Add or remove role assignments for the following roles:<br/>Azure Migrate Decide and Plan Expert<br/>Azure Migrate Execute Expert<br/>Storage Account Contributor<br/>Storage Blob Data Contributor<br/>Azure Migrate Service Reader |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants full access to create and manage Azure Migrate projects including appliance-based discovery, creation of business case & assessment report and execution of migrations; Also grants ability to assign Azure Migrate specific roles in Azure RBAC.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/fd8ea4d5-6509-4db0-bada-356ab233b4fa",
  "name": "fd8ea4d5-6509-4db0-bada-356ab233b4fa",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/write",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/locations/read",
        "Microsoft.Resources/checkResourceName/action",
        "Microsoft.Resources/deploymentScripts/write",
        "Microsoft.Resources/deploymentScripts/read",
        "Microsoft.Resources/links/write",
        "Microsoft.Authorization/*/read",
        "Microsoft.Authorization/locks/write",
        "Microsoft.Authorization/locks/delete",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Migrate/*",
        "Microsoft.ApplicationMigration/*",
        "Microsoft.OffAzure/*",
        "Microsoft.Support/*",
        "Microsoft.MySQLDiscovery/*",
        "Microsoft.DependencyMap/*",
        "Microsoft.KeyVault/vaults/*",
        "Microsoft.KeyVault/checkNameAvailability/read",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/register/action",
        "Microsoft.Network/networkInterfaces/read",
        "Microsoft.Network/networkInterfaces/write",
        "Microsoft.Network/networkInterfaces/delete",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/subnets/write",
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/networkSecurityGroups/join/action",
        "Microsoft.Network/virtualNetworks/join/action",
        "Microsoft.Network/privateEndpoints/read",
        "Microsoft.Network/privateEndpoints/write",
        "Microsoft.Network/privateEndpoints/privateDnsZoneGroups/write",
        "Microsoft.Network/privateDnsZones/write",
        "Microsoft.Network/privateDnsZones/virtualNetworkLinks/write",
        "Microsoft.Network/privateDnsZones/join/action",
        "Microsoft.Network/privateDnsZones/A/write",
        "Microsoft.Network/register/action",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/privateEndpoints/privateDnsZoneGroups/read",
        "Microsoft.Storage/storageAccounts/*",
        "Microsoft.GuestConfiguration/register/action",
        "Microsoft.Compute/register/action",
        "Microsoft.Compute/availabilitySets/read",
        "Microsoft.Compute/availabilitySets/vmSizes/read",
        "Microsoft.Compute/diskEncryptionSets/read",
        "Microsoft.Compute/skus/read",
        "Microsoft.Compute/disks/read",
        "Microsoft.Compute/disks/write",
        "Microsoft.Compute/disks/delete",
        "Microsoft.Compute/virtualMachines/read",
        "Microsoft.Compute/virtualMachines/write",
        "Microsoft.Compute/virtualMachines/delete",
        "Microsoft.HybridConnectivity/register/action",
        "Microsoft.RecoveryServices/vaults/*",
        "Microsoft.RecoveryServices/register/action",
        "Microsoft.RecoveryServices/operations/read",
        "Microsoft.DataReplication/*/read",
        "Microsoft.DataReplication/register/action",
        "Microsoft.DataReplication/replicationVaults/write",
        "Microsoft.KeyVault/register/action",
        "Microsoft.AzureArcData/register/action",
        "Microsoft.Resources/links/read"
      ],
      "notActions": [],
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
      "condition": "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836b, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836b, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63}))"
    }
  ],
  "roleName": "Azure Migrate Owner",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Migrate Service Reader

Grants required access to the system assigned managed identity of Azure Migrate project resource.

[Learn more](https://learn.microsoft.com/en-us/azure/migrate/prepare-azure-accounts)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | Microsoft.ApplicationMigration/*/read |  |
> | [Microsoft.Migrate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftmigrate)/*/read |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/*/read |  |
> | Microsoft.MySQLDiscovery/*/read |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectableItems/read | Read any Protectable Items |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/read | Read any Protected Items |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/replicationFabrics/replicationProtectionContainers/replicationMigrationItems/read | Read any Migration Items |
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
  "description": "Grants required access to the system assigned managed identity of Azure Migrate project resource.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/ba480ccd-6499-4709-b581-8f38bb215c63",
  "name": "ba480ccd-6499-4709-b581-8f38bb215c63",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Resources/deployments/*",
        "Microsoft.ApplicationMigration/*/read",
        "Microsoft.Migrate/*/read",
        "Microsoft.OffAzure/*/read",
        "Microsoft.MySQLDiscovery/*/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectableItems/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationProtectedItems/read",
        "Microsoft.RecoveryServices/vaults/replicationFabrics/replicationProtectionContainers/replicationMigrationItems/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Migrate Service Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Local Migrate Execute Expert

Grants restricted access on an Azure Local based Azure Migrate project to only perform migration related operations, including replication, execution of migrations, tracking and monitoring of migration progress, and initiation of agentless migrations.

Includes an ABAC condition to constrain role assignments.

[Learn more](https://learn.microsoft.com/en-us/azure/migrate/prepare-azure-accounts)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/write | Creates or updates a resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/locations/read | Gets the list of locations supported. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/checkResourceName/action | Check the resource name for validity. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/validate/action | Validates a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/write | Creates or updates a deployment script |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/read | Gets or lists deployment scripts |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/write | Creates or updates a resource link. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/write | Add locks at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/delete | Delete locks at the specified scope. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Migrate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftmigrate)/*/read |  |
> | Microsoft.ApplicationMigration/*/read |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/*/read |  |
> | Microsoft.MySQLDiscovery/*/read |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/*/read |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/*/write |  |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/listKeys/action | Returns the access keys for the specified storage account. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/read | Gets or lists resource links. |
> | Microsoft.DependencyMap/*/read |  |
> | Microsoft.DependencyMap/maps/*/action |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/*/Read |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/LogicalNetworks/join/action | Joins logical networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkInterfaces/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualHardDisks/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualMachines/Write | Creates/Updates virtual machine resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualMachineInstances/Write | Creates/Updates virtual machine instance resource |
> | Microsoft.DataReplication/*/read |  |
> | Microsoft.DataReplication/replicationVaults/protectedItems/* |  |
> | Microsoft.DataReplication/replicationVaults/replicationExtensions/* |  |
> | Microsoft.DataReplication/replicationVaults/replicationPolicies/* |  |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/read | Gets an Custom Location resource |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/read | Gets extension instance resource. |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/read | Gets an Appliance resource |
> | **NotActions** |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/hypervSites/machines/inventoryinsights/pendingupdates/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/hypervSites/machines/inventoryinsights/vulnerabilities/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/serverSites/machines/inventoryinsights/pendingupdates/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/serverSites/machines/inventoryinsights/vulnerabilities/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/vmwareSites/machines/inventoryinsights/vulnerabilities/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/vmwareSites/machines/inventoryinsights/pendingupdates/* |  |
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
> | ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe})) | Add or remove role assignments for the following roles:<br/>Storage Account Contributor<br/>Storage Blob Data Contributor |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants restricted access on an Azure Local based Azure Migrate project to only perform migration related operations, including replication, execution of migrations, tracking and monitoring of migration progress, and initiation of agentless migrations.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/1cfa4eac-9a23-481c-a793-bfb6958e836c",
  "name": "1cfa4eac-9a23-481c-a793-bfb6958e836c",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/write",
        "Microsoft.Resources/subscriptions/locations/read",
        "Microsoft.Resources/checkResourceName/action",
        "Microsoft.Resources/deployments/validate/action",
        "Microsoft.Resources/deploymentScripts/write",
        "Microsoft.Resources/deploymentScripts/read",
        "Microsoft.Resources/links/write",
        "Microsoft.Authorization/*/read",
        "Microsoft.Authorization/locks/write",
        "Microsoft.Authorization/locks/delete",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Migrate/*/read",
        "Microsoft.ApplicationMigration/*/read",
        "Microsoft.OffAzure/*/read",
        "Microsoft.MySQLDiscovery/*/read",
        "Microsoft.Support/*",
        "Microsoft.Storage/storageAccounts/*/read",
        "Microsoft.Storage/storageAccounts/*/write",
        "Microsoft.Storage/storageAccounts/listKeys/action",
        "Microsoft.Resources/links/read",
        "Microsoft.DependencyMap/*/read",
        "Microsoft.DependencyMap/maps/*/action",
        "Microsoft.AzureStackHCI/*/Read",
        "Microsoft.AzureStackHCI/LogicalNetworks/join/action",
        "Microsoft.AzureStackHCI/NetworkInterfaces/*",
        "Microsoft.AzureStackHCI/VirtualHardDisks/*",
        "Microsoft.AzureStackHCI/VirtualMachines/Write",
        "Microsoft.AzureStackHCI/VirtualMachineInstances/Write",
        "Microsoft.DataReplication/*/read",
        "Microsoft.DataReplication/replicationVaults/protectedItems/*",
        "Microsoft.DataReplication/replicationVaults/replicationExtensions/*",
        "Microsoft.DataReplication/replicationVaults/replicationPolicies/*",
        "Microsoft.ExtendedLocation/customLocations/read",
        "Microsoft.KubernetesConfiguration/extensions/read",
        "Microsoft.ResourceConnector/appliances/read"
      ],
      "notActions": [
        "Microsoft.OffAzure/hypervSites/machines/inventoryinsights/pendingupdates/*",
        "Microsoft.OffAzure/hypervSites/machines/inventoryinsights/vulnerabilities/*",
        "Microsoft.OffAzure/serverSites/machines/inventoryinsights/pendingupdates/*",
        "Microsoft.OffAzure/serverSites/machines/inventoryinsights/vulnerabilities/*",
        "Microsoft.OffAzure/vmwareSites/machines/inventoryinsights/vulnerabilities/*",
        "Microsoft.OffAzure/vmwareSites/machines/inventoryinsights/pendingupdates/*"
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
      "condition": "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe}))"
    }
  ],
  "roleName": "Azure Local Migrate Execute Expert",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Local Migrate Owner

Grants full access to create and manage Azure Local based Azure Migrate projects including appliance-based discovery and execution of migrations; Also grants ability to assign Azure Migrate Local specific roles in Azure RBAC

Includes an ABAC condition to constrain role assignments.

[Learn more](https://learn.microsoft.com/en-us/azure/migrate/prepare-azure-accounts)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/write | Creates or updates a resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/locations/read | Gets the list of locations supported. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/checkResourceName/action | Check the resource name for validity. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/validate/action | Validates a deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/write | Creates or updates a deployment script |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deploymentScripts/read | Gets or lists deployment scripts |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/write | Creates or updates a resource link. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/write | Add locks at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/locks/delete | Delete locks at the specified scope. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
> | [Microsoft.Migrate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftmigrate)/* |  |
> | Microsoft.ApplicationMigration/* |  |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure)/* |  |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | Microsoft.MySQLDiscovery/* |  |
> | Microsoft.DependencyMap/* |  |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/vaults/* |  |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/checkNameAvailability/read | Checks that a key vault name is valid and is not in use |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/register/action | Registers the subscription for the Microsoft.HybridCompute Resource Provider |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/write | Creates a virtual network subnet or updates an existing virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/read | Gets an private endpoint resource. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/write | Creates a new private endpoint, or updates an existing private endpoint. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/privateDnsZoneGroups/write | Puts a Private DNS Zone Group |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/write | Create or update a Private DNS zone within a resource group. Note that this command cannot be used to create or update virtual network links or record sets within the zone. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/virtualNetworkLinks/write | Create or update a Private DNS zone link to virtual network. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/join/action | Joins a Private DNS Zone |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateDnsZones/A/write | Create or update a record set of type 'A' within a Private DNS zone. The records specified will replace the current records in the record set. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/register/action | Registers the subscription |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/privateEndpoints/privateDnsZoneGroups/read | Gets a Private DNS Zone Group |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage)/storageAccounts/* | Create and manage storage accounts |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/register/action | Registers the subscription for the Microsoft.GuestConfiguration resource provider. |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/register/action | Register the subscription for Microsoft.HybridConnectivity |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/vaults/* |  |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/register/action | Registers subscription for given Resource Provider |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices)/operations/read | Operation returns the list of Operations for a Resource Provider |
> | Microsoft.DataReplication/*/read |  |
> | Microsoft.DataReplication/register/action | Registers the subscription for the Microsoft.DataReplication resource provider |
> | Microsoft.DataReplication/replicationFabrics/* |  |
> | Microsoft.DataReplication/replicationVaults/* |  |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault)/register/action | Registers a subscription |
> | Microsoft.AzureArcData/register/action | Register the subscription for Microsoft.AzureArcData |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/links/read | Gets or lists resource links. |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/*/Read |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/LogicalNetworks/join/action | Joins logical networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkInterfaces/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualHardDisks/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualMachines/Write | Creates/Updates virtual machine resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualMachineInstances/Write | Creates/Updates virtual machine instance resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/read | Gets an Custom Location resource |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/read | Gets extension instance resource. |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/read | Gets an Appliance resource |
> | **NotActions** |  |
> | *none* |  |
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
> | ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836c, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836c, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63})) | Add or remove role assignments for the following roles:<br/>Azure Migrate Decide and Plan Expert<br/>Azure Local Migrate Execute Expert<br/>Storage Account Contributor<br/>Storage Blob Data Contributor<br/>Azure Migrate Service Reader |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants full access to create and manage Azure Local based Azure Migrate projects including appliance-based discovery and execution of migrations; Also grants ability to assign Azure Migrate Local specific roles in Azure RBAC",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/fd8ea4d5-6509-4db0-bada-356ab233b4fb",
  "name": "fd8ea4d5-6509-4db0-bada-356ab233b4fb",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/write",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/locations/read",
        "Microsoft.Resources/checkResourceName/action",
        "Microsoft.Resources/deployments/validate/action",
        "Microsoft.Resources/deploymentScripts/write",
        "Microsoft.Resources/deploymentScripts/read",
        "Microsoft.Resources/links/write",
        "Microsoft.Authorization/*/read",
        "Microsoft.Authorization/locks/write",
        "Microsoft.Authorization/locks/delete",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Migrate/*",
        "Microsoft.ApplicationMigration/*",
        "Microsoft.OffAzure/*",
        "Microsoft.Support/*",
        "Microsoft.MySQLDiscovery/*",
        "Microsoft.DependencyMap/*",
        "Microsoft.KeyVault/vaults/*",
        "Microsoft.KeyVault/checkNameAvailability/read",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/register/action",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/subnets/write",
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/virtualNetworks/join/action",
        "Microsoft.Network/privateEndpoints/read",
        "Microsoft.Network/privateEndpoints/write",
        "Microsoft.Network/privateEndpoints/privateDnsZoneGroups/write",
        "Microsoft.Network/privateDnsZones/write",
        "Microsoft.Network/privateDnsZones/virtualNetworkLinks/write",
        "Microsoft.Network/privateDnsZones/join/action",
        "Microsoft.Network/privateDnsZones/A/write",
        "Microsoft.Network/register/action",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/privateEndpoints/privateDnsZoneGroups/read",
        "Microsoft.Storage/storageAccounts/*",
        "Microsoft.GuestConfiguration/register/action",
        "Microsoft.HybridConnectivity/register/action",
        "Microsoft.RecoveryServices/vaults/*",
        "Microsoft.RecoveryServices/register/action",
        "Microsoft.RecoveryServices/operations/read",
        "Microsoft.DataReplication/*/read",
        "Microsoft.DataReplication/register/action",
        "Microsoft.DataReplication/replicationFabrics/*",
        "Microsoft.DataReplication/replicationVaults/*",
        "Microsoft.KeyVault/register/action",
        "Microsoft.AzureArcData/register/action",
        "Microsoft.Resources/links/read",
        "Microsoft.AzureStackHCI/*/Read",
        "Microsoft.AzureStackHCI/LogicalNetworks/join/action",
        "Microsoft.AzureStackHCI/NetworkInterfaces/*",
        "Microsoft.AzureStackHCI/VirtualHardDisks/*",
        "Microsoft.AzureStackHCI/VirtualMachines/Write",
        "Microsoft.AzureStackHCI/VirtualMachineInstances/Write",
        "Microsoft.ExtendedLocation/customLocations/read",
        "Microsoft.KubernetesConfiguration/extensions/read",
        "Microsoft.ResourceConnector/appliances/read"
      ],
      "notActions": [],
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
      "condition": "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836c, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{7859c0b0-0bb9-4994-bd12-cd529af7d646, 1cfa4eac-9a23-481c-a793-bfb6958e836c, 17d1049b-9a84-46fb-8f53-869881c3d3ab, ba92f5b4-2d11-453d-a403-e96b0029c9fe, ba480ccd-6499-4709-b581-8f38bb215c63}))"
    }
  ],
  "roleName": "Azure Local Migrate Owner",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Migrate Arc Discovery Reader - Preview

Read metadata of Azure Arc enabled server resources and metadata, performance and migration suitability of Arc enabled SQL server resources. Users creating Azure Migrate project that uses Arc resource discovery require this role on Arc scope of the project. To enable periodic sync, Azure Migrate project managed identity must be assigned this role. This role is in preview and subject to change.

[Learn more](https://learn.microsoft.com/en-us/azure/migrate/concepts-arc-resource-discovery)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | Microsoft.AzureArcData/sqlServerInstances/read | Retrieves a SQL Server Instance resource |
> | Microsoft.AzureArcData/sqlServerInstances/databases/read | read databases |
> | Microsoft.AzureArcData/sqlServerInstances/availabilityGroups/read | read availabilityGroups |
> | Microsoft.AzureArcData/sqlServerInstances/getTelemetry/action | Retrieves SQL Server instance telemetry |
> | Microsoft.AzureArcData/sqlServerInstances/availabilityGroups/getDetailView/action | Retrieves detailed properties of the Availability Group. |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
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
  "description": "Read metadata of Azure Arc enabled server resources and metadata, performance and migration suitability of Arc enabled SQL server resources. Users creating Azure Migrate project that uses Arc resource discovery require this role on Arc scope of the project. To enable periodic sync, Azure Migrate project managed identity must be assigned this role. This role is in preview and subject to change.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/5d5dddae-e124-4753-972d-aae60b37deb4",
  "name": "5d5dddae-e124-4753-972d-aae60b37deb4",
  "permissions": [
    {
      "actions": [
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.AzureArcData/sqlServerInstances/read",
        "Microsoft.AzureArcData/sqlServerInstances/databases/read",
        "Microsoft.AzureArcData/sqlServerInstances/availabilityGroups/read",
        "Microsoft.AzureArcData/sqlServerInstances/getTelemetry/action",
        "Microsoft.AzureArcData/sqlServerInstances/availabilityGroups/getDetailView/action",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/extensions/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Migrate Arc Discovery Reader - Preview",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
