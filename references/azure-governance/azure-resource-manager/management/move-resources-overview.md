# Move Azure resources across resource groups, subscriptions, or regions.

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resources-overview  
> Microsoft doc last updated: 09/15/2025


Azure resources can be moved to a new resource group or subscription, or across regions.

## Move resources across resource groups or subscriptions

You can move Azure resources to either another Azure subscription or another resource group under the same subscription. You can use the Azure portal, Azure PowerShell, Azure CLI, or the REST API to move resources. To learn more, see [Move resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).

The move operation doesn't support moving resources to new [Microsoft Entra tenant](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant). If the tenant IDs for the source and destination subscriptions aren't the same, use the following methods to reconcile the tenant IDs:

* [Transfer ownership of an Azure subscription to another account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/billing-subscription-transfer)
* [How to associate or add an Azure subscription to Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory)

### Upgrade a subscription

If you actually want to upgrade your Azure subscription (such as switching from free to pay-as-you-go), you need to convert your subscription.

* To upgrade a free trial, see [Upgrade your Free Trial or Microsoft Imagine Azure subscription to pay-as-you-go](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/upgrade-azure-subscription).
* To change a pay-as-you-go account, see [Change your Azure pay-as-you-go subscription to a different offer](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/switch-azure-offer).

If you can't convert the subscription, [create an Azure support request](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/how-to-create-azure-support-request). Select **Subscription Management** for the issue type.

## Move resources across regions

