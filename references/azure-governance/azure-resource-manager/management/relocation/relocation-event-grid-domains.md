# Relocate Azure Event Grid domains to another region

> Source: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-grid-domains  
> Microsoft doc last updated: 09/15/2025


This article covers the recommended approach, guidelines, and practices to relocate Event Grid domains to another region.

There are various reasons why you may want to move your existing Azure resources from one region to another. You may want to:

- Take advantage of a new Azure region.
- Deploy features or services available in specific regions only.
- Meet internal policy and governance requirements.
- Align with company mergers and acquisitions
- Meet capacity planning requirements.

The high-level steps are:

- **Export the domain** resource to an Azure Resource Manager template.

    > [!IMPORTANT]
    > The domain resource and topics in the domain are exported to the template. Subscriptions to domain topics aren't exported.
- **Use the template to deploy the domain** to the target region.
- **Create subscriptions for domain topics manually** in the target region. When you exported the domain to a template in the current region, subscriptions for domain topics aren't exported. So, create them after the domain and domain topics are created in the target region.
- **Verify the deployment**. Send an event to a domain topic in the domain and verify the event handler associated with the subscription is invoked.
- To **complete the move**, delete domain from the source region.

## Prerequisites

- Ensure that the Event Grid service is available in the target region. See [Products available by region](https://azure.microsoft.com/global-infrastructure/services/?products=event-grid&regions=all).

## Prepare

To get started, export a Resource Manager template for the domain.

1. Sign in to the [Azure portal](https://portal.azure.com).
1. In the search bar, type **Event Grid Domains**, and select **Event Grid Domains** from the results list.

    

1. Select the **domain** that you want to export to a Resource Manager template.

    

1. On the **Event Grid Domain** page, select **Export Template** under **Settings** on the left menu, and then select **Download** on the toolbar.

    

    > [!IMPORTANT]
    > Domain and domain topics are exported. Subscriptions for domain topics aren't exported. So, you need to create subscriptions for domain topics after you move domain topics.

1. Locate the **.zip** file that you downloaded from the portal, and unzip that file to a folder of your choice. This zip file contains template and parameters JSON files.
1. Open the **template.json** in an editor of your choice.
1. Update `location` for the **domain** resource to the target region or location. To obtain location codes, see [Azure locations](https://azure.microsoft.com/global-infrastructure/locations/). The code for a region is the region name with no spaces, for example, `West US` is equal to `westus`.

    ```json
    "type": "Microsoft.EventGrid/domains",
    "apiVersion": "2020-06-01",
    "name": "[parameters('domains_spegriddomain_name')]",
    "location": "westus",
    ```

1. **Save** the template.

## Redeploy

Deploy the template to create the domain and domain topics in the target region.

1. In the Azure portal, select **Create a resource**.
1. In **Search the Marketplace**, type **template deployment**, and then press **ENTER**.
1. Select **Template deployment**.
1. Select **Create**.
1. Select **Build your own template in the editor**.
1. Select **Load file**, and then follow the instructions to load the **template.json** file that you downloaded in the last section.
1. Select **Save** to save the template.
1. On the **Custom deployment** page, follow these steps:
    1. Select an Azure **subscription**.
    1. Select an existing **resource group** in the target region or create one.
    1. For **Region**, select the target region. If you selected an existing resource group, this setting is read-only.
    1. For the **domain name**, enter a new name for the domain.
    1. Select **Review + create**.

        

    1. After the validation of the template succeeds, select **Create** at the bottom of the page to deploy the resource.
    1. After the deployment succeeds, select **Go to resource group** to navigate to the resource group page. Confirm that there's a domain in the resource group. Select the domain. Confirm that there are domain topics in the domain.

## Discard or clean up

To complete the move, delete the domain in the source region.  

If you want to start over, delete the domain in the target region, and repeat steps in the [Prepare](#prepare) and [Recreate](#redeploy) sections of this article.

To delete a domain by using the Azure portal:

1. In the search window at the top of Azure portal, type **Event Grid Domains**, and select **Event Grid Domains** from search results.
1. Select the domain to delete, and select **Delete** from the toolbar.
1. On the confirmation page, enter the name of the resource group, and select **Delete**.  

To delete the resource group that contains the domain by using the Azure portal:

1. In the search window at the top of Azure portal, type **Resource groups**, and select **Resource groups** from search results.
1. Select the resource group to delete, and select **Delete** from the toolbar.
1. On the confirmation page, enter the name of the resource group, and select **Delete**.  

## Related content

- [Relocate system topics across regions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-grid-system-topics).
- [Relocate custom topics across regions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/relocation/relocation-event-grid-custom-topics).
- [Move resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).
