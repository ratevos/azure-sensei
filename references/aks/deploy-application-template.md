# Deploy an Azure Kubernetes application by using an ARM template

> Source: https://learn.microsoft.com/en-us/azure/aks/deploy-application-template  
> Microsoft doc last updated: 05/15/2023


To deploy a Kubernetes application programmatically through Azure CLI, you select the Kubernetes application and settings, generate an ARM template, accept legal terms and conditions, and finally deploy the ARM template.

## Select Kubernetes application

First, you need to select the Kubernetes application that you want to deploy in the Azure portal.

1. In the Azure portal, go to the [Marketplace page](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/MarketplaceOffersBlade/selectedMenuItemId/home/fromContext/AKS).
1. Select your Kubernetes application.
1. Select the required plan.
1. Select the **Usage Information + Support** tab. Copy the values for `publisherID`, `productID`, and `planID`. You'll need these values later.

   

## Generate ARM template

Continue on to generate the ARM template for your deployment.

1. Select the **Create** button.
1. Fill out all the application (extension) details.
1. At the bottom of the **Review + Create** tab, select **Download a template for automation**. 

   

   If all the validations are passed, you'll see the ARM template in the editor.

   

1. Download the ARM template and save it to a file on your computer.

## Accept terms and agreements

Before you can deploy a Kubernetes application, you need to accept its terms and agreements. To do so, use [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/vm/image/terms) or [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/module/az.marketplaceordering/). Be sure to use the values you copied for `plan-publisher`, `plan-offerID`, and `plan-name` in your command.

```azurecli
az vm image terms accept --offer <Product ID> --plan <Plan ID> --publisher <Publisher ID>
```

> [!NOTE]
> Although this Azure CLI command is for VMs, it also works for containers. For more information, see the [`az cm image terms` reference](https://learn.microsoft.com/en-us/cli/azure/vm/image/terms).

```azurepowershell
## Get-AzMarketplaceTerms -Publisher <Publisher ID> -Product <Product ID> -Name <Plan ID>
```

## Deploy ARM template

Once you've accepted the terms, you can deploy your ARM template. For instructions, see [Tutorial: Create and deploy your first ARM template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-create-first-template).

## Next steps

- Learn about [Kubernetes applications available through Marketplace](https://learn.microsoft.com/en-us/azure/aks/deploy-marketplace).
- Learn about [cluster extensions](https://learn.microsoft.com/en-us/azure/aks/cluster-extensions).
