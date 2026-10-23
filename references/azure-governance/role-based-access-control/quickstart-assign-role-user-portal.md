# Tutorial: Grant a user access to Azure resources using the Azure portal - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/quickstart-assign-role-user-portal  
> Microsoft doc last updated: 03/30/2025


[Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) is the way that you manage access to Azure resources. In this tutorial, you grant a user access to create and manage virtual machines in a resource group.

In this tutorial, you learn how to:

> * Grant access for a user at a resource group scope
> * Remove access

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

## Sign in to Azure

Sign in to the [Azure portal](https://portal.azure.com).

## Create a resource group

1. In the navigation list, select **Resource groups**.

1. Select **New** to open the **Create a resource group** page.

    

1. Select a subscription.

1. For **Resource group** name, enter **example-group** or another name.

1. Select **Review + create** and then select **Create** to create the resource group.

1. Select **Refresh** to refresh the list of resource groups.

   The new resource group appears in your resource groups list.

## Grant access

In Azure RBAC, to grant access, you assign an Azure role.

1. In the list of **Resource groups**, open the new **example-group** resource group.

1. In the navigation menu, select **Access control (IAM)**.

1. Select the **Role assignments** tab to see the current list of role assignments.

    

1. Select **Add** > **Add role assignment**.

   If you don't have permissions to assign roles, the Add role assignment option will be disabled.

    

1. On the **Role** tab, select the **Virtual Machine Contributor** role.

    

1. On the **Members** tab, select yourself or another user.

1. On the **Review + assign** tab, review the role assignment settings.

1. Select **Review + assign** to assign the role.

   After a few moments, the user is assigned the Virtual Machine Contributor role at the example-group resource group scope.

    

## Remove access

In Azure RBAC, to remove access, you remove a role assignment.

1. In the list of role assignments, add a checkmark next to the user with the Virtual Machine Contributor role.

1. Select **Remove**.

    

1. In the remove role assignment message that appears, select **Yes**.

## Clean up

1. In the navigation list, select **Resource groups**.

1. Select **example-group** to open the resource group.

1. Select **Delete resource group** to delete the resource group.

1. On the **Are you sure you want to delete** pane, type the resource group name and then select **Delete**.

## Next steps

> [Tutorial: Grant a user access to Azure resources using Azure PowerShell](https://learn.microsoft.com/en-us/azure/role-based-access-control/tutorial-role-assignments-user-powershell)
