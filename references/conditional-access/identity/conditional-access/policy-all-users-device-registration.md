# Require MFA for device registration

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-registration  
> Microsoft doc last updated: 03/24/2026


## Overview

Use the [Conditional Access user action](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#user-actions) to enforce policy when users register or join devices to Microsoft Entra ID. This control provides granularity in configuring multifactor authentication for registering or joining devices instead of a tenant-wide policy that currently exists. Administrators can customize this policy to fit the security needs of their organization.

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Create a Conditional Access policy

> [!WARNING]
> If you use [external authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-external-method-manage), these methods are currently incompatible with authentication strength and you should use the **[Require multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-multifactor-authentication)** grant control.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts.
1. Under **Target resources** > **User actions**, select **Register or join devices**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require authentication strength**, then select the built-in **Multifactor authentication** authentication strength from the list.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!WARNING]
> When a Conditional Access policy is configured with the **Register or join devices** user action, you must set **Entra ID** > **Devices** > **Overview** > **Device Settings** - `Require Multifactor Authentication to register or join devices with Microsoft Entra` to **No**. Otherwise, Conditional Access policies with this user action aren't properly enforced. More information about this device setting can found in [Configure device settings](https://learn.microsoft.com/en-us/entra/identity/devices/manage-device-identities#configure-device-settings).
> 
> 

## Related content

- [Conditional Access authentication strength](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths)
- [Determine effect using Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)
- [Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
- [Manage device identities using the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/identity/devices/manage-device-identities)
