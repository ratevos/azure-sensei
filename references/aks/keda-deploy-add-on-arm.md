# Install the Kubernetes Event-driven Autoscaling (KEDA) add-on using an ARM template

> Source: https://learn.microsoft.com/en-us/azure/aks/keda-deploy-add-on-arm  
> Microsoft doc last updated: 09/26/2023


> [!IMPORTANT]
> The KEDA add-on for AKS doesn't currently support modifying the CPU requests or limits and other Helm values for the [Metrics Server](https://keda.sh/docs/2.14/operate/metrics-server/) or [Operator](https://keda.sh/docs/2.14/operate/cluster/). Keep this limitation in mind when using the add-on. If you have any questions, feel free to reach out [here](https://github.com/Azure/AKS/issues).

This article shows you how to deploy the Kubernetes Event-driven Autoscaling (KEDA) add-on to Azure Kubernetes Service (AKS) using an [ARM template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/).

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
- This article assumes you have an existing Azure resource group. If you don't have an existing resource group, you can create one using the [`az group create`][az-group-create] command.
- Ensure you have firewall rules configured to allow access to the Kubernetes API server. For more information, see [Outbound network and FQDN rules for Azure Kubernetes Service (AKS) clusters][aks-firewall-requirements].
- [Create an SSH key pair](#create-an-ssh-key-pair).

> [!NOTE]
> If you're using [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) and you enable KEDA before Workload ID, you need to restart the KEDA operator pods so the proper environment variables can be injected:
>
> 1. Restart the pods by running `kubectl rollout restart deployment keda-operator -n kube-system`.
>
> 1. Obtain KEDA operator pods using `kubectl get pod -n kube-system` and finding pods that begin with `keda-operator`.
>
> 1. Verify successful injection of the environment variables by running `kubectl describe pod <keda-operator-pod> -n kube-system`.
> Under `Environment`, you should see values for `AZURE_TENANT_ID`, `AZURE_FEDERATED_TOKEN_FILE`, and `AZURE_AUTHORITY_HOST`.

## Create an SSH key pair

1. Navigate to the [Azure Cloud Shell](https://shell.azure.com/).
2. Create an SSH key pair using the [`az sshkey create`][az-sshkey-create] command.

    ```azurecli-interactive
    az sshkey create --name <sshkey-name> --resource-group <resource-group-name>
    ```

## Enable the KEDA add-on with an ARM template

1. Deploy the [ARM template for an AKS cluster](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.kubernetes%2Faks%2Fazuredeploy.json).
2. Select **Edit template**.
3. Enable the KEDA add-on by specifying the `workloadAutoScalerProfile` field in the ARM template, as shown in the following example:

    ```json
        "workloadAutoScalerProfile": {
            "keda": {
                "enabled": true
            }
        }
    ```

4. Select **Save**.
5. Update the required values for the ARM template:

    - **Subscription**: Select the Azure subscription to use for the deployment.
    - **Resource group**: Select the resource group to use for the deployment.
    - **Region**: Select the region to use for the deployment.
    - **Dns Prefix**: Enter a unique DNS name to use for the cluster.
    - **Linux Admin Username**: Enter a username for the cluster.
    - **SSH public key source**: Select **Use existing key stored in Azure**.
    - **Store Keys**: Select the key pair you created earlier in the article.

6. Select **Review + create** > **Create**.

## Connect to your AKS cluster

To connect to the Kubernetes cluster from your local device, you use [kubectl][kubectl], the Kubernetes command-line client.

If you use the Azure Cloud Shell, `kubectl` is already installed. You can also install it locally using the [`az aks install-cli`][az-aks-install-cli] command.

- Configure `kubectl` to connect to your Kubernetes cluster, use the [az aks get-credentials][az-aks-get-credentials] command. The following example gets credentials for the AKS cluster named *MyAKSCluster* in the *MyResourceGroup*:

```azurecli
az aks get-credentials --resource-group MyResourceGroup --name MyAKSCluster
```

## Example deployment

The following snippet is a sample deployment that creates a cluster with KEDA enabled with a single node pool comprised of three `DS2_v5` nodes.

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "resources": [
        {
            "apiVersion": "2023-03-01",
            "dependsOn": [],
            "type": "Microsoft.ContainerService/managedClusters",
            "location": "westcentralus",
            "name": "myAKSCluster",
            "properties": {
                "kubernetesVersion": "1.27",
                "enableRBAC": true,
                "dnsPrefix": "myAKSCluster",
                "agentPoolProfiles": [
                    {
                        "name": "agentpool",
                        "osDiskSizeGB": 200,
                        "count": 3,
                        "enableAutoScaling": false,
                        "vmSize": "Standard_D2S_v5",
                        "osType": "Linux",
                        "type": "VirtualMachineScaleSets",
                        "mode": "System",
                        "maxPods": 110,
                        "availabilityZones": [],
                        "nodeTaints": [],
                        "enableNodePublicIP": false
                    }
                ],
                "networkProfile": {
                    "loadBalancerSku": "standard",
                    "networkPlugin": "kubenet"
                },
                "workloadAutoScalerProfile": {
                    "keda": {
                        "enabled": true
                    }
                }
            },
            "identity": {
                "type": "SystemAssigned"
            }
        }
    ]
}
```

## Start scaling apps with KEDA

You can autoscale your apps with KEDA using custom resource definitions (CRDs). For more information, see the [KEDA documentation][keda-scalers].

## Remove resources

- Remove the resource group and all related resources using the [`az group delete`][az-group-delete] command.

    ```azurecli-interactive
    az group delete --name <resource-group-name>
    ```

## Next steps

This article showed you how to install the KEDA add-on on an AKS cluster, and then verify that it's installed and running. With the KEDA add-on installed on your cluster, you can [deploy a sample application][keda-sample] to start scaling apps.

For information on KEDA troubleshooting, see [Troubleshoot the Kubernetes Event-driven Autoscaling (KEDA) add-on][keda-troubleshoot].

To learn more, view the [upstream KEDA docs][keda].

[az-group-delete]: https://learn.microsoft.com/en-us/cli/azure/group#az-group-delete
[keda-troubleshoot]: https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/troubleshoot-kubernetes-event-driven-autoscaling-add-on?context=/azure/aks/context/aks-context
[aks-firewall-requirements]: https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress#azure-global-required-network-rules
[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
[az-feature-register]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-register
[az-feature-show]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-show
[az-sshkey-create]: https://learn.microsoft.com/en-us/cli/azure/ssh#az-sshkey-create
[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[az-aks-install-cli]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-install-cli
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[az-group-create]: https://learn.microsoft.com/en-us/cli/azure/group#az-group-create
[keda-workload-identity]: https://learn.microsoft.com/en-us/azure/aks/keda-workload-identity

[kubectl]: https://kubernetes.io/docs/reference/kubectl/
[keda-scalers]: https://keda.sh/docs/scalers/
[keda-sample]: https://github.com/kedacore/sample-dotnet-worker-servicebus-queue
[keda]: https://keda.sh/docs/2.12/
[keda-support-policy]: https://github.com/kedacore/governance/blob/main/DEPRECATIONS.md
