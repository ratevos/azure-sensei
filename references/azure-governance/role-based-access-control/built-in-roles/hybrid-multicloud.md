# Azure built-in roles for Hybrid + multicloud - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/hybrid-multicloud  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the Hybrid + multicloud category (Azure Stack HCI).

## Arc Gateway Manager

Manage Arc Gateway Resources

[Learn more](https://learn.microsoft.com/en-us/azure/azure-arc/servers/arc-gateway)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/write | Writes an Azure Arc settings |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/read | Reads any Azure Arc settings |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/read | Reads any Azure Arc gateways |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/write | Writes an Azure Arc gateways |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/delete | Deletes an Azure Arc gateways |
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
  "description": "Manage Arc Gateway Resources",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/f6e92014-8af2-414d-9948-9b1abf559285",
  "name": "f6e92014-8af2-414d-9948-9b1abf559285",
  "permissions": [
    {
      "actions": [
        "Microsoft.HybridCompute/settings/write",
        "Microsoft.HybridCompute/settings/read",
        "Microsoft.HybridCompute/gateways/read",
        "Microsoft.HybridCompute/gateways/write",
        "Microsoft.HybridCompute/gateways/delete",
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
  "roleName": "Arc Gateway Manager",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Arc ScVmm Administrator role

Arc ScVmm VM Administrator has permissions to perform all ScVmm actions.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/built-in-roles)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.ScVmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/* |  |
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
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/Read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/UpgradeExtensions/action | Upgrades Extensions on Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/assessPatches/action | Assesses any Azure Arc machines to get missing software patches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/installPatches/action | Installs patches on any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/write | Installs or Updates an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/delete | Deletes an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/operations/read | Read all Operations for Azure Arc for Servers |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationresults/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationstatus/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/read | Reads any Azure Arc patchAssessmentResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/softwarePatches/read | Reads any Azure Arc patchAssessmentResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/read | Reads any Azure Arc patchInstallationResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/softwarePatches/read | Reads any Azure Arc patchInstallationResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/updateCenterOperationResults/read | Reads the status of an update center operation on machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/hybridIdentityMetadata/read | Read any Azure Arc machines's Hybrid Identity Metadata |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/read | Read all Azure Connected Machine Agent versions available |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/latest/read | Read the latest Azure Connected Machine Agent version |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/read | Reads any Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/write | Installs or Updates an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/delete | Deletes an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/read | Reads any Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/write | Installs or Updates an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/delete | Deletes an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/read | Reads any Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/write | Installs or Updates an Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/delete | Deletes an Azure Arc licenses |
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
  "description": "Arc ScVmm VM Administrator has permissions to perform all ScVmm actions.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/a92dfd61-77f9-4aec-a531-19858b406c87",
  "name": "a92dfd61-77f9-4aec-a531-19858b406c87",
  "permissions": [
    {
      "actions": [
        "Microsoft.ScVmm/*",
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
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/write",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operationstatuses/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "Microsoft.ExtendedLocation/customLocations/Read",
        "Microsoft.ExtendedLocation/customLocations/deploy/action",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/machines/UpgradeExtensions/action",
        "Microsoft.HybridCompute/machines/assessPatches/action",
        "Microsoft.HybridCompute/machines/installPatches/action",
        "Microsoft.HybridCompute/machines/extensions/read",
        "Microsoft.HybridCompute/machines/extensions/write",
        "Microsoft.HybridCompute/machines/extensions/delete",
        "Microsoft.HybridCompute/operations/read",
        "Microsoft.HybridCompute/locations/operationresults/read",
        "Microsoft.HybridCompute/locations/operationstatus/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/softwarePatches/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/softwarePatches/read",
        "Microsoft.HybridCompute/locations/updateCenterOperationResults/read",
        "Microsoft.HybridCompute/machines/hybridIdentityMetadata/read",
        "Microsoft.HybridCompute/osType/agentVersions/read",
        "Microsoft.HybridCompute/osType/agentVersions/latest/read",
        "Microsoft.HybridCompute/machines/runcommands/read",
        "Microsoft.HybridCompute/machines/runcommands/write",
        "Microsoft.HybridCompute/machines/runcommands/delete",
        "Microsoft.HybridCompute/machines/licenseProfiles/read",
        "Microsoft.HybridCompute/machines/licenseProfiles/write",
        "Microsoft.HybridCompute/machines/licenseProfiles/delete",
        "Microsoft.HybridCompute/licenses/read",
        "Microsoft.HybridCompute/licenses/write",
        "Microsoft.HybridCompute/licenses/delete"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Arc ScVmm Administrator role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Arc ScVmm Private Cloud User

Azure Arc ScVmm Private Cloud User has permissions to use the ScVmm resources to deploy VMs.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/built-in-roles)

> | Actions | Description |
> | --- | --- |
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
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/virtualnetworks/join/action | Join virtual network. |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/virtualnetworks/Read | Read virtualnetworks |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/virtualmachinetemplates/clone/action | Clones virtualmachinetemplates |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/virtualmachinetemplates/Read | Read virtualmachinetemplates |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/clouds/deploy/action | Deploy on resource pool. |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/clouds/Read | Read clouds |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/Read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/enabledresourcetypes/read | Gets EnabledResourceTypes for a Custom Location resource |
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
  "description": "Azure Arc ScVmm Private Cloud User has permissions to use the ScVmm resources to deploy VMs.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/c0781e91-8102-4553-8951-97c6d4243cda",
  "name": "c0781e91-8102-4553-8951-97c6d4243cda",
  "permissions": [
    {
      "actions": [
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
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/write",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operationstatuses/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "microsoft.scvmm/virtualnetworks/join/action",
        "microsoft.scvmm/virtualnetworks/Read",
        "microsoft.scvmm/virtualmachinetemplates/clone/action",
        "microsoft.scvmm/virtualmachinetemplates/Read",
        "microsoft.scvmm/clouds/deploy/action",
        "microsoft.scvmm/clouds/Read",
        "Microsoft.ExtendedLocation/customLocations/Read",
        "Microsoft.ExtendedLocation/customLocations/deploy/action",
        "Microsoft.ExtendedLocation/customLocations/enabledresourcetypes/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Arc ScVmm Private Cloud User",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Arc ScVmm Private Clouds Onboarding

Azure Arc ScVmm Private Clouds Onboarding role has permissions to provision all the required resources for onboard and deboard vmm server instances to Azure.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/built-in-roles)

> | Actions | Description |
> | --- | --- |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/vmmservers/Read | Read vmmservers |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/vmmservers/Write | Writes vmmservers |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/vmmservers/Delete | Deletes vmmservers |
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
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/Read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
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
  "description": "Azure Arc ScVmm Private Clouds Onboarding role has permissions to provision all the required resources for onboard and deboard vmm server instances to Azure.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/6aac74c4-6311-40d2-bbdd-7d01e7c6e3a9",
  "name": "6aac74c4-6311-40d2-bbdd-7d01e7c6e3a9",
  "permissions": [
    {
      "actions": [
        "microsoft.scvmm/vmmservers/Read",
        "microsoft.scvmm/vmmservers/Write",
        "microsoft.scvmm/vmmservers/Delete",
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
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/write",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operationstatuses/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "Microsoft.ExtendedLocation/customLocations/Read",
        "Microsoft.ExtendedLocation/customLocations/deploy/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Arc ScVmm Private Clouds Onboarding",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Arc ScVmm VM Contributor

Arc ScVmm VM Contributor has permissions to perform all VM actions.

[Learn more](https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/built-in-roles)

> | Actions | Description |
> | --- | --- |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/virtualmachines/* |  |
> | [microsoft.scvmm](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm)/virtualMachineInstances/* |  |
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
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/Read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/UpgradeExtensions/action | Upgrades Extensions on Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/assessPatches/action | Assesses any Azure Arc machines to get missing software patches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/installPatches/action | Installs patches on any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/write | Installs or Updates an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/delete | Deletes an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/operations/read | Read all Operations for Azure Arc for Servers |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationresults/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationstatus/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/read | Reads any Azure Arc patchAssessmentResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/softwarePatches/read | Reads any Azure Arc patchAssessmentResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/read | Reads any Azure Arc patchInstallationResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/softwarePatches/read | Reads any Azure Arc patchInstallationResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/updateCenterOperationResults/read | Reads the status of an update center operation on machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/hybridIdentityMetadata/read | Read any Azure Arc machines's Hybrid Identity Metadata |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/read | Read all Azure Connected Machine Agent versions available |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/latest/read | Read the latest Azure Connected Machine Agent version |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/read | Reads any Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/write | Installs or Updates an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/delete | Deletes an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/read | Reads any Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/write | Installs or Updates an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/delete | Deletes an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/read | Reads any Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/write | Installs or Updates an Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/delete | Deletes an Azure Arc licenses |
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
  "description": "Arc ScVmm VM Contributor has permissions to perform all VM actions.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/e582369a-e17b-42a5-b10c-874c387c530b",
  "name": "e582369a-e17b-42a5-b10c-874c387c530b",
  "permissions": [
    {
      "actions": [
        "microsoft.scvmm/virtualmachines/*",
        "microsoft.scvmm/virtualMachineInstances/*",
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
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/write",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operationstatuses/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "Microsoft.ExtendedLocation/customLocations/Read",
        "Microsoft.ExtendedLocation/customLocations/deploy/action",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/machines/UpgradeExtensions/action",
        "Microsoft.HybridCompute/machines/assessPatches/action",
        "Microsoft.HybridCompute/machines/installPatches/action",
        "Microsoft.HybridCompute/machines/extensions/read",
        "Microsoft.HybridCompute/machines/extensions/write",
        "Microsoft.HybridCompute/machines/extensions/delete",
        "Microsoft.HybridCompute/operations/read",
        "Microsoft.HybridCompute/locations/operationresults/read",
        "Microsoft.HybridCompute/locations/operationstatus/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/softwarePatches/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/softwarePatches/read",
        "Microsoft.HybridCompute/locations/updateCenterOperationResults/read",
        "Microsoft.HybridCompute/machines/hybridIdentityMetadata/read",
        "Microsoft.HybridCompute/osType/agentVersions/read",
        "Microsoft.HybridCompute/osType/agentVersions/latest/read",
        "Microsoft.HybridCompute/machines/runcommands/read",
        "Microsoft.HybridCompute/machines/runcommands/write",
        "Microsoft.HybridCompute/machines/runcommands/delete",
        "Microsoft.HybridCompute/machines/licenseProfiles/read",
        "Microsoft.HybridCompute/machines/licenseProfiles/write",
        "Microsoft.HybridCompute/machines/licenseProfiles/delete",
        "Microsoft.HybridCompute/licenses/read",
        "Microsoft.HybridCompute/licenses/write",
        "Microsoft.HybridCompute/licenses/delete"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Arc ScVmm VM Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Resource Bridge Deployment Role

Azure Resource Bridge Deployment Role is used only for Azure Stack HCI.

> [!IMPORTANT]
> This deployment role only applies to Azure Stack HCI. It does not apply to any other Arc Private Cloud and does not work for other private clouds.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleassignments/read | Get information about a role assignment. |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/Register/Action | Registers the subscription for the Azure Local resource provider and enables the creation of Azure Local resources. |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/register/action | Registers the subscription for Appliances resource provider and enables the creation of Appliance. |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/read | Gets an Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/write | Creates or Updates Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/delete | Deletes Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/locations/operationresults/read | Get result of Appliance operation |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/locations/operationsstatus/read | Get result of Appliance operation |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/listClusterUserCredential/action | Get an appliance cluster user credential |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/listKeys/action | Get an appliance cluster customer user keys |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/upgradeGraphs/read | Gets the upgrade graph of Appliance cluster |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/telemetryconfig/read | Get Appliances telemetry config utilized by Appliances CLI |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/operations/read | Gets list of Available Operations for Appliances |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/register/action | Registers the subscription for Custom Location resource provider and enables the creation of Custom Location. |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/write | Creates or Updates Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/delete | Deletes Custom Location resource |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/register/action | Register the subscription for Microsoft.HybridConnectivity |
> | [Microsoft.Kubernetes](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetes)/register/action | Registers Subscription with Microsoft.Kubernetes resource provider |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/register/action | Registers subscription to Microsoft.KubernetesConfiguration resource provider. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/write | Creates or updates extension resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/read | Gets extension instance resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/delete | Deletes extension instance resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/operations/read | Gets Async Operation status. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/namespaces/read | Get Namespace Resource |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/operations/read | Gets available operations of the Microsoft.KubernetesConfiguration resource provider. |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/guestConfigurationAssignments/read | Get guest configuration assignment. |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/register/action | Register the subscription for Microsoft.HybridContainerService |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/kubernetesVersions/read | Lists the supported kubernetes versions from the underlying custom location |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/kubernetesVersions/write | Puts the kubernetes version resource type |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/skus/read | Lists the supported VM SKUs from the underlying custom location |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/skus/write | Puts the VM SKUs resource type |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Write | Creates/Updates storage containers resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Read | Gets/Lists storage containers resource |
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
  "description": "Azure Resource Bridge Deployment Role",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/7b1f81f9-4196-4058-8aae-762e593270df",
  "name": "7b1f81f9-4196-4058-8aae-762e593270df",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/roleassignments/read",
        "Microsoft.AzureStackHCI/Register/Action",
        "Microsoft.ResourceConnector/register/action",
        "Microsoft.ResourceConnector/appliances/read",
        "Microsoft.ResourceConnector/appliances/write",
        "Microsoft.ResourceConnector/appliances/delete",
        "Microsoft.ResourceConnector/locations/operationresults/read",
        "Microsoft.ResourceConnector/locations/operationsstatus/read",
        "Microsoft.ResourceConnector/appliances/listClusterUserCredential/action",
        "Microsoft.ResourceConnector/appliances/listKeys/action",
        "Microsoft.ResourceConnector/appliances/upgradeGraphs/read",
        "Microsoft.ResourceConnector/telemetryconfig/read",
        "Microsoft.ResourceConnector/operations/read",
        "Microsoft.ExtendedLocation/register/action",
        "Microsoft.ExtendedLocation/customLocations/deploy/action",
        "Microsoft.ExtendedLocation/customLocations/read",
        "Microsoft.ExtendedLocation/customLocations/write",
        "Microsoft.ExtendedLocation/customLocations/delete",
        "Microsoft.HybridConnectivity/register/action",
        "Microsoft.Kubernetes/register/action",
        "Microsoft.KubernetesConfiguration/register/action",
        "Microsoft.KubernetesConfiguration/extensions/write",
        "Microsoft.KubernetesConfiguration/extensions/read",
        "Microsoft.KubernetesConfiguration/extensions/delete",
        "Microsoft.KubernetesConfiguration/extensions/operations/read",
        "Microsoft.KubernetesConfiguration/namespaces/read",
        "Microsoft.KubernetesConfiguration/operations/read",
        "Microsoft.GuestConfiguration/guestConfigurationAssignments/read",
        "Microsoft.HybridContainerService/register/action",
        "Microsoft.HybridContainerService/kubernetesVersions/read",
        "Microsoft.HybridContainerService/kubernetesVersions/write",
        "Microsoft.HybridContainerService/skus/read",
        "Microsoft.HybridContainerService/skus/write",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.AzureStackHCI/StorageContainers/Write",
        "Microsoft.AzureStackHCI/StorageContainers/Read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Resource Bridge Deployment Role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Stack HCI Administrator

Grants full access to the cluster and its resources, including the ability to register Azure Local and assign others as Azure Stack HCI VM Contributor and/or Azure Stack HCI VM Reader

[Learn more](https://learn.microsoft.com/en-us/azure-stack/hci/manage/assign-vm-rbac-roles)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/register/action | Registers the subscription for the Azure Local resource provider and enables the creation of Azure Local resources. |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/Unregister/Action | Unregisters the subscription for the Azure Local resource provider. |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/clusters/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/Read | Gets/Lists a network security group resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/SecurityRules/Read | Gets/Lists security rule resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/Write | Creates/Updates a network security group resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/SecurityRules/Write | Creates/Updates security rule resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/Delete | Deletes a network security group resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/SecurityRules/Delete | Deletes a security rule resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/join/action | Joins network security group resource |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/register/action | Registers the subscription for the Microsoft.HybridCompute Resource Provider |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/register/action | Registers the subscription for the Microsoft.GuestConfiguration resource provider. |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/guestConfigurationAssignments/read | Get guest configuration assignment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/write | Creates or updates a resource group. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/delete | Deletes a resource group and all its resources. |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity)/register/action | Register the subscription for Microsoft.HybridConnectivity |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/write | Create a role assignment at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleAssignments/delete | Delete a role assignment at the specified scope. |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/* | Create and manage a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement)/managementGroups/read | List management groups for the authenticated user. |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport)/* | Create and update a support ticket |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/EdgeMachines/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/DevicePools/* |  |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Write | Create or update a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Delete | Delete a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Activated/Action | Classic metric alert activated |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Resolved/Action | Classic metric alert resolved |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Throttled/Action | Classic metric alert rule throttled |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Incidents/Read | Read a classic metric alert incident |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/UpgradeExtensions/action | Upgrades Extensions on Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/assessPatches/action | Assesses any Azure Arc machines to get missing software patches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/installPatches/action | Installs patches on any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/write | Installs or Updates an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/delete | Deletes an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/operations/read | Read all Operations for Azure Arc for Servers |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationresults/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationstatus/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/read | Reads any Azure Arc patchAssessmentResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/softwarePatches/read | Reads any Azure Arc patchAssessmentResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/read | Reads any Azure Arc patchInstallationResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/softwarePatches/read | Reads any Azure Arc patchInstallationResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/updateCenterOperationResults/read | Reads the status of an update center operation on machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/hybridIdentityMetadata/read | Read any Azure Arc machines's Hybrid Identity Metadata |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/read | Read all Azure Connected Machine Agent versions available |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/latest/read | Read the latest Azure Connected Machine Agent version |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/read | Reads any Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/write | Installs or Updates an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/delete | Deletes an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/read | Reads any Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/write | Installs or Updates an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/delete | Deletes an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/read | Reads any Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/write | Installs or Updates an Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/delete | Deletes an Azure Arc licenses |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/register/action | Registers the subscription for Appliances resource provider and enables the creation of Appliance. |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/read | Gets an Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/write | Creates or Updates Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/delete | Deletes Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/locations/operationresults/read | Get result of Appliance operation |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/locations/operationsstatus/read | Get result of Appliance operation |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/listClusterUserCredential/action | Get an appliance cluster user credential |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/listKeys/action | Get an appliance cluster customer user keys |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/operations/read | Gets list of Available Operations for Appliances |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/register/action | Registers the subscription for Custom Location resource provider and enables the creation of Custom Location. |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/write | Creates or Updates Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/delete | Deletes Custom Location resource |
> | [Microsoft.EdgeMarketplace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace)/offers/read | List Offer resources by parent |
> | [Microsoft.EdgeMarketplace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace)/publishers/read | List Publisher resources by parent |
> | [Microsoft.Kubernetes](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetes)/register/action | Registers Subscription with Microsoft.Kubernetes resource provider |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/register/action | Registers subscription to Microsoft.KubernetesConfiguration resource provider. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/write | Creates or updates extension resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/read | Gets extension instance resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/delete | Deletes extension instance resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/operations/read | Gets Async Operation status. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/namespaces/read | Get Namespace Resource |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/operations/read | Gets available operations of the Microsoft.KubernetesConfiguration resource provider. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Write | Creates/Updates storage containers resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Read | Gets/Lists storage containers resource |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/register/action | Register the subscription for Microsoft.HybridContainerService |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/write | Writes an Azure Arc settings |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/settings/read | Reads any Azure Arc settings |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/read | Reads any Azure Arc gateways |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/write | Writes an Azure Arc gateways |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/gateways/delete | Deletes an Azure Arc gateways |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |
> | **Condition** |  |
> | ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{f5819b54-e033-4d82-ac66-4fec3cbf3f4c, cd570a14-e51a-42ad-bac8-bafd67325302, b64e21ea-ac4e-4cdf-9dc9-5b892992bee7, 4b3fe76c-f777-4d24-a2d7-b027b0f7b273, 874d1c73-6003-4e60-a13a-cb31ea190a85,865ae368-6a45-4bd1-8fbf-0d5151f56fc1,7b1f81f9-4196-4058-8aae-762e593270df,4633458b-17de-408a-b874-0445c86b69e6,c99c945f-8bd1-4fb1-a903-01460aae6068, b86a8fe4-44ce-4948-aee5-eccb2c155cd7, a4417e6f-fecd-4de8-b567-7b0420556985})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{f5819b54-e033-4d82-ac66-4fec3cbf3f4c, cd570a14-e51a-42ad-bac8-bafd67325302, b64e21ea-ac4e-4cdf-9dc9-5b892992bee7, 4b3fe76c-f777-4d24-a2d7-b027b0f7b273, 874d1c73-6003-4e60-a13a-cb31ea190a85,865ae368-6a45-4bd1-8fbf-0d5151f56fc1,7b1f81f9-4196-4058-8aae-762e593270df,4633458b-17de-408a-b874-0445c86b69e6,c99c945f-8bd1-4fb1-a903-01460aae6068, b86a8fe4-44ce-4948-aee5-eccb2c155cd7, a4417e6f-fecd-4de8-b567-7b0420556985})) | Add or remove role assignments for the following roles:<br/>Azure Connected Machine Resource Manager<br/>Azure Connected Machine Resource Administrator<br/>Azure Connected Machine Onboarding<br/>Azure Stack HCI Connected InfraVMs<br/>Azure Stack HCI VM Reader<br/>Azure Stack HCI VM Contributor<br/>Azure Stack HCI Device Management Role<br/>Azure Resource Bridge Deployment Role<br/>Key Vault Secrets User<br/>Key Vault Secrets Officer<br/>Key Vault Certificates Officer |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "Grants full access to the cluster and its resources, including the ability to register Azure Stack HCI and assign others as Azure Arc HCI VM Contributor and/or Azure Arc HCI VM Reader",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/bda0d508-adf1-4af0-9c28-88919fc3ae06",
  "name": "bda0d508-adf1-4af0-9c28-88919fc3ae06",
  "permissions": [
    {
      "actions": [
        "Microsoft.AzureStackHCI/register/action",
        "Microsoft.AzureStackHCI/Unregister/Action",
        "Microsoft.AzureStackHCI/clusters/*",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/Read",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/SecurityRules/Read",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/Write",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/SecurityRules/Write",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/Delete",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/SecurityRules/Delete",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/join/action",
        "Microsoft.HybridCompute/register/action",
        "Microsoft.GuestConfiguration/register/action",
        "Microsoft.GuestConfiguration/guestConfigurationAssignments/read",
        "Microsoft.Resources/subscriptions/resourceGroups/write",
        "Microsoft.Resources/subscriptions/resourceGroups/delete",
        "Microsoft.HybridConnectivity/register/action",
        "Microsoft.Authorization/roleAssignments/write",
        "Microsoft.Authorization/roleAssignments/delete",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Management/managementGroups/read",
        "Microsoft.Support/*",
        "Microsoft.AzureStackHCI/*",
        "Microsoft.AzureStackHCI/EdgeMachines/*",
        "Microsoft.AzureStackHCI/DevicePools/*",
        "Microsoft.Insights/AlertRules/Write",
        "Microsoft.Insights/AlertRules/Delete",
        "Microsoft.Insights/AlertRules/Read",
        "Microsoft.Insights/AlertRules/Activated/Action",
        "Microsoft.Insights/AlertRules/Resolved/Action",
        "Microsoft.Insights/AlertRules/Throttled/Action",
        "Microsoft.Insights/AlertRules/Incidents/Read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/write",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operationstatuses/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/machines/UpgradeExtensions/action",
        "Microsoft.HybridCompute/machines/assessPatches/action",
        "Microsoft.HybridCompute/machines/installPatches/action",
        "Microsoft.HybridCompute/machines/extensions/read",
        "Microsoft.HybridCompute/machines/extensions/write",
        "Microsoft.HybridCompute/machines/extensions/delete",
        "Microsoft.HybridCompute/operations/read",
        "Microsoft.HybridCompute/locations/operationresults/read",
        "Microsoft.HybridCompute/locations/operationstatus/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/softwarePatches/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/softwarePatches/read",
        "Microsoft.HybridCompute/locations/updateCenterOperationResults/read",
        "Microsoft.HybridCompute/machines/hybridIdentityMetadata/read",
        "Microsoft.HybridCompute/osType/agentVersions/read",
        "Microsoft.HybridCompute/osType/agentVersions/latest/read",
        "Microsoft.HybridCompute/machines/runcommands/read",
        "Microsoft.HybridCompute/machines/runcommands/write",
        "Microsoft.HybridCompute/machines/runcommands/delete",
        "Microsoft.HybridCompute/machines/licenseProfiles/read",
        "Microsoft.HybridCompute/machines/licenseProfiles/write",
        "Microsoft.HybridCompute/machines/licenseProfiles/delete",
        "Microsoft.HybridCompute/licenses/read",
        "Microsoft.HybridCompute/licenses/write",
        "Microsoft.HybridCompute/licenses/delete",
        "Microsoft.ResourceConnector/register/action",
        "Microsoft.ResourceConnector/appliances/read",
        "Microsoft.ResourceConnector/appliances/write",
        "Microsoft.ResourceConnector/appliances/delete",
        "Microsoft.ResourceConnector/locations/operationresults/read",
        "Microsoft.ResourceConnector/locations/operationsstatus/read",
        "Microsoft.ResourceConnector/appliances/listClusterUserCredential/action",
        "Microsoft.ResourceConnector/appliances/listKeys/action",
        "Microsoft.ResourceConnector/operations/read",
        "Microsoft.ExtendedLocation/register/action",
        "Microsoft.ExtendedLocation/customLocations/read",
        "Microsoft.ExtendedLocation/customLocations/deploy/action",
        "Microsoft.ExtendedLocation/customLocations/write",
        "Microsoft.ExtendedLocation/customLocations/delete",
        "Microsoft.EdgeMarketplace/offers/read",
        "Microsoft.EdgeMarketplace/publishers/read",
        "Microsoft.Kubernetes/register/action",
        "Microsoft.KubernetesConfiguration/register/action",
        "Microsoft.KubernetesConfiguration/extensions/write",
        "Microsoft.KubernetesConfiguration/extensions/read",
        "Microsoft.KubernetesConfiguration/extensions/delete",
        "Microsoft.KubernetesConfiguration/extensions/operations/read",
        "Microsoft.KubernetesConfiguration/namespaces/read",
        "Microsoft.KubernetesConfiguration/operations/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.AzureStackHCI/StorageContainers/Write",
        "Microsoft.AzureStackHCI/StorageContainers/Read",
        "Microsoft.HybridContainerService/register/action",
        "Microsoft.HybridCompute/settings/write",
        "Microsoft.HybridCompute/settings/read",
        "Microsoft.HybridCompute/gateways/read",
        "Microsoft.HybridCompute/gateways/write",
        "Microsoft.HybridCompute/gateways/delete"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": [],
      "conditionVersion": "2.0",
      "condition": "((!(ActionMatches{'Microsoft.Authorization/roleAssignments/write'})) OR (@Request[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{f5819b54-e033-4d82-ac66-4fec3cbf3f4c, cd570a14-e51a-42ad-bac8-bafd67325302, b64e21ea-ac4e-4cdf-9dc9-5b892992bee7, 4b3fe76c-f777-4d24-a2d7-b027b0f7b273, 874d1c73-6003-4e60-a13a-cb31ea190a85,865ae368-6a45-4bd1-8fbf-0d5151f56fc1,7b1f81f9-4196-4058-8aae-762e593270df,4633458b-17de-408a-b874-0445c86b69e6,c99c945f-8bd1-4fb1-a903-01460aae6068, b86a8fe4-44ce-4948-aee5-eccb2c155cd7, a4417e6f-fecd-4de8-b567-7b0420556985})) AND ((!(ActionMatches{'Microsoft.Authorization/roleAssignments/delete'})) OR (@Resource[Microsoft.Authorization/roleAssignments:RoleDefinitionId] ForAnyOfAnyValues:GuidEquals{f5819b54-e033-4d82-ac66-4fec3cbf3f4c, cd570a14-e51a-42ad-bac8-bafd67325302, b64e21ea-ac4e-4cdf-9dc9-5b892992bee7, 4b3fe76c-f777-4d24-a2d7-b027b0f7b273, 874d1c73-6003-4e60-a13a-cb31ea190a85,865ae368-6a45-4bd1-8fbf-0d5151f56fc1,7b1f81f9-4196-4058-8aae-762e593270df,4633458b-17de-408a-b874-0445c86b69e6,c99c945f-8bd1-4fb1-a903-01460aae6068, b86a8fe4-44ce-4948-aee5-eccb2c155cd7, a4417e6f-fecd-4de8-b567-7b0420556985}))"
    }
  ],
  "roleName": "Azure Stack HCI Administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Stack HCI Connected InfraVMs

Role of Arc Integration for Azure Stack HCI Infrastructure Virtual Machines.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/*/read |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/write | Installs or Updates an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/delete | Deletes an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/UpgradeExtensions/action | Upgrades Extensions on Azure Arc machines |
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
  "description": "Role of Arc Integration for Azure Stack HCI Infrastructure Virtual Machines.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/c99c945f-8bd1-4fb1-a903-01460aae6068",
  "name": "c99c945f-8bd1-4fb1-a903-01460aae6068",
  "permissions": [
    {
      "actions": [
        "Microsoft.HybridCompute/*/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/machines/extensions/read",
        "Microsoft.HybridCompute/machines/extensions/write",
        "Microsoft.HybridCompute/machines/extensions/delete",
        "Microsoft.HybridCompute/machines/UpgradeExtensions/action"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Stack HCI Connected InfraVMs",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Stack HCI Device Management Role

Microsoft.AzureStackHCI Device Management Role

[Learn more](https://learn.microsoft.com/en-us/azure-stack/hci/deploy/deployment-azure-resource-manager-template)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/Clusters/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/EdgeDevices/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/DevicePools/*/read |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/EdgeMachines/*/read |  |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/register/action | Register the subscription for Microsoft.HybridContainerService |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/kubernetesVersions/read | Lists the supported kubernetes versions from the underlying custom location |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/kubernetesVersions/write | Puts the kubernetes version resource type |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/skus/read | Lists the supported VM SKUs from the underlying custom location |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice)/skus/write | Puts the VM SKUs resource type |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/roleassignments/read | Get information about a role assignment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Write | Creates/Updates storage containers resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Read | Gets/Lists storage containers resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/LogicalNetworks/Read | Gets/Lists logical networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/LogicalNetworks/Write | Creates/Updates logical networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/Register/Action | Registers the subscription for the Azure Local resource provider and enables the creation of Azure Local resources. |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration)/guestConfigurationAssignments/read | Get guest configuration assignment. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/write | Creates or updates extension resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/read | Gets extension instance resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/delete | Deletes extension instance resource. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/operations/read | Gets Async Operation status. |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/namespaces/read | Get Namespace Resource |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/operations/read | Gets available operations of the Microsoft.KubernetesConfiguration resource provider. |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/read | Gets an Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/write | Creates or Updates Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/delete | Deletes Appliance resource |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/locations/operationresults/read | Get result of Appliance operation |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/locations/operationsstatus/read | Get result of Appliance operation |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/listClusterUserCredential/action | Get an appliance cluster user credential |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/listKeys/action | Get an appliance cluster customer user keys |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/appliances/upgradeGraphs/read | Gets the upgrade graph of Appliance cluster |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/telemetryconfig/read | Get Appliances telemetry config utilized by Appliances CLI |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector)/operations/read | Gets list of Available Operations for Appliances |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/write | Creates or Updates Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/delete | Deletes Custom Location resource |
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
  "description": "Microsoft.AzureStackHCI Device Management Role",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/865ae368-6a45-4bd1-8fbf-0d5151f56fc1",
  "name": "865ae368-6a45-4bd1-8fbf-0d5151f56fc1",
  "permissions": [
    {
      "actions": [
        "Microsoft.AzureStackHCI/Clusters/*",
        "Microsoft.AzureStackHCI/EdgeDevices/*",
        "Microsoft.AzureStackHCI/DevicePools/*/read",
        "Microsoft.AzureStackHCI/EdgeMachines/*/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.HybridContainerService/register/action",
        "Microsoft.HybridContainerService/kubernetesVersions/read",
        "Microsoft.HybridContainerService/kubernetesVersions/write",
        "Microsoft.HybridContainerService/skus/read",
        "Microsoft.HybridContainerService/skus/write",
        "Microsoft.Authorization/roleassignments/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.AzureStackHCI/StorageContainers/Write",
        "Microsoft.AzureStackHCI/StorageContainers/Read",
        "Microsoft.AzureStackHCI/LogicalNetworks/Read",
        "Microsoft.AzureStackHCI/LogicalNetworks/Write",
        "Microsoft.AzureStackHCI/Register/Action",
        "Microsoft.GuestConfiguration/guestConfigurationAssignments/read",
        "Microsoft.KubernetesConfiguration/extensions/write",
        "Microsoft.KubernetesConfiguration/extensions/read",
        "Microsoft.KubernetesConfiguration/extensions/delete",
        "Microsoft.KubernetesConfiguration/extensions/operations/read",
        "Microsoft.KubernetesConfiguration/namespaces/read",
        "Microsoft.KubernetesConfiguration/operations/read",
        "Microsoft.ResourceConnector/appliances/read",
        "Microsoft.ResourceConnector/appliances/write",
        "Microsoft.ResourceConnector/appliances/delete",
        "Microsoft.ResourceConnector/locations/operationresults/read",
        "Microsoft.ResourceConnector/locations/operationsstatus/read",
        "Microsoft.ResourceConnector/appliances/listClusterUserCredential/action",
        "Microsoft.ResourceConnector/appliances/listKeys/action",
        "Microsoft.ResourceConnector/appliances/upgradeGraphs/read",
        "Microsoft.ResourceConnector/telemetryconfig/read",
        "Microsoft.ResourceConnector/operations/read",
        "Microsoft.ExtendedLocation/customLocations/deploy/action",
        "Microsoft.ExtendedLocation/customLocations/read",
        "Microsoft.ExtendedLocation/customLocations/write",
        "Microsoft.ExtendedLocation/customLocations/delete"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Stack HCI Device Management Role",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Stack HCI VM Contributor

Grants permissions to perform all VM actions

[Learn more](https://learn.microsoft.com/en-us/azure-stack/hci/manage/assign-vm-rbac-roles)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualMachines/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/virtualMachineInstances/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkInterfaces/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualHardDisks/* |  |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualNetworks/Read | Gets/Lists virtual networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualNetworks/join/action | Joins virtual networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/LogicalNetworks/Read | Gets/Lists logical networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/LogicalNetworks/join/action | Joins logical networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/GalleryImages/Read | Gets/Lists gallery images resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/GalleryImages/deploy/action | Deploys gallery images resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Read | Gets/Lists storage containers resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/deploy/action | Deploys storage containers resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/MarketplaceGalleryImages/Read | Gets/Lists market place gallery images resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/MarketPlaceGalleryImages/deploy/action | Deploys market place gallery images resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/Clusters/Read | Gets clusters |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/Clusters/ArcSettings/Read | Gets Arc resource of Azure Local cluster |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/Read | Gets/Lists a network security group resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/SecurityRules/Read | Gets/Lists security rule resource |
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
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/write | Creates or updates an deployment. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/write | Writes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/delete | Deletes an Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/UpgradeExtensions/action | Upgrades Extensions on Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/assessPatches/action | Assesses any Azure Arc machines to get missing software patches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/installPatches/action | Installs patches on any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/write | Installs or Updates an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/delete | Deletes an Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/operations/read | Read all Operations for Azure Arc for Servers |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationresults/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/operationstatus/read | Reads the status of an operation on Microsoft.HybridCompute Resource Provider |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/read | Reads any Azure Arc patchAssessmentResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/softwarePatches/read | Reads any Azure Arc patchAssessmentResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/read | Reads any Azure Arc patchInstallationResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/softwarePatches/read | Reads any Azure Arc patchInstallationResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/locations/updateCenterOperationResults/read | Reads the status of an update center operation on machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/hybridIdentityMetadata/read | Read any Azure Arc machines's Hybrid Identity Metadata |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/read | Read all Azure Connected Machine Agent versions available |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/osType/agentVersions/latest/read | Read the latest Azure Connected Machine Agent version |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/read | Reads any Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/write | Installs or Updates an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/runcommands/delete | Deletes an Azure Arc runcommands |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/read | Reads any Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/write | Installs or Updates an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/delete | Deletes an Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/read | Reads any Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/write | Installs or Updates an Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/delete | Deletes an Azure Arc licenses |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/Read | Gets an Custom Location resource |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation)/customLocations/deploy/action | Deploy permissions to a Custom Location resource |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration)/extensions/read | Gets extension instance resource. |
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
  "description": "Grants permissions to perform all VM actions",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/874d1c73-6003-4e60-a13a-cb31ea190a85",
  "name": "874d1c73-6003-4e60-a13a-cb31ea190a85",
  "permissions": [
    {
      "actions": [
        "Microsoft.AzureStackHCI/VirtualMachines/*",
        "Microsoft.AzureStackHCI/virtualMachineInstances/*",
        "Microsoft.AzureStackHCI/NetworkInterfaces/*",
        "Microsoft.AzureStackHCI/VirtualHardDisks/*",
        "Microsoft.AzureStackHCI/VirtualNetworks/Read",
        "Microsoft.AzureStackHCI/VirtualNetworks/join/action",
        "Microsoft.AzureStackHCI/LogicalNetworks/Read",
        "Microsoft.AzureStackHCI/LogicalNetworks/join/action",
        "Microsoft.AzureStackHCI/GalleryImages/Read",
        "Microsoft.AzureStackHCI/GalleryImages/deploy/action",
        "Microsoft.AzureStackHCI/StorageContainers/Read",
        "Microsoft.AzureStackHCI/StorageContainers/deploy/action",
        "Microsoft.AzureStackHCI/MarketplaceGalleryImages/Read",
        "Microsoft.AzureStackHCI/MarketPlaceGalleryImages/deploy/action",
        "Microsoft.AzureStackHCI/Clusters/Read",
        "Microsoft.AzureStackHCI/Clusters/ArcSettings/Read",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/Read",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/SecurityRules/Read",
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
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/write",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operationstatuses/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/machines/write",
        "Microsoft.HybridCompute/machines/delete",
        "Microsoft.HybridCompute/machines/UpgradeExtensions/action",
        "Microsoft.HybridCompute/machines/assessPatches/action",
        "Microsoft.HybridCompute/machines/installPatches/action",
        "Microsoft.HybridCompute/machines/extensions/read",
        "Microsoft.HybridCompute/machines/extensions/write",
        "Microsoft.HybridCompute/machines/extensions/delete",
        "Microsoft.HybridCompute/operations/read",
        "Microsoft.HybridCompute/locations/operationresults/read",
        "Microsoft.HybridCompute/locations/operationstatus/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/softwarePatches/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/softwarePatches/read",
        "Microsoft.HybridCompute/locations/updateCenterOperationResults/read",
        "Microsoft.HybridCompute/machines/hybridIdentityMetadata/read",
        "Microsoft.HybridCompute/osType/agentVersions/read",
        "Microsoft.HybridCompute/osType/agentVersions/latest/read",
        "Microsoft.HybridCompute/machines/runcommands/read",
        "Microsoft.HybridCompute/machines/runcommands/write",
        "Microsoft.HybridCompute/machines/runcommands/delete",
        "Microsoft.HybridCompute/machines/licenseProfiles/read",
        "Microsoft.HybridCompute/machines/licenseProfiles/write",
        "Microsoft.HybridCompute/machines/licenseProfiles/delete",
        "Microsoft.HybridCompute/licenses/read",
        "Microsoft.HybridCompute/licenses/write",
        "Microsoft.HybridCompute/licenses/delete",
        "Microsoft.ExtendedLocation/customLocations/Read",
        "Microsoft.ExtendedLocation/customLocations/deploy/action",
        "Microsoft.KubernetesConfiguration/extensions/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Stack HCI VM Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Stack HCI VM Reader

Grants permissions to view VMs

[Learn more](https://learn.microsoft.com/en-us/azure-stack/hci/manage/assign-vm-rbac-roles)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualMachines/Read | Gets/Lists virtual machine resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/virtualMachineInstances/Read | Gets/Lists virtual machine instance resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualMachines/Extensions/Read | Gets/Lists virtual machine extensions resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualNetworks/Read | Gets/Lists virtual networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/LogicalNetworks/Read | Gets/Lists logical networks resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkInterfaces/Read | Gets/Lists network interfaces resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/VirtualHardDisks/Read | Gets/Lists virtual hard disk resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/StorageContainers/Read | Gets/Lists storage containers resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/GalleryImages/Read | Gets/Lists gallery images resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/MarketplaceGalleryImages/Read | Gets/Lists market place gallery images resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/Read | Gets/Lists a network security group resource |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci)/NetworkSecurityGroups/SecurityRules/Read | Gets/Lists security rule resource |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/licenses/read | Reads any Azure Arc licenses |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/extensions/read | Reads any Azure Arc extensions |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/licenseProfiles/read | Reads any Azure Arc licenseProfiles |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/read | Reads any Azure Arc patchAssessmentResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchAssessmentResults/softwarePatches/read | Reads any Azure Arc patchAssessmentResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/read | Reads any Azure Arc patchInstallationResults |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/patchInstallationResults/softwarePatches/read | Reads any Azure Arc patchInstallationResults/softwarePatches |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/read | Read any Azure Arc machines |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/privateLinkScopes/networkSecurityPerimeterConfigurations/read | Reads any Azure Arc networkSecurityPerimeterConfigurations |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/privateLinkScopes/privateEndpointConnections/read | Read any Azure Arc privateEndpointConnections |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/privateLinkScopes/read | Read any Azure Arc privateLinkScopes |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Write | Create or update a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Delete | Delete a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Activated/Action | Classic metric alert activated |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Resolved/Action | Classic metric alert resolved |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Throttled/Action | Classic metric alert rule throttled |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Incidents/Read | Read a classic metric alert incident |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/exportTemplate/action | Export template for a deployment |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourcegroups/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth)/availabilityStatuses/read | Gets the availability statuses for all resources in the specified scope |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/read | Gets the list of subscriptions. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/operationresults/read | Get the subscription operation results. |
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
  "description": "Grants permissions to view VMs",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/4b3fe76c-f777-4d24-a2d7-b027b0f7b273",
  "name": "4b3fe76c-f777-4d24-a2d7-b027b0f7b273",
  "permissions": [
    {
      "actions": [
        "Microsoft.AzureStackHCI/VirtualMachines/Read",
        "Microsoft.AzureStackHCI/virtualMachineInstances/Read",
        "Microsoft.AzureStackHCI/VirtualMachines/Extensions/Read",
        "Microsoft.AzureStackHCI/VirtualNetworks/Read",
        "Microsoft.AzureStackHCI/LogicalNetworks/Read",
        "Microsoft.AzureStackHCI/NetworkInterfaces/Read",
        "Microsoft.AzureStackHCI/VirtualHardDisks/Read",
        "Microsoft.AzureStackHCI/StorageContainers/Read",
        "Microsoft.AzureStackHCI/GalleryImages/Read",
        "Microsoft.AzureStackHCI/MarketplaceGalleryImages/Read",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/Read",
        "Microsoft.AzureStackHCI/NetworkSecurityGroups/SecurityRules/Read",
        "Microsoft.HybridCompute/licenses/read",
        "Microsoft.HybridCompute/machines/extensions/read",
        "Microsoft.HybridCompute/machines/licenseProfiles/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/read",
        "Microsoft.HybridCompute/machines/patchAssessmentResults/softwarePatches/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/read",
        "Microsoft.HybridCompute/machines/patchInstallationResults/softwarePatches/read",
        "Microsoft.HybridCompute/machines/read",
        "Microsoft.HybridCompute/privateLinkScopes/networkSecurityPerimeterConfigurations/read",
        "Microsoft.HybridCompute/privateLinkScopes/privateEndpointConnections/read",
        "Microsoft.HybridCompute/privateLinkScopes/read",
        "Microsoft.Insights/AlertRules/Write",
        "Microsoft.Insights/AlertRules/Delete",
        "Microsoft.Insights/AlertRules/Read",
        "Microsoft.Insights/AlertRules/Activated/Action",
        "Microsoft.Insights/AlertRules/Resolved/Action",
        "Microsoft.Insights/AlertRules/Throttled/Action",
        "Microsoft.Insights/AlertRules/Incidents/Read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Resources/deployments/exportTemplate/action",
        "Microsoft.Resources/deployments/operations/read",
        "Microsoft.Resources/deployments/operationstatuses/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
        "Microsoft.Resources/subscriptions/resourcegroups/deployments/operationstatuses/read",
        "Microsoft.ResourceHealth/availabilityStatuses/read",
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/subscriptions/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/subscriptions/operationresults/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Stack HCI VM Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Azure Stack Registration Owner

Lets you manage Azure Stack registrations.

> | Actions | Description |
> | --- | --- |
> | [Microsoft.AzureStack](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestack)/edgeSubscriptions/read |  |
> | [Microsoft.AzureStack](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestack)/registrations/products/*/action |  |
> | [Microsoft.AzureStack](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestack)/registrations/products/read | Gets the properties of an Azure Stack Marketplace product |
> | [Microsoft.AzureStack](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestack)/registrations/read | Gets the properties of an Azure Stack registration |
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
  "description": "Lets you manage Azure Stack registrations.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/6f12a6df-dd06-4f3e-bcb1-ce8be600526a",
  "name": "6f12a6df-dd06-4f3e-bcb1-ce8be600526a",
  "permissions": [
    {
      "actions": [
        "Microsoft.AzureStack/edgeSubscriptions/read",
        "Microsoft.AzureStack/registrations/products/*/action",
        "Microsoft.AzureStack/registrations/products/read",
        "Microsoft.AzureStack/registrations/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Azure Stack Registration Owner",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Hybrid Server Resource Administrator

Can read, write, delete, and re-onboard Hybrid servers to the Hybrid Resource Provider.

[Learn more](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/hybrid/arc-enabled-servers/eslz-identity-and-access-management)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/machines/* |  |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute)/*/read |  |
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
  "description": "Can read, write, delete, and re-onboard Hybrid servers to the Hybrid Resource Provider.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/48b40c6e-82e0-4eb3-90d5-19e40f49b624",
  "name": "48b40c6e-82e0-4eb3-90d5-19e40f49b624",
  "permissions": [
    {
      "actions": [
        "Microsoft.HybridCompute/machines/*",
        "Microsoft.HybridCompute/*/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Hybrid Server Resource Administrator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
