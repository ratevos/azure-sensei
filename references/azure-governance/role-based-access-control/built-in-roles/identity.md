# Azure built-in roles for Identity - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/identity  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the Identity category.

## Domain Services Contributor

Can manage Azure AD Domain Services and related network configurations

[Learn more](https://learn.microsoft.com/en-us/entra/identity/domain-services/tutorial-create-instance)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
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
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Write | Create or update a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Delete | Delete a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Activated/Action | Classic metric alert activated |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Resolved/Action | Classic metric alert resolved |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Throttled/Action | Classic metric alert rule throttled |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Incidents/Read | Read a classic metric alert incident |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Logs/Read | Reading data from all your logs |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Metrics/Read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/DiagnosticSettings/* | Creates, updates, or reads the diagnostic setting for Analysis Server |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/DiagnosticSettingsCategories/Read | Read diagnostic settings categories |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad)/register/action | Register Domain Service |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad)/unregister/action | Unregister Domain Service |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad)/domainServices/* |  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/register/action | Registers the subscription |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/unregister/action | Unregisters the subscription |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/write | Creates a virtual network or updates an existing virtual network |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/delete | Deletes a virtual network |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/peer/action | Peers a virtual network with another virtual network |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/write | Creates a virtual network subnet or updates an existing virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/delete | Deletes a virtual network subnet |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/join/action | Joins a virtual network. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/virtualNetworkPeerings/read | Gets a virtual network peering definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/virtualNetworkPeerings/write | Creates a virtual network peering or updates an existing virtual network peering |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/virtualNetworkPeerings/delete | Deletes a virtual network peering |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/providers/Microsoft.Insights/diagnosticSettings/read | Get the diagnostic settings of Virtual Network |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read | Gets available metrics for the PingMesh |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/azureFirewalls/read | Get Azure Firewall |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/ddosProtectionPlans/read | Gets a DDoS Protection Plan |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/ddosProtectionPlans/join/action | Joins a DDoS Protection Plan. Not alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/read | Gets a load balancer definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/delete | Deletes a load balancer |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/*/read |  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/backendAddressPools/join/action | Joins a load balancer backend address pool. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/inboundNatRules/join/action | Joins a load balancer inbound nat rule. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/natGateways/join/action | Joins a NAT Gateway |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/read | Gets a network interface definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/write | Creates a network interface or updates an existing network interface.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/delete | Deletes a network interface |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/join/action | Joins a Virtual Machine to a network interface. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/defaultSecurityRules/read | Gets a default security rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/read | Gets a network security group definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/write | Creates a network security group or updates an existing network security group |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/delete | Deletes a network security group |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/join/action | Joins a network security group. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/securityRules/read | Gets a security rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/securityRules/write | Creates a security rule or updates an existing security rule |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/securityRules/delete | Deletes a security rule |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/read | Gets a route table definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/write | Creates a route table or Updates an existing route table |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/delete | Deletes a route table definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/join/action | Joins a route table. Not Alertable. |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/routes/read | Gets a route definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/routes/write | Creates a route or Updates an existing route |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/routes/delete | Deletes a route definition |
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
  "description": "Can manage Azure AD Domain Services and related network configurations",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/eeaeda52-9324-47f6-8069-5d5bade478b2",
  "name": "eeaeda52-9324-47f6-8069-5d5bade478b2",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Resources/deployments/write",
        "Microsoft.Resources/deployments/delete",
        "Microsoft.Resources/deployments/cancel/action",
        "Microsoft.Resources/deployments/validate/action",
        "Microsoft.Resources/deployments/whatIf/action",
        "Microsoft.Resources/deployments/exportTemplate/action",
        "Microsoft.Resources/deployments/operations/read",
        "Microsoft.Resources/deployments/operationstatuses/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Insights/AlertRules/Write",
        "Microsoft.Insights/AlertRules/Delete",
        "Microsoft.Insights/AlertRules/Read",
        "Microsoft.Insights/AlertRules/Activated/Action",
        "Microsoft.Insights/AlertRules/Resolved/Action",
        "Microsoft.Insights/AlertRules/Throttled/Action",
        "Microsoft.Insights/AlertRules/Incidents/Read",
        "Microsoft.Insights/Logs/Read",
        "Microsoft.Insights/Metrics/Read",
        "Microsoft.Insights/DiagnosticSettings/*",
        "Microsoft.Insights/DiagnosticSettingsCategories/Read",
        "Microsoft.AAD/register/action",
        "Microsoft.AAD/unregister/action",
        "Microsoft.AAD/domainServices/*",
        "Microsoft.Network/register/action",
        "Microsoft.Network/unregister/action",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/write",
        "Microsoft.Network/virtualNetworks/delete",
        "Microsoft.Network/virtualNetworks/peer/action",
        "Microsoft.Network/virtualNetworks/join/action",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/virtualNetworks/subnets/write",
        "Microsoft.Network/virtualNetworks/subnets/delete",
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read",
        "Microsoft.Network/virtualNetworks/virtualNetworkPeerings/write",
        "Microsoft.Network/virtualNetworks/virtualNetworkPeerings/delete",
        "Microsoft.Network/virtualNetworks/providers/Microsoft.Insights/diagnosticSettings/read",
        "Microsoft.Network/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/azureFirewalls/read",
        "Microsoft.Network/ddosProtectionPlans/read",
        "Microsoft.Network/ddosProtectionPlans/join/action",
        "Microsoft.Network/loadBalancers/read",
        "Microsoft.Network/loadBalancers/delete",
        "Microsoft.Network/loadBalancers/*/read",
        "Microsoft.Network/loadBalancers/backendAddressPools/join/action",
        "Microsoft.Network/loadBalancers/inboundNatRules/join/action",
        "Microsoft.Network/natGateways/join/action",
        "Microsoft.Network/networkInterfaces/read",
        "Microsoft.Network/networkInterfaces/write",
        "Microsoft.Network/networkInterfaces/delete",
        "Microsoft.Network/networkInterfaces/join/action",
        "Microsoft.Network/networkSecurityGroups/defaultSecurityRules/read",
        "Microsoft.Network/networkSecurityGroups/read",
        "Microsoft.Network/networkSecurityGroups/write",
        "Microsoft.Network/networkSecurityGroups/delete",
        "Microsoft.Network/networkSecurityGroups/join/action",
        "Microsoft.Network/networkSecurityGroups/securityRules/read",
        "Microsoft.Network/networkSecurityGroups/securityRules/write",
        "Microsoft.Network/networkSecurityGroups/securityRules/delete",
        "Microsoft.Network/routeTables/read",
        "Microsoft.Network/routeTables/write",
        "Microsoft.Network/routeTables/delete",
        "Microsoft.Network/routeTables/join/action",
        "Microsoft.Network/routeTables/routes/read",
        "Microsoft.Network/routeTables/routes/write",
        "Microsoft.Network/routeTables/routes/delete"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Domain Services Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Domain Services Reader

Can view Azure AD Domain Services and related network configurations

> | Actions | Description |
> | --- | --- |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/read | Gets or lists deployments. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operations/read | Gets or lists deployment operations. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/deployments/operationstatuses/read | Gets or lists deployment operation statuses. |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources)/subscriptions/resourceGroups/read | Gets or lists resource groups. |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Read | Read a classic metric alert |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/AlertRules/Incidents/Read | Read a classic metric alert incident |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Logs/Read | Reading data from all your logs |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/Metrics/read | Read metrics |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/DiagnosticSettings/read | Read a resource diagnostic setting |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/DiagnosticSettingsCategories/Read | Read diagnostic settings categories |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad)/domainServices/*/read |  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/read | Get the virtual network definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/subnets/read | Gets a virtual network subnet definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/virtualNetworkPeerings/read | Gets a virtual network peering definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/providers/Microsoft.Insights/diagnosticSettings/read | Get the diagnostic settings of Virtual Network |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read | Gets available metrics for the PingMesh |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/azureFirewalls/read | Get Azure Firewall |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/ddosProtectionPlans/read | Gets a DDoS Protection Plan |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/read | Gets a load balancer definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/loadBalancers/*/read |  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/natGateways/read | Gets a Nat Gateway Definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkInterfaces/read | Gets a network interface definition.  |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/defaultSecurityRules/read | Gets a default security rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/read | Gets a network security group definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/networkSecurityGroups/securityRules/read | Gets a security rule definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/read | Gets a route table definition |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork)/routeTables/routes/read | Gets a route definition |
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
  "description": "Can view Azure AD Domain Services and related network configurations",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/361898ef-9ed1-48c2-849c-a832951106bb",
  "name": "361898ef-9ed1-48c2-849c-a832951106bb",
  "permissions": [
    {
      "actions": [
        "Microsoft.Authorization/*/read",
        "Microsoft.Resources/deployments/read",
        "Microsoft.Resources/deployments/operations/read",
        "Microsoft.Resources/deployments/operationstatuses/read",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Insights/AlertRules/Read",
        "Microsoft.Insights/AlertRules/Incidents/Read",
        "Microsoft.Insights/Logs/Read",
        "Microsoft.Insights/Metrics/read",
        "Microsoft.Insights/DiagnosticSettings/read",
        "Microsoft.Insights/DiagnosticSettingsCategories/Read",
        "Microsoft.AAD/domainServices/*/read",
        "Microsoft.Network/virtualNetworks/read",
        "Microsoft.Network/virtualNetworks/subnets/read",
        "Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read",
        "Microsoft.Network/virtualNetworks/providers/Microsoft.Insights/diagnosticSettings/read",
        "Microsoft.Network/virtualNetworks/providers/Microsoft.Insights/metricDefinitions/read",
        "Microsoft.Network/azureFirewalls/read",
        "Microsoft.Network/ddosProtectionPlans/read",
        "Microsoft.Network/loadBalancers/read",
        "Microsoft.Network/loadBalancers/*/read",
        "Microsoft.Network/natGateways/read",
        "Microsoft.Network/networkInterfaces/read",
        "Microsoft.Network/networkSecurityGroups/defaultSecurityRules/read",
        "Microsoft.Network/networkSecurityGroups/read",
        "Microsoft.Network/networkSecurityGroups/securityRules/read",
        "Microsoft.Network/routeTables/read",
        "Microsoft.Network/routeTables/routes/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Domain Services Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Managed Identity Contributor

Create, Read, Update, and Delete User Assigned Identity

[Learn more](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/read | Gets an existing user assigned identity |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/write | Creates a new user assigned identity or updates the tags associated with an existing user assigned identity |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/delete | Deletes an existing user assigned identity |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/federatedIdentityCredentials/read | Get or list Federated Identity Credentials |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/federatedIdentityCredentials/write | Add or update a Federated Identity Credential |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/federatedIdentityCredentials/delete | Delete a Federated Identity Credential |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/revokeTokens/action | Revoked all the existing tokens on a user assigned identity |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
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
  "description": "Create, Read, Update, and Delete User Assigned Identity",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/e40ec5ca-96e0-45a2-b4ff-59039f2c2b59",
  "name": "e40ec5ca-96e0-45a2-b4ff-59039f2c2b59",
  "permissions": [
    {
      "actions": [
        "Microsoft.ManagedIdentity/userAssignedIdentities/read",
        "Microsoft.ManagedIdentity/userAssignedIdentities/write",
        "Microsoft.ManagedIdentity/userAssignedIdentities/delete",
        "Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/read",
        "Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/write",
        "Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/delete",
        "Microsoft.ManagedIdentity/userAssignedIdentities/revokeTokens/action",
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Managed Identity Contributor",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Managed Identity Operator

Read and Assign User Assigned Identity

[Learn more](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities)

> | Actions | Description |
> | --- | --- |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/*/read |  |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity)/userAssignedIdentities/*/assign/action |  |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization)/*/read | Read roles and role assignments |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights)/alertRules/* | Create and manage a classic metric alert |
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
  "description": "Read and Assign User Assigned Identity",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/f1a07417-d97a-45cb-824c-7a7467783830",
  "name": "f1a07417-d97a-45cb-824c-7a7467783830",
  "permissions": [
    {
      "actions": [
        "Microsoft.ManagedIdentity/userAssignedIdentities/*/read",
        "Microsoft.ManagedIdentity/userAssignedIdentities/*/assign/action",
        "Microsoft.Authorization/*/read",
        "Microsoft.Insights/alertRules/*",
        "Microsoft.Resources/subscriptions/resourceGroups/read",
        "Microsoft.Resources/deployments/*",
        "Microsoft.Support/*"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Managed Identity Operator",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
