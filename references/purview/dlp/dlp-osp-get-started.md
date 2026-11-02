# Get started with Microsoft Purview DLP oversharing pop-ups in Outlook

> Source: https://learn.microsoft.com/en-us/purview/dlp-osp-get-started  
> Microsoft doc last updated: 2026-06-26


When you configure appropriate Microsoft Purview Data Loss Prevention (DLP) policy, DLP checks email messages before they're sent for any labeled or sensitive information and apply the actions defined in the DLP policy. Oversharing pop-ups require a Microsoft 365 **E5 subscription**, along with a version of Outlook that supports oversharing pop-ups. For more information in required version, see [Oversharing dialog for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips#oversharing-dialog-for-outlook-for-microsoft-365).

Important

The following is a hypothetical scenario with hypothetical values. It's only for illustrative purposes. You should substitute your own sensitive information types, sensitivity labels, distribution groups, and users when implementing this feature.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to create and deploy policies must be a member of one of the following role groups

- Compliance administrator
- Compliance data administrator
- Information Protection
- Information Protection Admin
- Security administrator

Important

Read [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units) before you start to make sure you understand the difference between an *unrestricted administrator* and an *administrative unit restricted administrator*.

### Granular roles and role groups

There are several roles and role groups that you can use to fine tune access controls for Microsoft Purview DLP policy management.

Here's a list of applicable roles. To learn more, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- DLP Compliance Management
- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

Here's a list of applicable role groups. To learn more about them, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

### Prerequisites and assumptions

In Outlook for Microsoft 365, an oversharing pop-up displays a pop-up before a message is sent. To enable these pop-ups, first scope your policy to the Exchange location and then select the **Show policy tip as a dialog for the user before send** option in the policy tip when you create a data loss prevention (DLP) rule for that policy.

Our example scenario uses the *Highly confidential* sensitivity label, so it requires that you have created and published sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

This procedure uses *contoso.com*. a hypothetical company domain.

## Policy intent statement and mapping

For this example, our policy intent statement is:

*We need to block emails to all recipients that have the 'highly confidential' sensitivity label applied, unless the recipient domain is contoso.com. We want to notify the user with a pop-up dialogue when they send the email. No users can be allowed to override the block.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| "We need to block emails to all recipients..." | - **Where to monitor**: Exchange - **Administrative scope**: Full directory - **Action**: Restrict access or encrypt the content in Microsoft 365 locations &gt; Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files &gt; Block everyone |
| "...that have the 'highly confidential' sensitivity label applied..." | - **What to monitor**: use the Custom template  - **Conditions for a match**: edit it to add the *highly confidential* sensitivity label |
| "...unless..." | **Condition group configuration** - Create a nested boolean NOT condition group joined to the first conditions using a boolean AND |
| "...the recipient domain is contoso.com." | **Condition for match**: Recipient domain is |
| "...Notify..." | **User notifications**: enabled |
| "...the user with a pop-up dialogue when they send..." | **Policy tips**: selected  - **Show policy tip as a dialog for the end user before send**: selected |
| "...No users can be allowed to override the block... | **Allow overrides from M365 Services**: not selected |

To configure oversharing pop-ups with default text, the DLP rule must include these conditions:

- **Content contains** &gt; **Sensitivity labels** &gt; **choose your sensitivity label(s)**

and one or more of the following recipient-based conditions

- Recipient is
- Recipient is a member of
- Recipient domain is

When these conditions are met, the policy tip displays untrusted recipients while the user is writing the mail in Outlook, before they send it.

If the block rules defined in the DLP policy are met, the message will be blocked regardless of how **Policy tips** is configured.

### Steps to configure "wait on send"

Optionally, you can set the *dlpwaitonsendtimeout Regkey (Value in dword)* on all the devices where you want to implement "wait on send" for oversharing pop-ups. This registry key (*RegKey*) defines the maximum amount of time to hold the email when a user selects **Send**. This allows the system to complete the DLP policy evaluation for labeled or sensitive content. You can find this RegKey under:

\*Software\Policies\Microsoft\office\16.0\Outlook\options\Mail\*

You can set this *RegKey* via group policy, **Specify wait time to evaluate sensitive content**, script, or other mechanism for configuring registry keys.

If you're using Group Policy, make sure you download the most recent version of the Group Policy Administrative Template files for Microsoft 365 Apps for enterprise and then navigate to **User Configuration** &gt; **Administrative Templates** &gt; **Microsoft Office 2016** &gt; **Security Settings** &gt; **Specify wait time to evaluate sensitive content**. If you're using the Cloud Policy service for Microsoft 365, search for the setting by name to configure it.

When this value is set and the DLP policy is configured, email messages are checked for sensitive information before they're sent. If a message contains a match to the conditions defined in the policy, a policy tip notification appears before the user select **Send**..

The *dlpwaitonsendtimeout* registry key allows you to specify the **wait on send** behavior for your Outlook clients.

Here's what each *dlpwaitonsendtimeout* setting means:

**Not configured** or **Disabled**: This is the default. When *dlpwaitonsendtimeout* isn't configured, the message isn't checked before the user sends it. The email message is sent immediately once **Send** is clicked. The DLP data classification service evaluates the message and apply the actions defined in the DLP policy.

**Enabled**: The email message is checked when the **Send** is clicked but before the message is sent. You can set a time limit on how long to wait for DLP policy evaluation to complete (**T** value, in seconds). If the policy evaluation doesn't complete in the specified time a **Send anyway** button appears allowing the user to bypass the presend check. The **T** value range is 0 to 9999 seconds.

Important

If the **T** value is greater than 9999, it's replaced with 10000 and the **Send Anyway** button doesn't appear. This holds the message until the policy evaluation completes and doesn't provide the user with an *override* option. The duration for completing the evaluation can vary depending on factors such as internet speed, content length, and the number of policies defined. Some users may encounter policy evaluation messages more frequently than others, depending on the policies that are deployed on their mailbox.