Azure geographies, regions, and availability zones form the foundation of the Azure global infrastructure. Azure [geographies](https://azure.microsoft.com/global-infrastructure/geographies/) typically contain two or more [Azure regions](https://azure.microsoft.com/global-infrastructure/regions/). A region is an area within a geography, containing Availability Zones, and multiple data centers.

After you deploy resources to a specific Azure region, there are many reasons that you might want to move resources to a different region.

* **Align to a region launch**: Move your resources to a newly introduced Azure region that wasn't previously available.
* **Align for services/features**: Move resources to take advantage of services or features that are available in a specific region.
* **Respond to business developments**: Move resources to a region in response to business changes, such as mergers or acquisitions.
* **Align for proximity**: Move resources to a region local to your business.
* **Meet data requirements**: Move resources to align with data residency requirements, or data classification needs. [Learn more](https://azure.microsoft.com/mediahandler/files/resourcefiles/achieving-compliant-data-residency-and-security-with-azure/Achieving_Compliant_Data_Residency_and_Security_with_Azure.pdf).
* **Respond to deployment requirements**: Move resources that were deployed in error, or move in response to capacity needs.
* **Respond to decommissioning**: Move resources because of decommissioned regions.

### Move resources with Resource Mover

You can move resources to a different region with [Azure Resource Mover](https://learn.microsoft.com/en-us/azure/resource-mover/overview). Resource Mover provides:

* A single hub for moving resources across regions.
* Reduced move time and complexity. Everything you need is in a single location.
* A simple and consistent experience for moving different types of Azure resources.
* An easy way to identify dependencies across resources you want to move. This identification helps you to move related resources together, so that everything works as expected in the target region, after the move.
* Automatic cleanup of resources in the source region, if you want to delete them after the move.
* Testing. You can try out a move, and then discard it if you don't want to do a full move.

You can move resources to another region using a couple of different methods:

* **Start moving resources from a resource group**: With this method, you kick off the region move from within a resource group. After selecting the resources you want to move, the process continues in the Resource Mover hub, to check resource dependencies, and orchestrate the move process. [Learn more](https://learn.microsoft.com/en-us/azure/resource-mover/move-region-within-resource-group).
* **Start moving resources directly from the Resource Mover hub**: With this method, you kick off the region move process directly in the hub. [Learn more](https://learn.microsoft.com/en-us/azure/resource-mover/tutorial-move-region-virtual-machines).

### Move resources manually through redeployment

To move resources that aren't supported by Azure Resource Mover or to move any service manually, see [Azure services relocation guidance overview](https://learn.microsoft.com/en-us/azure/operational-excellence/overview-relocation).

As Microsoft continues to expand Azure global infrastructure and launch new Azure regions worldwide, there's an increasing number of options available for you to relocate your workloads into new regions. Region relocation options vary by service and by workload architecture. To successfully relocate a workload to another region, you need to plan your relocation strategy with an understanding of what each service in your workload requires and supports.

Azure region relocation documentation (Preview) contains service-specific relocation guidance for Azure products and services. The relocation documentation set is founded on both [Azure Cloud Adoption Framework - Relocate cloud workloads](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/relocate/) and the following Well-architected Framework (WAF) Operational Excellence principles:

* [Deploy with confidence](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/principles#deploy-with-confidence)
* [Adopt safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/principles#adopt-safe-deployment-practices)  

Each service specific guide can contain service-specific information on articles such as:

* [Service-relocation automation tools](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/relocate/select#select-service-relocation-automation).
* [Data relocation automation](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/relocate/select#select-data-relocation-automation).
* [Cutover approaches](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/relocate/select#select-cutover-approach).
* Possible and actual service dependencies that also require relocation planning.
* Lists of considerations, features, and limitations in relation to relocation planning for that service.
* Links to how-tos and relevant product-specific relocation information.

The following tables provide links to each Azure service relocation document. The tables also provide information on which kind of relocation method is supported.

#### Analytics

| Product  | Relocation | Relocation with data migration | Resource Mover |
| --- | --- | --- | ---|
|[Azure Event Hubs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-hub)| Y   | N| N |
|[Azure Event Hubs Cluster](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-hub-cluster)| Y | N  | N |
|[Azure Stream Analytics -  Stream Analytics jobs](../../stream-analytics/copy-job.md?toc=/azure/operational-excellence/toc.json)| Y | Y|  N  |
|[Azure Stream Analytics -  Stream Analytics cluster](../../stream-analytics/move-cluster.md?toc=/azure/operational-excellence/toc.json)|Y | Y|  N  |
|[Power BI](https://learn.microsoft.com/en-us/power-bi/admin/service-admin-region-move?toc=/azure/operational-excellence/toc.json)| Y |N | N |

#### Compute

| Product  | Relocation | Relocation with data migration | Resource Mover |
| --- | --- | --- | ---|
|[Azure App Service](../../app-service/manage-move-across-regions.md?toc=/azure/operational-excellence/toc.json)|Y  |  N| N |
|[Azure Batch](../../batch/account-move.md?toc=/azure/operational-excellence/toc.json)|Y | Y|  N  |
|[Azure Functions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-functions)|Y  |N  | N |
|[Azure Static Web Apps](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-static-web-apps) |  Y |N | N |
|[Azure Virtual Machines]( ../../resource-mover/tutorial-move-region-virtual-machines.md?toc=/azure/operational-excellence/toc.json)| N | N|  Y  |
|[Azure Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-virtual-machine-scale-sets)|N  |Y   | N |

#### Containers

| Product  | Relocation | Relocation with data migration | Resource Mover |
| --- | --- | --- | ---|
|[Azure Container Registry](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-container-registry)|Y | Y| N |
|[Azure Functions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-functions)|Y  |N  | N |
|[Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-kubernetes-service)|Y  |Y  | N |

#### Databases

| Product  | Relocation | Relocation with data migration | Resource Mover |
| --- | --- | --- | ---|
|[Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-moving-resources?toc=/azure/operational-excellence/toc.json)| Y |  N| N |
|[Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-cosmos-db)|Y | Y|  N  |
|[Azure Database for MariaDB Server](https://learn.microsoft.com/en-us/azure/mariadb/howto-move-regions-portal?toc=/azure/operational-excellence/toc.json)|Y | Y|  N  |
|[Azure Database for MySQL Server](https://learn.microsoft.com/en-us/azure/mysql/howto-move-regions-portal?toc=/azure/operational-excellence/toc.json)|Y | Y|  N  |
|[Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-postgresql-flexible-server)| Y | Y| N |

#### Integration

| Product  | Relocation |Relocation with data migration |  Resource Mover |
| --- | --- | --- | ---|
|[Azure API Management](../../api-management/api-management-howto-migrate.md?toc=/azure/operational-excellence/toc.json)| Y | Y|  N  |
|[Azure Logic apps](../../logic-apps/move-logic-app-resources.md?toc=/azure/operational-excellence/toc.json)|  Y| N | N |

#### Internet of Things

| Product  | Relocation |Relocation with data migration |  Resource Mover |
| --- | --- | --- | ---|
|[Azure API Management](../../api-management/api-management-howto-migrate.md?toc=/azure/operational-excellence/toc.json)| Y | Y|  N  |
|[Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-cosmos-db)|Y | Y|  N  |
|[Azure Event Grid domains](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-grid-domains)| Y | N| N |
|[Azure Event Grid custom topics](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-grid-custom-topics)| Y | N| N |
|[Azure Event Grid system topics](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-grid-system-topics)| Y | N| N |
|[Azure Functions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-functions)|Y  |N  | N |
|[Azure IoT Hub](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-how-to-clone?toc=/azure/operational-excellence/toc.json)| Y | Y|  N  |
|[Azure Stream Analytics -  Stream Analytics jobs](../../stream-analytics/copy-job.md?toc=/azure/operational-excellence/toc.json)| Y | Y|  N  |
|[Azure Stream Analytics -  Stream Analytics cluster](../../stream-analytics/move-cluster.md?toc=/azure/operational-excellence/toc.json)|Y | Y|  N  |

#### Management and governance

| Product  | Relocation |Relocation with data migration |  Resource Mover |
| --- | --- | --- | ---|
|[Azure Automation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-automation)| Y | Y| N |
|[Azure Backup](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-backup)| Y | N| N |
|[Azure Monitor - Log Analytics](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-log-analytics)| Y| N | N |
|[Azure Site Recovery (Recovery Services vaults)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-site-recovery)| Y | Y|  N  |

#### Networking

| Product  | Relocation |Relocation with data migration |  Resource Mover |
| --- | --- | --- | ---|
|[Azure Application Gateway and Web Application Firewall](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-app-gateway)| Y | N| N |
|[Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/move-across-regions-external-load-balancer-portal)| Y | Y| N |
|[Azure Private Link Service](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-private-link) | Y| N | N |
|[Azure Virtual Network](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-virtual-network)|  Y| N  | Y |
|[Azure Virtual Network - Network Security Groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-virtual-network-nsg)|Y  |N   | Y |

#### Security

| Product  | Relocation |Relocation with data migration |  Resource Mover |
| --- | --- | --- | ---|
|[Azure Firewall](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-firewall)|N | Y| N |
|[Azure Application Gateway and Web Application Firewall](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-app-gateway)| Y | N| N |
|[Azure Key Vault](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-key-vault)| Y | Y| N |
|[Managed identities for Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-storage-account)| Y| N | N |

#### Storage

| Product  | Relocation |Relocation with data migration |  Resource Mover |
| --- | --- | --- | ---|
|[Azure Backup](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-backup)| Y | N| N |
|[Azure NetApp Files](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-netapp)| Y | Y|  N  |
|[Azure Storage Account](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-storage-account)| Y | Y| N |

For more information, see the following articles:

* [Azure Resources Mover documentation](https://learn.microsoft.com/en-us/azure/resource-mover/)
* [Azure Resource Manager (ARM) documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/)

### Move resources from non availability zone to availability zone support

To move resources from a region that doesn't support availability zones to one that does, see [Availability zone migration guidance overview for Microsoft Azure products and services](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-migration-overview).

## Next steps

* To check if a resource type supports being moved, see [Move operation support for resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-support-resources).
* To learn more about the region move process, see [About the move process](https://learn.microsoft.com/en-us/azure/resource-mover/about-move-process).
* To learn more deeply about service relocation and planning recommendations, see [Relocated cloud workloads](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/relocate/).
