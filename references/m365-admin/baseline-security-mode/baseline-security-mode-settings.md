# Baseline security mode settings

> Source: https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/baseline-security-mode-settings  
> Microsoft doc last updated: 04/17/2026


As a Microsoft 365 admin, you can use Baseline security mode settings to protect and secure your business environment against external threats.

Baseline security mode helps you:

- Protect business data.
- Prevent business disruption.
- Block unsafe end user practices.
- Secure internal accounts.
- Ensure secure collaboration.

Baseline Security Mode covers key Microsoft 365 services, including:

- Microsoft 365 apps.
- SharePoint and OneDrive.
- Microsoft Teams.
- Exchange Online.
- Microsoft Entra identity platform.

By using Baseline Security Mode in the Microsoft 365 admin center, you can set certain security settings that were previously available only in PowerShell.

Now that these settings are available in the admin center, your organization can carefully evaluate each of the Baseline Security Mode settings before deployment.

This article provides information about the Baseline security mode settings that you can turn on. It also has links to content that helps you understand what each setting does and why you should turn on the setting.

## Before you begin

Workload-specific administrators can manage only their own settings. To manage the settings you want to configure, make sure to sign in with an account that has the appropriate role. For example, to manage settings related to Microsoft 365 apps, sign in with an account that has the Security administrator role.

Baseline security mode settings support role-based access control (RBAC), so the following roles can also see these settings:

