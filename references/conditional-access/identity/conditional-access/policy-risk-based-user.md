# Require remediation for risky users

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user  
> Microsoft doc last updated: 03/24/2026


## Overview

Organizations with Microsoft Entra ID P2 licenses can create Conditional Access policies incorporating [Microsoft Entra ID Protection user risk detections](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks). This policy enables end users to self-remediate and unblock themselves, increasing their productivity while reducing incidents sent to your help desk or security operations teams.  

## User exclusions

Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Require risk remediation

This risk remediation policy covers both password-based and passwordless users.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **New policy**.
1. Give your policy a name. We recommend that organizations create a meaningful standard for the names of their policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
   1. Select **Done**.
1. Under **Target resources** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Conditions** > **User risk**, set **Configure** to **Yes**. 
   1. Under **Configure user risk levels needed for policy to be enforced**, select **High**. [This guidance is based on Microsoft recommendations and might be different for each organization](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#choosing-acceptable-risk-levels)
   1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require risk remediation**. The **Require authentication strength** grant control is automatically selected. Choose the strength appropriate for your organization.
   1. Select **Select**.
1. Under **Session**, **Sign-in frequency - Every time** is automatically applied as a session control and is mandatory.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to create your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Related content

- [Require reauthentication every time](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-session-lifetime#require-reauthentication-every-time)
- [Remediate risks and unblock users](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock)
- [Conditional Access common policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- [Sign-in risk-based Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-sign-in)
- [Determine effect using Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)
- [Use report-only mode for Conditional Access to determine the results of new policy decisions](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
