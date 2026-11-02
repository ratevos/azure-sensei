# Use data loss prevention with on-premises repositories

> Source: https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-use  
> Microsoft doc last updated: 2026-06-26


To help familiarize you with Microsoft Purview Data Loss Prevention on-premises features and how they surface in DLP policies, we've put together a couple of scenarios for you to follow. These scenarios show you how to discover files that match DLP rules across Activity Explorer, the audit log, and the information protection scanner, and how to enforce protective actions on on-premises file shares and SharePoint document libraries. Specifically, the first scenario covers where DLP rule-match data appears when scanning on-premises repositories, and the second scenario walks through enabling policy enforcement so that protective actions are applied to scanned files.

Important

These DLP on-premises scenarios are not the official procedures for creating and tuning DLP policies. Refer to the following topics when you need to work with DLP policies in general situations:

- [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
- [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy)

## Scenario: Discover files matching DLP rules

Data from DLP surfaces in several areas:

### View on-premises repository events in Activity Explorer

DLP reports rule matches are available in [Activity Explorer](https://compliance.microsoft.com/dataclassification?viewid=activitiesexplorer).

### View on-premises repository events in the Microsoft 365 audit log

The DLP rule matches are also available in the Audit log UI (see [Search the audit log](https://learn.microsoft.com/en-us/purview/audit-search)) and are accessible via PowerShell through the[Search-UnifiedAuditLog](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/search-unifiedauditlog).

### Use the information protection scanner to inspect matching files

Discovery data is available in a local report in .csv format and is stored under:

**%localappdata%\Microsoft\MSIP\Scanner\Reports\DetailedReport\_%timestamp%.csv report**.

Look for the following columns:

- DLP Mode
- DLP Status
- DLP Comment
- DLP Rule Name
- DLP Actions
- Owner
- Current NTFS Permissions (SDDL)
- Applied NTFS Permissions (SDDL)
- NTFS permissions type

## Scenario: Enforce DLP rule

If you want to enforce DLP rules on scanned files, enforcement must be enabled both on the content scan job and at the policy level in DLP.

### Configure DLP to enforce policy actions

To turn on enforcement for your DLP policy targeting on-premises repositories, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com)
2. Navigate to **Data loss prevention** &gt; **Policies**.
3. Select the DLP policy that is targeted to the on-premises location repositories you have configured for the scanner.
4. Edit the policy.
5. On the **Policy Mode** page, select **Turn the policy on immediately**.
6. Choose **Next** and then choose **Submit**.
7. Choose **Done**.
