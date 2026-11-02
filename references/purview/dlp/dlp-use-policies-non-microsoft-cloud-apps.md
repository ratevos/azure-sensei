# Use DLP policies for non-Microsoft cloud apps

> Source: https://learn.microsoft.com/en-us/purview/dlp-use-policies-non-microsoft-cloud-apps  
> Microsoft doc last updated: 2026-06-26


Important

The Instances policy location in Microsoft Purview Data Loss Prevention (DLP) and policy creation experiences are being retired on January 6th, 2027, as part of the retirement of Microsoft Defender for Cloud Apps file policies. Recreate your policies in Purview using dedicated policy locations for supported non-Microsoft connected apps before this date. For more information, see [Migrate file policies to Microsoft Purview](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/migrate-file-policies-to-purview).

You can scope DLP policies to **Instances** to monitor, detect, and take actions when sensitive items are used and shared via non-Microsoft cloud apps.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to create and deploy policies must be a member of one of these role groups

- Compliance administrator
- Compliance data administrator
- Information Protection
- Information Protection Admin
- Security administrator

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

### Prepare your Defender for Cloud Apps environment

Before you configure DLP policies scoped to **Instances**, you must prepare your Defender for Cloud Apps environment. For instructions, see [Quickstart: Get started with Microsoft Defender for Cloud Apps](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/get-started).

### Connect a non-Microsoft cloud app

To use a DLP policy that's scoped to a specific non-Microsoft cloud app, the app must be connected to Defender for Cloud Apps. For information, see:

- [Connect Box](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/connect-box)
- [Connect Dropbox](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/connect-dropbox)
- [Connect Google Workspace](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/connect-google-workspace)
- [Connect Salesforce](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/connect-salesforce)
- [Connect Cisco Webex](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/connect-webex)
- [Connect AWS](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/protect-aws)
- [Connect ServiceNow](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/protect-servicenow)

After you connect your cloud apps to Defender for Cloud Apps, you can create DLP policies for those apps.

## Create a DLP policy scoped to a non-Microsoft cloud app

Refer to [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) for the procedures to create a DLP policy. Keep these points in mind as you configure your policy:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data loss prevention** &gt; **Policies** &gt; **+ Create policy**.
3. Select **Custom** &gt; **Custom policy**.
4. Name the policy and add a description.
5. Set the **Admin units** scope as desired.
6. On the **Locations** page, toggle the **Instances** location to on.
7. To select a specific app or instance, select **Edit** &gt; **Specific instances** &gt; **+ Include instances** and then the instances (cloud apps) you want to include. If you don't select a instance, the policy will be scoped to all connected apps in your Microsoft Defender for Cloud Apps tenant.
8. **Create rule** with the desired settings. For more information on policy creation, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy).

    1. Under **Actions** select **Restrict Third Party Apps** and select any of the apps listed.

Note

When you create a DLP policy that is scoped to **Instances**, the same policy will be automatically created in Microsoft Defender for Cloud Apps.
