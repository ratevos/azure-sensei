# SharePoint activity reports - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/sharepoint-activity-ww  
> Microsoft doc last updated: 04/24/2026


The SharePoint activity report provides details about the activity of every licensed SharePoint user by looking at their interaction with files. The report helps you understand the level of collaboration by showing the number of files shared.

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the SharePoint activity report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **SharePoint**.
1. On the report page, select the **Activity** tab.
  
## Interpret the SharePoint activity report

To add or remove columns from the report, select **Choose columns**.

To export the report data into an Excel .csv file, select the **Export** link. This action exports data for all users and lets you do simple sorting and filtering for further analysis.

The SharePoint activity report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date (not the date the report was generated).
  
|Metric|Definition|
|:-----|:-----|
|Username  |The email address of the user who performed the activity on the SharePoint Site. |
|Last activity date (UTC)  |The latest date a file activity was performed or a page was visited for the selected date range. To see activity that occurred on a specific date, select the date directly in the chart. |
|Files viewed or edited  |The number of files that the user uploaded, downloaded, modified, or viewed.  |
|Files synced   |The number of files that are synced from a user's local device to the SharePoint site. |
|Files shared internally  | The count of files that are shared with users within the organization, or with users within groups (that might include external users). |
|Files shared externally  |The number of files that are shared with users outside of the organization. |
|Pages visited  |The visits to unique pages by the user. |
|Deleted  | This value indicates that the user's license was removed.<br/><br/>**NOTE:** Activity for a deleted user still displays in the report as long as the user was licensed at some time during the selected time period. The Deleted column helps you to note that the user might no longer be active, but contributed to the data in the report.  |
|Deleted date  |The date on which the user's license was removed. |
|Product assigned  |The Microsoft 365 products that are licensed to the user.|

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).
