# Quickstart - Check access for a user to a single Azure resource - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access  
> Microsoft doc last updated: 12/12/2024


Sometimes you need to check what access a user has to an Azure resource. You check their access by listing their assignments. A quick way to check the access for a single user is to use the **Check access** feature on the **Access control (IAM)** page.

## Step 1: Open the Azure resource

To check the access for a user, you first need to open the Azure resource you want to check access for. Azure resources are organized into levels that are typically called the *scope*. In Azure, you can specify a scope at four levels from broad to narrow: management group, subscription, resource group, and resource.

Follow these steps to open the Azure resource that you want to check access for.

1. Open the [Azure portal](https://portal.azure.com).

1. Open the Azure resource you want to check access for, such as **Management groups**, **Subscriptions**, **Resource groups**, or a particular resource.

1. Select the specific resource in that scope.

    The following shows an example resource group.

    

## Step 2: Check your access

Follow these steps to check your access to the previously selected Azure resource.

If you have a Microsoft Entra ID P2 or Microsoft Entra ID Governance license, [Microsoft Entra Privileged Identity Management (PIM)](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) functionality is integrated so you should follow the steps on the **PIM** tab.

# [Default](#tab/default)

1. Select **Access control (IAM)**.

    The following shows an example of the Access control (IAM) page for a resource group.

    

1. On the **Check access** tab, select the **View my access** button.

    An assignments pane appears that lists your access at this scope and inherited to this scope. Assignments at child scopes aren't listed.

    

# [PIM](#tab/pim)

1. Select **Access control (IAM)**.

1. On the **Check access** tab, view your role assignments at this scope and inherited to this scope. Assignments at child scopes aren't listed.

    The following shows an example of the Access control (IAM) page for a resource group.

    

    This page lists any [eligible and time-bound role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration). To activate any eligible role assignments, select **Activate role**. For more information, see [Activate eligible Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-eligible-activate).

---

## Step 3: Check access for a user

Follow these steps to check the access for a single user, group, service principal, or managed identity to the previously selected Azure resource.

1. Select **Access control (IAM)**.

1. On the **Check access** tab, select the **Check access** button.

    A **Check access** pane appears.

1. Select **User, group, or service principal**.

1. In the search box, enter a string to search the directory for name or email addresses.

    

1. Select the user to open the **assignments** pane.

    On this pane, you can see the access for the selected user at this scope and inherited to this scope. Assignments at child scopes aren't listed. You see the following assignments:

    - Role assignments added with Azure RBAC.
    - Deny assignments added using Azure Blueprints or Azure managed apps.

    If there are any [eligible or time-bound role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration), you can view these assignments on the **Eligible assignments** tab.

    

## Next steps

> [List Azure role assignments using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal)
