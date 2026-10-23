# Azure permissions - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations  
> Microsoft doc last updated: 07/01/2026


This article lists the permissions for Azure resource providers, which are used in built-in roles. You can use these permissions in your own [Azure custom roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles) to provide granular access control to resources in Azure. The permissions are always evolving. To get the latest permissions, use [Get-AzProviderOperation](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azprovideroperation) or [az provider operation list](https://learn.microsoft.com/en-us/cli/azure/provider/operation#az-provider-operation-list).

Click the resource provider name in the following list to see the list of permissions.

## General

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.Addons](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftaddons) |  | core |
> | [Microsoft.Capacity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcapacity) |  | core |
> | [Microsoft.Commerce](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftcommerce) |  | core |
> | [Microsoft.Marketplace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftmarketplace) |  | core |
> | [Microsoft.MarketplaceOrdering](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftmarketplaceordering) |  | core |
> | [Microsoft.Quota](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftquota) |  | [Azure Quotas](https://learn.microsoft.com/en-us/azure/quotas/quotas-overview) |
> | [Microsoft.Subscription](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsubscription) |  | core |
> | [Microsoft.Support](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/general#microsoftsupport) |  | core |

## Compute

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [microsoft.app](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftapp) |  | [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/) |
> | [Microsoft.AppPlatform](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftappplatform) | A fully managed Spring Cloud service, built and operated with Pivotal. | [Azure Spring Apps](https://learn.microsoft.com/en-us/azure/spring-apps/) |
> | [Microsoft.AVS](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftavs) |  | [Azure VMware Solution](https://learn.microsoft.com/en-us/azure/azure-vmware/introduction) |
> | [Microsoft.AzureFleet](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftazurefleet) |  | [Azure Compute Fleet](https://learn.microsoft.com/en-us/azure/azure-compute-fleet/overview) |
> | [Microsoft.Batch](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftbatch) | Cloud-scale job scheduling and compute management. | [Batch](https://learn.microsoft.com/en-us/azure/batch/) |
> | [Microsoft.Compute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcompute) | Access cloud compute capacity and scale on demand (such as virtual machines) and only pay for the resources you use. | [Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/)<br/>[Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/) |
> | [Microsoft.ComputeLimit](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcomputelimit) |  |  |
> | [Microsoft.ComputeSchedule](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftcomputeschedule) |  | [Azure Virtual Desktop](https://learn.microsoft.com/en-us/azure/virtual-desktop/overview) |
> | [microsoft.connectedvmwarevsphere](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftconnectedvmwarevsphere) |  | [Azure Arc-enabled VMware vSphere](https://learn.microsoft.com/en-us/azure/azure-arc/vmware-vsphere/) |
> | [Microsoft.DesktopVirtualization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftdesktopvirtualization) | The best virtual desktop experience, delivered on Azure. | [Azure Virtual Desktop](https://learn.microsoft.com/en-us/azure/virtual-desktop/) |
> | [Microsoft.Quantum](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftquantum) |  | [Azure Quantum](https://learn.microsoft.com/en-us/azure/quantum/overview-azure-quantum) |
> | [Microsoft.ServiceFabric](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute#microsoftservicefabric) | Develop microservices and orchestrate containers on Windows or Linux. | [Service Fabric](https://learn.microsoft.com/en-us/azure/service-fabric/) |

## Networking

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.Cdn](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftcdn) | Ensure secure, reliable content delivery with broad global reach. | [Content Delivery Network](https://learn.microsoft.com/en-us/azure/cdn/) |
> | [Microsoft.Network](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/networking#microsoftnetwork) | Connect cloud and on-premises infrastructure and services to provide your customers and users the best possible experience. | [Application Gateway](https://learn.microsoft.com/en-us/azure/application-gateway/)<br />[Azure Bastion](https://learn.microsoft.com/en-us/azure/bastion/)<br />[Azure DDoS Protection](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview)<br />[Azure DNS](https://learn.microsoft.com/en-us/azure/dns/)<br />[Azure ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/)<br />[Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/)<br />[Azure Front Door Service](https://learn.microsoft.com/en-us/azure/frontdoor/)<br />[Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/)<br />[Azure Route Server](https://learn.microsoft.com/en-us/azure/route-server/)<br />[Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/)<br />[Network Watcher](https://learn.microsoft.com/en-us/azure/network-watcher/)<br />[Traffic Manager](https://learn.microsoft.com/en-us/azure/traffic-manager/)<br />[Virtual Network](https://learn.microsoft.com/en-us/azure/virtual-network/)<br />[Virtual Network NAT](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview)<br />[Virtual Network Manager](https://learn.microsoft.com/en-us/azure/virtual-network-manager/overview)<br />[Virtual WAN](https://learn.microsoft.com/en-us/azure/virtual-wan/)<br />[VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/) |

## Storage

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.DataShare](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftdatashare) | A simple and safe service for sharing big data with external organizations. | [Azure Data Share](https://learn.microsoft.com/en-us/azure/data-share/) |
> | [Microsoft.ElasticSan](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftelasticsan) |  | [Azure Elastic SAN](https://learn.microsoft.com/en-us/azure/storage/elastic-san/) |
> | [Microsoft.NetApp](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftnetapp) | Enterprise-grade Azure file shares, powered by NetApp. | [Azure NetApp Files](https://learn.microsoft.com/en-us/azure/azure-netapp-files/) |
> | [Microsoft.Storage](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstorage) | Get secure, massively scalable cloud storage for your data, apps, and workloads. | [Storage](https://learn.microsoft.com/en-us/azure/storage/) |
> | [Microsoft.StorageCache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstoragecache) | File caching and Lustre file system capabilities for high-performance computing (HPC). | [Azure HPC Cache](https://learn.microsoft.com/en-us/azure/hpc-cache/)<br/>[Azure Managed Lustre](https://learn.microsoft.com/en-us/azure/azure-managed-lustre/) |
> | [Microsoft.StorageSync](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/storage#microsoftstoragesync) |  | [Storage](https://learn.microsoft.com/en-us/azure/storage/) |

## Web and Mobile

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.CertificateRegistration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/web-and-mobile#microsoftcertificateregistration) | Allow an application to use its own credentials for authentication. | [App Service Certificates](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate#buy-and-import-app-service-certificate) |
> | [Microsoft.DomainRegistration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/web-and-mobile#microsoftdomainregistration) |  | [App Service](https://learn.microsoft.com/en-us/azure/app-service/) |
> | [Microsoft.Maps](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/web-and-mobile#microsoftmaps) | Simple and secure location APIs provide geospatial context to data. | [Azure Maps](https://learn.microsoft.com/en-us/azure/azure-maps/) |
> | [Microsoft.SignalRService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/web-and-mobile#microsoftsignalrservice) | Add real-time web functionalities easily. | [Azure SignalR Service](https://learn.microsoft.com/en-us/azure/azure-signalr/) |
> | [microsoft.web](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/web-and-mobile#microsoftweb) | Quickly create and deploy mission critical web apps at scale. | [App Service](https://learn.microsoft.com/en-us/azure/app-service/)<br/>[Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/) |

## Containers

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.ContainerInstance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/containers#microsoftcontainerinstance) | Easily run containers on Azure without managing servers. | [Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/) |
> | [Microsoft.ContainerRegistry](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/containers#microsoftcontainerregistry) | Store and manage container images across all types of Azure deployments. | [Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/) |
> | [Microsoft.ContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/containers#microsoftcontainerservice) | Accelerate your containerized application development without compromising security. | [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/intro-kubernetes) |
> | [Microsoft.RedHatOpenShift](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/containers#microsoftredhatopenshift) |  | [Azure Red Hat OpenShift](https://learn.microsoft.com/en-us/azure/openshift/) |

## Databases

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.Cache](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftcache) | Power applications with high-throughput, low-latency data access. | [Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/), [Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/) |
> | [Microsoft.DBforMariaDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbformariadb) | Managed MariaDB database service for app developers. | [Azure Database for MariaDB](https://learn.microsoft.com/en-us/azure/mariadb/) |
> | [Microsoft.DBforMySQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbformysql) | Managed MySQL database service for app developers. | [Azure Database for MySQL](https://learn.microsoft.com/en-us/azure/mysql/) |
> | [Microsoft.DBforPostgreSQL](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdbforpostgresql) | Managed PostgreSQL database service for app developers. | [Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/) |
> | [Microsoft.DocumentDB](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftdocumentdb) | A NoSQL document database-as-a-service. | [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/) |
> | [Microsoft.InferenceService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftinferenceservice) |  |  |
> | [Microsoft.Sql](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsql) | Managed, intelligent SQL in the cloud. | [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/index)<br/>[Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/index)<br/>[Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/) |
> | [Microsoft.SqlVirtualMachine](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/databases#microsoftsqlvirtualmachine) | Host enterprise SQL Server apps in the cloud. | [SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview) |

## Analytics

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.AnalysisServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftanalysisservices) | Enterprise-grade analytics engine as a service. | [Azure Analysis Services](https://learn.microsoft.com/en-us/azure/analysis-services/index) |
> | [Microsoft.Databricks](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftdatabricks) | Fast, easy, and collaborative Apache Spark-based analytics platform. | [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/) |
> | [Microsoft.DataFactory](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftdatafactory) | Hybrid data integration at enterprise scale, made easy. | [Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/) |
> | [Microsoft.DataLakeAnalytics](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftdatalakeanalytics) | Distributed analytics service that makes big data easy. | [Data Lake Analytics](https://learn.microsoft.com/en-us/azure/data-lake-analytics/) |
> | [Microsoft.DataLakeStore](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftdatalakestore) | Highly scalable and cost-effective data lake solution for big data analytics. | [Azure Data Lake Storage Gen2](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) |
> | [Microsoft.Fabric](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftfabric) | Unified analytics platform for data engineering, data science, and business intelligence. | [Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/) |
> | [Microsoft.HDInsight](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsofthdinsight) | Provision cloud Hadoop, Spark, R Server, HBase, and Storm clusters. | [HDInsight](https://learn.microsoft.com/en-us/azure/hdinsight/) |
> | [Microsoft.Kusto](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftkusto) | Service for storing and running interactive analytics over Big Data. | [Azure Data Explorer](https://learn.microsoft.com/en-us/azure/data-explorer/) |
> | [Microsoft.PowerBIDedicated](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftpowerbidedicated) | Manage Power BI Premium dedicated capacities for exclusive use by an organization. | [Power BI Embedded](https://learn.microsoft.com/en-us/azure/power-bi-embedded/) |
> | [Microsoft.Purview](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftpurview) | Unified data governance and compliance solution. | [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) |
> | [Microsoft.Synapse](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/analytics#microsoftsynapse) | Limitless analytics service with enterprise data warehousing and big data analytics. | [Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/) |

## AI + machine learning

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.BotService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/ai-machine-learning#microsoftbotservice) | Intelligent, serverless bot service that scales on demand. | [Azure Bot Service](https://learn.microsoft.com/en-us/azure/bot-service/) |
> | [Microsoft.CognitiveServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/ai-machine-learning#microsoftcognitiveservices) | Add smart API capabilities to enable contextual interactions. | [Cognitive Services](https://learn.microsoft.com/en-us/azure/cognitive-services/) |
> | [Microsoft.HealthBot](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/ai-machine-learning#microsofthealthbot) |  | [Azure AI Health Bot](https://learn.microsoft.com/en-us/azure/health-bot/overview) |
> | [Microsoft.MachineLearningServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/ai-machine-learning#microsoftmachinelearningservices) | Enterprise-grade machine learning service to build and deploy models faster. | [Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/) |
> | [Microsoft.Search](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/ai-machine-learning#microsoftsearch) | Leverage search services and get comprehensive results. | [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/) |
> | [Microsoft.VideoIndexer](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/ai-machine-learning#microsoftvideoindexer) | Extract the insights from your videos using Azure AI Video Indexer video and audio models. | [Azure AI Video Indexer](https://learn.microsoft.com/en-us/azure/azure-video-indexer/) |

## Internet of Things

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.AzureSphere](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftazuresphere) |  | [Azure Sphere](https://learn.microsoft.com/en-us/azure-sphere/product-overview/what-is-azure-sphere) |
> | [Microsoft.DeviceRegistry](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftdeviceregistry) |  |  |
> | [Microsoft.Devices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftdevices) | Ensure that your users are accessing your resources from devices that meet your standards for security and compliance. | [IoT Hub](https://learn.microsoft.com/en-us/azure/iot-hub/)<br/>[IoT Hub Device Provisioning Service](https://learn.microsoft.com/en-us/azure/iot-dps/) |
> | [Microsoft.DeviceUpdate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftdeviceupdate) |  | [Device Update for IoT Hub](https://learn.microsoft.com/en-us/azure/iot-hub-device-update/) |
> | [Microsoft.DigitalTwins](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftdigitaltwins) |  | [Azure Digital Twins](https://learn.microsoft.com/en-us/azure/digital-twins/) |
> | [Microsoft.Edge](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedge) |  |  |
> | [Microsoft.EdgeMarketPlace](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftedgemarketplace) |  |  |
> | [Microsoft.IoTCentral](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftiotcentral) | Experience the simplicity of SaaS for IoT, with no cloud expertise required. | [IoT Central](https://learn.microsoft.com/en-us/azure/iot-central/) |
> | [Microsoft.IoTFirmwareDefense](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftiotfirmwaredefense) |  | [Microsoft Defender for IoT](https://learn.microsoft.com/en-us/azure/defender-for-iot/device-builders/overview) |
> | [Microsoft.IoTSecurity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftiotsecurity) |  | [IoT security](https://learn.microsoft.com/en-us/azure/iot/iot-security-architecture) |
> | [Microsoft.StreamAnalytics](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/internet-of-things#microsoftstreamanalytics) | Real-time data stream processing from millions of IoT devices. | [Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/) |

## Integration

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.ApiCenter](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftapicenter) |  | [Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/overview) |
> | [Microsoft.ApiManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftapimanagement) | Easily build and consume Cloud APIs. | [API Management](https://learn.microsoft.com/en-us/azure/api-management/) |
> | [Microsoft.AppConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftappconfiguration) | Fast, scalable parameter storage for app configuration. | [Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/) |
> | [Microsoft.Communication](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftcommunication) |  | [Azure Communication Services](https://learn.microsoft.com/en-us/azure/communication-services/overview) |
> | [Microsoft.DurableTask](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftdurabletask) |  | [Durable Functions](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview) |
> | [Microsoft.EventGrid](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventgrid) | Get reliable event delivery at massive scale. | [Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/) |
> | [Microsoft.EventHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofteventhub) | Receive telemetry from millions of devices. | [Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/) |
> | [Microsoft.HealthcareApis](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofthealthcareapis) |  | [Azure API for FHIR](https://learn.microsoft.com/en-us/azure/healthcare-apis/azure-api-for-fhir/) |
> | [Microsoft.HealthDataAIServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsofthealthdataaiservices) |  | [Azure Health Data Services](https://learn.microsoft.com/en-us/azure/healthcare-apis/healthcare-apis-overview) |
> | [Microsoft.Logic](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftlogic) | Automate the access and use of data across clouds without writing code. | [Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/) |
> | [Microsoft.NotificationHubs](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftnotificationhubs) | Send push notifications to any platform from any back end. | [Notification Hubs](https://learn.microsoft.com/en-us/azure/notification-hubs/) |
> | [Microsoft.Relay](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftrelay) | Expose services that run in your corporate network to the public cloud. | [Azure Relay](https://learn.microsoft.com/en-us/azure/azure-relay/relay-what-is-it) |
> | [Microsoft.ResourceNotifications](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftresourcenotifications) |  | [Azure Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview) |
> | [Microsoft.ServiceBus](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftservicebus) | Connect across private and public cloud environments. | [Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/) |
> | [Microsoft.ServicesHub](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/integration#microsoftserviceshub) |  | [Services Hub](https://learn.microsoft.com/en-us/services-hub/) |

## Identity

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.AAD](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaad) | Join Azure virtual machines to a domain without domain controllers. | [Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/) |
> | [microsoft.aadiam](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftaadiam) |  |  |
> | [Microsoft.ADHybridHealthService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftadhybridhealthservice) | Robust monitoring of your on-premises identity infrastructure. | [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/) |
> | [Microsoft.AzureActiveDirectory](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftazureactivedirectory) | Synchronize on-premises directories and enable single sign-on. | [Azure Active Directory B2C](https://learn.microsoft.com/en-us/azure/active-directory-b2c/) |
> | [Microsoft.ManagedIdentity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/identity#microsoftmanagedidentity) | An automatically managed identity in Microsoft Entra ID that authenticates to any service that supports Microsoft Entra | [Managed identities for Azure resources](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/) |

## Security

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.AppComplianceAutomation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftappcomplianceautomation) |  | [App Compliance Automation Tool for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365-app-certification/docs/acat-overview) |
> | [Microsoft.Attestation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftattestation) |  | Azure Attestation Service |
> | [Microsoft.DataProtection](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftdataprotection) |  | Data Protection |
> | [Microsoft.KeyVault](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftkeyvault) | Safeguard and maintain control of keys and other secrets. | [Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/) |
> | [Microsoft.Security](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftsecurity) | Protect your enterprise from advanced threats across hybrid cloud workloads. | [Security Center](https://learn.microsoft.com/en-us/azure/security-center/) |
> | [Microsoft.SecurityInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/security#microsoftsecurityinsights) |  | [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/) |

## DevOps

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.Chaos](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/devops#microsoftchaos) |  | [Azure Chaos Studio](https://learn.microsoft.com/en-us/azure/chaos-studio/) |
> | [Microsoft.DevCenter](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/devops#microsoftdevcenter) |  | [Azure Deployment Environments](https://learn.microsoft.com/en-us/azure/deployment-environments/overview-what-is-azure-deployment-environments) |
> | [Microsoft.DevOpsInfrastructure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/devops#microsoftdevopsinfrastructure) |  | [Managed DevOps Pools](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/overview) |
> | [Microsoft.DevTestLab](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/devops#microsoftdevtestlab) | Quickly create environments using reusable templates and artifacts. | [Azure Lab Services](https://learn.microsoft.com/en-us/azure/lab-services/) |
> | [Microsoft.LabServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/devops#microsoftlabservices) | Set up labs for classrooms, trials, development and testing, and other scenarios. | [Azure Lab Services](https://learn.microsoft.com/en-us/azure/lab-services/) |
> | [Microsoft.LoadTestService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/devops#microsoftloadtestservice) |  | [Azure Load Testing](https://learn.microsoft.com/en-us/azure/load-testing/) |
> | [Microsoft.VisualStudio](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/devops#microsoftvisualstudio) | The powerful and flexible environment for developing applications in the cloud. | [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/) |

## Migration

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.DataBox](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftdatabox) | Move stored or in-flight data to Azure quickly and cost-effectively. | [Azure Data Box](https://learn.microsoft.com/en-us/azure/databox/) |
> | [Microsoft.DataBoxEdge](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftdataboxedge) | Appliances and solutions for data transfer to Azure and edge compute. | [Azure Stack Edge](https://learn.microsoft.com/en-us/azure/databox-online/azure-stack-edge-overview) |
> | [Microsoft.DataMigration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftdatamigration) | Simplify on-premises database migration to the cloud. | [Azure Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/) |
> | [Microsoft.Migrate](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftmigrate) | Easily discover, assess, right-size, and migrate your on-premises VMs to Azure. | [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) |
> | [Microsoft.OffAzure](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/migration#microsoftoffazure) |  | [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) |

## Monitor

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.AlertsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftalertsmanagement) | Analyze all of the alerts in your Log Analytics repository. | [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/) |
> | [Microsoft.Dashboard](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftdashboard) |  | [Azure Managed Grafana](https://learn.microsoft.com/en-us/azure/managed-grafana/) |
> | [Microsoft.Insights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftinsights) | Full observability into your applications, infrastructure, and network. | [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/) |
> | [microsoft.monitor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftmonitor) |  | [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/) |
> | [Microsoft.OperationalInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationalinsights) |  | [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/) |
> | [Microsoft.OperationsManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/monitor#microsoftoperationsmanagement) | A simplified management solution for any enterprise. | [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/) |

## Management and governance

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.Advisor](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftadvisor) | Your personalized Azure best practices recommendation engine. | [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/) |
> | [Microsoft.Authorization](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftauthorization) |  | [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)<br/>[Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)<br/>[Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/) |
> | [Microsoft.Automation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftautomation) | Simplify cloud management with process automation. | [Automation](https://learn.microsoft.com/en-us/azure/automation/) |
> | [Microsoft.Billing](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbilling) | Manage your subscriptions and see usage and billing. | [Cost Management + Billing](https://learn.microsoft.com/en-us/azure/cost-management-billing/) |
> | [Microsoft.BillingBenefits](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftbillingbenefits) |  | [Azure savings plans](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-overview) |
> | [Microsoft.Blueprint](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftblueprint) | Enabling quick, repeatable creation of governed environments. | [Azure Blueprints](https://learn.microsoft.com/en-us/azure/governance/blueprints/) |
> | [Microsoft.Carbon](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcarbon) |  | [Azure carbon optimization](https://learn.microsoft.com/en-us/azure/carbon-optimization/overview) |
> | [Microsoft.Consumption](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftconsumption) | Programmatic access to cost and usage data for your Azure resources. | [Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/) |
> | [Microsoft.CostManagement](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcostmanagement) | Optimize what you spend on the cloud, while maximizing cloud potential. | [Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/) |
> | [Microsoft.CustomerLockbox](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftcustomerlockbox) | Interface for customers to review and approve or reject customer data access requests. | [Customer Lockbox for Microsoft Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/customer-lockbox-overview) |
> | [Microsoft.Features](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftfeatures) |  | [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/) |
> | [Microsoft.GuestConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftguestconfiguration) | Audit settings inside a machine using Azure Policy. | [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/) |
> | [Microsoft.Intune](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftintune) | Enable your workforce to be productive on all their devices, while keeping your organization's information protected. |  |
> | [Microsoft.Maintenance](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmaintenance) |  | [Azure Maintenance](https://learn.microsoft.com/en-us/azure/virtual-machines/maintenance-configurations)<br/>[Azure Update Manager](https://learn.microsoft.com/en-us/azure/update-manager/overview) |
> | [Microsoft.ManagedOps](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedops) |  |  |
> | [Microsoft.ManagedServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagedservices) |  | [Azure Lighthouse](https://learn.microsoft.com/en-us/azure/lighthouse/) |
> | [Microsoft.Management](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftmanagement) | Use management groups to efficiently apply governance controls and manage groups of Azure subscriptions. | [Management Groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/) |
> | [Microsoft.PolicyInsights](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftpolicyinsights) | Summarize policy states for the subscription level policy definition. | [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/) |
> | [Microsoft.Portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftportal) | Build, manage, and monitor all Azure products in a single, unified console. | [Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/) |
> | [Microsoft.RecoveryServices](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftrecoveryservices) | Hold and organize backup data for various Azure services such as IaaS VMs (Linux or Windows) and Azure SQL databases. | [Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/) |
> | [Microsoft.ResourceGraph](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcegraph) | Powerful tool to query, explore, and analyze your cloud resources at scale. | [Azure Resource Graph](https://learn.microsoft.com/en-us/azure/governance/resource-graph/) |
> | [Microsoft.ResourceHealth](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresourcehealth) | Diagnose and get support for service problems that affect your Azure resources. | [Azure Service Health](https://learn.microsoft.com/en-us/azure/service-health/) |
> | [Microsoft.Resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftresources) | Deployment and management service for Azure that enables you to create, update, and delete resources in your Azure subscription. | [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/) |
> | [Microsoft.Solutions](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftsolutions) | Find the solution to meet the needs of your application or business. | [Azure Managed Applications](https://learn.microsoft.com/en-us/azure/azure-resource-manager/managed-applications/) |
> | [Microsoft.Workloads](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/management-and-governance#microsoftworkloads) |  | [SAP on Azure](https://learn.microsoft.com/en-us/azure/sap/) |

## Hybrid + multicloud

> | Resource provider | Description | Azure service |
> | --- | --- | --- |
> | [Microsoft.AzureStack](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestack) | Build and run innovative hybrid applications across cloud boundaries. | [Azure Stack](https://learn.microsoft.com/en-us/azure-stack/) |
> | [Microsoft.AzureStackHCI](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftazurestackhci) |  | [Azure Local](https://learn.microsoft.com/en-us/azure-stack/hci/) |
> | [Microsoft.ExtendedLocation](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftextendedlocation) |  | [Custom locations](https://learn.microsoft.com/en-us/azure/azure-arc/platform/conceptual-custom-locations) |
> | [Microsoft.HybridCompute](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcompute) |  | [Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/) |
> | [Microsoft.HybridConnectivity](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridconnectivity) |  |  |
> | [Microsoft.HybridContainerService](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsofthybridcontainerservice) |  |  |
> | [Microsoft.Kubernetes](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetes) |  | [Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview) |
> | [Microsoft.KubernetesConfiguration](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftkubernetesconfiguration) |  | [Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/overview) |
> | [Microsoft.ResourceConnector](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftresourceconnector) |  |  |
> | [Microsoft.SCVMM](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/hybrid-multicloud#microsoftscvmm) |  | [Azure Arc-enabled System Center Virtual Machine Manager (SCVMM)](https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/overview) |

## Next steps

- [Match resource provider to service](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-services-resource-providers)
- [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)
- [Cloud Adoption Framework: Resource access management in Azure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management)
