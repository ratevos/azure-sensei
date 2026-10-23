# Get Started With Azure Kubernetes Service (AKS) Basics

> Source: https://learn.microsoft.com/en-us/azure/aks/get-started-aks  
> Microsoft doc last updated: 06/05/2026


This guide provides resources to help you learn the basics of [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/what-is-aks).

For most production workloads, start with [**AKS Automatic**](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic). AKS Automatic is the recommended production-ready default in AKS and provides preconfigured best-practice defaults for scaling, security, networking, monitoring, and upgrades.

Use AKS Standard when you need deeper control over platform configuration and lifecycle operations.

## AKS cluster modes

AKS supports two cluster modes:

- **AKS Automatic (recommended default)**: Best for most production workloads and faster time to value with preconfigured production-ready defaults.
- **AKS Standard**: Best when you require advanced customization for networking, identity, node topology, or upgrade behavior.

For detailed differences, see [AKS Automatic and AKS Standard feature comparison](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic#aks-automatic-and-standard-feature-comparison).

> [!NOTE]
> AKS Automatic is the recommended starting point for most production-ready AKS workloads. If your requirements demand deeper infrastructure customization, AKS Standard remains fully supported.

## Learn the basics of AKS

The resources in the following sections provide an introduction to AKS fundamentals and common platform areas.

### AKS fundamentals

- [What is AKS?](https://learn.microsoft.com/en-us/azure/aks/what-is-aks)
- [What is AKS Automatic?](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic)
- [Core concepts](https://learn.microsoft.com/en-us/azure/aks/core-aks-concepts)
- [Deploy clusters with AKS Automatic lab](https://azure-samples.github.io/aks-labs/docs/getting-started/aks-automatic/)
- [Kubernetes and AKS fundamentals lab](https://azure-samples.github.io/aks-labs/docs/getting-started/k8s-aks-fundamentals/)
- Create an AKS cluster
  - [Create a Linux-based AKS Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-from-code)
  - [Create a Linux-based AKS cluster](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli)
  - [Create a Windows-based AKS cluster](https://learn.microsoft.com/en-us/azure/aks/learn/quick-windows-container-deploy-cli)

### Networking

- [AKS networking overview](https://learn.microsoft.com/en-us/azure/aks/concepts-network)
- [AKS networking best practices video](https://www.youtube.com/watch?v=mAGqnX2WW1M)
- [Istio service mesh on AKS lab](https://azure-samples.github.io/aks-labs/docs/networking/istio-lab/)

### Access and identity

- [Access and identity concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-identity)
- [Workload identity lab](https://azure-samples.github.io/aks-labs/docs/security/workload-identity-lab/)

### Storage

- [Storage concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-storage)
- [Advanced storage concepts lab](https://azure-samples.github.io/aks-labs/docs/storage/advanced-storage-concepts/)

## Next steps

- [Create an AKS Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-from-code)
- [Learn about advanced AKS concepts](https://learn.microsoft.com/en-us/azure/aks/advanced-aks-concepts)
