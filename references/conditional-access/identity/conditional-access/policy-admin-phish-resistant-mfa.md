# Require phishing-resistant multifactor authentication for Microsoft Entra administrator roles

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa  
> Microsoft doc last updated: 03/24/2026


## Overview

Accounts with privileged administrative roles are frequent targets of attackers. Requiring phishing-resistant multifactor authentication (MFA) for these accounts reduces the risk of compromise.

> [!CAUTION]
> Before creating a policy requiring phishing-resistant multifactor authentication, make sure your administrators register the appropriate methods. Enabling this policy without completing this step risks locking you out of your tenant. Administrators can [configure Temporary Access Pass to register passwordless authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass) or follow the steps in [register a passkey (FIDO2)](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-register-passkey-with-security-key).

Microsoft recommends requiring phishing-resistant multifactor authentication for at least the following roles:

- Global Administrator
- Application Administrator
- Authentication Administrator
- Billing Administrator
- Cloud Application Administrator
- Conditional Access Administrator
- Exchange Administrator
- Helpdesk Administrator
- Password Administrator
- Privileged Authentication Administrator
- Privileged Role Administrator
- Security Administrator
- SharePoint Administrator
- User Administrator

Organizations can include or exclude roles based on their requirements.

Organizations can use this policy with features like Privileged Identity Management (PIM), which lets you [require MFA for role activation](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#on-activation-require-multifactor-authentication).

## Authentication strength

This article helps your organization create an MFA policy for your environment using authentication strengths. Microsoft Entra ID offers three [built-in authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths):

- Multifactor authentication strength (less restrictive)
- Passwordless MFA strength
- **Phishing-resistant MFA strength** (most restrictive), recommended in this article

Use one of the built-in strengths or create a [custom authentication strength](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-advanced-options) based on the authentication methods you want to require.

For external user scenarios, the MFA authentication methods that a resource tenant accepts vary depending on whether the user completes MFA in their home tenant or in the resource tenant. For more information, see [Authentication strength for external users](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-external-users).

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Create a Conditional Access policy

> [!WARNING]
> If you use [external authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-external-method-manage), these methods are currently incompatible with authentication strengths. Use the **[Require multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-multifactor-authentication)** grant control instead.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Name your policy. Create a meaningful naming standard for your organization's policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **Directory roles** and choose at least the previously listed roles.
   
      > [!WARNING]
      > Conditional Access policies support built-in roles. Conditional Access policies aren't enforced for other role types including [administrative unit-scoped](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal) or [custom roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create).

   1. Under **Exclude**, select **Users and groups**, and choose your organization's emergency access or break-glass accounts.
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require authentication strength**, then select **Phishing-resistant MFA strength** from the list.
   1. Select **Select**.
1. Confirm your settings, and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Related content

- [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
- [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- Learn how to [configure Microsoft Entra role settings in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings).
