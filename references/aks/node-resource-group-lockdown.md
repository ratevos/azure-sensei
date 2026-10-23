# Deploy a Fully Managed Resource Group with Node Resource Group Lockdown in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/node-resource-group-lockdown  
> Microsoft doc last updated: 06/30/2026


**Applies to**: :heavy_check_mark: AKS Automatic :heavy_check_mark: AKS Standard

AKS deploys infrastructure into your subscription for connecting to and running your applications. Changes made directly to resources in the [node resource group][whatis-nrg] can affect cluster operations or cause future issues. For example, scaling, storage, or network configurations should be made through the Kubernetes API and not directly on these resources.

To prevent changes from being made to the node resource group, you can apply a deny assignment and block users from modifying resources created as part of the AKS cluster.

AKS Automatic is the recommended production-ready default for most AKS workloads. In AKS Automatic, node resource group lockdown is preconfigured as part of the fully managed node resource group model.

In AKS Standard, node resource group lockdown is optional and you can configure it with restriction levels.

For more information about AKS Automatic, see [What is AKS Automatic?](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic)

## Before you begin

If you're configuring lockdown on AKS Standard using Azure CLI, you need:

- Azure CLI version 2.44.0 or later. Run `az --version` to find the current version. If you need to install or upgrade, see [Install Azure CLI][azure-cli-install].

## Restriction levels

| Restriction level | Behavior |
| ----------------- | -------- |
| ReadOnly | You can view node resource group resources, but a deny assignment blocks direct updates. |
| Unrestricted | Direct updates to node resource group resources are allowed. |

## AKS Automatic

Node resource group lockdown is preconfigured on AKS Automatic clusters. You don't need to run a separate enable command.

To create an AKS Automatic cluster, see [Create an Azure Kubernetes Service (AKS) Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network).

## AKS Standard: create a cluster with node resource group lockdown

Create an AKS Standard cluster with node resource group lockdown using the [`az aks create`][az-aks-create] command with the `--nrg-lockdown-restriction-level` flag set to `ReadOnly`. This configuration allows you to view the resources but not modify them.

```azurecli-interactive
# Set environment variables
export RESOURCE_GROUP_NAME=<your-resource-group-name>
export CLUSTER_NAME=<your-cluster-name>

# Create an AKS Standard cluster with node resource group lockdown
az aks create \
    --name $CLUSTER_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --nrg-lockdown-restriction-level ReadOnly \
    --generate-ssh-keys
```

## AKS Standard: update a cluster with node resource group lockdown

Update an existing AKS Standard cluster with node resource group lockdown using the [`az aks update`][az-aks-update] command with the `--nrg-lockdown-restriction-level` flag set to `ReadOnly`. This configuration allows you to view the resources but not modify them.

```azurecli-interactive
# Set environment variables
export RESOURCE_GROUP_NAME=<your-resource-group-name>
export CLUSTER_NAME=<your-cluster-name>

# Update an existing AKS Standard cluster with node resource group lockdown
az aks update --name $CLUSTER_NAME --resource-group $RESOURCE_GROUP_NAME --nrg-lockdown-restriction-level ReadOnly
```

## AKS Standard: remove node resource group lockdown

Remove node resource group lockdown from an existing AKS Standard cluster using the [`az aks update`][az-aks-update] command with the `--nrg-lockdown-restriction-level` flag set to `Unrestricted`. This configuration allows you to view and modify the resources.

```azurecli-interactive
# Set environment variables
export RESOURCE_GROUP_NAME=<your-resource-group-name>
export CLUSTER_NAME=<your-cluster-name>

# Remove node resource group lockdown from an existing AKS Standard cluster
az aks update --name $CLUSTER_NAME --resource-group $RESOURCE_GROUP_NAME --nrg-lockdown-restriction-level Unrestricted
```

## Frequently asked questions (FAQs)

### Is node resource group lockdown enabled by default on AKS Automatic?

Yes, it's preconfigured on AKS Automatic clusters.

### Do I need to run lockdown commands on AKS Automatic?

No, lockdown commands are for AKS Standard configuration.

### When should I use ReadOnly on AKS Standard?

Use ReadOnly when you want stronger protection against direct infrastructure edits and prefer cluster changes through AKS and Kubernetes APIs.

## Related content

- Learn more about AKS Automatic in [What is AKS Automatic?](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic)
- Create an AKS Automatic cluster in [Create an Azure Kubernetes Service (AKS) Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network)
- Learn more about the node resource group in AKS in [Node resource group][whatis-nrg].

[whatis-nrg]: https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads#node-resource-group
[azure-cli-install]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[az-aks-update]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-update
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[az-feature-register]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-register
[az-feature-show]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-show
[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
