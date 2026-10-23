# Plan Networking for Azure Kubernetes Service (AKS) Workloads

> Source: https://learn.microsoft.com/en-us/azure/aks/plan-networking  
> Microsoft doc last updated: 09/15/2026


This article provides an overview of the networking components you need to consider when planning your Azure Kubernetes Service (AKS) workloads.

## Networking components

When planning your AKS networking, you need to consider four main components: the **control plane**, **nodes**, **pods**, and **applications**.

Each component has its own networking requirements, considerations, and options. You can use the following articles to learn more about and plan for each component:

- [Plan control plane networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-control-plane-networking)
- [Plan node networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-node-networking)
- [Plan pod networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-pod-networking)
- [Plan application networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-application-networking)

Each article poses a question to help guide your planning, and then provides options, recommendations, and best practices.

> [!NOTE]
> You can share subnets for API server, system node pool, and agent node pool resources between multiple clusters. Ensure you allocate sufficient IP addresses to avoid issues.

## Related content

To learn more about networking in AKS, see the following articles:

- [Networking concepts for applications in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/concepts-network)
- [Kubernetes Services in AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-network-services)
- [Best practices for network connectivity and security in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-network)
