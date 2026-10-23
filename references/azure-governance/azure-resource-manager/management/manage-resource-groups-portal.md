# Use the Azure portal and Azure Resource Manager to Manage Resource Groups

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal  
> Microsoft doc last updated: 02/27/2026


Learn how to use the [Azure portal](https://portal.azure.com) with [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) to manage Azure resource groups.

## What is a resource group

A resource group is a container that holds related resources for an Azure solution. The resource group can include all the resources for the solution or only those resources that you want to manage as a group. You decide how to allocate resources to resource groups based on what makes the most sense for your organization. Generally, add resources sharing the same lifecycle to the same resource group so you can easily deploy, update, and delete them as a group.

The Azure portal uses the resource group scope to create views that span across multiple resources. For example:

- **Metrics blade** provides metrics information (CPU, resources) to users.
- **Deployments blade** shows the history of ARM template or Bicep deployments targeted to that resource group (which includes portal deployments).
- **Policy blade** provides information related to the policies enforced on the resource group.
- **Diagnostics settings blade** provides errors and warnings to review.

The resource group stores metadata about the resources. When you specify a location for the resource group, you're specifying where that metadata is stored. For compliance reasons, you might need to ensure that your data is stored in a particular region. Resources inside a resource group can be in different regions.

## Create resource groups

1. Sign in to the [Azure portal](https://portal.azure.com).
1. Select **Resource groups**.
1. Select **Create**.

    

1. Enter the following values:

   - **Subscription**: Select your Azure subscription.
   - **Resource group**: Enter a new resource group name.
   - **Region**: Select an Azure location such as **Central US**.

     

1. Select **Review + Create**.
1. Select **Create**. It takes a few seconds to create a resource group.
1. To refresh the resource group list, select **Refresh** from the top menu. To open the newly created resource group, select it from the list. Or, select **Notification** (the bell icon) from the top, and then select **Go to resource group** to open the newly created resource group.

    

## List resource groups

1. Sign in to the [Azure portal](https://portal.azure.com).
1. To list the resource groups, select **Resource groups**.
1. To customize the information displayed for the resource groups, configure the filters. The following screenshot shows the other columns that you can add to the display:

    

## Open resource groups

1. Sign in to the [Azure portal](https://portal.azure.com).
1. Select **Resource groups**.
1. Select the resource group you want to open.

## Delete resource groups

1. Open the resource group you want to delete. See [Open resource groups](#open-resource-groups).
1. Select **Delete resource group**.

    

For more information about how Resource Manager arranges how resources are deleted, see [Azure Resource Manager resource group and resource deletion](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group).

## Deploy resources to a resource group

After you create a Resource Manager template, use the Azure portal to deploy your Azure resources. For information about creating a template, see [Quickstart: Create and deploy Azure Resource Manager templates by using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/quickstart-create-templates-use-the-portal). For information about using the portal to deploy a template, see [Deploy resources with Resource Manager templates and Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-portal).

## Move to another resource group or subscription

You can move resources from one resource group to another. For more information and guidance, see [Move Azure resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).

## Lock resource groups

Locking prevents other users in your organization from accidentally deleting or modifying critical resources like an Azure subscription, resource group, or resource.

1. Open the resource group that you want to lock. For more information, see [Open resource groups](#open-resource-groups).
1. In the left pane, select **Locks**.
1. To add a lock to the resource group, select **Add**.
1. Enter **Lock name**, **Lock type**, and **Notes**. The lock types include **Read-only** and **Delete**.

    

See [Lock your resources to protect your infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources) to learn more.

## Tag resource groups

Apply tags to resource groups and resources to logically organize your assets. For more information, see [Use tags to organize your Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-portal).

## Export resource groups to templates

To learn about exporting templates, see [Single and multi-resource export to template - Portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal).

## Manage access to resource groups

Use [Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) to manage access to resources in Azure. For more information, see [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

## Next steps

- To learn more about managing Azure resources, see [Manage Azure resources by using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-portal).
- To learn more about Resource Manager, see the [What is Azure Resource Manager?](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) overview.
- To learn the Resource Manager template syntax, see [Understand the structure and syntax of Azure Resource Manager templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax).
- To learn how to develop templates, see the step-by-step [Azure Resource Manager documentation tutorials](../index.yml).
- To view Azure Resource Manager template schemas, see [Define resources with Bicep, ARM templates, and Terraform AzAPI provider](https://learn.microsoft.com/en-us/azure/templates/).
