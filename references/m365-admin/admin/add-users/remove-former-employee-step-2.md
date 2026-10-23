# Step 2 - Save the contents of a former employee's mailbox

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-2  
> Microsoft doc last updated: 03/06/2026


If a former employee is subject to a litigation hold or in-place hold, you can export their Outlook content to a `.pst` file. 

You must have appropriate permissions through a role, such as [Microsoft 365 Backup Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-backup-administrator) or [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) to perform the tasks in this article. 

## Place hold or export user's data to a .pst file

If a former employee is blocked from signing into your organization's Microsoft 365 subscription, and it's important that you don't lose their data, you can save the contents of the former employee's mailbox. There are two ways you can save the contents of the former employee's mailbox.
  
- **Place a litigation hold or an in-place hold on the mailbox** before the deleting the user account. This is much more complicated than the other option, but is worth doing if your Enterprise plan includes archiving and legal hold, litigation is a possibility, and you have a technically strong IT department.

   After you convert the mailbox to an inactive mailbox, administrators, compliance officers, or records managers can use In-Place eDiscovery tools in Exchange Online to access and search the contents.

   Inactive mailboxes can't receive email and aren't displayed in your organization's shared address book or other lists.

   To learn how to place a hold on a mailbox, see [Manage inactive mailboxes in Exchange Online](https://learn.microsoft.com/en-us/microsoft-365/compliance/create-and-manage-inactive-mailboxes).

**OR**

- **Add the former employee's email address to your version of Outlook** (desktop app), and then export the data to a `.pst` file. You can import the data to another email account as needed. 

   See the following articles:
   
   - [Step 4 - Give another employee access to OneDrive and Outlook data](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-4) 
   
   - [Export emails, contacts, and calendar items to Outlook using a .pst file](https://support.microsoft.com/office/export-emails-contacts-and-calendar-items-to-outlook-using-a-pst-file-14252b52-3075-4e9b-be4e-ff9ef1068f91)

## Related content

- [Exchange admin center in Exchange Online](https://learn.microsoft.com/en-us/exchange/exchange-admin-center)

- [Restore a user](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/restore-user)

- [Security and compliance for Exchange Online](https://learn.microsoft.com/en-us/exchange/security-and-compliance/security-and-compliance)

- [Export search results in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-export)

- [Export emails, contacts, and calendar items to Outlook using a .pst file](https://support.microsoft.com/office/export-emails-contacts-and-calendar-items-to-outlook-using-a-pst-file-14252b52-3075-4e9b-be4e-ff9ef1068f91)
