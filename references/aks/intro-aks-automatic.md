# Introduction to Azure Kubernetes Service (AKS) Automatic

> Source: https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic  
> Microsoft doc last updated: 07/07/2026


**Applies to**: :heavy_check_mark: AKS Automatic

Azure Kubernetes Service (AKS) Automatic offers an experience that makes the most common tasks on Kubernetes fast and frictionless, while preserving the flexibility, extensibility, and consistency of Kubernetes. Azure takes care of your cluster setup, including node management, scaling, security, and preconfigured settings that follow AKS well-architected recommendations. Automatic clusters dynamically allocate compute resources based on your specific workload requirements and are tuned for running production applications.

- **Production ready by default**: Clusters are preconfigured for optimal production use, suitable for most applications. They offer fully managed node pools that automatically allocate and scale resources based on your workload needs. Pods are bin packed efficiently, to maximize resource utilization.
- **Guaranteed pod readiness**: AKS Automatic includes a [pod readiness SLA][azure-sla] that guarantees 99.9% of qualifying pod readiness operations complete within five minutes. This means your workloads start running promptly during scaling events and node provisioning, giving you confidence in your application's responsiveness without manual tuning.
- **Built-in best practices and safeguards**: AKS Automatic clusters have a hardened default configuration, with many cluster, application, and networking security settings enabled by default. AKS automatically patches your nodes and cluster components while adhering to any planned maintenance schedules.
- **Code to Kubernetes in minutes**: Go from a container image to a deployed application that adheres to best practices patterns within minutes, with access to the comprehensive capabilities of the Kubernetes API and its rich ecosystem.

> [!IMPORTANT]
> Starting on **November 30, 2025**, Azure Kubernetes Service (AKS) no longer supports or provides security updates for Azure Linux 2.0. The Azure Linux 2.0 node image is frozen at the `202512.06.0` release. Beginning on **October 31, 2026**, node images will be removed, and you'll be unable to scale your node pools. Migrate to a supported Azure Linux version by [upgrading your node pools](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster) to a supported Kubernetes version or migrating to [osSku AzureLinux3](https://learn.microsoft.com/en-us/azure/aks/upgrade-os-version). For more information, see the [Retirement GitHub issue](https://github.com/Azure/AKS/issues/4988) and the [Azure Updates retirement announcement](https://azure.microsoft.com/updates?id=500645). To stay informed on announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

## Service level agreement

The service level agreement (SLA) for AKS Automatic clusters includes the following components:

- Pod readiness
- Uptime

For more information, see [Service Level Agreements (SLA) for Online Services][azure-sla].

### Pod readiness SLA

AKS Automatic includes a [pod readiness SLA][azure-sla], a financially backed guarantee that 99.9% of qualifying pod readiness operations complete within 5 minutes. This SLA covers pod scheduling and node provisioning when needed.

The pod readiness SLA benefits workloads that depend on predictable scaling behavior, such as:

- **Web and API workloads** that need to scale out quickly during traffic spikes without degrading response times.
- **Event-driven processing** where new consumer pods must be ready promptly to avoid message backlog.
- **CI/CD and batch jobs** that require consistent pod startup times for reliable pipeline execution.

This guarantee is exclusive to AKS Automatic and is backed by the [Microsoft Online Services SLA][azure-sla]. You don't need to configure anything to enable it and it comes included with every AKS Automatic cluster.

### Uptime SLA

AKS Automatic includes [uptime SLA][azure-sla], a financially backed guarantee for 99.95% availability of the Kubernetes API server. You don't need to configure anything to enable it and it comes included with every AKS Automatic cluster.

## AKS Automatic and Standard feature comparison

The following table provides a comparison of options that are available, preconfigured, and default in both AKS Automatic and AKS Standard. For more information on whether specific features are available in Automatic, you can check the documentation for that feature.

**Preconfigured** features are always enabled and you can't disable or change their settings. **Default** features are configured for you but can be changed. **Optional** features are available for you to configure and aren't enabled by default.

When enabling optional features, you can follow the linked feature documentation. When you reach a step for cluster creation, follow steps to create an [AKS Automatic cluster][quickstart-aks-automatic] instead of creating an AKS Standard cluster.

### Application deployment, monitoring, and observability

Application deployment can be streamlined using [automated deployments][automated-deployments] from source control, which creates Kubernetes manifest and generates CI/CD workflows. Additionally, the cluster is configured with monitoring tools such as Managed Prometheus for metrics, Managed Grafana for visualization, and Container Insights for log collection.

