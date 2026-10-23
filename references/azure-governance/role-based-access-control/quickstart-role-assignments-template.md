# Quickstart: Assign an Azure role using an Azure Resource Manager template - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/quickstart-role-assignments-template  
> Microsoft doc last updated: 12/01/2023


[Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) is the way that you manage access to Azure resources. In this quickstart, you create a resource group and grant a user access to create and manage virtual machines in the resource group. This quickstart uses an Azure Resource Manager template (ARM template) to grant the access.

If your environment meets the prerequisites and you're familiar with using ARM templates, select the **Deploy to Azure** button. The template will open in the Azure portal.

## Prerequisites

To assign Azure roles and remove role assignments, you must have:

- If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- `Microsoft.Authorization/roleAssignments/write` and `Microsoft.Authorization/roleAssignments/delete` permissions, such as [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator)
- To assign a role, you must specify three elements: security principal, role definition, and scope. For this quickstart, the security principal is you or another user in your directory, the role definition is [Virtual Machine Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-contributor), and the scope is a resource group that you specify.

## Review the template

The template used in this quickstart is from [Azure Quickstart Templates](https://azure.microsoft.com/resources/templates/rbac-builtinrole-resourcegroup/). The template has two parameters and a resources section. In the resources section, notice that it has the three elements of a role assignment: security principal, role definition, and scope.

:::code language="json" source="~/quickstart-templates/quickstarts/microsoft.authorization/rbac-builtinrole-resourcegroup/azuredeploy.json":::

The resource defined in the template is:

- [Microsoft.Authorization/roleAssignments](https://learn.microsoft.com/en-us/azure/templates/Microsoft.Authorization/roleAssignments)

## Deploy the template

1. Sign in to the [Azure portal](https://portal.azure.com).

1. Determine your email address that is associated with your Azure subscription. Or determine the email address of another user in your directory.

1. Open Azure Cloud Shell for PowerShell.

1. Copy and paste the following script into Cloud Shell.

    ```azurepowershell
    $resourceGroupName = Read-Host -Prompt "Enter a resource group name (i.e. ExampleGrouprg)"
    $emailAddress = Read-Host -Prompt "Enter an email address for a user in your directory"
    $location = Read-Host -Prompt "Enter a location (i.e. centralus)"

    $roleAssignmentName = New-Guid
    $principalId = (Get-AzAdUser -Mail $emailAddress).id
    $roleDefinitionId = (Get-AzRoleDefinition -name "Virtual Machine Contributor").id
    $templateUri = "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.authorization/rbac-builtinrole-resourcegroup/azuredeploy.json"

    New-AzResourceGroup -Name $resourceGroupName -Location $location
    New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateUri $templateUri -roleDefinitionID $roleDefinitionId -principalId $principalId
    ```

1. Enter a resource group name such as ExampleGrouprg.

1. Enter an email address for yourself or another user in your directory.

1. Enter a location for the resource group such as centralus.

1. If necessary, press Enter to run the New-AzResourceGroupDeployment command.

    The [New-AzResourceGroup](https://learn.microsoft.com/en-us/powershell/module/az.resources/new-azresourcegroup) command creates a new resource group and the [New-AzResourceGroupDeployment](https://learn.microsoft.com/en-us/powershell/module/az.resources/new-azresourcegroupdeployment) command deploys the template to add the role assignment.

    You should see output similar to the following:

    ```azurepowershell
    PS> New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateUri $templateUri -roleAssignmentName $roleAssignmentName -roleDefinitionID $roleDefinitionId -principalId $principalId

    DeploymentName          : azuredeploy
    ResourceGroupName       : ExampleGrouprg
    ProvisioningState       : Succeeded
    Timestamp               : 5/22/2020 9:01:30 PM
    Mode                    : Incremental
    TemplateLink            :
                              Uri            : https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.authorization/rbac-builtinrole-resourcegroup/azuredeploy.json
                              ContentVersion : 1.0.0.0

    Parameters              :
                              Name                  Type                       Value
                              ====================  =========================  ==========
                              roleDefinitionID      String                     9980e02c-c2be-4d73-94e8-173b1dc7cf3c
                              principalId           String                     {principalId}

    Outputs                 :
    DeploymentDebugLogLevel :
    ```

## Review deployed resources

1. In the Azure portal, open the resource group you created.

1. In the left menu, click **Access control (IAM)**.

1. Click the **Role assignments** tab.

1. Verify that the **Virtual Machine Contributor** role is assigned to the user you specified.

   

## Clean up resources

To remove the role assignment and resource group you created, follow these steps.

1. Copy and paste the following script into Cloud Shell.

    ```azurepowershell
    $emailAddress = Read-Host -Prompt "Enter the email address of the user with the role assignment to remove"
    $resourceGroupName = Read-Host -Prompt "Enter the resource group name to remove (i.e. ExampleGrouprg)"

    $principalId = (Get-AzAdUser -Mail $emailAddress).id

    Remove-AzRoleAssignment -ObjectId $principalId -RoleDefinitionName "Virtual Machine Contributor" -ResourceGroupName $resourceGroupName
    Remove-AzResourceGroup -Name $resourceGroupName
    ```

1. Enter the email address of the user with the role assignment to remove.

1. Enter the resource group name to remove such as ExampleGrouprg.

1. If necessary, press Enter to run the Remove-AzResourceGroup command.

1. Enter **Y** to confirm that you want to remove the resource group.

## Next steps

> [Tutorial: Grant a user access to Azure resources using Azure PowerShell](https://learn.microsoft.com/en-us/azure/role-based-access-control/tutorial-role-assignments-user-powershell)
