# Snapshot Azure Kubernetes Service (AKS) node pools

> Source: https://learn.microsoft.com/en-us/azure/aks/node-pool-snapshot  
> Microsoft doc last updated: 01/29/2024


AKS releases a new node image weekly. Every new cluster, new node pool, or upgrade cluster always receives the latest image, which can make it hard to maintain consistency and have repeatable environments.

Node pool snapshots allow you to take a configuration snapshot of your node pool and then create new node pools or new clusters based of that snapshot for as long as that configuration and kubernetes version is supported. For more information on the supportability windows, see [Supported Kubernetes versions in AKS][supported-versions].

The snapshot is an Azure resource that contains the configuration information from the source node pool, such as the node image version, kubernetes version, OS type, and OS SKU. You can then reference this snapshot resource and the respective values of its configuration to create any new node pool or cluster based off of it.

## Before you begin

This article assumes that you have an existing AKS cluster. If you don't have an AKS cluster, for guidance on a designing an enterprise-scale implementation of AKS, see [Plan your AKS design][plan-aks-design].

### Limitations

- Any node pool or cluster created from a snapshot must use a VM from the same virtual machine family as the snapshot, for example, you can't create a new N-Series node pool based of a snapshot captured from a D-Series node pool because the node images in those cases are structurally different.
- Snapshots must be created same region as the source node pool, those snapshots can be used to create or update clusters and node pools in other regions.

## Take a node pool snapshot

In order to take a snapshot from a node pool, you need the node pool resource ID, which you can get from the following command:

```azurecli-interactive
NODEPOOL_ID=$(az aks nodepool show --name nodepool1 --cluster-name myAKSCluster --resource-group myResourceGroup --query id -o tsv)
```

> [!IMPORTANT]
> Your AKS node pool must be created or upgraded after Nov 10th, 2021 in order for a snapshot to be taken from it.
> If you are using the `aks-preview` Azure CLI extension version `0.5.59` or newer, the commands for node pool snapshot have changed. For updated commands, see the [Node Pool Snapshot CLI reference][az-aks-nodepool-snapshot].

Now, to take a snapshot from the previous node pool, you use the `az aks snapshot` CLI command.

```azurecli-interactive
az aks nodepool snapshot create --name MySnapshot --resource-group MyResourceGroup --nodepool-id $NODEPOOL_ID --location eastus
```

## Create a node pool from a snapshot

First, you need the resource ID from the snapshot that was previously created, which you can get from the following command:

```azurecli-interactive
SNAPSHOT_ID=$(az aks nodepool snapshot show --name MySnapshot --resource-group myResourceGroup --query id -o tsv)
```

Now, we can use the following command to add a new node pool based off of this snapshot.

```azurecli-interactive
az aks nodepool add --name np2 --cluster-name myAKSCluster --resource-group myResourceGroup --snapshot-id $SNAPSHOT_ID
```

## Upgrading a node pool to a snapshot

You can upgrade a node pool to a snapshot configuration if the snapshot Kubernetes version and node image version are more recent than the current node pool versions. And the snapshot node image version is within 90 days of the node image publish date.

First, you need the resource ID from the snapshot that was previously created, which you can get from the following command:

```azurecli-interactive
SNAPSHOT_ID=$(az aks nodepool snapshot show --name MySnapshot --resource-group myResourceGroup --query id -o tsv)
```

Now, we can use this command to upgrade this node pool to this snapshot configuration.

```azurecli-interactive
az aks nodepool upgrade --name nodepool1 --cluster-name myAKSCluster --resource-group myResourceGroup --snapshot-id $SNAPSHOT_ID
```

> [!NOTE]
> Your node pool image version is the same contained in the snapshot and remains the same throughout every scale operation. However, if this node pool is upgraded or a node image upgrade is performed without providing a snapshot-id the node image is upgraded to the latest version.

> [!NOTE]
> To upgrade only the node version for your node pool, use the `--node-image-only` flag. This is required when upgrading the node image version for a node pool based on a snapshot with an identical Kubernetes version.

## Create a cluster from a snapshot

When you create a cluster from a snapshot, the snapshot configuration creates the cluster original system pool.

First, you need the resource ID from the snapshot that was previously created, which you can get from the following command:

```azurecli-interactive
SNAPSHOT_ID=$(az aks nodepool snapshot show --name MySnapshot --resource-group myResourceGroup --query id -o tsv)
```

Now, we can use this command to create this cluster off of the snapshot configuration.

```azurecli-interactive
az aks create \
    --name myAKSCluster2 \
    --resource-group myResourceGroup \
    --snapshot-id $SNAPSHOT_ID \
    --generate-ssh-keys
```

## Next steps

- See the [AKS release notes](https://github.com/Azure/AKS/releases) for information about the latest node images.
- Learn how to upgrade the Kubernetes version with [Upgrade an AKS cluster][upgrade-cluster].
- Learn how to upgrade your node image version with [Node Image Upgrade][node-image-upgrade]
- Learn more about multiple node pools with [Create multiple node pools][use-multiple-node-pools].

[plan-aks-design]: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-start-here?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json
[supported-versions]: https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions
[upgrade-cluster]: https://learn.microsoft.com/en-us/azure/aks/upgrade-cluster
[node-image-upgrade]: https://learn.microsoft.com/en-us/azure/aks/node-image-upgrade
[github-schedule]: https://learn.microsoft.com/en-us/azure/aks/node-upgrade-github-actions
[use-multiple-node-pools]: https://learn.microsoft.com/en-us/azure/aks/create-node-pools
[max-surge]: https://learn.microsoft.com/en-us/azure/aks/upgrade-cluster#customize-node-surge-upgrade
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-aks-nodepool-snapshot]:https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[az-feature-list]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-list
[az-feature-register]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-register
[az-aks-install-cli]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-install-cli
[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
