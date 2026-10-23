# Control security information registration with Conditional Access

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-security-info-registration  
> Microsoft doc last updated: 03/24/2026


## Overview

Securing when and how users register for Microsoft Entra multifactor authentication and self-service password reset is possible with user actions in a Conditional Access policy. This feature is available to organizations who enable [combined registration](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-registration-mfa-sspr-combined). This functionality allows organizations to treat the registration process like any application in a Conditional Access policy and use the full power of Conditional Access to secure the experience. Users signing in to the Microsoft Authenticator app or enabling passwordless phone sign-in are subject to this policy.

> [!IMPORTANT]
> Starting **July 6, 2026**, Conditional Access policies that target **Register security information** will apply during Windows Hello for Business and macOS Platform SSO credential registration. Today, these registration flows don't evaluate registration-targeting Conditional Access policies. However, MFA is still required by default to register passwordless credentials — regardless of whether a Conditional Access policy is configured. After enforcement, users registering Windows Hello for Business or macOS Platform SSO credentials must also satisfy your policy's Grant controls — such as authentication strength, trusted locations, or a specific MFA method — before completing enrollment. Review your policies scoped to **Register security information** and test with report-only mode before enforcement begins.

Some organizations in the past might have used trusted network location or device compliance as a means to secure the registration experience. With the addition of [Temporary Access Pass](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass) in Microsoft Entra ID, administrators can provide time-limited credentials to their users that allow them to register from any device or location. Temporary Access Pass credentials satisfy Conditional Access requirements for multifactor authentication.

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Create a policy to secure registration

The following policy applies to the selected users, who attempt to register using the combined registration experience. The policy requires users who are not on a trusted network to do multifactor authentication. Users from trusted networks are excluded from this policy.

> [!WARNING]
> If you use [external authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-external-method-manage), these are currently incompatible with authentication strength and you should use the **[Require multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-multifactor-authentication)** grant control.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. In Name, Enter a Name for this policy. For example, **Combined Security Info Registration with TAP**.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.

      > [!WARNING]
      > Users must be enabled for the [combined registration](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-registration-mfa-sspr-combined).

   1. Under **Exclude**.
      1. Select **All guest and external users**.
      
         > [!NOTE]
         > Temporary Access Pass does not work for guest users.

      1. Select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
1. Under **Target resources** > **User actions**, check **Register security information**.
1. Under **Conditions** > **Locations**. 
   1. Set **Configure** to **Yes**. 
      1. Include **Any location**.
      1. Exclude **All trusted locations**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require authentication strength**, then select the appropriate built-in or custom authentication strength from the list.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

Administrators have to issue Temporary Access Pass credentials to new users so they can satisfy the requirements for multifactor authentication to register. Steps to accomplish this task, are found in the section [Create a Temporary Access Pass in the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass#create-a-temporary-access-pass).

Organizations might choose to require other grant controls with or in place of **Require multifactor authentication** at step 8a. When selecting multiple controls, be sure to select the appropriate radio button toggle to require **all** or **one** of the selected controls when making this change.

### Guest user registration

For [guest users](https://learn.microsoft.com/en-us/entra/external-id/what-is-b2b) who need to register for multifactor authentication in your directory you might choose to block registration from outside of [trusted network locations](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions#locations) using the following guide.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. In Name, Enter a Name for this policy. For example, **Combined Security Info Registration on Trusted Networks**.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All guest and external users**.
1. Under **Target resources** > **User actions**, check **Register security information**.
1. Under **Conditions** > **Locations**.
   1. Configure **Yes**.
   1. Include **Any location**.
   1. Exclude **All trusted locations**.
1. Under **Access controls** > **Grant**.
   1. Select **Block access**.
   1. Then choose **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Related content

- [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
- [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- [Require users to reconfirm authentication information](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks#reconfirm-authentication-information)
