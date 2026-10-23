# Microsoft 365 Copilot readiness report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-readiness  
> Microsoft doc last updated: 04/03/2026


The Microsoft 365 Copilot readiness report helps you identify which users are technically eligible for Copilot and streamline your organization's rollout. From the report, you can assign licenses and monitor usage of Microsoft 365 apps that Copilot integrates best with. The report is available within 72 hours, and once available, the usage data shown in the report can have up to a maximum of 72 hours latency.

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the Microsoft 365 Copilot Readiness and usage report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **Microsoft 365 Copilot**, and then select **Copilot**.
1. On the report page, you can view **Readiness** on the first tab. Select the **Usage** tab to view adoption and usage metrics.

## Interpret the Readiness section in the Microsoft 365 Copilot report

Use the Microsoft 365 Copilot readiness report to see how ready your organization is to adopt Microsoft 365 Copilot. The Readiness section shows your data over the past 28 days.

You can see the following summary charts in this report:

- **Total Prerequisite Licenses**: The number is the sum of all users who have at least one license assigned to them or who can be assigned a license. To learn more about the license types eligible for Copilot, see [Licensing requirements for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing).

- **Users on an eligible update channel**: This number is the sum of all users who are enrolled in Current Channel or Monthly Enterprise Channel for app updates in your organization and can be assigned a Copilot license.

- **Assigned Licenses**: This number is the sum of all users who are already assigned a Copilot license in your organization.

- **Available Licenses**: This number is the sum of all users who don't have a Copilot license assigned, and should be prioritized first.

Recommended action cards highlight important actions to take to prepare your organization for Copilot, such as moving users to a monthly app update channel and assigning available Copilot licenses.

The last recommended action card promotes the [Microsoft Copilot Dashboard](https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard), where you can deliver insights to your IT leaders to explore Copilot readiness, adoption, and impact in Viva Insights.

This graph shows the sum of users who could benefit the most from Copilot based on where Copilot provides the most value in day-to-day scenarios. By default, it's sorted by descending order across all rows by column **Suggested candidate for Copilot**.

Use the user table to get an at-a-glance view of which users are assigned a Copilot license, whether their devices are configured correctly, and if they're using a Microsoft 365 app that has Copilot enabled.

You can also export the report data into an Excel .csv file by selecting the Export link. This action exports the Microsoft 365 Copilot readiness data of all users with any engagement on Teams meetings, Teams chat, and Outlook email for Office docs in the past 30 days. By exporting this data, you can do simple sorting, filtering, and searching for further analysis.

To ensure data quality, the system performs daily data validation checks for the past three days and fills any detected gaps. You might notice differences in historical data during the process.

## User activity table

| Item | Description |
|------|-------------|
| User name| The user's principal name. |
| Has Copilot license been assigned | Yes/No field indicating if the user has a Copilot license assigned to them. |
| Uses eligible update channel      | Yes/No field indicating if devices are configured to get the latest or monthly updates. |
| Uses Teams Meetings               | Indicates whether the user attended at least one meeting using Teams in the past 30 days. |
| Uses Teams chat                   | Indicates whether the user participated in at least one chat using Teams in the past 30 days. |
| Uses Outlook Email                | Indicates whether the user sent at least one email using Outlook in the past 30 days. |
| Uses Office docs                  | Indicates whether the user collaborated on at least one document or file using OneDrive or SharePoint in the past 30 days. |
| Suggested candidate for Copilot   | Indicates the top 25% of nonlicensed users based on their Microsoft 365 app usage over the prior month. For more information, see [Extra details for Suggested candidate for Copilot](#extra-details-for-suggested-candidate-for-copilot).  |

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

## Extra details for Suggested candidate for Copilot

The **Suggested candidate for Copilot** column in the Microsoft 365 Copilot Readiness report helps organizations identify users who might benefit most from Microsoft 365 Copilot as part of initial rollouts and pilot programs. Each week, the feature flags the top 25% of nonlicensed users within an organization. The flagged users are based on their consistent usage of the Microsoft 365 applications where Copilot adds value, such as Microsoft Teams and Outlook. Admins can use this information to prepare a data-driven licensing plan for their Copilot rollout. The following list contains key details about this feature:

- The feature analyzes the Microsoft 365 usage across the users that aren't assigned Copilot licenses each week. It then flags the top 25% of them as suggested candidates. This selection is based on app usage intensity in applications where Microsoft 365 Copilot provides value, such as Microsoft Outlook, Teams, and Word.
- The feature is only available to customers who purchase Microsoft 365 Copilot licenses.
- The feature doesn't rank users within the selected 25% group; there's no individual stack ranking among suggested candidates.
- Each week, the feature reevaluates the user base and suggests the top 25% based on usage metrics for the preceding 28-day period. Users that are assigned a Microsoft 365 Copilot license are removed from consideration. Over time, every eligible user in the organization can be flagged as a suggested candidate for Copilot.
- To support interpretability, several of the inputs to the suggestion model are also shown in the Copilot readiness details table. Users that actively used Teams meetings, Teams chats, Outlook emails, or Office docs over the preceding 28 day period have a "Yes" value in the columns corresponding with each of these applications.
- The intended purpose of this capability is to support organizations with the rollout of Microsoft 365 Copilot by highlighting users who are most likely to quickly benefit from its capabilities based on their consistent usage of Microsoft 365 apps. It's not intended to be used to evaluate employee performance.

## Related content

- [Microsoft 365 Copilot service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot) (article)
- [Set up Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup) (article)
- [Microsoft 365 Copilot Adoption](https://adoption.microsoft.com/copilot/) (resources)
