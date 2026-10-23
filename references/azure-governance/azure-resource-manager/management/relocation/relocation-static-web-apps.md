# Relocate Azure Static Web Apps to another region

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-static-web-apps  
> Microsoft doc last updated: 09/15/2025


This article describes how to relocate [Azure Static Web Apps](https://learn.microsoft.com/en-us/azure/static-web-apps/overview) resources to another Azure region.

There are various reasons why you may want to move your existing Azure resources from one region to another. You may want to:

- Take advantage of a new Azure region.
- Deploy features or services available in specific regions only.
- Meet internal policy and governance requirements.
- Align with company mergers and acquisitions
- Meet capacity planning requirements.

## Prerequisites

Review the following prerequisites before you prepare for the relocation.

- [Validate that Azure Static Web Apps is available in the target region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/).
- Make sure that you have permission to create Static Web App resources in the target region.
- Find out if there any Azure Policy region restrictions applied to your organization.
- If using integrated API support provided by Azure Functions:

  - Determine the availability of Azure Functions in the target region.
  - Determine if Function API Keys are being used. For example, are you using Key Vault or do you deploy them as part of your application configuration files?
  - Determine the deployment model for API support in the target region: [Bring Your own functions](https://learn.microsoft.com/en-us/azure/static-web-apps/functions-bring-your-own). Understand the differences between the two models.

- Ensure that the Standard Hosting Plan is used to host the Static Web App. For more information about hosting plans, see [Azure Static Web Apps hosting plans](https://learn.microsoft.com/en-us/azure/static-web-apps/plans).
- Determine the permissible downtime for relocation.
- Depending on your Azure Static Web App deployment, the following dependent resources may need to be deployed and configured in the target region *prior* to relocation:

  - [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-functions).
  - [Azure Virtual Network](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-virtual-network)
  - [Azure Front Door](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview)
  - [Network Security Group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-virtual-network-nsg)
  - [Azure Private Link Service](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-private-link)
  - [Azure Key Vault](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-key-vault)
  - [Azure Storage Account](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-storage-account)
  - [Azure Application Gateway](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-app-gateway)

## Downtime

The relocation of an Azure Static Web site introduces downtime to your application. The downtime is affected by which high availability pattern you have implemented for your Azure Static Web site. General patterns are:

- **Cold standby**: Workload data is backed up regularly based on its requirements. In case of a disaster, the workload is redeployed in a new Azure region and data is restored.
- **Warm standby**: The workload is deployed in the business continuity and disaster recovery (BCDR) region, and data is replicated asynchronously or synchronously. In the event of a disaster, the deployment in the disaster recovery (DR) region is scaled up and out.
- **Multi-region**: The workload is [deployed in both regions](https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/multi-region) and data is replicated synchronously. Both regions have a writable copy of the data. The implementation can be active/passive or active/active.

## Prepare

### Deployments with private endpoints

If your Static Web Apps is deployed with private endpoints, make sure to:

- Update host name for connection endpoint.
- Update host name on DNS private zone or custom DNS server (only applicable to Private Link).

For more information, see [Configure private endpoint in Azure Static Web Apps](https://learn.microsoft.com/en-us/azure/static-web-apps/private-endpoint).

### All other deployments

For all other deployment types, make sure to:

- If applicable, retrieve the new Function API keys from Azure Functions in the new region.
- If the Azure Function has a dependency on a database, ensure that the `DATABASE_CONNECTION_STRING` is updated. This database may not be in scope of regional migration.
- Update the custom domain to point to the new hostname of the static web app.
- If using Key Vault, provision a new Key Vault in target region. Update the Function API Keys in Key Vault if applicable. Any other sensitive data not to be stored in code or config files should be stored in this Key Vault

### Export the template

To export the Resource Manager template that contains settings that describe your static web app:

1. Sign in to the [Azure portal](https://portal.azure.com).
1. Go to your static web app.
1. From the left menu, under *Automation*, select **Export template**.

    The template may take a moment to generate.

1. Select **Download**.
1. Locate the downloaded `.zip` file, and open it into a folder of your choice.

    This file contains the `.json` files that include the template and scripts to deploy the template.

1. Make the necessary changes to the template, such as updating the location with target region.

## Relocate

Use the following steps to relocate your static web app to another region.

1. If you're relocating with Private Endpoint, follow the guidelines in [Relocate Azure Private Link Service to another region](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-private-link).
1. If you've provided an existing Azure Functions to your static web app, follow the relocation procedure for [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-functions).
1. Redeploy you static web app using the [template that you exported and configured in the previous section](#export-the-template).

    >[!IMPORTANT]
    > If you're not using a custom domain, your application's URL changes in the target region. In this scenario, ensure that users know about the URL change.

1. If you're using an Integrated API, create a new Integrated API that's supported by Azure Functions.
1. Reconfigure your repository (GitHub or Azure DevOps) to deploy into the newly deployed static web app in the target region. Initiate the deployment of the application using GitHub actions or Azure Pipelines.
1. With a *cold standby* deployment, make sure you inform clients about the new URL. If you're using a custom DNS domain, change the DNS entry to point to the target region. With a *warm standby* deployment, a load balancer, such as Front Door or Traffic manager handle migration of the static web app in the source region to the target region.
