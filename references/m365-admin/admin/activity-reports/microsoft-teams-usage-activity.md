# Microsoft Teams usage report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-teams-usage-activity  
> Microsoft doc last updated: 04/03/2026


The Microsoft Teams usage report provides an overview of the usage activity in Teams, including the number of active users, channels, and messages. You can quickly see how many users across your organization are using Teams to communicate and collaborate. The report also includes other Teams-specific activities, like the number of active guests, meetings, and messages.

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the Microsoft Teams usage report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **Microsoft Teams**.
1. On the report page, select the **Team usage** tab.

## Interpret the Team usage report

Use the Team usage report to view channel and team usage, including data about individual teams. The **Team usage** tab displays the following charts:

- **Channel usage**: Tracks the number of channel uses, by activity type, over time.

  
  
- **Team usage**: Tracks the number of teams, by type and activity, over time.

  
  
Additionally, the chart includes usage details for individual teams, such as last activity date, active users, active channels, and other data.

In the table, select **Choose columns** to add or remove columns from the report.

Select the **Export** link to export the report data into an Excel .csv file. This action exports data for all users and enables you to do simple sorting and filtering for further analysis. The exported format for **audio time**, **video time**, and **screen share time** follows ISO8601 duration format.

You can view the **Microsoft Teams usage activity** report for trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date (not the date the report was generated).

> [!NOTE]
> Activity dates in this report are based on Coordinated Universal Time (UTC). Post counts attributed to a given day reflect messages sent between 12:00 AM and 11:59 PM UTC, which might differ from your organization's local time zone.

To ensure data quality, the system performs daily data validation checks for the past three days and fills any detected gaps. You might notice differences in historical data during the process.

> [!Important]
> Data for a given day appears within 48 hours. For example, data for January 10th appears in the report by January 12th.

### Channel usage metrics

The Channel usage chart shows data about the following metrics.

|Metric |Definition |
|:-----|:-----|
|Active channel users |This metric is the total of internal active users, active guests, and external active users.  <br/><br/> **Internal active users** - Users that have at least one panel action in the specified time period. This metric excludes guests.   <br/> **Active guests** - Guests that have at least one panel action in the specified time period. A guest is a person from outside your organization who accesses shared resources by signing in to a guest account in my directory.  <br/> **External active user** - External participants that have at least one panel action in the specified time period. An external participant is a person from outside your organization who is participating in a resource – such as a shared channel – using their own identity and not a guest account in your directory.|
|Active channels|Valid channels in active teams that have at least one active user in the specified time period. This metric includes public, private, or shared channels.|
|Channel messages|The number of unique messages that the user posted in a private chat during the specified time period.|

> [!NOTE]
> Panel action refers to any action taken by the user in the panel within Microsoft Teams.

### Team usage metrics

The Teams usage chart shows data on the following metrics.

|Metric |Definition|
|:-----|:-----|
|Private teams|A private team that is either active or inactive.|
|Public teams|A public team that is either active or inactive.|
|Active private teams|A team that is private and active.|
|Active public teams|A team that is public and active.|

### Teams details

You can view data for the following metrics for individual teams.

|Metric|Definition|
|:-----|:-----|
|Team ID|Team identifier|
|Internal active users|Users that have at least one panel action in the specified time period, including guests. <br/> <br/> Internal users and guests that reside in the same tenant. Internal users exclude guests.|
|Active guests|Guests that have at least one panel action in the specified time period. <br/> <br/> A guest is defined as persons from outside your organization who access shared resources by signing in to a guest account in my directory.|
|External active users|External participants that have at least one panel action in the specified time period.<br/><br/> An external participant is defined as a person from outside your organization who is participating in a resource – such as a shared channel – using their own identity and not a guest account in your directory.|
|Active channels|Valid channels in active teams that have at least one active user in the specified time period. This metric includes public, private, or shared channels.|
|Active shared channels|Valid shared channels in active teams that have at least one active user in the specified time. <br/><br/>A shared channel is defined as a Teams channel that you can share with people outside the team. These people can be inside your organization or from other Microsoft Entra organizations.<br/><br/>**NOTE:** For shared channels that include external users, the report might undercount the number of active shared channels due to current telemetry limitations. |
|Total organized meetings |The sum of one-time scheduled, recurring, ad hoc, and unclassified meetings a user organized during the specified time period.|
|Posts|Count of all the post messages originally created in a channel during the specified time period. Cross-posted messages are counted only in the channel where they were originally created and aren't included in the post count of channels that received the cross-post.|
|Replies|Count of all the reply messages in channels in the specified time period.|
|Mentions|Count of all mentions made in the specified time period.|
|Reactions|Number of reactions an active user made in the specified time period.|
|Urgent messages|Count of urgent messages in the specified time period.|
|Channel messages|The number of unique messages that the user posted in a team chat during the specified time period.|
|Last activity date|The latest date that any member of the team committed an action.|

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

> [!NOTE]
> Metric counts include Teams client built-in features, but don't include changes to chat and channel through service integration, such as Teams app posts or replies and emails in the channel.

## Related content

[Microsoft Teams device usage report](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-teams-device-usage-preview) (article)\
[Microsoft Teams user activity report](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-teams-user-activity-preview) (article)
