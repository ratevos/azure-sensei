# Advanced Container Networking Services for Azure Kubernetes Service (AKS) Overview

> Source: https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview  
> Microsoft doc last updated: 05/28/2024


Advanced Container Networking Services is a suite of services designed to enhance the networking capabilities of Azure Kubernetes Service (AKS) clusters. Advanced Container Networking Services offers the following key feature sets: [**Container Network Observability**](#container-network-observability), [**Container Network Security**](#container-network-security), and [**Container Network Performance**](#container-network-performance). These features provide deep insights into network traffic, strengthen security measures, and optimize network performance for containerized applications running in AKS.

## Container Network Observability

Container Network Observability provides deep insights into network traffic and performance across containerized environments. This feature set **works across both Cilium and non-Cilium data planes**, offering flexibility for diverse networking needs. The feature uses eBPF to enhance scalability and performance by identifying potential bottlenecks and network congestion before applications are affected.

Key benefits of Container Network Observability include:

- Compatibility with all Container Networking Interface (CNI) variants in Azure.
- [_Container network metrics_](#container-network-metrics), including node-level metrics and Hubble metrics for detailed network insights.
- Hubble metrics for Domain Name System (DNS) resolution, pod-to-pod communication, and service interactions.
- [_Container network logs_](#container-network-logs) that capture essential metadata such as IPs, ports, and traffic flow for troubleshooting, monitoring, and security enforcement.
- Integration with the managed service for Prometheus in Azure Monitor and Azure Managed Grafana for simplified metrics storage and visualization.

### Container network metrics

This feature collects node-level metrics, including CPU, memory, and network performance, to monitor the health of cluster nodes. For deeper insights, Hubble metrics provide data on DNS resolution times, service-to-service communication, and pod-level network behavior. These metrics help you analyze application performance, detect anomalies, and optimize workloads.

For more information, see the [metrics overview](https://learn.microsoft.com/en-us/azure/aks/container-network-observability-metrics).

### Container network logs

Container network logs give you detailed insight into traffic within and across clusters by capturing metadata like source and destination IP addresses, ports, protocols, and flow direction. These logs enable monitoring network behavior, troubleshooting connectivity issues, and enforcing security policies. Persistent and real-time logging options ensure comprehensive, actionable network observability.

For more information, see the [container network logs overview](https://learn.microsoft.com/en-us/azure/aks/container-network-observability-logs).

## Container Network Security

Container Network Security enhances the security posture of AKS clusters by providing advanced network security features. It leverages eBPF technology to enforce network policies at the kernel level, ensuring efficient and effective security controls for containerized applications. **Container Network Security is available only on clusters with Azure CNI Powered by Cilium**.

### FQDN-based filtering

FQDN-based filtering allows you to create network policies based on fully qualified domain names (FQDNs) rather than IP addresses. This capability simplifies policy management, especially in dynamic environments where IP addresses frequently change. By using FQDNs, you can ensure that your applications communicate only with trusted external services, enhancing security and compliance.

For more information, see the [FQDN-based filtering overview](https://learn.microsoft.com/en-us/azure/aks/container-network-security-fqdn-filtering-concepts).

### Layer 7 policy

Layer 7 policy enables application-layer traffic control, allowing you to define policies based on specific application protocols. This feature provides granular control over network traffic, enabling you to enforce security policies that align with application behavior. With Layer 7 policy, you can monitor and restrict traffic based on HTTP methods, URLs, headers, and other application-level attributes.

For more information, see the [Layer 7 policy overview](https://learn.microsoft.com/en-us/azure/aks/container-network-security-l7-policy-concepts).

### WireGuard Encryption

WireGuard Encryption leverages the WireGuard protocol to provide secure, encrypted communication between Cilium-managed endpoints within your AKS cluster. This feature ensures that data transmitted over the network is protected from eavesdropping and tampering, enhancing the overall security of your containerized applications.

For more information, see the [WireGuard encryption overview](https://learn.microsoft.com/en-us/azure/aks/container-network-security-wireguard-encryption-concepts).

### Cilium mTLS Encryption
Cilium mTLS encryption provides transparent, mutual TLS (mTLS) encryption and authentication for pod-to-pod traffic in Kubernetes without requiring application changes or introducing any extra networking stack.

For more information, see the [Cilium mTLS encryption overview](https://learn.microsoft.com/en-us/azure/aks/container-network-security-cilium-mutual-tls-concepts).

## Container Network Performance

Container Network Performance optimizes network performance for containerized applications running in AKS clusters. It leverages eBPF technology to enhance network routing and reduce latency, ensuring that applications can communicate efficiently and effectively. **Container Network Performance is available only on clusters with Azure CNI Powered by Cilium**.

### eBPF Host Routing

eBPF Host Routing uses extended Berkeley Packet Filter (eBPF) technology to optimize traffic flow in AKS clusters.

For more information, see the [eBPF Host Routing overview](https://learn.microsoft.com/en-us/azure/aks/container-network-performance-ebpf-host-routing).

## Container Network Connectivity

## Cross Cluster Networking (Preview)

Cross-cluster networking enables direct pod-to-pod communication across multiple AKS clusters, providing seamless east-west connectivity, multi-cluster observability, and consistent security enforcement. It uses a managed offering of Cilium Cluster Mesh through Azure Kubernetes Fleet Manager to create a flat pod network across clusters without overlays or gateways.

For more information, see the [Cross-cluster networking use cases for Azure Kubernetes Fleet Manager](https://learn.microsoft.com/en-us/azure/aks/cross-cluster-networking-fleet-use-cases).

## Related content

- [Set up Advanced Container Networking Services on your Azure Kubernetes Service (AKS) cluster](https://learn.microsoft.com/en-us/azure/aks/use-advanced-container-networking-services)
- [Advanced Container Networking Services pricing](https://azure.microsoft.com/pricing/details/azure-container-networking-services/)
