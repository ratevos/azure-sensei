# Microsoft 365 Copilot credits report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-credits  
> Microsoft doc last updated: 04/03/2026


The Microsoft 365 Copilot credits report helps you manage metered consumption costs for Microsoft 365 Copilot Chat. This report gives you visibility into credits used for your Microsoft 365 Copilot pay-as-you-go billing policies. It includes key metrics such as:

- Total credits used
- Cumulative and daily time series
- Credits used per user, per agent, per billing policy, and per agent-user pair

To learn more about meters, see [Meters for Microsoft 365 Copilot pay-as-you-go for IT admins](https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/meters).

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the Copilot credits report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **Microsoft 365 Copilot**, and then select **Credits**.

## Interpret the Copilot Credits report

After you [set up pay-as-you-go for Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/setup), either in the Microsoft 365 admin center or the <a href="https://go.microsoft.com/fwlink/p/?linkid=2160305" target="_blank">Power Platform admin center</a>, and enable agent usage in your organization, you see a new report that includes metrics for credits used.

To help you mitigate overspending, the report includes alerts when users in your organization use more than 2,000 credits. To learn more, see [Using agents in Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/copilot/agents) and the [overview on enabling agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management), which explains how agents are billed.  

You can filter the report by different time periods. You can view the Copilot credits report over the last 7 or 30 days.

>[!NOTE]
> During preview, the report displays a maximum of 30 days of Copilot credits history. In addition, usage information from before May 3, 2025, isn't available in the report.

### Credits used

The **Credits used** metric shows the [total credits used](https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing#billed-messages) from interactions by users in your organization who don't have a Microsoft 365 Copilot license and are interacting with agents in Copilot Chat that spin the [Copilot Studio meter](https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing#copilot-studio-pay-as-you-go-meter) during the selected time period. You can view usage within an hour from when users interact with a metered agent.  

The number of credits used depends on the design of the agent, how often users interact with it, and the features the agent uses. Each interaction with an agent might use multiple message types simultaneously. For example, an agent grounded in a tenant graph could use 12 credits (10 credits for tenant graph-grounding, and two credits for generative answers) to respond to a single complex prompt from a user.

### Alerts

The **Alert** card is visible in the report when one or more users consume more than 3,000 credits in the past 30 days.

Select **View Copilot credits details** to see the user list and export it to CSV. If users consume 2,000 to 3,000 credits, a similar alert appears.

>[!NOTE]
> For preview, the alerts remain visible in the report for up to seven days and disappear after if there are no new users who crossed the threshold.  

## Copilot credits usage report details

Use the Microsoft 365 Copilot Credits usage report to view user details, agent details, and user and agent details.

### Users

| Item                    | Description            |
|-------------------------|------------------------|
| Username                | The user's principal name. |
| Display name            | The full name of the user. |
| Past seven days         | The total credits used over the past seven days, including today. |
| Past 30 days            | The total credits used over the past 30 days, including today. |
| Last activity date (UTC)| The latest date the user had activity with a metered agent in Copilot chat. |

### Agents

| Item                    | Description      |
|-------------------------|------------------|
| Agent ID                | An agent is an element of an app. The ID is the app identifier generated by Microsoft. |
| Agent name              | The name of the app as present in the app manifest. |
| Past seven days         | The total credits used by users who used the agent over the past seven days, including today. |
| Past 30 days            | The total credits used by users who used this agent over the past 30 days including today. |
| Last activity date (UTC)| The date when the agent was last used by users in your org who don't have Microsoft 365 Copilot license. |

### Billing policies

| Item                    | Description          |
|-------------------------|----------------------|
| Billing Policy ID       | The ID is a Microsoft-generated identifier linked to the billing policy that you created for specific users in a security group. |
| Past seven days         | The total credits used by members of the security group linked to the billing policy over the past seven days, including today. |
| Past 30 days            | The total credits used by members of the security group linked to the billing policy over the past 30 days, including today. |
| Last activity date (UTC)| The most recent date on which a member of the security group linked to the billing policy consumed credits. |

### Users and agents

| Item                    | Description     |
|-------------------------|-----------------|
| Agent ID                | An agent is an element of an app. The ID is the app identifier generated by Microsoft. |
| Agent name              | The name of the app as present in the app manifest. |
| Username                | The user's principal name. |
| Billing Policy ID       | The ID is a Microsoft-generated identifier linked to the billing policy that you created for specific users in a security group. |
| Past seven days         | The total credits used by the user who used this agent over the past seven days, including today. |
| Past 30 days            | The total credits used by the user who used this agent over the past 30 days, including today. |
| Last activity date (UTC)| The date when the agent was last used by users in your org who don't have Microsoft 365 Copilot license. |

> [!NOTE]
> The report shows data up to today, but it doesn't automatically update if there's recent usage. To view the latest data, manually refresh the report.

## FAQ

### Will I see consumption in this report if I configured the billing policy in the Power Platform admin center?  

Yes. You can set up the pay-as-you-go billing policy in the Microsoft 365 admin center or Power Platform admin center. If you configure pay-as-you-go, and users without a Microsoft 365 Copilot license use metered agents in Copilot Chat, the data appears in the report.

### What is "Last activity detected?"

**Last activity detected** is the date and timestamp of the most recent prompt or user activity that generated the credits consumed.

### How can I test that pay-as-you-go is correctly configured and working properly?

Have a user who qualifies for pay-as-you-go use one of the following three agents: "Learning Coach", "Writing Coach", or "Career Coach." Have them submit a simple prompt such as "What can you do?" This prompt consumes about 12 credits and is visible in the Copilot Credits Report.

### How do I find a Billing policy name from the Billing policy ID?

1. In the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>, go to **Copilot** > **Billing & usage**.
1. On the **Billing policies** tab, select a billing policy, and then select **Details**. You see the **Policy name** and **Billing Policy ID**.  

### How can I view the billing policy ID if it's hidden?  

By default, the Copilot credits report anonymizes the Billing Policy ID, just like the username and display name. Global administrators can change the settings to show or hide the Billing Policy ID.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

To learn how to change the setting to show the Username and Display name information, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

> [!NOTE]
> Changes to this hidden data setting affect the username, display name, and Billing Policy ID.
