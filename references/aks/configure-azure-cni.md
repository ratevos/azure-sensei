# Configure Azure CNI Networking in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni  
> Microsoft doc last updated: 01/29/2026


This article shows you how to use Container Networking Interface (CNI) networking in Azure to create and use a virtual network subnet for an Azure Kubernetes Service (AKS) cluster. For more information on network options and considerations, see [Networking concepts for applications in Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/concepts-network).

## Prerequisites

### [Azure portal](#tab/configure-networking-portal)

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

### [Azure PowerShell](#tab/configure-networking-powershell)

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

- Azure Cloud Shell or Azure PowerShell.

  The steps in this article run the Azure PowerShell cmdlets interactively in [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview). To run the commands in Cloud Shell, select **Open Cloud Shell** at the upper-right corner of a code block. Select **Copy** to copy the code, and then paste it into Cloud Shell to run it. You can also run Cloud Shell from within the Azure portal.

  You can also [install Azure PowerShell locally](https://learn.microsoft.com/en-us/powershell/azure/install-azure-powershell) to run the cmdlets. The steps in this article require Azure PowerShell module version 5.4.1 or later. Run `Get-Module -ListAvailable Az` to find your installed version. If you need to upgrade for a specific operating system, see the installation instructions for [macOS][macOSUpgrade], [Windows][windowsUpgrade], or [Linux][linuxUpgrade].

  If you run PowerShell locally, run `Connect-AzAccount` to connect to Azure.

### [Azure CLI](#tab/configure-networking-cli)

- You need an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

---

## Configure networking

For information on planning IP addresses, see [IP address planning for your Azure Kubernetes Service clusters](https://learn.microsoft.com/en-us/azure/aks/concepts-network-ip-address-planning). If you bring your own virtual network, review the [virtual network prerequisites](https://learn.microsoft.com/en-us/azure/aks/concepts-network-cni-overview#aks-cni-networking-prerequisites).

### [Azure portal](#tab/configure-networking-portal)

1. Sign in to the [Azure portal](https://portal.azure.com/).

1. On the Azure portal home page, select **Create a resource**.

1. Under **Categories**, select **Containers** > **Azure Kubernetes Service (AKS)**.

1. On the **Basics** tab, configure the following settings:

   - Under **Project details**:
     - **Subscription**: Select your Azure subscription.
     - **Resource group**: Select **Create new**, enter a resource group name (such as **test-rg**), and then select **Ok**.
   - Under **Cluster details**:
     - **Kubernetes cluster name**: Enter a cluster name, such as **aks-cluster**.
     - **Region**: Select **East US 2**.

1. Select **Next** > **Next** to get to the **Networking** tab.

1. For **Container networking**, select **Azure CNI Node Subnet**.

1. Select **Review + create** > **Create**.

### [Azure PowerShell](#tab/configure-networking-powershell)

When you create an AKS cluster by using Azure PowerShell, you can also configure Azure CNI networking.

Use [New-AzAksCluster](https://learn.microsoft.com/en-us/powershell/module/az.aks/new-azakscluster) to create an AKS cluster with default settings and Azure CNI networking:

```azurepowershell-interactive
## Create a resource group for the AKS cluster. ##
$rg = @{
    Name = "test-rg"
    Location = "eastus2"
}
New-AzResourceGroup @rg

$net = @{
      NetworkPlugin = "azure"
      ResourceGroupName = "test-rg"
      Name = "aks-cluster"
}
New-AzAksCluster @net
```

### [Azure CLI](#tab/configure-networking-cli)

When you create an AKS cluster by using the Azure CLI, you can also configure Azure CNI networking.

Use [`az aks create`][az-aks-create] with the `--network-plugin azure` argument to create a cluster with [Azure CNI Node Subnet][azure-cni-node-subnet]:

```azurecli-interactive
az group create \
    --name test-rg \
    --location eastus2

az aks create \
    --resource-group test-rg \
    --name aks-cluster \
    --network-plugin azure \
    --generate-ssh-keys
```

---

## Related content

- [Configure Azure CNI Pod Subnet: Dynamic IP Allocation and enhanced subnet support in Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni-dynamic-ip-allocation)

[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[macOSUpgrade]: https://learn.microsoft.com/en-us/powershell/azure/install-azps-macos#update-the-azure-powershell-module
[windowsUpgrade]: https://learn.microsoft.com/en-us/powershell/azure/install-azps-windows#update-the-az-powershell-module
[linuxUpgrade]: https://learn.microsoft.com/en-us/powershell/azure/install-azps-linux#update-the-az-powershell-module
[azure-cni-node-subnet]: https://learn.microsoft.com/en-us/azure/aks/concepts-network-cni-overview
