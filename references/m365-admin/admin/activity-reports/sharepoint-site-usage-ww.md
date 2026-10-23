# SharePoint site usage report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/sharepoint-site-usage-ww  
> Microsoft doc last updated: 04/28/2026


The SharePoint site usage report provides a high-level view of the value you get from SharePoint. The report includes details about the total number of files that users store in SharePoint sites, how many files are actively used, and the storage consumed across all these sites. You can drill into the SharePoint site usage report to understand the trends and per-site level details for all sites.

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the SharePoint site usage report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **SharePoint**.
1. On the report page, select the **Site usage** tab.

## Interpret the SharePoint site usage report

To add or remove columns from the report, select **Choose columns**.

To export the report data into an Excel .csv file, select the **Export** link. This action exports data for all users and lets you do simple sorting and filtering for further analysis.

The SharePoint site usage report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date (not the date the report was generated).

|Metric|Description|
|:-----|:-----|
|Site URL  |The full URL of the site. |
|Deleted  |The deletion status of the site. The site is marked as deleted after at least 7 days.  |
|Site owner  |The username of the primary owner of the site.   |
|Site owner principal name  |The email address of the owner of the site. |
|Last activity date (UTC)  | The most recent date when activity occurred on the site or OneDrive account within the selected reporting period. Last activity date is retained for up to 180 days. For active and inactive sites, the report shows the most recent activity date within that 180-day window. If a site is disabled, the last activity date is dropped and might no longer appear in the report.  |
|Site sensitivity label ID  | The sensitivity label on the site.  |
|External sharing  | The value of the external sharing setting for the site. This value doesn't reflect changes to the effective setting made by site sensitivity labels. If you use sensitivity labels, use the [data access governance reports](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports) to get the correct values.|
|Unmanaged device policy  | The site access policy for unmanaged devices.  |
|Geo location  | The Geo location of the site.  |
|Files  |The number of files on the site. |
|Active files  | The number of active files on the site. A file is active if it's saved, synced, modified, or shared within the specified time period.<br/> **NOTE:** If files were removed during the specified time period for the report, the number of active files shown in the report might be larger than the current number of files on the site.  |
|Storage used (MB)  |The amount of storage currently used on the site.  |
|Storage allocated (MB)  |The maximum amount of storage allocated for the site.  |
|Page views  |The number of times pages were viewed on the site.  |
|Pages visited  |The number of unique pages that were visited on the site.  |
|Anonymous link count  |The number of times documents or folders are shared using "Anyone with the link" on the site.  |
|Company link count  |The number of times documents or folders are shared using "People in org with the link" on the site.  |
|Secure link for guest count  |The number of times documents or folders are shared using "specific people" on the site.  |
|Secure link for member count  |The number of times documents or folders are shared using "specific people" on the site.  |
|Root Web Template  |The template used for creating the site.<br/><br/>**NOTE**: To filter the data by different site types, export the data and use the Root Web Template column. |
|Site ID | The site ID of the site. |

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

>[!NOTE]
>The SharePoint site URL doesn't display if [BYOK](https://learn.microsoft.com/en-us/azure/information-protection/byok-price-restrictions) or [Customer Lockbox](https://learn.microsoft.com/en-us/azure/security/fundamentals/customer-lockbox-overview) is enabled. If you meet the requirement, submit a request via [ODSP Site URLs Displaying Request](https://forms.office.com/r/16hLY6na5W). The site URL is visible within one week. If the requirement isn't met, you can use PowerShell. To follow the steps, see [Use PowerShell to resolve site URLs](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/resolve-site-urls).

You might see differences between the sites listed in the Site udage report and those listed on the **Sites** > <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">Active sites</a> page in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> because certain site templates and URLs aren't included as Active sites. For more information, see [Manage sites in the SharePoint admin center](https://learn.microsoft.com/en-us/sharepoint/manage-sites-in-new-admin-center).
