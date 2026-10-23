# Block access for users with elevated insider risk

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-insider-block  
> Microsoft doc last updated: 03/24/2026


## Overview

Most users have a normal behavior that can be tracked, when they fall outside of this norm it could be risky to allow them to just sign in. You might want to block that user or ask them to review a specific [terms of use policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/terms-of-use). Microsoft Purview can provide an [insider risk signal](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions#insider-risk) to Conditional Access to refine access control decisions. Insider risk management is part of [Microsoft Purview](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection). You must enable it before you can use the signal in Conditional Access.

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Block access with Conditional Access policy

> [!TIP]
> Configure [adaptive protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) before you create the following policy.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**:
      1. Select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
      1. Select **Guest or external users** and choose the following:
         1. **B2B direct connect users**.
         1. **Service provider users**.
         1. **Other external users**.
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Conditions** > **Insider risk**, set **Configure** to **Yes**. 
   1. Under **Select the risk levels that must be assigned to enforce the policy**. 
      1. Select **Elevated**.
      1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Block access**, then select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

Some administrators might create other Conditional Access policies that use other access controls, like terms of use on lower levels of insider risk.

## Related content

- [Dynamically mitigate risks with adaptive protection](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection)
- [Insider risk as a condition](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions#insider-risk)
- [Determine effect using Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)
- [Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