To learn more about configuring and using GPO see, [Administer Group Policy in a Microsoft Entra Domain Services managed domain](https://learn.microsoft.com/en-us/en-us/azure/active-directory-domain-services/manage-group-policy).

### Steps to create a DLP policy for an oversharing pop-up

Perform the following steps to create a DLP policy that triggers an oversharing pop-up in Outlook.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Policies**
2. Choose **+ Create policy**.
3. Select **Custom** from the **Categories** list.
4. Select **Custom** from the **Regulations** list.
5. Give the policy a name.
6. Fill in a description. You can use the policy intent statement here.
7. Select **Next**.
8. Select **Full directory** under **Admin units**.
9. Select only the **Exchange email** location.
10. Select **Next**.
11. On the **Define policy settings** page, select **Create or customize advanced DLP rules**.
12. The **Create or customize advanced DLP rules** option should already be selected.
13. Select **Next**.
14. Select **Create rule**. Name the rule and provide a description.
15. Select **Add condition** &gt; **Content contains** &gt; **Add** &gt; **Sensitivity labels** &gt; **Highly confidential**. Choose **Add**.
16. Select **Add group** &gt; **AND** &gt; **NOT** &gt; **Add condition**.
17. Select **Recipient domain is** &gt; **contoso.com**. Choose **Add**.

    Tip

    You can also use **Recipient is** or **Recipient is a member of** instead of **Recipient domain is** to trigger an oversharing pop-up.
18. Select **Add an action** &gt; **Restrict access or encrypt the content in Microsoft 365 locations**.
19. Select **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files, and Power BI items**.
20. Select **Block everyone**.
21. Set the **User notifications** toggle to **On**.
22. Select **Policy tips** &gt; **Show the policy tip as a dialog for the end user before send (available for Exchange workload only)**.
23. *If already selected*, uncheck the **Allow override from M365 services** option.
24. Choose **Save**.
25. Change the **Status** toggle to **On** and then choose **Next**.
26. On the **Policy mode** page, select **Run the policy in test mode** and check the box for the **Show policy tips while in simulation mode** option.
27. Choose **Next** and then choose **Submit**.
28. Choose **Done**.

#### PowerShell steps to create policy

DLP policies and rules can also be configured in PowerShell. To configure oversharing pop-ups using PowerShell, first you create a DLP policy (using PowerShell) and add DLP rules for each warn, justify or block pop-up type.

You'll configure and scope your DLP Policy using [New-DlpCompliancePolicy](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancepolicy). Then, you configure each oversharing rule using [New-DlpComplianceRule](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule)

To configure a new DLP policy for the oversharing pop-up scenario use this code snippet:

```powershell
PS C:\> New-DlpCompliancePolicy -Name <DLP Policy Name> -ExchangeLocation All
```

This sample DLP policy is scoped to all users in your organization. Scope your DLP Policies using `-ExchangeSenderMemberOf` and `-ExchangeSenderMemberOfException`.

| Parameter | Configuration |
| --- | --- |
| [-ContentContainsSensitiveInformation](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule?view=exchange-ps#-contentcontainssensitiveinformation&amp;preserve-view=true) | Configures one or more sensitivity label conditions. This sample includes one. At least one label is mandatory. |
| [-ExceptIfRecipientDomainIs](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule?view=exchange-ps#-exceptifrecipientdomainis&amp;preserve-view=true) | List of trusted domains. |
| [-NotifyAllowOverride](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule?view=exchange-ps#-notifyallowoverride&amp;preserve-view=true) | "WithJustification" enables justification radio buttons, "WithoutJustification" disables them. |
| [-NotifyOverrideRequirements](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule?view=exchange-ps#-notifyoverriderequirements&amp;preserve-view=true) | "WithAcknowledgement" enables the new acknowledgment option. This is optional. |
|  |  |

To configure a new DLP rule to generate a *warn* pop-up using trusted domains, run the following PowerShell code:

```powershell
PS C:\> New-DlpComplianceRule -Name <DLP Rule Name> -Policy <DLP Policy Name> -NotifyUser Owner -NotifyPolicyTipDisplayOption "Dialog" -ContentContainsSensitiveInformation @(@{operator = "And"; groups = @(@{operator="Or";name="Default";labels=@(@{name=<Label GUID>;type="Sensitivity"})})}) -ExceptIfRecipientDomainIs @("contoso.com","microsoft.com")
```

To configure a new DLP rule to generate a *justify* pop-up using trusted domains, run this PowerShell code:

```powershell
PS C:\> New-DlpComplianceRule -Name <DLP Rule Name> -Policy <DLP Policy Name> -NotifyUser Owner -NotifyPolicyTipDisplayOption "Dialog" -BlockAccess $true -ContentContainsSensitiveInformation @(@{operator = "And"; groups = @(@{operator = "Or"; name = "Default"; labels = @(@{name=<Label GUID 1>;type="Sensitivity"},@{name=<Label GUID 2>;type="Sensitivity"})})}) -ExceptIfRecipientDomainIs @("contoso.com","microsoft.com") -NotifyAllowOverride "WithJustification"
```

To configure a new DLP rule to generate a *block* pop-up using trusted domains, run this PowerShell code:

```powershell
PS C:\> New-DlpComplianceRule -Name <DLP Rule Name> -Policy <DLP Policy Name> -NotifyUser Owner -NotifyPolicyTipDisplayOption "Dialog" -BlockAccess $true -ContentContainsSensitiveInformation @(@{operator = "And"; groups = @(@{operator = "Or"; name = "Default"; labels = @(@{name=<Label GUID 1>;type="Sensitivity"},@{name=<Label GUID 2>;type="Sensitivity"})})}) -ExceptIfRecipientDomainIs @("contoso.com","microsoft.com")
```

For more information, see [Business justification X-Header](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#business-justification-x-header).
