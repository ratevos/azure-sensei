# Concepts - Access and Identity in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/concepts-identity  
> Microsoft doc last updated: 04/18/2026


**Applies to**: :heavy_check_mark: AKS Automatic :heavy_check_mark: AKS Standard

AKS uses identity in five distinct scenarios. Each scenario answers a different question and has its own configuration model.

For most production AKS workloads, AKS Automatic is the recommended default because it starts with a production-ready platform baseline, including identity-related defaults, while preserving the same AKS identity model described in this article.

This article gives a brief introduction to each scenario, explains how the guidance maps to AKS Automatic and AKS Standard, and points to the deep-dive documentation.

## The five identity scenarios in AKS

| Scenario | Question it answers | Deep-dive docs |
| -------- | ------------------- | -------------- |
| **A. Kubernetes control-plane authentication** | Who is the caller hitting the Kubernetes API? | [Cluster authentication concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authentication), [external identity providers](https://learn.microsoft.com/en-us/azure/aks/external-identity-provider-authentication-overview) |
| **B. Kubernetes control-plane authorization** | What is the caller allowed to do once authenticated to the Kubernetes API? | [Cluster authorization concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authorization) |
| **C. AKS resource authorization (Azure Resource Manager)** | Who can perform Azure-level operations on the AKS resource, such as pulling `kubeconfig`? | [Limit access to cluster configuration file](https://learn.microsoft.com/en-us/azure/aks/control-kubeconfig-access), [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#containers) |
| **D. Cluster identity (cluster → Azure)** | How does the AKS cluster act on Azure to manage resources on your behalf? | [Managed identities in AKS](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity) |
| **E. Workload identity (pod → Azure)** | How do pods authenticate to Azure services such as Key Vault or Storage? | [Microsoft Entra Workload ID overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) |

## Identity posture in AKS Automatic and AKS Standard

The five identity scenarios in this article apply to both AKS Automatic and AKS Standard. The main difference is operational posture:

- AKS Automatic provides more preconfigured identity and security defaults.
- AKS Standard provides more manual control and requires more setup choices.

Use AKS Automatic as the default starting point for most production workloads, and use AKS Standard when you need deeper custom platform configuration.

For an overview of AKS Automatic, see [Introduction to Azure Kubernetes Service (AKS) Automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic).

### AKS Automatic and AKS Standard identity posture comparison

| Identity area | AKS Automatic posture | AKS Standard posture | Learn more |
| ------------- | --------------------- | -------------------- | ---------- |
| Kubernetes API authentication | Production-oriented defaults with Microsoft Entra integration as the recommended model | Configurable, including local accounts and Entra integration choices | [Cluster authentication concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authentication) |
| Kubernetes API authorization | Azure RBAC for Kubernetes authorization is preconfigured | Local-account-first and authorization model selected by cluster configuration | [Cluster authorization concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authorization) |
| AKS resource authorization | Uses standard Azure RBAC model on AKS resource operations | Uses standard Azure RBAC model on AKS resource operations | [Control kubeconfig access](https://learn.microsoft.com/en-us/azure/aks/control-kubeconfig-access) |
| Cluster identity | Uses managed identity model with production baseline defaults | Uses managed identity model with operator-selected setup | [Managed identities in AKS](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity) |
| Workload identity | Workload identity and OIDC issuer are preconfigured | Optional and configured by operator | [Workload identity overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) |

The rest of this article gives a brief orientation to each scenario.

## A. Kubernetes control-plane authentication

Kubernetes control-plane authentication establishes the identity of a user or service principal calling the Kubernetes API server. AKS supports:

- **Microsoft Entra ID (recommended)**: Use Entra ID identities and groups to sign in to the cluster. Microsoft Entra integration provisions and rotates the integration on your behalf. To enable, see [Use Microsoft Entra integration](https://learn.microsoft.com/en-us/azure/aks/entra-id-control-plane-authentication).
- **Local accounts**: A built-in cluster admin certificate that bypasses Entra ID. We recommend disabling local accounts in production. See [Manage local accounts](https://learn.microsoft.com/en-us/azure/aks/local-accounts).
- **External identity providers**: Use an OIDC-compliant identity provider other than Microsoft Entra ID. See [External identity provider authentication](https://learn.microsoft.com/en-us/azure/aks/external-identity-provider-authentication-overview).

For most production workloads, start with AKS Automatic and Microsoft Entra integration.

For an in-depth look at how AKS authenticates Kubernetes API requests, see [Cluster authentication concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authentication).

## B. Kubernetes control-plane authorization

After a caller is authenticated to the Kubernetes API, AKS authorizes the request using one (or both) of two models:

- **Kubernetes RBAC**: The native Kubernetes `Role`, `ClusterRole`, and `RoleBinding` model evaluated by the API server. Permissions live in the cluster as Kubernetes objects.
- **Microsoft Entra ID authorization**: An AKS authorization webhook delegates authorization decisions to Microsoft Entra ID using Azure role assignments. Azure RBAC role assignments with `dataActions` are supported for all standard Kubernetes API resources, and role assignments with Azure ABAC conditions are supported for custom resources. Manage permissions centrally in Microsoft Entra ID to govern many clusters from a single role assignment at subscription, management group, or resource group scope.

In AKS Automatic, Azure RBAC for Kubernetes authorization is preconfigured as part of the production-ready default posture.

For a comparison and guidance on when to use each model, see [Cluster authorization concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authorization).

<a name='kubernetes-rbac'></a>
<a name='azure-rbac-for-kubernetes-authorization'></a>
<a name='azure-rbac-to-authorize-access-to-the-aks-resource'></a>

## C. AKS resource authorization (Azure Resource Manager)

In addition to authorizing calls to the Kubernetes API, you also need to authorize Azure-level operations on the AKS resource itself. The most common example is controlling who can pull a cluster's `kubeconfig`, which is a standalone Azure Resource Manager operation that you can govern granularly with Azure RBAC. This operation uses standard Azure RBAC against the `Microsoft.ContainerService` resource provider, is separate from Kubernetes API authorization, and applies the same way to AKS Automatic and AKS Standard. For more information, see [Limit access to the cluster configuration file](https://learn.microsoft.com/en-us/azure/aks/control-kubeconfig-access) and the built-in roles in [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#containers).

## D. Cluster identity (cluster → Azure)

AKS clusters use Azure managed identities to act on Azure resources on your behalf — for example, to create load balancers, attach disks, or pull images from Azure Container Registry. The main identities are:

- **Control-plane identity**: Used by the cluster control plane to manage Azure resources for the cluster.
- **Kubelet identity**: Used by the kubelet on each node to authenticate to services such as Azure Container Registry.
- **Add-ons/extensions identity**: Some AKS add-ons and extensions use their own managed identities.

AKS Automatic keeps this same identity model while reducing setup friction through preconfigured production defaults.

For details on each identity type and how to use system-assigned vs user-assigned identities, see [Managed identities in AKS](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity).

## E. Workload identity (pod → Azure)

Workload identity lets pods running in your AKS cluster authenticate to Microsoft Entra–protected Azure services (such as Key Vault, Storage, or Cosmos DB) without storing secrets in the cluster. AKS uses [Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview), which projects a Kubernetes service account token federated to a Microsoft Entra application or user-assigned managed identity.

AKS Automatic includes workload identity and OIDC issuer as preconfigured defaults. In AKS Standard, these capabilities are optional and configured by the operator.

Don't use the deprecated [Microsoft Entra pod-managed identity](https://learn.microsoft.com/en-us/azure/aks/use-azure-ad-pod-identity) for new workloads.

## Decision guide

| Goal | Use these docs |
| ---- | -------------- |
| Start with a production-ready identity baseline for most workloads | [Introduction to AKS Automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic) |
| Sign users into the cluster with Microsoft Entra ID | [Enable Microsoft Entra integration](https://learn.microsoft.com/en-us/azure/aks/entra-id-control-plane-authentication) |
| Govern who can do what in the Kubernetes API across many clusters | [Use Microsoft Entra ID authorization for the Kubernetes API](https://learn.microsoft.com/en-us/azure/aks/entra-id-authorization) |
| Restrict access to specific custom resource types | [ABAC conditions in Entra ID authorization](https://learn.microsoft.com/en-us/azure/aks/entra-id-authorization#restrict-custom-resource-access-using-abac-conditions-preview) |
| Author per-cluster, per-namespace permissions as Kubernetes objects | [Use Kubernetes RBAC with Entra integration](https://learn.microsoft.com/en-us/azure/aks/kubernetes-rbac-entra-id) |
| Let the cluster pull from ACR or attach disks | [Managed identities in AKS](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity) |
| Let pods reach Key Vault or Storage without secrets | [Microsoft Entra Workload ID overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview) |
| Restrict who can download the cluster `kubeconfig` | [Limit access to cluster configuration file](https://learn.microsoft.com/en-us/azure/aks/control-kubeconfig-access) |
| Create a production-ready cluster with default identity posture | [Create an AKS Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network) |

<a name='aks-service-permissions'></a>

## AKS service permissions reference

For the Azure permissions that AKS uses (the identity that creates the cluster, the cluster identity at runtime, additional cluster identity permissions, and AKS node access), see [AKS service permissions reference](https://learn.microsoft.com/en-us/azure/aks/aks-service-permissions).

## Related content

- [Introduction to Azure Kubernetes Service (AKS) Automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic)
- [Create an Azure Kubernetes Service (AKS) Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network)
- [Cluster authentication concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authentication)
- [Cluster authorization concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-cluster-authorization)
- [Use Microsoft Entra ID authorization for the Kubernetes API](https://learn.microsoft.com/en-us/azure/aks/entra-id-authorization)
- [Managed identities in AKS](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity)
- [Microsoft Entra Workload ID overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview)

For more information on core Kubernetes and AKS concepts, see the following articles:

- [Kubernetes / AKS clusters and workloads][aks-concepts-clusters-workloads]
- [Kubernetes / AKS security][aks-concepts-security]
- [Kubernetes / AKS virtual networks][aks-concepts-network]
- [Kubernetes / AKS storage][aks-concepts-storage]
- [Kubernetes / AKS scale][aks-concepts-scale]

[aks-concepts-clusters-workloads]: https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads
[aks-concepts-security]: https://learn.microsoft.com/en-us/azure/aks/concepts-security
[aks-concepts-scale]: https://learn.microsoft.com/en-us/azure/aks/concepts-scale
[aks-concepts-storage]: https://learn.microsoft.com/en-us/azure/aks/concepts-storage
[aks-concepts-network]: https://learn.microsoft.com/en-us/azure/aks/concepts-network
