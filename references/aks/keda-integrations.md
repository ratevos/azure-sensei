# Integrations with Kubernetes Event-driven Autoscaling (KEDA) on Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/keda-integrations  
> Microsoft doc last updated: 09/27/2023


The Kubernetes Event-driven Autoscaling (KEDA) add-on for AKS integrates with features provided by Azure and open-source projects.

> [!IMPORTANT]
> The [AKS support policy][aks-support-policy] doesn't cover integrations with open-source projects.

## Observe your autoscaling with Kubernetes events

KEDA automatically emits Kubernetes events allowing customers to operate their application autoscaling.

To learn about the available metrics, we recommend reading the [KEDA documentation][keda-event-docs].

## Scalers for Azure services

KEDA can integrate with various tools and services through [a rich catalog of Azure KEDA scalers][keda-scalers] and supports leading cloud platforms and open-source technologies.

KEDA leverages the following scalers for Azure services:

- [Azure Application Insights](https://keda.sh/docs/latest/scalers/azure-app-insights/)
- [Azure Blob Storage](https://keda.sh/docs/latest/scalers/azure-storage-blob/)
- [Azure Data Explorer](https://keda.sh/docs/latest/scalers/azure-data-explorer/)
- [Azure Event Hubs](https://keda.sh/docs/latest/scalers/azure-event-hub/)
- [Azure Log Analytics](https://keda.sh/docs/latest/scalers/azure-log-analytics/)
- [Azure Monitor](https://keda.sh/docs/latest/scalers/azure-monitor/)
- [Azure Pipelines](https://keda.sh/docs/latest/scalers/azure-pipelines/)
- [Azure Service Bus](https://keda.sh/docs/latest/scalers/azure-service-bus/)
- [Azure Storage Queue](https://keda.sh/docs/latest/scalers/azure-storage-queue/)

As of KEDA version `2.10`, the [Prometheus scaler][prometheus-scaler] supports Azure managed service for Prometheus. You can also use self-hosted Prometheus but this falls outside support scope.

You can also install external scalers to autoscale on other Azure services:
- [Azure Cosmos DB (Change feed)](https://github.com/kedacore/external-scaler-azure-cosmos-db)

> [!IMPORTANT]
> External scalers *aren't supported as part of the add-on* and rely on community support.

> [!IMPORTANT]
>
> Open-source software is mentioned throughout AKS documentation and samples. Software that you deploy is excluded from AKS service-level agreements, limited warranty, and Azure support. As you use open-source technology alongside AKS, consult the support options available from the respective communities and project maintainers to develop a plan.
>
> Microsoft takes responsibility for building the open-source packages that we deploy on AKS. That responsibility includes having complete ownership of the build, scan, sign, validate, and hotfix process, along with control over the binaries in container images. For more information, see [Vulnerability management for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-vulnerability-management#aks-container-images) and [AKS support coverage](https://learn.microsoft.com/en-us/azure/aks/support-policies#aks-support-coverage).

## Next steps

* [Enable the KEDA add-on with an ARM template][keda-arm]
* [Enable the KEDA add-on with the Azure CLI][keda-cli]
* [Troubleshoot KEDA add-on problems][keda-troubleshoot]
* [Autoscale a .NET Core worker processing Azure Service Bus Queue message][keda-sample]
* [View the upstream KEDA docs][keda]

[aks-support-policy]: https://learn.microsoft.com/en-us/azure/aks/support-policies
[keda-cli]: https://learn.microsoft.com/en-us/azure/aks/keda-deploy-add-on-cli
[keda-arm]: https://learn.microsoft.com/en-us/azure/aks/keda-deploy-add-on-arm
[keda-troubleshoot]: https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/troubleshoot-kubernetes-event-driven-autoscaling-add-on?context=/azure/aks/context/aks-context

[keda-scalers]: https://keda.sh/docs/latest/scalers/
[keda-event-docs]: https://keda.sh/docs/latest/reference/events/
[keda-sample]: https://github.com/kedacore/sample-dotnet-worker-servicebus-queue
[prometheus-scaler]: https://keda.sh/docs/2.11/scalers/prometheus/
[keda]: https://keda.sh/docs/2.12/
