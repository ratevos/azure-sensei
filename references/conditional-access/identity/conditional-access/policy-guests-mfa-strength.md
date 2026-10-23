# Conditional Access - Authentication strength for external users

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-guests-mfa-strength  
> Microsoft doc last updated: 03/24/2026


## Overview

Authentication strength is a Conditional Access control that lets you define a specific combination of multifactor authentication (MFA) methods that an external user must complete to access your resources. This control is especially useful for restricting external access to sensitive apps in your organization. For example, you can create a Conditional Access policy, require a phishing-resistant authentication strength in the policy, and assign it to guests and external users.

Microsoft Entra ID provides three [built-in authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths):

- **Multifactor authentication strength** (less restrictive) recommended in this article
- Passwordless MFA strength
- Phishing-resistant MFA strength (most restrictive)

You can use one of the built-in strengths or create a [custom authentication strength](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-advanced-options) based on the authentication methods you want to require.

In external user scenarios, the MFA authentication methods that a resource tenant can accept vary depending on whether the user is completing MFA in their home tenant or in the resource tenant. For details, see [Authentication strength for external users](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-external-users).

> [!NOTE]
> Currently, you can only apply authentication strength policies to external users who authenticate with Microsoft Entra ID. For email one-time passcode, SAML/WS-Fed, Google federation, and Microsoft personal (MSA) users, use the [MFA grant control](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-multifactor-authentication) to require MFA.

## Configure cross-tenant access settings to trust MFA

Authentication strength policies work together with [MFA trust settings](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-settings-b2b-collaboration.yml#to-change-inbound-trust-settings-for-mfa-and-device-claims) in your cross-tenant access settings to determine where and how the external user must perform MFA. A Microsoft Entra user first authenticates with their own account in their home tenant. Then when this user tries to access your resource, Microsoft Entra ID applies the authentication strength Conditional Access policy and checks to see if you enabled MFA trust.

- **If MFA trust is enabled**, Microsoft Entra ID checks the user's authentication session for a claim indicating that MFA was fulfilled in the user's home tenant.
- **If MFA trust is disabled**, the resource tenant presents the user with a challenge to complete MFA in the resource tenant using an acceptable authentication method.

The authentication methods that external users can use to satisfy MFA requirements are different depending on whether the user is completing MFA in their home tenant or the resource tenant. See the table in [Conditional Access authentication strength](https://aka.ms/b2b-auth-strengths).

> [!IMPORTANT]
> Before you create the Conditional Access policy, check your cross-tenant access settings to make sure your inbound MFA trust settings are configured as intended.

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Create a Conditional Access policy

Use the following steps to create a Conditional Access policy that applies an authentication strength to external users.

> [!WARNING]
> If you use [external authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-external-method-manage), these are currently incompatible with authentication strength and you should use the **[Require multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-multifactor-authentication)** grant control.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, choose **Select users and groups**, and then select **Guest or external users**.
      1. Select the types of [guest or external users](https://learn.microsoft.com/en-us/entra/external-id/authentication-conditional-access#assign-conditional-access-policies-to-external-user-types) you want to apply the policy to.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts.
1. Under **Target resources** > **Resources (formerly cloud apps)**, under **Include** or **Exclude**, select any applications you want to include in or exclude from the authentication strength requirements.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require authentication strength**, then select the appropriate built-in or custom authentication strength from the list.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Related content

- [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- [Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
- [Configure cross-tenant access settings](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-settings-b2b-collaboration#to-change-inbound-trust-settings-for-mfa-and-device-claims)
