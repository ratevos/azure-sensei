# Step 7 - Delete a former employee's user account

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-7  
> Microsoft doc last updated: 10/28/2025


After an employee has left your organization, and you've saved and accessed their user data, you can delete the former employee's account.

> [!IMPORTANT]
> Don't delete the account if you've set up email forwarding or converted it to a shared mailbox. Both need the account to anchor the forwarding or shared mailbox.
> 
> You must have appropriate permissions through a role, such as [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) to perform the tasks in this article. 

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** > **Active users**. (Or, go directly to the [Active users page](https://go.microsoft.com/fwlink/p/?linkid=834822).)

2. Select the name of the former employee's account that you want to delete.

3. Under the user's name, select **Delete user**. Choose the options you want for this user, and then select **Delete user**. If you've already given another user access to this user's email and OneDrive, you don't have to do it again here.

When you delete a user, the account becomes inactive for approximately 30 days. You have until then to restore the account before it's permanently deleted.

## Watch: Delete a former employee's user account

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=f1196f82-611c-41c8-8cc1-98e70f591d5d]

If you found this video helpful, check out the [complete training series for small businesses and those new to Microsoft 365](../../business-video/index.yml).

## Does your organization use Active Directory?

If your organization synchronizes user accounts to Microsoft 365 from a local Active Directory environment, you must delete and restore those user accounts in your local Active Directory service. You can't delete or restore the user in the Microsoft 365 admin center.

To learn how to delete and restore user account in Active Directory, see [Delete a User Account](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753730(v=ws.11)).
  
If you're using Microsoft Entra ID, see the [Remove-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/remove-mguser) PowerShell cmdlet.
  
## What you need to know about terminating an employee's email session

Here's information about how to get an employee out of email (Exchange).

|What you can do|How you do it|
|-----|-----|
|Terminate a session (such as Outlook on the web, Outlook, Exchange active sync, etc.) and force to open a new session|Reset password|
|Terminate a session and block access to future sessions (for all protocols)|Disable the account. For example, in the Exchange admin center or using PowerShell: <br/>  `Set-Mailbox user@contoso.com -AccountDisabled:$true`|
|Terminate the session for a particular protocol (such as ActiveSync)|Disable the protocol. For example, in the Exchange admin center or using PowerShell: <br/>  `Set-CASMailbox user@contoso.com -ActiveSyncEnabled:$false`|

The preceding operations can be done in three places:

|If you terminate the session here|How long it takes|
|---|---|
|In the Exchange admin center or using PowerShell|Expected delay is within 30 min|
|In the Microsoft Entra admin center|Expected delay is 60 min|
|In an on-premises environment|Expected delay is 3 hours or more|

### How to get fastest response for account termination

**Fastest**: Use the Exchange admin center (use PowerShell) or Microsoft Entra admin center. In an on-premises environment, it can take several hours to sync the change through Microsoft Entra Connect.
  
**Fastest for a user with presence on-premises and in the Exchange Datacenter**: Terminate the session using Microsoft Entra admin center/Exchange admin center AND make the change in the on-premises environment as well. Otherwise, the change in Microsoft Entra admin center/Exchange admin center is overwritten by Microsoft Entra Connect.
  
## Related content

- [Restore a user](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/restore-user)

- [Reset passwords](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/reset-passwords)

- [Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/fundamentals/entra-admin-center)

- [Exchange admin center](https://learn.microsoft.com/en-us/exchange/exchange-admin-center)

- [Exchange PowerShell](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell)
