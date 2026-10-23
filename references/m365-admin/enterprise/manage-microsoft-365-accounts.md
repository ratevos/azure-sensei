# Manage Microsoft 365 user accounts

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-accounts  
> Microsoft doc last updated: 09/05/2024


You can manage Microsoft 365 user accounts in several different ways, depending on your configuration. You can manage user accounts in the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>, [PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-user-accounts-and-licenses-with-microsoft-365-powershell), in Active Directory Domain Services (AD DS), or in the Microsoft Entra admin center.

As soon as you purchase Microsoft 365, the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a> and PowerShell can be used to manage accounts. When managing cloud identities, every person in your organization has a separate user account name and password. If you want to integrate with your on-premises infrastructure and have user accounts synchronized with Microsoft 365, you can use Microsoft Entra Connect to provide synchronization of identities and passwords for single sign-on (SSO) functionality.
  
## Plan for where and how you will manage your user accounts

Where and how you can manage your user accounts depends on the identity model you want to use for your Microsoft 365. The two overall models are cloud-only and hybrid.
  
### Cloud-only

You create and manage users in the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>. You can also use PowerShell or the Microsoft Entra admin center.

### Hybrid

User accounts are synchronized with Microsoft 365 from AD DS, so you must use on-premises AD DS tools to manage user accounts.

## Managing Accounts

When deciding which way your organization will create and manage accounts, consider the following requirements:
  
- The directory synchronization software needs to be installed on servers within your on-premises environment to connect the identities between Microsoft 365 and your AD DS.

- Any directory synchronization option, including SSO options, requires that your AD DS attributes meet standards. The specifics of what attributes are used in your directory and what cleanup (if any) is needed are described in [Prepare for directory synchronization to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/prepare-for-directory-synchronization).

- Plan how you are going to create Microsoft 365 accounts.

The following table lists the different account management tools.

|Tool|Notes|
|:-----|:-----|
|Microsoft 365 admin center  <br/> |[Add users individually or in bulk](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users) <br/>  Provides a simple web interface to add and change user accounts.  <br/>  Can't be used to change users if directory synchronization is enabled (location and license assignment can be set).  <br/>  Can't be used with SSO options.  <br/> |
|Windows PowerShell  <br/> |[Manage Microsoft 365 with Windows PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-with-microsoft-365-powershell) <br/>  Allows you to add users in bulk users by using a Windows PowerShell script.  <br/>  Can be used to assign location and licenses to accounts, regardless of how the accounts are created.  <br/> |
|Bulk import  <br/> |[Add several users at the same time](https://learn.microsoft.com/en-us/microsoft-365/enterprise/add-several-users-at-the-same-time) <br/>  Allows you to import a CSV file to add a group of users to Microsoft 365.  <br/>  Can't be used with SSO options.  <br/> |
|Microsoft Entra ID  <br/> |You get a free edition of Microsoft Entra ID with your Microsoft 365 subscription. You can perform functions like self-service password reset for cloud users, and customization of the Sign-in and Access Panel pages by using the free edition. To get enhanced functionality, you can upgrade to the basic edition, Microsoft Entra ID P1, or Microsoft Entra ID P2. See [Microsoft Entra editions](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis) for the list of supported features.  <br/> |
|Directory synchronization  <br/> |[Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/whatis-hybrid-identity) <br/>  For directory synchronization with or without password synchronization, use [Microsoft Entra Connect with express settings](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-install-express).  <br/>  For multiple forests and SSO options, use [Custom Installation of Microsoft Entra Connect](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-install-custom).  <br/>  Provides the infrastructure that's necessary to enable SSO.  <br/>  Required for many hybrid scenarios such as staged migration and hybrid Exchange  <br/>  Synchronizes security and mail-enabled groups from your AD DS.  <br/> |
|||

- Regardless of how you intend to add the user accounts to Microsoft 365, you need to manage several account features, such as assigning licenses, specifying location, and so on. These features can be managed long-term from the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a> or you can also [create user accounts with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/create-user-accounts-with-microsoft-365-powershell).

    If you choose to add and manage all your users through the admin center, you will specify the location and assign licenses at the same time as creating the Microsoft 365 account. As a result, not much planning is required.

    > [!IMPORTANT]
    > Creating accounts in Microsoft 365 without assigning a license (to SharePoint Online, for example) means that the account owner can view the Microsoft 365 center but can't access any of the services within your company's subscription. After you assign a location and the license, the account is replicated to the service or services that you assigned. The user can sign in to their account and use the services that you assigned to them.
  
## See also

- <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>
- [Manage user accounts and licenses with Microsoft 365 PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-user-accounts-and-licenses-with-microsoft-365-powershell)
