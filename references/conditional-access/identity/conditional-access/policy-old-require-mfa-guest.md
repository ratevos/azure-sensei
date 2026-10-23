# Require MFA for guest users with Conditional Access

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-guest  
> Microsoft doc last updated: 03/24/2026


## Overview

> [!WARNING]
> This article describes a Conditional Access policy that uses the **Require multifactor authentication** grant control. For external users who authenticate with Microsoft Entra ID, consider using **authentication strength** policies to specify which MFA methods are accepted. For more information, see [Require multifactor authentication strength for external users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-guests-mfa-strength). Authentication strength policies don't apply to email one-time passcode, SAML/WS-Fed, or Google federation users — for those scenarios, continue using the **Require multifactor authentication** grant control.

Require guest users perform multifactor authentication when accessing your organization's resources. Some organizations might be ready to move to stronger authentication methods for their guest users. These organizations might choose to implement a policy like the one described in the article [Require multifactor authentication strength for external users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-guests-mfa-strength).

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Create a Conditional Access policy

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All guest and external users**
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.
   1. Under **Exclude**, select any applications that don't require multifactor authentication.
1. Under **Access controls** > **Grant**, select **Grant access**, **Require multifactor authentication**, and select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Related content

[Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)

[Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
