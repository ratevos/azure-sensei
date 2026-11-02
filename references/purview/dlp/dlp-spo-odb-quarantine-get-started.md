# Get started with DLP file quarantine for SharePoint and OneDrive

> Source: https://learn.microsoft.com/en-us/purview/dlp-spo-odb-quarantine-get-started  
> Microsoft doc last updated: 2026-06-22


Note

The features described in this article are in preview. This article walks you through the prerequisites and configuration for using the DLP file quarantine action for SharePoint and OneDrive locations.

## Before you begin

### Licensing

For information on licensing, see:

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

DLP file quarantine for SharePoint and OneDrive is only available for E5 licenses.

### Permissions

To configure and manage DLP file quarantine, you need one of the following Microsoft Entra ID roles:

- Compliance administrator
- Security administrator
- Compliance data administrator

#### Recommended permissions for quarantine site management

Because the quarantine site contains highly sensitive files, the administrator who manages it should also have the following data classification permissions:

- **Data Classification List Viewer** — Allows viewing items listed in Data Explorer.
- **Data Classification Content Viewer** — Allows viewing the actual contents of items in Data Explorer.

> 
> ![CAUTION] These permissions aren't technically required to configure or use file quarantine. However, you should use the same criteria when selecting accounts for administering this feature as you do for selecting accounts to be members of the **Data Classification List Viewer** and **Data Classification Content Viewer** roles. You should apply the same account-selection criteria because the quarantine site can contain files with sensitive content that the admin might need to inspect before deciding whether to restore or delete them. To learn more, see [Get started with Data Explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer).

#### Roles and role groups

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

## Deploy a DLP policy with the quarantine action

For step-by-step instructions on how to configure quarantine settings and create and deploy a policy see, [Create a DLP policy to quarantine files in SharePoint and OneDrive](https://learn.microsoft.com/en-us/purview/dlp-create-policy-spo-odb-quarantine).

## View quarantine alerts

Use the following steps to view alerts for quarantined files:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data loss prevention** &gt; **Alerts**.
2. Review alerts for policies that use the quarantine action. DLP alerts and DLP rule match events include:

    - The quarantine file location.
    - The file owner.
    - The original file path.
3. For more information, see [Get started with the data loss prevention alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) and [Investigate data loss incidents with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender).

## View quarantine activity in Data Explorer

Use Activity explorer to review quarantine-related DLP events:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data classification** &gt; **Activity explorer**.
2. Filter for DLP policy rule match events related to your quarantine policy.
3. For more information, see [Get started with Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer).

## Restore a quarantined file

File restore is a manual process.

Important

After restore, original sharing permissions aren't restored. Only the latest file version is preserved. The same DLP rule won't re-quarantine the restored file, even if the file or policy is modified. Other DLP rules continue to apply.

To restore a quarantined file:

1. Locate the quarantined file in the quarantine site.
2. Identify the original file path by using audit logs or the DLP alert details.
3. Move the file from the quarantine site back to the original location.
4. Delete the tombstone text file from the original location.
