# Plan Control Plane Networking for Azure Kubernetes Service (AKS) Workloads

> Source: https://learn.microsoft.com/en-us/azure/aks/plan-control-plane-networking  
> Microsoft doc last updated: 09/15/2026


In this article, you learn control plane networking options for Azure Kubernetes Service (AKS). We first pose a question to help guide your planning, and then provide options, recommendations, and best practices.

## How do you want to access your API server?

The Azure-managed AKS control plane consists of several components that help manage the cluster, including the API server. You need to configure networking so that nodes and end users can access the API server for things like updates and cluster management.

## Control plane networking options

When setting up control plane networking, you can choose a **public cluster** or a **private cluster**:

| Control plane networking option | Diagram of networking components | Features & functionality |
|---------------------------------|----------------------------------|--------------------------|
| Public cluster |  | • API server accessible via a _public IP address_, allowing users and nodes to connect without any extra configuration. <br> • You can restrict access to certain source IP ranges. <br> • Uses konnectivity tunnel for node and pod access. <br> • Supports [API Server VNet Integration](#api-server-vnet-integration). |
| Private cluster |  | • API server accessible via internal IP address, with [Azure Private DNS](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview) used for API server hostname. <br> • Uses [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) to securely connect to the API server. <br> • Uses konnectivity tunnel for node and pod access. <br> • Supports [API Server VNet Integration](#api-server-vnet-integration). |

### API Server VNet Integration

[API Server VNet Integration](https://learn.microsoft.com/en-us/azure/aks/api-server-vnet-integration) is supported for public or private clusters. API Server VNet Integration enables network communication between the API server and the cluster nodes without requiring a private link or tunnel. The API server is available behind an internal load balancer VIP in the delegated subnet, which the nodes are configured to utilize.

With API Server VNet Integration:

- API server provisions into a delegated subnet within your virtual network (VNet).
- Can use a konnectivity tunnel for pod access in [Overlay](https://learn.microsoft.com/en-us/azure/aks/concepts-network-azure-cni-overlay) or [BYO CNI](https://learn.microsoft.com/en-us/azure/aks/use-byo-cni) clusters.
- Can add or remove API server public access at any time without cluster disruption.

> [!NOTE]
> API Server VNet Integration isn't currently available in qatarcentral.

## Recommendations

Our **general recommendation** is to use a **public cluster**, as it simplifies the networking setup and allows for easier access to the API server. However, if you have **specific security or compliance requirements**, a **private cluster** might be more appropriate.

To enhance security and simplify network management, enable [API Server VNet Integration](#api-server-vnet-integration) for both public and private clusters.

> [!NOTE]
> You can share subnets for the API server, system node pool, and agent node pool resources between multiple clusters. You must ensure sufficient IP addresses are allocated to avoid issues.

## Related content

- [Plan node networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-node-networking)
- [Plan pod networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-pod-networking)
- [Plan application networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-application-networking)
