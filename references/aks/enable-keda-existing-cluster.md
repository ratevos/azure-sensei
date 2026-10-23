# Enable the Kubernetes Event-driven Autoscaling (KEDA) add-on on an existing AKS cluster

> Source: https://learn.microsoft.com/en-us/azure/aks/enable-keda-existing-cluster  
> Microsoft doc last updated: 09/19/2024


> [!IMPORTANT]
> The KEDA add-on for AKS doesn't currently support modifying the CPU requests or limits and other Helm values for the [Metrics Server](https://keda.sh/docs/2.14/operate/metrics-server/) or [Operator](https://keda.sh/docs/2.14/operate/cluster/). Keep this limitation in mind when using the add-on. If you have any questions, feel free to reach out [here](https://github.com/Azure/AKS/issues).

This article shows you how to enable the Kubernetes Event-driven Autoscaling (KEDA) add-on on an existing Azure Kubernetes Service (AKS) cluster using the Azure portal.

> [!IMPORTANT]
> Your cluster Kubernetes version determines what KEDA version will be installed on your AKS cluster. To see which KEDA version maps to each AKS version, see the **AKS managed add-ons** column of the [Kubernetes component version table](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions#aks-components-breaking-changes-by-version). 
>
> For GA Kubernetes versions, AKS offers full support of the corresponding KEDA minor version in the table. Kubernetes preview versions and the latest KEDA patch are partially covered by customer support on a best-effort basis. As such, these features aren't meant for production use. For more information, see the following support articles:
> - [AKS support policies](https://learn.microsoft.com/en-us/azure/aks/support-policies)
> - [Azure support FAQ](https://azure.microsoft.com/support/legal/faq/)

> [!NOTE]
> KEDA version 2.15+ introduces a breaking change that [removes pod identity support](https://github.com/kedacore/keda/issues/5035). We recommend moving over to workload identity for your authentication if you're using pod identity. While the KEDA managed add-on doesn't currently run KEDA version 2.15, it will begin running it in the AKS preview version 1.31.
>
> For more information on how to securely scale your applications with workload identity, please read our [tutorial][keda-workload-identity]. To view KEDA's breaking change/deprecation policy, please read their [official documentation][keda-support-policy].

## Before you begin

- An Azure subscription. If you don't have an Azure subscription, you can create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An existing AKS cluster. If you don't have an AKS cluster, create one using the steps in [Deploy an Azure Kubernetes Service (AKS) cluster](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal).
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

## Enable the KEDA add-on on an existing AKS cluster

1. Sign in to the [Azure portal](https://portal.azure.com/) and navigate to your AKS cluster resource.
1. From the service menu, under **Settings**, select **Application scaling** > **Enable KEDA add-on**.

    It may take a few minutes for the changes to take effect.

1. Once the KEDA add-on is enabled, you can [verify KEDA is running on your cluster](#verify-keda-is-running-on-your-cluster).

## Verify KEDA is running on your cluster

1. From the service menu of your AKS cluster resource, under **Kubernetes resources**, select **Workloads**.
1. Select the **Pods** tab, and look for the `keda` pods. If they're listed, KEDA is successfully running on your cluster.

    

1. Once you verify that KEDA is running, you can [check the KEDA version on your cluster](#check-the-keda-version-on-your-cluster).

## Check the KEDA version on your cluster

1. From the service menu of your AKS cluster resource, under **Kubernetes resources**, select **Custom resources**.
1. Find the **keda.sh** resource. From there, you can view the KEDA version running on your cluster.

    

## Disable the KEDA add-on on an existing cluster

To disable the KEDA add-on, see [Disable the KEDA add-on on your AKS cluster](https://learn.microsoft.com/en-us/azure/aks/keda-deploy-add-on-cli#disable-the-keda-add-on-on-your-aks-cluster).

## Next steps

In this article, you learned how to enable the KEDA add-on on an existing AKS cluster using the Azure portal. With the KEDA add-on installed on your cluster, you can [deploy a sample application][keda-sample] to start scaling apps.

For information on KEDA troubleshooting, see [Troubleshoot the Kubernetes Event-driven Autoscaling (KEDA) add-on][keda-troubleshoot]. For more information on KEDA, see the [upstream KEDA docs][keda].

[keda-troubleshoot]: https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/troubleshoot-kubernetes-event-driven-autoscaling-add-on?context=/azure/aks/context/aks-context
[aks-firewall-requirements]: https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress#azure-global-required-network-rules
[keda-workload-identity]: https://learn.microsoft.com/en-us/azure/aks/keda-workload-identity

[keda-sample]: https://github.com/kedacore/sample-dotnet-worker-servicebus-queue
[keda]: https://keda.sh/docs/2.12/
[keda-support-policy]: https://github.com/kedacore/governance/blob/main/DEPRECATIONS.md
