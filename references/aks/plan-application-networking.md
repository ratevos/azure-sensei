# Plan Application Networking for Azure Kubernetes Service (AKS) Workloads

> Source: https://learn.microsoft.com/en-us/azure/aks/plan-application-networking  
> Microsoft doc last updated: 03/24/2025


In this article, you learn application networking options for Azure Kubernetes Service (AKS). We first pose a question to help guide your planning, and then provide options, recommendations, and best practices.

## How do you want to access your applications?

Application networking controls how the applications running in your Kubernetes pods are exposed to clients from outside the cluster.

## Application networking options

When setting up application networking, you can choose between a **Load Balancer Service with layer-4 load balancing** or **Ingress controllers with layer-7 load balancing**:

| Application networking option | Features & functionality |
|-------------------|--------------------------|
| Load Balancer Service | • Uses a Kubernetes `LoadBalancer` Service to directly expose an application on a public or private IP. <br> • Supports multiple ports and any TCP or UDP traffic. <br> • Requires _at least one_ unique IP:port pair per application. |
| Ingress controllers | • Exposes an application behind a layer-7 reverse proxy. <br> • Usable only for HTTP-like traffic (HTTP, HTTPS, gRPC). <br> • Can share a single public IP and ports for all ingress definitions on the same ingress controller. <br> • Managed ingress options include: Managed ingress-nginx through the [application routing add-on](https://learn.microsoft.com/en-us/azure/aks/app-routing), [Azure Application Gateway for Containers (recommended)](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview), and [Istio ingress gateway](https://learn.microsoft.com/en-us/azure/aks/istio-about). |

## Recommendations

For **non-HTTP traffic**, we recommend using **Load Balancer Service with layer-4 load balancing**. This approach provides direct access to your applications and supports a wide range of protocols. For **HTTP-like traffic**, we recommend using **Ingress controllers with layer-7 load balancing**. This approach allows you to take advantage of advanced routing features and share a single public IP for multiple applications.

## Related content

- [Plan control plane networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-control-plane-networking)
- [Plan node networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-node-networking)
- [Plan pod networking for Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/plan-pod-networking)
