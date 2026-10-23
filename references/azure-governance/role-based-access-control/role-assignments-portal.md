# Assign Azure roles using the Azure portal - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal  
> Microsoft doc last updated: 03/17/2026


[Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) is the authorization system you use to manage access to Azure resources. To grant access, you assign roles to users, groups, service principals, or managed identities at a particular scope. This article describes how to assign roles using the Azure portal.

If you need to assign administrator roles in Microsoft Entra ID, see [Assign Microsoft Entra roles to users](https://learn.microsoft.com/en-us/azure/active-directory/roles/manage-roles-portal).

## Prerequisites

To assign Azure roles, you must have:

- `Microsoft.Authorization/roleAssignments/write` permissions, such as [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator) or [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator)

## Step 1: Identify the needed scope

When you assign roles, you must specify a scope. A Scope is the set of resources the access applies to. In Azure, you can specify a scope at four levels from broad to narrow: [management group](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview), subscription, [resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups), and resource. For more information, see [Understand scope](https://learn.microsoft.com/en-us/azure/role-based-access-control/scope-overview).

1. Sign in to the [Azure portal](https://portal.azure.com).

1. In the Search box at the top, search for the scope you want to grant access to. For example, search for **Management groups**, **Subscriptions**, **Resource groups**, or a specific resource.

1. Click the specific resource for that scope.

   The following shows an example resource group.

   

## Step 2: Open the Add role assignment page

**Access control (IAM)** is the page that you typically use to assign roles to grant access to Azure resources. It's also known as identity and access management (IAM) and appears in several locations in the Azure portal.

1. Click **Access control (IAM)**.

   The following shows an example of the Access control (IAM) page for a resource group.

   

1. Click the **Role assignments** tab to view the role assignments at this scope.

1. Click **Add** > **Add role assignment**.

   If you don't have permissions to assign roles, the Add role assignment option will be disabled.

   

   The Add role assignment page opens.

## Step 3: Select the appropriate role

To select a role, follow these steps:

1. On the **Role** tab, select the tab for the type of role you want to assign.

   - **Job function roles** – Roles for general Azure resource management or roles for specific services.
   - **Privileged administrator roles** – Roles that grant privileged access, such as Owner, Contributor, User Access Administrator, or Role Based Access Control Administrator. For best practices when using privileged administrator role assignments, see [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices#limit-privileged-administrator-role-assignments).

   

1. Select a role from the list by clicking on it.

    Use the **Search** box to filter the list of roles by name or description. You can also filter roles by **Type** and **Category** to narrow down the results.

1. In the **Details** column, click **View** to get more details about a role.

   

   > [!TIP]
   > If you're unsure which role to assign, you can use Copilot to help you select the appropriate role. On the **Role** tab, click **Copilot can help pick role** to open the Copilot dialog box.
   >
   > 
   >
   > In the dialog box, describe what you need the user to be authorized to do. For example, *"Help me select a role to deploy and manage Azure functions"* or *"Which role should I use if I want a user to manage and view a workspace?"*
   >
   > Copilot suggests one or more roles based on your requirements. Click **Select permissions** to confirm, and then **Select role** to apply the recommendation, or click **Recommend other roles** to see alternatives.

1. Click **Next**.

## Step 4: Select who needs access

To select who needs access, follow these steps:

1. On the **Members** tab, select **User, group, or service principal** to assign the selected role to one or more Microsoft Entra users, groups, or service principals (applications).

   

1. Click **Select members**.

1. Find and select the users, groups, or service principals.

   You can type in the **Select** box to search the directory for display name or email address.

   

1. Click **Select** to add the users, groups, or service principals to the Members list.

1. To assign the selected role to one or more managed identities, select **Managed identity**.

1. Click **Select members**.

1. In the **Select managed identities** pane, select whether the type is [user-assigned managed identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) or [system-assigned managed identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview).

1. Find and select the managed identities.

   For system-assigned managed identities, you can select managed identities by Azure service instance.

   

1. Click **Select** to add the managed identities to the Members list.

1. In the **Description** box enter an optional description for this role assignment.

   Later you can show this description in the role assignments list.

1. Click **Next**.

## Step 5: (Optional) Add condition

If you selected a role that supports conditions, a **Conditions** tab will appear and you have the option to add a condition to your role assignment. A [condition](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-overview) is an additional check that you can optionally add to your role assignment to provide more fine-grained access control.

The **Conditions** tab will look different depending on the role you selected.

### Delegate condition

If you selected one of the following privileged roles, follow the steps in this section.

- [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner)
- [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator)
- [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator)

1. On the **Conditions** tab under **What user can do**, select the **Allow user to only assign selected roles to selected principals (fewer privileges)** option.

   

1. Click **Select roles and principals** to add a condition that constrains the roles and principals this user can assign roles to.

1. Follow the steps in [Delegate Azure role assignment management to others with conditions](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-portal#step-3-add-a-condition).

### Storage condition

If you selected one of the following storage roles, follow the steps in this section.

- [Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor)
- [Storage Blob Data Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner)
- [Storage Blob Data Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-reader)
- [Storage Queue Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-contributor)
- [Storage Queue Data Message Processor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-message-processor)
- [Storage Queue Data Message Sender](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-message-sender)
- [Storage Queue Data Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-reader)

1. Click **Add condition** if you want to further refine the role assignments based on storage attributes.

   

1. Follow the steps in [Add or edit Azure role assignment conditions](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-role-assignments-portal#step-3-review-basics).

## Step 6: Select assignment type

If you have a Microsoft Entra ID P2 or Microsoft Entra ID Governance license, an **Assignment type** tab will appear for management group, subscription, and resource group scopes. Use eligible assignments to provide just-in-time access to a role. Users with eligible and/or time-bound assignments must have a valid license.

If you don't want to use the PIM functionality, select the **Active** assignment type and **Permanent** assignment duration options. These settings create a role assignment where the principal always has permissions in the role.

This capability is being deployed in stages, so it might not be available yet in your tenant or your interface might look different. For more information, see [Eligible and time-bound role assignments in Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration).

1. On the **Assignment type** tab, select the **Assignment type**.

   - **Eligible** - User must perform one or more actions to use the role, such as perform a multifactor authentication check, provide a business justification, or request approval from designated approvers. You can't create eligible role assignments for applications, service principals, or managed identities because they can't perform the activation steps.
   - **Active** -  User doesn't have to perform any action to use the role.

   

1. Depending on your settings, for **Assignment duration**, select **Permanent** or **Time bound**.

   Select permanent if you want member to always be allowed to activate or use role. Select time bound to specify start and end dates. This option might be disabled if permanent assignments creation is not allowed by PIM policy.

1. If **Time bound** is selected, set **Start date and time** and **Start date and time** to specify when user is allowed to activate or use role.

   It's possible to set the start date in the future. The maximum allowed eligible duration depends on your Privileged Identity Management (PIM) policy.

1. (Optional) Use **Configure PIM Policy** to configure expiration options, role activation requirements (approval, multifactor authentication, or Conditional Access authentication context), and other settings.

   When you select the **Update PIM policy** link, a PIM page is displayed. Select **Settings** to configure PIM policy for roles. For more information, see [Configure Azure resource role settings in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-configure-role-settings).

1. Click **Next**.

## Step 7: Assign role

1. On the **Review + assign** tab, review the role assignment settings.

   

1. Click **Review + assign** to assign the role.

   After a few moments, the security principal is assigned the role at the selected scope.

   

1. If you don't see the description for the role assignment, click **Edit columns** to add the **Description** column.

## Edit assignment

If you have a Microsoft Entra ID P2 or Microsoft Entra ID Governance license, you can edit your role assignment type settings. For more information, see [Eligible and time-bound role assignments in Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration).

1. On the **Access control (IAM)** page, click the **Role assignments** tab to view the role assignments at this scope.

1. Find the role assignment that you want to edit.

1. In the **State** column, click the link, such as **Eligible time-bound** or **Active permanent**.

   The **Edit assignment** pane appears where you can update the role assignment type settings. The pane might take a few moments to open.

   

1. When finished, click **Save**.

   Your updates might take a while to be processed and reflected in the portal.

## Related content

- [Assign a user as an administrator of an Azure subscription](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal-subscription-admin)
- [Remove Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-remove)
- [Troubleshoot Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting)
