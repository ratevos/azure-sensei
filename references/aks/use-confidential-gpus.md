# Use Confidential GPUs on Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/use-confidential-gpus  
> Microsoft doc last updated: 09/17/2026


Confidential GPUs provide hardware-based security and isolation for workloads running on Azure Kubernetes Service (AKS). They help protect sensitive data and computations from unauthorized access, even from privileged users. To create a node pool with Confidential GPUs, you need to skip the automatic GPU driver installation and install the NVIDIA GPU Operator to provide the signed drivers.

This article shows you how to create an AKS node pool with a [NCCads_H100_v5 sizes series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nccadsh100v5-series) VM size.

By enabling confidential computing on GPUs, you have more options and flexibility to run your workloads securely and efficiently on the cloud. These virtual machines (VMs) are ideal for inferencing, fine-tuning, or training small-to-medium sized models. You can also use them for applied AI workloads, such as:

- GPU-accelerated analytics and databases
- Batch inferencing with heavy pre-processing and post-processing
- Machine learning (ML) development
- Video processing
- AI/ML web services

## Limitations

- Confidential GPUs aren't supported for Windows nodes.
- You can't use Confidential GPUs with [node auto-provisioning (NAP)](https://learn.microsoft.com/en-us/azure/aks/use-node-auto-provisioning).

## Prerequisites

- This article assumes you have an existing AKS cluster. If you don't have a cluster, create one using the [Azure CLI][aks-quickstart-cli], [Azure PowerShell][aks-quickstart-powershell], or the [Azure portal][aks-quickstart-portal].
- You need the Azure CLI version 2.72.2 or later installed to set the `--gpu-driver` field. Run `az --version` to find the version. If you need to install or upgrade, see [Install Azure CLI][install-azure-cli].

> [!NOTE]
> GPU-enabled VMs contain specialized hardware subject to higher pricing and region availability. For more information, see the [pricing][azure-pricing] tool and [region availability][azure-availability].

## Get the credentials for your cluster

Get the credentials for your AKS cluster by using the [`az aks get-credentials`][az-aks-get-credentials] command. The following example gets the credentials for the cluster _myAKSCluster_ in the _myResourceGroup_ resource group:

```azurecli-interactive
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
```

> [!NOTE]
> The NVIDIA GPU Operator isn't compatible with multiple OS versions on the same AKS cluster.

## Create a node pool with Confidential GPUs

The NVIDIA GPU Operator automates the management and deployment of all NVIDIA software components needed to provision a GPU, including driver installation, the [NVIDIA device plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin), the NVIDIA container runtime, and more. Because the NVIDIA GPU Operator handles these components, you don't need to separately install the NVIDIA device plugin on your AKS cluster. This setup also means you should skip automatic GPU driver installation to use the NVIDIA GPU Operator on AKS.

