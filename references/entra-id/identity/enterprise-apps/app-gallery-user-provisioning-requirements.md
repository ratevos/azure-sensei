# User provisioning requirements for Microsoft Entra App Gallery

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/app-gallery-user-provisioning-requirements  
> Microsoft doc last updated: 08/26/2026


Review these requirements before you validate and publish an application that supports user provisioning in Microsoft Entra App Gallery. For requirements that apply to every submission, see [Prerequisites to validate and publish your app](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/v2-howto-app-gallery-listing).

If your application also supports SSO, see [SSO requirements for Microsoft Entra App Gallery](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/app-gallery-sso-requirements).

## SCIM API requirements

Your System for Cross-Domain Identity Management (SCIM) API must meet the following requirements:

- Support a SCIM 2.0 user and group endpoint. User provisioning is required. Group provisioning is recommended. (Required)
- Support at least 25 requests per second per tenant so that users and groups are provisioned and deprovisioned without delay. (Required)
- Validate and test user and group provisioning by using a [non-gallery application](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups#getting-started). (Required)
- Validate client credentials authentication or another supported authentication method by using a [non-gallery application](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups#getting-started). (Required)
- Support soft delete or hard delete for users. You can support both methods. (Required)
- Return a successful response with zero results when a query doesn't match a user. Don't return a bad request. (Required)
- Support schema discovery on the SCIM endpoint. (Required)
- Support updating multiple group memberships with a single `PATCH` request. (Recommended)
- Support SCIM bulk APIs to improve connector performance. (Recommended)

## SCIM authentication requirements

Use OAuth 2.0 client credentials or workload identity federation to authenticate the Microsoft Entra provisioning service to your SCIM endpoint. Microsoft doesn't onboard SCIM provisioning applications that use basic authentication, long-lived bearer tokens, or the authorization code grant flow.

### OAuth 2.0 client credentials

If you use OAuth 2.0 client credentials, meet these requirements:

- Provide customers with a client ID, client secret, token endpoint, and SCIM endpoint. (Required)
- Set the client secret to expire after one to three years. Don't issue an access token when the credentials are expired. (Required)
- Enable smooth secret rotation by allowing multiple active secrets and deletion of old secrets. Alternatively, let customers create a new client ID and client secret. (Required)
- Set access tokens to expire between 60 minutes and six hours after issuance. (Required)

For implementation guidance, see [OAuth 2.0 client credentials grant flow](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups#oauth-20-client-credentials-grant-flow).

### Workload identity federation

Workload identity federation lets the Microsoft Entra provisioning service authenticate to your SCIM endpoint without storing a long-lived secret. Microsoft Entra ID presents a signed JSON Web Token (JWT) assertion to your token endpoint by using the OAuth 2.0 JWT bearer profile in [RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523). Your token endpoint validates the assertion and returns a short-lived access token for the SCIM endpoint.

To support workload identity federation, validate Microsoft Entra-issued JWTs against Microsoft's published JSON Web Key Set and issue access tokens scoped to your SCIM endpoint. For the configuration flow, token claims, and implementation requirements, see [Workload identity federation for SCIM provisioning](https://github.com/AzureAD/SCIMReferenceCode/blob/master/Workload-Identity-Federation-for-SCIM-Provisioning.md). (Recommended)

## ISV requirements

As an independent software vendor (ISV), you must meet these requirements:

- Establish engineering and support contacts for App Gallery onboarding, post-onboarding support, and future communication from Microsoft. (Required)
- Publish documentation for your SCIM endpoint. (Required)
- Deploy your SCIM provisioning integration to at least 100 mutual customers by using the Microsoft Entra non-gallery approach.
- Meet the compliance requirements for each cloud where you plan to list the application, such as Azure Government or Microsoft Azure operated by 21Vianet. (Required)

## Known limitations

Review [Known issues for application provisioning](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/known-issues.md?pivots=app-provisioning) before submitting your integration.

## Validate your integration

After your SCIM endpoint meets these requirements, validate it against the Microsoft Entra provisioning service and submit the results with your gallery submission. For instructions, see [Validate user provisioning for Microsoft Entra App Gallery](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/validate-user-provisioning-app-gallery).

## Prepare customer documentation

Publish documentation that includes at least the following information:

- An introduction to your provisioning functionality.
- Licensing requirements.
- Roles required to configure provisioning.
- Your SCIM endpoint and supported resources and attributes.
- Authentication setup and credential rotation instructions.
- Testing steps for pilot users.
- Troubleshooting information, including error codes and messages.
- Support options.

## Next steps

- [Build a SCIM endpoint and configure user provisioning](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups).
- [Publish your app to Microsoft Entra App Gallery](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/publish-app-gallery).
