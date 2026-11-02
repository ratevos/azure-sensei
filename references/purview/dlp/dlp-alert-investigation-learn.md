# Learn about investigating data loss prevention alerts

> Source: https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn  
> Microsoft doc last updated: 2025-10-15


This article introduces you to the alert investigation flow and the tools you can use to investigate DLP alerts.

## Before you begin

1. [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units)
2. [Learn about Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
3. [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#plan-for-data-loss-prevention-dlp)- by working through this article you will:
    1. [Identify stakeholders](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#identify-stakeholders)
    2. [Describe the categories of sensitive information to protect](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#describe-the-categories-of-sensitive-information-to-protect)
    3. [Set goals and strategy](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#set-goals-and-strategy)
4. [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview)
5. [Collection policy reference](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference)
6. [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference) - this article introduces all the components of a DLP policy and how each one influences the behavior of a policy
7. [Design a DLP policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) - this article walks you through creating a policy intent statement and mapping it to a specific policy configuration.
8. [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) - This article presents some common policy intent scenarios that you map to configuration options, then it walks you through configuring those options.
9. [Learn about investigating data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn) - This article introduces you to the lifecycle of alerts from creation, through final remediation and policy tuning. It also introduces you to the tools you use to investigate alerts.

## The lifecycle of a DLP alert

All alerts and your interaction with them go through these six steps:

- Trigger
- Notify
- Triage
- Investigate
- Remediate
- Tune

### Trigger

The life of a Microsoft Purview Data Loss Prevention (DLP) alert starts when the [conditions defined in the policy are matched](https://learn.microsoft.com/en-us/purview/dlp-policy-design). When a policy match occurs, the actions defined in the policy are triggered, which can include generating an alert [if the policy is configured](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) to do so.

DLP policies are typically configured to monitor for and generate alerts when:

- Sensitive information, such as personally identifying data or intellectual property, is exfiltrated from your organization.
- Sensitive information is shared inappropriately with people outside or inside your organization.
- Users engage in risky activities, such as downloading sensitive information to removable media.

### Notify

When an alert is generated, it's sent to the [Microsoft Defender portal](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender) as an incident and the [DLP alert management dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started). DLP policies can be configured to send notifications to users, administrators, and other stakeholders via email.

In the notify phase Microsoft Purview:

- Reports on DLP policy matches and user overrides.
- You can use [Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) to view DLP related activities and filter for report generation purposes.

To export activity data for reporting use Export-ActivityExplorerData (ExchangePowerShell) | Microsoft Doc by using O365 Management Activity API or Incident API.

Note

The Microsoft Defender portal retains incidents for six months. The DLP alert management dashboard retains alerts for 30 days.

### Triage

In this step, you analyze an alert and any associated logs and decide if the alert is a true positive or a false positive. If it's a true positive, you set the priority of the alert based on the severity of the issue and its impact on your organization and assign an owner. If it's a false positive, you can unblock the user and move on to the next alert.

Defender portal groups DLP events into incidents. Incidents are a collection of related alerts that are grouped together based on all the other signals that Defender is receiving. For example, when you have a DLP policy configured to monitor and alert on sensitive files on SharePoint sites, and a user downloads a file from a SharePoint site and then uploads it to a personal OneDrive, and then shares it with an external user, Defender groups all of those alerts into a single incident. This is a powerful feature that allows you to focus on the most important alerts first.

In the Defender portal you can immediately start triaging incidents and use tags, comments, and other features to structure your incident management. You should be utilizing the Incidents page in the Microsoft Defender portal to manage your DLP alerts. You can filter the Incidents queue to view all incidents with Microsoft Purview DLP alerts by selecting **Filters** and choose **Service Source: Data Loss Prevention**.

If you have enabled [sharing of insider risk management data with Microsoft Defender XDR](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) - you'll see the severity level of the Insider Risk Management policy that is associated with a user in the DLP alerts page. Insider Risk Management severity levels are: **Low**, **Medium**, **High**, and **None**. You can use this information to prioritize your investigation and remediation efforts. This information will also be available in the Microsoft 365 Defender portal in the details of the incident.

#### Triage with Microsoft Security Copilot

Another tool you can use to help triage alerts it [Microsoft Security Copilot](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview). Security Copilot is a cloud-based AI platform that can assist security and compliance professionals in protecting their organization's data. It is available in the [DLP Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started#investigate-a-dlp-alert) and in [Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management-copilot).

#### Triage with Microsoft Security Copilot DLP Alert Triage Agent

Microsoft Security Copilot for Purview supports the [Data Security Triage Agent for DLP](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview). Microsoft Security Copilot agents are AI powered processes that are designed to help you with specific role based tasks.

### Investigate

The main goal of the investigation stage is for the assigned owner to correlate evidence, determine the cause and full impact of the alert and decide on a remediation plan. The assigned owner is responsible for deeper investigation and remediation of the alert. The primary alert investigation tools are the [Microsoft Defender portal](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender) and the [DLP alert management dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started). You might also use [Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) to investigate alerts. You can also [share alert events](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started#create-a-shareable-link-to-an-alert-event) with other users in your organization.

You can take advantage of DLP features like:

- [Evidence collection for file activities on devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-learn) makes files like email and documents that matched a policy easily accessible.
- Use [Content explorer](https://learn.microsoft.com/en-us/purview/data-classification-content-explorer) to deeply investigate the content in the incident.

You can use both Microsoft Defender portal and Purview tools to triage and investigate alerts, but the Microsoft Defender portal provides more capabilities for managing alerts and incidents, such as:

- View all your DLP alerts grouped under incidents in the Microsoft Defender XDR incident queue.
- View intelligent inter-solution (DLP-MDE, DLP-MDO) and intra-solution (DLP-DLP) correlated alerts under a single incident.
- Hunt for compliance logs along with security under Advanced Hunting.
- In-place admin remediation actions on user, file, and device.
- Associate custom tags to DLP incidents and filter by them.
- Filter by DLP policy name, tag, Date, service source, incident status, and user on the unified incident queue.

If you're sharing [insider risk management data with Defender](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data), you can see the **User activity summary** of all the exfiltration activities the user has engaged in up to the past 120 days.

### Remediate

Your remediation plan is unique to your organization's policies, the industry, the geopolitical regulations it must comply with, and business practices. How your organization chooses to respond to an alert revolves around the accuracy of the alert (true positive, false positive, false negative), the severity of the issue, and the impact on your organization.

Remediation actions can include:

- Monitor only, no further action required.
- No further action required because the actions take by the policy sufficiently mitigated the risk.
- Risk mitigated by automated policy actions but user education is necessary.
- The issue wasn't fully mitigated by the policy, so further clean up and risk mitigation is required along with more user training.
- Via [Adaptive Protection in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn) where DLP integrates with Insider Risk Management, you can assign a risk level to the user for further monitoring and actions.

With the Defender portal, you can immediately take remediation actions on alerts and incidents. For example:

- Reset password
- Disable account
- View user activity
- Actions on DLP detections
- Remove document
- Apply sensitivity label
- Unshare
- Download email
- [Advanced Hunting](https://learn.microsoft.com/en-us/en-us/defender-xdr/advanced-hunting-overview)
- Isolate Device
- Collect investigation pack from Device
- Run AV Scan
- Quarantine file
- Disable user
- Reset pwd
- Delete email
- Move mail to other mailbox folder
- Download file

### Tune

Based on the accuracy and effectiveness of your policy, you might need to update it so it remains effective. You've already tuned your policy during the [policy creation and deployment process](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy), but as your data estate and business needs change, policies have to be updated to continue to be effective. These changes are best tracked in the [policy intent statement](https://learn.microsoft.com/en-us/purview/dlp-policy-design#define-intent-for-the-policy) and the [policy configuration](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy).

Items you tune:

- The scope of the policy.
- The conditions required for a policy match.
- The actions taken when a policy match occurs.
- Notifications sent to users and administrators.

For more information about mapping business needs to policy design and testing policies, see:

- [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy)
- [Test your Data Loss Prevention policies](https://learn.microsoft.com/en-us/purview/dlp-test-dlp-policies)

## Toolsets

There are multiple tools that you can use to investigate and manage Microsoft Purview Data Loss Prevention (DLP) alerts. There are:

- [Microsoft Defender portal](https://go.microsoft.com/fwlink/p/?linkid=2077139)
- [Microsoft Purview portal Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started)
- [Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer)
- [Content explorer](https://learn.microsoft.com/en-us/purview/data-classification-content-explorer)
- [Key features in the embedded experience](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview#key-features-in-the-embedded-experience)
- [Key features in the standalone experience](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview#key-features-in-the-standalone-experience)
- [Data Security Posture Management](https://learn.microsoft.com/en-us/purview/data-security-posture-management)

Microsoft recommends using the unified incident queue in Microsoft Defender portal to manage your DLP alerts. However, your organization may have needs that can be met by using the DLP alert management dashboard in addition to the Microsoft Defender portal.

### Microsoft Defender portal

- DLP alerts are integrated with other events and alerts into a single incident queue, which provides a more complete picture of the incident.
- Six months of incident history is available.
- [Advanced hunting](https://learn.microsoft.com/en-us/en-us/defender-xdr/advanced-hunting-overview) is available.
- [Investigate data loss incidents with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender) - You can manage DLP incidents along with security incidents from **Incidents & alerts** &gt; **Incidents** on the quick launch of the Microsoft Defender portal.
- [Responding to your first incident in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/respond-first-incident-365-defender)
- [Incident response with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/incidents-overview)
- [Prioritize incidents in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/incident-queue)
- [Manage incidents in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/manage-incidents)
- [Investigate incidents in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/investigate-incidents)
- [Investigate alerts in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/investigate-alerts)
- [Proactively hunt for threats with advanced hunting in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/advanced-hunting-overview)

### Microsoft Purview portal

- Alerts dashboard, Activity explorer, and Content explorer are all available in the Microsoft Purview portal. You can summarize alerts using Microsoft Security Copilot [Investigate a DLP alert](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started#investigate-a-dlp-alert)
- You can set an alert status to **Investigating**.
- You can [share alert events](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started#create-a-shareable-link-to-an-alert-event) with other users in your organization.
- Download files from OneDrive and SharePoint ([data classification content viewer role](https://learn.microsoft.com/en-us/en-us/microsoft-365/security/office-365-security/scc-permissions#role-groups-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance) is required for this action)

If you're new to using the DLP Alerts dashboard, you should read through these articles to help you get started.

- [Get started with the data loss prevention Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started#get-started-with-the-data-loss-prevention-alerts-dashboard)
- [Share data loss prevention alert events](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started#create-a-shareable-link-to-an-alert-event)
- [Get started with data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)
- [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#get-started-with-activity-explorer)
- [Get started with content explorer](https://learn.microsoft.com/en-us/purview/data-classification-content-explorer)