| Option | AKS Automatic | AKS Standard |
|--------|---------------|--------------|
| Application deployment | **Optional**: <br> • Use [automated deployments][automated-deployments] to containerize applications from source control, create Kubernetes manifests, and continuous integration/continuous deployment (CI/CD) workflows. <br> • Create deployment pipelines using [GitHub Actions for Kubernetes][kubernetes-action]. <br> • Bring your own CI/CD pipeline. | **Optional**: <br> • Use [automated deployments][automated-deployments] to containerize applications from source control, create Kubernetes manifests, and continuous integration/continuous deployment (CI/CD) workflows. <br> • Create deployment pipelines using [GitHub Actions for Kubernetes][kubernetes-action]. <br> • Bring your own CI/CD pipeline. |
| Monitoring, logging, and visualization | **Default**: <br> • [Managed Prometheus][managed-prometheus] for metric collection when using Azure CLI or the Azure portal. <br> • [Container insights][container-insights] for log collection when using Azure CLI or the Azure portal. <br> • [Azure Monitor Dashboards with Grafana](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/visualize-use-grafana-dashboards) for visualization is built in when using the Azure portal. <br> **Optional**: <br> • [Managed Grafana][managed-grafana] for visualization when using Azure CLI or the Azure portal. | **Default**: [Azure Monitor Dashboards with Grafana](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/visualize-use-grafana-dashboards) for visualization is built in when using the Azure portal. <br> **Optional**: <br> • [Managed Prometheus][managed-prometheus] for metric collection. <br> • [Managed Grafana][managed-grafana] for visualization. <br> • [Container insights][container-insights] for log collection. <br> • [Advanced Container Networking Services](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview) container network observability for pod metrics, DNS, L4 metrics, and network flow logs. |

### Node management, scaling, and cluster operations

Node management is automatically handled without the need for manual user node pool creation, [system node pools and components are managed][managed-system-node-pool] by AKS. Scaling is seamless, with nodes created based on workload requests. Additionally, features for workload scaling like Horizontal Pod Autoscaler (HPA), [Kubernetes Event Driven Autoscaling (KEDA)][keda], and [Vertical Pod Autoscaler (VPA)][vpa] are enabled. The [pod readiness SLA][azure-sla] that guarantees 99.9% of pod readiness operations complete within 5 minutes. Clusters are configured for automatic node repair, automatic cluster upgrades, and detection of deprecated Kubernetes standard API usage. You can also set a planned maintenance schedule for upgrades if needed.

| Option | AKS Automatic | AKS Standard |
|--------|---------------|--------------|
| System node pools | **Preconfigured**: [AKS Automatic with managed system node pools][managed-system-node-pool] creates, scales, upgrades the system nodes and system components on your behalf and hosts them in the AKS subscriptions. | **Default**: You create and manage system node pools. |
| Node autoprovisioning | **Preconfigured**: AKS Automatic manages the node pools using [node autoprovisioning][node-autoprovisioning]. | **Optional**: AKS Standard manages user node pools using [node autoprovisioning][node-autoprovisioning]. |
| Scaling | **Preconfigured**: AKS Automatic creates nodes based on workload requests using [Node Autoprovisioning][node-autoprovisioning]. <br> [Horizontal Pod Autoscaler (HPA)][aks-hpa], [Kubernetes Event Driven Autoscaling (KEDA)][keda], and [Vertical Pod Autoscaler (VPA)][vpa] are enabled on the cluster. | **Default:** Manual scaling of node pools. <br> **Optional**: <br> • [Cluster autoscaler][cluster-autoscaler] <br> • [Node Autoprovisioning][node-autoprovisioning] <br> • [Kubernetes Event Driven Autoscaling (KEDA)][keda] <br> • [Vertical Pod Autoscaler (VPA)][vpa] |
| Cluster tier and Service Level Agreement (SLA) | **Preconfigured**: Standard tier cluster with up to 5,000 nodes, a [cluster uptime SLA][uptime-sla], and a [pod readiness SLA][azure-sla] that guarantees 99.9% of qualifying pod readiness operations complete within 5 minutes. |  **Default**: Free tier cluster with 10 nodes but can support up to 1,000 nodes. <br/> **Optional**: <br> • Standard tier cluster with up to 5,000 nodes and a [cluster uptime SLA][uptime-sla]. <br> • Premium tier cluster with up to 5,000 nodes, [cluster uptime SLA][uptime-sla], and [long term support][long-term-support]. |
| Node operating system | **Preconfigured for system node pool**: [Azure Linux][azure-linux] <br> **Optional for user nodes**: <br> • [Azure Linux][azure-linux] <br> • Ubuntu | **Default**: Ubuntu <br> **Optional**: <br> • [Azure Linux][azure-linux] <br> • [Windows Server][windows-server] |
| Node resource group | **Preconfigured**: [Fully managed node resource group][nrg-lockdown] to prevent accidental or intentional changes to cluster resources. | **Default**: Unrestricted <br/> **Optional**: [Read only][nrg-lockdown]  with node resource group lockdown |
| Node auto-repair | **Preconfigured**: Continuously monitors the health state of worker nodes and performs [automatic node repair][node-auto-repair] if they become unhealthy. |  **Preconfigured**: Continuously monitors the health state of worker nodes and performs [automatic node repair][node-auto-repair] if they become unhealthy.  |
| Cluster upgrades | **Preconfigured**: Clusters are [automatically upgraded using the stable channel][cluster-upgrade-channels] to minor version N-1, where N is the latest supported minor version. |  **Default**: Manual upgrade. <br> **Optional**: Automatic upgrade using a selectable [upgrade channel][cluster-upgrade-channels].  |
| Node OS image upgrades | **Preconfigured**: Clusters are [automatically upgraded using the NodeImage channel][nodeos-updates] with security fixes and bug fixes. | **Default**: Manual upgrade. <br> **Optional**: Automatic upgrade using a selectable [node OS upgrade channel][nodeos-updates]|
| Kubernetes API breaking change detection | **Preconfigured**: Cluster upgrades are stopped on detection of [deprecated Kubernetes standard API usage][stop-cluster-upgrade-api-breaking-changes]. |  **Preconfigured**: Cluster upgrades are stopped on detection of [deprecated Kubernetes standard API usage][stop-cluster-upgrade-api-breaking-changes].  |
| Planned maintenance windows | **Default**: Set [planned maintenance schedule][planned-maintenance] configuration to control upgrades. |  **Optional**: Set [planned maintenance schedule][planned-maintenance] configuration to control upgrades.  |

