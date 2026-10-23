# Overview of AKS Automatic Clusters with Managed System Node Pools

> Source: https://learn.microsoft.com/en-us/azure/aks/automatic/aks-automatic-managed-system-node-pools-about  
> Microsoft doc last updated: 09/08/2026


This overview explains the managed system node pools feature, which is by default enabled on new AKS Automatic clusters and only available in AKS Automatic. Managed system node pools allow you to focus on your applications while AKS manages the underlying infrastructure, including system node pools, to optimize performance and reliability.

To create an AKS Automatic cluster with managed system node pools, see the [Quickstart: Create an Azure Kubernetes Service (AKS) Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network) quickstart.

## Key features and benefits

The managed system node pools feature allows you to focus on your applications while AKS Automatic ensures that the underlying infrastructure is optimized for performance and reliability. Key features and benefits include:

- **No operational overhead**: AKS provisions, upgrades, and scales the system node pools automatically, eliminating the need for manual intervention.
- **Simplified cluster creation**: You don't need to track or allocate compute quotas for system node pools because AKS handles quotas for you.
- **Cost efficiency**: Virtual machines (VMs) running on system node pools aren't charged to customer subscriptions, allowing you to optimize costs while maintaining high performance.
- **Enhanced performance**: Isolating system workloads from customer applications improves reliability and ensures consistent performance backed by [Services Level Agreements (SLAs)](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services).
- **Managed system node pool by default**: New AKS Automatic clusters enable managed system node pools by default. If you have an existing AKS Automatic cluster without managed system node pools, you can migrate the cluster to use managed system node pools in preview.
- **Autoscaling and Node repair**: [Cluster autoscaler](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler-overview) is enabled for system nodes in the managed system node pool. [Node auto-repair](https://learn.microsoft.com/en-us/azure/aks/node-auto-repair) is enabled for system nodes in the managed system node pool.

> [!IMPORTANT]
> Starting on AKS 1.36, new AKS Automatic clusters will by default enable [Kubernetes Gateway API via the application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api) instead of [Managed NGINX ingress with the application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing) due to the upstream [Ingress NGINX retirement](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/).
>
> Existing Automatic clusters aren't affected but should begin migration to [Kubernetes Gateway API via the application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api#enable-for-an-existing-cluster).

## Limitations

The following limitations apply to AKS Automatic clusters:

- AKS Automatic is generally available in the following regions: `australiacentral`, `australiaeast`, `australiasoutheast`, `austriaeast`, `belgiumcentral`, `brazilsouth`, `canadacentral`, `canadaeast`, `centralindia`, `centralus`, `chilecentral`, `denmarkeast`, `eastasia`, `eastus`, `eastus2`, `francecentral`, `germanywestcentral`, `indonesiacentral`, `israelcentral`, `italynorth`, `japaneast`, `japanwest`, `koreacentral`, `koreasouth`, `malaysiawest`, `mexicocentral`, `newzealandnorth`, `northcentralus`, `northeurope`, `norwayeast`, `polandcentral`, `southafricanorth`, `southcentralus`, `southeastasia`, `southindia`, `spaincentral`, `swedencentral`, `switzerlandnorth`, `uaenorth`, `uksouth`, `ukwest`, `westcentralus`, `westeurope`, `westus`, `westus2`, `westus3`.
- New AKS Automatic clusters by default enable managed system node pools and [LocalDNS](https://learn.microsoft.com/en-us/azure/aks/dns-concepts#localdns-in-azure-kubernetes-service). You can't create AKS Automatic clusters without managed system node pools in any region.
- AKS Automatic cluster has [node resource group lockdown](https://learn.microsoft.com/en-us/azure/aks/node-resource-group-lockdown) preconfigured, which doesn't allow changes to the `MC_` resource group, preventing virtual network links on the default Private DNS zone. For cross‑VNet or custom DNS scenarios, use custom network and private DNS by following [Create a private Azure Kubernetes Service (AKS) Automatic cluster in a custom virtual network](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-private-custom-network).
- Azure CLI version 2.86.0 or later is required. To find the version, run `az --version` command. If you need to install or upgrade, see [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli).
- The following extensions aren't supported:
  - [Dapr](https://learn.microsoft.com/en-us/azure/aks/dapr)
  - [Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-attach-kubernetes-anywhere)
- Windows nodes aren't supported.
- Migration from AKS base SKU to automatic SKU isn't supported.
- Migration from an existing AKS Automatic cluster without managed system node pools to AKS Automatic with managed system node pools is supported in preview in regions where managed system node pools are generally available. Migration from AKS Automatic with managed system node pools back to AKS Automatic without managed system node pools isn't supported.

## Components of managed system node pools

The following table outlines the components managed by AKS in managed system node pools. AKS handles the creation, upgrading, and scaling of the system nodes where these components run.

| Component | Namespace | Deployment |
|-----------|-----------|------------|
| [Workload identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) | `kube-system` | `azure-wi-webhook-controller-manager` |
| [CoreDNS](https://learn.microsoft.com/en-us/azure/aks/dns-concepts#coredns-in-azure-kubernetes-service) | `kube-system` | `coredns`, `coredns-autoscaler` |
| [Eraser](https://learn.microsoft.com/en-us/azure/aks/image-cleaner) | `kube-system` | `eraser-controller-manager` |
| [Kubernetes Event-driven Autoscaling (KEDA)](https://learn.microsoft.com/en-us/azure/aks/keda-about) | `kube-system` | `keda-admission-webhooks`, `keda-operator`, `keda-operator-metrics-apiserver` |
| [Konnectivity](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-konnectivity/) | `kube-system` | `konnectivity-agent`, `konnectivity-agent-autoscaler` |
| [Metrics Server](https://kubernetes-sigs.github.io/metrics-server/) | `kube-system` | `metrics-server` |
| [Vertical Pod Autoscaling (VPA)](https://learn.microsoft.com/en-us/azure/aks/vertical-pod-autoscaler) | `kube-system` | `vpa-admission-controller`, `vpa-recommender`, `vpa-updater` |

Other add-ons and extensions run on an `aks-system-surge` node, with scaling handled by [node auto-provisioning (NAP)](https://learn.microsoft.com/en-us/azure/aks/node-auto-provisioning). `DaemonSets` run on both managed system node pools and nodes in your subscription, including the `aks-system-surge` nodes.

## Migrate an existing AKS Automatic cluster to managed system node pools (preview)

AKS Automatic supports preview migration from non-managed system node pools to managed system node pools in regions where managed system node pools are generally available. To use this preview feature, register the `Microsoft.ContainerService/NonHoboToHoboConversionPreview` feature flag in your subscription, and then update the cluster with the `--enable-hosted-system` parameter.

```azurecli-interactive
az feature register \
    --namespace Microsoft.ContainerService \
    --name NonHoboToHoboConversionPreview
```

Check the registration status by using the [`az feature show`](https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-show) command:

```azurecli-interactive
az feature show \
    --namespace Microsoft.ContainerService \
    --name NonHoboToHoboConversionPreview \
    --query properties.state \
    --output tsv
```

Wait until the command returns `Registered` before you continue. Then, refresh the `Microsoft.ContainerService` resource provider registration.

```azurecli-interactive
az provider register --namespace Microsoft.ContainerService
```

To migrate an existing AKS Automatic cluster that uses AKS-managed networking, run the [`az aks update`](https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-update) command with the `--enable-hosted-system` parameter:

```azurecli-interactive
az aks update \
    --resource-group <resource-group> \
    --name <cluster-name> \
    --enable-hosted-system
```

For an AKS Automatic cluster that uses a custom virtual network, also provide the subnet for the managed system node pool. The system node subnet must be in the same virtual network and region as the cluster, be at least `/26`, and not be delegated to another service. The `--node-subnet-id` parameter is optional. If you don't provide it, AKS uses the existing system node pool subnet.

```azurecli-interactive
az aks update \
    --resource-group <resource-group> \
    --name <cluster-name> \
    --enable-hosted-system \
    --system-node-subnet-id <system-node-subnet-resource-id> \
    --node-subnet-id <node-subnet-resource-id>
```

For more information, see [Migrate between AKS Automatic and AKS Base clusters](https://learn.microsoft.com/en-us/azure/aks/automatic/aks-automatic-sku-migration).

## Security restrictions for managed system node pools

Since AKS manages the system node pool on your behalf, AKS applies multiple layers of security restrictions through built-in policies, baseline pod security standards, and admission time policies. These restrictions help protect managed system components and preserve the boundary between customer workloads and AKS-managed infrastructure.

| Restriction | What AKS prevents | Why it matters |
|-------------|-------------------|----------------|
| Managed system resource changes | Creating, updating, or deleting resources in AKS-managed system namespaces. | Helps protect AKS-managed components from customer-initiated changes. |
| Interactive access to system pods | Using pod `exec`, `attach`, or `port-forward` against AKS-managed system pods. | Helps prevent direct access to system workloads running on managed system node pools. |
| Managed system node changes | Modifying managed system nodes or labeling regular nodes as managed system nodes. | Helps maintain the boundary between customer-managed nodes and AKS-managed system nodes. |
| Workload placement on managed system nodes | Scheduling or running customer workloads on AKS-managed system nodes, including workloads with reserved tolerations, broad wildcard tolerations, or custom schedulers. | Helps prevent customer workloads from running on dedicated system nodes. |
| Privileged cluster access paths | Granting access to sensitive node proxy permissions. | Reduces paths that could bypass normal controls or escalate access to cluster resources. |
| Protected identity impersonation | Impersonating protected AKS, Kubernetes, or system service account identities. | Helps prevent callers from assuming identities used by trusted system components. |
| AKS-managed security control changes | Modifying AKS-managed security policies and admission controls. | Helps prevent weakening or disabling the controls that protect managed system node pools. |

### Unsupported AKS API operations

The following AKS API operations are **unsupported**:

- Upgrading a managed system node pool.
- Deleting a managed system node pool.
- Stopping a cluster with a managed system node pool.
- Listing agent pools on a cluster doesn't include managed system node pools.

## Next steps

> [Create an Azure Kubernetes Service (AKS) Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network)
