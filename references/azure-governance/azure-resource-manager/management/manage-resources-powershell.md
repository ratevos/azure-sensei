# Manage resources - Azure PowerShell

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-powershell  
> Microsoft doc last updated: 02/27/2026


Learn how to use Azure PowerShell with [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) to manage your Azure resources. For managing resource groups, see [Manage Azure resource groups by using Azure PowerShell](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-powershell).

Other articles about managing resources:

- [Manage Azure resources by using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-portal)
- [Manage Azure resources by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-cli)

## Deploy resources to an existing resource group

You can deploy Azure resources directly by using Azure PowerShell, or deploy a Resource Manager template to create Azure resources.

### Deploy a resource

The following script creates a storage account.

```azurepowershell-interactive
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name"
$location = Read-Host -Prompt "Enter the location (i.e. centralus)"
$storageAccountName = Read-Host -Prompt "Enter the storage account name"

# Create the storage account.
$storageAccount = New-AzStorageAccount -ResourceGroupName $resourceGroupName `
  -Name $storageAccountName `
  -Location $location `
  -SkuName "Standard_LRS"

# Retrieve the context.
$ctx = $storageAccount.Context
```

### Deploy a template

The following script deploys a Quickstart template to create a storage account. For more information, see [Quickstart: Create Azure Resource Manager templates by using Visual Studio Code](../templates/quickstart-create-templates-use-visual-studio-code.md?tabs=PowerShell).

```azurepowershell-interactive
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name"
$location = Read-Host -Prompt "Enter the location (i.e. centralus)"
$templateUri = "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-account-create/azuredeploy.json"
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateUri $templateUri -Location $location
```

For more information, see [Deploy resources with Resource Manager templates and Azure PowerShell](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-powershell).

## Deploy a resource group and resources

You can create a resource group and deploy resources to the group. For more information, see [Create resource group and deploy resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-subscription#resource-groups).

## Deploy resources to multiple subscriptions or resource groups

Typically, you deploy all the resources in your template to a single resource group. However, there are scenarios where you want to deploy a set of resources together but place them in different resource groups or subscriptions. For more information, see [Deploy Azure resources to multiple subscriptions or resource groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-resource-group).

## Delete resources

The following script shows how to delete a storage account.

```azurepowershell-interactive
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name"
$storageAccountName = Read-Host -Prompt "Enter the storage account name"

Remove-AzStorageAccount -ResourceGroupName $resourceGroupName -AccountName $storageAccountName
```

For more information about how Azure Resource Manager orders the deletion of resources, see [Azure Resource Manager resource group deletion](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group).

## Move resources

The following script shows how to remove a storage account from one resource group to another resource group.

```azurepowershell-interactive
$srcResourceGroupName = Read-Host -Prompt "Enter the source Resource Group name"
$destResourceGroupName = Read-Host -Prompt "Enter the destination Resource Group name"
$storageAccountName = Read-Host -Prompt "Enter the storage account name"

$storageAccount = Get-AzResource -ResourceGroupName $srcResourceGroupName -ResourceName $storageAccountName
Move-AzResource -DestinationResourceGroupName $destResourceGroupName -ResourceId $storageAccount.ResourceId
```

For more information, see [Move resources to new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).

## Lock resources

Locking prevents other users in your organization from accidentally deleting or modifying critical resources, such as Azure subscription, resource group, or resource.

The following script locks a storage account so the account can't be deleted.

```azurepowershell-interactive
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name"
$storageAccountName = Read-Host -Prompt "Enter the storage account name"

New-AzResourceLock -LockName LockStorage -LockLevel CanNotDelete -ResourceGroupName $resourceGroupName -ResourceName $storageAccountName -ResourceType Microsoft.Storage/storageAccounts 
```

The following script gets all locks for a storage account:

```azurepowershell-interactive
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name"
$storageAccountName = Read-Host -Prompt "Enter the storage account name"

Get-AzResourceLock -ResourceGroupName $resourceGroupName -ResourceName $storageAccountName -ResourceType Microsoft.Storage/storageAccounts
```

The following script deletes a lock of a storage account:

```azurepowershell-interactive
$resourceGroupName = Read-Host -Prompt "Enter the Resource Group name"
$storageAccountName = Read-Host -Prompt "Enter the storage account name"

$lockId = (Get-AzResourceLock -ResourceGroupName $resourceGroupName -ResourceName $storageAccountName -ResourceType Microsoft.Storage/storageAccounts).LockId
Remove-AzResourceLock -LockId $lockId
```

For more information, see [Lock resources with Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources).

## Tag resources

Tagging helps you organize your resource group and resources logically. For information, see [Using tags to organize your Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-powershell).

## Manage access to resources

[Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) is the way that you manage access to resources in Azure. For more information, see [Add or remove Azure role assignments using Azure PowerShell](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell).

## Next steps

- To learn Azure Resource Manager, see [Azure Resource Manager overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview).
- To learn the Resource Manager template syntax, see [Understand the structure and syntax of Azure Resource Manager templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax).
- To learn how to develop templates, see the [step-by-step tutorials](../index.yml).
- To view the Azure Resource Manager template schemas, see [template reference](https://learn.microsoft.com/en-us/azure/templates/).
