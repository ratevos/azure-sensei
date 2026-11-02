# Get started with the DLP Alerts dashboard

> Source: https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started  
> Microsoft doc last updated: 2026-06-26


Microsoft Purview Data Loss Prevention (DLP) policies can take protective actions to prevent unintentional sharing of sensitive items. You can be notified when an action is taken on a sensitive item by configuring alerts for DLP.

You use the [DLP alert management dashboard](https://purview.microsoft.com/datalossprevention?viewid=dlpalerts) in the [Microsoft Purview portal](https://purview.microsoft.com) to view alerts, events, and associated metadata for DLP policy violations.

If you're new to DLP alerts, you should review [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

[Microsoft Purview portal](https://purview.microsoft.com) shows alerts for DLP policies that are enforced on the following workloads:

- Exchange email
- SharePoint sites
- OneDrive accounts
- Teams chat and channel messages
- Devices
- Instances
- On-premises repositories
- Fabric and Power BI

## Prerequisites and permissions

Make sure you have the necessary prerequisites:

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Roles and Role Groups

If you want to view the DLP alert management dashboard or to edit the alert configuration options in a DLP policy, you must be a member of one of these role groups:

- Compliance Administrator
- Compliance Data Administrator
- Security Administrator
- Security Operator
- Security Reader
- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator

To learn more about these role groups, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

Here's a list of applicable role groups:

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators

To access the DLP alert management dashboard, you need the *Manage alerts* role and either of these two roles:

- DLP Compliance Management
- View-Only DLP Compliance Management

To access the Content preview feature and the Matched sensitive content and context features, you must be a member of the *Content Explorer Content Viewer* role group, which has the *Data classification content viewer* role preassigned.

## Configure DLP alerts

To learn how to configure an alert in your DLP policy, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy).

Important

Your organization's audit log retention policy configuration controls how long an alert remains visible in the console. See [Manage audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies#manage-audit-log-retention-policies) for more information.

## Investigate a DLP alert

There are three tools you can use to investigate DLP alerts in the DLP Alerts dashboard:

- The **DLP Alerts** dashboard in standard view
- The **DLP Alerts** dashboard in Alert Triage Agent (Preview)
- [Microsoft Security Copilot](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview)

### Standard view

To investigate an alert using the standard DLP Alerts dashboard view, follow these steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention**.
2. Select **Alerts** to view the **DLP Alerts** dashboard.
3. Use the **Filter** fields to refine the list of alerts.
4. Choose **Customize columns** to list the properties you want to see.
5. To sort the results in ascending or descending order, double-click the column header.
6. Double-click an alert for more information about it.
7. The **Details** tab opens by default and provides high-level information about the alert.
8. Select **Summarize with Copilot**. This causes the Microsoft Security Copilot to generate a summary of the alert. The alert summary will contain the:
    - alert severity
    - alert title
    - the name of the policy that was matched
    - the name of the file involved and a link to the file
    - alert status
    - the email address of the user who performed the action that matched the policy
9. Select the ellipsis in the **Security Copilot**summary to:
    - copy the summary to the clipboard
    - regenerate the summary
    - open the alert in the Security Copilot standalone experience.
10. Select **View details** to open the **Overview** tab. The **Overview**tab provides a summary of the following information:
    - What happened
    - Who performed the actions that caused the policy match
    - Additional information about the policy match
11. The **Events** tab lists all of the events associated with the alert. Select any event in the list to get detailed information about the event. For each event, choose the **Actions** drop down for a list of actions you can take on the alert, such as verifying whether or not the alert has identified a true match or a false positive.
12. The **User activity summary** tab requires that [sharing be turned *On* in the **insider risk management** settings](https://learn.microsoft.com/en-us/en-us/purview/insider-risk-management-settings-share-data) Once enabled, the **User activity summary** tab provides all the exfiltration activities the user has engaged in (up to the past 120 days). Users [must be in scope of an insider risk management policy](https://learn.microsoft.com/en-us/en-us/purview/insider-risk-management-policies) to see the **User activity summary** tab.
13. After you investigate the alert, return to the **Overview** tab where you can **View details** to triage and manage the disposition of the alert, add comments and assign ownership of the alert. (To see the history of workflow management.)
14. After you take the required action for the alert, set the **Status** of the alert to **Resolved**.

### Alert Triage Agent

In preview, Microsoft Security Copilot in Purview supports [Security Copilot Agents (preview)](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview). The Alert Triage Agent helps reduce the time it takes to triage alerts by reasoning over the alerts and identifying the ones that pose the greatest risk to your organization.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** with appropriate permissions, see [DLP agent permissions and roles](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started#permissions-and-roles) for Data Loss Prevention workloads or [IRM agent permissions and roles](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started#permissions-and-roles) for Insider Risk Management workloads.
2. Select **Alerts** to view the **DLP Alerts** dashboard.
3. Set the Alerts page view toggle to **Alert Triage Agent**.
4. Choose the category (**All**, **Needs attention**, **Less urgent**, or **Not categorized**) to see the alerts that are relevant to your task.
5. Select the triaged alert to view the **Agent summary**, an **Overview**, and **Events** associated with the alert.

    Note

    If an alert contains multiple assets, the agent will summarize the top 10 assets that contributed to the summary of findings and the decision on which category to assign the alert to.
6. After you review the summary, you can select **Manage alert** to assign it to an analyst, change the status of the alert or add more comments.

### Security Copilot

Security Copilot is a cloud-based AI platform that can assist security and compliance professionals in protecting their organization's data. You can use it to summarize Microsoft Purview alerts, triage alerts and to drill down into your Microsoft Purview data. It is available in the [DLP Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started#investigate-a-dlp-alert) and in [Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-copilot).

## Create a shareable link to an alert event

Users with the appropriate permissions can view Microsoft Purview Data Loss Prevention (DLP) alerts in the DLP Alerts console. However, as alerts are triaged and investigated, you may want to share alert events with users who don't have access to DLP and the alerts console. You can create a shareable link to an alert event:

1. In the [Purview Portal](https://purview.microsoft.com), navigate to **Data Loss Prevention**, and then select **Alerts**.
2. Select an alert, and then select **View details**.
3. On the Alert details screen, select the **Events** tab just below the alert title to view the events contained in this alert.
4. Select the event you want to share, and then click the **Actions** button at the bottom of the screen to see the **Actions** menu.
5. Select Copy event link, and then select Copy to copy the shareable link to the event.
6. Now you can paste the link from your clipboard to share the link via chat, email, or other means.

### View other matched conditions in DLP events

Microsoft Purview supports showing matched conditions in a DLP event to reveal the exact cause for a flagged DLP policy. This information shows up in:

- DLP Alerts console
- [Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#get-started-with-activity-explorer)
- [Microsoft Defender for Business portal](https://learn.microsoft.com/en-us/en-us/defender-business/mdb-view-manage-incidents)

In the **Events** tab, open **Details** to see **Other matched conditions**.

#### Enhanced matched conditions for Exchange Online (preview)

For Exchange Online DLP events, matched conditions include enhanced detail for non-sensitive information type (SIT) conditions in addition to SIT matches. For the full list of supported condition categories and detail levels, see [Enhanced matched conditions for Exchange DLP events](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#enhanced-matched-conditions-for-exchange-dlp-events-preview).

#### Prerequisites

Make sure the following requirements are met before you use matched conditions on endpoints:

- Must be running Windows 10 x64 (build 1809 or later) or Windows 11.
    - See [March 21, 2023—KB5023773 (OS Builds 19042.2788, 19044.2788, and 19045.2788) Preview](https://support.microsoft.com/en-us/topic/march-21-2023-kb5023773-os-builds-19042-2788-19044-2788-and-19045-2788-preview-5850ac11-dd43-4550-89ec-9e63353fef23) for required minimum Windows Operating System builds.
- Matched conditions data is available for valid E3 and E5 license holders.
- Enable [Auditing](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable#turn-auditing-on-or-off).
- Enable [Advanced classification scanning and protection](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection).

Matched events information is supported for these conditions

| Condition | Exchange | Sharepoint | Teams | Endpoint |
| --- | --- | --- | --- | --- |
| Sender is | Yes | No | Yes | No |
| Sender domain is | Yes | No | Yes | No |
| Sender address contains words | Yes | No | No | No |
| Sender address matches patterns | Yes | No | No | No |
| Sender is a member of | Yes | No | No | No |
| Sender IP address is | Yes | No | No | No |
| Has sender overridden the policy tip | Yes | No | No | No |
| SenderAdAttribute Contains words | Yes | No | No | No |
| SenderAdAttribute Matches patterns | Yes | No | No | No |
| Recipient is | Yes | No | Yes | No |
| Recipient domain is | Yes | No | Yes | No |
| Recipient address contains words | Yes | No | No | No |
| Recipient address matches patterns | Yes | No | No | No |
| Recipient is a member of | Yes | No | No | No |
| RecipientAdAttribute Contains words | Yes | No | No | No |
| RecipientAdAttribute Matches patterns | Yes | No | No | No |
| Document is password protected | Yes | No | No | No |
| Document could not be scanned | Yes | No | No | No |
| Document did not complete scanning | Yes | No | No | No |
| Document name contains words | Yes | Yes | No | No |
| Document name matches patterns | Yes | No | No | No |
| Document property is | Yes | Yes | No | No |
| Document size over | Yes | Yes | No | No |
| Document content contains words | Yes | No | No | No |
| Document content matches patterns | Yes | No | No | No |
| Document type is | No | No | No | Yes |
| Document extension is | Yes | Yes | No | Yes |
| Content is shared from M365 | Yes | Yes | Yes | No |
| Content is received from | Yes | No | No | No |
| Content character set contains words | Yes | No | No | No |
| Subject contains words | Yes | No | No | No |
| Subject matches patterns | Yes | No | No | No |
| Subject or body contains words | Yes | No | No | No |
| Subject or body matches patterns | Yes | No | No | No |
| Header contains words | Yes | No | No | No |
| Header matches patterns | Yes | No | No | No |
| Message size over | Yes | No | No | No |
| Message type is | Yes | No | No | No |
| Message importance is | Yes | No | No | No |

## Limitation when downloading emails from within a DLP alert

In general, when using the DLP alert management dashboard, you can download specific emails from within an alert. However, emails that have been deleted in any of the following scenarios can't be downloaded.

| Sender | Recipient | Email Status |
| --- | --- | --- |
| Internal | External | Deleted by sender |
| External | Internal | Deleted by recipient |
| Internal | Internal | Deleted by both parties |
