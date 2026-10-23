# Sign-in risk-based multifactor authentication

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-sign-in  
> Microsoft doc last updated: 03/24/2026


## Overview

Most users have normal behavior that can be tracked. When their behavior falls outside this norm, it might be risky to let them sign in. You might want to block the user or ask them to complete multifactor authentication to confirm their identity. 

Sign-in risk represents the likelihood that an authentication request isn't from the identity owner. Organizations with Microsoft Entra ID P2 licenses can create Conditional Access policies incorporating [Microsoft Entra ID Protection sign-in risk detections](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks). 

The sign-in risk-based policy prevents users from registering MFA during risky sessions. If users aren't registered for MFA, their risky sign-ins are blocked, and they receive an AADSTS53004 error.

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Enable with Conditional Access policy

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **New policy**.
1. Give your policy a name. We recommend that organizations create a meaningful standard for the names of their policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
   1. Select **Done**.
1. Under **Cloud apps or actions** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Conditions** > **Sign-in risk**, set **Configure** to **Yes**. 
   1. Under **Select the sign-in risk level this policy will apply to**, select **High** and **Medium**. [This guidance is based on Microsoft recommendations and might be different for each organization](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#choosing-acceptable-risk-levels)
   1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require authentication strength**, then select the built-in **Multifactor authentication** authentication strength from the list.
   1. Select **Select**.
1. Under **Session**.
   1. Select **Sign-in frequency**.
   1. Ensure **Every time** is selected.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to create to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

### Passwordless scenarios

For organizations that adopt [passwordless authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-passwordless-deployment) make the following changes: 

#### Update your passwordless sign-in risk policy

1. Under **Users**:
   1. **Include**, select **Users and groups** and target your passwordless users.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts.
   1. Select **Done**.
1. Under **Cloud apps or actions** > **Include**, select **All resources** (formerly 'All cloud apps').
1. Under **Conditions** > **Sign-in risk**, set **Configure** to **Yes**.
    1. Under **Select the sign-in risk level this policy will apply to**, select **High** and **Medium**. For more information on risk levels, see [Choosing acceptable risk levels](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#choosing-acceptable-risk-levels).
    1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Grant access**.
    1. Select **Require authentication strength**, then select the built-in **Passwordless MFA** or **Phishing-resistant MFA** based on which method the targeted users have.
    1. Select **Select**.
1. Under **Session**:
    1. Select **Sign-in frequency**.
    1. Ensure **Every time** is selected.
    1. Select **Select**.

## Related content

- [Require reauthentication every time](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-session-lifetime#require-reauthentication-every-time)
- [Remediate risks and unblock users](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock)
- [Conditional Access common policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- [User risk-based Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user)
- [Determine effect using Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)
- [Use report-only mode for Conditional Access to determine the results of new policy decisions](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
- [Configure cross-tenant access settings](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-settings-b2b-collaboration#to-change-inbound-trust-settings-for-mfa-and-device-claims)
