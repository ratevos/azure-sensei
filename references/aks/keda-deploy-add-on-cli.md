# Install the Kubernetes Event-driven Autoscaling (KEDA) add-on using the Azure CLI

> Source: https://learn.microsoft.com/en-us/azure/aks/keda-deploy-add-on-cli  
> Microsoft doc last updated: 09/26/2023


> [!IMPORTANT]
> The KEDA add-on for AKS doesn't currently support modifying the CPU requests or limits and other Helm values for the [Metrics Server](https://keda.sh/docs/2.14/operate/metrics-server/) or [Operator](https://keda.sh/docs/2.14/operate/cluster/). Keep this limitation in mind when using the add-on. If you have any questions, feel free to reach out [here](https://github.com/Azure/AKS/issues).

This article shows you how to install the Kubernetes Event-driven Autoscaling (KEDA) add-on to Azure Kubernetes Service (AKS) using the Azure CLI.

> [!IMPORTANT]
> Your cluster Kubernetes version determines what KEDA version will be installed on your AKS cluster. To see which KEDA version maps to each AKS version, see the **AKS managed add-ons** column of the [Kubernetes component version table](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions#aks-components-breaking-changes-by-version). 
>
> For GA Kubernetes versions, AKS offers full support of the corresponding KEDA minor version in the table. Kubernetes preview versions and the latest KEDA patch are partially covered by customer support on a best-effort basis. As such, these features aren't meant for production use. For more information, see the following support articles:
> - [AKS support policies](https://learn.microsoft.com/en-us/azure/aks/support-policies)
> - [Azure support FAQ](https://azure.microsoft.com/support/legal/faq/)

> [!NOTE]
> KEDA version 2.15+ introduces a breaking change that [removes pod identity support](https://github.com/kedacore/keda/issues/5035). We recommend moving over to workload identity for your authentication if you're using pod identity. While the KEDA managed add-on doesn't currently run KEDA version 2.15+, it will begin running it in the AKS preview version 1.31.
>
> For more information on how to securely scale your applications with workload identity, please read our [tutorial][keda-workload-identity]. To view KEDA's breaking change/deprecation policy, please read their [official documentation][keda-support-policy].

## Before you begin

- You need an Azure subscription. If you don't have an Azure subscription, you can create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You need the [Azure CLI installed](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
- Ensure you have firewall rules configured to allow access to the Kubernetes API server. For more information, see [Outbound network and FQDN rules for Azure Kubernetes Service (AKS) clusters][aks-firewall-requirements].

> [!NOTE]
> If you're using [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) and you enable KEDA before Workload ID, you need to restart the KEDA operator pods so the proper environment variables can be injected:
>
> 1. Restart the pods by running `kubectl rollout restart deployment keda-operator -n kube-system`.
>
> 1. Obtain KEDA operator pods using `kubectl get pod -n kube-system` and finding pods that begin with `keda-operator`.
>
> 1. Verify successful injection of the environment variables by running `kubectl describe pod <keda-operator-pod> -n kube-system`.
> Under `Environment`, you should see values for `AZURE_TENANT_ID`, `AZURE_FEDERATED_TOKEN_FILE`, and `AZURE_AUTHORITY_HOST`.

## Install the KEDA add-on with Azure CLI

To install the KEDA add-on, use `--enable-keda` when creating or updating a cluster.

## Enable the KEDA add-on on your AKS cluster

> [!NOTE]
> While KEDA provides various customization options, the KEDA add-on currently provides basic common configuration.
>
> If you require custom configurations, you can manually edit the KEDA YAML files to customize the installation. **Azure doesn't offer support for custom configurations**.

### Create a new AKS cluster with KEDA add-on enabled

1. Create a resource group using the [`az group create`][az-group-create] command.

    ```azurecli-interactive
    az group create --name myResourceGroup --location eastus
    ```

2. Create a new AKS cluster using the [`az aks create`][az-aks-create] command and enable the KEDA add-on using the `--enable-keda` flag.

    ```azurecli-interactive
    az aks create \
        --resource-group myResourceGroup \
        --name myAKSCluster \
        --enable-keda \
        --generate-ssh-keys
    ```

### Enable the KEDA add-on on an existing AKS cluster

- Update an existing cluster using the [`az aks update`][az-aks-update] command and enable the KEDA add-on using the `--enable-keda` flag.

    ```azurecli-interactive
    az aks update \
        --resource-group myResourceGroup \
        --name myAKSCluster \
        --enable-keda 
    ```

## Get the credentials for your cluster

- Get the credentials for your AKS cluster using the [`az aks get-credentials`][az-aks-get-credentials] command.

    ```azurecli-interactive
    az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
    ```

## Verify the KEDA add-on is installed on your cluster

- Verify the KEDA add-on is installed on your cluster using the [`az aks show`][az-aks-show] command and set the `--query` parameter to `workloadAutoScalerProfile.keda.enabled`.

    ```azurecli-interactive
    az aks show --resource-group myResourceGroup --name myAKSCluster --query "workloadAutoScalerProfile.keda.enabled" 
    ```

    The following example output shows the KEDA add-on is installed on the cluster:

    ```output
    true
    ```

## Verify KEDA is running on your cluster

- Verify the KEDA add-on is running on your cluster using the `kubectl get pods` command.

    ```azurecli-interactive
    kubectl get pods -n kube-system 
    ```

    The following example output shows the KEDA operator, admissions hook, and metrics API server are installed on the cluster:

    ```output
    keda-admission-webhooks-**********-2n9zl           1/1     Running   0            3d18h
    keda-admission-webhooks-**********-69dkg           1/1     Running   0            3d18h
    keda-operator-*********-4hb5n                      1/1     Running   0            3d18h
    keda-operator-*********-pckpx                      1/1     Running   0            3d18h
    keda-operator-metrics-apiserver-**********-gqg4s   1/1     Running   0            3d18h
    keda-operator-metrics-apiserver-**********-trfcb   1/1     Running   0            3d18h
    ```

## Verify the KEDA version on your cluster

To verify the version of your KEDA, use `kubectl get crd/scaledobjects.keda.sh -o yaml `. For example:

```azurecli-interactive
kubectl get crd/scaledobjects.keda.sh -o yaml 
```

The following example output shows the configuration of KEDA in the `app.kubernetes.io/version` label:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.9.0
    meta.helm.sh/release-name: aks-managed-keda
    meta.helm.sh/release-namespace: kube-system
  creationTimestamp: "2023-08-09T15:58:56Z"
  generation: 1
  labels:
    app.kubernetes.io/component: operator
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: keda-operator
    app.kubernetes.io/part-of: keda-operator
    app.kubernetes.io/version: 2.10.1
    helm.toolkit.fluxcd.io/name: keda-adapter-helmrelease
    helm.toolkit.fluxcd.io/namespace: 64d3b6fd3365790001260647
  name: scaledobjects.keda.sh
  resourceVersion: "1421"
  uid: 29109c8c-638a-4bf5-ac1b-c28ad9aa11fa
spec:
  conversion:
    strategy: None
  group: keda.sh
  names:
    kind: ScaledObject
    listKind: ScaledObjectList
    plural: scaledobjects
    shortNames:
    - so
    singular: scaledobject
  scope: Namespaced
  # Redacted due to length
```

## Vertically scale the keda-operator if you are experiencing OOMKill Errors

If the keda-operator pods are experiencing OOMKill errors, you can use the [Vertical Pod Autoscaler (VPA)][vpa] to automatically adjust CPU and memory limits.

1. Enable VPA on your AKS cluster using the [`az aks update`][az-aks-update] command.

    ```azurecli-interactive
    az aks update \
        --resource-group myResourceGroup \
        --name myAKSCluster \
        --enable-vpa
    ```

1. Create a file named `keda-operator-vpa.yaml` with the following VPA configuration to target the keda-operator deployment.

    ```yaml
    apiVersion: autoscaling.k8s.io/v1
    kind: VerticalPodAutoscaler
    metadata:
      name: keda-operator-vpa
    spec:
      targetRef:
        apiVersion: "apps/v1"
        kind: Deployment
        name: keda-operator
      updatePolicy:
        updateMode: "InPlaceOrRecreate"
    ```

1. Apply the VPA configuration to your cluster using the `kubectl apply` command.

    ```azurecli-interactive
    kubectl apply -f keda-operator-vpa.yaml
    ```

    The VPA automatically adjusts the CPU and memory requests and limits for the keda-operator pods based on observed usage.

## Disable the KEDA add-on on your AKS cluster

- Disable the KEDA add-on on your cluster using the [`az aks update`][az-aks-update] command with the `--disable-keda` flag.

    ```azurecli-interactive
    az aks update \
      --resource-group myResourceGroup \
      --name myAKSCluster \
      --disable-keda 
    ```

## Next steps

This article showed you how to install the KEDA add-on on an AKS cluster using the Azure CLI.

With the KEDA add-on installed on your cluster, you can [deploy a sample application][keda-sample] to start scaling apps.

For information on KEDA troubleshooting, see [Troubleshoot the Kubernetes Event-driven Autoscaling (KEDA) add-on][keda-troubleshoot].

To learn more, view the [upstream KEDA docs][keda].

[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
[az-feature-register]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-register
[az-feature-show]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-show
[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[keda-troubleshoot]: https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/troubleshoot-kubernetes-event-driven-autoscaling-add-on?context=/azure/aks/context/aks-context
[aks-firewall-requirements]: https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress#azure-global-required-network-rules
[az-aks-update]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-update
[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[az-aks-show]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-show
[az-group-create]: https://learn.microsoft.com/en-us/cli/azure/group#az-group-create
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[keda-workload-identity]: https://learn.microsoft.com/en-us/azure/aks/keda-workload-identity
[vpa]: https://learn.microsoft.com/en-us/azure/aks/vertical-pod-autoscaler

[kubectl]: https://kubernetes.io/docs/user-guide/kubectl
[keda-sample]: https://github.com/kedacore/sample-dotnet-worker-servicebus-queue
[keda]: https://keda.sh/docs/2.12/
[keda-support-policy]: https://github.com/kedacore/governance/blob/main/DEPRECATIONS.md
