# Operate cost optimized Azure Kubernetes Service (AKS) at scale

> Source: https://learn.microsoft.com/en-us/azure/aks/operate-cost-optimized-scale  
> Microsoft doc last updated: 03/18/2025


This article provides guidance on how to operate cost optimized Azure Kubernetes Service (AKS) at scale.

## Azure Kubernetes Fleet Manager (Kubernetes Fleet)

[Azure Kubernetes Fleet Manager (Kubernetes Fleet)](https://learn.microsoft.com/en-us/azure/kubernetes-fleet/overview) enables at-scale management of multiple AKS clusters. You can create a *Fleet resource* and use it to manage multiple clusters as a single entity, orchestrate updates across multiple clusters, and propagate Kubernetes resources across multiple clusters. When creating a new *Fleet resource*, you can create it with or without a *hub cluster*. A *hub cluster* is a managed AKS cluster that acts a hub to store and propagate Kubernetes resources.

Kubernetes Fleet can help you reduce the management overhead cost of operating multiple clusters by providing a single entry point for managing multiple clusters. For more information, see the [Azure Kubernetes Fleet Manager documentation](https://learn.microsoft.com/en-us/azure/kubernetes-fleet/).

### Resource propagation

Kubernetes Fleet provides *resource propagation* to enable at-scale management of Kubernetes resources. You can create Kubernetes resources in the *hub cluster* and propagate them to specified *member clusters* using the `MemberCluster` and `ClusterResourcePlacement` custom resources.

For more information, see [Kubernetes Fleet resource placement from hub cluster to member clusters](https://learn.microsoft.com/en-us/azure/kubernetes-fleet/concepts-resource-propagation).

### Intelligent resource placement

Kubernetes Fleet provides *intelligent resource placement*, which can make scheduling decisions based on node count, cost of compute/memory in target member clusters, and resource availability in target member clusters. This allows you to place workloads in the most cost-effective member cluster based on your workload requirements.

For more information, see [Intelligent cross-cluster Kubernetes resource placement using Azure Kubernetes Fleet Manager](https://learn.microsoft.com/en-us/azure/kubernetes-fleet/intelligent-resource-placement).

## AKS Automatic

[AKS Automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic) offers an experience that makes the most common tasks on Kubernetes fast and frictionless, while preserving the flexibility, extensibility, and consistency of Kubernetes. Azure takes care of cluster setup, including node management, scaling, and security, and preconfigures settings that follow AKS well-architected recommendations.

AKS Automatic clusters are designed to help reduce management overhead costs of creating cluster templates, managing the cluster lifecycle, guardrails, and updates. Scaling is seamless and dynamic. Nodes are created based on workload requests using [node autoprovisioning (NAP)](https://learn.microsoft.com/en-us/azure/aks/node-autoprovision) and workloads are automatically scaled with features like Horizontal Pod Autoscaler (HPA), [Kubernetes Event Driven Autoscaling (KEDA)](https://learn.microsoft.com/en-us/azure/aks/keda-about), and [Vertical Pod Autoscaler (VPA)](https://learn.microsoft.com/en-us/azure/aks/vertical-pod-autoscaler).

## Azure Advisor cost recommendations

AKS cost recommendations in Azure Advisor provide recommendations to help you achieve cost-efficiency without sacrificing reliability. Advisor analyzes your resource configurations and recommends optimization solutions. For more information, see [Get Azure Kubernetes Service (AKS) cost recommendations in Azure Advisor](https://learn.microsoft.com/en-us/azure/aks/cost-advisors).

## Next steps

To learn more about cost optimization in Azure Kubernetes Service (AKS), see the following articles:

- [Best practices for cost optimization in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/best-practices-cost)
- [Understand Azure Kubernetes Service (AKS) usage and costs](https://learn.microsoft.com/en-us/azure/aks/understand-aks-costs)
- [Optimize Azure Kubernetes Service (AKS) usage and costs](https://learn.microsoft.com/en-us/azure/aks/optimize-aks-costs)
- [Azure Kubernetes Service (AKS) cost analysis](https://learn.microsoft.com/en-us/azure/aks/cost-analysis)
