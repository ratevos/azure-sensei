# Assign Azure Role-based access control (RBAC) Roles - Entitlement management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-azure-role-assignments  
> Microsoft doc last updated: 04/07/2026


Entitlement Management supports access lifecycle for various resource types such as Applications, SharePoint sites, Groups, Teams, and [Microsoft Entra Roles](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-roles). To manage access to Azure resources, You can assign access to Azure RBAC roles directly to Access packages and Catalogs.

By assigning Azure RBAC roles to employees, and guests, using Entitlement Management, you can look at an identity's entitlements to quickly determine which Azure roles are assigned to that identity. Following the security principle of [least privilege access](https://learn.microsoft.com/en-us/entra/identity-platform/secure-least-privileged-access), you're able to assign both **Active** and **Eligible** role types allowing privilege to be activated just in time when access to Azure resources are needed.

By assigning Azure resources, administrators can:
- Choose the target scope that aligns with the catalog resource options (Management Group, Subscription, or Resource Group).
- Select eligible or active role type that a user receives when assigned to the access package.
- Select the appropriate Azure RBAC role (supports custom Azure roles and built-in roles). End users who request and are approved, or are assigned, to the access package receive the Azure role assignment automatically.

## Supported Scenarios

| Catalog scope where the resource is added | Access Package scope allowed | What end users can receive |
|-------------------------------------------|------------------------------|----------------------------| 
| Management Group | Management Group | Eligible or active Azure roles assigned at the Management Group scope |
| Subscription | Subscription | Eligible or active Azure roles assigned at the Subscription scope |
| Subscription | Resource Group (tied to the subscription) | Eligible or active Azure roles assigned at the Resource Group scope |

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

### Azure RBAC requirements for catalog onboarding

To onboard an Azure Subscription or Management Group into an Entitlement Management catalog, the administrator performing this action must have Azure RBAC permissions that allow role assignment management at that scope.

Specifically, Entitlement Management performs an Azure RBAC check for:

- `Microsoft.Authorization/roleassignments/read`
- `Microsoft.Authorization/roleassignments/write`
- `Microsoft.Authorization/roleassignments/delete`

at the selected Management Group or Subscription. This check ensures that the administrator has sufficient permissions for Entitlement Management to later assign Azure RBAC roles at that scope on behalf of approved access package assignments.

If any of these checks fail, onboarding of the Azure resource into the catalog fails.

### Azure RBAC requirements for adding a role to an access package

After a Subscription or Management Group has been onboarded into a catalog, an Access Package administrator can add Azure RBAC roles at:

- Management Group
- Subscription
- Resource Group (within an onboarded Subscription)

When adding an Azure RBAC role to an access package, Entitlement Management dynamically enumerates available role definitions at the selected assignment scope. As a result, the administrator configuring the access package must have:

- `Microsoft.Authorization/roleDefinitions/read`

at the specific scope selected for role assignment (Management Group, Subscription, or Resource Group) to query role visibility.

## Add an Azure RBAC role to a Catalog

To assign an Azure RBAC role to a catalog within entitlement management, you'd do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator) or [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) with Catalog Owner permissions.

1. Browse to **ID Governance** > **Catalogs**.

1. On the Catalogs page, open the catalog you want to add the Azure resource role to and select **Add Resources**.

1. On the add resources page, select **Azure Resources**.
    
1. On the **Select Azure Resources** pane, select either **Subscription** or **Management Group**.
    
1. From the list, select which Azure subscription or management group that you want to add to the catalog.
    

1. With the resource selected, select **Add**.
    

## Add an Azure RBAC role to an access package

After you add an Azure resource to a catalog, you're now able to add it as a resource to access packages within that catalog. Azure resources can be added to both new, and existing, access packages. This section walks you through how to add an Azure RBAC role to an existing access package. To add an Azure RBAC role to an existing access package, you'd do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
    > [!TIP]
    > Other least privilege roles that can complete this task include the Catalog owner or Access Package manager.
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. Select an existing access package you want to add the Azure RBAC roles to.

1. On the access package overview page, select **Resources**.
     
1. On the add resources page, select **Azure Resources**.

1. On the **Select Azure Resources** pane, select either **Subscription** or **Management Group**.
    
1. From the list, select which Azure subscription or management group that you want to add to the access package.
    
1. If choosing subscription, under Scope, choose where the role assignment applies.
    
1. For **Role Type**, you can select the following types:
    **Active**: For roles that should be permanently assigned. <br>
    **Eligible**: For roles that require elevation via [Privileged Identity Management (PIM)](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) when needed. 
    
1. Select the Azure RBAC Role to assign. Both built-in roles and Azure Custom roles are available.
    

1. With the resource selected, select **Add** to add it to the access package.

## Related content

- [Assign Microsoft Entra roles (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-roles)
