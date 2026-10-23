# Microsoft 365 Copilot Agents usage report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-agents-new  
> Microsoft doc last updated: 04/03/2026


The Microsoft 365 Copilot Agent usage report helps you track how agents are used in Microsoft 365 Copilot Chat and Microsoft 365 apps – Word, Excel, and PowerPoint. You can see which agents both licensed and unlicensed Microsoft 365 Copilot users use across Declarative, SharePoint, and Custom engine agents. These agents include agents built by your org, Microsoft, and Microsoft Partners.

You can view usage within an hour from when users interact with agents. The report includes key metrics such as:

- Total active users and agents
- Summary and daily time series
- Active usage per user, per agent, and per agent-user pair

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the Microsoft 365 Copilot Agents usage report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **Microsoft 365 Copilot**, and then select **Agents**.

## Interpret the Microsoft 365 Copilot Agents usage report

Use the Agents usage report to see the usage of agents in your organization that your organization, Microsoft, or Microsoft Partners built. These agents include agents that an admin approves and agents that users create through agent builder and share with users in your org. Admins can manage agents in the same way as they manage any other app in the Copilot Control system section of the Microsoft 365 admin center. For more information, see [Manage agents for Microsoft 365 Copilot in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps).  

At the top of the report, you can filter by different periods. You can view the agent report over the last 7 or 30 days.

> [!NOTE]
> The data for declarative agents in Agent usage preview report is available as of August 19, 2025. For SharePoint agents and Custom engine agents, it's available as of November 11, 2025.

- **Total active users** shows you how many unique users in your organization - whether they have a Microsoft 365 Copilot license or not - used agents in Microsoft 365 Copilot Chat during the selected time period. This count includes agents created by your organization, Microsoft, or Microsoft partners.

- **Active users (licensed)** shows you how many unique users in your org who had a Microsoft 365 Copilot license used agents in Microsoft 365 Copilot Chat during the selected time period.

- **Active users (unlicensed)** shows you how many unique users in your org, who didn't have a Microsoft 365 Copilot license and used agents in Microsoft 365 Copilot Chat during the selected time period.  

- **Total active agents** shows you how many unique apps with an agent element in that app with at least one active user over the selected time period. This count includes agents created by your org, including agents both admin approved and shared by users in your org, Microsoft built agents, and agents built by Microsoft partners.

End-users interact with agents in two ways: either by at-mentioning the agent in a chat experience, by selecting the agent from the side panel in Microsoft 365 Copilot Chat, or from the hamburger menu on the top left corner in Microsoft 365 Copilot in Word, Excel, or PowerPoint. An active user of an agent is a user who sends a prompt request to an agent and receives a response.

To learn more about managing and enabling agents in your org, see [Manage agents for Microsoft 365 Copilot in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps).

### Users by license type

The definition of active users (licensed and unlicensed) is the same as provided earlier.  

You can switch between **Summary** view and **Trend** view.

- **Summary view** shows how many users with a Microsoft 365 Copilot license used agents compared with users who don't have a Microsoft 365 Copilot license, over the selected time frame.

- **Trend view** shows daily agent usage over the selected time frame, comparing how many users with a Microsoft 365 Copilot license used agents compared with users who don't have a Microsoft 365 Copilot license.

### Users by creator type

Shows how many users actively used an agent, grouped by who created the agent.

The definition of active users is the same as provided earlier. The **Creator type** tells you who built the agent. The following table describes the different types:

