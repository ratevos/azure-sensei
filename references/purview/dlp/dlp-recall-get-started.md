# Get started with data loss prevention protections for Recall

> Source: https://learn.microsoft.com/en-us/purview/dlp-recall-get-started  
> Microsoft doc last updated: 2026-06-22


[Recall](https://learn.microsoft.com/en-us/en-us/windows/client-management/manage-recall) is a [Copilot+ PC](https://www.microsoft.com/en-us/windows/learning-center/getting-started-copilot-plus-pc) feature that allows users to search locally saved and locally analyzed snapshots of their screen using natural language. To help protect against the inclusion of sensitive content in these snapshots, you can use DLP policies. The following sections walk you through the prerequisites and configuration steps you perform to start using DLP protections for Recall.

DLP protections for Recall are supported for sensitive information types and sensitivity labeled items in:

- Sensitivity labeled Teams channels
- Sensitivity labeled Teams meeting chats
- SIT or sensitivity labeled files that are opened with Microsoft 365 Copilot App (Word, Excel PowerPoint web apps) using Microsoft Edge for Business
- Labeled emails Outlook
- Locally stored files with sensitivity labels or SITs
- Files stored in the cloud that with sensitivity labels or SITS that get opened in Office apps (Word, Excel, PowerPoint) on the device

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

IT admins can set policies that give Copilot+ PC users the option to enable saving snapshots. The user must then opt in to taking snapshots. For more information, see [Manage Recall](https://learn.microsoft.com/en-us/en-us/windows/client-management/manage-recall).

### Prerequisites

Before you configure DLP protections for Recall, ensure the following prerequisites are met:

- meet all device prerequisites for Recall as described in [Manage Recall](https://learn.microsoft.com/en-us/en-us/windows/client-management/manage-recall).
- Microsoft Purview endpoint DLP is enabled for the tenant the Copilot+ PC is onboarded [to endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started).
- Microsoft Intune is running on the tenant to create Windows tenant policies.
- Copilot+ PC must be running
    - Windows build greater than 262100.67225
    - Anti-malware Client version greater than 4.18.2508.5 or higher
    - Teams version 25290.205.4069.4 or higher
    - Office desktop apps (Word, Excel, PowerPoint) version 19127 or higher
    - Microsoft Edge for Business. For more information, see [Automatic activation of your Microsoft Purview DLP policy in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration#step-3-turn-on-microsoft-edge-settings)

Set the following Group Policy settings on the Copilot+ PC to enable DLP protections for Recall using either Microsoft Intune or Local Group Policy Editor.

| Local Group Policy | Set to | Required | Notes |
| --- | --- | --- | --- |
| WindowsAI &gt; Turn off saving snapshots for use with Recall | Disable | Yes | This policy makes the Recall feature available to users to opt in. This doesn't automatically start Recall for users. Users must launch recall and opt-in to taking snapshots on their machines. |
| WindowsAI &gt; Set maximum duration for storing snapshots used by Recall | 30-180 | Optional | This is the retention period for snapshots in days |
| WindowsAI/Set maximum storage for snapshots used by Recall | 10-150 | Optional | This is the storage limit. For more information, see, [Manage Recall](https://learn.microsoft.com/en-us/en-us/windows/client-management/manage-recall). |
| WindowsAI &gt; SetDataLossPreventionProvider policy | HKEY\_LOCAL\_MACHINE\software\microsoft\windows defender; value:InstallLocation; binary:endpointdlp.dll; minversion:4.18.25080.5 | Yes | This registry value sets the DLP provider (Microsoft Purview) to be used with Recall. This capability is implemented as a public API. |

For more information, see: [SetDataLossPreventionProvide](https://learn.microsoft.com/en-us/en-us/windows/client-management/mdm/policy-csp-windowsai#setdatalosspreventionprovider)

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

For information on the permissions required to create and manage DLP policies, see [Permissions for creating and deploying DLP policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions).

## Configuring DLP policy protections for Recall

When you configure a Copilot+ PC so that the user can opt in to Recall, and the user does opt in, you can create new DLP policies or edit existing policies to include protections for Recall.

For general information on creating DLP policies, see [Create and deploy a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy).

The setting to enable DLP protections for Recall is available when you create or edit a DLP policy in **Enterprise Applications & devices** policies. In the policy editing workflow under **Actions** &gt; **Audit or restrict activities on devices** &gt; **Restrictions in Windows Recall in Copilot+ PCs** &gt; **Restrict content in Windows Recall**. You can select **Audit only** or **Block**.



If you select **Audit only**, then the user doesn't see any notification when a snapshot is taken that contains sensitive information. However, the event is logged in the DLP reports.

If you select **Block**, then when a snapshot is taken that contains sensitive information, then the sensitive content isn't included in the snapshot.

View Recall related events in [Microsoft Purview Activity Explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer).
