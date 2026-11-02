# Learn about collecting files that match DLP policies from devices

> Source: https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-learn  
> Microsoft doc last updated: 2026-06-22


When you're investigating a Microsoft Purview Data Loss Prevention (DLP) incident or troubleshooting a DLP policy, it can be helpful to have a complete copy of the item that matched the policy to refer to. DLP can copy the item that matches a DLP policy from onboarded Windows devices or macOS devices (preview) to an Azure storage account. DLP incident investigators and administrators that have been granted the appropriate permissions on the Azure storage blob can then access the files.

To get started configuring and using the feature, see [Get started with collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

If you're new to Microsoft Purview DLP, here's a list of the core articles you need as you implement DLP:

1. [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units)
2. [Learn about Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) - This article introduces you to the data loss prevention discipline and Microsoft's implementation of DLP.
3. [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#plan-for-data-loss-prevention-dlp)- by working through this article you will:
    1. [Identify stakeholders](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#identify-stakeholders)
    2. [Describe the categories of sensitive information to protect](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#describe-the-categories-of-sensitive-information-to-protect)
    3. [Set goals and strategy](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#set-goals-and-strategy)
4. [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference) - This article introduces all the components of a DLP policy and how each one influences the behavior of a policy.
5. [Design a DLP policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) - This article walks you through creating a policy intent statement and mapping it to a specific policy configuration.
6. [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) - This article presents some common policy intent scenarios that you'll map to configuration options, then it walks you through configuring those options.

## Where evidence collection for file activities on devices fits in Purview

Endpoint DLP is part of the [larger DLP offering](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) and part of the larger range of services offered in [Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview). You should understand how evidence collection for file activities on devices fits into the larger set of service offerings.

### Evidence collection for file activities on devices and eDiscovery

This feature makes copies of items that match DLP policies on onboarded Windows devices or macOS devices (preview) and places those copies in an Azure storage account. These copies aren't held in a changeless state and aren't evidence in the legal sense of the term. If you need to find and hold items for legal purposes, you should use the [Microsoft Purview eDiscovery solutions](https://learn.microsoft.com/en-us/purview/ediscovery). Electronic discovery, or eDiscovery, is the process of identifying and delivering electronic information that can be used as evidence in legal cases.

### Evidence collection for file activities on devices and contextual summary

When an item and the activity that a user takes on that item match the conditions defined in a DLP policy, a **DLPRuleMatch** event shows up in [Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). This is true for every location that DLP supports. The **DLPRuleMatch** event contains a limited amount of the text that surrounds the matched content. This limited amount of text is called [contextual summary](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#contextual-summary).

It's important to understand the difference between evidence collection for file activities on devices and a contextual summary. Evidence collection for file activities on devices are available for onboarded Windows devices or macOS devices (preview). It saves a copy of the entire item that matched a policy to the Azure storage account. A contextual summary is captured for every DLP policy rule match and only contains a limited amount of the text that surrounds the target text that triggered the match.

### Evidence collection for file activities on devices and Data Security Investigations

[Microsoft Purview Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations) can query endpoint DLP evidence collection data as an additional data source for security investigations. Investigators can use the [endpoint DLP evidence collection (preview)](https://learn.microsoft.com/en-us/purview/data-security-investigations-search#endpoint-dlp-evidence-collection-preview) search option in Data Security Investigations to aggregate endpoint events and analyze them collectively using AI-powered tools, rather than triaging individual alerts one by one. Data Security Investigations queries whatever data is already collected by your endpoint DLP policies — no additional configuration is required beyond enabling evidence collection.

## Covered user activities

You can configure evidence collection for file activities on devices to save a copy of a matched item to the Azure storage account when a user attempts to do one of these activities on a matched item:

- Copy to a removable USB
- Copy to network share
- Print
- Copy or move using unallowed Bluetooth app
- Copy or move through RDP
- Upload to cloud service domains or access from an unallowed browser
- Paste to supported browsers
- Access by restricted apps

The detection of these activities is configured in the DLP policy. For more information on how to create a DLP policy, see, [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) and [Using Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-using).

## Covered actions

When you enable evidence collection for file activities on devices in Endpoint DLP settings and configure a DLP policy to use this feature, it saves a copy of a matched item for these actions:

- Audit only
- Block with override
- Block

These actions are configured in the DLP policy. For more information on how to create a DLP policy, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) and [Using Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-using).

## Design considerations

### Regions for your Azure Storage accounts

To comply with regulatory requirements, make sure that the Azure storage accounts that you use are in the same geopolitical or regulatory boundaries as the devices that they're being copied from. Also, be aware of the geopolitical location of the DLP investigators who will access the sensitive items once they're saved. Consider using [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units) to scope the administration of the users and devices appropriately for each DLP policy. To learn how to use data loss prevention to comply with data privacy regulations, see [Deploy information protection for data privacy regulations with Microsoft Purview](https://go.microsoft.com/fwlink/?linkid=2239593&amp;clcid=0x409). Evidence collection for file activities on devices supports up to 10 Azure storage accounts.

To learn how to use data loss prevention to comply with data privacy regulations, see [Deploy information protection for data privacy regulations with Microsoft Purview](https://go.microsoft.com/fwlink/?linkid=2239593&amp;clcid=0x409).

### Local storage and bandwidth

By default, copies of matched items are saved asynchronously to the configured Azure storage account over the existing network connection. If the device doesn't have connectivity, matched items are save locally, up to the 500-MB limit. You can save items locally up to 60 days.

While the device has connectivity to the Azure storage account URL, there's no limit on bandwidth usage. The bandwidth that evidence collection for file activities on devices uses doesn't affect the default or configured bandwidth limits for [Advanced classification scanning and protection](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection).

### Azure storage accounts

Customers are responsible for creating and managing their own Azure storage accounts. If you're new to Azure storage, see:

- [What is Azure Blob storage](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/storage-blobs-overview)
- [Introduction to Azure Storage](https://learn.microsoft.com/en-us/en-us/azure/storage/common/storage-introduction)
- [Create a storage account](https://learn.microsoft.com/en-us/en-us/azure/storage/common/storage-account-create)

Items that match a policy are copied from the users' device to the Azure storage account blob in the security context of the logged in user. So, all users who are in-scope for the policy must have read and write permission to the blob storage. For more information, see [Get started with collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started)

Similarly, all administrators who are reviewing the saved items must have `read` permission to the Azure storage account blob. For more information, see [Get started with collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started).

## Storing evidence when sensitive information is detected

### Supported file types

For more information on supported file types, see [Supported file types for storing and previewing evidence](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started#supported-file-types-for-storing-and-previewing-evidence).

### Supported storage types

You have two options for storing the evidence Purview collects when it detects sensitive information in your content. You can use a **Customer-managed** data store, or a **Microsoft Managed** data store. The option you should use depends on your requirements and your use cases. To help you decide, review the comparison table that follows.

#### Storage type comparison

Matched files continue to be included in alert results even after changing your storage type as long as the role-based access control (RBAC) permissions remain intact. Since customer managed storage is owned by customers, DLP admins can continue to download files directly from the storage on a per-file basis.

The following table identifies the differences between customer-managed storage and Microsoft-managed storage for collecting evidence of the sensitive information detected in your content.

| Feature Element | Customer Managed | Microsoft Managed |
| --- | --- | --- |
| File retention | You can keep files as long as you need/want to. | Files are retained for a maximum of 180 days. |
| Upload limit | You can upload files based on your blob storage size settings. | You can upload upto 5 GB per day at the overall tenant level. |
| Endpoint settings | You must add blob storage (container URLs) in the endpoint settings and then use the [Microsoft Entra admin center](https://entra.microsoft.com/#home) to configure explicit user permissions on the blob for in-scope users. | All configuration and permissions are handled with a single click when configuring your endpoint settings. |
| Policy and location configuration | You must add and configure storage blobs on a per-policy basis for each location where a policy is applied. | No storage selection is needed for specific policy locations. |
| Access to storage | Users with relevant permissions to storage blob can access the evidence | No human access to storage. Evidence is uploaded and rendered by the system. |
| Data store location/region | Chosen by the customer | The same region as your Microsoft Purview tenant. |
| Charges | Storage costs are charged in addition to the cost of your Entra subscription. | Storage cost today is included in E5. However, Microsoft will monitor storage usage and may charge additionally based on excessive usage. This will be communicated to customers separately should there be a change in the business model. |
| Network configuration | You must allow the container URLs for your storage blobs to pass through your network firewall. | You must include **compliancedrive.microsoft.com** on an "allow" list, so that it can pass through the network firewall. |
| Retention | Customers can selectively archive and purge to free up storage) | 30 days on Purview and 180 days on Defender XDR |
| Preview and Download Permissions | Read access on storage blobs, RBAC roles **Data Classification Content Viewer** to preview the evidence and **Data Classification Content Download** to download the evidence | RBAC roles **Data Classification Content Viewer** to preview the evidence and **Data Classification Content Download** to download the evidence |

#### Changing storage types

Customers can switch between storage types at any time. However, best practice is to carefully plan for the type of storage you'll need over the long term and select the appropriate option for your use case. For more information on the differences between the two types of storage, see the Storage type comparison table.

Note

When switching storage types, you'll need to refresh your policies to ensure that they are applied to the files in the new data store.

#### Impact of changing storage types on evidence files

Matched files continue to be included in alert results, even after you change the storage management type, provided that the role-based access control (RBAC) permissions do not change.

Because you own your customer-managed storage solution, your DLP admins can continue to download files directly on a per-file basis after they have been moved to the Microsoft-managed storage solution.
