# SSO requirements for Microsoft Entra App Gallery

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/app-gallery-sso-requirements  
> Microsoft doc last updated: 08/26/2026


Review these requirements before you validate and publish an application that supports single sign-on (SSO) in Microsoft Entra App Gallery. For requirements that apply to every submission, see [Prerequisites to validate and publish your app](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/v2-howto-app-gallery-listing).

If your application also supports user provisioning, see [User provisioning requirements for Microsoft Entra App Gallery](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/app-gallery-user-provisioning-requirements).

## SAML SSO requirements

These requirements apply to applications that use Security Assertion Markup Language (SAML) 2.0 for SSO.

Your application must meet the following authentication requirements:

- Support the SAML 2.0 protocol in service provider-initiated mode, identity provider-initiated mode, or both. (Required)
- Validate the SAML token certificate key, certificate validity, issuer, audience, and other required user claims. (Required)
- Test your SAML integration with Microsoft Entra ID by using a non-gallery application. (Required)
- Support [SAML Single Logout](https://learn.microsoft.com/en-us/entra/identity-platform/single-sign-out-saml-protocol). (Recommended)
- Retrieve the identity provider SAML federation metadata from the URL that Microsoft Entra ID provides. This approach reduces customer configuration and supports certificate rotation. For more information, see [Certificate rotation guidance](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-manage-certificates-for-federated-single-sign-on#guidance-and-best-practices-for-isvs-on-rotating-certificates). (Recommended)
- Provide a user interface and APIs that customers can use to configure SSO for their application instance. (Recommended)
- Provide a way to enforce SSO for the entire tenant. You can support other authentication options or bypass mechanisms for administrators and emergency access scenarios. (Recommended)

As an independent software vendor (ISV), you must also meet these requirements:

- Publish the application as software as a service (SaaS) in the cloud or distribute it to customers for installation so that customers can own and configure it. (Required)
- Establish engineering and support contacts for App Gallery onboarding and post-onboarding support. (Required)
- Publish documentation for configuring SAML SSO. (Required)
- Meet the compliance requirements for each cloud where you plan to list the application, such as Azure Government or Microsoft Azure operated by 21Vianet. (Required)

## Multitenant OIDC SSO requirements

These requirements apply to applications that use OpenID Connect (OIDC) for SSO.

Your application must meet the following authentication requirements:

- Support OpenID Connect. Use the [OAuth 2.0 authorization code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow). Don't use the [resource owner password credentials flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth-ropc). Use the [device authorization grant flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code) only when your scenario requires it. (Required)
- Use a [multitenant application](https://learn.microsoft.com/en-us/entra/identity-platform/howto-convert-app-to-be-multi-tenant) for a cloud SaaS application. A [single-tenant application](https://learn.microsoft.com/en-us/entra/identity-platform/single-and-multi-tenant-apps) is acceptable when you deploy a separate application instance for each customer by using an infrastructure as a service (IaaS) or platform as a service (PaaS) architecture. (Required)
- Use the Microsoft identity platform v2.0 endpoint for authentication. (Required)
- Request the [least-privileged Microsoft Graph permissions](https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http#best-practices-for-using-microsoft-graph-permissions) for your scenarios. (Required when using Microsoft Graph)
- Use [delegated permissions](https://learn.microsoft.com/en-us/security/zero-trust/develop/developer-strategy-delegated-permission) so that a user or administrator can grant consent. Avoid [application permissions](https://learn.microsoft.com/en-us/security/zero-trust/develop/developer-strategy-application-permissions) unless your scenario requires them. (Required when using Microsoft Graph)
- Use a certificate instead of a client secret when the application uses the client credentials flow. (Required)
- For single-page applications, use the authorization code flow instead of the OAuth 2.0 implicit grant flow. For more information, see [Security concerns with implicit grant flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-implicit-grant-flow#security-concerns-with-implicit-grant-flow). (Recommended)

As an ISV, you must also meet these requirements:

- Publish the application as SaaS in the cloud or distribute it to customers for installation so that customers can own and configure it. (Required)
- Add a **Sign in with Microsoft** button to the sign-in page and follow the [application branding guidelines](https://learn.microsoft.com/en-us/entra/identity-platform/howto-add-branding-in-apps). (Recommended)
- Complete publisher verification by using your Microsoft AI Cloud Partner Program ID. (Required)
- Establish engineering and support contacts for post-onboarding support. (Required)
- Publish documentation for configuring OIDC and OAuth SSO. (Required)
- Meet the compliance requirements for each cloud where you plan to list the application, such as Azure Government or Microsoft Azure operated by 21Vianet. (Required)
- Use a confidential client application. Microsoft Entra App Gallery doesn't onboard public client applications.

## Prepare customer documentation

Publish documentation that includes at least the following information:

- An introduction to your SSO functionality, including supported protocols, versions, SKUs, and identity providers.
- Licensing requirements.
- Roles required to configure SSO.
- SAML configuration steps, including expected values and service provider information.
- OIDC and OAuth permissions with business justifications.
- Testing steps for pilot users.
- Troubleshooting information, including error codes and messages.
- Support options.

## Next steps

- [Validate an OIDC multitenant app](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/validate-oidc-multitenant-app-gallery).
- [Validate a SAML single sign-on app](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/validate-saml-single-sign-on-app-gallery).
- [Publish your app to Microsoft Entra App Gallery](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/publish-app-gallery).
