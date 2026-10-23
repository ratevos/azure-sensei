# List Available VM SKUs for Azure Kubernetes Service (AKS) Clusters (Preview)

> Source: https://learn.microsoft.com/en-us/azure/aks/aks-list-skus  
> Microsoft doc last updated: 05/19/2026


When you create an Azure Kubernetes Service (AKS) cluster or add a new node pool, you need to choose a VM SKU that's available in your target Azure region and supported by AKS. You can use the [`az aks list-vm-skus`][az-aks-list-vm-skus] command to quickly view SKUs for AKS in a specific region.

In this article, you learn how to:

- List VM SKUs for AKS in a specific region.
- Filter SKUs by exact or partial Azure VM size name.
- List only SKUs that support availability zones.
- Include all regional SKUs, including SKUs not currently available to your subscription.

> [!NOTE]
> This feature lists options of SKUs that are supported in AKS in the specified Azure region and does not consider your current quota or real-time available capacity. Visit the [Azure quota documentation](https://learn.microsoft.com/en-us/azure/quotas/view-quotas) to learn more about managing quota requests.

## Prerequisites

- Azure CLI installed and updated to minimum version `2.85.0`. If you need to install or update, see [Install Azure CLI][install-azure-cli].
- [Install and upgrade to latest version of the `aks-preview` extension](#install-the-aks-preview-cli-extension).

> [!TIP]
> If `az aks list-vm-skus` isn't recognized in your environment, update Azure CLI to the latest version and update installed AKS extensions.

### Install the `aks-preview` CLI extension

Install the aks-preview CLI extension by using the [`az extension add`][az-extension-add] command.

```azurecli-interactive
az extension add --name aks-preview
```

Update the extension to ensure you have the latest version installed by using the [`az extension update`][az-extension-update] command.

```azurecli-interactive
az extension update --name aks-preview
```

[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update

### Set environment variables

Set the following environment variables to use with commands in this article:

```azurecli-interactive
export RESOURCE_GROUP=<resource-group-name>
export CLUSTER_NAME=<cluster-name>
export LOCATION=<location>
```

## List supported VM SKUs on an AKS cluster

List supported VM SKUs on an AKS cluster using the [`az aks list-vm-skus`][az-aks-list-vm-skus] command.

```azurecli-interactive
LOCATION=eastus

az aks list-vm-skus \
  --location $LOCATION \
  --query "[].name" \
  --output table
```

Example output:

```output
Result
--------------------------
Standard_D2ds_v5
Standard_D4ds_v5
Standard_D8ds_v5
Standard_E4ds_v5
Standard_E8ds_v5
```

By default, this command only returns VM SKUs available to your current Azure subscription.

## Filter by Azure VM size name

List supported VM SKUs on an AKS cluster using the [`az aks list-vm-skus`][az-aks-list-vm-skus] command with the `--size` parameter to apply a case-insensitive partial match against the SKU name. The following example sets `--size` to _d4ds_:

```azurecli-interactive
az aks list-vm-skus \
  --location $LOCATION \
  --size d4ds \
  --query "[].name" \
  --output table
```

Example output:

```output
Result
--------------------
Standard_D4ds_v5
Standard_D4ds_v6
```

## Show only zone-capable Azure VM SKUs

List supported VM SKUs on an AKS cluster using the [`az aks list-vm-skus`][az-aks-list-vm-skus] command with the `--zone` parameter to return only SKUs that support availability zones in the selected region.

```azurecli-interactive
az aks list-vm-skus \
  --location $LOCATION \
  --zone \
  --query "[].{name:name,zones:join(', ', locationInfo[0].zones)}" \
  --output table
```

Example output:

```output
Name                Zones
------------------  ---------
Standard_D4ds_v5    [1, 2, 3]
Standard_E8ds_v5    [1, 2, 3]
```

## Include all SKUs in the Azure region

List supported VM SKUs on an AKS cluster using the [`az aks list-vm-skus`][az-aks-list-vm-skus] command with the `--all` parameter to include SKUs that might not currently be available to your subscription.

```azurecli-interactive
az aks list-vm-skus \
  --location $LOCATION \
  --all \
  --query "[].name" \
  --output table
```

> [!NOTE]
> AKS uses a best-effort approach to provision VM SKUs. A SKU appearing in this list doesn't guarantee allocation success at deployment time.

## View full details in JSON

List supported VM SKUs on an AKS cluster using the [`az aks list-vm-skus`][az-aks-list-vm-skus] command with the `--output` parameter set to _jsonc_ to return a JSON output with all returned properties of the supported Azure VM SKUs.

```azurecli-interactive
az aks list-vm-skus \
  --location $LOCATION \
  --zone \
  --output jsonc
```

Example output:

```json
[
  {
    "name": "Standard_D4ds_v5",
    "locationInfo": [
      {
        "location": "eastus",
        "zones": [
          "1",
          "2",
          "3"
        ]
      }
    ]
  },
  {
    "name": "Standard_E8ds_v5",
    "locationInfo": [
      {
        "location": "eastus",
        "zones": [
          "1",
          "2",
          "3"
        ]
      }
    ]
  }
]
```

The exact set of returned properties might vary by Azure CLI or API version.

## Use a returned SKU for AKS cluster or node pool creation

After you identify a suitable Azure VM SKU in your target region, specify the name with the `--node-vm-size` parameter when creating your AKS cluster or node pool. The following examples set the VM size to `Standard_D4ds_v5`:

```azurecli-interactive
RESOURCE_GROUP=myResourceGroup
CLUSTER_NAME=myAKSCluster
VM_SIZE=Standard_D4ds_v5

az aks create \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --node-count 3 \
  --node-vm-size $VM_SIZE \
  --generate-ssh-keys

az aks nodepool add \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --node-count 1 \
  --node-vm-size $VM_SIZE \
```

## Troubleshooting

- If no suitable Azure VM SKU appears, verify regional availability and quota by reviewing [Quotas, virtual machine size restrictions, and region availability in Azure Kubernetes Service (AKS)][quotas-skus-regions].
- If AKS cluster or node pool creation fails with allocation or capacity errors, rerun `az aks list-vm-skus` and select another SKU family or region.

## Related content

- Learn more about AKS limits and regional availability in [Quotas, virtual machine size restrictions, and region availability in Azure Kubernetes Service (AKS)][quotas-skus-regions].
- Compare Azure VM options in [Sizes for virtual machines in Azure][azure-vm-sizes].
- Create your first AKS cluster using [Quickstart: Deploy an AKS cluster using Azure CLI][aks-quickstart-cli].

[az-aks-list-vm-skus]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-list-vm-skus
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[quotas-skus-regions]: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions
[azure-vm-sizes]: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes
[aks-quickstart-cli]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli
[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az_aks_get_credentials
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
