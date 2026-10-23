# Microsoft 365 for business security overview

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-security-overview  
> Microsoft doc last updated: 09/30/2025


Microsoft 365 for business is the collective name of Microsoft 365 subscriptions that cater to small to medium sized businesses up to 300 users. For more information, see [What is Microsoft 365 for business?](https://learn.microsoft.com/en-us/microsoft-365/admin/admin-overview/what-is-microsoft-365-for-business).

Microsoft 365 for business includes the following subscriptions:

- **Microsoft 365 Business Basic**: For setup instructions, see [Set up Microsoft 365 Business Basic](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/setup-business-basic).
- **Microsoft 365 Business Standard**: For setup instructions, see [Set up Microsoft 365 Business Standard with a new or existing domain](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/setup-business-standard).
- **Microsoft 365 Business Premium**: For setup instructions, see [Sign in and set up Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365-business-premium-setup).

  > [!TIP]
  > Microsoft 365 for Campaigns is a low priced version of Business Premium for eligible political campaigns or political parties in eligible countries. The security features in Business Premium and Microsoft 365 for Campaigns are identical, unless otherwise identified. For setup instructions, see [Microsoft 365 for Campaigns](https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365-campaigns-setup).

This article and the related content is intended for "administrators" or "admins" who are responsible for the security configuration and settings that affect the entire organization. Whether you have a background in IT or you're thrust into the role by default, you're an admin (congratulations).

## Areas of security in Microsoft 365 for business

After you finish setting up your Microsoft 365 for business organization, you need to review and configure the security settings. You can organize the security settings in Microsoft 365 for business into the following categories:

- Account security.
- Email and collaboration security.
- Device security.

These security categories are described in the following sections and are summarized in the following table:

|&nbsp;|Business<br/>Basic|Business<br/>Standard|Business<br/>Premium|
|---|:---:|:---:|:---:|
|**Account security**||||
|&nbsp;&nbsp;Microsoft Entra ID|Free|Free|Plan 1|
|&nbsp;&nbsp;Microsoft Defender Suite for Business Premium|||Purchased separately<br/>(includes Microsoft Entra ID P2)|
|**Email and collaboration security**||||
|&nbsp;&nbsp;Built-in security features for all cloud mailboxes|✔|✔|✔|
|&nbsp;&nbsp;Microsoft Defender for Office 365|||Plan 1|
|&nbsp;&nbsp;Microsoft Defender Suite for Business Premium|||Purchased separately<br/>(includes Defender for Office 365 Plan 2)|
|**Device security**||||
|&nbsp;&nbsp;Basic Mobility and Security|✔|✔|✔|
|&nbsp;&nbsp;Microsoft Intune|||Plan 1|
|&nbsp;&nbsp;Microsoft Defender for Business|||✔|
|&nbsp;&nbsp;Microsoft Defender Suite for Business Premium|||Purchased separately<br/>(includes Defender for Endpoint Plan 2)|

## Account security

All subscriptions in Microsoft 365 for business include Microsoft Entra ID Free, which includes the feature named _security defaults_. Because security defaults is on by default, multifactor authentication (MFA) is enabled by default in Microsoft 365 for business organizations.

Business Premium also includes Microsoft Entra ID P1, which includes the feature named _Conditional Access_. Conditional Access uses granular policies based on Zero Trust architecture to give users access to resources. If your organization requires increased or complex security settings, you can use Conditional Access policies instead of security defaults.

For information about security defaults and conditional access, see [Multifactor authentication in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/multi-factor-authentication-microsoft-365).

For other considerations for administrator or admin accounts, see [Admin account security in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-account-security-admins)

## Email and collaboration security

All subscriptions in Microsoft 365 for business include the built-in security features for all cloud mailboxes against malware, spam, and phishing (spoofing) in email. For more information, see [Overview of the built-in security features for all cloud mailboxes](https://learn.microsoft.com/en-us/defender-office-365/eop-about).

The built-in security features for all cloud mailboxes include the following types of threat policies that are on by default:

- [Anti-malware policies](https://learn.microsoft.com/en-us/defender-office-365/anti-malware-protection-about#anti-malware-policies)
- [Anti-spam policies](https://learn.microsoft.com/en-us/defender-office-365/anti-spam-protection-about#anti-spam-policies)
- [Spoofing protection in anti-phishing policies](https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about)

Microsoft 365 Business Premium also includes Microsoft Defender for Office 365 Plan 1, which adds the following types of protection:

- [Impersonation protection and phishing email thresholds in anti-phishing policies](https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about#exclusive-settings-in-anti-phishing-policies-in-microsoft-defender-for-office-365)
- [Safe Attachments policies](https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-about)
- [Safe Attachments for SharePoint, OneDrive, and Microsoft Teams](https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-for-spo-odfb-teams-about)
- [Safe Links policies](https://learn.microsoft.com/en-us/defender-office-365/safe-links-about)

The default settings for these email and collaboration protection features provide a good level of protection. But for even better protection, we recommend configuring more settings and features for the best available protection (for example, [turn on and assign the Standard and/or Strict preset security policies](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies#use-the-microsoft-defender-portal-to-assign-standard-and-strict-preset-security-policies-to-users)).

For more information, see [Email and collaboration security in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-email-collaboration-security).

> [!TIP]
> For a deeper dive into default policies vs. custom policies vs. preset security policies, see [Configure threat policies in Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide#step-2-configure-threat-policies).
>
> The security settings in default policies, the Standard preset security policy, and the Strict preset security policy are listed in the tables in [Recommended email and collaboration threat policy settings for cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365).

## Device security

All subscriptions in Microsoft 365 for business include _Basic Mobility and Security_, which is a [limited subset of Microsoft Intune](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview#comparison-of-basic-mobility-and-security-and-microsoft-intune). Basic Mobility and Security is a mobile device management (MDM) solution that helps you secure access to company data on enrolled devices in supported apps.

For more information, see [Overview of Basic Mobility and Security for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview).

**Business Premium** includes the following extra features for device security:

- **Microsoft Intune Plan 1**: Improves upon Basic Mobility and Security with [more features](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview#comparison-of-basic-mobility-and-security-and-microsoft-intune):
  - Support for mobile device management (MDM) and mobile application management (MAM) strategies. In MDM, the company manages the whole device. In MAM, the company manages _company data_ on the device (which is an option for personal devices, also known as bring your own device or BYOD).
  - Support for more device types (including macOS).
  - and more.

  For more information, see the following articles:

  - [Microsoft Intune overview](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/what-is-intune)
  - [Device and application management in Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-enrollment)
  - [Device groups and Microsoft Intune categories in Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-groups-categories)
  - [Device and application protection in Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-protection).

- **Microsoft Defender for Business**: Endpoint security for devices designed especially for small to medium sized businesses. Defender for Business is equivalent to Microsoft Defender for Endpoint Plan 1 with [some features from Defender for Endpoint Plan 2](https://learn.microsoft.com/en-us/defender-business/mdb-faq#what-are-the-differences-between-defender-for-business-and-defender-for-endpoint-plans-1-and-2).

  For more information, see the following articles:

  - [Device groups and Microsoft Intune categories in Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-groups-categories)
  - [Device and application protection in Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-protection).

- **Ability to add Microsoft Defender Suite for Business Premium**: If you choose to buy this extra subscription, you get the following upgraded features:
  - [Microsoft Entra ID P2](https://learn.microsoft.com/en-us/entra/fundamentals/licensing)
  - [Microsoft Defender for Identity](https://learn.microsoft.com/en-us/defender-for-identity/what-is)
  - [Microsoft Defender for Endpoint Plan 2](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint)
  - [Microsoft Defender for Office 365 Plan 2](https://learn.microsoft.com/en-us/defender-office-365/mdo-about#defender-for-office-365-plan-1-vs-plan-2-cheat-sheet)
  - [Microsoft Defender for Cloud Apps](https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps)

  For more information, see [Add Microsoft Defender Suite for Business Premium to your Microsoft 365 Business Premium subscription](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/add-defender-suite-business-premium).

## See also

- [Microsoft 365 Business Premium frequently asked questions](https://learn.microsoft.com/en-us/microsoft-365/business-premium/microsoft-365-business-faqs)
- [Set up information protection capabilities in Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-information-protection)
