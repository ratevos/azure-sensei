# Enable eBPF Host Routing with Advanced Container Networking Services

> Source: https://learn.microsoft.com/en-us/azure/aks/how-to-enable-ebpf-host-routing  
> Microsoft doc last updated: 09/23/2025


This article shows you how to enable eBPF Host Routing with Advanced Container Networking Services (ACNS) on Azure Kubernetes Service (AKS) clusters.

## Requirements and parameters

| Requirement or parameter | Supported versions or values | Description |
| ------------------------ | ---------------------------- | ----------- |
| Azure CLI version | 2.71.0 or later | The Azure CLI version must be 2.71.0 or later to support eBPF Host Routing. |
| Kubernetes version | 1.33 or later | The Kubernetes version must be 1.33 or later to support eBPF Host Routing. |
| Node operating system | Azure Linux 3.0 or Ubuntu 24.04 | eBPF Host Routing is supported only on Azure CNI powered by Cilium clusters with Azure Linux 3.0 or Ubuntu 24.04. |
| Dataplane | Azure CNI powered by Cilium | eBPF Host Routing is supported only on AKS clusters that use Azure CNI powered by Cilium. |

Review the [Limitations](https://learn.microsoft.com/en-us/azure/aks/container-network-performance-ebpf-host-routing#limitations) section for node requirements and compatibility with existing iptable rules.

## Enable Advanced Container Networking Services and eBPF Host Routing

To proceed, you must have an AKS cluster with [Advanced Container Networking Services](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview) enabled.

The `az aks create` command with the Advanced Container Networking Services flag, `--enable-acns`, creates a new AKS cluster with all Advanced Container Networking Services features. These features encompass:
* **Container Network Observability:**  Provides insights into your network traffic. To learn more visit [Container Network Observability](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview#container-network-observability).

* **Container Network Security:** Offers security features like FQDN filtering. To learn more visit  [Container Network Security](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview#container-network-security).

* **Container Network Performance:** Improves latency and throughput for pod network traffic. To learn more visit [Container Network Performance](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview#container-network-performance)

Create an Azure resource group for the cluster using the [`az group create`](https://learn.microsoft.com/en-us/cli/azure/group#az-group-create) command.

```azurecli-interactive
export LOCATION="<location>"

az group create --location $LOCATION --name <resourcegroup-name>
```

Create a new AKS cluster with eBPF Host Routing by enabling ACNS through `--enable-acns` and setting the acceleration mode with `--acns-datapath-acceleration-mode BpfVeth`.

```azurecli-interactive
# Set environment variables for the AKS cluster name and resource group. Make sure to replace the placeholders with your own values.
export CLUSTER_NAME="<aks-cluster-name>"
export RESOURCE_GROUP="<resourcegroup-name>"
export LOCATION="<location>"
export OS_SKU="<os-sku>" # Use AzureLinux or Ubuntu2404
 
# Create an AKS cluster
az aks create \
    --name $CLUSTER_NAME \
    --resource-group $RESOURCE_GROUP \
    --location $LOCATION \
    --network-plugin azure \
    --network-plugin-mode overlay \
    --network-dataplane cilium \
    --kubernetes-version 1.33 \
    --os-sku $OS_SKU \
    --enable-acns \
    --acns-datapath-acceleration-mode BpfVeth \
    --generate-ssh-keys
```

## Enable eBPF Host Routing with Advanced Container Networking Services on an existing cluster

The [`az aks update`](https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-update) command with the Advanced Container Networking Services flag, `--enable-acns`, updates an existing AKS cluster with `--acns-datapath-acceleration-mode BpfVeth` to enable Advanced Container Networking Services features that includes [Container Network Observability](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview#container-network-observability), [Container Network Security](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview#container-network-security), and [Container Network Performance](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview#container-network-performance).

> [!NOTE]
> Enabling eBPF Host Routing on an existing cluster may disrupt existing connections.

```azurecli-interactive
az aks update \
    --resource-group $RESOURCE_GROUP \
    --name $CLUSTER_NAME \
    --enable-acns \
    --acns-datapath-acceleration-mode BpfVeth
```

## Disable eBPF Host Routing on an existing cluster

eBPF Host Routing can be disabled independently without affecting other ACNS features. To disable it, set the flag `--acns-datapath-acceleration-mode=None`.

```azurecli-interactive
az aks update \
    --resource-group $RESOURCE_GROUP \
    --name $CLUSTER_NAME \
    --enable-acns \
    --acns-datapath-acceleration-mode None
```

## Related content

* Get more information about [Advanced Container Networking Services for AKS](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview).
* Explore the [Container Network Observability feature](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview#container-network-observability) in Advanced Container Networking Services.
