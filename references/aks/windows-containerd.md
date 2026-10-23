# Create Windows Server Node Pools with containerd in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/windows-containerd  
> Microsoft doc last updated: 09/26/2025


For Kubernetes version 1.20 and higher, you can specify [`containerd`](https://containerd.io/) as the container runtime for Windows Server 2019 node pools. Starting with Kubernetes 1.23, `containerd` is the default and only container runtime for Windows.

In this article, you learn how to create Windows Server node pools with `containerd` in Azure Kubernetes Service (AKS).

## Prerequisites

- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured. Find the version using the `az version` command. If you need to install or upgrade, see [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
- An existing AKS cluster with a system node pool. If you need to create one, see [Create an AKS cluster with a single node pool](https://learn.microsoft.com/en-us/azure/aks/create-node-pools#create-an-aks-cluster-with-a-single-node-pool-using-the-azure-cli).

## Limitations and considerations

When using Windows Server node pools with `containerd`, keep the following limitations and considerations in mind:

- Both the control plane and Windows Server 2019 node pools must use Kubernetes version 1.20 or greater.
- When you create or update a node pool to run Windows Server containers, the default value for `--node-vm-size` is `Standard_D2s_v3`, which was the minimum recommended size for Windows Server 2019 node pools up to Kubernetes version 1.20. The minimum recommended size for Windows Server 2019 node pools using `containerd` is `Standard_D4s_v3`. When setting the `--node-vm-size` parameter, check the [list of restricted virtual machine (VM) sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview).
- We recommend using [taints or labels](https://learn.microsoft.com/en-us/azure/aks/manage-node-pools#set-node-pool-taints) with your Windows Server 2019 node pools running `containerd` and tolerations or node selectors with your deployments to guarantee your workloads are scheduled correctly.

## Add a Windows Server node pool with `containerd`

- Add a Windows Server node pool with `containerd` into your existing cluster using the [`az aks nodepool add`][az-aks-nodepool-add].

    > [!NOTE]
    > If you don't specify the `WindowsContainerRuntime=containerd` custom header, the node pool still uses `containerd` as the container runtime by default.

    ```azurecli-interactive
    az aks nodepool add \
        --resource-group $RESOURCE_GROUP \
        --cluster-name $CLUSTER_NAME \
        --os-type Windows \
        --name $CONTAINER_D_NODE_POOL_NAME \
        --node-vm-size Standard_D4s_v3 \
        --kubernetes-version 1.20.5 \
        --aks-custom-headers WindowsContainerRuntime=containerd \
        --node-count 1
    ```

## Upgrade an existing Windows Server node pool to `containerd`

- Upgrade a specific node pool from Docker to `containerd` using the [`az aks nodepool upgrade`][az-aks-nodepool-upgrade] command.

    ```azurecli-interactive
    export CONTAINER_D_NODE_POOL_NAME="mywindowsnodepool"
    
    az aks nodepool upgrade \
        --resource-group $RESOURCE_GROUP \
        --cluster-name $CLUSTER_NAME \
        --name $CONTAINER_D_NODE_POOL_NAME \
        --kubernetes-version 1.20.7 \
        --aks-custom-headers WindowsContainerRuntime=containerd
    ```

## Upgrade all existing Windows Server node pools to `containerd`

- Upgrade all node pools from Docker to `containerd` using the [`az aks nodepool upgrade`][az-aks-nodepool-upgrade] command.

    ```azurecli-interactive
    az aks nodepool upgrade \
        --resource-group $RESOURCE_GROUP \
        --cluster-name $CLUSTER_NAME \
        --kubernetes-version 1.20.7 \
        --aks-custom-headers WindowsContainerRuntime=containerd
    ```

## Next steps

For more information about node pools in AKS, see [Manage node pools for a cluster in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/manage-node-pools).

[az-aks-nodepool-add]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-add
[az-aks-nodepool-upgrade]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-upgrade
