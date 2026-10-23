# Step 3 - Wipe and block a former employee's mobile device

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-3  
> Microsoft doc last updated: 10/28/2025


If an employee has left your organization and they had a business phone, you can use the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) to wipe and block that device. This action helps ensure that your business data is removed from the device and it can no longer connect to your organization's Microsoft 365 subscription. 

If your organization uses Basic Mobility and Security to manage mobile devices, you can wipe and block those devices [using Basic Mobility and Security](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-wipe-devices).

> [!NOTE]
> You must have appropriate permissions through a an appropriate role, such as the [Directory Writers role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#directory-writers) to perform the tasks in this article. 

## Wipe mobile device using the Exchange admin center

1. In the [Exchange admin center](https://admin.exchange.microsoft.com/), go to > **Recipients** > **Mailboxes**. (Or, go directly to the [Mailboxes page](https://go.microsoft.com/fwlink/p/?linkid=2183135).)

1. Select the user, and under **Email apps & mobile devices**, select **Manage mobile devices**.

1. On the **Mobile Device Details** page, under **Mobile devices**, select a device. Then select an option, such as **Account Only Remote Wipe Device**, and then select **Block access**. See [Perform a remote wipe on a mobile phone in Exchange Online](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/exchange-activesync/remote-wipe-on-mobile-phone).

1. Save your changes.

## Related content

- [Exchange admin center in Exchange Online](https://learn.microsoft.com/en-us/exchange/exchange-admin-center)

- [Perform a remote wipe on a mobile phone in Exchange Online](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/exchange-activesync/remote-wipe-on-mobile-phone)
