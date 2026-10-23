# Assign Microsoft 365 licenses to user accounts

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/assign-licenses-to-user-accounts  
> Microsoft doc last updated: 03/12/2025


*This article applies to both Microsoft 365 Enterprise and Office 365 Enterprise.*

For the cloud-only identity model, you can assign Microsoft 365 licenses to user accounts as they're created, depending on how you create them.

For the hybrid identity model, when Active Directory Domain Services (AD DS) user accounts are synchronized for the first time, they aren't automatically assigned a location or a Microsoft 365 license. **You must configure each user account with a user location prior to or along with assigning a license.**

In either case, you must assign a license to user accounts so your users can access Microsoft 365 services, such as email and Microsoft Teams.

You can assign licenses to user accounts either individually or automatically through group membership.

To assign Microsoft 365 licenses to individual user accounts, you can use:

- [The Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users)
- [PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/assign-licenses-to-user-accounts-with-microsoft-365-powershell)
- The Microsoft Entra admin center

## Group-based licensing

You can configure security groups in Microsoft Entra ID to automatically assign licenses from a set of subscriptions to all the members of the group. This is known as *group-based licensing*. If a user account is added to or removed from the group, the licenses for the group's subscriptions will be automatically assigned or unassigned from the user account.

Make sure you have enough licenses for all the group members. If you run out of licenses, new users won't be assigned licenses until licenses become available.

> [!NOTE]
> You should not configure group-based licensing for groups that contain Azure business to business (B2B) accounts.

For more information, see [group-based licensing in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-licensing-whatis-azure-portal).

## Next steps

With the appropriate set of user accounts that have been assigned licenses, you're now ready to:

- [Implement security](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/defender-for-office-365)
- [Deploy client software, such as Microsoft 365 Apps](https://learn.microsoft.com/en-us/DeployOffice/deployment-guide-microsoft-365-apps)
- [Set up device management](https://learn.microsoft.com/en-us/microsoft-365/enterprise/device-management-roadmap-microsoft-365)
- [Configure services and applications](https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-services-and-applications)
