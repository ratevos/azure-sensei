# Require MFA for all users with Conditional Access

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-mfa-strength  
> Microsoft doc last updated: 03/24/2026


## Overview

As Alex Weinert, the Director of Identity Security at Microsoft, mentions in his blog post [Your Pa$$word doesn't matter](https://techcommunity.microsoft.com/t5/Azure-Active-Directory-Identity/Your-Pa-word-doesn-t-matter/ba-p/731984):

> Your password doesn't matter, but MFA does! Based on our studies, your account is more than 99.9% less likely to be compromised if you use MFA.

## Authentication strength

The guidance in this article helps your organization create an MFA policy for your environment using authentication strengths. Microsoft Entra ID provides three [built-in authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths):

- **Multifactor authentication strength** (less restrictive) recommended in this article
- Passwordless MFA strength
- Phishing-resistant MFA strength (most restrictive)

You can use one of the built-in strengths or create a [custom authentication strength](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-advanced-options) based on the authentication methods you want to require.

For external user scenarios, the MFA authentication methods that a resource tenant can accept vary depending on whether the user is completing MFA in their home tenant or in the resource tenant. For more information, see [Authentication strength for external users](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-external-users).

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Create a Conditional Access policy

The following steps help create a Conditional Access policy to require all users do multifactor authentication, using the authentication strength policy, [without any app exclusions](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#conditional-access-for-all-resources).

> [!WARNING]
> [External authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-external-method-manage) are currently incompatible with authentication strength. You should use the **[Require multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-multifactor-authentication)** grant control.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**
   1. Under **Exclude**: 
      1. Select **Users and groups** 
         1. Choose your organization's emergency access or break-glass accounts.
         1. If you use hybrid identity solutions like Microsoft Entra Connect or Microsoft Entra Connect Cloud Sync, select **Directory roles**, then select **Directory Synchronization Accounts**
      1. You might choose to exclude your guest users if you're targeting them with a [guest user specific policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-guests-mfa-strength). 
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.

   > [!TIP]
   > Microsoft recommends all organizations create a baseline Conditional Access policy that targets: All users, all resources without any app exclusions, and requires multifactor authentication.

1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require authentication strength**, then select the built-in **Multifactor authentication strength** from the list.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

### Named locations

Organizations might choose to incorporate known network locations known as **Named locations** in their Conditional Access policies. These named locations might include trusted IP networks like those for a main office location. For more information about configuring named locations, see the article [What is the location condition in Microsoft Entra Conditional Access?](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-assignment-network#ipv4-and-ipv6-address-ranges)

In the previous example policy, an organization might choose to not require multifactor authentication if accessing a cloud app from their corporate network. In this case they could add the following configuration to the policy:

1. Under **Assignments**, select **Network**.
   1. Configure **Yes**.
   1. Include **Any network or location**.
   1. Exclude **All trusted networks and locations**.
1. **Save** your policy changes.

## Related content

- [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- [Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
- [Windows subscription activation](https://learn.microsoft.com/en-us/windows/deployment/windows-subscription-activation#adding-conditional-access-policy)
- [Configure cross-tenant access settings](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-settings-b2b-collaboration#to-change-inbound-trust-settings-for-mfa-and-device-claims)
