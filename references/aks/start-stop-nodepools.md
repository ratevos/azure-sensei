# Stop and start node pools in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/start-stop-nodepools  
> Microsoft doc last updated: 08/12/2026


You might not need to continuously run your AKS workloads. For example, you might have a development cluster that has node pools running specific workloads. To optimize your compute costs, you can completely stop your node pools in your AKS cluster. When you need to run your workloads again, you can restart the node pools. This article shows you how to stop and start node pools in an AKS cluster using the Azure CLI.

## Features and limitations

- You can't stop system pools.
- Spot node pools are supported.
- Stopped node pools can be upgraded.
- To stop a node pool, the cluster and user node pool must be running, and the node pool `provisioningState` must be `Succeeded`.
- To start a node pool, the cluster must be running and the user node pool must be stopped.
- You can't stop node pools from clusters that use [node auto-provisioning (NAP)](https://learn.microsoft.com/en-us/azure/aks/node-autoprovision).

> [!TIP]
> You can use Azure Copilot to stop and start your node pools in the Azure portal. For more information, see [Work with AKS clusters efficiently using Azure Copilot](https://learn.microsoft.com/en-us/azure/copilot/work-aks-clusters#start-and-stop-node-pools).

## Before you begin

This article assumes you have an existing AKS cluster. If you need an AKS cluster, create one using the [Azure CLI][aks-quickstart-cli], [Azure PowerShell][aks-quickstart-powershell], or the [Azure portal][aks-quickstart-portal].

This article requires Azure CLI version 2.38.0 or later. Run `az --version` to find your installed version. For more information about installing or upgrading the Azure CLI, see [Install the Azure CLI][install-azure-cli].

## Stop a running AKS node pool using the Azure CLI

Before you stop a node pool, confirm that the cluster and user node pool are running, the node pool `provisioningState` is `Succeeded`, and the cluster doesn't use node auto-provisioning.

> [!WARNING]
> Stopping a node pool stops all virtual machines in the pool. Before you stop the pool, ensure its workloads can tolerate an interruption or can run on another node pool.

1. Stop a running AKS node pool using the [`az aks nodepool stop`][az-aks-nodepool-stop] command.

    ```azurecli-interactive
    az aks nodepool stop --resource-group myResourceGroup --cluster-name myAKSCluster --nodepool-name testnodepool 
    ```

1. Verify your node pool stopped using the [`az aks nodepool show`][az-aks-nodepool-show] command.

    ```azurecli-interactive
    az aks nodepool show --resource-group myResourceGroup --cluster-name myAKSCluster --nodepool-name testnodepool
    ```

    The following condensed example output shows the `powerState` as `Stopped`:

    ```output
    {
    [...]
     "osType": "Linux",
        "podSubnetId": null,
        "powerState": {
            "code": "Stopped"
            },
        "provisioningState": "Succeeded",
        "proximityPlacementGroupId": null,
    [...]
    }
    ```

    > [!NOTE]
    > If the `provisioningState` shows `Stopping`, your node pool is still in the process of stopping.

    > [!NOTE]
    > Stopping the node pool also stops the [Cluster Autoscaler](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler-overview) for that node pool. Starting the node pool restarts its Cluster Autoscaler. Don't manually modify the number of virtual machine scale set instances in the pool while it's stopped. Directly modifying AKS-managed infrastructure resources is unsupported and can cause Cluster Autoscaler inconsistencies and operation failures. For more information, see [User customization of agent nodes](https://learn.microsoft.com/en-us/azure/aks/support-policies#user-customization-of-agent-nodes).

---

## Restart an AKS node pool using the Azure CLI

Before you start a node pool, confirm that the cluster is running and the user node pool is stopped.

1. Restart a [stopped node pool](#stop-a-running-aks-node-pool-using-the-azure-cli) using the [`az aks nodepool start`][az-aks-nodepool-start] command.

    ```azurecli-interactive
    az aks nodepool start --resource-group myResourceGroup --cluster-name myAKSCluster --nodepool-name testnodepool 
    ```

1. Verify your node pool started using the [`az aks nodepool show`][az-aks-nodepool-show] command.

    ```azurecli-interactive
    az aks nodepool show --resource-group myResourceGroup --cluster-name myAKSCluster --nodepool-name testnodepool
    ```

    The following condensed example output shows the `powerState` as `Running`:

    ```output
    {
    [...]
     "osType": "Linux",
        "podSubnetId": null,
        "powerState": {
            "code": "Running"
            },
        "provisioningState": "Succeeded",
        "proximityPlacementGroupId": null,
    [...]
    }
    ```

    > [!NOTE]
    > If the `provisioningState` shows `Starting`, your node pool is still in the process of starting.

---

## Next steps

- To learn how to scale `User` pools to 0, see [scale `User` pools to 0](https://learn.microsoft.com/en-us/azure/aks/scale-cluster#scale-user-node-pools-to-0).
- To learn how to stop your cluster, see [cluster start/stop](https://learn.microsoft.com/en-us/azure/aks/start-stop-cluster).
- To learn how to save costs using Spot instances, see [add a spot node pool to AKS](https://learn.microsoft.com/en-us/azure/aks/spot-node-pool).
- To learn more about the AKS support policies, see [AKS support policies](https://learn.microsoft.com/en-us/azure/aks/support-policies).

[aks-quickstart-cli]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli
[aks-quickstart-portal]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
[aks-quickstart-powershell]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-powershell
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[az-aks-nodepool-stop]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-stop
[az-aks-nodepool-start]:https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-start
[az-aks-nodepool-show]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-show
