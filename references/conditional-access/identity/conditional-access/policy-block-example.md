# Conditional Access - Block access

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-example  
> Microsoft doc last updated: 03/24/2026


## Overview

For organizations with a conservative cloud migration approach, the block all policy is an option that can be used. 

> [!CAUTION]
> Misconfiguration of a block policy can lead to organizations being locked out.

Policies like these can have unintended side effects. Proper testing and validation are vital before enabling. Administrators should utilize tools such as [Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) and [the What If tool in Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) when making changes.

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Create a Conditional Access policy

The following steps help create Conditional Access policies to block access to all apps except for [Office 365](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#office-365) (Microsoft 365) if users aren't on a trusted network. These policies are put in to [Report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting) to start so administrators can determine the impact on existing users. When administrators are comfortable that the policies apply as they intend, they can switch them to **On**.

The first policy blocks access to all apps except for Microsoft 365 applications if not on a trusted location.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
1. Under **Target resources** > **Resources (formerly cloud apps)**, select the following options:
   1. Under **Include**, select **All resources (formerly 'All cloud apps')**.
   1. Under **Exclude**, select **Office 365**, select **Select**.
1. Under **Conditions**:
   1. Under **Conditions** > **Location**.
      1. Set **Configure** to **Yes**
      1. Under **Include**, select **Any location**.
      1. Under **Exclude**, select **All trusted locations**.
   1. Under **Client apps**, set **Configure** to **Yes**, and select **Done**.
1. Under **Access controls** > **Grant**, select **Block access**, then select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

The following policy is created to require multifactor authentication or a compliant device for users of Microsoft 365.

1. Select **Create new policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include** > **Select resources**, choose **Office 365**, and select **Select**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require multifactor authentication** and **Require device to be marked as compliant** select **Select**.
   1. Ensure **Require one of the selected controls** is selected.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!NOTE]
> Conditional Access policies are enforced after first-factor authentication is completed. Conditional Access isn't intended to be an organization's first line of defense for scenarios like denial-of-service (DoS) attacks, but it can use signals from these events to determine access.

## Related content

[Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)

[Determine effect using Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)

[Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
