# Exchange Web Services usage report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/ews-usage  
> Microsoft doc last updated: 04/03/2026


The Exchange Web Services (EWS) usage report displays the SOAP actions used by each application calling EWS in your organization. It also shows the successful-call volume for each SOAP action. This information enables you to coordinate with the application owners to ensure they're preparing for the [EWS deprecation in October 2026](https://techcommunity.microsoft.com/blog/exchange/retirement-of-exchange-web-services-in-exchange-online/3924440).

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the EWS usage report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **Exchange**.
1. On the report page, select the **EWS usage** tab.

## Interpret the EWS usage report

To review the applications that use EWS within your organization, examine the **Usage trend** and **Usage details** sections. Additionally, summarized information at the top provides an overview of the overall usage.

You can filter the EWS usage report by the last 7, 30, or 90 days.

> [!NOTE]
> Usage data is collected and aggregated weekly, not daily.

### Summary data

Two summary headers appear at the top of the page:

- **Active apps** shows the number of unique apps that sent at least one request to EWS during the selected period.
- **Daily average call volume** shows the average number of daily requests from active apps during the selected period.

### Usage trend chart

The usage trend chart displays the projected EWS usage trend in your tenant, using weekly data points that summarize all active apps in your tenant that use EWS during that week. The Y-axis represents the number of apps, and the X-axis indicates the first date of the week within the selected period.

### Usage details table

The following table provides a breakdown of the EWS usage per SOAP action by each active application in your tenant during the selected period. You can't customize the columns.

| Item | Description |
|---------|---------|
|Application ID    |The Microsoft Entra identifier for the registered application |
|SOAP Action     |The specific Exchange Web Service SOAP action executed |
|Call Volume    |The number of SOAP action calls in the given period |
|Last Activity date (UTC) |The last date of activity recorded for that app and SOAP action |

Select the **Export** link to export the report data into an Excel .csv file. For a list of Microsoft first-party client application IDs, see [Commonly used Microsoft first-party services and portal apps](https://learn.microsoft.com/en-us/power-platform/admin/apps-to-allow). For Microsoft applications, Microsoft updates those periodically to remove EWS dependencies. Keep your client applications up-to-date. If you still can't find the Application ID, check your Enterprise Applications in Entra ID. For more information, see [Quickstart: View enterprise applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/view-applications-portal).
