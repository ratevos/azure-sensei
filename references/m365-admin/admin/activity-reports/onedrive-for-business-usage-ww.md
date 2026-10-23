# OneDrive usage report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/onedrive-for-business-usage-ww  
> Microsoft doc last updated: 04/24/2026


The OneDrive usage report provides a high-level view of the value you get from OneDrive. The report includes details about the total number of accounts, files, and storage used across your organization. You can drill into it to understand the trends of active OneDrive accounts, how many files users are interacting with, and the amount of storage used. It also gives you details for each user's OneDrive.

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the OneDrive usage report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **OneDrive**.
1. On the report page, select the **Usage** tab. 
  
## Interpret the OneDrive usage report

To add or remove columns from the report, select **Choose columns**.  

To export the report data into an Excel .csv file, select the **Export** link. This action exports data for all users and lets you do simple sorting and filtering for further analysis.

The OneDrive usage report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date (not the date the report was generated).
  
|Metric|Definition|
|:-----|:-----|
|URL |The web address for the user's OneDrive. Note: URL is temporarily empty. |
|Deleted  |The deletion status of the OneDrive. It takes at least seven days for accounts to be marked as deleted. |
|Owner |The username of the primary administrator of the OneDrive. |
|Owner principal name |The email address of the owner of the OneDrive. |
|Last activity date (UTC) | The latest date a file activity was performed in the OneDrive. If the OneDrive has no file activity, the value is blank. |
|Files |The number of files in the OneDrive. |
|Active files | The number of active files within the time period.<br/><br/> **NOTE:** If you remove files during the specified time period for the report, the number of active files shown in the report might be larger than the current number of files in the OneDrive. >  Deleted users continue to appear in reports for 180 days. |
|Storage used (MB) |The amount of storage the OneDrive uses in MB. |
| Site ID | The site ID of the site. |

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

> [!IMPORTANT]
> The report only includes users who have a valid OneDrive license.

> [!NOTE]
> The OneDrive site URL might not be displayed in related usage reports. You can use PowerShell to display the site URL. For more information, see [Use PowerShell to resolve site URLs](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/resolve-site-urls).