> [!IMPORTANT]
>
> Open-source software is mentioned throughout AKS documentation and samples. Software that you deploy is excluded from AKS service-level agreements, limited warranty, and Azure support. As you use open-source technology alongside AKS, consult the support options available from the respective communities and project maintainers to develop a plan.
>
> Microsoft takes responsibility for building the open-source packages that we deploy on AKS. That responsibility includes having complete ownership of the build, scan, sign, validate, and hotfix process, along with control over the binaries in container images. For more information, see [Vulnerability management for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-vulnerability-management#aks-container-images) and [AKS support coverage](https://learn.microsoft.com/en-us/azure/aks/support-policies#aks-support-coverage).

The following example shows how to create an AKS node pool with Confidential GPUs by using the [Azure NCCads_H100_v5](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nccadsh100v5-series?tabs=sizebasic#sizes-in-series) VM size.

1. Skip automatic GPU driver installation by creating an NVIDIA GPU-enabled node pool by using the [`az aks nodepool add`][az-aks-nodepool-add] command and setting the API field `--gpu-driver` to the value `none`. Setting this API field to `none` during node pool creation skips the default GPU driver installation. For an example, see [Skip GPU driver installation](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu#skip-gpu-driver-installation). This setting doesn't change any existing nodes. You can scale the node pool to zero and then back up to make the change take effect.

    ```azurecli-interactive
    az aks nodepool add \
    --resource-group myResourceGroup \
    --cluster-name myAKSCluster \
    --name gpunp \
    --node-count 1 \
    --node-vm-size Standard_NCC40ads_H100_v5 \
    --node-taints sku=gpu:NoSchedule \
    --gpu-driver none
    ```

1. Install the NVIDIA GPU Operator. The GPU Operator might rely on autodetection of the confidential GPU SKU, but you can enforce signed NVIDIA GPU driver installation by explicitly pinning the `-signed` tag. For example:

    > [!NOTE]
    > NVIDIA publishes a compatible signed driver image with your Ubuntu version, so you should verify this image when installing the GPU Operator.

    ```bash
    helm install gpu-operator nvidia/gpu-operator \
      -n gpu-operator --create-namespace \
      --set driver.enabled=true \
      --set driver.repository=nvcr.io/nvidia \
      --set driver.version=550.90.07-signed-ubuntu22.04 \
      --set toolkit.enabled=true \
      --wait
    ```

    The output should show a `STATUS: deployed` message.

1. Verify that the NVIDIA GPU Operator is running by checking the status of the pods in the `gpu-operator` namespace:

    ```bash
    kubectl get pods -n gpu-operator
    ```

    Example output:

    ```output
    NAME                                                 READY   STATUS      RESTARTS   AGE
    gpu-operator-xxxx                                    1/1     Running     0          5m
    nvidia-driver-daemonset-xxxxx                        2/2     Running     0          4m
    nvidia-container-toolkit-daemonset-xxxxx             1/1     Running     0          3m
    nvidia-device-plugin-daemonset-xxxxx                 1/1     Running     0          2m
    nvidia-dcgm-exporter-xxxxx                           1/1     Running     0          2m
    nvidia-operator-validator-xxxxx                      1/1     Running     0          2m
    gpu-feature-discovery-xxxxx                          1/1     Running     0          2m
    ```

1. Verify that the NVIDIA GPU driver is loaded and the module is signed:

    ```bash
    DRIVER_POD=$(kubectl get pod -n gpu-operator -l app=nvidia-driver-daemonset -o jsonpath='{.items[0].metadata.name}')

    kubectl exec -n gpu-operator -it $DRIVER_POD -c nvidia-driver-ctr -- nvidia-smi
    kubectl exec -n gpu-operator -it $DRIVER_POD -c nvidia-driver-ctr -- modinfo nvidia | grep -i sig
    ```

    In the output, `nvidia-smi` should show the H100 GPU and a driver version of 550.90.07. `modinfo` should show signer fields. For example:

    ```output
    signer:         NVIDIA CERTIFICATE
    sig_key:        <key-id>
    sig_hashalgo:   sha512
    ```

    Missing signer fields indicate that the module isn't signed despite the image tag.

1. Confirm that the GPU is schedulable:

    ```bash
    kubectl get node <node-name> -o jsonpath='{.status.capacity.nvidia\.com/gpu}'
    ```

    The output should show the number of GPUs available on the node. For this example, it should show `1` for a single GPU.

## Clean up resources

To clean up the resources you created for the NVIDIA GPU Operator, delete the namespace:

```bash
kubectl delete namespace gpu-operator
```

You can also delete the node pool that you created for the NVIDIA GPU Operator by using the [`az aks nodepool delete`][az-aks-nodepool-delete] command. For example:

```azurecli-interactive
az aks nodepool delete \
    --resource-group myResourceGroup \
    --cluster-name myAKSCluster \
    --name gpupool
```

## Next steps

To learn more about confidential features on AKS, see the following resources:

- [Use NVIDIA GPU Operator on Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/nvidia-gpu-operator)
- [Use GPUs for compute-intensive workloads on Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu)

[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[az-aks-nodepool-add]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-nodepool-add
[az-aks-nodepool-delete]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-nodepool-delete
[aks-quickstart-cli]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli
[aks-quickstart-portal]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
[aks-quickstart-powershell]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-powershell
[azure-pricing]: https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers
[azure-availability]: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
