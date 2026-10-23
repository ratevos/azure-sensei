# App support for SMS-based authentication in Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-sms-supported-apps  
> Microsoft doc last updated: 03/04/2025


SMS-based authentication is available to Microsoft apps integrated with the Microsoft identity platform (Microsoft Entra ID). This article lists the web and mobile apps that support SMS-based authentication.

## Move to modern, phishing-resistant authentication

> [!IMPORTANT]
> Microsoft recommends phishing-resistant authentication methods for improved security. Consider migrating users to one of the following methods:
>
> - [Passkeys (FIDO2)](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2)
> - [Windows Hello for Business](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/hello-overview)
> - [Certificate-based authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication)

SMS-based authentication is available to Microsoft apps integrated with the Microsoft identity platform (Microsoft Entra ID). The table lists some of the web and mobile apps that support SMS-based authentication. If you would like to add or validate any app, [contact us](https://feedback.azure.com/d365community/forum/22920db1-ad25-ec11-b6e6-000d3a4f0789).

| App | Web/browser app | Native mobile app |
| --- |:---:|:---:|
| Office 365- Microsoft Online Services* | ● |   |
| Microsoft One Note | ● |   |
| Microsoft Teams | ● | ● |
| Company portal | ● | ● |
| My Apps portal | ● |Not available|
| Microsoft Forms | ● |Not available|
| Microsoft Edge | ● |   |
| Microsoft Power BI | ● |   |
| Microsoft Stream | ● |   |
| Microsoft Power Apps | ● |   |
| Microsoft Azure | ● | ● |
| Azure Virtual Desktop | ● |  | 

*_SMS sign-in isn't available for office applications, such as Word, Excel, etc., when accessed directly on the web, but is available when accessed through the [Office 365 web app](https://www.office.com)_

The above mentioned Microsoft apps support SMS sign-in is because they use the Microsoft Identity login (`https://login.microsoftonline.com/`), which allows users to enter phone number and SMS code.

## Unsupported Microsoft apps

Microsoft 365 desktop (Windows or Mac) apps and Microsoft 365 web apps (except MS One Note) that are accessed directly on the web don't support SMS sign-in. These apps use the Microsoft Office login (`https://office.live.com/start/*`) that requires a password to sign in.
For the same reason, Microsoft Office mobile apps (except Microsoft Teams, Company portal, and Microsoft Azure) don't support SMS sign-in.

| Unsupported Microsoft apps| Examples |
| --- | --- |
| Native desktop Microsoft apps | Microsoft Teams, Microsoft 365 apps, Word, Excel, and so on.|
| Native mobile Microsoft apps (except Microsoft Teams, Company portal, and Microsoft Azure) | Outlook, Edge, Power BI, Stream, SharePoint, Power Apps, Word, and so on.|
| Microsoft 365 web apps (accessed directly on web) | [Outlook](https://outlook.live.com/owa/), [Word](https://office.live.com/start/Word.aspx), [Excel](https://office.live.com/start/Excel.aspx), [PowerPoint](https://office.live.com/start/PowerPoint.aspx)|  

## Support for Non-Microsoft apps 

To make Non-Microsoft apps compatible with the SMS sign-in feature: 
- Integrate Non-Microsoft web apps with Microsoft Entra ID and use Microsoft Entra authentication. Use Security Assertion Markup Language [SAML](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso) or OpenID Connect [OIDC](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-oidc-sso) to integrate with Microsoft Entra SSO. 
- Integrate Non-Microsoft on-premises apps with Microsoft Entra ID using [Microsoft Entra application proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy/application-proxy-add-on-premises-application)
- Integrate Non-Microsoft client apps with [Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview) for authentication 
    - [Sample app iOS](https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-ios)
    - [Sample app Android](https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-android)

## Next steps

- [How to enable SMS-based sign-in for users](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-sms-signin)
- See the following links to enable SMS sign-in for native mobile apps using MSAL Libraries: 
  - [iOS](https://github.com/AzureAD/microsoft-authentication-library-for-objc)
  - [Android](https://github.com/AzureAD/microsoft-authentication-library-for-android)
- [Integrate SAAS application with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/saas-apps/tutorial-list)

## Recommended content

- [Add an application to your Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal)
- [Overview of MSAL libraries to acquire token from Microsoft identity platform to authenticate users](https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview)
- [Configure Microsoft Managed Home Screen with Microsoft Entra ID](https://learn.microsoft.com/en-us/mem/intune/apps/app-configuration-managed-home-screen-app)
