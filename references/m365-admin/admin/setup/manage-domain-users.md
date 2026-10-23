# Synchronize domain users to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/manage-domain-users  
> Microsoft doc last updated: 04/23/2026


## 1. Prepare for Directory Synchronization

Before you synchronize your users and computers from the local Active Directory Domain, review [Prepare for directory synchronization to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/prepare-for-directory-synchronization). In particular:

- Make sure that no duplicates exist in your directory for the following attributes: **mail**, **proxyAddresses**, and **userPrincipalName**. These values must be unique and any duplicates must be removed.

- We recommend that you configure the **userPrincipalName** (UPN) attribute for each local user account to match the primary email address that corresponds to the licensed Microsoft 365 user. For example: *mary.shelley@contoso.com* rather than *mary@contoso.local*.

- If the Active Directory domain ends in a non-routable suffix like *.local* or *.lan*, instead of an internet routable suffix such as *.com* or *.org*, adjust the UPN suffix of the local user accounts first as described in [Prepare a non-routable domain for directory synchronization](https://learn.microsoft.com/en-us/microsoft-365/enterprise/prepare-a-non-routable-domain-for-directory-synchronization).

The **Run IdFix** in the following steps makes sure that your on-premises Active Directory is ready for directory synchronization.

<a name='2-install-and-configure-azure-ad-connect'></a>

## 2. Install and configure Microsoft Entra Connect

To synchronize your users, groups, and contacts from the local Active Directory into Microsoft Entra ID, install Microsoft Entra Connect and set up directory synchronization.

 1. In the [admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), select **Setup** in the left nav.

 2. Under **Sign-in and security**, select **Add or sync users to Microsoft Entra ID**.

 3. On the **Add or sync users to your Microsoft account** page, choose **Get started**.

 4. In the first step  run IdFix tool to prepare for Directory sync.

 5. Follow the wizard steps to download Microsoft Entra Connect and use it to synchronize your domain-controlled users to Microsoft 365.

See [Set up directory synchronization for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/set-up-directory-synchronization) to learn more.

As you configure your options for Microsoft Entra Connect, we recommend that you enable **Password Synchronization**, **Seamless Single Sign-On**, and the **password writeback** feature, which is also supported in Microsoft 365 for business.

> [!NOTE]
> There are some additional steps for password writeback beyond the check box in Microsoft Entra Connect. For more information, see [How-to: configure password writeback](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-sspr-writeback).

If you also want to manage domain-joined Windows 10 devices, see [Enable domain-joined Windows 10 devices to be managed by Microsoft 365 Business Premium](https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365bp-manage-windows-devices) to set up a Microsoft Entra hybrid join.
