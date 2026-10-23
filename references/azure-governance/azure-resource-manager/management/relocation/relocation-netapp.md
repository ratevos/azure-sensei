# Relocate an Azure NetApp Files volume to another region

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-netapp  
> Microsoft doc last updated: 09/15/2025


This article covers guidance for relocating [Azure NetApp Files](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-introduction) volumes to another region.

There are various reasons why you may want to move your existing Azure resources from one region to another. You may want to:

- Take advantage of a new Azure region.
- Deploy features or services available in specific regions only.
- Meet internal policy and governance requirements.
- Align with company mergers and acquisitions
- Meet capacity planning requirements.

## Prerequisites

Before you begin the relocation planning stage, review the following prerequisites:

- The target NetApp account should already be created.
- Source and target regions must be paired regions. To see if they're paired, see [Supported cross-region replication pairs](../../../azure-netapp-files/cross-region-replication-introduction.md?#supported-region-pairs).
- Understand all dependent resources. Some of the resources could be:

  - [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/azure-netapp-files/understand-guidelines-active-directory-domain-service-site)
  - [Virtual Network](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-virtual-network)
  - Azure DNS
  - [Storage services](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-storage-account)
  - [Capacity pools](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-set-up-capacity-pool)
  
## Prepare

Before you begin the relocation process, complete the following preparations:

- The target Microsoft Entra ID connection must have access to the DNS servers, AD DS Domain Controllers, or Microsoft Entra Domain Services Domain Controllers that are reachable from the delegated subnet in the target region.

- The network configurations (including separate subnets if needed and IP ranges) should already be planned and prepared.

- Disable replication to the disaster recovery region. If you've established a disaster recovery (DR) solution using replication to a DR region, turn off replication to the DR site before initiating relocation procedures.

- Understand the following considerations in regards to replication:

  - SMB, NFS, and dual-protocol volumes are supported. Replication of SMB volumes requires a Microsoft Entra ID connection in the source and target NetApp accounts.
  - The replication destination volume is read-only until the entire move is complete.
  - Azure NetApp Files replication doesn't currently support multiple subscriptions. All replications must be performed under a single subscription.
  - There are resource limits for the maximum number of cross-region replication destination volumes. For more information, see [Resource limits for Azure NetApp Files](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-resource-limits).

## Redeploy

**To redeploy your NetApp resources:**

1. [Create the target NetApp account](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-create-netapp-account).
1. [Create the target capacity pool](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-set-up-capacity-pool).
1. [Delegate a subnet in the target region](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-delegate-subnet). Azure NetApp Files creates a system route to the delegated subnet. Peering and endpoints can be used to connect to the target as needed.
1. Create a data replication volume by following the directions in [Create volume replication for Azure NetApp Files](https://learn.microsoft.com/en-us/azure/azure-netapp-files/cross-region-replication-create-peering).
1. [Verify that the health status](https://learn.microsoft.com/en-us/azure/azure-netapp-files/cross-region-replication-display-health-status) of replication is healthy.

## Cleanup

Once the replication is complete, you can safely delete the replication peering the source volume.

To learn how to clean up a replication, see [Delete volume replications or volumes](https://learn.microsoft.com/en-us/azure/azure-netapp-files/cross-region-replication-delete).

## Related content

- [Cross-region replication of Azure NetApp Files volumes](https://learn.microsoft.com/en-us/azure/azure-netapp-files/cross-region-replication-introduction)

To learn more about moving resources between regions and disaster recovery in Azure, refer to:

- [Requirements for Active Directory Connections](https://learn.microsoft.com/en-us/azure/azure-netapp-files/create-active-directory-connections#requirements-for-active-directory-connections)
- [Guidelines for Azure NetApp Files network planning](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-network-topologies)
- [Fail over to the destination region](https://learn.microsoft.com/en-us/azure/azure-netapp-files/cross-region-replication-manage-disaster-recovery#fail-over-to-destination-volume)
- [Move resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)
- [Move Azure VMs to another region](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-migrate)
