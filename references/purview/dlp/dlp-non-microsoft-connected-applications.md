# Use Microsoft Purview data loss prevention policies for non-Microsoft connected apps (preview)

> Source: https://learn.microsoft.com/en-us/purview/dlp-non-microsoft-connected-applications  
> Microsoft doc last updated: 2026-08-26


Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

Microsoft Purview Data Loss Prevention (DLP) extend to non-Microsoft connected apps, allowing you to detect, monitor, and protect sensitive data at rest in non-Microsoft SaaS applications. You can create DLP policies that apply to data stored in these non-Microsoft apps, using the same classification engine and policy framework available for Microsoft 365 locations.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Supported non-Microsoft apps

Microsoft Purview supports DLP policies for the following non-Microsoft apps:

- Box
- Dropbox
- Google Workspace
- Salesforce
- AWS
- Cisco Webex
- ServiceNow

Note

These apps are rolling out in phases. Not all apps may be available in your tenant at the same time. Check the [Microsoft 365 roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) for the latest availability information.

## Before you begin

### Licensing requirements

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to create and deploy policies must be a member of one of these role groups:

- Compliance administrator
- Compliance data administrator
- Information Protection
- Information Protection Admin
- Security administrator

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

### Set up a Microsoft Defender for Cloud Apps connector

Before you can apply DLP policies to a non-Microsoft app, you must connect that app to Microsoft Defender for Cloud Apps using an app connector. Purview uses the existing Microsoft Defender for Cloud Apps connectors to access capabilities in the non-Microsoft app.

For instructions on setting up app connectors, see [Connect apps to get visibility and control with Microsoft Defender for Cloud Apps](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps).

After you connect your cloud apps to Defender for Cloud Apps, you can create DLP policies for them in Microsoft Purview.

## Create a DLP policy for non-Microsoft connected apps

To create a DLP policy scoped to non-Microsoft connected apps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Go to **Solutions** &gt; **Data Loss Prevention** &gt; **Policies** &gt; **+ Create policy**.
3. On **What info do you want to protect?**, choose the **Enterprise applications & devices** option.
4. Select **Custom** &gt; **Custom policy**, and then select **Next**.

    Important

    Non-Microsoft connected app policies are only supported with the **Custom** policy template. The predefined Financial, Medical and health, and Privacy templates don't support non-Microsoft app locations.
5. Enter a name and description for the DLP policy, then select **Next**.
6. On **Assign admin units**, the scope is set to **Full directory**. Administrative units aren't supported for non-Microsoft app locations.
7. On **Choose where to apply the policy**, select one or more of the supported non-Microsoft apps (such as **Box**, **Dropbox**, **Google Workspace**, **Salesforce, AWS, Cisco Webex, ServiceNow**.

    Important

    Non-Microsoft app locations can be selected together, but they can't be combined with other locations like SharePoint, OneDrive, Exchange, Fabric, or Devices in the same policy.
8. By default, the policy applies to all instances of the selected app. To scope the policy to specific tenants, select **Edit**.

    1. To exclude instances, in **All instances**, select **Exclude instances** &gt; **+ Exclude instance**. From the list of instances, select instances to exclude from the policy, and then select **Done** &gt; **Done**.
    2. To apply the policy to specific instances, select **Specific instances** &gt; **+ Include instance**. From the list of instances, select instances to include, then select **Done** &gt; **Done**.
9. Select **Next** to proceed.
10. On **Define policy settings**, select **Create or customize advanced DLP rules** to define an advanced DLP rule. Only advanced DLP rules are supported for non-Microsoft connected apps. Select **Next**.
11. Select **+ Create rule**, and provide a **Name** and **Description**.
12. Configure **Conditions** for the rule. The conditions you can use vary by app.
13. Configure **Actions** for the rule. The available actions vary by app.
14. Configure **Notifications**. Note the following limitations for non-Microsoft apps:

    - **Policy tips** aren't supported.
    - **User overrides** aren't supported.
15. Select **Save** to save the rule, then select **Next**.
16. On **Policy mode**, choose either **Turn the policy on immediately** or **Leave the policy turned off**. Select **Next**.

    Important

    **Simulation mode** isn't supported for non-Microsoft connected app policies.
17. Review your settings and select **Submit** to create the policy.

## Attribute availability by app

The conditions and actions you can use in a policy depend on the item attributes that each app makes available. Most attributes are available for all supported apps, but some aren't available for certain apps. Use the following table to understand which attributes you can rely on when you build rules for a specific app.

| Attribute | Description | Availability |
| --- | --- | --- |
| Name | The display name of the item. | Available in all apps |
| File access level | The item's access level, which indicates its sharing scope. | Available in all apps |
| Created date | The date the item was created. | Not available in Dropbox |
| Modified date | The date the item was last modified. | Available in all apps |
| Collaborators | The users the item is shared with, including their roles. | Available in all apps |
| Parent folders | The parent folders that contain the item. | Available in all apps |

## Monitoring and reporting

### Activity explorer

Activity explorer supports non-Microsoft connected app policies. You can monitor DLP policy activity for your non-Microsoft apps in the same way you monitor Microsoft 365 locations.

### Content explorer

Content explorer isn't supported for non-Microsoft connected apps. You can't browse or inspect content stored in these apps through Content explorer.

### Alerts

DLP alerts are supported for non-Microsoft connected app policies. Alerts appear in the DLP alerts dashboard alongside alerts from other locations.

## Known issues

The following is a list of known issues when using non-Microsoft connected apps for DLP policies:

- **Encrypted files** – Encrypted files stored in non-Microsoft apps aren't currently supported for classification.
- **PDF files** – PDF files stored in non-Microsoft apps aren't currently supported for classification.
