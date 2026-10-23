# Relocate Azure Private Link Service to another region

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-private-link  
> Microsoft doc last updated: 09/15/2025


This article shows you how to relocate [Azure Private Link Service](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) when moving your workload to another region.

There are various reasons why you may want to move your existing Azure resources from one region to another. You may want to:

- Take advantage of a new Azure region.
- Deploy features or services available in specific regions only.
- Meet internal policy and governance requirements.
- Align with company mergers and acquisitions
- Meet capacity planning requirements.

To learn how to reconfigure [private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) for a particular service, see the [appropriate service relocation guide](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resources-overview).

## Downtime

To understand the possible downtimes involved, see [Cloud Adoption Framework for Azure: Select a relocation method](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/relocate/select#select-a-relocation-method).

## Prepare

Identify all resources that are used by Private Link Service, such as Standard load balancer, virtual machines, virtual network, etc.

## Redeploy

1. Redeploy all resources that are used by Private Link Service.
1. Ensure that a standard load balancer with all dependent resources is relocated to the target region.
1. Create a Private Link Service that references the relocated load balancer. To create the Private Link, you can use the [Azure portal](https://learn.microsoft.com/en-us/azure/private-link/create-private-link-service-portal), [PowerShell](https://learn.microsoft.com/en-us/azure/private-link/create-private-link-service-powershell), or [Azure CLI](https://learn.microsoft.com/en-us/azure/private-link/create-private-link-service-cli).

    In the load balancer selection process:
        - Choose the frontend IP configuration where you want to receive the traffic.
        - Choose a subnet for NAT IP addresses for the Private Link Service.
        - Choose Private Link Service settings that are the same as the source Private Link Service.

1. Redeploy the private endpoint into the relocated virtual network.
1. Configure your DNS settings by following guidance in [Private DNS zone values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns?branch=main).

    

## Next steps

To learn more about moving resources between regions and disaster recovery in Azure, refer to:

- [Move resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription)
- [Move Azure VMs to another region](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-migrate)