| Creator type value | Description |
| --- | --- |
| User | Agents created by individuals in your organization using tools like [agent builder](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder). These agents aren't listed in the organization-wide catalog but users can use them for themselves, or share them via a link with others in the same organization. |
| Your org  | Agents created by individuals in your organization using tools like [Microsoft 365 Agents Toolkit](https://learn.microsoft.com/en-us/microsoft-365/developer/overview-m365-agents-toolkit) or [Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and admin-approved for broader use across your org. |
| Microsoft  | Agents built by Microsoft  |
| Microsoft partner  | Agent built by Microsoft partners and admin-approved for use in your org.   |
| Any | The agent is any of the listed creator types, such as User, Your org, Microsoft, or Microsoft Partner.  |

You can switch between **Summary** view and **Trend** view.

- **Summary view** shows how many users used an agent where the agent was one of the Creator types described earlier, regardless of whether the user had a Microsoft 365 Copilot license, over the selected time frame.  

- **Trend view** shows daily usage of agents - how many users used an agent each day where the agent was one of the Creator types described earlier, regardless of whether the user had a Microsoft 365 Copilot license, over the selected time frame.

### Agents by creator type

Shows how many agents users in your organization used, grouped by who created the agent.

The definition of **active agents** and **Creator type** is the same as provided earlier.

You can switch between **Summary** view and **Trend** view.

- **Summary view** shows how many agents users in your org used where the agent was one of the Creator types described earlier, regardless of whether the users had a Microsoft 365 Copilot license, over the selected time frame.

- **Trend view** shows daily usage of agents - how many agents users in your org used each day where the agent was one of the Creator types described earlier, regardless of whether the user had a Microsoft 365 Copilot license, over the selected time frame.

### User details table

| Item | Description |
| --- | --- |
| Username | The user's principal name. |
| Display name | The full name of the user.  |
| Number of agents used  | The number of distinct agents the user used for the selected time period.  |
| Agent responses received  | Total responses from all agents used during the selected time period.   |
| Last activity date (UTC)  | The most recent date the user used an agent, regardless of the selected time period of past 7 or 30 days.   |

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

### Agent details table

| Item | Description |
| --- | --- |
| Agent ID | An agent is an element of an app. The ID is the app identifier generated by Microsoft.|
| Agent name | The name of the app as present in the app manifest.  |
| Creator type | Indicates who built the agent. The following list defines the values:<ul><li>**User** are agents created by individuals in your organization using tools like [agent builder](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder). These agents aren't listed in the organization-wide catalog, but users can use the agents for themselves, or share agents via a link with others in the same organization.</li><li>**Your org** are agents created by individuals in your organization using tools like [Microsoft 365 Agents Toolkit](https://learn.microsoft.com/en-us/microsoft-365/developer/overview-m365-agents-toolkit), [Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and admin-approved for broader use across your org.</li><li>**Microsoft** are agents built by Microsoft.</li><li>**Microsoft partner** are agent built by Microsoft partners and admin-approved for use in your org.</li><li>**Any** are agents from any of the listed creator types.</li></ul>  |
| Active users (licensed)   | The number of unique users in your org with a Microsoft 365 Copilot license who used the agent for the selected time period.  |
| Active users (unlicensed)  | The number of unique users in your org without a Microsoft 365 Copilot license who used the agent for the time period selected.   |
| Responses sent to users   | The total agent responses sent to all users during the selected period.  |
| Last activity date (UTC)  | The date when the agent was last used by anyone in your organization.  |

### Users and agent details table

| Item | Description |
| --- | --- |
| Agent ID | An agent is an element of an app. The ID is the app identifier generated by Microsoft.|
| Agent name | The name of the app as present in the app manifest.  |
| Creator type | Indicates who built the agent. The following list defines the values:<ul><li>**User** are agents created by individuals in your organization using tools like [agent builder](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder). These agents aren't listed in the organization-wide catalog, but users can use the agents for themselves, or share agents via a link with others in the same organization.</li><li>**Your org** are agents created by individuals in your organization using tools like [Microsoft 365 Agents Toolkit](https://learn.microsoft.com/en-us/microsoft-365/developer/overview-m365-agents-toolkit), [Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and admin-approved for broader use across your org.<br> - **Microsoft** are agents built by Microsoft.</li><li>**Microsoft partner** are agent built by Microsoft partners and admin-approved for use in your org.</li><li>**Any** are agents from any of the listed creator types.</li></ul>  |
| Username | The user's principal name.  |
| Responses sent to users   | The total agent responses sent to all users during the selected period.  |
| Last activity date (UTC)  | The date when the agent was last used by anyone in your organization.  |

## FAQ

### Why don't I see the Export button in the details table anymore?

The **Export** button is temporarily removed from tables in the **Details** section. The export functionality will be restored soon.

### What is the difference between the agent report and the Agent usage in Microsoft 365 Copilot and which should I use?  

The new Agent usage report gives a broader view than the one in Microsoft 365 Copilot. The [original report](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-agents) only includes agents built by your organization or users (using Agent Builder), and only for licensed Copilot users. The new report includes usage by both licensed and unlicensed users, and covers all agent creators, including Microsoft and Microsoft partners. It also includes line level details at the per-user, per-agent, and per-user and agent level. Over time, this new report replaces the current Agent usage report in Microsoft 365 Copilot.

### Why does this report only show the past 7 and 30 days, while other usage reports also show the past 90 and 180 days?

The agent report is in preview and doesn't yet include the past 90 and 180 days but will be added at a later date.

### What is "Last activity detected"?

Last activity detected shows the most recent date and timestamp (in UTC) when user activity generated agent usage.  

### Are agents created from Microsoft Copilot Studio and Teams Toolkit included?  

Yes. The following agents are the agents for which usage is reported:

- Agents created in Microsoft Copilot Studio by users in your organization and approved by an admin.
- Agents created in Teams Toolkit by users in your organization and approved by an admin.
- Agents created by users through [agent builder](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder) for users that have this feature enabled and shared with other users in your organization.

### Why is the total active user count less than the sum of licensed and unlicensed active users?

The sum of active users without a license and active users with a license might exceed the total active users if you assigned or removed licenses during the selected timeframe.

### How can I view the username or display name if it's hidden?

By default, the usage report anonymizes the username and display name. Global administrators can change settings to reveal or conceal these values.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

To learn how to change the setting to show the username and display name information, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

### Are SharePoint agents used in Teams included in the usage report?

No. SharePoint agents used in Teams aren't currently included in the usage metrics in the report. For more information, see [Share an agent from SharePoint in Teams - Microsoft Support](https://support.microsoft.com/office/share-an-agent-from-sharepoint-in-teams-6dcbf7b5-8c13-44e5-a68a-dbd71fb76ad3).

### Why is the total active users count smaller than the sum of unlicensed and licensed user counts for my organization?

You might see this discrepancy if a user's Microsoft 365 Copilot license changes during the selected time period. For example, the user might be assigned a Copilot license and later remove it within that same period.
