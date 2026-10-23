# Azure subscription and service limits, quotas, and constraints

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits  
> Microsoft doc last updated: 08/04/2026


This document lists some of the most common Microsoft Azure limits, which are also sometimes called quotas.

- To learn more about Azure pricing, see the [Azure pricing](https://azure.microsoft.com/pricing/) overview and details page.
- The Azure pricing page provides details for specific services; for example, [Windows Virtual Machines](https://azure.microsoft.com/pricing/details/virtual-machines/Windows/).
- You can also use the Azure [pricing calculator](https://azure.microsoft.com/pricing/calculator/) to estimate your costs.
- See [What is Microsoft Billing?](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) for tips to help manage your costs.

## How to manage limits

> [!NOTE]
> Some services have adjustable limits.
>
> When the limit can be adjusted, the tables include **Default limit** and **Maximum limit** headers. The limit can be raised above the default limit but not above the maximum limit. Some services with adjustable limits use different headers with information about adjusting the limit.
>
> When a service doesn't have adjustable limits, the following tables use the header **Limit** without any additional information about adjusting the limit. In those cases, the default and the maximum limits are the same.
>
> If you want to raise the limit or quota above the default limit, [open an online customer support request at no charge](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/error-resource-quota#solution).
>
> The terms *soft limit* and *hard limit* are often used informally to describe the current, adjustable limit (soft limit) and the maximum limit (hard limit). If a limit isn't adjustable, there won't be a soft limit but only a hard limit.
>

[Free Azure trial subscriptions](https://azure.microsoft.com/pricing/offers/ms-azr-0044p?cid=msft_learn) aren't eligible for limit or quota increases. If you have this type of subscription, you can upgrade to a [Pay-as-you-go](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn) one. For more information, see [Upgrade your Azure account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/upgrade-azure-subscription) and the overviews for [Try Azure for free or pay as you go](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

Some limits are managed at a regional level. You decide what your quotas must be for your workload in any one region, and then request that amount for each region into which you want to deploy.

For example, with virtual central processing unit (vCPU) quotas:

- To request a quota increase with support for vCPUs, you decide how many vCPUs to use in which regions.
- You then request an increase in vCPU quotas for the amounts and regions that you want.
- If you need to use 30 vCPUs in West Europe to run your application there, you specifically request 30 vCPUs in West Europe.
- Your vCPU quota doesn't increase in any other region; only West Europe has the 30-vCPU quota.

See [Resolve errors for resource quotas](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/error-resource-quota) for more information about how to determine quotas for specific regions.

## General limits

- See [Naming rules and restrictions for Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules) for limits on resource names.
- See [Understand how Azure Resource Manager throttles requests](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling) to learn about Resource Manager API read and write limits.

### Azure management group limits

The following limits apply to [Azure management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).

|                                                           Resource                                                            |                Limit                 |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Management groups per Microsoft Entra tenant                                                                                  | 10,000                               |
| Subscriptions per management group                                                                                            | Unlimited                            |
| Levels of management group hierarchy                                                                                          | Root level plus 6 levels<sup>1</sup> |
| Direct parent management group per management group                                                                           | One                                  |
| [Management group level deployments](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-management-group)              | 800<sup>2</sup>                      |
| Locations of [Management group level deployments](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-management-group) | 10                                   |

<sup>1</sup>The 6 levels don't include the subscription level.

<sup>2</sup>If you reach the limit of 800 deployments, delete deployments from the history that are no longer needed. To delete management group level deployments, use [Remove-AzManagementGroupDeployment](https://learn.microsoft.com/en-us/powershell/module/az.resources/Remove-AzManagementGroupDeployment) or [az deployment mg delete](https://learn.microsoft.com/en-us/cli/azure/deployment/mg#az-deployment-mg-delete). Deployments are automatically deleted from the history as you near the limit. Deleting an entry from the deployment history doesn't affect the deployed resources. For more information, see [Automatic deletions from deployment history](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history-deletions).

### Azure subscription limits

The following limits apply when you use Azure Resource Manager and Azure resource groups.

|                                                                           Resource                                                                           |      Limit      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| Azure subscriptions [associated with a Microsoft Entra tenant](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory) | Unlimited       |
| [Coadministrators](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/add-change-subscription-administrator) per subscription                                             | Unlimited       |
| [Resource groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) per subscription                                                                        | 980             |
| Azure Resource Manager API request size                                                                                                                      | 4,194,304 bytes |
| Tags per subscription<sup>1</sup>                                                                                                                            | 50              |
| Unique tag calculations per subscription<sup>2</sup>                                                                                                         | 80,000          |
| [Subscription-level deployments](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-subscription)                                                             | 800<sup>3</sup> |
| Locations of [Subscription-level deployments](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-to-subscription)                                                | 10              |

<sup>1</sup>You can apply up to 50 tags directly to a subscription. Within the subscription, each resource or resource group is also limited to 50 tags. However, the subscription can contain an unlimited number of tags that are dispersed across resources and resource groups.

<sup>2</sup>Resource Manager returns a list of tag name and values in the subscription only when the number of unique tags is 80,000 or less. A unique tag is defined by the combination of resource ID, tag name, and tag value. For example, two resources with the same tag name and value would be calculated as two unique tags. You still can find a resource by tag when the number exceeds 80,000.

<sup>3</sup>Deployments are automatically deleted from the history as you near the limit. For more information, see Automatic deletions from deployment history.

Note that subscription IDs must be non-empty GUIDs.

### Azure resource group limits

| Resource | Limit |
| --- | --- |
| Resources per [resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups) | Resources aren't limited by resource group. Instead, they're limited by resource type in a resource group. See next row. |
| Resources per resource group, per resource type |800 - Some resource types can exceed the 800 limit. See [Resources not limited to 800 instances per resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resources-without-resource-group-limit). |
| Deployments per resource group in the deployment history |800<sup>1</sup> |
| Resources per deployment |800 |
| Management locks per unique [scope](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview#understand-scope)  |20 |
| Number of tags per resource or resource group |50 |
| Tag key length |512 |
| Tag value length |256 |

<sup>1</sup>Deployments are automatically deleted from the history as you near the limit. Deleting an entry from the deployment history doesn't affect the deployed resources. For more information, see [Automatic deletions from deployment history](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history-deletions).

#### Template limits

| Value | Limit |
| --- | --- |
| Parameters |256 |
| Variables |256 |
| Resources (including copy count) |800 |
| Outputs |64 |
| Template expression |24,576 chars |
| Resources in exported templates |200 |
| Template size |4 MB |
| Resource definition size |1 MB |
| Parameter file size |4 MB |

You can exceed some template limits by using a nested template. For more information, see [Use linked templates when you deploy Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/linked-templates). To reduce the number of parameters, variables, or outputs, you can combine several values into an object. For more information, see [Objects as parameters](https://learn.microsoft.com/en-us/azure/architecture/guide/azure-resource-manager/advanced-templates/objects-as-parameters).

You may get an error with a template or parameter file of less than 4 MB, if the total size of the request is too large. For more information about how to simplify your template to avoid a large request, see [Resolve errors for job size exceeded](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/error-job-size-exceeded).

## Azure API Center limits

## Azure API Management limits

This section provides information about limits that apply to Azure API Management instances in different [service tiers](https://learn.microsoft.com/en-us/azure/api-management/api-management-features), including the following:

- [Resource limits in API Management classic and v2 tiers](#limits---api-management-classic-and-v2-tiers)
- [Resource limits in API Management workspaces](#limits---api-management-workspaces)
- [Resource limits in developer portal in API Management v2 tiers](#limits---developer-portal-in-api-management-v2-tiers)
- [Gateway runtime limits](#api-management-gateway-runtime-limits)

### Limits - API Management classic and v2 tiers

The following limits are introduced starting March 2026. Services in the classic tiers that surpass the revised limits are allowed to keep their existing capacity. For more information, see [Understanding API Management service limits](https://learn.microsoft.com/en-us/azure/api-management/service-limits).

> [!NOTE]
> * Limits are per service instance unless stated otherwise.
>
> * When counting the number of API-related resources (such as API operations and tags), API Management also includes API versions and revisions.
>

| Entity/Resource | Consumption | Developer | Basic/<br/>Basic v2 | Standard/<br/>Standard v2 | Premium/<br/>Premium v2 |
|-----------------|-------------|-----------|-------|----------|---------| 
| API operations | 3,000 | 3,000 | 10,000 | 50,000 | 75,000 |
| API tags | 1,500 | 1,500 | 1,500 | 2,500 | 15,000 |
| Named values | 5,000 | 5,000 | 5,000 | 10,000 | 18,000 |
| Loggers | 100 | 100 | 100 | 200 | 400 |
| Products | 100 | 100 | 200 | 500 | 2,000 |
| Subscriptions | N/A | 10,000 | 15,000 | 25,000 | 75,000 |
| Users | N/A | 20,000 | 20,000 | 50,000 | 75,000 |
| User-assigned managed identities | 10 | 10 | 10 | 10 | 10 |
| Workspaces per workspace gateway | N/A | N/A | 30<sup>1</sup> | 30<sup>1</sup> | 30 |
| Self-hosted gateways | N/A | 5 | N/A | N/A | 100<sup>2</sup> |

<sup>1</sup> Currently applies to v2 tiers only.<br/>
<sup>2</sup> Applies to Premium tier only.<br/>

### Limits - API Management workspaces

The following are resource limits per [workspace](https://learn.microsoft.com/en-us/azure/api-management/workspaces-overview) in Azure API Management:

| Resource | Workspace - Premium tier  |
| ---------| ----------- | 
| Workspaces per instance | 100  |
| Scale units per premium workspace gateway | 12 | 
| APIs (including versions and revisions)  | 200 |
| API operations  | 5,000  |
| Operations per API |  100 |
| Releases per API | 100 |
| Schemas per API | 100 |
| Subscriptions per API | 200 |
| Tags per API | 100 |
| Backends  | 200 |
| Certificates  | 200 | 
| Groups  | 50 |
| Loggers  | 50 |
| Named values  | 200 |
| Policy fragments  | 50 |
| Products  | 100 |
| APIs per product | 200 |
| Groups per product | 200 |
| Subscriptions per product | 1,000 |
| Tags per product | 50 |
| Schemas  | 500 | 
| Subscriptions  | 5,000 |
| Tags  | 200 |
| Groups per user  | 200 |
| Version sets  | 50 |

### Limits - Developer portal in API Management v2 tiers

| Item | Basic v2 | Standard v2 | Premium v2 |
| ---------| ----------- | ----------- | ----------- |    
| Number of media files to upload | 15 | 15 | 15 |
| Size of a media file | 500 KB | 500 KB | 500 KB |
| Number of pages | 30 | 50 | 50 |
| Number of widgets<sup>1</sup> | 30 | 50 | 50 |
| Size of metadata per page | 350 KB | 350 KB | 350 KB |
| Size of metadata per widget<sup>1</sup> | 350 KB | 350 KB | 350 KB |  
| Number of client requests per minute | 200 | 200 | 200 |

<sup>1</sup> Limit for built-in widgets such as text, images, or APIs list. Currently, custom widgets and custom HTML code widgets aren't supported in the v2 tiers.

### API Management gateway runtime limits

| Runtime limit | Classic | V2 | Consumption |
| ---------| ----------- | ----------- | ----------- |
| Concurrent back-end connections<sup>1</sup> per HTTP authority | 2,048<sup>2</sup> per unit | 2,048 | Unlimited |
| Cached response size | 2 MiB | 2 MiB | 2 MiB |
| Policy document size  | 512 KiB | 512 KiB | 16 KiB |
| Request payload size | Unlimited | 1 GiB | 1 GiB |
| Buffered payload size | 500 MiB | 2 MiB | 2 MiB |
| Request/response payload size in diagnostic logs | 8,192 bytes | 8,192 bytes | 8,192 bytes |
| Request URL size<sup>3</sup> | Unlimited | 16,384 bytes | 16,384 bytes |
| Length of URL path segment | 1,024 characters | 1,024 characters | 1,024 characters |
| Length of named value | 4,096 characters | 4,096 characters | 4,096 characters |
| Size of request or response body in [validate-content policy](https://learn.microsoft.com/en-us/azure/api-management/validate-content-policy) | 100 KiB | 100 KiB | 100 KiB |
| Size of API schema used by [validation policy](https://learn.microsoft.com/en-us/azure/api-management/validation-policies) | 4 MB | 4 MB | 4 MB |
| Total request duration | Unlimited | Unlimited | 30 seconds |
| Active WebSocket connections per unit<sup>4</sup> | 5,000 | 5,000 | N/A |

<sup>1</sup> Connections are pooled and reused unless explicitly closed by the backend.<br/>
<sup>2</sup> Limit is 1,024 in the Developer tier.<br/>
<sup>3</sup> Includes an up to 2048-bytes long query string.<br/>
<sup>4</sup> Up to a maximum of 60,000 connections per service instance.

## Azure App Service limits

| Resource | Free | Shared | Basic | Standard | Premium (v1-v4) | Isolated </th> |
| --- | --- | --- | --- | --- | --- | --- |
| [Apps](https://azure.microsoft.com/services/app-service/) per [Azure App Service plan](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans)<sup>1</sup> |10 |100 |Unlimited<sup>2</sup> |Unlimited<sup>2</sup> |Unlimited<sup>2</sup> |Unlimited<sup>2</sup>|
| App Service environments | | | | | | X |
| Windows code-only |X | X | X | X | X | X |
| Windows containers | | | | | X | X |
| Linux code-only and containers |X | | X | X | X | X |
| Compute instance type |Shared |Shared |Dedicated<sup>3</sup> |Dedicated<sup>3</sup> |Dedicated<sup>3</sup></p> |Dedicated<sup>3</sup>|
| [App Service plan](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans) |10 per region |10 per resource group |100 per resource group |100 per resource group |100 per resource group |100 per resource group|
| Compute instance type |Shared |Shared |Dedicated<sup>3</sup> |Dedicated<sup>3</sup> |Dedicated<sup>3</sup></p> |Dedicated<sup>3</sup>|
| [Scale out](https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up) (maximum instances) |1 shared |1 shared |3 dedicated<sup>3</sup> |10 dedicated<sup>3</sup> | 20 dedicated for v1; 30 dedicated for v2, v3, and v4.<sup>3</sup>|100 dedicated<sup>4</sup>|
| Storage<sup>5</sup> |1 GB<sup>5</sup> |1 GB<sup>5</sup> |10 GB<sup>5</sup> |50 GB<sup>5</sup> |250 GB<sup>5</sup> |1 TB<sup>12</sup> <br/><br/> The available storage quota is 999 GB. |
| CPU time (5 minutes)<sup>6</sup> |3 minutes |3 minutes |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a> |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a> |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a> |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a>|
| CPU time (day)<sup>6</sup> |60 minutes |240 minutes |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a> |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a> |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a> |Unlimited, pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/)</a> |
| Memory (1 hour) |1,024 MB per App Service plan |1,024 MB per app |N/A |N/A |N/A |N/A |
| Bandwidth |165 MB |Unlimited, [data transfer rates](https://azure.microsoft.com/pricing/details/data-transfers/) apply |Unlimited, [data transfer rates](https://azure.microsoft.com/pricing/details/data-transfers/) apply |Unlimited, [data transfer rates](https://azure.microsoft.com/pricing/details/data-transfers/) apply |Unlimited, [data transfer rates](https://azure.microsoft.com/pricing/details/data-transfers/) apply |Unlimited, [data transfer rates](https://azure.microsoft.com/pricing/details/data-transfers/) apply |
| Application architecture |32-bit |32-bit |32-bit/64-bit |32-bit/64-bit |32-bit/64-bit |32-bit/64-bit |
| WebSockets per instance (Windows)<sup>7</sup> |5 |35 |350 |Unlimited |Unlimited |Unlimited |
| WebSockets per instance (Linux)<sup>7</sup> |5 |N/A |~50K  |~50K  |~50K  |~50K  |
| Outbound IP connections per instance | 600 | 600 | Depends on instance size<sup>8</sup> | Depends on instance size<sup>8</sup> | Depends on instance size<sup>8</sup> | 16,000 |
| Concurrent [debugger connections](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-dotnet-visual-studio) per application |1 |1 |1 |5 |5 |5 |
| App Service Certificates per subscription | Not supported | Not supported |10 |10 |10 |10 |
| Custom domains per app</a> |0 (azurewebsites.net subdomain only)|500 |500 |500 |500 |500 |
| Custom domain [SSL support](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate) |Not supported, wildcard certificate for \*.azurewebsites.net available by default|Not supported, wildcard certificate for \*.azurewebsites.net available by default|Unlimited SNI SSL connections |Unlimited SNI SSL and 1 IP SSL connections included |Unlimited SNI SSL and 1 IP SSL connections included | Unlimited SNI SSL and 1 IP SSL connections included|
| [Hybrid connections](https://learn.microsoft.com/en-us/azure/app-service/app-service-hybrid-connections) | | | 5 per plan | 25 per plan | 220 per app | 220 per app |
| [Virtual Network Integration](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration) | | | X  |  X |  X  |  X  |
| [Private Endpoints](https://learn.microsoft.com/en-us/azure/app-service/networking/private-endpoint) | | | 100 per app | 100 per app | 100 per app |    |
| Integrated load balancer | |X |X |X |X |X<sup>9</sup> |
| [Access restrictions](https://learn.microsoft.com/en-us/azure/app-service/networking-features#access-restrictions) | 512 rules per app | 512 rules per app | 512 rules per app | 512 rules per app | 512 rules per app | 512 rules per app |
| [Always On](https://learn.microsoft.com/en-us/azure/app-service/configure-common) | | |X |X |X |X |
| [Custom scheduled backups](https://learn.microsoft.com/en-us/azure/app-service/manage-backup) | | | Scheduled backups every 2 hours, a maximum of 12 backups per day (manual + scheduled | Scheduled backups every 2 hours, a maximum of 12 backups per day (manual + scheduled) | Scheduled backups every hour, a maximum of 50 backups per day (manual + scheduled) | Scheduled backups every hour, a maximum of 50 backups per day (manual + scheduled) |
| [Autoscale](https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up) | | | |X |X |X |
| [WebJobs](https://learn.microsoft.com/en-us/azure/app-service/webjobs-create)<sup>10</sup> |X |X |X |X |X |X |
| [Endpoint monitoring](https://learn.microsoft.com/en-us/azure/app-service/web-sites-monitor) | | |X |X |X |X |
| [Staging slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) per app| | | |5 |20 |20 |
| [Testing in Production](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots#route-production-traffic-automatically)| | | |X |X |X |
| [Diagnostic Logs](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs) | X | X | X | X | X | X |
| Kudu | X | X | X | X | X | X |
| [Authentication and Authorization](https://learn.microsoft.com/en-us/azure/app-service/overview-authentication-authorization) | X | X | X | X | X | X |
| [App Service Managed Certificates](https://azure.microsoft.com/updates/secure-your-custom-domains-at-no-cost-with-app-service-managed-certificates-preview/)<sup>11</sup> | |  | X | X | X | X |
| SLA | |  |99.95%|99.95%|99.95%|99.95%|

<sup>1</sup> Apps and storage quotas are per App Service plan unless noted otherwise.

<sup>2</sup> The actual number of apps that you can host on these machines depends on the activity of the apps, the size of the machine instances, and the corresponding resource utilization.

<sup>3</sup> Dedicated instances can be of different sizes. For more information, see [App Service pricing](https://azure.microsoft.com/pricing/details/app-service/).

<sup>4</sup> More are allowed upon request.

<sup>5</sup> The storage limit is the total content size across all apps in the same App service plan. The total content size of all apps across all App service plans in a single resource group and region cannot exceed 500 GB. The file system quota for App Service hosted apps is determined by the aggregate of App Service plans created in a region and resource group.

<sup>6</sup> These resources are constrained by physical resources on the dedicated instances (the instance size and the number of instances).

<sup>7</sup>If you scale a Windows app in the Basic tier to two instances, you have 350 concurrent connections for each of the two instances. For Windows apps on Standard tier and above, there are no theoretical limits to WebSockets, but other factors can limit the number of WebSockets. For example, maximum concurrent requests allowed (defined by `maxConcurrentRequestsPerCpu`) are: 7,500 per small VM, 15,000 per medium VM (7,500 x 2 cores), and 75,000 per large VM (18,750 x 4 cores). Linux apps are limited 5 concurrent WebSocket connections on Free SKU and ~50k concurrent WebSocket connections per instance on all other SKUs.

<sup>8</sup> The maximum IP connections are per instance and depend on the instance size: 1,920 per B1/S1/P0V3/P1V3/P0V4/P1V4 instance, 3,968 per B2/S2/P2V3/P2V4 instance, 8,064 per B3/S3/P3V3/P4V4 instance.

<sup>9</sup> App Service Isolated SKUs can be internally load balanced (ILB) with Azure Load Balancer, so there's no public connectivity from the internet. As a result, some features of an ILB Isolated App Service must be used from machines that have direct access to the ILB network endpoint.

<sup>10</sup> Run custom executables and/or scripts on demand, on a schedule, or continuously as a background task within your App Service instance. Always On is required for continuous WebJobs execution. There's no predefined limit on the number of WebJobs that can run in an App Service instance. There are practical limits that depend on what the application code is trying to do.

<sup>11</sup> Only issuing standard certificates (wildcard certificates aren't available). Limited to only one free certificate per custom domain.

<sup>12</sup> Total storage usage across all apps deployed in a single App Service environment (regardless of how they're allocated across different resource groups).

## Azure Automation limits

#### Process automation

| Resource | Limit |Notes|
| --- | --- |---|
| Maximum number of active Automation accounts in a subscription in a region |10 | Enterprise and CSP subscriptions can create Automation accounts in any of the public [regions supported by the service](https://azure.microsoft.com/pricing/details/automation/). Create a [Support request](https://ms.portal.azure.com/#view/Microsoft_Azure_Support/NewSupportRequestV3Blade/callerWorkflowId/01133068-af18-43c8-baa4-a54f5fa7c684/callerName/Microsoft_Azure_Support%2FHelpPane.ReactView/productId/06bfd9d3-516b-d5c6-5802-169c800dec89/issueType/quota) to request for Quota increase.  [Learn more](https://learn.microsoft.com/en-us/azure/automation/automation-limits-quotas). |
| | 2 |  Pay-as-you-go, Sponsored, MSDN, MPN, Azure Pass subscriptions can create Automation accounts in any of the public [regions supported](https://azure.microsoft.com/pricing/details/automation/) by the service. Create a [Support request](https://ms.portal.azure.com/#view/Microsoft_Azure_Support/NewSupportRequestV3Blade/callerWorkflowId/01133068-af18-43c8-baa4-a54f5fa7c684/callerName/Microsoft_Azure_Support%2FHelpPane.ReactView/productId/06bfd9d3-516b-d5c6-5802-169c800dec89/issueType/quota) to request for Quota increase. [Learn more](https://learn.microsoft.com/en-us/azure/automation/automation-limits-quotas).
| | 1 |Free trial and Azure for Student subscriptions can create only one Automation account per region per subscription. Allowed list of regions: EastUS, EastUS2, WestUS, NorthEurope, SoutheastAsia, and JapanWest2 <sup>2</sup>|
| Maximum number of concurrent running jobs at the same instance of time per Automation account  | 50 | When this limit is reached, the subsequent requests to create a job fail. The client receives an error response. </br> Enterprise and CSP subscription in public regions. Create a [Support request](https://ms.portal.azure.com/#view/Microsoft_Azure_Support/NewSupportRequestV3Blade/callerWorkflowId/01133068-af18-43c8-baa4-a54f5fa7c684/callerName/Microsoft_Azure_Support%2FHelpPane.ReactView/productId/06bfd9d3-516b-d5c6-5802-169c800dec89/issueType/quota) to request for Quota increase. [Learn more](https://learn.microsoft.com/en-us/azure/automation/automation-limits-quotas). |
| | 10 | Pay-as-you-go, Sponsored, MSDN, MPN, Azure Pass subscriptions in public regions. Create a support request to request for a Quota increase. | 
| | 5  | Free trial and Azure for Student Azure in open subscriptions in public regions <sup>2</sup>.|
| Maximum number of new jobs that can be submitted every 30 seconds per Azure Automation account | 100 | When this limit is reached, the subsequent requests to create a job fail. The client receives an error response.|
| Maximum storage size of job metadata for a 30-day rolling period | 10 GB (approximately 4 million jobs)|When this limit is reached, the subsequent requests to create a job fail. |
| Maximum job stream limit|1 MiB|A single stream cannot be larger than 1 MiB.|
| Maximum job stream limit on Azure Automation portal | 200KB | Portal limit to show the job logs.|
| Maximum number of modules that can be imported every 30 seconds per Automation account |5 ||
| Maximum size of a module |100 MB ||
| Maximum size of a  node configuration file | 1 MB | Applies to state configuration |
| Job run time, Free tier |500 minutes per subscription per calendar month ||
| Maximum amount of disk space allowed per sandbox<sup>1</sup> |1 GB |Applies to Azure sandboxes only.|
| Maximum amount of memory given to a sandbox<sup>1</sup> |400 MB |Applies to Azure sandboxes only.|
| Maximum number of network sockets allowed per sandbox<sup>1</sup> |1,000 |Applies to Azure sandboxes only.|
| Maximum runtime allowed per runbook<sup>1</sup> |3 hours |Applies to Azure sandboxes only.|
| Maximum number of runbooks per Automation account | 800 |
| Maximum number of system hybrid runbook workers per Automation Account|4,000||
| Maximum number of user hybrid runbook workers per Automation Account|4,000||
|Maximum number of concurrent jobs that can be run on a single Hybrid Runbook Worker|50 ||
| Maximum runbook job parameter size   | 512 kilobytes||
| Maximum runbook parameters   | 50|If you reach the 50-parameter limit, you can pass a JSON or XML string to a parameter and parse it with the runbook.|
| Maximum webhook payload size |  512 kilobytes|
| Maximum days that job data is retained|30 days|
| Maximum PowerShell workflow state size |5 MB| Applies to PowerShell workflow runbooks when checkpointing workflow.|
| Maximum number of tags supported by an Automation account|15||
|Maximum number of characters in the value field of a variable| 1048576||

<sup>1</sup>A sandbox is a shared environment that can be used by multiple jobs. Jobs that use the same sandbox are bound by the resource limitations of the sandbox.</br>
<sup>2</sup>Free subscriptions including [Azure Free Account](https://azure.microsoft.com/pricing/offers/ms-azr-0044p?cid=msft_learn) and [Azure for Students](https://azure.microsoft.com/offers/ms-azr-0170p/) aren't eligible for limit or quota changes. If you have a free subscription, you can [upgrade](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/upgrade-azure-subscription) to pay-as-you-go subscription.
<sup>3</sup>Limits for Government clouds: 200 concurrent running jobs at the same instance of time per Automation account, no limit on number of Automation accounts per subscription. 

#### Change Tracking and Inventory

The following table shows the tracked item limits per machine for change tracking.

| **Resource** | **Limit**| **Notes** |
|---|---|---|
|File|500||
|File size|5 MB||
|Registry|250||
|Windows software|250|Doesn't include software updates.|
|Linux packages|1,250||
|Services|250||
|Daemon|250||

#### Azure Update Manager

The following are the Dynamic scope recommended limits for **each dynamic scope**:

| Resource    | Limit          |
|----------|----------------------------|
| Resource associations     | 1000  |
| Number of tag filters | 50 |
| Number of Resource Group filters    | 50 |

The following are the limits for schedule patching:

| Indicator    | Public Cloud Limit          | Mooncake/Fairfax Limit |
|----------|----------------------------|--------------------------|
| Number of schedules per subscription per region     | 250  | 250 |
| Total number of resource associations to a schedule | 3,000 | 3,000 |
| Resource associations on each dynamic scope    | 1,000 | 1,000 |
| Number of dynamic scopes per resource group or subscription per region     | 250  | 250  |
| Number of dynamic scopes per schedule   | 200  | 100  |
| Total number of subscriptions attached to all dynamic scopes per schedule   | 200  | 100  |

## Azure App Configuration

| Resource | Limit | Comment |
| --- | --- | ---|
| Configuration stores for Free tier | 3 stores per region per subscription. |
| Configuration stores for Developer tier | Unlimited stores per subscription. |
| Configuration stores for Standard tier | Unlimited stores per subscription. |
| Configuration stores for Premium tier | Unlimited stores per subscription. |
| Configuration store requests for Free tier | 1,000 requests per day  | Once the quota is exhausted, HTTP status code 429 is returned for all requests until the end of the day. |
| Configuration store requests for Developer tier | 6,000 requests per hour  | Once the quota is exhausted, requests may return HTTP status code 429 indicating Too Many Requests - until the end of the hour. |
| Configuration store requests for Standard tier | 30,000 requests per hour  | Once the quota is exhausted, requests may return HTTP status code 429 indicating Too Many Requests - until the end of the hour.|
| Configuration store requests for Premium tier | No quota limit on requests.  |
| Throughput for Free tier | No guaranteed throughput. |
| Throughput for Developer tier | No guaranteed throughput. |
| Throughput for Standard tier | Allow up to 300 requests per second (RPS) for read requests and up to 60 RPS for write requests. |
| Throughput for Premium tier | Allow up to 450 requests per second (RPS) for read requests and up to 100 RPS for write requests. |
| Storage for Free tier | 10 MB | There is no limit on the number of keys and labels as long as their total size is below the storage limit. |
| Storage for Developer tier | 500 MB | There is no limit on the number of keys and labels as long as their total size is below the storage limit. |
| Storage for Standard tier | 1 GB | There is no limit on the number of keys and labels as long as their total size is below the storage limit. |
| Storage for Premium tier | 4 GB | There is no limit on the number of keys and labels as long as their total size is below the storage limit. |
| Keys and values | 10 KB  | For a single key-value item, including all metadata. |
| Length for key, label, feature flag name, tag name, and tag value | 256 characters each | Applies to each field individually. For key-value based feature flags, the reserved prefix counts toward the key length limit. The default key may need to be shortened to accommodate longer key-value based feature flag names. |
| Snapshots storage for Free tier | 10 MB | Snapshots storage is extra and in addition to "Storage for Free Tier". Storage for both archived and active snapshots is counted towards this limit. |
| Snapshots storage for Developer tier | 500 MB | Snapshots storage is extra and in addition to "Storage for Free Tier". Storage for both archived and active snapshots is counted towards this limit. |
| Snapshots storage for Standard tier | 1 GB | Snapshots storage is extra and in addition to "Storage for Standard Tier". Storage for both archived and active snapshots is counted towards this limit. |
| Snapshots storage for Premium tier | 4 GB | Snapshots storage is extra and in addition to "Storage for Premium Tier". Storage for both archived and active snapshots is counted towards this limit. |
| Snapshot size | 1 MB | |

## Azure Cache for Redis limits

## Azure Cloud Services limits

| Resource | Limit |
| --- | --- |
| [Web or worker roles per deployment](https://learn.microsoft.com/en-us/azure/cloud-services/cloud-services-choose-me)<sup>1</sup> |25 |
| [Instance input endpoints](https://learn.microsoft.com/en-us/previous-versions/azure/reference/gg557552(v=azure.100)#instanceinputendpoint) per deployment |25 |
| [Input endpoints](https://learn.microsoft.com/en-us/previous-versions/azure/reference/gg557552(v=azure.100)#inputendpoint) per deployment |25 |
| [Internal endpoints](https://learn.microsoft.com/en-us/previous-versions/azure/reference/gg557552(v=azure.100)#internalendpoint) per deployment |25 |
| [Hosted service certificates](https://learn.microsoft.com/en-us/azure/cloud-services/cloud-services-certs-create#what-are-service-certificates) per deployment |199 |

<sup>1</sup>Each Azure Cloud Service with web or worker roles can have two deployments, one for production and one for staging. This limit refers to the number of distinct roles, that is, configuration. This limit doesn't refer to the number of instances per role, that is, scaling.

## Azure AI Search limits

Pricing tiers determine the capacity and limits of your search service. These tiers include:

- **Free**: Multitenant service that's shared with other Azure subscribers and helps with evaluations and small development projects
- **Basic**: Provides dedicated computing resources for production workloads at a smaller scale and with up to three replicas for highly available query workloads
- **Standard**: Includes S1, S2, S3, and S3 High Density; is for larger production workloads; multiple levels exist within the Standard tier for you to choose a resource configuration that best matches your workload profile

**Limits per subscription**

**Limits per search service**

See [Service limits in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity) for more details about limits, including document size, queries per second, keys, requests, and responses.

<a name='azure-cognitive-services-limits'></a>

## Foundry Tools limits

The following limits are for the number of Azure AI services resources per Azure subscription. 
There is a limit of only one allowed 'Free' account, per resource type, per subscription.
Each of the Foundry Tools may have other limitations, for more information, see [Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/).

| Type | Limit | Example |
|------|-------|---------|
| A mixture of Azure AI services resources | Maximum of 200 total Azure AI services resources per region. | 100 Azure Vision in Foundry Tools resources in West US, 50 Azure Speech in Foundry Tools resources in West US, and 50 Azure Language in Foundry Tools resources in West US. |
| A single type of Azure AI services resources. | Maximum of 100 resources per region | 100 Vision resources in West US 2, and 100 Vision resources in East US. |

## Azure Chaos Studio limits

For Chaos Studio Workspaces, see [Chaos Studio Workspaces limitations](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-workspaces-limitations). For Experiments (classic), see [Service limits for Experiments (classic)](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-service-limits).

## Azure Container Apps limits

See [Quotas in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/quotas) for Azure Container Apps limits.

The amount of disk space available to your application varies based on the associated workload profile. Available disk space determines the image size limit you can deploy to your container apps.

For dedicated workload profiles, the image size limit is per instance.

| Display name | Name | Image Size Limit (GB) |
|---|---|---|
| Consumption | consumption | 8\* |
| Dedicated-D4 | D4 |  90 |
| Dedicated-D8 | D8 |  210 |
| Dedicated-D16 | D16 |  460 |
| Dedicated-D32 | D32 |  940 |
| Dedicated-E4 | E4 |  90 |
| Dedicated-E8 | E8 |  210 |
| Dedicated-E16 | E16 |  460 |
| Dedicated-E32 | E32 |  940 |
| Dedicated-NC24-A100 (preview) | NC24-A100 | 210 |
| Dedicated-NC48-A100 (preview) | NC48-A100 | 460 |
| Dedicated-NC96-A100 (preview) | NC96-A100 | 940 |

\* The image size limit for a consumption workload profile is a shared among both image and app. For example, logs used by your app are subject to this size limit.

## Azure Cosmos DB limits

See [Limits in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits) for Azure Cosmos DB limits.

## Azure Data Explorer limits

The following table describes the maximum limits for Azure Data Explorer clusters.

| Resource | Limit |
| --- | --- |
| Clusters per region per subscription | 20 |
| Instances per cluster | 1,000 | 
| Number of databases in a cluster | 10,000 |
| Number of follower clusters (data share consumers) per leader cluster (data share producer) | 100 |
| Recommended maximum extents per cluster | 10,000,000 |

> [!NOTE]
> You can request higher limits for *Number of databases in a cluster* and *Clusters per region per subscription*. To request an increase, contact [Azure Support](https://azure.microsoft.com/support/legal/faq/).

The following table describes the limits on management operations performed on Azure Data Explorer clusters.

| Scope | Operation | Limit |
| --- | --- | --- |
| Cluster | read (for example, get a cluster) | 500 per 5 minutes |
| Cluster | write (for example, create a database) | 1,000 per hour |

## Azure Database for MySQL flexible server

See [Limitations in Azure Database for MySQL - Flexible Server](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/concepts-limitations) for Azure Database for MySQL - Flexible Server limits.

## Azure Database for PostgreSQL flexible server

See [Limits in Azure Database for PostgreSQL flexible server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-limits) for Azure Database for PostgreSQL flexible server limits.

## Azure Deployment Environments limits

|Subscription |Runtime limit per deployment​ |Runtime limit per month per region per subscription​ |Storage limit per Environment​ |
|---------------------|---------|----------|--------|
|Enterprise           | 30 min  | 5000 min |  1 GB  |
|Pay as you go        | 10 min  |  200 min |  1 GB  |
|Azure Pass           | 10 min  |  200 min |  1 GB  |
|MSDN                 | 10 min  |  200 min |  1 GB  |
|CSP                  | 10 min  |  200 min |  1 GB  |
|Free trial           | 10 min  |  200 min |  1 GB  |
|Azure for students   | 10 min  |  200 min |  1 GB  |

## Azure Files and Azure File Sync

See [Scalability and performance targets for Azure Files and Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-scale-targets) to learn more about the limits for Azure Files and Azure File Sync.

## Azure Functions limits

| Resource | [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) | [Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) | [Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)/[ASE](https://learn.microsoft.com/en-us/azure/app-service/environment/overview) | [Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview) | [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan) |
| --- | --- | --- | --- | --- | --- |
| Default [timeout duration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout) (min) | 30 | 30 | 30 | 30<sup>16</sup> | 5 |
| Max [timeout duration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout) (min) | unbounded<sup>9</sup> | unbounded<sup>9</sup> | unbounded<sup>2</sup> | unbounded<sup>17</sup> | 10 |
| Max outbound connections (per instance) | unbounded | unbounded | see [App Service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-app-service-limits) | unbounded | 600 active (1200 total) |
| Max request size (MB)<sup>3</sup> | 210 | 210 | 210 | 210 | 210 |
| Max query string length<sup>3</sup> | 4096 | 4096 | 4096 | 4096 | 4096 |
| Max request URL length<sup>3</sup> | 8192 | 8192 | 8192 | 8192 | 8192 |
| [ACU](https://learn.microsoft.com/en-us/azure/virtual-machines/acu) per instance | 210-840 | 100-840/210-250<sup>10</sup> | [varies](https://learn.microsoft.com/en-us/azure/container-apps/billing) | 100 | varies |
| Max memory (GB per instance) | 4<sup>14</sup> | 3.5-14 | 1.75-256/8-256 | [varies](https://learn.microsoft.com/en-us/azure/container-apps/billing) | 1.5 |
| Max instance count (Windows&nbsp;\|&nbsp;Linux)<sup>15</sup> | n/a&nbsp;\|&nbsp;1000 | 20-100 | 10-30 (100 ASE)<sup>11</sup> | 300-1000<sup>1</sup> | 200&nbsp;\|&nbsp;100 |
| Function apps per plan<sup>13</sup> | 1 | 100 | unbounded<sup>4</sup> | unbounded<sup>4</sup> | 100 |
| [App Service plans](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans) | n/a | 100 per resource group | 100 per resource group | n/a | 100 per [region](https://azure.microsoft.com/global-infrastructure/regions/) |
| [Deployment slots](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots) per app<sup>12</sup> | n/a | 3 | 1-20<sup>11</sup> | not supported | 2 |
| Storage (temporary)<sup>5</sup> | 0.8 GB | 11-61 GB | 11-140 GB | n/a | 0.5 GB |
| Storage (persisted) | 0 GB<sup>7</sup> | 250 GB | 10-1000 GB<sup>11</sup> | n/a | 1 GB<sup>6,7</sup> |
| Custom domains per app</a> | 25<sup>8</sup> | 500 | 500 | not supported | 500<sup>8</sup> |
| Custom domain [TSL/SSL support](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings) | unbounded SNI SSL and one IP SSL connection included | unbounded SNI SSL and one IP SSL connection included | unbounded SNI SSL and one IP SSL connection included | not supported | unbounded SNI SSL connection included |

Notes on service limits:

1. On Container Apps, you can set the [maximum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition), which the platform honors as long as there's enough cores quota available.
2. Requires the App Service plan be set to [Always On](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan#always-on). Pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/). A grace period of 10 minutes is given for HTTP triggered functions during platform updates but not for other triggers.
3. These limits are [set in the host](https://github.com/Azure/azure-functions-host/blob/dev/src/WebJobs.Script.WebHost/web.config).  
4. The actual number of function apps that you can host depends on the activity of the apps, the size of the machine instances, and the corresponding resource utilization.  
5. The storage limit is the total content size in temporary storage across all apps in the same App Service plan. For Consumption plans on Linux, the storage is currently 1.5 GB.
6. Consumption plan uses an Azure Files share for persisted storage. When you provide your own Azure Files share, the specific share size limits depend on the storage account you set for [WEBSITE_CONTENTAZUREFILECONNECTIONSTRING](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_contentazurefileconnectionstring). 
7. On Linux, you must [explicitly mount your own Azure Files share](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#mount-file-shares).
8. When your function app is hosted in a [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan), only the CNAME option is supported. For function apps in a [Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) or an [App Service plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan), you can map a custom domain using either a CNAME or an A record.  
9. There's no maximum execution timeout duration enforced. However, the grace period given to a function execution is 60 minutes [during scale in](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling#scale-in-behaviors) and 10 minutes during platform updates.
10. Workers are roles that host customer apps. Workers are available in three fixed sizes: One vCPU/3.5 GB RAM; Two vCPU/7 GB RAM; Four vCPU/14 GB RAM.   
11. See [App Service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#app-service-limits) for details.  
12. Including the production slot.  
13. There's currently a limit of 5,000 function apps in a given subscription. 
14. Flex Consumption plan instance sizes are currently defined as 512 MB, 2,048 MB, or 4,096 MB. For more information, see [Instance memory](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#instance-sizes).  
15. For details, see [Scale](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#scale) in the Hosting comparison article.
16. When the [minimum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition) is set to zero, the default timeout depends on the specific triggers used in the app.
17. When the [minimum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition) is set to one or more.

See [Azure Functions hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) for more information.

## Azure Health Data Services

### Azure Health Data Services limits

Health Data Services is a set of managed API services based on open standards and frameworks. Health Data Services enables workflows to improve healthcare and offers scalable and secure healthcare solutions. Health Data Services includes Fast Healthcare Interoperability Resources (FHIR) service, the Digital Imaging and Communications in Medicine (DICOM) service, and MedTech service.

FHIR service is an implementation of the FHIR specification within Health Data Services. It enables you to combine in a single workspace one or more FHIR service instances with optional DICOM and MedTech service instances. Azure API for FHIR is generally available as a stand-alone service offering.

Each FHIR service instance in Azure Health Data Services has a storage limit of 4 TB by default. If you have more data, you can ask Microsoft to increase storage up to 100 TB for your FHIR service. To request storage greater than 4 TB, [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/overview) on the Azure portal and use the issue type Service and Subscription limit (quotas).

| **Quota Name** | **Default Limit**| **Maximum Limit** | **Notes** |
|---|---|---|---|
|Workspace |10|[Contact support](https://azure.microsoft.com/support/options/) |Limit per subscription|
|FHIR service |10|[Contact support](https://azure.microsoft.com/support/options/) |Limit per workspace|
|DICOM service |10|[Contact support](https://azure.microsoft.com/support/options/) |Limit per workspace|
The per-subscription and per-workspace limits are enforced independently. To deploy more than 10 FHIR services in a subscription, distribute them across multiple workspaces.

### Azure API for FHIR service limits

Azure API for FHIR is a managed, standards-based, compliant API for clinical health data that enables solutions for actionable analytics and machine learning.

| **Quota Name** | **Default Limit**| **Maximum Limit** | **Notes** |
|---|---|---|---|
|Request Units (RUs)|100,000 RUs|[Contact support](https://azure.microsoft.com/support/options/) Maximum available is 1,000,000. |You need a minimum of 400 RUs or 40 RUs/GB, whichever is larger.|
|Concurrent connections |15 concurrent connections on two instances (for a total of 30 concurrent requests)|[Contact support](https://azure.microsoft.com/support/options/)||
|Azure API for FHIR Service Instances per Subscription|10|[Contact support](https://azure.microsoft.com/support/options/)||

## Azure Kubernetes Service limits

## Azure Lab Services

The following limits are for the number of Azure Lab Services resources. 

#### Per resource type

| Grouping |Resource type | Limit |
|-----|------|-------|
|Per subscription|Labs|980|
|Per resource group|Labs|800|
| |Lab plans|800|
|Per lab|Schedules|250|
| |	Virtual machines (VMs)|400| 

#### Per region - Lab plans and labs

| Subscription type | Lab plan limits |Lab limits|
|------|------|-------|
| Default | 2 | 2 |
| Pay As You Go | 500 | 500 |
| MPN | 500 | 500 |
| Azure In Open | 500 | 500 |
| Enterprise Agreement | 500 | 500 | 
| MSDN | 500 | 500 |
| Sponsored | 100 | 15 |
| CSP | 500 | 500 |
| Azure Pass | 100 | 25 |
| Free Trial | 100 | 15 |
| Azure for Students | 100| 15 |

For more information about Azure Lab Services capacity limits, see [Capacity limits in Azure Lab Services](https://learn.microsoft.com/en-us/azure/lab-services/capacity-limits).

Contact support to request an increase your limit. 

## Azure Load Testing limits

For Azure Load Testing limits, see [Service limits in Azure Load Testing](https://learn.microsoft.com/en-us/azure/app-testing/load-testing/resource-limits-quotas-capacity).

## Azure Machine Learning limits

See [Manage and increase quotas and limits for resources with Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-quotas) for the latest values for Azure Machine Learning Compute quotas.

## Azure Maps limits

> [!NOTE]
>
> **Azure Maps Gen1 Price Tier Retirement**
>
> Gen1 pricing tier is now deprecated and will be retired on September 15, 2026. Gen2 pricing tier replaces Gen1 (both S0 and S1) pricing tier. If your Azure Maps account has Gen1 pricing tier selected, you can switch to Gen2 pricing before Gen1 is retired, otherwise it will automatically be updated. For more information, see [Manage the pricing tier of your Azure Maps account](https://learn.microsoft.com/en-us/azure/azure-maps/how-to-manage-pricing-tier).

For Azure Maps queries per second (QPS) limits, see [Azure Maps QPS rate limits](https://learn.microsoft.com/en-us/azure/azure-maps/azure-maps-qps-rate-limits)

The following table shows the cumulative data size limit for Azure Maps accounts in an Azure subscription. The Azure Maps Data service is available only at the Gen1 (S1) and Gen2 pricing tier.

| Resource                               | Limit  |
|----------------------------------------|:------:|
| Maximum storage per Azure subscription |   1 GB |
| Maximum size per file upload           | 100 MB |

> [!NOTE]
>
> **Azure Maps Data Registry service Retirement**
>
> The Azure Maps Data Registry service is now deprecated and is retired as of September 30, 2025. For more information, see [How to create data registry](https://learn.microsoft.com/en-us/azure/azure-maps/how-to-create-data-registries).

## Azure Managed Grafana limits

> [!NOTE]
> The Essential tier is deprecated. Existing Essential instances continue to run during the transition period, but you can't create new Essential instances. The Essential tier is scheduled to retire on March 31, 2027.

| Limit                                | Description                                                                                                                                                          | Essential (deprecated; existing instances only) | Standard X1            | Standard X2            |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|------------------------|------------------------|
| Alert rules                          | Maximum number of alert rules that you can create.                                                                                                                   | Not supported          | 500 per instance       | 1000 per instance      |
| Memory for Grafana instance          | Amount of memory for Grafana in your dedicated instance.                                                                                                             | Basic                  | Standard               | Expanded               | 
| Dashboards                           | Maximum number of dashboards that you can create.                                                                                                                    | 20 per instance        | Unlimited              | Unlimited              |
| Data sources                         | Maximum number of data sources that you can create.                                                                                                                   | 5 per instance         | Unlimited              | Unlimited              |
| Git Sync repositories                | Maximum number of GitHub repositories that you can connect with Git Sync.                                                                                            | 10 per instance        | 10 per instance        | 10 per instance        |
| Git Sync resources per repository    | Maximum number of resources per repository that you can synchronize with Git Sync.                                                                                  | 1,000 per repository   | 1,000 per repository   | 1,000 per repository   |
| API keys                             | Maximum number of API keys that you can create.                                                                                                                      | 2 per instance         | 100 per instance       | 100 per instance       |
| Data query timeout                   | Maximum wait duration for the reception of data query response headers, before Grafana times out.                                                                    | 200 seconds            | 200 seconds            | 200 seconds            |
| Data source query size               | Maximum number of bytes that are read or accepted from responses of outgoing HTTP requests.                                                                             | 80 MB                  | 80 MB                  | 80 MB                  |
| Render image or PDF report wait time | Maximum duration for an image or report PDF rendering request to complete before Grafana times out.                                                                  | Not supported          | 220 seconds            | 220 seconds            |
| Instance count                       | Maximum number of instances in a single subscription per Azure region.                                                                                               | 1                      | 50                     | 50                     |
| Requests per IP                      | Maximum number of requests per IP per second.                                                                                                                        | 90 requests per second | 90 requests per second | 90 requests per second |
| Requests per HTTP host               | Maximum number of requests per HTTP host per second. The HTTP host stands for the Host header in incoming HTTP requests, which can describe each unique host client. | 45 requests per second | 45 requests per second | 45 requests per second |

## Azure Monitor limits

For Azure Monitor limits, see [Azure Monitor service limits](https://learn.microsoft.com/en-us/azure/azure-monitor/service-limits).

## Azure Data Factory limits

Azure Data Factory is a multitenant service that has the following default limits in place to make sure customer subscriptions are protected from each other's workloads. To raise the limits up to the maximum for your subscription, contact support.

| Resource | Default limit | Maximum limit |
| -------- | ------------- | ------------- |
| Total number of entities, such as pipelines, data sets, triggers, linked services, Private Endpoints, and integration runtimes, within a data factory | 5,000 |5,000   |
| Total CPU cores for Azure-SSIS Integration Runtimes under one subscription | 64 | [Find out how to request a quota increase from support](https://azure.microsoft.com/blog/azure-limits-quotas-increase-requests/). |
| Concurrent pipeline runs per data factory shared among all pipelines in the factory | 10,000  | 10,000 |
| Concurrent External activity runs per subscription per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-ir-location)<br>External activities are managed on integration runtime but execute on linked services, including Databricks, stored procedure, Web, and others. This limit doesn't apply to Self-hosted IR. | 3,000 | 3,000 |
| Concurrent Pipeline activity runs per subscription per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-ir-location) <br>Pipeline activities execute on integration runtime, including Lookup, GetMetadata, and Delete. This limit doesn't apply to Self-hosted IR. | 1,000 | 1,000                                                        |
| Concurrent authoring operations per subscription per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-ir-location)<br>Including test connection, browse folder list and table list, preview data. This limit doesn't apply to Self-hosted IR. | 200 | 200                                                          |
| Concurrent Data Integration Units<sup>1</sup> consumption per subscription per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#integration-runtime-location)| Region group 1<sup>2</sup>: 6,000<br>Region group 2<sup>2</sup>: 3,000<br>Region group 3<sup>2</sup>: 1,500 | Region group 1<sup>2</sup>: 6,000<br/>Region group 2<sup>2</sup>: 3,000<br/>Region group 3<sup>2</sup>: 1,500 |
| Concurrent Data Integration Units<sup>1</sup> consumption per subscription per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#integration-runtime-location) in managed virtual network|  2,400 | 2,400 |
| Maximum activities per pipeline, which includes inner activities for containers | 120 | 120 |
| Maximum number of linked integration runtimes that can be created against a single self-hosted integration runtime | 100 | 100 |
| Maximum number of nodes that can be created against a single self-hosted integration runtime | 4 | 4 |
| Maximum parameters per pipeline | 50 | 50 |
| ForEach items | 100,000 | 100,000 |
| ForEach parallelism | 20 | 50 |
| Maximum queued runs per pipeline | 100 | 100 |
| Characters per expression | 8,192 | 8,192 |
| Minimum tumbling window trigger interval | 5 min | 15 min |
| Minimum timeout for pipeline activity runs | 10 min | 10 min |
| Maximum timeout for pipeline activity runs | 7 days | 7 days |
| Bytes per object for pipeline objects<sup>3</sup> | 200 KB | 200 KB |
| Bytes per object for dataset and linked service objects<sup>3</sup> | 100 KB | 2,000 KB |
| Bytes per payload for each activity run<sup>4</sup> | 896 KB | 896 KB |
| Data Integration Units<sup>1</sup> per copy activity run | 256 | 256 |
| Write API calls | 1,200/h | 1,200/h<br/><br/> This limit is imposed by Azure Resource Manager, not Azure Data Factory. |
| Read API calls | 12,500/h | 12,500/h<br/><br/> This limit is imposed by Azure Resource Manager, not Azure Data Factory. |
| Monitoring queries per minute | 1,000 | 1,000 |
| Maximum time of data flow debug session | 8 hrs | 8 hrs |
| Concurrent number of data flows per integration runtime | 50 | 50 |
| Concurrent number of data flows per integration runtime in managed vNet| 50 | 50 |
| Concurrent number of data flow debug sessions per user per factory | 3 | 3 |
| Data Flow Azure IR TTL (time to live) limit | 4 hrs |  4 hrs |
| Meta Data Entity Size limit in a factory | 2 GB | 2 GB |

<sup>1</sup> The data integration unit (DIU) is used in a cloud-to-cloud copy operation. Learn more from [Data integration units (version 2)](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-performance#data-integration-units). For information on billing, see [Azure Data Factory pricing](https://azure.microsoft.com/pricing/details/data-factory/).

<sup>2</sup> [Azure Integration Runtime](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-integration-runtime) is [globally available](https://azure.microsoft.com/global-infrastructure/services/) to ensure data compliance, efficiency, and reduced network egress costs. 

| Region group | Regions |
| -------- | ------ |
| Region group 1 | Central US, East US, East US 2, North Europe, West Europe, West US, West US 2 |
| Region group 2 | Australia East, Australia Southeast, Brazil South, Central India, Japan East, North Central US, South Central US, Southeast Asia, West Central US |
| Region group 3 | Other regions |

If managed virtual network is enabled, the data integration unit (DIU) in all region groups are 2,400.

<sup>3</sup> Pipeline, data set, and linked service objects represent a logical grouping of your workload. Limits for these objects don't relate to the amount of data you can move and process with Azure Data Factory. Data Factory is designed to scale to handle petabytes of data.

<sup>4</sup> The payload for each activity run includes the activity configuration, one or more associated datasets, and linked service configurations if any, and a small portion of system properties generated per activity type. Limit for this payload size doesn't relate to the amount of data you can move and process with Azure Data Factory. Learn about the [symptoms and recommendation](https://learn.microsoft.com/en-us/azure/data-factory/data-factory-troubleshoot-guide#payload-is-too-large) if you hit this limit.

#### Web service call limits
Azure Resource Manager has limits for API calls. You can make API calls at a rate within the [Azure Resource Manager API limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-resource-group-limits).

## Azure NetApp Files

Azure NetApp Files has a regional limit for capacity. The standard capacity limit for each subscription is 25 TiB, per region, across all service levels. To increase the capacity, use the [Service and subscription limits (quotas)](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-resource-limits#request-limit-increase) support request.

To learn more about the limits for Azure NetApp Files, see [Resource limits for Azure NetApp Files](https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-resource-limits).

## Azure Policy limits

## Azure Quantum limits

### Provider Limits & Quota

The Azure Quantum Service supports both first and third-party service providers. 
Third-party providers own their limits and quotas. Users can view offers and limits in the Azure portal when configuring third-party providers. 

You can find the published quota limits for Microsoft's first party Optimization Solutions provider below. 

#### Learn & Develop SKU

| Resource | Limit |
| --- | --- |
| CPU-based concurrent jobs | up to 5<sup>1</sup> concurrent jobs |
| FPGA-based concurrent jobs | up to 2<sup>1</sup> concurrent jobs |
| CPU-based solver hours | 20 hours per month  |
| FPGA-based solver hours | 1 hour per month  |

While on the Learn & Develop SKU, you **cannot** request an increase on your quota limits. Instead you should switch to the Performance at Scale SKU.

#### Performance at Scale SKU

| Resource | Default Limit | Maximum Limit |
| --- | --- | --- |
| CPU-based concurrent jobs | up to 100<sup>1</sup> concurrent jobs | same as default limit |
| FPGA-based concurrent jobs | up to 10<sup>1</sup> concurrent jobs | same as default limit |
| Solver hours | 1,000 hours per month  | up to 50,000 hours per month |

Reach out to Azure Support to request a limit increase.

For more information, please review the [Azure Quantum pricing page](https://aka.ms/AQ/Pricing).
Review the relevant provider pricing pages in the Azure portal for details on third-party offerings.

<sup>1</sup> Describes the number of jobs that can be queued at the same time.

## Azure RBAC limits

The following limits apply to [Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview).

| Area | Resource | Limit |
| --- | --- | --- |
| [Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) |  |  |
|  | Number of Azure role assignments per Azure subscription | 5,000 |
|  | Number of Azure role assignments per management group | 500 |
|  | Size of description for Azure role assignments | Recommended maximum: 512 chars<br/>Maximum: 2,048 chars |
|  | Size of [condition](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-overview) for Azure role assignments | 8 KB |
| [Azure custom roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles) |  |  |
|  | Number of Azure custom roles per tenant | 5,000 |
|  | Number of Azure custom roles per tenant<br/>(for Microsoft Azure operated by 21Vianet) | 2,000 |
|  | Size of role name for Azure custom roles | Recommended maximum: 256 chars<br/>Maximum: 512 chars |
|  | Size of description for Azure custom roles | Recommended maximum: 512 chars<br/>Maximum: 2,048 chars |
|  | Size of an Azure custom role definition | 1 MB |
|  | Number of assignable scopes for Azure custom roles | 2,000 |
|  | Number of management group assignable scopes for Azure custom roles | 1 |
| [Azure deny assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/deny-assignments) |  |  |
|  | Number of system-managed deny assignments per Azure subscription | 2,000 |

## Azure SignalR Service limits

| Resource | Default limit | Maximum limit | 
| --- | --- | --- |
| Azure SignalR Service units per instance for Free tier |1 |1 |
| Azure SignalR Service units per instance for Standard/Premium_P1 tier |100 |100 |
| Azure SignalR Service units per instance for Premium_P2 tier |100 - 1,000 |100 - 1,000 |
| Azure SignalR Service units per subscription per region for Free tier|5 |5 |
| Total Azure SignalR Service unit counts per subscription per region |150 |Unlimited |
| Concurrent connections per unit for Free tier |20 |20 |
| Concurrent connections per unit for Standard/Premium tier |1,000 |1,000|
| Included messages per unit per day for Free tier|20,000 |20,000 |
| Additional messages per unit per day for Free tier|0 |0 |
| Included messages per unit per day for Standard/Premium tier|1,000,000 |1,000,000 |
| Additional messages per unit per day for Standard/Premium tier|Unlimited |Unlimited |

To request an update to your subscription's default limits, open a support ticket.

For more information about how connections and messages are counted, see [Messages and connections in Azure SignalR Service](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-concept-messages-and-connections).

If your requirements exceed the limits, switch from Free tier to Standard tier and add units. For more information, see [How to scale an Azure SignalR Service instance?](https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-howto-scale-signalr) 

If your requirements exceed the limits of a single instance, add instances. For more information, see [How to enable Geo-Replication in Azure SignalR Service](https://learn.microsoft.com/en-us/azure/azure-signalr/howto-enable-geo-replication).

## Azure Spring Apps limits

See [Quotas and service plans for Azure Spring Apps](https://learn.microsoft.com/en-us/azure/spring-apps/basic-standard/quotas) to learn more about the limits for Azure Spring Apps.

## Azure Storage limits

This section lists the following limits for Azure Storage:

- [Standard storage account limits](#standard-storage-account-limits)
- [Azure Storage resource provider limits](#azure-storage-resource-provider-limits)
- [Azure Blob Storage limits](#azure-blob-storage-limits)
- [Azure Queue storage limits](#azure-queue-storage-limits)
- [Azure Table storage limits](#azure-table-storage-limits)

### Standard storage account limits

The following table describes default limits for Azure general-purpose v2 (GPv2), general-purpose v1 (GPv1), and Blob Storage accounts.

A few entries in the table also apply to disk access and are explicitly labeled. Disk access is a resource that is exclusively used for importing or exporting managed disks through [private links](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-restrict-import-export-overview#private-links).

Customers should use a GPv2 storage account, because [GPv1 is being retired](https://learn.microsoft.com/en-us/azure/storage/common/general-purpose-version-1-account-migration-overview). You can easily upgrade a GPv1 or Blob Storage account to a GPv2 account with no downtime and no need to copy data. For more information, see [Upgrade to a GPv2 storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-upgrade).

The *ingress* limit refers to all data sent to a storage account or disk access. The *egress* limit refers to all data received from a storage account or disk access.

> [!NOTE]
> You can request higher capacity and ingress limits. To request an increase, contact [Azure Support](https://azure.microsoft.com/support/faq/).

| Resource | Limit |
|--|--|
| Maximum number of storage accounts with standard endpoints per region per subscription, including standard and premium storage accounts. | 250 by default, 1000 by request<sup>1</sup> |
| Maximum number of storage accounts with Azure DNS zone endpoints (preview) per region per subscription, including standard and premium storage accounts. | 5,000 (preview) |
| Default maximum storage account capacity. | 5 PiB <sup>2</sup> |
| Maximum number of blob containers, blobs, directories, and subdirectories (if hierarchical namespace is enabled), file shares, tables, queues, entities, or messages per storage account. | No limit |
| Default maximum request rate per general-purpose v2, Blob Storage account, and disk access resources in the following regions:<br /><ul><li>**Americas**: Brazil South, Canada Central, Central US, East US, East US 2, North Central US, South Central US, West US, West US 2, West US 3</li><li>**Asia Pacific**: Australia East, Central India, China East 2, China North 3, East Asia, Japan East, Jio India West, Korea Central, Southeast Asia</li><li>**Europe**: France Central, Germany West Central, North Europe, Norway East, Sweden Central, UK South, West Europe</li><li>**Africa**: South Africa North</li><li>**Azure Government**: USGov Arizona, USGov Virginia</li></ul>| 40,000 requests per second<sup>2</sup> |
| Default maximum request rate per general-purpose v2, Blob Storage account, and disk access resources in regions that aren't listed in the previous row. | 20,000 requests per second<sup>2</sup> |
| Default maximum ingress per general-purpose v2, Blob Storage account, and disk access resources in the following regions:<br /><ul><li>**Americas**: Brazil South, Canada Central, Central US, East US, East US 2, North Central US, South Central US, West US, West US 2, West US 3</li><li>**Asia Pacific**: Australia East, Central India, China East 2, China North 3, East Asia, Japan East, Jio India West, Korea Central, Southeast Asia</li><li>**Europe**: France Central, Germany West Central, North Europe, Norway East, Sweden Central, UK South, West Europe</li><li>**Africa**: South Africa North</li><li>**Azure Government**: USGov Arizona, USGov Virginia</li></ul>| 60 Gbps<sup>2</sup> |
| Default maximum ingress per general-purpose v2, Blob Storage account, and disk access resources in regions that aren't listed in the previous row. | 25 Gbps<sup>2</sup> |
| Default maximum ingress for general-purpose v1 storage accounts (all regions). | 10 Gbps<sup>2</sup> |
| Default maximum egress for general-purpose v2, Blob Storage accounts, and disk access resources in the following regions:<br /><ul><li>**Americas**: Brazil South, Canada Central, Central US, East US, East US 2, North Central US, South Central US, West US, West US 2, West US 3</li><li>**Asia Pacific**: Australia East, Central India, China East 2, China North 3, East Asia, Japan East, Jio India West, Korea Central, Southeast Asia</li><li>**Europe**: France Central, Germany West Central, North Europe, Norway East, Sweden Central, UK South, West Europe</li><li>**Africa**: South Africa North</li><li>**Azure Government**: USGov Arizona, USGov Virginia</li></ul> | 200 Gbps<sup>2</sup> |
| Default maximum egress for general-purpose v2, Blob Storage accounts, and disk access resources in regions that aren't listed in the previous row. | 50 Gbps<sup>2</sup> |
| Maximum egress for general-purpose v1 storage accounts (US regions). | 20 Gbps if RA-GRS/GRS is enabled, 30 Gbps for LRS/ZRS |
| Maximum egress for general-purpose v1 storage accounts (non-US regions). | 10 Gbps if RA-GRS/GRS is enabled, 15 Gbps for LRS/ZRS |
| Maximum number of IP address rules per storage account. | 400 |
| Maximum number of virtual network rules per storage account. | 400 |
| Maximum number of resource instance rules per storage account. | 200 |
| Maximum number of private endpoints per storage account. | 200 |

<sup>1</sup> With a quota increase, you can create up to 1000 storage accounts with standard endpoints per region. For more information, see [Increase Azure Storage account quotas](https://learn.microsoft.com/en-us/azure/quotas/storage-account-quota-requests).

<sup>2</sup> Azure Storage standard accounts support higher capacity limits and higher limits for ingress and egress by request. To request an increase in account limits, contact [Azure Support](https://azure.microsoft.com/support/faq/).

### Azure Storage resource provider limits

The following limits apply only when you perform management operations by using Azure Resource Manager with Azure Storage and the Storage Resource Provider. The limits apply per subscription per region of the resource in the request.

| Resource | Limit |
| --- | --- |
| Storage account management operations (read) |800 per 5 minutes |
| Storage account management operations (write) |10 per second / 1200 per hour |
| Storage account management operations (list) |100 per 5 minutes |

### Azure Blob Storage limits

| Resource | Target |
|-|-|
| Maximum size of single blob container | Same as maximum storage account capacity |
| Maximum number of blocks in a block blob or append blob | 50,000 blocks |
| Maximum size of a block in a block blob | 4,000 MiB |
| Maximum size of a block blob | 50,000 x 4,000 MiB (approximately 190.7 TiB) |
| Maximum size of a block in an append blob | 4 MiB |
| Maximum size of an append blob | 50,000 x 4 MiB (approximately 195 GiB) |
| Maximum size of a page blob | 8 TiB<sup>2</sup> |
| Maximum number of stored access policies per blob container | 5 |
| Target request rate for a single block blob | Up to 3,000 requests per second |
| Target request rate for a single page blob | Up to 500 requests per second |
| Target throughput for a single page blob | Up to 60 MiB per second<sup>2</sup> |
| Target throughput for a single block blob | Up to storage account ingress/egress limits<sup>1</sup> |

<sup>1</sup> Throughput for a single blob depends on several factors. These factors include but aren't limited to concurrency, request size, performance tier, speed of source for uploads, and destination for downloads. To take advantage of the performance enhancements of [high-throughput block blobs](https://azure.microsoft.com/blog/high-throughput-with-azure-blob-storage/), upload larger blobs or blocks. Specifically, call the [Put Blob](https://learn.microsoft.com/en-us/rest/api/storageservices/put-blob) or [Put Block](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block) operation with a blob or block size that's greater than 256 KiB.

<sup>2</sup> Page blobs aren't yet supported in accounts that have a hierarchical namespace enabled.

The following table describes the maximum block and blob sizes permitted by service version.

| Service version | Maximum block size (via Put Block) | Maximum blob size (via Put Block List) | Maximum blob size via single write operation (via Put Blob) |
|-|-|-|-|
| Version 2019-12-12 and later | 4,000 MiB | Approximately 190.7 TiB (4,000 MiB x 50,000 blocks) | 5,000 MiB |
| Version 2016-05-31 through version 2019-07-07 | 100 MiB | Approximately 4.75 TiB (100 MiB x 50,000 blocks) | 256 MiB |
| Versions prior to 2016-05-31 | 4 MiB | Approximately 195 GiB (4 MiB x 50,000 blocks) | 64 MiB |

### Azure Queue storage limits

| Resource | Target |
|----------|---------------|
| Maximum size of a single queue | 500 TiB |
| Maximum size of a message in a queue | 64 KiB |
| Maximum number of stored access policies per queue | 5 |
| Maximum request rate per storage account | 20,000 messages per second, which assumes a 1-KiB message size |
| Target throughput for a single queue (1-KiB messages) | Up to 2,000 messages per second |

### Azure Table storage limits

The following table describes capacity, scalability, and performance targets for Table storage.

| Resource | Target |
|----------|---------------|
| Number of tables in an Azure storage account | Limited only by the capacity of the storage account |
| Number of partitions in a table | Limited only by the capacity of the storage account |
| Number of entities in a partition | Limited only by the capacity of the storage account |
| Maximum size of a single table | 500 TiB |
| Maximum size of a single entity, including all property values | 1 MiB |
| Maximum number of properties in a table entity | 255 (including the three system properties, **PartitionKey**, **RowKey**, and **Timestamp**) |
| Maximum total size of an individual property in an entity | Varies by property type. For more information, see **Property Types** in [Understanding the Table Service Data Model](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-the-table-service-data-model). |
| Size of the **PartitionKey** | A string up to 1024 characters in size |
| Size of the **RowKey** | A string up to 1024 characters in size |
| Size of an entity group transaction | A transaction can include at most 100 entities and the payload must be less than 4 MiB in size. An entity group transaction can include an update to an entity only once. |
| Maximum number of stored access policies per table | 5 |
| Maximum request rate per storage account | 20,000 transactions per second, which assumes a 1-KiB entity size |
| Target throughput for a single table partition (1 KiB-entities) | Up to 2,000 entities per second |

## Azure subscription creation limits

See [Billing accounts and scopes in the Azure portal](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts) to learn more about creating limits for Azure subscriptions.

## Azure Virtual Desktop Service limits

The following table describes the maximum limits for Azure Virtual Desktop.

| **Azure Virtual Desktop Object**                    | **Per Parent Container Object**                     | **Service Limit**   |
|-----------------------------------------------------|-------------------------------------------------|--------------------------------------------------|
| Workspace                                           | Microsoft Entra tenant                   | 1300 |
| HostPool                                            | Workspace                                       | 400 |
| Application group                                   | Microsoft Entra tenant                   | 1000<sup>1</sup>  |
| RemoteApp                                           | Application group                               | 500 |
| Role Assignment                                     | Any Azure Virtual Desktop Object                | 200 |
| Session Host                                        | HostPool                                        | 10,000 |

<sup>1</sup>If you require over 1000 Application groups then please raise a support ticket via the Azure portal.

All other Azure resources used in Azure Virtual Desktop such as Virtual Machines, Storage, Networking etc. are all subject to their own resource limitations documented in the relevant sections of this article. 
To visualise the relationship between all the Azure Virtual Desktop objects, review this article [Relationships between Azure Virtual Desktop logical components](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/wvd/windows-virtual-desktop#azure-virtual-desktop-limitations).

To get started with Azure Virtual Desktop, use the [getting started guide](https://learn.microsoft.com/en-us/azure/virtual-desktop/overview).
For deeper architectural content for Azure Virtual Desktop, use the [Azure Virtual Desktop section of the Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/wvd/).
For pricing information for Azure Virtual Desktop, add "Azure Virtual Desktop" within the Compute section of the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator).

## Azure VMware Solution limits

## Azure Web PubSub limits

| Resource | Default limit | Maximum limit | 
| --- | --- | --- |
| Azure Web PubSub Service units per instance for Free tier |1 |1 |
| Azure Web PubSub Service units per instance for Standard/Premium_P1 tier |100 |100 |
| Azure Web PubSub Service units per instance for Premium_P2 tier |100 - 1,000 |100 - 1,000 |
| Azure Web PubSub Service units per subscription per region for Free tier|5 |5 |
| Total Azure Web PubSub Service unit counts per subscription per region |150 |Unlimited |
| Concurrent connections per unit for Free tier |20 |20 |
| Concurrent connections per unit for Standard/Premium tier |1,000 |1,000|
| Included messages per unit per day for Free tier|20,000 |20,000 |
| Additional messages per unit per day for Free tier|0 |0 |
| Included messages per unit per day for Standard/Premium tier|1,000,000 |1,000,000 |
| Additional messages per unit per day for Standard/Premium tier|Unlimited |Unlimited |

To request an update to your subscription's default limits, open a support ticket.

For more information about how connections and messages are counted in billing, see [Billing model in Azure Web PubSub Service](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/concept-billing-model).

If your requirements exceed the limits, scale up from Free tier to Standard/Premium tier or scale out units. For more information, see [How to scale an Azure Web PubSub Service instance](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-scale-manual-scale).

If your requirements exceed the limits of a single instance, add instances. For more information, see [How to use Geo-Replication in Azure Web PubSub](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-enable-geo-replication).

## Backup limits

For a summary of Azure Backup support settings and limitations, see [Azure Backup Support Matrices](https://learn.microsoft.com/en-us/azure/backup/backup-support-matrix).

## Batch limits

| **Resource** | **Default limit** | **Maximum limit** |
| --- | --- | --- |
| Azure Batch accounts per region per subscription | 1-3 | 50 |
| Dedicated cores per Batch account | 0-900<sup>1</sup> | Contact support |
| Low-priority cores per Batch account | 0-100<sup>1</sup> | Contact support |
| **[Active](https://learn.microsoft.com/en-us/rest/api/batchservice/jobs/get-job)** jobs and job schedules per Batch account (**completed** jobs have no limit) | 100-300 | 1,000<sup>2</sup> |
| Pools per Batch account | 0-100<sup>1</sup> | 500<sup>2</sup> |
| Private endpoint connections per Batch account | 100 | 100 |

<sup>1</sup> For capacity management purposes, the default quotas for new Batch accounts in some regions and for some subscription
types have been reduced from the above range of values. In some cases, these limits have been reduced to zero. When you create a
new Batch account, [check your quotas](https://learn.microsoft.com/en-us/azure/batch/batch-quota-limit#view-batch-quotas) and
[request an appropriate core or service quota increase](https://learn.microsoft.com/en-us/azure/batch/batch-quota-limit#increase-a-quota), if necessary.
Alternatively, consider reusing Batch accounts that already have sufficient quota or user subscription pool allocation
Batch accounts to maintain core and VM family quota across all Batch accounts on the subscription. Service quotas like
active jobs or pools apply to each distinct Batch account even for user subscription pool allocation Batch accounts.

<sup>2</sup> To request an increase beyond this limit, contact Azure Support.

> [!NOTE]
> Default limits vary depending on the type of subscription you use to create a Batch account. Cores quotas shown are for Batch
> accounts in Batch service mode. [View the quotas in your Batch account](https://learn.microsoft.com/en-us/azure/batch/batch-quota-limit#view-batch-quotas).

## Classic deployment model limits

The following limits apply if you use a classic deployment model instead of the Azure Resource Manager deployment model.

| Resource | Default limit | Maximum limit |
| --- | --- | --- |
| vCPUs per [subscription](https://azure.microsoft.com/pricing/)<sup>1</sup> |20 |10,000 |
| [Coadministrators](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/add-change-subscription-administrator) per subscription |200 |200 |
| [Storage accounts](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create) per subscription<sup>2</sup> |100 |100 |
| [Cloud services](https://learn.microsoft.com/en-us/azure/cloud-services/cloud-services-choose-me) per subscription |20 |200 |
| [Local networks](https://learn.microsoft.com/en-us/previous-versions/azure/reference/jj157100(v=azure.100)) per subscription |10 |500 |
| DNS servers per subscription |9 |100 |
| Reserved IPs per subscription |20 |100 |
| [Affinity groups](https://learn.microsoft.com/en-us/previous-versions/azure/virtual-network/virtual-networks-migrate-to-regional-vnet) per subscription |256 |256 |
| Subscription name length (characters) | 64 | 64 |

<sup>1</sup>Extra small instances count as one vCPU toward the vCPU limit despite using a partial CPU core.

<sup>2</sup>The storage account limit includes both Standard and Premium storage accounts.

## Container Instances limits

| Resource | Actual Limit |
| --- | :--- |
| Standard sku container groups per region per subscription | 100 |
| Dedicated sku container groups per region per subscription | 0<sup>1</sup> |
| Number of containers per container group | 60 |
| Number of volumes per container group | 20 |
| Standard sku cores (CPUs) per region per subscription | 100 | 
| Standard sku cores (CPUs) for K80 GPU per region per subscription | 0 |
| Standard sku cores (CPUs) for V100 GPU per region per subscription | 0 |
| Ports per IP | 5 |
| Container instance log size - running instance | 4 MB |
| Container instance log size - stopped instance | 16 KB or 1,000 lines |
| Container group creates per hour |300<sup>1</sup> |
| Container group creates per 5 minutes | 100<sup>1</sup> |
| Container group deletes per hour | 300<sup>1</sup> |
| Container group deletes per 5 minutes | 100<sup>1</sup> |

<sup>1</sup>To request a limit increase, create an [Azure Support request][azure-support]. Free subscriptions including [Azure Free Account](https://azure.microsoft.com/pricing/offers/ms-azr-0044p?cid=msft_learn) and [Azure for Students](https://azure.microsoft.com/offers/ms-azr-0170p/) aren't eligible for limit or quota increases. If you have a free subscription, you can [upgrade](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/upgrade-azure-subscription) to a Pay-As-You-Go subscription.<br />
<sup>2</sup>Default limit for [Pay-As-You-Go](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn) subscription. Limit may differ for other category types.<br/>

[azure-support]: https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest

## Azure Container Registry limits

The following table details the features and limits of the Basic, Standard, and Premium [Azure Container Registry service tiers](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus).

## Azure Content Delivery Network limits

| Resource | Limit |
| --- | --- |
| Azure Content Delivery Network profiles | 25 |
| Content Delivery Network endpoints per profile | 25 |
| Custom domains per endpoint | 25 |
| Maximum origin group per profile | 10 |
| Maximum origin per origin group | 10 |
| Maximum number of rules per CDN endpoint | 25 |
| Maximum number of match conditions per rule	| 10 |
| Maximum number of actions per rule	| 5 |
| Maximum bandwidth per profile* | 75 Gbps |
| Maximum requests per second per profile | 100,000 |
| HTTP header size limit (per header) | 32 KB |

*These two limits are only applicable to Azure CDN Standard from Microsoft (classic). If the traffic isn't globally distributed and concentrated in one or two regions, or if a higher quota limit is needed, create an [Azure Support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). 

A Content Delivery Network subscription can contain one or more Content Delivery Network profiles. A Content Delivery Network profile can contain one or more Content Delivery Network endpoints. You might want to use multiple profiles to organize your Content Delivery Network endpoints by internet domain, web application, or some other criteria.

## Azure Data Lake Analytics limits

Azure Data Lake Analytics makes the complex task of managing distributed infrastructure and complex code easy. It dynamically provisions resources, and you can use it to do analytics on exabytes of data. When the job completes, it winds down resources automatically. You pay only for the processing power that was used. As you increase or decrease the size of data stored or the amount of compute used, you don't have to rewrite code. To raise the default limits for your subscription, contact support.

| **Resource** | **Limit** | **Comments** |
| --- | --- | --- |
| Maximum number of concurrent jobs |20 | |
| Maximum number of analytics units (AUs) per account |250 | Use any combination of up to a maximum of 250 AUs across 20 jobs. To increase this limit, contact Microsoft Support. |
| Maximum script size for job submission | 3 MB | |
| Maximum number of Data Lake Analytics accounts per region per subscription | 5 | To increase this limit, contact Microsoft Support. |

## Azure Data Lake Storage limits

**Azure Data Lake Storage Gen2** is not a dedicated service or storage account type. It is the latest release of capabilities that are dedicated to big data analytics.  These capabilities are available in a general-purpose v2 or BlockBlobStorage storage account, and you can obtain them by enabling the **Hierarchical namespace** feature of the account. For scale targets, see these articles. 

- [Scale targets for Blob storage](https://learn.microsoft.com/en-us/azure/storage/blobs/scalability-targets#scale-targets-for-blob-storage).
- [Scale targets for standard storage accounts](../articles/storage/common/scalability-targets-standard-account.md?toc=%2fazure%2fstorage%2fblobs%2ftoc.json#scale-targets-for-standard-storage-accounts-and-disk-access-resources).

**Azure Data Lake Storage Gen1** is a dedicated service. It's an enterprise-wide hyper-scale repository for big data analytic workloads. You can use Data Lake Storage Gen1 to capture data of any size, type, and ingestion speed in one single place for operational and exploratory analytics. There's no limit to the amount of data you can store in a Data Lake Storage Gen1 account.

| **Resource** | **Limit** | **Comments** |
| --- | --- | --- |
| Maximum number of Data Lake Storage Gen1 accounts, per subscription, per region |10 | To request an increase for this limit, contact support. |
| Maximum number of access ACLs, per file or folder |32 | This is a hard limit. Use groups to manage access with fewer entries. |
| Maximum number of default ACLs, per file or folder |32 | This is a hard limit. Use groups to manage access with fewer entries. |

## Azure Data Share limits

Azure Data Share enables organizations to simply and securely share data with their customers and partners.

| **Resource** | **Limit** |
| --- | --- |
| Maximum number of Data Share resources per Azure subscription |100 |
| Maximum number of sent shares per Data Share resource |200 |
| Maximum number of received shares per Data Share resource |100 |
| Maximum number of invitations per sent share |200 |
| Maximum number of share subscriptions per sent share |200 |
| Maximum number of datasets per share |200 |
| Maximum number of snapshot schedules per share |1 |

## Azure Database Migration Service Limits

Azure Database Migration Service is a fully managed service designed to enable seamless migrations from multiple database sources to Azure data platforms with minimal downtime.

| **Resource** | **Limit** | **Comments** |
| --- | --- | --- |
| Maximum number of services per subscription, per region |10 | To request an increase for this limit, contact support. |

## Azure Device Registry limits

## Azure Device Update for IoT Hub limits

Limits can be adjusted only for the Standard SKU. Limit adjustment requests are evaluated on a case-by-case basis, and approvals aren't guaranteed.

Limit adjustment requests aren't accepted for the Free SKU. Also, Free SKU instances can't be upgraded to Standard SKU instances.

The following table shows the limits for the Device Update for IoT Hub resource in Azure Resource Manager.

| Resource |  Standard SKU limit | Free SKU limit | Adjustable for Standard SKU? |
| --- | --- | --- | --- | 
| Accounts per subscription | 50 | 1 | No |
| Instances per account | 50 | 1 | No |
| Length of account name | 3-24 characters | 3-24 characters | No |
| Length of instance name | 3-36 characters | 3-36 characters | No |

The following table shows the limits associated with various Device Update operations.

| Operation | Standard SKU limit | Free SKU limit | Adjustable for Standard SKU? |
| --- | --- | --- | --- |
| Number of devices per instance | 1 million | 10 | Yes |
| Number of device groups per instance | 100 | 10 | Yes |
| Number of device classes per instance | 80 | 10 | Yes |
| Number of active deployments per instance | 50, including one reserved for cancellations | 5, including one reserved for cancellations | Yes |
| Number of total deployments per instance, including all active, inactive, and canceled deployments that aren't deleted | 100 | 20 | No |
| Number of update providers per instance | 25 | 2 | No |
| Number of update names per provider per instance | 25 | 2 | No |
| Number of update versions per update provider and name per instance | 100 | 5 | No |
| Total number of updates per instance | 100 | 10 | No |
| Maximum single update file size | 2 GB | 2 GB | Yes |
| Maximum combined size of all files in a single import action | 2 GB | 2 GB | Yes |
| Maximum number of files in a single update | 10 | 10 | No |
| Total data storage included per instance | 100 GB | 5 GB | No |

> [!NOTE]
> Canceled or inactive deployments count toward your total deployment limit. Make sure to clean up these deployments periodically so you aren't prevented from creating new deployments.

## Azure Digital Twins limits

> [!NOTE]
> Some areas of this service have adjustable limits, and others do not. The following tables use the *Adjustable?* column to represent this condition. When the limit can be adjusted, the *Adjustable?* value is *Yes*.

## Azure Event Grid limits

## Azure Event Hubs limits
The following tables provide quotas and limits specific to [Azure Event Hubs](https://azure.microsoft.com/services/event-hubs/). For information about Event Hubs pricing, see [Event Hubs pricing](https://azure.microsoft.com/pricing/details/event-hubs/).

### Common limits for all tiers

### Basic vs. standard vs. premium vs. dedicated tiers

## Azure IoT Central limits
IoT Central limits the number of applications you can deploy in a subscription to 100. To learn more, see [Azure IoT Central quota and limits](https://learn.microsoft.com/en-us/azure/iot-central/core/concepts-quotas-limits).

## Azure IoT Hub limits

The following table lists the limits associated with the different service tiers S1, S2, S3, and F1. For information about the cost of each *unit* in each tier, see [Azure IoT Hub pricing](https://azure.microsoft.com/pricing/details/iot-hub/).

| Resource | S1 Standard | S2 Standard | S3 Standard | F1 Free |
| --- | --- | --- | --- | --- |
| Messages/day |400,000 |6,000,000 |300,000,000 |8,000 |
| Maximum units |200 |200 |10 |1 |

The following table lists the limits that apply to IoT Hub resources.

| Resource | Limit |
| --- | --- |
| Maximum paid IoT hubs per Azure subscription |50 |
| Maximum free IoT hubs per Azure subscription |1 |
| Maximum number of characters in a device ID | 128 |
| Maximum number of device identities<br/> returned in a single call |1,000 |
| IoT Hub message maximum retention for device-to-cloud messages |7 days |
| Maximum size of device-to-cloud message |256 KB |
| Maximum size of device-to-cloud batch |AMQP and HTTP: 256 KB for the entire batch <br/>MQTT: 256 KB for each message |
| Maximum messages in device-to-cloud batch |500 |
| Maximum size of cloud-to-device message |64 KB |
| Maximum TTL for cloud-to-device messages |2 days |
| Maximum delivery count for cloud-to-device <br/> messages |100 |
| Maximum cloud-to-device queue depth per device |50 |
| Maximum delivery count for feedback messages <br/> in response to a cloud-to-device message |100 |
| Maximum TTL for feedback messages in <br/> response to a cloud-to-device message |2 days |
| [Maximum size of device twin](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins#device-twin-size) | 8 KB for tags section, and 32 KB for desired and reported properties sections each |
| Maximum length of device twin string key | 1 KB |
| Maximum length of device twin string value | 4 KB |
| [Maximum depth of object in device twin](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins#tags-and-properties-format) | 10 |
| Maximum size of direct method payload | 128 KB |
| Job history maximum retention | 30 days |
| Maximum concurrent jobs | 10 (for S3), 5 for (S2), 1 (for S1) |
| Maximum additional endpoints (beyond [built-in endpoints](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-endpoints)) | 10 (for S1, S2, and S3) |
| Maximum message routing rules | 100 (for S1, S2, and S3) |
| Maximum number of concurrently connected device streams | 50 (for S1, S2, S3, and F1 only) |
| Maximum device stream data transfer | 300 MB per day (for S1, S2, S3, and F1 only) |

> [!NOTE]
> The total number of devices plus modules that can be registered to a single IoT hub is capped at 1,000,000.

IoT Hub throttles requests when the following quotas are exceeded.

| Throttle | Per-hub value |
| --- | --- |
| Identity registry operations <br/> (create, retrieve, list, update, and delete), <br/> individual or bulk import/export |83.33/sec/unit (5,000/min/unit) (for S3). <br/> 1.67/sec/unit (100/min/unit) (for S1 and S2). |
| Device connections |6,000/sec/unit (for S3), 120/sec/unit (for S2), 12/sec/unit (for S1). <br/>Minimum of 100/sec. |
| Device-to-cloud sends |6,000/sec/unit (for S3), 120/sec/unit (for S2), 12/sec/unit (for S1). <br/>Minimum of 100/sec. |
| Cloud-to-device sends | 83.33/sec/unit (5,000/min/unit) (for S3), 1.67/sec/unit (100/min/unit) (for S1 and S2). |
| Cloud-to-device receives |833.33/sec/unit (50,000/min/unit) (for S3), 16.67/sec/unit (1,000/min/unit) (for S1 and S2). |
| File upload operations |83.33 file upload initiations/sec/unit (5,000/min/unit) (for S3), 1.67 file upload initiations/sec/unit (100/min/unit) (for S1 and S2). <br/> 10 concurrent file uploads per device. |
| Direct methods | 24 MB/sec/unit (for S3), 480 KB/sec/unit (for S2), 160 KB/sec/unit (for S1).<br/> Based on 8-KB throttling meter size. |
| Device twin reads | 500/sec/unit (for S3), Maximum of 100/sec or 10/sec/unit (for S2), 100/sec (for S1) |
| Device twin updates | 250/sec/unit (for S3), Maximum of 50/sec or 5/sec/unit (for S2), 50/sec (for S1) |
| Jobs operations <br/> (create, update, list, and delete) | 83.33/sec/unit (5,000/min/unit) (for S3), 1.67/sec/unit (100/min/unit) (for S2), 1.67/sec/unit (100/min/unit) (for S1). |
| Jobs per-device operation throughput | 50/sec/unit (for S3), maximum of 10/sec or 1/sec/unit (for S2), 10/sec (for S1). |
| Device stream initiation rate | 5 new streams/sec (for S1, S2, S3, and F1 only). |

### IoT Hub with ADR integration (preview) limits

The following table lists the limits that apply to IoT Hub (preview) instances.

|Feature|Limit|
|----------------------------------|-------------------------------|
|Number of devices per IoT Hub (preview) instance    | 10,000|
|Number of IoT Hub (preview) instances per ADR namespace | 3|
|Protocols supported for certificate provisioning|HTTP, MQTT, and MQTT-Web-Sockets protocols. |

All other throttles, limits to IoT Hub preview resources are equivalent to a S1 standard IoT Hub

The following table lists the limits that apply to [ADR integration](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-device-registry-overview).

| Feature    | Limit|
|----------------------------------|-------------------------------|
|Number of ADR namespaces per Azure subscription    | 100|
|Number of device create per minute    | 500 devices per minute per subscription|
|Number of devices to be disabled per minute    | 500|
|Number of devices to be enabled per minute    | 500|

For more information, you can view the [full list of ADR limits](#azure-device-registry-limits).

## Azure IoT Hub Device Provisioning Service limits

Some areas of this service have adjustable limits. The tables below include an *Adjustable?* column. If the limit is adjustable, the *Adjustable?* value is *Yes*.

The actual value that you can adjust a limit to might vary based on your deployment. Very large deployments might require multiple instances of DPS.

If your business requires a higher adjustable limit or quota, [open a support ticket](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest) to request additional resources. An increase request isn't guaranteed because each case requires individual review. Contact Microsoft support as early as possible during your implementation so the team can determine whether to approve your request and help you plan accordingly.

The following table lists the limits that apply to Azure IoT Hub Device Provisioning Service resources.

| Resource | Limit | Adjustable? |
| --- | --- | --- |
| Maximum device provisioning services per Azure subscription | 10 | Yes |
| Maximum number of registrations | 1,000,000 | Yes |
| Maximum number of individual enrollments | 1,000,000 | Yes |
| Maximum number of enrollment groups *(X.509 certificate)* | 100 | Yes |
| Maximum number of enrollment groups *(symmetric key)* | 100 | No |
| Maximum number of CAs | 25 | Yes |
| Maximum number of linked IoT hubs | 50 | No |
| Maximum size of message | 96 KB| No |

> [!TIP]
> If the hard limit on symmetric key enrollment groups is a blocking issue, use individual enrollments as a workaround.

The Device Provisioning Service has the following rate limits.

| Rate | Per-unit value | Adjustable? |
| --- | --- | --- |
| Operations | 1,000/min/service | Yes |
| Device registrations | 1,000/min/service | Yes |
| Device polling operation | 5/10 sec/device | No |

## Azure Key Vault limits

## Azure Key Vault: Managed HSM limits

## Azure Managed Identity limits

- Each managed identity counts towards the object quota limit in a Microsoft Entra tenant as described in [Microsoft Entra service limits and restrictions](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/directory-service-limits-restrictions).
-	The rate at which managed identities can be created have the following limits:

    1. Per Microsoft Entra tenant per Azure region: 400 create operations per 20 seconds.
    2. Per Azure Subscription per Azure region : 80 create operations per 20 seconds.

-	The rate at which a user-assigned managed identity can be assigned with an Azure resource :

    1. Per Microsoft Entra tenant per Azure region: 400 assignment operations per 20 seconds.
    2. Per Azure Subscription per Azure region : 300 assignment operations per 20 seconds.

## Azure Media Services limits

> [!NOTE]
> For resources that aren't fixed, open a support ticket to ask for an increase in the quotas. Don't create additional Azure Media Services accounts in an attempt to obtain higher limits.

### Account limits

| Resource | Default Limit |
| --- | --- |
| Media Services accounts in a single subscription | 100 (fixed) |

### Asset limits

| Resource | Default Limit |
| --- | --- |
| Assets per Media Services account | 1,000,000|

### Storage (media) limits

| Resource | Default Limit |
| --- | --- |
| File size| In some scenarios, there is a limit on the maximum file size supported for processing in Media Services. <sup>(1)</sup> |
| Storage accounts | 100<sup>(2)</sup> (fixed) |

<sup>1</sup> The maximum size supported for a single blob is currently up to 5 TB in Azure Blob Storage. Additional limits apply in Media Services based on the VM sizes that are used by the service. The size limit applies to the files that you upload and also the files that get generated as a result of Media Services processing (encoding or analyzing). If your source file is larger than 260-GB, your Job will likely fail.

<sup>2</sup> The storage accounts must be from the same Azure subscription.

### Jobs (encoding & analyzing) limits

| Resource | Default Limit |
| --- | --- |
| Jobs per Media Services account | 500,000 <sup>(3)</sup> (fixed)|
| Job inputs per Job | 50  (fixed)|
| Job outputs per Job | 20 (fixed) |
| Transforms per Media Services account | 100  (fixed)|
| Transform outputs in a Transform | 20 (fixed) |
| Files per job input|10 (fixed)|

<sup>3</sup> This number includes queued, finished, active, and canceled Jobs. It does not include deleted Jobs.

Any Job record in your account older than 90 days will be automatically deleted, even if the total number of records is below the maximum quota.

### Live streaming limits

| Resource | Default Limit |
| --- | --- |
| Live Events <sup>(4)</sup> per Media Services account |5|
| Live Outputs per Live Event |3 <sup>(5)</sup> |
| Max Live Output duration | [Size of the DVR window](https://learn.microsoft.com/en-us/azure/media-services/latest/live-event-cloud-dvr-time-how-to) |

<sup>4</sup> For detailed information about Live Event limitations, see [Live Event types comparison and limitations](https://learn.microsoft.com/en-us/azure/media-services/latest/live-event-types-comparison-reference).

<sup>5</sup> Live Outputs start on creation and stop when deleted.

### Packaging & delivery limits

| Resource | Default Limit |
| --- | --- |
| Streaming Endpoints (stopped or running) per Media Services account| 2 |
| Dynamic Manifest Filters|100|
| Streaming Policies | 100 <sup>(6)</sup> |
| Unique Streaming Locators associated with an Asset at one time | 100<sup>(7)</sup> (fixed) |

<sup>6</sup> When using a custom [Streaming Policy](https://learn.microsoft.com/en-us/cli/azure/ams/streaming-policy), you should design a limited set of such policies for your Media Service account, and re-use them for your StreamingLocators whenever the same encryption options and protocols are needed. You should not be creating a new Streaming Policy for each Streaming Locator.

<sup>7</sup> Streaming Locators are not designed for managing per-user access control. To give different access rights to individual users, use Digital Rights Management (DRM) solutions.

### Protection limits

| Resource | Default Limit |
| --- | --- |
| Options per Content Key Policy | 30 |
| Licenses per month for each of the DRM types on Media Services key delivery service per account|1,000,000|

### Support ticket

For resources that are not fixed, you may ask for the quotas to be raised, by opening a [support ticket](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Include detailed information in the request on the desired quota changes, use-case scenarios, and regions required. <br/>Do **not** create additional Azure Media Services accounts in an attempt to obtain higher limits.

### Azure Media Services v2 (legacy)

For limits specific to Media Services v2 (legacy), see [Media Services v2 (legacy)]

## Azure Mobile Services limits

| Tier | Free | Basic | Standard |
| --- | --- | --- | --- |
| API calls |500,000 |1.5 million per unit |15 million per unit |
| Active devices |500 |Unlimited |Unlimited |
| Scale |N/A |Up to 6 units |Unlimited units |
| Push notifications |Azure Notification Hubs Free tier included, up to 1 million pushes |Notification Hubs Basic tier included, up to 10 million pushes |Notification Hubs Standard tier included, up to 10 million pushes |
| Real-time messaging/<br/>WebSockets |Limited |350 per mobile service |Unlimited |
| Offline synchronizations |Limited |Included |Included |
| Scheduled jobs |Limited |Included |Included |
| Azure SQL Database (required) <br/>Standard rates apply for additional capacity |20 MB included |20 MB included |20 MB included |
| CPU capacity |60 minutes per day |Unlimited |Unlimited |
| Outbound data transfer |165 MB per day (daily rollover) |Included |Included |

For more information on limits and pricing, see [Azure Mobile Services pricing](https://azure.microsoft.com/pricing/details/mobile-services/).

## Azure networking limits

### <a name="azure-resource-manager-virtual-networking-limits"></a>Networking limits - Azure Resource Manager
The following limits apply only for networking resources managed through **Azure Resource Manager** per region per subscription. Learn how to [view your current resource usage against your subscription limits](https://learn.microsoft.com/en-us/azure/networking/check-usage-against-limits).

> [!NOTE]
> We have increased all default limits to their maximum limits. If there's no maximum limit column, the resource doesn't have adjustable limits. If you had these limits manually increased by support in the past and are currently seeing limits lower than what is listed in the following tables, [open an online customer support request at no charge](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/error-resource-quota)

| Resource | Limit | 
| --- | --- |
| Virtual networks |1,000 |
| Subnets per virtual network |3,000 |
| Virtual network peerings per virtual network |650 |
| [Virtual network gateways (VPN gateways) per virtual network](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus#benchmark) |1 |
| [Virtual network gateways (ExpressRoute gateways) per virtual network](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-virtual-network-gateways#gwsku) |1 |
| DNS servers per virtual network |20 |
| DNS servers per network interface |20 |
| Private IP addresses per virtual network |65,536 |
| Total Private Addresses for a group of Peered Virtual networks | 128,000 |
| Private IP addresses per network interface |256 |
| Private IP addresses per virtual machine |256 * N (N is number of NICs on VM) |
| Public IP addresses per network interface |256 |
| Public IP addresses per virtual machine |256 |
| [Concurrent TCP or UDP flows per NIC of a virtual machine or role instance](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-machine-network-throughput#flow-limits-and-active-connections-recommendations) |500,000 |
| Network interface cards |65,536 |
| Network Security Groups |5,000 |
| NSG rules per NSG |2,000 |
| IP addresses and ranges specified for source or destination in a security group (The limit applies separately to source and destination) |6,000 |
| Application security groups |3,000 |
| Application security groups per IP configuration, per NIC | 20 |
| Application security groups referenced as source/destination per NSG rule | 10 |
| IP configurations per application security group |4,000 |
| Application security groups that can be specified within all security rules of a network security group |100 |
| User-defined route tables |600 |
| User-defined routes per route table |1,000 |
| Routes with service tag per route table | 25 |
| Point-to-site root certificates per Azure VPN Gateway |20 |
| Point-to-site revoked client certificates per Azure VPN Gateway |300 |
| Virtual network TAP configurations per subscription |10 |

#### <a name="publicip-address"></a>Public IP address limits
| Resource | Default limit | Maximum limit |
| --- | --- | --- |
| Basic Public IPv4, IPv6 addresses<sup>1,2,3</sup> | 10 | Contact support |
| Standard Public IPv4, IPv6 addresses<sup>1</sup> | 10 | Contact support |
| Global Tier Public IPv4, IPv6 addresses<sup>1</sup> | 10 | Contact support |
| Routing Preference Internet Public IPv4, IPv6 addresses<sup>1</sup> | 10 | Contact support |
| Public IP prefixes | limited by number of Standard Public IPs in a subscription | Contact support |
| Public IP prefix length | /28 | Contact support |
| Custom IP prefixes | 5 | Contact support |

<sup>1</sup>Default limits for Public IPv4/v6 addresses vary by offer category type, such as Free Trial, pay-as-you-go, CSP. For example, the default for Enterprise Agreement subscriptions is 1000 and the default for pay-as-you-go is 20. The majority of offers start at 10.  There's also an overall maximum number of Public IP addresses per subscription.

<sup>2</sup>Basic Public IP addresses are retired as of September 30, 2025. See [here](https://azure.microsoft.com/updates?id=upgrade-to-standard-sku-public-ip-addresses-in-azure-by-30-september-2025-basic-sku-will-be-retired) for more details.

<a name="virtual-networking-limits-classic"></a>The following limits apply only for networking resources managed through the **classic** deployment model per subscription. Learn how to [view your current resource usage against your subscription limits](https://learn.microsoft.com/en-us/azure/networking/check-usage-against-limits).

| Resource | Default limit | Maximum limit |
| --- | --- | --- |
| Virtual networks |100 |100 |
| Local network sites |20 |50 |
| DNS servers per virtual network |20 |20 |
| Private IP addresses per virtual network |4,096 |4,096 |
| Concurrent TCP or UDP flows per NIC of a virtual machine or role instance |500,000, up to 1,000,000 for two or more NICs. |500,000, up to 1,000,000 for two or more NICs. |
| Network Security Groups (NSGs) |200 |200 |
| NSG rules per NSG |200 |1,000 |
| User-defined route tables |200 |200 |
| User-defined routes per route table |600 |600 |
| Public IP addresses (dynamic) |500 |500 |
| Reserved public IP addresses |500 |500 |
| Public IP per deployment |5 |Contact support |
| Private IP (internal load balancing) per deployment |1 |1 |
| Endpoint access control lists (ACLs) |50 |50 |

### <a name="load-balancer"></a>Azure Load Balancer limits
### Standard Load Balancer

| Resource                                | Limit         |
|-----------------------------------------|-------------------------------|
| Load balancers                          | 1,000                         |
| Frontend IP configurations              | 600                           |
| Rules (Load Balancer + Inbound NAT) per resource  | 1,500               |
| Rules per NIC (across all IPs on a NIC)<sup>1<sup> | 300                           |
| High-availability ports rule            | 1 per internal frontend       |
| Outbound rules per Load Balancer        | 600                           |
| Backend pool size                       | 5,000                         |
| IP configurations per Load Balancer (across all backend pools) | 20,000 |
| Azure global Load Balancer Backend pool size                       | 300                         |
| Backend IP configurations per frontend <sup>2<sup> | 10,000                        |
| Backend IP configurations across all frontends | 500,000 |

<sup>1<sup> Each NIC can have a total of 300 rules (load balancing, inbound NAT, and outbound rules combined) configured across all IP configurations on the NIC.
<sup>2</sup> Backend IP configurations are aggregated across all load balancer rules including load balancing, inbound NAT, and outbound rules. Each rule a backend pool instance is configured to counts as one configuration.

Load Balancer doesn't apply any throughput limits. However, throughput limits for virtual machines and virtual networks still apply. For more information, see [Virtual machine network bandwidth](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-machine-network-throughput).

### Gateway Load Balancer

| Resource                                | Limit        |
|-----------------------------------------|------------------------------|
| Resources chained per Gateway Load Balancer frontend (Load Balancer frontend configurations or VM NIC IP configurations combined) | 100 |

All limits for Standard Load Balancer also apply to Gateway Load Balancer.

### Basic Load Balancer

| Resource                                | Limit        |
|-----------------------------------------|------------------------------|
| Load balancers                          | 1,000                        |
| Rules per resource                      | 250                          |
| Rules per NIC (across all IPs on a NIC) | 300                          |
| Frontend IP configurations <sup>3<sup>  | 200                          |
| Backend pool size                       | 300 IP configurations, single availability set |
| Availability sets per Load Balancer     | 1                            |
| Load Balancers per VM                   | 2 (1 Public and 1 internal)  |

<sup>3</sup> The limit for a single discrete resource in a backend pool (standalone virtual machine, availability set, or virtual machine scale-set placement group) is to have up to 250 Frontend IP configurations across a single Basic Public Load Balancer and Basic Internal Load Balancer.

### Azure Application Gateway limits

The following table applies to v1, v2, Standard, and WAF SKUs unless otherwise stated.
| Resource | Limit | Note |
| --- | --- | --- |
| Azure Application Gateway |1,000 per region per subscription | |
| Frontend IP configurations |4 |IPv4 - 1 public and 1 private.<br>IPv6 - 1 public and 1 private. |
| Frontend ports |100<sup>1</sup> | |
| Backend address pools |100 | |
| Backend targets per pool |1,200 | |
| HTTP listeners |200<sup>1</sup> |Limited to 100 active listeners that are routing traffic. Active listeners = total number of listeners - listeners not active.<br>If a default configuration inside a routing rule is set to route traffic (for example, it has a listener, a backend pool, and HTTP settings) then that also counts as a listener. For more information, see [Frequently asked questions about Application Gateway](../articles/application-gateway/application-gateway-faq.yml#what-is-an-active-listener-versus-an-inactive-listener).|
| HTTP load-balancing rules |400<sup>1</sup> | |
| Backend HTTP settings |100<sup>1</sup> | |
| Instances per gateway |V1 SKU - 32<br>V2 SKU - 125 | |
| SSL certificates |100<sup>1</sup> |1 per HTTP listener |
| Maximum SSL certificate size |V1 SKU - 10 KB<br>V2 SKU - 16 KB| |
| Maximum trusted client CA certificate size | 25 KB| 25 KB is the maximum aggregated size of root and intermediate certificates contained in an uploaded pem or cer file. |
| Maximum trusted client CA certificates |200 | 100 per SSL Profile |
| Authentication certificates |100 | |
| Trusted root certificates |100 | |
| Request timeout minimum |1 second | |
| Request timeout maximum to private backend |24 hours | |
| Request timeout maximum to external backend |4 minutes | |
| Number of sites |100<sup>1</sup> |1 per HTTP listener |
| URL maps per listener |1 | |
| Host names per listener |5 | |
| Maximum path-based rules per URL map|100||
| Redirect configurations |100<sup>1</sup>| |
| Number of rewrite rule sets |400| |
| Number of Header or URL configuration per rewrite rule set|40| |
| Number of conditions per rewrite rule set|40| |
| Concurrent WebSocket connections |Medium gateways 20k<sup>2</sup><br> Large gateways 50k<sup>2</sup>| |
| Maximum URL length|32 KB| |
| Maximum header size|32 KB| |
| Maximum header field size for HTTP/2|8 KB| |
| Maximum header size for HTTP/2|16 KB| |
| Maximum requests per HTTP/2 connection| 1000 | The total number of requests that can share the same frontend HTTP/2 connection|
| Maximum file upload size (Standard SKU) |V1 - 2 GB<br>V2 - 4 GB |This maximum size limit is shared with the request body|
| Maximum file upload size (WAF SKU)<sup>3</sup> |V1 Medium - 100 MB<br>V1 Large - 500 MB<br>V2 - 750 MB<br>V2 (with CRS 3.2 or DRS) - 4 GB<sup>4</sup>|1 MB - Minimum Value<br>100 MB - Default value<br>V2 with CRS 3.2 or DRS - can be turned On/Off|
| Maximum request size limit Standard SKU (without files)|V1 - 2 GB<br>V2 - 4 GB | |
| Maximum custom request size limit WAF SKU (without files)|V1 or V2 (with CRS 3.1 and older) - 128 KB<br>V2 (with CRS 3.2 or DRS) - 2 MB<sup>4</sup> with feature enabled<br>2GB - with feature disabled|8 KB - Minimum Value<br>128 KB - Default value<br>V2 with CRS 3.2 or DRS - can be turned On/Off|
| Maximum request inspection limit WAF SKU| V1 or V2 (with CRS 3.1 and older) - 128 KB<br>V2 (with CRS 3.2 or DRS) - 2 MB<sup>4</sup>|8 KB - Minimum Value<br>128 KB - Default value<br>V2 with CRS 3.2 or DRS - can be turned On/Off|
| Maximum Private Link Configurations| 2 | 1 for public IP, 1 for private IP |
| Maximum Private Link IP Configurations| 8 | |
| Maximum WAF custom rules per WAF policy|100||
| Maximum WAF match conditions per custom rule|10|This limit is not enforced by the WAF. Adding more than 10 match conditions can lead to performance degradation|
| WAF IP address ranges per match condition|540<br>600 - with CRS 3.2 or DRS|
| Maximum WAF exclusions per Application Gateway|40<br>200 - with CRS 3.2 or DRS|
| WAF string match values per match condition|10||

<sup>1</sup> The number of resources listed in the table applies to standard Application Gateway SKUs and WAF-enabled SKUs running CRS 3.2 or DRS. For WAF-enabled SKUs running CRS 3.1 or lower, the supported number is 40. For more information, see [WAF engine](https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/waf-engine).

<sup>2</sup> Limit is per Application Gateway instance not per Application Gateway resource.

<sup>3</sup> There is a 4 KB buffer on the file upload limit. The file size restriction won't be enforced until the file upload exceeds your set limit plus this buffer.

<sup>4</sup> Must define the value via WAF Policy for Application Gateway.

### Azure Application Gateway for Containers limits

| Resource | Limit |
| --- | --- |
| Application Gateway for Containers | 1000 per subscription |
| Associations | 1 per gateway |
| Frontends | 5 per gateway |

Kubernetes Ingress and Gateway API configuration limits

| Resource | Limit |
| --- | --- |
| Resource naming | 128 characters |
| Namespace naming | 128 characters |
| Listeners per gateway | 64 listeners per gateway resource (enforced by Gateway API) |
| Total AGC references | 5 per ALB controller |
| Total certificate references | 100 per AGC |
| Total listeners | 200 per AGC |
| Total routes | 200 per AGC |
| Total rules | 200 per AGC |
| Total services | 100 per AGC |
| Total endpoints | 5000 per AGC |

### Azure Bastion limits

An instance is an optimized Azure VM that is created when you configure Azure Bastion. When you configure Azure Bastion using the Basic SKU, 2 instances are created. If you use the Standard SKU, you can specify the number of instances between 2-50.

| Workload Type* | Session Limit per Instance** |
| --- | --- |
| Light |25 |
| Medium |20 |
| Heavy |2 |

*These workload types are defined here: [Remote Desktop workloads](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remote-desktop-workloads)<br>
**These limits are based on RDP performance tests for Azure Bastion. The numbers may vary due to other on-going RDP sessions or other on-going SSH sessions.

### Azure DNS limits

#### Public DNS

##### Public DNS zones

| Resource | Limit |
| --- | --- |
| Public DNS zones per subscription |250 <sup>1</sup> |
| Record sets per public DNS zone |10,000 <sup>1</sup> |
| Records per record set in public DNS zone |20 <sup>1</sup> |
| TXT Records per record set in public DNS zone |400 |
| Number of Alias records for a single Azure resource |50|

<sup>1</sup>If you need to increase these quota limits, contact Azure Support.

##### Public DNS zone operations

| Operation | Limit (per zone) |
| --------- | ----- |
| Create | 40/min |
| Delete | 40/min |
| Get | 1000/min |
| List | 60/min |
| List By Resource Group | 60/min (per resource group) |
| Update | 40/min |

##### Public DNS resource record operations

| Operation | Limit (per zone) |
| --------- | ----- |
| Create | 200/min |
| Delete | 200/min |
| Get | 2000/min |
| List By DNS Zone | 60/min |
| List By Type | 60/min |
| Update | 200/min |

#### Private DNS

##### Private DNS zones

| Resource | Limit |
| --- | --- |
| Private DNS zones per subscription |1000|
| Record sets per private DNS zone |25000|
| Records per record set for private DNS zones |20|
| Virtual Network Links per private DNS zone |1000|
| Virtual Networks Links per private DNS zones with autoregistration enabled |100|
| Number of private DNS zones a virtual network can get linked to with autoregistration enabled |1|
| Number of private DNS zones a virtual network can get linked |1000|

##### Private DNS zone operations

| Operation | Limit (per subscription) |
| --- | --- |
| Create |40/min|
| Delete |40/min|
| Get |200/min<sup> (per zone)|
| List by subscription |60/min|
| List by resource group |100/min (per resource group)|
| Update |40/min|

##### Private DNS resource record operations

| Operation | Limit (per zone)|
| --- | --- |
| Create |60/min|
| Delete |60/min|
| Get |200/min|
| List |100/min|
| Update |60/min|

#### Virtual network links operations

| Operation | Limit (per zone) |
| --- | --- |
| Create |60/min|
| Delete |60/min|
| Get |100/min|
| List by virtual network |20/min|
| Update |60/min|

#### Azure-provided DNS resolver VM limits

| Resource | Limit |
| --- | --- |
| Number of DNS queries a virtual machine can send to Azure DNS resolver, per second |1000 <sup>1</sup> |
| Maximum number of DNS queries queued (pending response) per virtual machine |200 <sup>1</sup> |

<sup>1</sup>These limits are applied to every individual virtual machine and not at the virtual network level. DNS queries exceeding these limits are dropped. These limits apply to the default Azure resolver, not the DNS private resolver.

#### DNS Private Resolver<sup>1</sup>

| Resource | Limit |
| --- | --- |
| DNS private resolvers per subscription |15|
| DNS private resolvers per virtual network |1|
| Inbound endpoints per DNS private resolver |5|
| Outbound endpoints per DNS private resolver |5|
| Forwarding rules per DNS forwarding ruleset |1000|
| Virtual network links per DNS forwarding ruleset |500|
| DNS forwarding ruleset linked to a virtual network |1|
| Outbound endpoints per DNS forwarding ruleset |2|
| DNS forwarding rulesets per outbound endpoint |2|
| Target DNS servers per forwarding rule |6|
| QPS per endpoint |10,000|

<sup>1</sup>Different limits might be enforced by the Azure portal until the portal is updated. Use PowerShell to provision elements up to the most current limits.

### Azure Firewall limits

| Resource | Limit |
| --- | --- |
| Azure Firewalls per virtual network | 1 |
| Max Data throughput | 100 Gbps for Premium, 30 Gbps for Standard, 250 Mbps for Basic (preview) SKU<br><br> For more information, see [Azure Firewall performance](https://learn.microsoft.com/en-us/azure/firewall/firewall-performance#performance-data). |
| Rule limits | 20,000 unique source-destination combinations in network rules <br><br> **Unique source-destination combinations in network rules** = (number of IP protocols) × (number of source IP addresses) × (number of destination IP addresses) × (number of destination ports ÷ 14, rounded up to the nearest whole number)<br><br>You can track the Firewall Policy network rule count in the [policy analytics](https://learn.microsoft.com/en-us/azure/firewall/policy-analytics) under the **Insights** tab. As a proxy, you can also monitor your Firewall Latency Probe metrics to ensure it stays within 20 ms even during peak hours. |
|Total size of rules within a single Rule Collection Group| 1 MB for Firewall policies created before July 2022<br>2 MB for Firewall policies created after July 2022|
|Number of Rule Collection Groups in a firewall policy|50 for Firewall policies created before July 2022<br>90 for Firewall policies created after July 2022|
|Number of firewalls referenced by a single firewall policy|50|
|Maximum DNAT rules (Maximum external destinations)|250 maximum [number of firewall public IP addresses + unique destinations (destination address, port, and protocol)]<br><br> The DNAT limitation is due to the underlying platform.<br><br>For example, you can configure 500 UDP rules to the same destination IP address and port (one unique destination), while 500 rules to the same IP address but to 500 different ports exceeds the limit (500 unique destinations).<br><br>If you need more than 250, you'll need to add another firewall in a separate virtual network|
|Minimum AzureFirewallSubnet size |/26|
|Port range in network and application rules|1 - 65535|
|Public IP addresses|250 maximum. All public IP addresses can be used in DNAT rules and they all contribute to available SNAT ports.|
|IP addresses in IP Groups|It is recommended to have a maximum of 50 unique IP Groups per classic firewall. <br>Maximum of 600 unique IP Groups per firewall policy.<br>Maximum 5000 individual IP addresses or IP prefixes per each IP Group.|
| Firewalls referencing a single IP Group | 50 (soft limit). Exceeding this limit might affect performance and cause IP Group updates to fail. |
|Route table|By default, AzureFirewallSubnet has a 0.0.0.0/0 route with the NextHopType value set to **Internet**.<br><br>Azure Firewall must have direct Internet connectivity. If your AzureFirewallSubnet learns a default route to your on-premises network via BGP, you must override that with a 0.0.0.0/0 UDR with the **NextHopType** value set as **Internet** to maintain direct Internet connectivity. By default, Azure Firewall doesn't support forced tunneling to an on-premises network.<br><br>However, if your configuration requires forced tunneling to an on-premises network, Microsoft will support it on a case by case basis. Contact Support so that we can review your case. If accepted, we'll allow your subscription and ensure the required firewall Internet connectivity is maintained.|
|FQDNs in network rules|For good performance, do not exceed more than 1000 FQDNs across all network rules per firewall.|
|TLS inspection timeout|120 seconds|

### Azure Front Door (classic) limits

In addition to the following limits, there's a [composite limit on the number of routing rules, front-end domains, protocols, and paths](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-routing-limits).

| Resource | Classic tier limit |
| --- | --- |
| Azure Front Door resources per subscription | 100 |
| Front-end hosts, which include custom domains per resource | 500 |
| Routing rules per resource | 500 |
| Rules per Rule set | 25 |
| Back-end pools per resource <sup>2</sup> | 50 |
| Back ends per back-end pool | 100 |
| Path patterns to match for a routing rule | 25 |
| URLs in a single cache purge call | 100 |
| Maximum bandwidth <sup>1</sup> | 75 Gbps |
| Maximum requests per second per profile <sup>1</sup> | 100,000 |
| HTTP header size limit (per header) | 64 KB |
| Custom web application firewall rules per policy | 100 |
| Web application firewall policy per subscription | 100 |
| Web application firewall match conditions per custom rule | 10 |
| Web application firewall IP address ranges per custom rule | 600 |
| Web application firewall string match values per match condition | 10 |
| Web application firewall string match value length | 256 |
| Web application firewall POST body parameter name length | 256 |
| Web application firewall HTTP header name length | 256 |
| Web application firewall cookie name length | 256 |
| Web application firewall exclusion limit | 100 |
| Web application firewall HTTP request body inspection limit | 128 KB |
| Web application firewall custom response body length | 32 KB |

<sup>1</sup> If the traffic isn't globally distributed and concentrated in one or more regions, or if a higher quota limited is need, create an [Azure support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest).

<sup>2</sup> To request a limit increase, create an [Azure Support request][azure-support]. Free subscriptions including [Azure Free Account](https://azure.microsoft.com/pricing/offers/ms-azr-0044p?cid=msft_learn) and [Azure for Students](https://azure.microsoft.com/offers/ms-azr-0170p/) aren't eligible for limit or quota increases. If you have a free subscription, you can [upgrade](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/upgrade-azure-subscription) to a Pay-As-You-Go subscription.<br />

[azure-support]: https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest

### Azure Front Door Standard and Premium service limits

- Maximum of **500** total Standard and Premium profiles per subscription.
- In addition to the following limits, there's a [composite limit on the number of routes, domains, protocols, and paths](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-routing-limits).

| Resource | Standard tier limit | Premium tier limit |
| --- | --- | --- |
| Maximum profiles per subscription | 500 | 500 |
| Maximum endpoint per profile | 10 | 25 |
| Maximum custom domain per profile	| 100 | 500 |
| Maximum origin groups per profile | 100 | 200 |
| Maximum origins per origin group | 50 | 50 |
| Maximum origins per profile | 100 | 200 |
| Maximum origin timeout | 16 - 240 secs | 16 - 240 secs |
| Maximum routes per profile | 100 | 200 | 
| Maximum rule set per profile | 100 | 200 |
| Maximum rules per route | 100 | 100 |
| Maximum rules per rule set | 100 | 100 |
| Maximum bandwidth <sup>1</sup> | 75 Gbps | 75 Gbps |
| Maximum requests per second per profile <sup>1,</sup> <sup>2</sup> | 100,000 | 100,000 |
| Maximum concurrent WebSocket connections per profile <sup>3</sup> | 3,000 | 3,000 |
| Path patterns to match for a routing rule | 100 | 100 |
| URLs in a single cache purge call | 100 | 100 |
| Maximum security policy per profile | 100 | 200 |
| Maximum associations per security policy | 110 | 225 |
| Maximum secrets per profile | 100 | 500 |
| Maximum key groups per profile | 100 | 200 |
| HTTP header size limit (total header size) | 64 KB | 64 KB |
| HTTP header size limit (total header size - Private Link Service origin) | 32 KB | 32 KB |
| Web Application Firewall (WAF) policy per subscription | 100 | 100 |
| WAF custom rules per policy | 100 | 100 |
| WAF match conditions per custom rule | 10 | 10 |
| WAF custom regex rules per policy | 5 | 5 |
| WAF IP address ranges per match conditions | 600 | 600 |
| WAF string match values per match condition | 10 | 10 |
| WAF string match value length | 256 | 256 |
| WAF POST body parameter name length | 256 | 256 |
| WAF HTTP header name length | 256 | 256 |
| WAF cookie name length | 256 | 256|
| WAF exclusion per policy | 100 | 100 |
| WAF HTTP request body and file upload inspection limit | 128 KB | 128 KB |
| WAF custom response body length | 32 KB | 32 KB |
| Edge action code size <sup>4</sup> | 16 KB | 16 KB |
| Edge action version counts <sup>4</sup> | 3 | 3 |
| Edge action execution time <sup>4</sup> | 10 ms | 10 ms |
| Maximum number of Edge Actions resources per subscription <sup>4</sup> | 100 | 100 |

<sup>1</sup> If the traffic isn't globally distributed and concentrated in one or more regions, or if a higher quota limit is needed, create an [Azure support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest).

<sup>2</sup> There's currently a 5,000 requests per second per PoP limit for each Front Door profile. Beyond this limit, the PoP location drops connections. If requests are concentrated in one or more regions and exceed this limit, you can request a higher PoP limit by submitting an [Azure support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). 

<sup>3</sup> If you need more than 3,000 concurrent WebSocket connections, submit an [Azure support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest).

<sup>4</sup> Currently, **JavaScript** is the only supported language.

#### Timeout values

##### From client to Front Door

- Header timeout - After establishing TCP/TLS connection, Front Door has a 5-second timeout for receiving all headers from the client. The connection is terminated if the client doesn't send headers within 5 seconds. You can't configure this timeout value.
- HTTP keep-alive timeout - Front Door has a 90-second HTTP keep-alive timeout. The connection is terminated if the client doesn't send data for 90 seconds. You can't configure this timeout value.

##### Front Door to application back-end

- After the HTTP request gets forwarded to the back end, Azure Front Door waits for 60 seconds (Standard and Premium) or 30 seconds (classic) for the first packet from the back end. Then it returns a 503 error to the client, or 504 for a cached request. You can configure this value using the *originResponseTimeoutSeconds* field in Azure Front Door Standard and Premium API, or the sendRecvTimeoutSeconds field in the Azure Front Door (classic) API.

- After the back end receives the first packet, if the origin pauses for any reason in the middle of the response body beyond the originResponseTimeoutSeconds or sendRecvTimeoutSeconds, the response is canceled.

- Front Door uses HTTP keep-alive to keep connections open for reuse from previous requests. These connections have an idle timeout of 90 seconds. Azure Front Door disconnects idle connections after reaching the 90-second idle timeout. You can't configure this timeout value.

#### Upload and download data limit

|  | With chunked transfer encoding (CTE) | Without HTTP chunking |
| ---- | ------- | ------- |
| **Download** | There's no limit on the download size. | There's no limit on the download size. |
| **Upload** |    There's no limit as long as each CTE upload is less than 2 GB. | The size can't be larger than 2 GB. |

#### Other limits
- Maximum URL size - 8,192 bytes - Specifies maximum length of the raw URL (scheme + hostname + port + path + query string of the URL)
- Maximum Query String size - 4,096 bytes - Specifies the maximum length of the query string, in bytes.
- Maximum HTTP response header size from health probe URL - 4,096 bytes - Specifies the maximum length of all the response headers of health probes. 
- Maximum rules engine action header value character: 640 characters.
- Maximum rules engine condition header value character: 256 characters.
- Maximum ETag header size: 128 bytes
- Maximum endpoint name for Standard and Premium: 46 characters.

For more information about limits that apply to Rules Engine configurations, see [rules engine terminology](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-rules-engine#terminology).

### Azure Network Watcher limits

| Resource | Limit |
| --- | --- |
| Network Watcher instances per region per subscription | 1 (One instance in a region to enable access to the service in the region) |
| Connection monitors per region per subscription | 100 |
| Maximum test groups per a connection monitor | 20 |
| Maximum sources and destinations per a connection monitor | 100 |
| Maximum test configurations per a connection monitor | 20 |
| Packet capture sessions per region per subscription | 10,000 (Number of sessions only, not saved captures) |
| VPN troubleshoot operations per subscription | 1 (Number of operations at one time) |

### Azure Route Server limits

| Resource | Limit |
|----------|-------|
| Number of BGP peers | 16 |
| Number of routes each BGP peer can advertise to Azure Route Server <sup>1</sup> | 4,000 |
| Number of VMs in the virtual network (including peered virtual networks) that Azure Route Server can support | 50,000 |
| Number of virtual networks that Azure Route Server can support | 500 |
| Number of total on-premises and Azure Virtual Network prefixes that Azure Route Server can support | 10,000 |

<sup>1</sup> If your NVA advertises more routes than the limit, the BGP session gets dropped.

> [!NOTE]
> The total number of routes advertised from virtual network address space and Route Server towards ExpressRoute circuit, when [Branch-to-branch](https://learn.microsoft.com/en-us/azure/route-server/configure-route-server#configure-route-exchange) enabled, must not exceed 1,000. For more information, see [Route advertisement limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-expressroute-limits) of ExpressRoute.

### Azure ExpressRoute limits

| Resource | Limit |
| --- | --- |
| ExpressRoute circuits per subscription | 50 (Submit a support request to increase limit) |
| ExpressRoute circuits per region per subscription, with Azure Resource Manager | 10 |
| Maximum number of circuits in the same peering location linked to the same virtual network | 4 |
| Maximum number of circuits in different peering locations linked to the same virtual network |Standard / ERGw1Az - 4 </br> High Perf / ERGw2Az - 8 </br> Ultra Performance / ErGw3Az - 16 |
| Maximum number of IPs for ExpressRoute provider circuit with Fastpath | 25,000 |
| Maximum number of IPs for ExpressRoute Direct 10 Gbps with Fastpath | 100,000 |
| Maximum number of IPs for ExpressRoute Direct 100 Gbps with Fastpath | 200,000 |
| Maximum number of flows for ExpressRoute Traffic Collector | 300,000 |

#### Route advertisement limits

| Resource | Local / Standard SKU | Premium SKU |
|--|--|--|
| Maximum number of IPv4 on-prem routes advertised over Azure private peering to the ExpressRoute circuit | 4,000 | 10,000 |
| Maximum number of IPv6 on-prem routes advertised over Azure private peering to the ExpressRoute circuit | 100 | 100 |
| Maximum number of IPv4 Virtual Network routes advertised by the Gateway to the ExpressRoute circuit over Azure private peering | 1,000 | 1,000 |
| Maximum number of IPv6 Virtual Network routes advertised by the Gateway to the ExpressRoute circuit over Azure private peering | 100 | 100 |
| Maximum number of IPv4 routes advertised to Microsoft peering from on-premises | 200 | 200 |
| Maximum number of IPv6 routes advertised to Microsoft peering from on-premises | 200 | 200 |

#### Virtual networks links allowed for each ExpressRoute circuit limit

| Circuit size | Local / Standard SKU | Premium SKU |
| --- | --- |--|
| 50 Mbps |  10 | 20 |
| 100 Mbps | 10 | 25 |
| 200 Mbps | 10 | 25 |
| 500 Mbps | 10| 40 |
| 1 Gbps | 10 | 50 |
| 2 Gbps | 10 | 60 |
| 5 Gbps | 10| 75 |
| 10 Gbps | 10| 100 |
| 40 Gbps* | 10 | 100 |
| 100 Gbps* | 10| 100 |

**100-Gbps ExpressRoute Direct Only*

> [!NOTE]
> Global Reach connections count against the limit of virtual network connections per ExpressRoute Circuit. For example, a 10 Gbps Premium Circuit would allow for 5 Global Reach connections and 95 connections to the ExpressRoute Gateways or 95 Global Reach connections and 5 connections to the ExpressRoute Gateways or any other combination up to the limit of 100 connections for the circuit.

#### ExpressRoute gateway performance limits

The following tables provide an overview of the different types of gateways, their respective limitations, and their expected performance metrics.

#### Maximum supported limits

This table applies to both the Azure Resource Manager and classic deployment models.

| Gateway SKU | Megabits per second | Packets per second | Supported number of VMs in the virtual network <sup>1</sup> | Flow count limit | Number of routes learned by gateway |
|--|--|--|--|--|--|
| **Standard/ERGw1Az** | 1,000 | 100,000 | 2,000 | 200,000 | 4,000 |
| **High Performance/ERGw2Az** | 2,000 | 200,000 | 4,500 | 400,000 | 9,500 |
| **Ultra Performance/ErGw3Az** | 10,000 | 1,000,000 | 11,000 | 1,000,000 | 9,500 |
| **ErGwScale (per scale unit 1-10)** | 1,000 per scale unit | 100,000 per scale unit | 2,000 per scale unit | 100,000 per scale unit | 9,500 total per gateway
| **ErGwScale (per scale unit 11-40)** | 1,000 per scale unit | 200,000 per scale unit | 1,000 per scale unit | 100,000 per scale unit | 9,500 total per gateway

<sup>1</sup> "Supported number of VMs in the virtual network" refers to the count of resources that communicate through the gateway. This includes:

- Virtual Machines in the hub virtual network
- Virtual Machines in peered spoke virtual networks (Hub-Spoke topology)
- Private Endpoints
- Network Virtual Appliances (such as Application Gateway, Azure Firewall)
- Backend instances of PaaS services deployed in virtual networks (such as SQL Managed Instance, App Service Environment, Azure API Management in VNet mode)

The values in the table are estimates and vary depending on the CPU utilization of the gateway. If the CPU utilization is high and the number of supported VMs is exceeded, the gateway will start to drop packets.
> [!NOTE]
> ExpressRoute can facilitate up to 11,000 routes that span virtual network address spaces, on-premises networks, and any relevant virtual network peering connections. To ensure stability of your ExpressRoute connection, refrain from advertising more than 11,000 routes to ExpressRoute. The maximum number of routes advertised by gateway is 1,000 routes.

> [!IMPORTANT]
> * Application performance depends on multiple factors, such as end-to-end latency and the number of traffic flows that the application opens. The numbers in the table represent the upper limit that the application can theoretically achieve in an ideal environment. Additionally, we perform routine host and OS maintenance on the ExpressRoute virtual network gateway, to maintain reliability of the service. During a maintenance period, the control plane and data path capacity of the gateway is reduced.
> * During a maintenance period, you might experience intermittent connectivity problems to private endpoint resources.
> * ExpressRoute supports a maximum TCP and UDP packet size of 1,400 bytes. Fragmented packets are not supported by ExpressRoute Gateways. Please adjust your application to prevent IP fragmentation. If IP fragmentation support is required, enable the [ExpressRoute FastPath](https://learn.microsoft.com/en-us/azure/expressroute/about-fastpath) feature to bypass the ExpressRoute gateway.
> * Azure Route Server can support up to 4,000 VMs. This limit includes VMs in virtual networks that are peered. For more information, see [Azure Route Server limitations](https://learn.microsoft.com/en-us/azure/route-server/overview#route-server-limits).
> * The values in the table above represent the limits at each Gateway SKU.

### Azure NAT Gateway limits

The following limits apply to Standard and StandardV2 NAT gateway resources managed through Azure Resource Manager per region per subscription. Learn how to [view your current resource usage against your subscription limits](https://learn.microsoft.com/en-us/azure/networking/check-usage-against-limits).

> [!NOTE]
> Each subscription has a combined quota for both Standard and StandardV2 NAT gateways. For example, if your subscription has a quota of 100 NAT gateways, you can create any combination of Standard and StandardV2 NAT gateways up to that quota.

| Resource            | Standard SKU       | StandardV2 SKU     |
|---------------------|--------------------|--------------------|
| Public IP addresses | 16 IPv4 addresses  | 16 IPv4 addresses, 16 IPv6 addresses |
| Subnets             | 800 per NAT gateway | 800 per NAT gateway |
| Data throughput<sup>1</sup>     | 50 Gbps per NAT gateway | 100 Gbps per NAT gateway, 1 Gbps per connection |
| NAT gateways for Enterprise and CSP agreements<sup>2</sup>       | 1,000 per subscription per region | see previous column for combined quota |
| NAT gateways for Sponsored and pay-as-you-go<sup>2</sup>         | 100 per subscription per region | see previous column for combined quota |
| NAT gateways for Free Trial and all other offer types<sup>2</sup>             | 15 per subscription per region | see previous column for combined quota|
| Packets processed   | 5 million packets per second per NAT gateway, split across directions (2.5 million PPS outbound and 2.5 million PPS return traffic) | 10M packets per second per NAT Gateway, 100,000 PPS per connection  |
| Connections to same destination endpoint | 50,000 connections to the same destination per public IP | 50,000 connections to the same destination per public IP |
| Connections total | 2M connections per NAT gateway | 2M connections per NAT gateway |

<sup>1</sup> For a Standard SKU NAT gateway resource, the total data throughput of 50 Gbps is split between outbound and inbound (return) data. Data throughput is supported up to 25 Gbps for outbound data and up to 25 Gbps for inbound (response) data through NAT gateway.

<sup>2</sup> Default limits for NAT gateways vary by offer category type, such as Free Trial, pay-as-you-go, and CSP. For example, the default for Enterprise Agreement subscriptions is 1000.

### Azure Private Link limits

The following limits apply to Azure private link:

|Resource |Limit |
|---------|---------|
|Number of private endpoints per virtual network     |  1000       |
|Number of private endpoints across peered virtual networks     |  4000       |
|Number of private endpoints per subscription       |   64000       |
|Number of private link services per subscription         |   800      |
|Number of private link services per Standard Load Balancer         |   8      |
|Number of IP Configurations on a private link service     |  8 (This number is for the NAT IP addresses used per PLS)       |
|Number of private endpoints on the same private link service   |  1000       |
|Number of subscriptions allowed in visibility setting on private link service   |  100       |
|Number of subscriptions allowed in auto-approval setting on private link service   |  100       |
|Number of private endpoints per key vault | 64 |
|Number of private DNS zone groups that can be linked to a private endpoint | 1 |
|Number of DNS zones in each group | 5 |
|Number of private IP addresses on private endpoint network interface     |  500   |

### Azure Traffic Manager limits

#### Resource limits

| Resource | Limit |
| --- | --- |
| Profiles per subscription |200 <sup>1</sup> |
| Endpoints per profile |200 |

<sup>1</sup>If you need to increase these limits, contact Azure Support.

#### Default throttling limits 

##### Profiles

| Operation | Limit (per minute) |
| --- | --- |
| Create/update | 600 |
| Get | 450 |
| Delete | 150 |
| List in resource group or subscription | 450 |
| Check DNS name availability | 300 |

##### Endpoints

| Operation | Limit (per minute) |
| --- | --- |
| Create/update/delete | 300 |
| Get | 1500 |

##### Metrics & heatmap

| Operation | Limit (per minute) |
| --- | --- |
| Get/create/delete user metrics key | 150 |
| Get heat map | 150 |

##### Geo hierarchy

| Operation | Limit (per minute) |
| --- | --- |
| Get | 150 |

### Azure VPN Gateway limits

Unless stated otherwise, the following limits apply to Azure VPN Gateway resources and virtual network gateways.

| Resource                                | Limit        |
|-----------------------------------------|------------------------------|
| VNet Address Prefixes                   | 600 per VPN gateway          |
| Aggregate BGP routes                    | 4,000 per VPN gateway        |
| Local Network Gateway address prefixes  | 1000 per local network gateway               |
| S2S connections                         | Limit depends on the gateway SKU. See the [Limits by gateway SKU](#limits-by-gateway-sku) table.|
| P2S connections                         | Limit depends on the gateway SKU. See the [Limits by gateway SKU](#limits-by-gateway-sku) table.|
| P2S route limit - IKEv2                 | 256 for non-Windows **/** 25 for Windows           |
| P2S route limit - OpenVPN               | 1000                         |
| Max. flows                              | 500K inbound and 500K outbound for VpnGw1-5/AZ|
| Traffic Selector Policies               | 100  |
| Custom APIPA BGP addresses              | 32   |
| Supported number of VMs in the virtual network | Limit depends on the gateway SKU. See the [Limits by gateway SKU](#limits-by-gateway-sku) table.|

#### Limits by gateway SKU

The following SKUs can be used to deploy new VPN gateways. They have zone-redundant options and are recommended for all new deployments.

| **VPN<br>Gateway<br>Generation** | **SKU** | **S2S/VNet-to-VNet<br>Tunnels** | **P2S<br> SSTP Connections** | **P2S<br> IKEv2/OpenVPN Connections** | **Aggregate<br>Throughput Benchmark** | **BGP** | **Zone-redundant** | **Supported Number of VMs in the Virtual Network** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|**Generation1**|**Basic**   | Max. 10    | Max. 128  | Not Supported  | 100 Mbps  | Not Supported| No | 200 |
|**Generation1**|**VpnGw1AZ**| Max. 30    | Max. 128  | Max. 250       | 650 Mbps  | Supported | Yes | 1000 |
|**Generation1**|**VpnGw2AZ**| Max. 30    | Max. 128  | Max. 500       | 1 Gbps    | Supported | Yes | 2000 |
|**Generation1**|**VpnGw3AZ**| Max. 30    | Max. 128  | Max. 1000      | 1.25 Gbps | Supported | Yes | 5000 |
| | | | | | | | | |
|**Generation2**|**VpnGw2AZ**| Max. 30    | Max. 128  | Max. 500       | 1.25 Gbps | Supported | Yes | 2000 |
|**Generation2**|**VpnGw3AZ**| Max. 30    | Max. 128  | Max. 1000      | 2.5 Gbps  | Supported | Yes | 3300 |
|**Generation2**|**VpnGw4AZ**| Max. 100*  | Max. 128  | Max. 5000      | 5 Gbps    | Supported | Yes | 4400 |
|**Generation2**|**VpnGw5AZ**| Max. 100*  | Max. 128  | Max. 10000     | 10 Gbps   | Supported | Yes | 9000 |

VpnGw1~5 are slated for migration and should not be used to create new VPN gateways. For more information, see [VPN Gateway SKU consolidation and migration](https://learn.microsoft.com/en-us/azure/vpn-gateway/gateway-sku-consolidation).

| **VPN<br>Gateway<br>Generation** | **SKU** | **S2S/VNet-to-VNet<br>Tunnels** | **P2S<br> SSTP Connections** | **P2S<br> IKEv2/OpenVPN Connections** | **Aggregate<br>Throughput Benchmark** | **BGP** | **Zone-redundant** | **Supported Number of VMs in the Virtual Network** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|**Generation1**|**VpnGw1**  | Max. 30    | Max. 128  | Max. 250    | 650 Mbps  | Supported | No | 450 |
|**Generation1**|**VpnGw2**  | Max. 30    | Max. 128  | Max. 500    | 1 Gbps    | Supported | No | 1300 |
|**Generation1**|**VpnGw3**  | Max. 30    | Max. 128  | Max. 1000   | 1.25 Gbps | Supported | No | 4000 |
| | | | | | | | | |
|**Generation2**|**VpnGw2**  | Max. 30    | Max. 128  | Max. 500    | 1.25 Gbps | Supported | No | 685 |
|**Generation2**|**VpnGw3**  | Max. 30    | Max. 128  | Max. 1000   | 2.5 Gbps  | Supported | No | 2240 |
|**Generation2**|**VpnGw4**  | Max. 100*  | Max. 128  | Max. 5000   | 5 Gbps    | Supported | No | 5300 |
|**Generation2**|**VpnGw5**  | Max. 100*  | Max. 128  | Max. 10000  | 10 Gbps   | Supported | No | 6700 |

> [!NOTE]
> "Supported Number of VMs in the Virtual Network" refers to the count of resources that communicate through the gateway. This includes:
> - Virtual Machines in the hub and peered spoke virtual networks
> - Private Endpoints
> - Network Virtual Appliances (such as Application Gateway, Azure Firewall)
> - Backend instances of PaaS services deployed in virtual networks (such as SQL Managed Instance, App Service Environment)

For more information about gateway SKUs and limits, see [About gateway SKUs](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus#benchmark).

#### Gateway performance limits

The table in this section lists the results of performance tests for VpnGw SKUs. A VPN tunnel connects to a VPN gateway instance. Each instance throughput is mentioned in the throughput table in the previous section and is available aggregated across all tunnels connecting to that instance. The table shows the observed bandwidth and packets per second throughput per tunnel for the different gateway SKUs. All testing was performed between gateways (endpoints) within Azure across different regions with 100 connections and under standard load conditions. We used publicly available iPerf and CTSTraffic tools to measure performances for site-to-site connections

* The best performance was obtained when we used the GCMAES256 algorithm for both IPsec Encryption and Integrity.
* Average performance was obtained when using AES256 for IPsec Encryption and SHA256 for Integrity.
* The lowest performance was obtained when we used DES3 for IPsec Encryption and SHA256 for Integrity.

|**Generation**|**SKU**   | **Algorithms<br>used** | **Throughput<br>observed per tunnel** | **Packets per second per tunnel<br>observed** |
|---           |---       | ---                 | ---            | ---                    |
|**Generation1**|**VpnGw1**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 650 Mbps<br>500 Mbps<br>130 Mbps   | 62,000<br>47,000<br>12,000|
|**Generation1**|**VpnGw2**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.2 Gbps<br>650 Mbps<br>140 Mbps | 100,000<br>61,000<br>13,000|
|**Generation1**|**VpnGw3**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.25 Gbps<br>700 Mbps<br>140 Mbps | 120,000<br>66,000<br>13,000|
|**Generation1**|**VpnGw1AZ**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 650 Mbps<br>500 Mbps<br>130 Mbps   | 62,000<br>47,000<br>12,000|
|**Generation1**|**VpnGw2AZ**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.2 Gbps<br>650 Mbps<br>140 Mbps | 110,000<br>61,000<br>13,000|
|**Generation1**|**VpnGw3AZ**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.25 Gbps<br>700 Mbps<br>140 Mbps | 120,000<br>66,000<br>13,000|
| | |
|**Generation2**|**VpnGw2**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.25 Gbps<br>550 Mbps<br>130 Mbps | 120,000<br>52,000<br>12,000|
|**Generation2**|**VpnGw3**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.5 Gbps<br>700 Mbps<br>140 Mbps | 140,000<br>66,000<br>13,000|
|**Generation2**|**VpnGw4**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 2.3 Gbps<br>700 Mbps<br>140 Mbps | 220,000<br>66,000<br>13,000|
|**Generation2**|**VpnGw5**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 2.3 Gbps<br>700 Mbps<br>140 Mbps | 220,000<br>66,000<br>13,000|
|**Generation2**|**VpnGw2AZ**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.25 Gbps<br>550 Mbps<br>130 Mbps | 120,000<br>52,000<br>12,000|
|**Generation2**|**VpnGw3AZ**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 1.5 Gbps<br>700 Mbps<br>140 Mbps | 140,000<br>66,000<br>13,000|
|**Generation2**|**VpnGw4AZ**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 2.3 Gbps<br>700 Mbps<br>140 Mbps | 220,000<br>66,000<br>13,000|
|**Generation2**|**VpnGw5AZ**| GCMAES256<br>AES256 & SHA256<br>DES3 & SHA256| 2.3 Gbps<br>700 Mbps<br>140 Mbps | 220,000<br>66,000<br>13,000|

### Azure Virtual WAN limits

| Resource |  Limit |
| --- | --- |
| VPN (branch) connections per hub | 1,000 |
| Aggregate throughput per Virtual WAN Site-to-site VPN gateway | 20 Gbps |
| Throughput per Virtual WAN VPN connection (2 tunnels) | 2 Gbps with 1 Gbps/IPsec tunnel |
| Point-to-site users per hub| 100,000 |
| Aggregate throughput per Virtual WAN User VPN (Point-to-site) gateway | 200 Gbps |
| Aggregate throughput per Virtual WAN ExpressRoute gateway | 20 Gbps |
| ExpressRoute circuit connections per hub | 8 - [Read more here](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-expressroute-about#expressroute-limits-in-virtual-wan) |
| VNet connections per hub without Routing Intent enabled | 500 minus total number of hubs in Virtual WAN |
| Address spaces across all VNets directly connected to single hub with Routing Intent with private routing policies enabled| 600 per Virtual WAN hub - [Read more here](https://learn.microsoft.com/en-us/azure/virtual-wan/how-to-routing-policies#address-limits)|
| Aggregate throughput per Virtual WAN hub router | 50 Gbps for VNet to VNet transit |
| VM workload across all VNets connected to a single Virtual WAN hub | 2000 (If you want to raise the limit or quota above the default limit, see [hub settings](https://learn.microsoft.com/en-us/azure/virtual-wan/hub-settings)). |
| Total number of routes the hub can accept from its connected resources (virtual networks, branches, other virtual hubs, etc.) | 10,000 |

## Azure Notification Hubs limits

| Tier              | Free         | Basic    | Standard   |
| ------------------ | ------------ | ---------- | ---------- |
| Included pushes    | 1 million    | 10 million | 10 million |
| Active devices     | 500          | 200,000    | 10 million |
| Tag quota per installation or registration | 60  | 60 |  60 |

For more information on limits and pricing, see [Notification Hubs pricing](https://azure.microsoft.com/pricing/details/notification-hubs/).

## Microsoft Dev Box limits

| Subscription type  | VM Cores | Network Connections | Dev centers | Dev box definitions | Dev box projects |
| ------------------ | -------- | ------------------- | ----------- | ------------------- | ---------------- |
| Pay as you go      |   20     |         5           |     2       |     200             |     500          |
| Azure Pass         |   20     |         5           |     2       |     200             |     500          |
| CSP                |   20     |         5           |     2       |     200             |     500          |
| Free trial         |    0     |         0           |     0       |       0             |       0          |
| Azure for Students |    0     |         0           |     0       |       0             |       0          |
| Enterprise         |   80     |        10           |     5       |     200             |     500          |
| MSDN               |  n/a     |         5           |     2       |     200             |     500          |

<a name='azure-active-directory-limits'></a>

## Microsoft Entra service limits

See [Microsoft Entra service limits](https://learn.microsoft.com/en-us/entra/identity/users/directory-service-limits-restrictions) for Microsoft Entra service limits.

## Microsoft Purview limits

See [Classic Microsoft Purview data governance limits](https://learn.microsoft.com/en-us/azure/purview/how-to-manage-quotas#classic-microsoft-purview-data-governance-limits) for the most current Microsoft Purview quotas.

## Microsoft Sentinel limits

See [Service limits for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-service-limits) for Microsoft Sentinel limits.

## Azure Service Bus limits

The following table lists quota information specific to Azure Service Bus messaging. For information about pricing and other quotas for Service Bus, see [Service Bus pricing](https://azure.microsoft.com/pricing/details/service-bus/).

### Common limits for all tiers

### Basic vs. standard vs. premium tiers

## Azure Site Recovery limits

The following limits apply to Azure Site Recovery.

| Limit identifier | Limit |
| --- | --- |
| Number of vaults per subscription |500 |    
| Number of protected disks per subscription (Both Data and OS) |3000 |
| Number of appliances per Recovery Services vault |250 |
| Number of protection groups per Recovery Services vault |No limit |
| Number of recovery plans per Recovery Services vault |No limit |
| Number of servers per protection group |No limit |
| Number of servers per recovery plan |100 |

## Azure SQL Database limits

For Azure SQL Database limits see:

- [Overview of Azure SQL Managed Instance resource limits](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/resource-limits)
- [Resource limits for single databases using the vCore purchasing model](https://learn.microsoft.com/en-us/azure/azure-sql/database/resource-limits-vcore-single-databases)
- [Resource limits for elastic pools using the vCore purchasing model](https://learn.microsoft.com/en-us/azure/azure-sql/database/resource-limits-vcore-elastic-pools)

The maximum number of private endpoints per Azure SQL Database logical server is 250.

## Azure Synapse Analytics limits

Azure Synapse Analytics has the following default limits to ensure customer's subscriptions are protected from each other's workloads. To raise the limits to the maximum for your subscription, contact support.

### Azure Synapse limits for workspaces

For Pay-As-You-Go, Free Trial, Azure Pass, and Azure for Students subscription offer types:

| Resource | Default limit | Maximum limit | 
| -------- | ------------- | ------------- |
| Synapse workspaces in an Azure subscription | 2 | 2 |

For other subscription offer types:

| Resource | Default limit | Maximum limit | 
| -------- | ------------- | ------------- |
| Synapse workspaces in an Azure subscription per region | 20 | 100 |

### Azure Synapse limits for Apache Spark

For Pay-As-You-Go, Free Trial, Azure Pass, and Azure for Students subscription offer types:

| Resource | Memory Optimized cores | GPU cores | 
| -------- | ------------- | ------------- |
| Spark cores in a Synapse workspace | 12 | 48 |

For other subscription offer types:

| Resource | Memory Optimized cores | GPU cores | 
| -------- | ------------- | ------------- |
| Spark cores in a Synapse workspace | 50 | 50 |

For additional limits for Spark pools, see [Concurrency and API rate limits for Apache Spark pools in Azure Synapse Analytics](https://learn.microsoft.com/en-us/rest/api/synapse/concurrency-limits-spark-pools).

### Azure Synapse limits for pipelines

| Resource | Default limit | Maximum limit |
| -------- | ------------- | ------------- |
| Synapse pipelines in a Synapse workspace | 800 | 800 |
| Total number of entities, such as pipelines, data sets, triggers, linked services, Private Endpoints, and integration runtimes, within a workspace | 5,000 | 5,000 |
| Total CPU cores for Azure-SSIS Integration Runtimes under one workspace | 256 | [Find out how to request a quota increase from support](https://azure.microsoft.com/blog/azure-limits-quotas-increase-requests/). |
| Concurrent pipeline runs per workspace that's shared among all pipelines in the workspace | 10,000  | 10,000 |
| Concurrent External activity runs per workspace per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-ir-location)<br>External activities are managed on integration runtime but execute on linked services, including Databricks, stored procedure, HDInsight, Web, and others. This limit doesn't apply to Self-hosted IR. | 3,000 | 3,000 |
| Concurrent Pipeline activity runs per workspace per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-ir-location) <br>Pipeline activities execute on integration runtime, including Lookup, GetMetadata, and Delete. This limit doesn't apply to Self-hosted IR. | 1,000 | 1,000                                                        |
| Concurrent authoring operations per workspace per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-ir-location)<br>Including test connection, browse folder list and table list, preview data. This limit doesn't apply to Self-hosted IR. | 200 | 200                                                          |
| Concurrent Data Integration Units<sup>1</sup> consumption per workspace per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#integration-runtime-location)| Region group 1<sup>2</sup>: 6,000<br>Region group 2<sup>2</sup>: 3,000<br>Region group 3<sup>2</sup>: 1,500<br>Managed virtual network<sup>2</sup>: 2,0 | Region group 1<sup>2</sup>: 6,000<br/>Region group 2<sup>2</sup>: 3,000<br/>Region group 3<sup>2</sup>: 1,500 |
| Concurrent Data Integration Units<sup>1</sup> consumption per subscription per [Azure Integration Runtime region](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#integration-runtime-location) in managed virtual network| 2,0 | 2,0 |
| Maximum activities per pipeline, which includes inner activities for containers | 120 | 120 |
| Maximum number of linked integration runtimes that can be created against a single self-hosted integration runtime | 100 | 100 |
| Maximum parameters per pipeline | 50 | 50 |
| ForEach items | 100,000 | 100,000 |
| ForEach parallelism | 20 | 50 |
| Maximum queued runs per pipeline | 100 | 100 |
| Characters per expression | 8,192 | 8,192 |
| Minimum tumbling window trigger interval | 5 min | 15 min |
| Maximum timeout for pipeline activity runs | 7 days | 7 days |
| Bytes per object for pipeline objects<sup>3</sup> | 200 KB | 200 KB |
| Bytes per object for dataset and linked service objects<sup>3</sup> | 100 KB | 2,000 KB |
| Bytes per payload for each activity run<sup>4</sup> | 896 KB | 896 KB |
| Data Integration Units<sup>1</sup> per copy activity run | 256 | 256 |
| Write API calls | 1,200/h | 1,200/h<br/><br/> This limit is imposed by Azure Resource Manager, not Azure Synapse Analytics. |
| Read API calls | 12,500/h | 12,500/h<br/><br/> This limit is imposed by Azure Resource Manager, not Azure Synapse Analytics. |
| Monitoring queries per minute | 1,000 | 1,000 |
| Maximum time of data flow debug session | 8 hrs | 8 hrs |
| Concurrent number of data flows per integration runtime | 50 | 50 |
| Concurrent number of data flows per integration runtime in managed vNet| 20 | 20 |
| Concurrent number of data flow debug sessions per user per workspace | 3 | 3 |
| Data Flow Azure IR TTL limit | 4 hrs |  4 hrs |
| Meta Data Entity Size limit in a workspace | 2 GB | 2 GB |

<sup>1</sup> The data integration unit (DIU) is used in a cloud-to-cloud copy operation, learn more from [Data integration units (version 2)](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-performance#data-integration-units). For information on billing, see [Azure Synapse Analytics Pricing](https://azure.microsoft.com/pricing/details/synapse-analytics/).

<sup>2</sup> [Azure Integration Runtime](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#azure-integration-runtime) is [globally available](https://azure.microsoft.com/global-infrastructure/services/) to ensure data compliance, efficiency, and reduced network egress costs. 

| Region group | Regions |
| -------- | ------ |
| Region group 1 | Central US, East US, East US 2, North Europe, West Europe, West US, West US 2 |
| Region group 2 | Australia East, Australia Southeast, Brazil South, Central India, Japan East, North Central US, South Central US, Southeast Asia, West Central US |
| Region group 3 | Other regions |

If managed virtual network is enabled, the data integration unit (DIU) in all region groups are 2,400.

<sup>3</sup> Pipeline, data set, and linked service objects represent a logical grouping of your workload. Limits for these objects don't relate to the amount of data you can move and process with Azure Synapse Analytics. Synapse Analytics is designed to scale to handle petabytes of data.

<sup>4</sup> The payload for each activity run includes the activity configuration, the associated dataset(s), and linked service(s) configurations if any, and a small portion of system properties generated per activity type. Limit for this payload size doesn't relate to the amount of data you can move and process with Azure Synapse Analytics. Learn about the [symptoms and recommendation](https://learn.microsoft.com/en-us/azure/data-factory/data-factory-troubleshoot-guide#payload-is-too-large) if you hit this limit.

### Azure Synapse limits for dedicated SQL pools
For details of capacity limits for dedicated SQL pools in Azure Synapse Analytics, see [dedicated SQL pool resource limits](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-service-capacity-limits).

### Azure Resource Manager limits for web service calls
Azure Resource Manager has limits for API calls. You can make API calls at a rate within the [Azure Resource Manager API limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-resource-group-limits).

### Azure virtual machine disk limits

See [sizes for virtual machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json) for more information.

**For VM Applications**

When working with VM applications in Azure, you may encounter an error message that says "Operation could not be completed as it results in exceeding approved UnmanagedStorageAccountCount quota." This error occurs when you have reached the limit for the number of unmanaged storage accounts that you can use.

When you publish a VM application, Azure needs to replicate it across multiple regions. To do this, Azure creates an unmanaged storage account for each region. The number of unmanaged storage accounts that an application uses is determined by the number of replicas across all applications.

As a general rule, each storage account can accommodate up to 200 simultaneous connections. Below are options for resolving the "UnmanagedStorageAccountCount" error:

- Use page blobs for your source application blobs. Unmanaged accounts are only used for block blob replication. Page blobs have no such limits.
- Reduce the number of replicas for your VM Application versions or delete applications you no longer need.
- File a support request to obtain a quota increase.

See [VM Applications overview](https://learn.microsoft.com/en-us/azure/virtual-machines/vm-applications) for more information.

#### Azure disk encryption sets

Each region and subscription supports up to 5,000 disk encryption sets. [Contact Azure support](https://learn.microsoft.com/en-us/azure/communications-gateway/request-changes) to increase the quota. 

See the following documentation to learn more about encryption restrictions:

- [Linux](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption#restrictions)
- [Windows](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption#restrictions) virtual machines

### Azure managed disks

### Unmanaged virtual machine disks

## Azure StorSimple System limits

| Limit identifier | Limit | Comments |
| --- | --- | --- |
| Maximum number of storage account credentials |64 | |
| Maximum number of volume containers |64 | |
| Maximum number of volumes |255 | |
| Maximum number of schedules per bandwidth template |168 |A schedule for every hour, every day of the week. |
| Maximum size of a tiered volume on physical devices |64 TB for StorSimple 8100 and StorSimple 8600 |StorSimple 8100 and StorSimple 8600 are physical devices. |
| Maximum size of a tiered volume on virtual devices in Azure |30 TB for StorSimple 8010 <br></br> 64 TB for StorSimple 8020 |StorSimple 8010 and StorSimple 8020 are virtual devices in Azure that use Standard storage and Premium storage, respectively. |
| Maximum size of a locally pinned volume on physical devices |9 TB for StorSimple 8100 <br></br> 24 TB for StorSimple 8600 |StorSimple 8100 and StorSimple 8600 are physical devices. |
| Maximum number of iSCSI connections |512 | |
| Maximum number of iSCSI connections from initiators |512 | |
| Maximum number of access control records per device |64 | |
| Maximum number of volumes per backup policy |24 | |
| Maximum number of backups retained per backup policy |64 | |
| Maximum number of schedules per backup policy |10 | |
| Maximum number of snapshots of any type that can be retained per volume |256 |This amount includes local snapshots and cloud snapshots. |
| Maximum number of snapshots that can be present in any device |10,000 | |
| Maximum number of volumes that can be processed in parallel for backup, restore, or clone |16 |<ul><li>If there are more than 16 volumes, they're processed sequentially as processing slots become available.</li><li>New backups of a cloned or a restored tiered volume can't occur until the operation is finished. For a local volume, backups are allowed after the volume is online.</li></ul> |
| Restore and clone recover time for tiered volumes |<2 minutes |<ul><li>The volume is made available within 2 minutes of a restore or clone operation, regardless of the volume size.</li><li>The volume performance might initially be slower than normal as most of the data and metadata still resides in the cloud. Performance might increase as data flows from the cloud to the StorSimple device.</li><li>The total time to download metadata depends on the allocated volume size. Metadata is automatically brought into the device in the background at the rate of 5 minutes per TB of allocated volume data. This rate might be affected by Internet bandwidth to the cloud.</li><li>The restore or clone operation is complete when all the metadata is on the device.</li><li>Backup operations can't be performed until the restore or clone operation is fully complete. |
| Restore recover time for locally pinned volumes |<2 minutes |<ul><li>The volume is made available within 2 minutes of the restore operation, regardless of the volume size.</li><li>The volume performance might initially be slower than normal as most of the data and metadata still resides in the cloud. Performance might increase as data flows from the cloud to the StorSimple device.</li><li>The total time to download metadata depends on the allocated volume size. Metadata is automatically brought into the device in the background at the rate of 5 minutes per TB of allocated volume data. This rate might be affected by Internet bandwidth to the cloud.</li><li>Unlike tiered volumes, if there are locally pinned volumes, the volume data is also downloaded locally on the device. The restore operation is complete when all the volume data has been brought to the device.</li><li>The restore operations might be long and the total time to complete the restore will depend on the size of the provisioned local volume, your Internet bandwidth, and the existing data on the device. Backup operations on the locally pinned volume are allowed while the restore operation is in progress. |
| Thin-restore availability |Last failover | |
| Maximum client read/write throughput, when served from the SSD tier* |920/720 MB/sec with a single 10-gigabit Ethernet network interface |Up to two times with MPIO and two network interfaces. |
| Maximum client read/write throughput, when served from the HDD tier* |120/250 MB/sec | |
| Maximum client read/write throughput, when served from the cloud tier* |11/41 MB/sec |Read throughput depends on clients generating and maintaining sufficient I/O queue depth. |

&#42;Maximum throughput per I/O type was measured with 100 percent read and 100 percent write scenarios. Actual throughput might be lower and depends on I/O mix and network conditions.

## Azure Stream Analytics limits

---
| Limit identifier | Limit | Comments |
| --- | --- | --- |
| Maximum number of streaming units per subscription per region |83 |To request an increase in streaming units for your subscription beyond 83, contact [Microsoft Support](https://support.microsoft.com/en-us). |
| Maximum number of inputs per job |60 |There's a hard limit of 60 inputs per Azure Stream Analytics job. |
| Maximum number of outputs per job |60 |There's a hard limit of 60 outputs per Stream Analytics job. |
| Maximum number of functions per job |60 |There's a hard limit of 60 functions per Stream Analytics job. |
| Maximum number of streaming units per job |66 |There's a hard limit of 66 streaming units per Stream Analytics job. |
| Maximum number of jobs per region |1,500 |Each subscription can have up to 1,500 jobs per geographical region. |
| Reference data blob MB | 5 GB | Up to 5 GB when using 1 or more SUs. |
| Maximum number of characters in a query | 512000 | There's a hard limit of 512k characters in an Azure Stream Analytics job query.|

## Azure Virtual Machines limits

### Azure Virtual Machines limits

| Resource | Limit |
| --- | --- |
| Virtual machines per cloud service <sup>1</sup> |50 |
| Input endpoints per cloud service <sup>2</sup> |150 |

<sup>1</sup> Virtual machines created by using the classic deployment model instead of Azure Resource Manager are automatically stored in a cloud service. You can add more virtual machines to that cloud service for load balancing and availability. 

<sup>2</sup> Input endpoints allow communications to a virtual machine from outside the virtual machine's cloud service. Virtual machines in the same cloud service or virtual network can automatically communicate with each other.

### Azure Virtual Machines limits - Azure Resource Manager

The following limits apply when you use Azure Resource Manager and Azure resource groups.

| Resource | Limit |
| --- | --- |
| VMs per [subscription](https://azure.microsoft.com/pricing/) |25,000<sup>1</sup> per region. |
| VM total cores per [subscription](https://azure.microsoft.com/pricing/) |20<sup>1</sup> per region. Contact support to increase limit. |
| Azure Spot VM total cores per [subscription](https://azure.microsoft.com/pricing/) |20<sup>1</sup> per region. Contact support to increase limit. |
| VM per series, such as Dv2 and F, cores per [subscription](https://azure.microsoft.com/pricing/) |20<sup>1</sup> per region. Contact support to increase limit. |
| [Availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview) per subscription |2,500 per region. |
| Virtual machines per availability set | 200 |
| [Proximity placement groups](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/proximity-placement-groups-portal) per [resource group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups) | 800 |
| Certificates per availability set | 199<sup>2</sup> |
| Certificates per subscription |Unlimited<sup>3</sup> |

<sup>1</sup> Default limits vary by offer category type, such as Free Trial and Pay-As-You-Go, and by series, such as Dv2, F, and G. For example, the default for Enterprise Agreement subscriptions is 350. For security, subscriptions default to 20 cores to prevent large core deployments. If you need more cores, submit a support ticket.

<sup>2</sup> Properties such as SSH public keys are also pushed as certificates and count towards this limit. To bypass this limit, use the [Azure Key Vault extension for Windows](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/key-vault-windows) or the [Azure Key Vault extension for Linux](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/key-vault-linux) to install certificates.

<sup>3</sup> With Azure Resource Manager, certificates are stored in the Azure Key Vault. The number of certificates is unlimited for a subscription. There's a 1-MB limit of certificates per deployment, which consists of either a single VM or an availability set.

> [!NOTE]
> Virtual machine cores have a regional total limit. They also have a limit for regional per-size series, such as Dv2 and F. These limits are separately enforced. For example, consider a subscription with a US East total VM core limit of 30, an A series core limit of 30, and a D series core limit of 30. This subscription can deploy 30 A1 VMs, or 30 D1 VMs, or a combination of the two not to exceed a total of 30 cores. An example of a combination is 10 A1 VMs and 20 D1 VMs.
> 
>

### Azure Compute Gallery limits

There are limits per subscription for deploying resources when you use Compute Galleries:

- 100 compute galleries per subscription and per region
- 1,000 image definitions per subscription and per region
- 10,000 image versions per subscription and per region

### Managed Run Command limit

The maximum allowed Managed Run Commands is currently limited to 25.

## Azure Virtual Machine Scale Sets limits

| Resource | Limit |
| --- | --- |
| Maximum number of VMs in a scale set |1,000 |
| Maximum number of VMs based on a custom VM image in a scale set|600 |
| Maximum number of scale sets per subscription per region |2,500 |
| Maximum number of nodes supported in VMSS for IB cluster |100 |

## Azure Virtual Network Manager limits

| Category | Limitation |
| --- | --- |
| **General Limitations** | |
| Cross-tenant Support | Only with static membership network groups |
| Azure Subscriptions | Policy application limited to fewer than 15,000 subscriptions |
| Policy Enforcement Mode | No addition to network group if set to Disabled |
| Policy Evaluation Cycle | Standard evaluation cycle not supported |
| Subscription Movement | Moving subscription to another tenant not supported |
| **Limits for Connectivity Configurations** | |
| Virtual Networks in a Connected Group | A connected group can include up to 250 virtual networks by default. In supported regions, you can increase the limit to 3,000 by registering the high-scale connected group feature. You can request an increase to 5,000 by submitting the [scaling request form](https://forms.cloud.microsoft.com/r/BBNK1V8qTD). |
| Private Endpoints | 2,000 private endpoints per connected group |
| Hub-and-Spoke Configuration | Up to 1,000 virtual networks peered to the hub |
| Direct Connectivity | Up to 250 virtual networks by default. In supported regions, you can increase the limit to 3,000 by registering the high-scale connected group feature. You can request an increase to 5,000 by submitting the [scaling request form](https://forms.cloud.microsoft.com/r/BBNK1V8qTD). |
| Group Membership | A virtual network can be part of up to two connected groups. You can request an increase to 1,000 by submitting the [connected group limit request form](https://forms.cloud.microsoft.com/r/1Je8uWNkXJ). |
| Overlapping IP Spaces | Communication to an overlapping IP address is dropped |
| **Limits for Security Admin Rules** | |
| IP Prefixes | Max 20,000 IP prefixes combined per one Azure Virtual Network Manager resource |
| Admin Rules | Max 100 admin rules combined per one Azure Virtual Network Manager resource |
| **Limits for User Defined Routes** | |
| User Defined Routes per Route Table | Max 1,000 |

## Dev tunnels limits

The following limits apply to [dev tunnels](https://aka.ms/devtunnels/docs). The limits reset monthly. 

| Resource | Limit |
| --- | --- |
| Bandwidth | 5 GB per user |
| Tunnels | 10 per user |
| Active connections | 1000 per port |
| Ports | 10 per tunnel |
| HTTP request rate | 1500/min per port |
| Data transfer rate | Up to 20 MB/s per tunnel |
| Max web-forwarding HTTP request body size | 16 MB |

For questions on these limits, open an issue in our [GitHub repo](https://github.com/Microsoft/dev-tunnels/issues).

## Network security perimeter limits

### Scale limitations

Network security perimeter functionality can be used to support deployments of PaaS resources with common public network controls with following scale limitations:

| **Limitation** | **Description** |
|-----------------|-----------------|
| **Number of network security perimeters**  | Supported up to 100 as recommended limit per subscription. |
| **Profiles per network security perimeters** | Supported up to 200 as recommended limit. |
| **Number of rule elements per profile** | Supported up to 200 for inbound and outbound each as hard limit. |
| **Number of PaaS resources across subscriptions associated with the same network security perimeter** | Supported up to 1000 as recommended limit. |

### Other limitations

Network security perimeter has other limitations as follows:

| **Limitation/Issue** | **Description** |
|-----------------|-------------|
| **Missing field in network security perimeter access logs** | Network security perimeter access logs can be aggregated. If the fields 'count' and 'timeGeneratedEndTime' are missing, consider the aggregation count as 1. |
| **Association creations through SDK fails with permission issue** | 'Status: 403 (Forbidden); ErrorCode: AuthorizationFailed' might be received while performing action 'Microsoft.Network/locations/networkSecurityPerimeterOperationStatuses/read' over scope '/subscriptions/xyz/providers/Microsoft.Network/locations/xyz/networkSecurityPerimeterOperationStatuses/xyz'.  <br> <br> Until the fix, use permission 'Microsoft.Network/locations/*/read' or use WaitUntil.Started in CreateOrUpdateAsync SDK API for association creations. |
| **Resource names cannot be longer than 44 characters to support network security perimeter** | The network security perimeter resource association created from the Azure portal has the format `{resourceName}-{perimeter-guid}`. To align with the requirement name field can't have more than 80 characters, resources names would have to be limited to 44 characters. |
| **Service endpoint traffic is not supported.** | It's recommended to use private endpoints for IaaS to PaaS communication. Currently, service endpoint traffic can be denied even when an inbound rule allows 0.0.0.0/0. |

> [!NOTE]
> Refer to individual PaaS documentation for respective limitations for each service.

## Next steps

Continue to the following resources to learn more:

- [Understand Azure Limits and Increases](https://azure.microsoft.com/blog/azure-limits-quotas-increase-requests/)
- [Sizes for virtual machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)
- [Sizes for Cloud Services (classic)](https://learn.microsoft.com/en-us/azure/cloud-services/cloud-services-sizes-specs)
- [Naming rules and restrictions for Azure resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules)
