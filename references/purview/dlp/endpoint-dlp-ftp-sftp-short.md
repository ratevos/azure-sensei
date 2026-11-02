# Protect FTP/SFTP Transfers in Microsoft Purview

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-ftp-sftp-short  
> Microsoft doc last updated: 2026-10-16


Endpoint data loss prevention (DLP) in Microsoft Purview can monitor and protect sensitive data transferred over FTP and SFTP from managed Windows devices. Endpoint DLP evaluates these transfers against your policy rules, just as it does other device activities such as copying to USB devices or network shares. You can review the resulting events in Activity explorer.

This article explains how to add FTP and SFTP transfers to an Endpoint DLP policy rule and review the resulting events.

Before you begin, review the device onboarding and permissions requirements in Prerequisites.

## Prerequisites

- Devices onboarded to Microsoft Purview.
- Permissions to [create and deploy DLP policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions) and [view Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#permissions). Use the least-privileged roles needed for these tasks.

## Create the policy

We recommend starting with a small pilot group and setting the action to Audit only. Review Activity explorer to understand how users transfer files over FTP/SFTP before you deploy the policy broadly.

To create the policy:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), go to Data loss prevention &gt; Policies &gt; Create policy.
2. On the Locations page, select Devices, and then scope the policy to the users or device groups you want.
3. Create a rule, and add the conditions you want to detect, such as sensitive information types or sensitivity labels.
4. Under Actions, select Audit or restrict activities on devices.
5. In File activities for all apps, select Apply restrictions to specific activity.
6. Select the FTP and SFTP transfers checkbox, and then choose an action. Supported actions are Audit only, Block, Block with override, and Allow.
7. (Optional) Turn on policy tips under User notifications.
8. Review and publish the policy.

The Create rule page shows FTP and SFTP transfers selected with its action set to Block.



## End-user notification

Example of an end-user notification for a blocked FTP transfer:



## Review activity

Use Activity explorer to review the details of each transfer.

1. Open Activity explorer.
2. Filter Activity to File transfer by FTP/SFTP. Review the user, device, file, matched policy, and action for each transfer.

## Collect full file evidence

FTP and SFTP transfers support full file evidence (FFE) collection. Enable evidence collection in Endpoint DLP settings and configure it in your DLP policy. When a user attempts to transfer a matched file, a complete copy can be saved.

For requirements and setup, see [Get started with evidence collection for file activities on devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started).
