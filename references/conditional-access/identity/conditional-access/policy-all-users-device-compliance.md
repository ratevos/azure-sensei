# How to Require Device Compliance with Conditional Access

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-compliance  
> Microsoft doc last updated: 03/24/2026


## Overview

Microsoft Intune and Microsoft Entra work together to secure your organization through [device compliance policies](https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started) and Conditional Access. Device compliance policies ensure user devices meet minimum configuration requirements. The requirements can be enforced when users access services protected with Conditional Access policies.

Some organizations might not be ready to require device compliance for all users. These organizations might instead choose to deploy the following policies: 

- [Require a compliant or Microsoft Entra hybrid joined device for administrators](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-admin-device-compliand-hybrid)
- [Require a compliant device, Microsoft Entra hybrid joined device, **OR** multifactor authentication for all users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-all-users-compliant-hybrid-or-mfa)
- [Block unknown or unsupported device platforms](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-unknown-unsupported)
- [Disable browser persistence](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-persistent-browser)

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Create a Conditional Access policy

The following steps help create a Conditional Access policy to require devices accessing resources be marked as compliant with your organization's [Intune compliance policies](https://learn.microsoft.com/en-us/mem/intune/protect/create-compliance-policy). 

> [!WARNING]
> Without a compliance policy created in Microsoft Intune, this Conditional Access policy won't function as intended. Create a compliance policy first and ensure you have at least one compliant device before proceeding.

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
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Access controls** > **Grant**.
   1. Select **Require device to be marked as compliant**.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!NOTE]
> You can enroll your new devices to Intune even if you select **Require device to be marked as compliant** for **All users** and **All resources (formerly 'All cloud apps')** using the previous steps. The **Require device to be marked as compliant** control doesn't block Intune enrollment. 
>
> Similarly, the **Require device to be marked as compliant** doesn't block Microsoft Authenticator app access to the UserAuthenticationMethod.Read scope. Authenticator needs access to the UserAuthenticationMethod.Read scope during Authenticator registration to determine which credentials a user can configure. Authenticator needs access to UserAuthenticationMethod.ReadWrite to register credentials, which doesn't bypass the **Require device to be marked as compliant** check.

### Known behavior

On iOS, Android, macOS, and some non-Microsoft web browsers, Microsoft Entra ID identifies the device using a client certificate that is provisioned when the device is registered with Microsoft Entra ID. When a user first signs in through the browser the user is prompted to select the certificate. The end user must select this certificate before they can continue to use the browser.

### B2B scenarios

For organizations you have a relationship with and trust, you might trust their device compliance claims. To configure this setting, see the article [Manage cross-tenant access settings for B2B collaboration](../../external-id/cross-tenant-access-settings-b2b-collaboration.yml#to-change-inbound-trust-settings-for-mfa-and-device-claims).

### Subscription activation

Organizations that use the [Subscription Activation](https://learn.microsoft.com/en-us/windows/deployment/windows-10-subscription-activation) feature to enable users to "step-up" from one version of Windows to another, might want to exclude the Windows Store for Business, AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f from their device compliance policy.

## Related content

- Learn how to [create a compliance policy in Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/protect/create-compliance-policy).
- Learn about [Conditional Access grant controls](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-device-to-be-marked-as-compliant).
- Learn how to [configure cross-tenant access settings](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-settings-b2b-collaboration#to-change-inbound-trust-settings-for-mfa-and-device-claims).
