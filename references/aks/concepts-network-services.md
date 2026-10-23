# Concepts - Services in Azure Kubernetes Services (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/concepts-network-services  
> Microsoft doc last updated: 04/08/2024


You can use Kubernetes Services to logically group pods and provide network connectivity by allowing direct access to them through a specific IP address or DNS name on a designated port. This allows you to expose your application workloads to other services within the cluster or to external clients without having to manually manage the network configuration for each pod hosting a workload.

You can specify what kind of service you want using Kubernetes *Service `type` values*. For more information, see the [Kubernetes Service documentation][service-types].

The following Service types are available in AKS: [`ClusterIP`](#clusterip), [`NodePort`](#nodeport), [`LoadBalancer`](#loadbalancer), and [`ExternalName`](#externalname).

## ClusterIP
  
`ClusterIP` creates an internal IP address for use within the AKS cluster. The `ClusterIP` Service is good for *internal-only applications* that support other workloads within the cluster. ClusterIP is used by default if you don't explicitly specify a type for a Service.

## NodePort

`NodePort` creates a port mapping on the underlying node that allows the application to be accessed directly with the node IP address and port.

## LoadBalancer

`LoadBalancer` creates an Azure load balancer resource, configures an external IP address, and connects the requested pods to the load balancer backend pool. To allow customer traffic to reach the application, load balancing rules are created on the desired ports.

For HTTP load balancing of inbound traffic, you can also use an [Ingress controller][ingress-controllers].

You can also use the `LoadBalancer` type to create multiple public load balancers in a single AKS cluster. This is useful for large clusters or port-heavy workloads that can quickly exhaust the limits of a single load balancer. For more information, see [Use multiple public load balancers in Azure Kubernetes Service (preview)](https://learn.microsoft.com/en-us/azure/aks/use-multiple-standard-load-balancer).

## ExternalName

`ExternalName` creates a specific DNS entry for easier application access. You can dynamically assign the load balancers and service IP address, or you can specify an existing static IP address. You can assign both internal and external static IP addresses. Existing static IP addresses are often tied to a DNS entry.

You can create both *internal* and *external* load balancers. Internal load balancers are only assigned a private IP address, so they can't be accessed from the Internet.

[service-types]: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types

[ingress-controllers]:https://learn.microsoft.com/en-us/azure/aks/concepts-network-ingress#ingress-controllers
