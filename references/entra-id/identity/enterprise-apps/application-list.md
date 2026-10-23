# Viewing apps using your tenant for identity management

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/application-list  
> Microsoft doc last updated: 07/14/2023


The [Quickstart Series on Application Management](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/view-applications-portal) walks you the basics. In it, you learn how to view all of the apps using your Microsoft Entra tenant for identity management. This article dives a bit deeper into the types of apps you'll find.

## Why does a specific application appear in my all applications list?

When filtered to **All Applications**, the **All Applications** **List** shows every Service Principal object in your tenant. Service Principal objects can appear in this list in a various ways:

- When you add any application from the application gallery, including:

  - **Microsoft Entra ID - Enterprise applications** – Apps added to your tenant using the **Enterprise applications** option on the Microsoft Entra admin center. Usually apps integrated using the SAML standard.
  - **Microsoft Entra ID - App registrations** – Apps added to your tenant using the **App registrations** option on the Microsoft Entra admin center. Usually custom developed apps using the OpenID Connect and OAuth standards.
  - **Application Proxy Applications** – An application running in your on-premises environment that you want to provide secure single-sign on to externally
- When signing up for, or signing in to, a third-party application integrated with Microsoft Entra ID. One example is [Smartsheet](https://app.smartsheet.com/b/home) or [DocuSign](https://www.docusign.net/member/MemberLogin.aspx).
- Microsoft apps such as Microsoft 365.
- When you use managed identities for Azure resources. For more information, see [Managed identity types](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview#managed-identity-types).
- When you add a new application registration by creating a custom-developed application using the [Application Registry](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)
- When you add a new application registration by creating a custom-developed application using the [V2.0 Application Registration portal](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)
- When you add an application, you’re developing using Visual Studio’s [ASP.NET authentication methods](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?tabs=visual-studio) or [Connected Services](https://devblogs.microsoft.com/visualstudio/connecting-to-cloud-services/)
- When you create a service principal object using the [Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation) module.
- When you [consent to an application](https://learn.microsoft.com/en-us/entra/identity-platform/howto-convert-app-to-be-multi-tenant) as an administrator to use data in your tenant
- When a [user consents to an application](https://learn.microsoft.com/en-us/entra/identity-platform/howto-convert-app-to-be-multi-tenant) to use data in your tenant
- When you enable certain services that store data in your tenant. One example is Password Reset, which is modeled as a service principal to store your password reset policy securely.

Learn more about how, and why, apps are added to your directory, see [How applications are added to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-applications-are-added).

## Next steps

[Managing Applications with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-application-management)
