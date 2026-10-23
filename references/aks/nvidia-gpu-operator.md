# Use NVIDIA GPU Operator on Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/nvidia-gpu-operator  
> Microsoft doc last updated: 07/02/2025


The NVIDIA GPU Operator automates the management and deployment of all NVIDIA software components needed to provision GPU including driver installation, the [NVIDIA device plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin?tab=readme-ov-file), the NVIDIA container runtime, and more. Since the NVIDIA GPU Operator handles these components, it's not necessary to separately install the NVIDIA device plugin on your AKS cluster. This also means that the automatic GPU driver installation should be skipped in order to use the NVIDIA GPU Operator on AKS.

> [!TIP]
> If you don't need the full control of the NVIDIA GPU Operator, [AKS-managed GPU node pools (preview)](https://learn.microsoft.com/en-us/azure/aks/aks-managed-gpu-nodes) install and maintain the NVIDIA driver, Kubernetes device plugin, and DCGM metrics exporter for you.

> [!IMPORTANT]
>
> Open-source software is mentioned throughout AKS documentation and samples. Software that you deploy is excluded from AKS service-level agreements, limited warranty, and Azure support. As you use open-source technology alongside AKS, consult the support options available from the respective communities and project maintainers to develop a plan.
>
> Microsoft takes responsibility for building the open-source packages that we deploy on AKS. That responsibility includes having complete ownership of the build, scan, sign, validate, and hotfix process, along with control over the binaries in container images. For more information, see [Vulnerability management for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-vulnerability-management#aks-container-images) and [AKS support coverage](https://learn.microsoft.com/en-us/azure/aks/support-policies#aks-support-coverage).

## Before you begin

- This article assumes you have an existing AKS cluster. If you don't have a cluster, create one using the [Azure CLI][aks-quickstart-cli], [Azure PowerShell][aks-quickstart-powershell], or the [Azure portal][aks-quickstart-portal].
- You need the Azure CLI version 2.72.2 or later installed to set the `--gpu-driver` field. Run `az --version` to find the version. If you need to install or upgrade, see [Install Azure CLI][install-azure-cli].

> [!NOTE]
> GPU-enabled VMs contain specialized hardware subject to higher pricing and region availability. For more information, see the [pricing][azure-pricing] tool and [region availability][azure-availability].

## Limitations

NVIDIA GPU Operator isn't supported for the following OS options: Windows Server versions, [Flatcar Container Linux for AKS (preview)][flatcar], and [Azure Linux with OS Guard for AKS (preview)][os-guard].

## Get the credentials for your cluster

Get the credentials for your AKS cluster using the [`az aks get-credentials`][az-aks-get-credentials] command. The following example command gets the credentials for the cluster `myAKSCluster` in the `myResourceGroup` resource group:

```azurecli-interactive
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
```

> [!NOTE]
> The NVIDIA GPU Operator is not compatible with multiple OS versions on the same AKS cluster.

### [Standard node pool](#tab/standard-node-pool)

1. Skip automatic GPU driver installation by creating an NVIDIA GPU-enabled node pool by using the [`az aks nodepool add`][az-aks-nodepool-add] command and setting the API field `--gpu-driver` to the value `none`. Setting this API field to `none` during node pool creation skips the default GPU driver installation. For an example, see [Skip GPU driver installation](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu#skip-gpu-driver-installation). This setting doesn't change any existing nodes. You can scale the node pool to zero and then back up to make the change take effect.

```azurecli-interactive
az aks nodepool add \
--resource-group myResourceGroup \
--cluster-name myAKSCluster \
--name gpunp \
--node-count 1 \
--node-vm-size Standard_NC4as_T4_v3 \
--node-taints sku=gpu:NoSchedule \
--gpu-driver none
```

1. Follow the NVIDIA documentation to [Install the GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html).

1. After you install the GPU Operator, check that your [GPUs are schedulable](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu#confirm-that-gpus-are-schedulable) and [run a GPU workload](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu#run-a-gpu-enabled-workload).

> [!NOTE]
> There might be additional considerations to take when using the NVIDIA GPU Operator and deploying on SPOT instances. Please refer to <https://github.com/NVIDIA/gpu-operator/issues/577>

### [Node Auto Provisioning node pool](#tab/nap-nodes)

1. Skip automatic GPU driver installation by setting the AKSNodeClass CRD `spec.gpu.mode` field to the value `none`. Setting this AKSNodeClass field to `none` skips the default GPU driver installation, see [this example](https://learn.microsoft.com/en-us/azure/aks/node-auto-provisioning-aksnodeclass#gpu-settings). The process replaces any existing nodes that use this AKSNodeClass CRD with a new node that has no GPU driver installed.

```yaml
apiVersion: karpenter.azure.com/v1beta1
kind: AKSNodeClass
metadata:
  name: my-node-class
spec:
  gpu:
    mode: 
      none
```

1. Follow the NVIDIA documentation to [Install the GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html).

1. After you install the GPU Operator, check that your [GPUs are schedulable](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu#confirm-that-gpus-are-schedulable) and [run a GPU workload](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu#run-a-gpu-enabled-workload).

> [!NOTE]
> There might be additional considerations to take when using the NVIDIA GPU Operator and deploying on SPOT instances. For more information, see <https://github.com/NVIDIA/gpu-operator/issues/577>.

## Next steps

- Compare with [AKS-managed GPU node pools (preview)](https://learn.microsoft.com/en-us/azure/aks/aks-managed-gpu-nodes), which install and maintain the NVIDIA driver, device plugin, and DCGM metrics exporter for you.
- [Monitor NVIDIA GPU metrics](https://learn.microsoft.com/en-us/azure/aks/monitor-gpu-metrics) using Azure Managed Prometheus and Azure Managed Grafana.
- Learn more about [Ray clusters on AKS](https://learn.microsoft.com/en-us/azure/aks/ray-overview).

[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[az-aks-nodepool-add]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-nodepool-add
[aks-quickstart-cli]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli
[aks-quickstart-portal]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
[aks-quickstart-powershell]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-powershell
[flatcar]: https://learn.microsoft.com/en-us/azure/aks/flatcar-container-linux-for-aks
[os-guard]: https://learn.microsoft.com/en-us/azure/aks/use-azure-linux-os-guard
[azure-pricing]: https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers
[azure-availability]: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
