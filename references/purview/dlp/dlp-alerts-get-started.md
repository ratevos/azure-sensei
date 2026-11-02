# Get started with data loss prevention alerts

> Source: https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started  
> Microsoft doc last updated: 2026-06-26


Your Microsoft Purview Data Loss Prevention (DLP) policies can be configured to generate alerts when the conditions in a rule are matched. Alerts are configured in DLP policy rules.

For a brief overview of alerts see:

- [DLP Alerts](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#dlp-alerts)
- [Incident reports](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#incident-reports)

This article includes the licensing and permission details and other crucial information you need as you work with alerts.

DLP alerts can be investigated and managed in the [Microsoft Defender XDR dashboard](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender) and in the [Microsoft Purview portal](https://purview.microsoft.com). The Microsoft Defender XDR dashboard is the recommended location for investigating and managing DLP alerts. The Microsoft Purview portal is the recommended location for creating and editing DLP policies.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Types of DLP alerts

Alerts can be sent every time an activity matches a rule or they can be aggregated to cut down on the noise. There are two types of alerts that can be configured in DLP policies.

**Single-event alerts** Single-event alerts are typically used in policies that monitor for highly sensitive events that occur in a low volume, like a single email with 10 or more customer credit card numbers being sent outside your organization. By default when events from a single rule occur in a one minute window of each other they are aggregated for E5 license and 15 mins for E3 license. In preview, single-event alerts can be aggregated on per rule per user basis. This is called user and rule-based alert aggregation.

**Aggregate-event alerts** are typically used in policies that monitor for events that occur in a higher volume over a period of time. For example, an aggregate alert can be triggered when 10 individual emails each with one customer credit card number is sent outside your org over 48 hours.

## Before you begin

Before you begin, make sure you have these prerequisites:

### Licensing for alert configuration options

The following licensing requirements apply to each alert configuration option:

- **Single-event alert configuration**: All organizations with a DLP subscription (E1, E3, E5, F1, G1, E3, G3, E5, G5) can configure policies to generate an alert for every time a triggering activity occurs.
- **Aggregated alert configuration**: To configure aggregate alert policies based on a threshold, you must have either of the following configurations:
    - An A5 subscription
    - An E5 or G5 subscription
    - An E1, F1, or G1 subscription or an E3 or G3 subscription that includes one of the following features:
        - Office 365 Advanced Threat Protection Plan 2
        - Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance)
        - Microsoft 365 eDiscovery and Audit add-on license

Customers who use [endpoint DLP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about) and who are eligible for [Teams DLP](https://learn.microsoft.com/en-us/purview/dlp-microsoft-teams) will see their endpoint DLP policy alerts and Teams DLP policy alerts in the DLP alert management dashboard.

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

To learn more about these role groups, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions)

Here's a list of applicable role groups. To learn more about these role groups, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators

To access the DLP alert management dashboard, you need the *Manage alerts* role and either of these two roles:

- DLP Compliance Management
- View-Only DLP Compliance Management

To access the Content preview feature and the Matched sensitive content and context features, you must be a member of the *Content Explorer Content Viewer* role group, which has the *Data classification content viewer* role preassigned.

Tip

If the admin requires access to alerts but not contextual/sensitive information, you can create and assign a custom role that does not include Data Classification Content Viewer permission.

## Configure DLP alerts

To learn how to configure an alert in your DLP policy, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy). There are different alert configuration experiences depending on your licensing.

Note

It may take up to 3 hours to generate alerts after you configure or modify existing alerts in a DLP policy.

An Alert email, Incident Report email, and User Notification will only be sent once per document. If a document with a **Content is Shared** condition is shared twice, there will still be only one notification.

### Aggregate event alert configuration

If you're licensed for aggregated alert configuration options, then you'll see options to generate alerts for each rule match, when thresholds are met, and within a defined time window when you create or edit a DLP policy.



This configuration allows you to set up a policy to generate an alert:

- every time an activity matches the conditions in a rule for default aggregation based on a rule or of user and rule based aggregation.
- when the defined threshold is met or exceeded based on the number of matches or the volume of or on the volume of exfiltrated data
- for activities that meet the criteria that you define within a speficied time window

### Single event alert configuration

If you're licensed for single-event alert configuration options, then you'll see the single-event alert settings when you create or edit a DLP policy. Use this option to create an alert that's raised every time a DLP rule match happens.



### User and rule based alert aggregation (preview)

When you enable user based alert aggration in DLP setting at the tenant level, single event alerts are aggregated based on users. The rule match events must occur within the configurable time window (15, 30, 45 and 60 minutes). Alerts are generated per rule match event per user.

### Compare alert aggregation options

| I want DLP to... | Time window | Aggregation type | Notes |
| --- | --- | --- | --- |
| ...generate single alert when an email containing credit card information is sent by any number of users. | These windows *are not* configurable by the admin-E5: 60 seconds-E3: 15 minutes | - User based alert aggregation is set to **Off** at the tenant level.- Single event alert aggregation configured at the rule level and is available if match occurs within time window. -Aggregate DLP rule matches of multiple users into one alert. | - Applies to multiple users for one rule. |
| ...generate one alert for each email sender when an email containing credit card information is sent out. | This time window *is configurable* by the admin at the tenant level.- 15 - 60 minutes | - User based alert aggregation is set to **On** at the tenant level. - Single event alert aggregation configured at the rule level.-Aggregate DLP rule matches by single user into one alert. | - For single user per rule. - Expect an increase in alert volume. - If the alert is closed within the aggregation time window and a new match occurs for the same user and rule, then the new rule match will be aggregated into the same alert. |
| ...to generate an alert when more than 100 sensitive files are accessed by multiple users within 60 minutes. | - Configured at the rule level, 60-999 minutes. | - Threshold based aggregation - Aggregate DLP rule matches based on count of matches. - User based alert aggregation not applicable. | - pivots on rules - Use this for multiple users for one rule. - Only works for the **All users** option. |
| ...to generate an alert when more than 25 MB data is exfiltrated by multiple users within 60 minutes. | Configured at the rule level, 60-999 minutes. | -Threshold based aggregateon based on the volume of data.- user based alert aggregation not applicable. | - pivots on rules - Use this for multiple users for one rule. - Only works for the **All users** option. |

## Types of DLP alert events

Here are some of the events associated with an alert. In the Alert dashboard, you can choose a particular event to view its details.

### Review event details

The following table describes the event details shown for alert events.

| Property name | Description | Event types |
| --- | --- | --- |
| ID | unique ID associated with the event | all events |
| Location | workload where the event was detected | all events |
| time of activity | time of the user activity that matched the criteria of the DLP policy |  |

### Review affected entities in an alert

The following table lists the entities that can be associated with a DLP alert event.

| Property name | Description | Event types |
| --- | --- | --- |
| user | user who took the action that caused the policy match | all events |
| hostname | host name of the computer where the DLP policy match occurred | device events |
| IP address | IP address of the computer where the DLP policy match occurred | device events |
| sha1 | SHA-1 hash of the file | device events |
| sha256 | SHA-256 hash of the file | device events |
| MDATP device ID | endpoint device MDATP ID |  |
| file size | size of the file | SharePoint, OneDrive, and device events |
| file path | the absolute path of the item involved with the DLP policy match | SharePoint, OneDrive, and devices events |
| email recipients | if an email was the sensitive item that matched the DLP policy, this field includes the recipients of that email | Exchange events |
| email subject | subject of the email that matched the DLP policy | Exchange events |
| email attachments | names of the attachments in the email that matched the DLP policy | Exchange events |
| site owner | name of the site owner | SharePoint and OneDrive events |
| site URL | full of the URL of the SharePoint or OneDrive site where the DLP policy match occurred | SharePoint and OneDrive events |
| file created | time of creation of the file that matched the DLP policy | SharePoint and OneDrive events |
| file last modified | the last time that the file that matched the DLP policy was changed | SharePoint and OneDrive events |
| file size | size of the file that matched the DLP policy | SharePoint and OneDrive events |
| file owner | owner of the file that matched the DLP policy | SharePoint and OneDrive events |

### Review policy details for an alert

The following table describes the policy-related details available for alert events.

| Property name | Description | Event types |
| --- | --- | --- |
| DLP policy matched | name of the matched DLP policy | all events |
| rule matched | name of the matched DLP policy rule | all events |
| sensitive information types (SIT) detected | SITs that were detected as part of the DLP policy match | all events |
| actions taken | actions that were taken that caused the DLP policy match | all events |
| violating action | action on the endpoint device that raised the DLP alert | device events |
| user overrode policy | did the user override the policy via a policy tip | all events |
| use override justification | the text of the reason provided by the user for the override | all events |

Important

Your organization's audit log retention policy configuration controls for how long an alert remains visible in the console. For more information, see [Manage audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies#manage-audit-log-retention-policies).
