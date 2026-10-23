# Move regions for resources in Microsoft.Resources

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/microsoft-resources-move-regions  
> Microsoft doc last updated: 02/27/2026


You might need to move an existing resource to a new region. This article shows how to move two resource types - templateSpecs and deploymentScripts - that are in the Microsoft.Resources namespace.

## Move template specs to new region

If you have a [template spec](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-specs) in one region and want to move it to new region, you can export the template spec and redeploy it.

1. Use the command to export an existing template spec. For the parameter values, provide the values that match the template spec you want to export.

   For Azure PowerShell, use:

   ```azurepowershell
   Export-AzTemplateSpec `
     -ResourceGroupName demoRG `
     -Name demoTemplateSpec `
     -Version 1.0 `
     -OutputFolder c:\export
   ```

   For Azure CLI, use:

   ```azurecli
   az template-specs export \
     --resource-group demoRG \
     --name demoTemplateSpec \
     --version 1.0 \
     --output-folder c:\export
   ```

1. Use the exported template spec to create a new template spec. The following examples show `westus` for the new region but you can provide the region you want.

   For Azure PowerShell, use:

   ```azurepowershell
   New-AzTemplateSpec `
     -Name movedTemplateSpec `
     -Version 1.0 `
     -ResourceGroupName newRG `
     -Location westus `
     -TemplateJsonFile c:\export\1.0.json
   ```

   For Azure CLI, use:

   ```azurecli
   az template-specs create \
     --name movedTemplateSpec \
     --version "1.0" \
     --resource-group newRG \
     --location "westus" \
     --template-file "c:\export\demoTemplateSpec.json"
   ```

## Move deployment scripts to new region

1. Select the resource group that contains the deployment script you want to move to a new region.

1. [Export the template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal). When exporting, select the deployment script and any other required resources.

1. Delete the following properties in the exported template:

   * tenantId
   * principalId
   * clientId

1. Find the hardcoded value for the region of the deployment script.

   ```json
   "location": "westus2",
   ```

   Change the template to allow a parameter for setting the location. For more information, see [Set resource location in ARM template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/resource-location).

   ```json
   "location": "[parameters('location')]",
   ```

1. [Deploy the exported template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-powershell) and specify a new region for the deployment script.

## Next steps

* To learn about moving resources to a new resource group or subscription, see [Move resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).
* To learn about moving resources to a new region, see [Move resources across regions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resources-overview#move-resources-across-regions).
