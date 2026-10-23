# Mailbox usage report - Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/mailbox-usage  
> Microsoft doc last updated: 04/03/2026


The Mailbox usage report provides information about users with a user mailbox and the level of activity by each user, based on the email send, read, create appointment, send meeting, accept meeting, decline meeting, and cancel meeting activity. It also provides information about how much storage each user mailbox consumes, and how many of them are approaching storage quotas. The mailbox usage report also contains information about mailboxes shared among users, providing storage and quota data on shared mailboxes.

For general information about Microsoft 365 Usage reports and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

## View the Mailbox usage report

For information about the roles needed to view usage reports, see [Microsoft 365 admin center usage reports overview](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports).

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.
1. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
1. Select <a href="https://go.microsoft.com/fwlink/p/?linkid=2074756" target="_blank">Usage</a>.
1. On the **Usage** page, under **Reports**, select **Exchange**.
1. On the report page, select the **Email activity** tab.
1. Under **Email activity**, select **View More**. 
1. From the **Email activity** drop-down list, select **Exchange** \> **Mailbox usage**.

## Interpret the Mailbox usage report

You can view your organization's mailbox usage by looking at the **Mailbox**, **Storage**, and **Quota** charts.

To access shared mailbox information, change the drop-down selection at the top right of the charts to **Shared**. If your tenant doesn't have shared mailboxes, you can't view any shared mailbox information.

> [!NOTE]
> You can't currently export the summary chart information for shared mailboxes. This known issue will be corrected in a future update.
  

You can view the Mailbox usage report for trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date (not the date the report generated). The data in each report usually covers up to the last 24 to 48 hours.

### The Mailbox chart

The **Mailbox** chart shows you the total number of user or shared mailboxes in your organization, and the total number of user mailboxes that are active on any given day of the reporting period. A user mailbox is active if it had an email activity that included at least one of the following actions:

- Send
- Read
- Create appointment
- Send meeting
- Accept meeting
- Decline meeting
- Cancel meeting activity

> [!NOTE]
> Shared mailboxes don't have activity independent of a user mailbox, so the report shows only a count of shared mailboxes when you select this mailbox type.

On the **Mailbox** chart:

- The Y axis is the number of user or shared mailboxes. 
- The X axis is the selected date range for this specific report.

### The Storage chart

The **Storage** chart shows you the amount of storage used in your organization by mailbox type. The **Storage** chart doesn't include archive mailboxes. For more information about auto-expanding archiving, see [Overview of auto-expanding archiving in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/compliance/autoexpanding-archiving).

On the **Storage** chart:

- The Y axis is the amount of storage used by user or shared mailboxes in your organization.
- The X axis is the selected date range for this specific report.

### The Quota chart

The **Quota** chart shows the number of user or shared mailboxes in each quota category. There are four quota categories:

- **Good**: The number of users or shared mailboxes whose storage used is below the "issue warning" quota.
- **Warning**: The number of users or shared mailboxes whose storage used is at or above the "issue warning" quota, but below the "prohibit send" quota.
- **Can't send**: The number of users or shared mailboxes whose storage used is at or above the "prohibit send" quota, but below the "prohibit send/receive" quota.
- **Can't send/receive**: The number of users or shared mailboxes whose storage used is at or above the "prohibit send/receive" quota.

On the **Quota** chart:

- The Y axis is the number of user or shared mailboxes in each storage quota.
- The X axis is the quota category.

Filter the charts you see by selecting an item in the legend.

### Mailbox usage per mailbox table

This table shows a breakdown of mailbox usage at the per mailbox level. You can add extra columns to the table. 

|Item|Description|
|:-----|:-----|
|Recipient type |Either Shared or User. |
|User name |The email address of the user. |
|Display Name  |The full name of the user. |
|Deleted |The mailbox whose current state is deleted, but was active during some part of the reporting period of the report.|
|Deleted date |The date the mailbox was deleted. |
|Create date | The date the mailbox was created.  |
|Last activity date | The date the mailbox last had an email send or read activity.   |
|Item count|The total number of items in the mailbox. |
|Storage used (MB)|The total storage used. |
|Deleted Item Count|The total number of recoverable items in the mailbox. |
|Deleted Item Size (MB)|The total size of all recoverable items in the mailbox. |
|Issue warning quota (MB)|The storage limit when the mailbox owner receives a warning that it's about to hit the storage quota.  |
|Prohibit send quota (MB)|The storage limit when the mailbox can no longer send emails. |
|Prohibit send receive quota (MB)|The storage limit when the mailbox can no longer send or receive emails. |
|Recoverable Item Quota (MB)|The storage limit for recoverable (deleted) items in the mailbox when the mailbox can no longer delete emails. |
|Report Period| The period for which the report is available.|
|Has Archive|Shows if the mailbox has an online archive enabled. |

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).

To learn more about the recoverable items folder, see [Recoverable Items folder in Exchange Online](https://learn.microsoft.com/en-us/exchange/security-and-compliance/recoverable-items-folder/recoverable-items-folder#recoverable-items-mailbox-quotas).

Select **Choose columns** to add or remove columns from the report.

To export the report data into an Excel .csv file, select the **Export** link.