- [Office Apps administrator role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).
- [SharePoint administrator role](https://learn.microsoft.com/en-us/sharepoint/sharepoint-admin-role).
- [Exchange Administrator role](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-exchange-online-admin-role).
- [Teams administrator role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

For more information, see [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

> [!IMPORTANT]
>
> You can configure Baseline security mode settings on all Microsoft 365 subscriptions and plans.

## Baseline security mode settings recommendation

Baseline security mode settings provide flexibility and control, so you can manage each setting independently. You can also experiment by disabling a setting for a defined period (such as a few days) to assess dependencies.

Run the Baseline security mode settings in this way:

- Run impact reports for each of the Baseline security mode settings.
- If the setting displays zero impacts, turn on that setting.
- If critical dependencies exist, don't turn on the setting. Plan to address those dependencies before making the changes permanent. This intuitive, phased approach ensures a smooth transition to secure-by-default configurations.

## How to access Baseline Security Mode settings

To access **Baseline Security Mode** settings, follow these steps:

1. Sign in to [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Org Settings**](https://go.microsoft.com/fwlink/p/?linkid=2053743).

1. In the **Org Settings** page, select the [**Security and Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756) tab.

1. In the **Security and Privacy** tab, select **Baseline Security Mode**.

## Authentication

This section outlines the options available to block insecure authentication methods in the Microsoft 365 admin center.

> [!IMPORTANT]
>
> Customers who accessed Baseline Security Mode in Microsoft 365 between November 2025 and early February 2026 might see two draft Microsoft Entra ID Conditional Access policies created in their tenant in a **Disabled** state. These policies are associated with Baseline Security Mode and might appear as created by the administrator who signed in to the Microsoft Baseline Security Mode page.
>
> This behavior doesn't represent a security incident and has no effect on tenant security. The policies are in a disabled draft state. A fix is in progress to ensure policies are created only through explicit administrator action. Microsoft removes any unintentionally created policy drafts and notifies customers in advance.

|Setting|More information|
|---|---|
|**Protect admin access to Microsoft admin portals with phishing resistant authentication**|Accounts that are assigned [specific privileged administrative roles](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) are frequent targets of attackers. Requiring phishing-resistant multifactor authentication (MFA) on those accounts is an easy way to reduce the risk of those accounts being compromised.<br/><br/> For more information, see [Require phishing-resistant multifactor authentication for administrators](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) <br/><br/> You must be a member of the [Security administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) or the [Conditional access administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) roles to perform this task.|
|**Block legacy authentication flows**|Block authentication requests that use legacy protocols that don't support multifactor authentication. Based on analysis, most credential stuffing attacks use legacy authentication and most password spray attacks use legacy authentication protocols. You can help stop these attacks by disabling or blocking basic authentication. <br/><br/> For more information, see [Block legacy authentication with Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication) <br/><br/> You must be a member of the [Security administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) or the [Conditional access administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) roles to perform this task.|
|**Block addition of new password credentials to apps**|To increase security, block the addition of password credentials on applications. Passwords are one of the weakest methods of service authentication and are vulnerable to compromise by bad actors. Switching to a more secure method improves security and reduces management overhead.<br/><br/>For more information, see [Restrict password usage on Microsoft Entra apps](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/block-password-addition).<br/><br/> You must be a member of the [Security administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference), [Application administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference), or the [Cloud Application administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) roles to perform this task.|
|**Restrict end-user consent to Microsoft 365 certified and single tenant apps with low risk permissions**|Update your Microsoft Entra user consent settings to restrict users to grant access to applications created in your tenant or from the [Microsoft 365 certified list](https://learn.microsoft.com/en-us/microsoft-365-app-certification/saas/saas-apps). Microsoft works with Microsoft 365 developer partners to provide this information so organizations can expedite and inform decisions about apps and add-ins their users can use. <br/><br/> For more information, see [Configure how users consent to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal) <br/><br/> You must be a member of the [Security administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) or the [Privileged role administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) roles to perform this task.|
|**Block basic authentication**|Basic authentication is an outdated and insecure method that transmits user credentials in a way that can easily be intercepted and stolen. When you block basic authentication prompts, this setting helps protect your users from credential theft, especially during phishing attacks or when accessing services over insecure networks. When you enable this setting, users no longer see prompts for basic authentication. This setting reduces the risk of credential theft and enforces more secure authentication methods. <br/><br/> For more information, see [Block basic authentication in Microsoft 365 apps](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-basic-authentication).|
|**Block insecure protocols for file opens**|When users open files from locations using insecure protocols like HTTP or FTP, sensitive data can be exposed because these protocols transmit information in plain text. Blocking these protocols helps prevent attackers from intercepting credentials or other confidential data during file access. When you enable this setting, users are prevented from opening files from locations that use HTTP or FTP. This setting helps enforce secure data transmission practices and reduces exposure to man-in-the-middle attacks. <br/><br/> For more information, see [Block insecure protocols for file opens](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-insecure-protocols-file-opens).|
|**Block FrontPage Remote Procedure Call (FPRPC) protocol for file opens**|FrontPage Remote Procedure Call (FPRPC) is an outdated protocol that was used for remote web page authoring. While no longer widely used, attackers can still exploit FPRPC to execute arbitrary commands or compromise a system through specially crafted files or network traffic. Microsoft 365 apps now block FPRPC by default in favor of HTTPS. Enabling this setting ensures users in your environment can't override the default configuration. <br/><br/> For more information, see [Block FrontPage Server Extensions Remote Procedure Call (FPRPC) for file opens in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-server-extensions-protocol-file-opens).|
|**Block legacy browser authentication connections to SharePoint and OneDrive with legacy Relying Party suite (RPS) protocol**|Legacy protocols are more susceptible to brute-force and phishing attacks. Microsoft reports that organizations that disable legacy authentication experience fewer account compromises. Enforcing this setting prevents applications (including non-Microsoft applications) from using legacy authentication protocols to access SharePoint and OneDrive resources in a browser. <br/><br/> Reporting on this setting shows which users are accessing SharePoint or OneDrive with RPS authentication. The report also lets you know the date and time, and which SharePoint site or OneDrive file or folder they accessed. <br/><br/> **Note**: The change isn't instant. It might take up to 24 hours to be applied. <br/><br/> For more information, see [Set-SPOTenant -LegacyBrowserAuthProtocolsEnabled](https://learn.microsoft.com/en-us/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant#-legacybrowserauthprotocolsenabled). <br/><br/> **Note**: Legacy browser authentication was deprecated for enterprise tenants as of October 2025. This setting is longer available to set to true. The RPS protocol no longer functions.|
|**Block legacy client authentication connections to SharePoint and OneDrive with legacy Identity Client Runtime Library (IDCRL) protocol**|Legacy protocols are more susceptible to brute-force and phishing attacks. Microsoft reports that organizations that disable legacy authentication experience fewer account compromises. Enforcing this setting prevents clients from using legacy authentication protocols from accessing SharePoint and OneDrive resources. <br/><br/>Reporting on this setting shows which users are accessing SharePoint with IDCRL authentication. The reports also let you know the date and time, and which SharePoint site or OneDrive file or folder they accessed. <br/><br/> **Note**: The change isn't instant. It might take up to 24 hours to be applied. <br/><br/> For more information, see [Set-SPOTenant -LegacyAuthProtocolsEnabled](https://learn.microsoft.com/en-us/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant#-legacyauthprotocolsenabled).|
|**Don't allow new custom scripts in SharePoint sites**|Custom scripts are used to modify SharePoint site behaviors. When you allow users to run custom script, you can no longer enforce governance, scope the capabilities of inserted code, block specific parts of code, or block all deployed custom code. This setting permanently removes the ability to add new custom scripts in OneDrive and SharePoint sites. Instead of allowing custom script, use the [SharePoint Framework](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/sharepoint-framework-overview). <br/><br/> For more information, see [Allow or prevent custom script](https://learn.microsoft.com/en-us/sharepoint/allow-or-prevent-custom-script).|
|**Disable Access to Microsoft Store for SharePoint**|Users can install certain applications from the Microsoft Store. Sometimes, this capability can go against organizational policies and can increase governance costs. This setting removes the ability for end users to install applications directly from the Microsoft Store. <br/><br/> For more information, see [Configure settings for the SharePoint store](https://learn.microsoft.com/en-us/sharepoint/configure-sharepoint-store-settings)|
|**Disable organization-wide access to Exchange Web Services (EWS)**|Exchange Web Services (EWS) provides cross-platform API access to sensitive Exchange Online data like emails, meetings, and contacts. If compromised, attackers can access confidential data, send phishing emails, spoof identities and potentially gain system control. When you disable access to EWS, you also reduce legacy app usage and minimize the number of endpoints that attackers can target. EWS is also used in some first party features in both Outlook and the web add-in platform. Web add-ins for Word, Excel, PowerPoint, and Outlook don't work in some builds. <br/><br/> For more information, see [Control access to EWS](https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-control-access-to-ews-in-exchange).|

### Exchange Web Services requirements

Before you disable EWS, make sure that you have the required build to avoid disruption of Office Add-ins. **Build 16.0.19725** is the first build with the baseline security mode feature.

Here's when that build reaches the various update channels:

- Current Channel (CC): Currently available.
- Monthly Enterprise Channel (MEC): Currently available.
- Semi-Annual Enterprise Channel (SAC): July 2026.
- Teams panels: To avoid disruption, update your devices Teams app version 1449/1.0.97.2025120101, which was shipped in September 2025.

> [!NOTE]
>
> These statements and build requirements are for Win32 only.

#### Impact of baseline security mode settings on Authentication

Currently, the following feature doesn't work when you enable baseline security mode settings:

- Certificate Based Authentication for Exchange ActiveSync (legacy Exchange flow, not Microsoft Entra CBA flow).

#### Impact of baseline security mode settings on the Exchange connector across Power Query supported hosts

Currently, the following features don't work when you enable baseline security mode settings:

- Excel for Windows.
- Excel for the web.
- Power BI and Microsoft Fabric - Power BI Desktop, Dataflows (Gen1 and Gen2), Power BI Web Modeling, Power BI Report Server.
- Microsoft Power Platform - Power Platform Dataflows (Standard and Analytical), Dynamics 365 Customer Insights.

#### Impact of baseline security mode settings on cross-tenant features

Currently, the following features don't work when you enable baseline security mode settings:

- Calendar sharing and Free/Busy (cross-tenant/cloud).
- MailTips (cross-tenant/cloud).

#### Impact of baseline security mode on hybrid deployments

- Turn off EWS access only after your hybrid Microsoft Exchange setup supports REST APIs. This change helps reduce legacy app usage and lowers the risk of data exposure.

- Server-side sync between Dynamics on-premises and Exchange Online doesn't work with this setting. To keep using sync features, [Connect Exchange Online to Dynamics 365 Customer Engagement (on-premises)](https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/admin/connect-dynamics-365-on-premises-exchange-online).

## Files

This section outlines the options available within OneDrive and SharePoint to turn off Baseline security mode settings in the Microsoft 365 admin center.

You must be a member of the [SharePoint administrator role](https://learn.microsoft.com/en-us/sharepoint/sharepoint-admin-role) to perform these tasks.

|Setting|More information|
|---|---|
|**Open ancient legacy formats in Protected View and disallow editing**|Ancient legacy file formats in Microsoft 365 apps (formerly Office) are vulnerable to memory corruption. When users open these outdated formats in Protected View with editing disabled, you prevent potential exploits while still allowing users to view the content without risk. <br/><br/> For more information, see [Open ancient legacy formats in Protected View and disallow editing](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/open-ancient-legacy-formats-protected-view-disallow-editing).|
|**Open old legacy formats in Protected View and allow editing**|Many legacy file formats in Microsoft 365 apps (such as older Word, Excel, and PowerPoint files) are prone to memory corruption vulnerabilities. By opening legacy formats in Protected View, you minimize the risk of malicious code execution, while still allowing users to edit their content safely. <br/><br/> For more information, see [Open old legacy formats in Protected View and disallow editing](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/open-old-legacy-formats-protected-view-disallow-editing).|
|**Block ActiveX controls**|ActiveX controls are small programs used to add interactive features to Microsoft 365 documents and web pages. They're highly vulnerable to exploitation. Malicious actors often use ActiveX to run harmful code, install malware, or take control of a system, especially when users open compromised files or visit unsafe websites. Because of their history of security problems and declining usage, Microsoft 365 apps block ActiveX by default. Enforcing this setting ensures users in your environment can't override the default configuration. <br/><br/> For more information, see [Block ActiveX controls in Microsoft 365 apps documents](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-active-x-controls).|
|**Block OLE graph and OrgChart objects**|Block OLE Graph and OrgChart objects. When you turn on this setting, Microsoft 365 apps block loading OLE Graph and OrgChart objects to protect users from known exploitation techniques. <br/><br/> For more information, see [Block OLE Graph and OrgChart objects](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-ole-graph-org-chart-objects).|
|**Dynamic Data Exchange (DDE) server launches are blocked in Excel**|Windows Dynamic Data Exchange (DDE) allows Excel to pull data from external sources in real time. However, if the source is malicious, it can send harmful code to Excel and potentially compromise the system without requiring macros or other active content. Attackers use this technique in targeted phishing attacks to execute arbitrary commands. Blocking DDE server launch reduces this risk. When you enable this setting, Excel blocks DDE server launches, helping prevent malicious external sources from injecting harmful code into spreadsheets. <br/><br/> For more information, see [Block Dynamic Data Exchange (DDE) server launches in Excel](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-dynamic-data-exchange-server-launches-excel).|
|**Block Microsoft Publisher**|Publisher has a large attack surface and won't be included in Microsoft 365 starting in October 2026. Blocking Publisher now reduces security risk and aligns with Microsoft's support strategy. When you enable this setting, Microsoft Publisher doesn't launch. <br/><br/> For more information, see [Block Microsoft Publisher](https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-microsoft-publisher).|

## Room devices

This section outlines the options available within Teams to turn off Baseline security mode settings in the Microsoft 365 admin center.

You must be a member of the [Teams administrator role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) to perform these tasks.

|Setting|More information|
|---|---|
|**Don't allow resource accounts on Teams Rooms devices from accessing Microsoft 365 files**|To increase security, remove resource accounts access that Teams Rooms and devices use to access Microsoft 365 assets for meeting and collaboration. <br/><br/> For more information, see [Set-SPOTenant](https://learn.microsoft.com/en-us/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant) and the [restrict resource account access parameter](https://learn.microsoft.com/en-us/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant#-restrictresourceaccountaccess).|
|**Only allow endpoint managed, compliant devices to sign in**|To increase security, only compliant, organization-managed Teams Rooms devices can sign in to Microsoft 365 applications and resource accounts can't be misused to authenticate from unmanaged devices. <br/><br/> For more information, see [Block Teams resource account sign in to Microsoft 365 clients](https://learn.microsoft.com/en-us/MicrosoftTeams/rooms/block-non-compliant-teams-rooms-devices).|
|**Block unmanaged devices and resource account sign-ins to Microsoft 365 apps**|To increase security, block resource accounts used for Teams devices from being used to sign in to Microsoft 365 clients. <br/><br/> For more information, see [Block Teams resource account sign in to Microsoft 365 clients](https://learn.microsoft.com/en-us/MicrosoftTeams/rooms/block-non-compliant-teams-rooms-devices).|

### Block unmanaged devices and resource account sign-ins to Microsoft 365 apps

|Setting|More information|
|---|---|
|**Don't allow resource accounts on Teams Rooms devices from accessing Microsoft 365 files**|To increase security, remove resource accounts access that Teams Rooms and devices use to access Microsoft 365 assets for meeting and collaboration. <br/><br/> For more information, see [Set-SPOTenant](https://learn.microsoft.com/en-us/powershell/module/microsoft.online.sharepoint.powershell/set-spotenant).|

### Don't allow resource accounts on Teams Rooms devices from accessing Microsoft 365 files

|Setting|More information|
|---|---|
|**Don't allow resource accounts on Teams Rooms devices from accessing Microsoft 365 files**|To increase security, block resource accounts used for Teams devices from being used to sign in to Microsoft 365 clients. <br/><br/> For more information, see [Block Teams resource account sign in to Microsoft 365 clients](https://learn.microsoft.com/en-us/MicrosoftTeams/rooms/block-non-compliant-teams-rooms-devices).|

## Related content

- Learn how [security defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults) and [Microsoft-managed Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies) help protect authentication.
