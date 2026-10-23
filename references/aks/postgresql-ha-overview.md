# Deploying a PostgreSQL Database on AKS with CloudNativePG

> Source: https://learn.microsoft.com/en-us/azure/aks/postgresql-ha-overview  
> Microsoft doc last updated: 06/18/2025


In this guide, you deploy a highly available PostgreSQL cluster that spans multiple Azure availability zones on AKS with Azure CLI.

This article walks through the prerequisites for setting up a PostgreSQL cluster on [Azure Kubernetes Service (AKS)][what-is-aks] and provides an overview of the full deployment process and architecture.

> [!IMPORTANT]
>
> Open-source software is mentioned throughout AKS documentation and samples. Software that you deploy is excluded from AKS service-level agreements, limited warranty, and Azure support. As you use open-source technology alongside AKS, consult the support options available from the respective communities and project maintainers to develop a plan.
>
> Microsoft takes responsibility for building the open-source packages that we deploy on AKS. That responsibility includes having complete ownership of the build, scan, sign, validate, and hotfix process, along with control over the binaries in container images. For more information, see [Vulnerability management for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-vulnerability-management#aks-container-images) and [AKS support coverage](https://learn.microsoft.com/en-us/azure/aks/support-policies#aks-support-coverage).

## Prerequisites

* This guide assumes a basic understanding of [core Kubernetes concepts][core-kubernetes-concepts] and [PostgreSQL][postgresql].
* You need the **Owner** or **User Access Administrator** and the **Contributor** [Azure built-in roles][azure-roles] on a subscription in your Azure account.

* You also need the following resources installed:

  * [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) version 2.56 or later.
  * [jq][jq], version 1.5 or later.
  * [kubectl][install-kubectl] version 1.21.0 or later.
  * [Helm][install-helm] version 3.0.0 or later.
  * [openssl][install-openssl] version 3.3.0 or later.
  * [Visual Studio Code][install-vscode] or equivalent.
  * [Krew][install-krew] version 0.4.4 or later.
  * [kubectl CloudNativePG (CNPG) Plugin][cnpg-plugin].

## Deployment process

In this guide, you learn how to:

* Use Azure CLI to create a multi-zone AKS cluster.
* Deploy a highly available PostgreSQL cluster and database using the [CNPG operator][cnpg-plugin].
* Set up monitoring for PostgreSQL using Prometheus and Grafana.
* Deploy a sample dataset to a PostgreSQL database.
* Perform PostgreSQL and AKS cluster upgrades.
* Simulate a cluster interruption and PostgreSQL replica failover.
* Perform backup and restore of a PostgreSQL database.

## Deployment architecture

This diagram illustrates a PostgreSQL cluster setup with one primary replica and two read replicas managed by the [CloudNativePG (CNPG)](https://cloudnative-pg.io/) operator. The architecture provides a highly available PostgreSQL running on an AKS cluster that can withstand a zone outage by failing over across replicas.

Backups are stored on [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/), providing another way to restore the database in the event of an issue with streaming replication from the primary replica.

You might choose to host PostgreSQL on AKS when you need full control over database configuration, extensions, and deployment architecture. It’s ideal for integrating tightly with Kubernetes-native tooling, optimizing costs at scale, and fine-tuning performance through custom resource allocation, caching strategies, and storage configurations tailored to your workload.

> [!NOTE]
> For applications that require data separation at the database level, you can add more databases with postInitSQL commands and similar. It's currently not possible to add more databases in a declarative way with the CNPG operator. [Learn more](https://github.com/cloudnative-pg/cloudnative-pg) about the CNPG operator.

### Storage considerations

The type of storage you use can have large effects on PostgreSQL performance. Later in this guide, you select the option best suited for your goals and performance needs.

| Storage type | Compatible driver | Description  |
|-|-|-|
| [Premium SSD][pv1] | Azure Disks CSI driver | **Maximum data resiliency**. Azure Premium SSD delivers high-performance storage and seamlessly works with Azure Premium zone-redundant storage (ZRS). Premium SSD is provisioned based on specific sizes, which each offer certain IOPS and throughput levels. |
| [Premium SSD v2][pv2] | Azure Disks CSI driver | **Best price-performance**. Azure Premium SSD v2 offers higher performance than Azure Premium SSDs while also generally being less costly. Unlike Premium SSDs, Premium SSD v2 doesn't have dedicated sizes. You can set a Premium SSD v2 to any supported size you prefer, and make granular adjustments to the performance without downtime. Azure Premium SSD v2 disks have certain limitations that you should be aware of. For a complete list, see [Premium SSD v2 limitations][pv2-limitations]. |
| [Local NVMe or temp SSD (Ephemeral Disks)][ephemeral-disks] | Azure Container Storage only | **Maximum performance**. Ephemeral Disks are local NVMe and temporary SSD storage available on select VM families. They offer the highest possible IOPS, throughput, and submillisecond latency for your AKS cluster. You can also take advantage of Ephemeral Disks' high performance using [Azure Container Storage](https://learn.microsoft.com/en-us/azure/storage/container-storage/container-storage-introduction), a managed Kubernetes storage solution that dynamically provisions persistent volumes for stateful workloads like PostgreSQL. However, because these disks reside on the local VMs hosting the cluster, data isn't persisted to an Azure storage service. As a result, any data stored on these disks will be lost if the cluster is stopped or deallocated. To address this limitation, later sections in this guide show you how to set up periodic backups of your PostgreSQL data to [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/).|

## Next steps

> [Create PostgreSQL infrastructure][create-infrastructure]

## Contributors

*Microsoft maintains this article. The following contributors originally wrote it:*

* Ken Kilty | Principal TPM
* Russell de Pina | Principal TPM
* Adrian Joian | Senior Customer Engineer
* Jenny Hayes | Senior Content Developer
* Carol Smith | Senior Content Developer
* Erin Schaffer | Content Developer 2
* Adam Sharif | Customer Engineer 2

## Acknowledgment

This documentation was jointly developed with EnterpriseDB, the maintainers of the CloudNativePG operator. We thank [Gabriele Bartolini](https://cloudnative-pg.io/authors/gbartolini/) for reviewing earlier drafts of this document and offering technical improvements.  

[what-is-aks]: https://learn.microsoft.com/en-us/azure/aks/what-is-aks
[postgresql]: https://www.postgresql.org/
[core-kubernetes-concepts]: https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads
[azure-roles]: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
[jq]: https://jqlang.github.io/jq/
[install-kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
[install-helm]: https://helm.sh/docs/intro/install/
[install-openssl]: https://www.openssl.org/
[install-vscode]: https://code.visualstudio.com/Download
[install-krew]: https://krew.sigs.k8s.io/
[cnpg-plugin]: https://cloudnative-pg.io/documentation/current/kubectl-plugin/#using-krew
[create-infrastructure]: https://learn.microsoft.com/en-us/azure/aks/create-postgresql-ha
[pv1]: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types#premium-ssds
[pv2]: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types#premium-ssd-v2
[pv2-limitations]: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types#premium-ssd-v2-limitations
[ephemeral-disks]: https://learn.microsoft.com/en-us/azure/storage/container-storage/use-container-storage-with-local-disk#what-is-ephemeral-disk