### Security and policies

Cluster authentication and authorization use [Azure Role-based Access Control (RBAC) for Kubernetes authorization][azure-rbac-for-k8s-auth] and applications can use features like [workload identity with Microsoft Entra Workload ID][workload-identity] and [OpenID Connect (OIDC) cluster issuer][oidc-issuer] to have secure communication with Azure services. [Deployment safeguards][deployment-safeguards] enforce Kubernetes best practices through Azure Policy controls and the built-in [image cleaner][image-cleaner] removes unused images with vulnerabilities, enhancing image security.

| Option | AKS Automatic | AKS Standard |
|--------|---------------|--------------|
| Cluster authentication and authorization | **Preconfigured**: [Azure RBAC for Kubernetes authorization][azure-rbac-for-k8s-auth] for managing cluster authentication and authorization by using Azure role-based access control.  | **Default**: Local accounts. <br/> **Optional**: <br> • [Azure RBAC for Kubernetes authorization][azure-rbac-for-k8s-auth] <br> • [Kubernetes RBAC with Microsoft Entra integration][k8s-rbac-with-entra] |
| Cluster security | **Preconfigured**: [API server virtual network integration][api-server-vnet-integration] enables network communication between the API server and the cluster nodes over a private network without requiring a private link or tunnel. | **Optional**: [API server virtual network integration][api-server-vnet-integration] enables network communication between the API server and the cluster nodes over a private network without requiring a private link or tunnel.|
| Application security | **Preconfigured**: <br> • [Workload identity with Microsoft Entra Workload ID][workload-identity] <br> • [OpenID Connect (OIDC) cluster issuer][oidc-issuer] <br/> **Optional**:<br> • [Advanced Container Networking Services](https://learn.microsoft.com/en-us/azure/aks/container-network-security-wireguard-encryption-concepts) container network security for pod traffic with Wireguard node encryption.| **Optional**: <br> • [Workload identity with Microsoft Entra Workload ID][workload-identity] <br> • [OpenID Connect (OIDC) cluster issuer][oidc-issuer] <br/> **Optional**:<br> • [Advanced Container Networking Services ](https://learn.microsoft.com/en-us/azure/aks/container-network-security-wireguard-encryption-concepts) container network security for pod traffic with Wireguard node encryption.|
| Image security | **Preconfigured**: [Image cleaner][image-cleaner] to remove unused images with vulnerabilities. | **Optional**: [Image cleaner][image-cleaner] to remove unused images with vulnerabilities. |
| Policy enforcement | **Preconfigured**: [Deployment safeguards][deployment-safeguards] and [baseline Pod Security Standards][pod-security-standards] that enforce Kubernetes best practices in your AKS cluster through Azure Policy controls in enforce mode. <br/> • [Security restrictions for managed system node pools][security-restrictions] protect managed system components and preserve the boundary between customer workloads and AKS-managed infrastructure. <br/> **Optional**:<br> • [Advanced Container Networking Services](https://learn.microsoft.com/en-us/azure/aks/how-to-apply-l7-policies) container network security for Cilium DNS and L7 policies. | **Optional**: [Deployment safeguards][deployment-safeguards] and [Pod Security Standards][pod-security-standards] enforce Kubernetes best practices in your AKS cluster through Azure Policy controls in enforce mode or warning mode. <br/> **Optional**:<br> • [Advanced Container Networking Services ](https://learn.microsoft.com/en-us/azure/aks/how-to-apply-l7-policies) container network security for Cilium DNS and L7 policies. |
| Managed namespaces | **Optional**: Use [Managed namespaces](https://learn.microsoft.com/en-us/azure/aks/managed-namespaces) to create preconfigured namespaces where you can define network policies for ingress/egress, resource quotas for memory/CPU, and set-up labels/annotations. | **Optional**: Use [Managed namespaces](https://learn.microsoft.com/en-us/azure/aks/managed-namespaces) to create preconfigured namespaces where you can define network policies for ingress/egress, resource quotas for memory/CPU, and set-up labels/annotations. |

### Networking

AKS Automatic clusters use [managed Virtual Network powered by Azure CNI Overlay with Cilium][azure-cni-powered-by-cilium] for high-performance networking and robust security. Ingress is handled by [managed NGINX using the application routing add-on][app-routing], integrating seamlessly with Azure DNS and Azure Key Vault. Egress uses a [managed NAT gateway][managed-nat-gateway] for scalable outbound connections.

| Option | AKS Automatic | AKS Standard |
|--------|---------------|--------------|
| Virtual network | **Default**: [Managed Virtual Network using Azure CNI Overlay powered by Cilium][azure-cni-powered-by-cilium] combines the robust control plane of Azure CNI with the data plane of Cilium to provide high-performance networking and security. <br/> **Optional**: <br> • [Custom virtual network][automatic-custom-network] <br> • [Custom virtual network][automatic-private-custom-network] with private cluster. | **Default**: [Managed Virtual Network with kubenet][kubenet] <br/> **Optional**: <br> • [Azure CNI][azure-cni] <br> • [Azure CNI Overlay][azure-cni-overlay] <br> • [Azure CNI Overlay powered by Cilium][azure-cni-powered-by-cilium] <br> • [Bring your own CNI][use-byo-cni] |
| Ingress | **Default**: <br> • Starting on AKS 1.36, [Kubernetes Gateway API via the application routing add-on][app-routing-gateway-api] for new clusters. <br> • Older version before AKS 1.36, [Managed NGINX using the application routing add-on][app-routing] with integrations for Azure DNS and Azure Key Vault. <br/> **Optional**: <br> • [Istio-based service mesh add-on for AKS][istio-deploy-ingress] ingress gateway with [Istio CNI][istio-cni] enabled. The add-on isn't auto-upgraded with the cluster, so you must [upgrade it][istio-upgrade] to keep it compatible and avoid blocking cluster auto-upgrade. | **Optional**: <br> • [Kubernetes Gateway API via the application routing add-on][app-routing-gateway-api] <br> • [Istio-based service mesh add-on for AKS][istio-deploy-ingress] ingress gateway <br> • Bring your own ingress or gateway. |
| Egress | **Preconfigured**: [AKS managed NAT gateway][managed-nat-gateway] for a scalable outbound connection flows when used with managed virtual network <br> **Optional (with custom virtual network)**: <br> • [Azure Load Balancer][egress-load-balancer] <br> • [User-assigned NAT gateway][managed-nat-gateway] <br> • [User-defined routing (UDR)][udr] | **Default**: [Azure Load Balancer][egress-load-balancer] <br> **Optional**: <br> • [User-assigned NAT gateway][managed-nat-gateway] <br> • [AKS managed NAT gateway][userassigned-nat-gateway] <br> • [User-defined routing (UDR)][udr] |
| [LocalDNS](https://learn.microsoft.com/en-us/azure/aks/dns-concepts#localdns-in-azure-kubernetes-service) | **Preconfigured** for AKS Automatic. | **Optional** for AKS Standard. |

## Next steps

To learn more about AKS Automatic, follow the quickstart to create a cluster.

> [Create an Azure Kubernetes Service (AKS) Automatic cluster][quickstart-aks-automatic]

[aks-hpa]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-scale#autoscale-pods
[node-autoprovisioning]: https://learn.microsoft.com/en-us/azure/aks/node-autoprovision
[cluster-autoscaler]: https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler-overview
[vpa]: https://learn.microsoft.com/en-us/azure/aks/vertical-pod-autoscaler
[keda]: https://learn.microsoft.com/en-us/azure/aks/keda-about
[azure-linux]: https://learn.microsoft.com/en-us/azure/aks/use-azure-linux
[windows-server]: https://learn.microsoft.com/en-us/azure/aks/windows-vs-linux-containers
[nrg-lockdown]: https://learn.microsoft.com/en-us/azure/aks/node-resource-group-lockdown
[node-auto-repair]: https://learn.microsoft.com/en-us/azure/aks/node-auto-repair
[cluster-upgrades]: https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-cluster
[cluster-upgrade-channels]: https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-cluster#cluster-autoupgrade-channels
[nodeos-updates]: https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-node-os-image#available-node-os-upgrade-channels
[stop-cluster-upgrade-api-breaking-changes]: https://learn.microsoft.com/en-us/azure/aks/stop-cluster-upgrade-api-breaking-changes
[planned-maintenance]: https://learn.microsoft.com/en-us/azure/aks/planned-maintenance
[azure-rbac-for-k8s-auth]: https://learn.microsoft.com/en-us/azure/aks/entra-id-authorization
[k8s-rbac-with-entra]: https://learn.microsoft.com/en-us/azure/aks/kubernetes-rbac-entra-id
[workload-identity]: https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview
[oidc-issuer]: https://learn.microsoft.com/en-us/azure/aks/use-oidc-issuer
[image-cleaner]: https://learn.microsoft.com/en-us/azure/aks/image-cleaner
[deployment-safeguards]: https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards
[pod-security-standards]: https://learn.microsoft.com/en-us/azure/aks/deployment-safeguards#turn-on-pod-security-standards
[api-server-vnet-integration]: https://learn.microsoft.com/en-us/azure/aks/api-server-vnet-integration
[azure-cni-powered-by-cilium]: https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium
[kubenet]: https://learn.microsoft.com/en-us/azure/aks/configure-kubenet
[azure-cni]: https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni
[azure-cni-overlay]: https://learn.microsoft.com/en-us/azure/aks/azure-cni-overlay
[use-byo-cni]: https://learn.microsoft.com/en-us/azure/aks/use-byo-cni
[app-routing]: https://learn.microsoft.com/en-us/azure/aks/app-routing
[app-routing-gateway-api]: https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api
[istio-deploy-ingress]: https://learn.microsoft.com/en-us/azure/aks/istio-deploy-ingress
[istio-upgrade]: https://learn.microsoft.com/en-us/azure/aks/istio-upgrade
[managed-nat-gateway]: https://learn.microsoft.com/en-us/azure/aks/nat-gateway#create-an-aks-cluster-with-a-managed-nat-gateway
[userassigned-nat-gateway]: https://learn.microsoft.com/en-us/azure/aks/nat-gateway#create-an-aks-cluster-with-a-userassignednatgateway
[udr]: https://learn.microsoft.com/en-us/azure/aks/egress-outboundtype#outbound-type-of-userdefinedrouting
[egress-load-balancer]: https://learn.microsoft.com/en-us/azure/aks/egress-outboundtype#outbound-type-of-loadbalancer
[istio-mesh]: https://learn.microsoft.com/en-us/azure/aks/istio-about
[istio-cni]: https://learn.microsoft.com/en-us/azure/aks/istio-cni
[automated-deployments]: https://learn.microsoft.com/en-us/azure/aks/automated-deployments
[kubernetes-action]: https://learn.microsoft.com/en-us/azure/aks/kubernetes-action
[managed-prometheus]: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
[managed-grafana]: https://learn.microsoft.com/en-us/azure/managed-grafana/overview
[container-insights]: https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview
[uptime-sla]: https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers#uptime-sla-terms-and-conditions
[long-term-support]: https://learn.microsoft.com/en-us/azure/aks/long-term-support
[quickstart-aks-automatic]: https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network
[automatic-custom-network]: https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-custom-network
[automatic-private-custom-network]: https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-private-custom-network
[azure-sla]: https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services
[managed-system-node-pool]: https://learn.microsoft.com/en-us/azure/aks/automatic/aks-automatic-managed-system-node-pools-about#key-features-and-benefits
[nrg-lockdown]: https://learn.microsoft.com/en-us/azure/aks/node-resource-group-lockdown
[security-restrictions]: https://learn.microsoft.com/en-us/azure/aks/automatic/aks-automatic-managed-system-node-pools-about#security-restrictions-for-managed-system-node-pools
