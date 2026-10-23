# Set the password expiration policy for your organization

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/set-password-expiration-policy  
> Microsoft doc last updated: 03/13/2026


This article is for people who set password expiration policies for organizations, such as a business, school, or nonprofit organization, using Microsoft 365 for business.

As a user administrator, you can make user passwords expire after a certain number of days, or set passwords to never expire. **By default, passwords never expire for your organization**.

To avoid security risks associated with users setting weak passwords or reusing old passwords, enable [multifactor authentication](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication). See [Password policy recommendations](https://learn.microsoft.com/en-us/microsoft-365/admin/misc/password-policy-recommendations).

## Before you begin

You must be a [user administrator](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles) to perform these steps.

## Set password expiration policy

To set user passwords to expire after a set amount of time, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Org Settings**](https://go.microsoft.com/fwlink/p/?linkid=2053743).

   If you don't have an appropriate role assigned, you won't see the **Org Settings** option. In this case, [Check administrator roles in your organization](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/assign-admin-roles#check-administrator-roles-in-your-organization).

1. In the **Org Settings** page, select the [**Security and Privacy**](https://go.microsoft.com/fwlink/p/?linkid=2072756) tab.

1. In the **Security and Privacy** tab, select **Password expiration policy**.

1. In the **Password expiration policy** pane, clear the check box **Set passwords to never expire (recommended)**.

1. In the **Days before passwords expire** text box, enter how often passwords should expire. Choose a number of days from **14 to 730**, and then select **Save**.

> [!IMPORTANT]
> The Microsoft 365 admin center and Microsoft 365 productivity apps no longer support password expiration notifications.

## Important things you need to know about the password expiration feature

People who only use the Outlook app aren't forced to reset their Microsoft 365 password until it expires in the cache. This process can take days after the actual expiration date. There's no workaround for this configuration at the admin level.

## Prevent last password from being used again

To prevent users from recycling old passwords, enforce password history in Active Directory (AD). For more information, see [Create a custom password policy](https://learn.microsoft.com/en-us/azure/active-directory-domain-services/password-policy#create-a-custom-password-policy).

In Microsoft Entra ID, users can't reuse their last password when they change a password. This password policy applies to all user accounts that you create and manage directly in Entra ID, and it can't be modified. For more information, see [Microsoft Entra password policies](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-sspr-policy#password-policies-that-only-apply-to-cloud-user-accounts).

## New and federated domains

Set password policies for each managed domain in your organization. If you add a new domain or convert a domain from *federated* to *managed*, re-enable the organization password policy to update all domains. Otherwise, the new or converted domain keeps the default policy.

## Synchronize user password hashes from on-premises Active Directory to Microsoft Entra ID

This article explains how to set the expiration policy for cloud-only users (Microsoft Entra ID). It doesn't apply to hybrid identity users who use password hash sync, pass-through authentication, or on-premises federation like Active Directory Federation Services (ADFS).

To learn how to synchronize user password hashes from an on-premises Active Directory to Microsoft Entra ID, see [Implement password hash synchronization with Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-password-hash-synchronization).

## Password policies and account restrictions in Microsoft Entra ID

You can set more password policies and restrictions in Microsoft Entra ID. For more information, see [Password policies and account restrictions in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-sspr-policy).

## Update password policy using PowerShell

The `Update-MgDomain` cmdlet updates the password policy of a specified domain or tenant and indicates the length of time that a password remains valid before it must be changed.

To learn how to update password policy for a specific domain or tenant, see [Update-MgDomain](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/update-mgdomain).

## Related content

- [Let users reset their own passwords](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/let-users-reset-passwords).
- [Reset passwords](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/reset-passwords).
- [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).
