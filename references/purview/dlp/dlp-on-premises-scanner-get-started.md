# Get started with data loss prevention for on-premises repositories

> Source: https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-get-started  
> Microsoft doc last updated: 2026-06-26


Note

There's a new version of the information protection scanner. For more information, see [Upgrade the Microsoft Purview Information Protection scanner](https://learn.microsoft.com/en-us/purview/upgrade-scanner-migrate).

This article walks you through the prerequisites and configuration for using the Microsoft Purview Data Loss Prevention on-premises repositories location in a DLP policy.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

Important

All users who contribute to the scanned location, either by adding files or consuming files, need to have a license, not just the scanner user.

### Permissions

Data from DLP can be viewed in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). There are four roles that grant permission to activity explorer, the account you use for accessing the data must be a member of any one of them.

- Compliance administrator
- Security administrator
- Compliance data administrator
- Global administrator

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](https://learn.microsoft.com/en-us/purview/purview-permissions).

#### Roles and Role Groups

There are roles and role groups in the Microsoft Purview portal that you can test to fine-tune your access controls.

Here's a list of applicable roles. To learn more about them, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

Here's a list of applicable role groups. To learn more, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

### DLP on-premises repositories prerequisites

Before you deploy DLP on-premises repositories, ensure that the following prerequisites are met:

- The Microsoft Purview Information Protection scanner implements DLP policy matching and policy enforcement. The scanner is installed as part of the information protection client, so your installation must meet all the prerequisites for the rights management encryption service, the information protection client, and the information protection scanner.
- Deploy the client and scanner. For more information, see, [Install or upgrade the information protection client](https://learn.microsoft.com/en-us/purview/information-protection-client#install-or-upgrade-the-information-protection-client) and, [Configuring and installing the information protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install).
- There must be at least one label and policy published in the tenant, even if all your detection rules are based on sensitive information types only.

## Deploy the DLP on-premises scanner

Perform the following steps to deploy the DLP on-premises scanner:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Follow the procedures in [Install or upgrade the information protection client](https://learn.microsoft.com/en-us/purview/information-protection-client#install-or-upgrade-the-information-protection-client).
3. Follow the procedures in [Configuring and installing the information protection scanner](https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install) to complete the scanner installation.

    1. You must create a content scan job and specify the repositories that host the files to be evaluated by the DLP engine.
    2. Enable DLP rules in the created content scan job, and set the **Enforce** option to **Off** (unless you want to proceed directly to the DLP enforcement stage).
4. Verify that your content scan job is assigned to the right cluster. If you haven't created a content scan job, create a new one and assign it to the cluster that contains the scanner nodes.
5. Connect to the Microsoft Purview portal and add your repositories to the content scan job that will perform the scan.
6. Do one of the following to run your scan:

    1. Set the scanner schedule
    2. Use the manual **Scan Now** option in the portal
    3. Run **Start-Scan** PowerShell cmdlet

    Important

    Remember that the scanner runs a delta scan of the repository by default and files that were scanned in the previous scan cycle will be skipped, unless the file was changed or you initiated a full rescan. A full rescan can be initiated by using the **Rescan all files** option in the UI or by running **Start-Scan -Reset**.
7. Open the [Microsoft Purview portal](https://purview.microsoft.com) &gt; Data Loss Prevention &gt; Policies.
8. Choose **+ Create policy** and create a test DLP policy. See [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) if you need help with creating a policy. Be sure to [**Run the policy in simulation mode**](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn) until you're comfortable with this feature. Use these parameters for your policy:

    1. Scope the DLP on-premises repositories rule to specific locations if needed. If you scope **locations** to **All**, all files scanned will be subject to the DLP rule matching and enforcement.
    2. When specifying the locations, you can use either exclusion or inclusion list. You can either define that the rule is relevant only to paths matching one of the patterns listed in inclusion list or, all files, except the files matching the pattern listed in inclusion list. No local paths are supported. Here are some examples of valid paths:

    - \\server\share
    - \\server\share\folder1\subfolderabc
    - \*\folder1
    - \*secret\*.docx
    - \*secret\*.\*
    - https:// sp2010.local/sites/HR
    - https://\*/HR

    1. Here are some examples of unacceptable values use:

    - \*
    - \*\a
    - Aaa
    - c:\
    - C:\test

Important

The *exclusion* list takes precedence over the *inclusions* list.

### Viewing DLP alerts

Use the following steps to view alerts for your on-premises DLP policies:

1. Open [Data loss prevention](https://purview.microsoft.com/datalossprevention) in the Microsoft Purview portal and select **Alerts**.
2. Refer to the procedures in [Get started with the data loss prevention Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) and [Investigate data loss incidents with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender) to view alerts for your on-premises DLP policies.

### Viewing DLP data in activity explorer and audit log

Note

The Information Protection scanner requires that auditing be enabled. Auditing is enabled by default in Microsoft 365.

1. Open the [Data classification page](https://purview.microsoft.com/dataclassification?viewid=overview) for your domain in the Microsoft Purview portal and select **Activity explorer**.
2. Refer to the procedures in [Get started with Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) to access and filter all the data for your on-premises scanner locations.
3. Open the [Audit log](https://security.microsoft.com/auditlogsearch). The DLP rule matches are available in the Audit log UI or accessible by [Search-UnifiedAuditLog](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/search-unifiedauditlog) in PowerShell.
