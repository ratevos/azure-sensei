# Microsoft traffic Conditional Access policies

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-microsoft-profile  
> Microsoft doc last updated: 03/25/2026


## Overview

You apply Conditional Access policies to Global Secure Access traffic. With Conditional Access, you can require multifactor authentication and device compliance for accessing Microsoft resources. 

This article describes how to apply Conditional Access policies to your Global Secure Access internet traffic.

## Prerequisites

* Administrators who interact with **Global Secure Access** features must have one or more of the following role assignments depending on the tasks they're performing.
   * The [Global Secure Access Administrator role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator) role to manage the Global Secure Access features.
   * The [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) role to create and interact with Conditional Access policies.
* The product requires licensing. For details, see the licensing section of [What is Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).

## Create a Conditional Access policy targeting Global Secure Access internet traffic

### Example policy

The following example policy targets all users except for your break-glass accounts and guest/external users, requiring multifactor authentication, device compliance, or a Microsoft Entra hybrid joined device for Global Secure Access internet traffic.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **Create new policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select the **Users and groups** link.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**:
      1. Select **Users and groups** and choose your organization's [emergency access or break-glass accounts](#user-exclusions).
      1. Select **Guest or external users** and select all checkboxes.
1. Under **Target resources** > **Resources (formerly cloud apps)**.
   1. Choose **All internet resources with Global Secure Access**.

   

   > [!NOTE]
   > To only enforce the *Internet Access traffic forwarding profile* and **not** the *Microsoft traffic forwarding profile* then choose **Select resources** and select **Internet resources** from the app picker and configure a security profile. 

1. Under **Access controls** > **Grant**.
   1. Select **Require multifactor authentication**, **Require device to be marked as compliant**, and **Require Microsoft Entra hybrid joined device**
   1. **For multiple controls** select **Require one of the selected controls**.
   1. Select **Select**.

After administrators confirm the policy settings using [report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only), an administrator can move the **Enable policy** toggle from **Report-only** to **On**.

### User exclusions

Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Next steps

The next step for getting started with Microsoft Entra Internet Access is to [review the Global Secure Access logs](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-global-secure-access-logs-monitoring).

For more information about traffic forwarding, see the following articles:

- [Learn about traffic forwarding profiles](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding)
- [Manage the Microsoft traffic profile](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-microsoft-profile)
