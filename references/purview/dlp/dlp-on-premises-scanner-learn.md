# Learn about data loss prevention on-premises repositories

> Source: https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-learn  
> Microsoft doc last updated: 2025-03-31


When you select the **On-premises repositories** location, Microsoft Purview Data Loss Prevention (DLP) can enforce protective actions on on-premises data-at-rest in file shares and SharePoint document libraries and folders. This gives you the visibility and control you need to ensure that sensitive items are used and protected properly, and to help prevent risky behavior that might compromise them. The DLP detects sensitive information by using [built-in](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions) or [custom sensitive information](https://learn.microsoft.com/en-us/purview/sit-create-a-custom-sensitive-information-type) types, [sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels) or file properties. The information about what users are doing with sensitive items is made visible in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) and you can enforce protective actions on those items via [DLP policies](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## DLP relies on Microsoft Purview Information Protection scanner

DLP relies on a full implementation of the Microsoft Purview Information Protection scanner to monitor, label, and protect sensitive items. If you haven't implemented the information protection scanner, you must do so before you can use DLP. For more information, read these articles:

- [Learn about the information protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner)
- [Get started with the information protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner-prereqs)
- [Configuring and installing the information protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install)
- [Microsoft Purview Information Protection client - Release management and supportability](https://learn.microsoft.com/en-us/purview/information-protection-client-relnotes)

## DLP On-premises repository actions

DLP detects files in on-premises repositories by looking for the following:

- sensitive information types
- sensitivity labels
- file extension
- custom document properties on Office files only

When a detected file matches a DLP policy, DLP can take one of the following four actions.

| Action | Description |
| --- | --- |
| **Block people from accessing file stored in on-premises scanner - Block everyone** | When enforced, this action blocks access to all accounts except the content owner, the account that last modified the item, and the administrator. It does this by removing all accounts from NTFS/SharePoint permissions at the file level except for the file owner, repository owner (set in the [Use a DLP policy](https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install#use-a-dlp-policy) setting in content scan job), last modifier (can be identified in SharePoint only), and admin. The scanner account is also granted FC rights on the file. |
| **Block only people who have access to your on-premises network and users in your organization who weren't granted explicit access to the files from accessing file** | When enforced, this action removes the ***Everyone***, ***NT AUTHORITY\authenticated users***, and ***Domain Users*** SIDs from the file access control list (ACL). Only users and groups that have been explicitly granted rights to the file or parent folder will be able to access the file. |
| **Set permissions on the file (permissions will be inherited from the parent folder)** | When enforced, this action forces the file to inherit the permissions of its parent folder. By default, this action will only be enforced if the permissions on the parent folder are more restrictive than the permissions that are already on the file. For example, if the ACL on the file is set to allow only ***specific users*** and the parent folder is configured to allow the ***Domain Users*** group, the parent folder permissions wouldn't be inherited by the file. You can override this behavior by selecting the **Inherit even if parent permissions are less restrictive** option. |
| **Remove the file from improper location** | When enforced, this action replaces the original file with a stub file with .txt extension and places a copy of the original file in a quarantine folder. |

## What's different in the on-premises scanner

There are a few extra concepts that you need to be aware of before you dig into the on-premises scanner.

### Scanner repositories and content scan jobs

You must create a content scan job for the information protection scanner and identify the repositories that host the files that you want to DLP to evaluate. Make sure you enable DLP rules in the created content scan job.

### Policy tips

[Policy tips](https://learn.microsoft.com/en-us/purview/dlp-use-notifications-and-policy-tips) aren't available in on-premises scanner.

### Viewing DLP on-premises scanner events

You view DLP data in the Microsoft Purview portal [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer).
