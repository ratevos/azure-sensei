# Microsoft 365 for business security best practices

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-security-best-practices  
> Microsoft doc last updated: 08/14/2025


> [!TIP]
> **This article is for small and medium sized businesses with up to 300 users**.
>
> If you're looking for information for enterprise organizations, see [Deploy ransomware protection for your Microsoft 365 organization](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/ransomware-protection-microsoft-365).
>
> If you're a Microsoft partner, see [Resources for Microsoft partners working with small and medium-sized businesses](https://learn.microsoft.com/en-us/defender-business/mdb-partners).

Microsoft 365 for business, which includes Microsoft 365 Business Basic, Microsoft 365 Business Standard, and Microsoft 365 Business Premium, includes anti-phishing, anti-spam, and anti-malware protection for email. Microsoft 365 Business Premium includes even more security capabilities, such as advanced cybersecurity protection for:

- Devices (computers, tablets, and phones; also known as _endpoints_)
- Email & collaboration content (for example, Office documents)
- Data (encryption, sensitivity labels, and Data Loss Prevention or DLP)

This article describes the top 10 ways to secure your business data with Microsoft 365 for business. For more information about what each plan includes, see [Microsoft 365 User Subscription Suites for Small and Medium-sized Businesses](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RWR6bM).

## Top 10 ways to secure your business data

The following table summarizes how to secure your data using Microsoft 365 for business.

|Best practices and capabilities|Business<br/>Basic|Business<br/>Standard|Business<br/>Premium|
|---|:---:|:---:|:---:|
|**1. Use multi-factor authentication** (MFA), also known as two-step verification:||||
|&nbsp;&nbsp;&nbsp;[Security defaults](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication#manage-security-defaults) is on by default and is suitable for most organizations.|✔|✔|✔|
|&nbsp;&nbsp;&nbsp;Use [Conditional Access](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication#manage-conditional-access-policies) for more stringent requirements.|||✔|
|**2. Protect admin accounts**. See [Admin account security in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-account-security-admins).|✔|✔|✔|
|**3. Use preset security policies**. See [Preset security policies in cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies) and [Determine your threat policy strategy](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide#determine-your-threat-policy-strategy).||||
|&nbsp;&nbsp;&nbsp;[Built-in security features for all cloud mailboxes](https://learn.microsoft.com/en-us/defender-office-365/eop-about). Includes: Anti-spam, anti-malware, and anti-phishing (spoof) protection.|✔|✔|✔|
|&nbsp;&nbsp;&nbsp;[Microsoft Defender for Office 365 Plan 1](https://learn.microsoft.com/en-us/defender-office-365/mdo-about#defender-for-office-365-plan-1-capabilities) protection. Includes: Extra anti-phishing protection features (impersonation protection and anti-phishing thresholds), Safe Links (email, Office apps, and Microsoft Teams), and Safe Attachments (email and files in SharePoint, OneDrive, and Microsoft Teams)|||✔|
|**4. Protect all devices** that access company data, including personal and company devices:||||
|&nbsp;&nbsp;&nbsp;[Basic Mobility and Security](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview) (provides mobile device management or MDM)|✔|✔|✔|
|&nbsp;&nbsp;&nbsp;[Microsoft Intune Plan 1](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-enrollment) (provides MDM _and_ mobile app management or MAM)|||✔|
|&nbsp;&nbsp;&nbsp;[Device protection policies in Microsoft Defender for Business and Microsoft Intune](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-protection)|||✔|
|**5. Use email securely**||||
 &nbsp;&nbsp;&nbsp;[Protect yourself against phishing and other attacks](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-users-phishing-spam-malware).|✔|✔|✔|
|&nbsp;&nbsp;&nbsp;Use [Microsoft Purview Message Encryption](https://learn.microsoft.com/en-us/purview/email-encryption) automatically with [Exchange mail flow rules](https://learn.microsoft.com/en-us/purview/define-mail-flow-rules-to-encrypt-email) (also known as transport rules) or [manually](https://support.microsoft.com/office/eaa43495-9bbb-4fca-922a-df90dee51980). [Custom branding](https://learn.microsoft.com/en-us/purview/add-your-organization-brand-to-encrypted-messages) is also available.|||✔|
|&nbsp;&nbsp;&nbsp;Use [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) to safeguard company data.|||✔|
|&nbsp;&nbsp;&nbsp;Use [Sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels) to mark email messages as sensitive, confidential, etc.|||✔|
|**6. Work together in Microsoft Teams**||||
|&nbsp;&nbsp;&nbsp;Use [Microsoft Teams](https://learn.microsoft.com/en-us/microsoft-365/business-premium/create-teams-for-collaboration) for communication, collaboration, and sharing|✔|✔|✔|
|&nbsp;&nbsp;&nbsp;Get time of click protection for URLs and files in Teams messages with [Safe Links for Microsoft Teams](https://learn.microsoft.com/en-us/defender-office-365/safe-links-about#safe-links-settings-for-microsoft-teams) and [Safe Attachments for SharePoint, OneDrive, and Microsoft Teams](https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-for-spo-odfb-teams-about).|||✔|
|&nbsp;&nbsp;&nbsp;Allow/block [URLs](https://learn.microsoft.com/en-us/defender-office-365/tenant-allow-block-list-urls-configure) and [files](https://learn.microsoft.com/en-us/defender-office-365/tenant-allow-block-list-files-configure) inside Teams using the Tenant Allow/Block List.|||✔|
|&nbsp;&nbsp;&nbsp;Use [sensitivity labels for meetings](https://learn.microsoft.com/en-us/purview/sensitivity-labels-meetings) to protect calendar items, Teams meetings, and chat.|||✔|
|&nbsp;&nbsp;&nbsp;Use [Microsoft Purview Data Loss Prevention in Microsoft Teams](https://learn.microsoft.com/en-us/purview/dlp-teams-default-policy) to safeguard company data.|||✔|
|**7. Set file sharing settings**||||
|&nbsp;&nbsp;&nbsp;[Safe Links](https://learn.microsoft.com/en-us/defender-office-365/safe-links-about) and [Safe Attachments](https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-for-spo-odfb-teams-about) for SharePoint and OneDrive|||✔|
|&nbsp;&nbsp;&nbsp;Use [Sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels) to mark items as sensitive, confidential, etc.|||✔|
|&nbsp;&nbsp;&nbsp;Use [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) to safeguard company data.|||✔|
|**8. Use Microsoft 365 Apps**||||
|&nbsp;&nbsp;&nbsp;Use [Outlook and web/mobile versions of Microsoft 365 Apps](https://support.microsoft.com/office/56e60c2b-1929-4a04-bd9b-ff5b844364f3) for all users|✔|✔|✔|
|&nbsp;&nbsp;&nbsp;Install [Microsoft 365 Apps](https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365bp-users-install-m365-apps) on user devices.||✔|✔|
|&nbsp;&nbsp;&nbsp;Use the [User quick setup guide](https://support.microsoft.com/office/7f34c318-e772-46a5-8c0a-ab86661542d1) to help users get set up and running.|✔|✔|✔|
|**9. Manage calendar sharing**||||
|&nbsp;&nbsp;&nbsp;[Outlook](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/setup-outlook) for email and calendars.|✔|✔|✔|
|&nbsp;&nbsp;&nbsp;[Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) to safeguard company data.|||✔|
|**10. Maintain your environment**: See [Maintain your environment](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-security-monitor).|✔|✔|✔|

For more information about what each plan includes, see [Microsoft 365 User Subscription Suites for Small and Medium-sized Businesses](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RWR6bM).
