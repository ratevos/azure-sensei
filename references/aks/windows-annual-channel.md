# Use Windows Server Annual Channel for Containers on Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/windows-annual-channel  
> Microsoft doc last updated: 07/01/2024


> [!IMPORTANT]
> Starting on **May 15, 2026**, AKS no longer supports Windows Server Annual Channel (Preview). AKS will no longer produce new Windows Server Annual Channel node images or provide security patches. You won't be able to create new node pools with Windows Server Annual Channel. On **May 15, 2027**, AKS will remove all existing Windows Server Annual Channel node images, which will cause scaling and remediation (reimage and redeploy) operations to fail. To avoid disruption, we recommend migrating to the [Long Term Servicing Channel (LTSC)](https://learn.microsoft.com/en-us/azure/aks/upgrade-windows-os).
>
> - Windows Server Annual Channel uses Windows Server 2022 base images, which will run on Windows Server 2022 and Windows Server 2025.
> - If you're using [Host Process Containers (HPC)](https://learn.microsoft.com/en-us/azure/aks/use-windows-hpc) or running other privileged containers for administration purposes, you need to do extra testing.
>
> For more information on this retirement, see the [Retirement GitHub issue](https://aka.ms/aks/windows-annual-channel-retirement). To stay informed on announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

AKS supports [Windows Server Annual Channel for Containers](https://techcommunity.microsoft.com/t5/windows-server-news-and-best/windows-server-annual-channel-for-containers/ba-p/3866248) in public preview. Each channel version is released annually and is supported for *two years*. This channel is beneficial if you require increased innovation cycles and portability.

Windows Server Annual Channel versions are based on the Kubernetes version of your node pool. To upgrade from one Annual Channel version to the next, you can [upgrade to a Kubernetes version][upgrade-aks-cluster] that supports the next Annual Channel version.

## Supported Annual Channel releases

AKS releases support for new releases of Windows Server Annual Channel for Containers in alignment with Kubernetes versions. For the latest updates, see the [AKS release notes][release-notes]. The following table provides an *estimated* release schedule for upcoming Annual Channel releases:

|  K8s version | Annual Channel (host) version | Container image supported | End of support date |
|--------------|-------------------|-------------------|-------------------|
| 1.28 | 23H2 (preview only) | Windows Server 2022 | End of 1.33 support |
| 1.34 | 24H2 | Windows Server 2022 & Windows Server 2025 | End of 1.35 support |

## Windows Server Annual Channel vs. Long Term Servicing Channel Releases (LTSC)

AKS supports Long Term Servicing Channel Releases (LTSC), including Windows Server 2025 and Windows Server 2022. These come from a different release channel than Windows Server Annual Channel for Containers. To view our current recommendations, see the [Windows best practices documentation][windows-best-practices].

> [!IMPORTANT]
> Starting on March 01, 2026, Azure Kubernetes Service (AKS) no longer supports Windows Server 2019 node pools. Node pools running Kubernetes version 1.33+ can't use Windows Server 2019. Starting on April 01, 2027, AKS will remove all existing node images for Windows Server 2019, meaning that scaling operations will fail. For more information on this retirement, see the [Retirement GitHub issue](https://github.com/Azure/AKS/issues/4091) and the [Azure Updates retirement announcement](https://azure.microsoft.com/updates?id=aks-will-stop-support-for-windows-server-2019-on-march-1-2026). To stay informed on announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

> [!IMPORTANT]
> Starting on June 30, 2028, Azure Kubernetes Service (AKS) no longer supports Windows Server 2022 node pools. Windows Server 2022 isn't supported in Kubernetes version 1.37 and later. Starting on June 30, 2029, AKS will remove all existing node images for Windows Server 2022, meaning that scaling operations will fail. For more information on this retirement, see the [Retirement GitHub issue](https://github.com/Azure/AKS/issues/4168) and the [Azure Updates retirement announcement](https://azure.microsoft.com/updates?id=ws2022-retirement-aks). To stay informed about announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

The following table compares Windows Server Annual Channel and Long Term Servicing Channel releases:

| Channel | Support | Upgrades |
|---------|---------|----------|
| Long Term Servicing Channel (LTSC) | LTSC channels are released every three years and are supported for five years. This channel is recommended for customers using Long Term Support. | To upgrade from one release to the next, you need to migrate your node pools to a new OS SKU option and rebuild your container images with the new OS version. |
| Windows Server Annual Channel for Containers | Annual Channel releases occur annually and are supported for two years. | To upgrade to the latest release, you can upgrade the Kubernetes version of your node pool. |

## Before you begin

* You need the Azure CLI version 2.56.0 or later installed and configured to set `os-sku` to `WindowsAnnual` with the `az aks nodepool add` command. Run `az --version` to find the version. If you need to install or upgrade, see [Install Azure CLI][install-azure-cli].

### Limitations

* Windows Server Annual Channel doesn't support Azure Network Policy Manager.

### Install the `aks-preview` Azure CLI extension

* Register or update the aks-preview extension using the [`az extension add`][az-extension-add] or [`az extension update`][az-extension-update] command.

    ```azurecli-interactive
    # Register the aks-preview extension
    az extension add --name aks-preview
    # Update the aks-preview extension
    az extension update --name aks-preview
    ```

### Register the `AKSWindowsAnnualPreview` feature flag

1. Register the `AKSWindowsAnnualPreview` feature flag using the [`az feature register`][az-feature-register] command.

    ```azurecli-interactive
    az feature register --namespace "Microsoft.ContainerService" --name "AKSWindowsAnnualPreview"
    ```

    It takes a few minutes for the status to show *Registered*.

2. Verify the registration status using the [`az feature show`][az-feature-show] command.

    ```azurecli-interactive
    az feature show --namespace "Microsoft.ContainerService" --name "AKSWindowsAnnualPreview"
    ```

3. When the status reflects *Registered*, refresh the registration of the *Microsoft.ContainerService* resource provider using the [`az provider register`][az-provider-register] command.

    ```azurecli-interactive
    az provider register --namespace Microsoft.ContainerService
    ```

## Use Windows Server Annual Channel for Containers on AKS

To use Windows Server Annual Channel on AKS, specify the following parameters:

* `os-type` set to `Windows`
* `os-sku` set to `WindowsAnnual`

Windows Server Annual Channel versions are based on the Kubernetes version of your node pool. To check which release you'll get based on the Kubernetes version of your node pool, see the [supported Annual Channel releases](#supported-annual-channel-releases).

### Create a new Windows Server Annual Channel node pool

#### [Azure CLI](#tab/azure-cli)

* Create a Windows Server Annual Channel node pool using the [`az aks nodepool add`][az-aks-nodepool-add] command. The following example creates a Windows Server Annual Channel node pool with the 23H2 release:

    ```azurecli-interactive
    az aks nodepool add \
        --resource-group $RESOURCE_GROUP_NAME \
        --cluster-name $CLUSTER_NAME \
        --os-type Windows \
        --os-sku WindowsAnnual \
        --kubernetes-version 1.29
        --name $NODE_POOL_NAME \
        --node-count 1
    ```

    > [!NOTE]
    > If you don't specify the Kubernetes version during node pool creation, AKS uses the same Kubernetes version as your cluster.

#### [Azure PowerShell](#tab/azure-powershell)

* Create a Windows Server Annual Channel node pool using the [`New-AzAksNodePool`][new-azaksnodepool] cmdlet.

    ```azurepowershell
    New-AzAksNodePool -ResourceGroupName $RESOURCE_GROUP_NAME `
        -ClusterName $CLUSTER_NAME `
        -VmSetType VirtualMachineScaleSets `
        -OsType Windows `
        -OsSKU WindowsAnnual `
        -Name $NODE_POOL_NAME
    ```

---

### Verify Windows Server Annual Channel node pool creation

* Verify Windows Server Annual Channel node pool creation by checking the OS SKU of your node pool using `kubectl describe node` command.

    ```bash
    kubectl describe node $NODE_POOL_NAME
    ```

    If you successfully created a Windows Server Annual Channel node pool, you should see the following output:

    ```output
    Name:               npwin
    Roles:              agent
    Labels:             agentpool=npwin
    ...
                        kubernetes.azure.com/os=windows
    ...
                        kubernetes.azure.com/node-image-version=AKSWindows-23H2-gen2
    ...
                        kubernetes.azure.com/os-sku=WindowsAnnual
    ```

### Upgrade an existing node pool to Windows Server Annual Channel

You can upgrade an existing node pool from an LTSC release to Windows Server Annual Channel by following the guidance in [Upgrade the OS version for your Azure Kubernetes Service (AKS) Windows workloads][upgrade-windows-os].

To upgrade from one Annual Channel version to the next, you can [upgrade to a Kubernetes version][upgrade-aks-cluster] that supports the next Annual Channel version.

## Next steps

To learn more about Windows Containers on AKS, see the following resources:

> [Windows best practices][windows-best-practices]
> [Windows FAQ][windows-faq]

[windows-best-practices]: https://learn.microsoft.com/en-us/azure/aks/windows-best-practices
[windows-FAQ]: ./windows-faq.yml
[upgrade-aks-cluster]: https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster
[upgrade-windows-os]: https://learn.microsoft.com/en-us/azure/aks/upgrade-windows-os
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview#add-extensions
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview#update-extensions
[az-feature-register]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-register
[az-feature-show]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-show
[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
[az-aks-nodepool-add]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-add
[new-azaksnodepool]: https://learn.microsoft.com/en-us/powershell/module/az.aks/new-azaksnodepool
[release-notes]: https://github.com/Azure/AKS/releases
