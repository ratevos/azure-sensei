# Manage resources - Azure CLI

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-cli  
> Microsoft doc last updated: 02/27/2026


Learn how to use Azure CLI with [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) to manage your Azure resources. For managing resource groups, see [Manage Azure resource groups by using Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli).

## Deploy resources to an existing resource group

You can deploy Azure resources directly by using Azure CLI, or deploy a Resource Manager template to create Azure resources.

### Deploy a resource

The following script creates a storage account.

```azurecli-interactive
echo "Enter the Resource Group name:" &&
read resourceGroupName &&
echo "Enter the location (i.e. centralus):" &&
read location &&
echo "Enter the storage account name:" &&
read storageAccountName &&
az storage account create --resource-group $resourceGroupName --name $storageAccountName --location $location --sku Standard_LRS --kind StorageV2 &&
az storage account show --resource-group $resourceGroupName --name $storageAccountName 
```

### Deploy a template

The following script creates a Quickstart template to create a storage account. For more information, see [Quickstart: Create ARM templates with Visual Studio Code](../templates/quickstart-create-templates-use-visual-studio-code.md?tabs=PowerShell).

```azurecli-interactive
echo "Enter the Resource Group name:" &&
read resourceGroupName &&
echo "Enter the location (i.e. centralus):" &&
read location &&
az deployment group create --resource-group $resourceGroupName --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.storage/storage-account-create/azuredeploy.json"
```

For more information, see [Deploy resources with Resource Manager templates and Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-cli).

## Deploy a resource group and resources

You can create a resource group and deploy resources to the group. For more information, see [Create resource group and deploy resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-subscription#resource-groups).

## Deploy resources to multiple subscriptions or resource groups

Typically, you deploy all the resources in your template to a single resource group. However, there are scenarios where you want to deploy a set of resources together but place them in different resource groups or subscriptions. For more information, see [Deploy Azure resources to multiple subscriptions or resource groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-resource-group).

## Delete resources

The following script shows how to delete a storage account.

```azurecli-interactive
echo "Enter the Resource Group name:" &&
read resourceGroupName &&
echo "Enter the storage account name:" &&
read storageAccountName &&
az storage account delete --resource-group $resourceGroupName --name $storageAccountName 
```

For more information about how Azure Resource Manager orders the deletion of resources, see [Azure Resource Manager resource group deletion](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group).

## Move resources

The following script shows how to remove a storage account from one resource group to another resource group.

```azurecli-interactive
echo "Enter the source Resource Group name:" &&
read srcResourceGroupName &&
echo "Enter the destination Resource Group name:" &&
read destResourceGroupName &&
echo "Enter the storage account name:" &&
read storageAccountName &&
storageAccount=$(az resource show --resource-group $srcResourceGroupName --name $storageAccountName --resource-type Microsoft.Storage/storageAccounts --query id --output tsv) &&
az resource move --destination-group $destResourceGroupName --ids $storageAccount
```

For more information, see [Move resources to new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).

## Lock resources

Locking prevents other users in your organization from accidentally deleting or modifying critical resources, such as Azure subscription, resource group, or resource.

The following script locks a storage account so the account can't be deleted.

```azurecli-interactive
echo "Enter the Resource Group name:" &&
read resourceGroupName &&
echo "Enter the storage account name:" &&
read storageAccountName &&
az lock create --name LockSite --lock-type CanNotDelete --resource-group $resourceGroupName --resource-name $storageAccountName --resource-type Microsoft.Storage/storageAccounts 
```

The following script gets all locks for a storage account:

```azurecli-interactive
echo "Enter the Resource Group name:" &&
read resourceGroupName &&
echo "Enter the storage account name:" &&
read storageAccountName &&
az lock list --resource-group $resourceGroupName --resource-name $storageAccountName --resource-type Microsoft.Storage/storageAccounts --parent ""
```

The following script deletes a lock of a storage account:

```azurecli-interactive
echo "Enter the Resource Group name:" &&
read resourceGroupName &&
echo "Enter the storage account name:" &&
read storageAccountName &&
lockId=$(az lock show --name LockSite --resource-group $resourceGroupName --resource-type Microsoft.Storage/storageAccounts --resource-name $storageAccountName --output tsv --query id)&&
az lock delete --ids $lockId
```

For more information, see [Lock resources with Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources).

## Tag resources

Tagging helps you organize your resource group and resources logically. For information, see [Using tags to organize your Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-cli).

## Manage access to resources

[Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) is the way that you manage access to resources in Azure. For more information, see [Add or remove Azure role assignments using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli).

## Next steps

- To learn Azure Resource Manager, see [Azure Resource Manager overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview).
- To learn the Resource Manager template syntax, see [Understand the structure and syntax of Azure Resource Manager templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax).
- To learn how to develop templates, see the [step-by-step tutorials](../index.yml).
- To view the Azure Resource Manager template schemas, see [template reference](https://learn.microsoft.com/en-us/azure/templates/).
