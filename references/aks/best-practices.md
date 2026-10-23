# Best Practices for Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/best-practices  
> Microsoft doc last updated: 11/21/2023


**Applies to**: :heavy_check_mark: AKS Automatic :heavy_check_mark: AKS Standard

Building and running applications successfully in Azure Kubernetes Service (AKS) requires understanding and implementation of some key concepts, including:

- Multi-tenancy and scheduler features.
- Cluster and pod security.
- Business continuity and disaster recovery.

The AKS product group, engineering teams, and field teams (including global black belts (GBBs)) contributed to, wrote, and grouped the following best practices and conceptual articles. Their purpose is to help cluster operators and developers better understand the concepts above and implement the appropriate features.

## Choose your AKS mode first

AKS supports two cluster modes: **AKS Automatic** and **AKS Standard**. Choose AKS Automatic when you want a production-ready baseline with less day-2 platform management. Choose AKS Standard when you need deeper control over cluster infrastructure and configuration.

The best practices in this article apply to both modes. However, implementation responsibility differs by mode: AKS Automatic provides more preconfigured defaults, while AKS Standard typically requires more explicit operator configuration.

| Area | AKS Automatic | AKS Standard |
| ---- | ------------- | ------------ |
| Baseline cluster setup | More preconfigured defaults | More explicit setup choices |
| System node pools | Service-managed model | Operator-managed model |
| Security baseline controls | Several controls are preconfigured in common scenarios | Controls are commonly enabled and maintained by operators |
| Networking baseline | Opinionated defaults for common patterns | Broader configuration flexibility |
| Upgrades and operations | More managed operational behavior | More operator-directed behavior |
| Best-practice focus | Validate, govern, and tune defaults | Design and configure platform controls |

## Cluster operator best practices

If you're a cluster operator, work with application owners and developers to understand their needs. Then, you can use the following best practices to configure your AKS clusters to fit your needs.

An important practice that you should include as part of your application development and deployment process is remembering to follow commonly used deployment and testing patterns. Testing your application before deployment is an important step to ensure its quality, functionality, and compatibility with the target environment. It can help you identify and fix any errors, bugs, or issues that might affect the performance, security, or usability of the application or underlying infrastructure.

In AKS Standard, operators usually implement more platform controls directly. In AKS Automatic, operators typically focus more on validating service-managed defaults, defining guardrails, and tuning policy and workload boundaries.

### Multi-tenancy

Multi-tenancy guidance applies to both modes. In AKS Automatic, baseline cluster defaults can reduce initial setup work. In AKS Standard, platform teams usually configure more tenancy and scheduling controls explicitly.

- [Best practices for cluster isolation](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-cluster-isolation): Includes multi-tenancy core components and logical isolation with namespaces.
- [Best practices for basic scheduler features](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-scheduler): Includes using resource quotas and pod disruption budgets.
- [Best practices for advanced scheduler features](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-advanced-scheduler): Includes using taints and tolerations, node selectors and affinity, and inter-pod affinity and anti-affinity.
- [Cluster authentication concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authentication): Includes integration with Microsoft Entra ID, using Kubernetes role-based access control (Kubernetes RBAC), and using Azure RBAC.
- [Cluster authorization concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authorization): Includes integration with Microsoft Entra ID, using Kubernetes role-based access control (Kubernetes RBAC), using Azure RBAC, and pod identities.

### Security

Security guidance applies to both modes. AKS Automatic includes preconfigured security defaults for many common scenarios, while AKS Standard typically requires explicit enablement and lifecycle ownership of more controls.

- [Best practices for cluster security and upgrades](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-cluster-security): Includes securing access to the API server, limiting container access, and managing upgrades and node reboots.
- [Best practices for container image management and security](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-container-image-management): Includes securing the image and runtimes and automated builds on base image updates.
- [Best practices for pod security](https://learn.microsoft.com/en-us/azure/aks/developer-best-practices-pod-security): Includes securing access to resources, limiting credential exposure, and using pod identities and digital key vaults.

#### AKS Automatic security baseline

AKS Automatic is designed with a hardened baseline and preconfigured controls for many production scenarios. Use the security best-practice articles to validate posture, manage exceptions, and align with enterprise policy requirements.

For current feature behavior and scope, see [Introduction to AKS Automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic).

### Network and storage

Network and storage best practices apply to both modes. AKS Automatic provides more opinionated defaults for common patterns, while AKS Standard provides broader configuration flexibility and operator control.

- [Best practices for network connectivity](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-network): Includes different network models, using ingress and web application firewalls (WAF), and securing node SSH access.
- [Best practices for storage and backups](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-storage): Includes choosing the appropriate storage type and node size, dynamically provisioning volumes, and data backups.

### Running enterprise-ready workloads

Reliability and recovery practices apply to both modes. AKS Automatic can simplify baseline operations, while AKS Standard offers greater design-time control for specialized architectures.

- [Best practices for business continuity and disaster recovery](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-multi-region): Includes using region pairs, multiple clusters with Azure Traffic Manager, and geo-replication of container images.

## Developer best practices

If you're a developer or application owner, you can simplify your development experience and define required application performance features.

Developer guidance applies to both modes. In AKS Automatic, teams can usually move faster with preconfigured cluster foundations. In AKS Standard, developers should align assumptions with platform-team cluster configuration choices.

- [Best practices for application developers to manage resources](https://learn.microsoft.com/en-us/azure/aks/developer-best-practices-resource-management): Includes defining pod resource requests and limits, configuring development tools, and checking for application issues.
- [Best practices for pod security](https://learn.microsoft.com/en-us/azure/aks/developer-best-practices-pod-security): Includes securing access to resources, limiting credential exposure, and using pod identities and digital key vaults.
- [Best practices for deployment and cluster reliability](https://learn.microsoft.com/en-us/azure/aks/best-practices-app-cluster-reliability): Includes deployment, cluster, and node pool level best practices.

## Kubernetes and AKS concepts

The following conceptual articles cover some of the fundamental features and components for clusters in AKS:

- [Kubernetes core concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads)
- [Access and identity](https://learn.microsoft.com/en-us/azure/aks/concepts-identity)
- [Security concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-security)
- [Network concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-network)
- [Storage options](https://learn.microsoft.com/en-us/azure/aks/concepts-storage)
- [Scaling options](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)

## Related content

For guidance on a designing an enterprise-scale implementation of AKS, see [Plan your AKS design][plan-aks-design].

To choose the right cluster mode for your workload and operating model, see [AKS Automatic and AKS Standard feature comparison](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic#aks-automatic-and-standard-feature-comparison).

For more information about AKS, see the following documentation:

- [Kubernetes core concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads)
- [Access and identity](https://learn.microsoft.com/en-us/azure/aks/concepts-identity)
- [Security concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-security)
- [Network concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-network)
- [Storage options](https://learn.microsoft.com/en-us/azure/aks/concepts-storage)
- [Scaling options](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)

[plan-aks-design]: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-start-here?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json
