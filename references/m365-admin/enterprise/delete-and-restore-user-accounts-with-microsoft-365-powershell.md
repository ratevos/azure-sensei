# Delete Microsoft 365 user accounts with PowerShell

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/delete-and-restore-user-accounts-with-microsoft-365-powershell  
> Microsoft doc last updated: 12/06/2024


You can use PowerShell for Microsoft 365 to delete and restore user accounts.

>[!Note]
>Learn how to [restore a user account](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/restore-user) by using the Microsoft 365 admin center.
>
>For a list of additional resources, see [Manage users and groups](https://learn.microsoft.com/en-us/admin).
>

## Use Microsoft Graph PowerShell to delete a user account

> [!NOTE]
> The Azure Active Directory (AzureAD) PowerShell module is being deprecated and replaced by the Microsoft Graph PowerShell SDK. You can use the Microsoft Graph PowerShell SDK to access all Microsoft Graph APIs. For more information, see [Get started with the Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started).
>
> Also see [Install the Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation) and [Upgrade from Azure AD PowerShell to Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/migration-steps) for information on how to install and upgrade to Microsoft Graph PowerShell, respectively.
>
> For information about how to use different methods to authenticate ```Connect-Graph``` in an unattended script, see the article [Authentication module cmdlets in Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/authentication-commands).

Deleting a user account requires the User.ReadWrite.All permission scope, which is listed in the ['Assign license' Microsoft Graph API reference page](https://learn.microsoft.com/en-us/graph/api/user-assignlicense).

The User.Read.All permission scope is required to read the user account details in the tenant.

First, [connect to your Microsoft 365 tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-to-microsoft-365-powershell).

```powershell
# Connect to your tenant
Connect-MgGraph -Scopes User.Read.All, User.ReadWrite.All
```

After you connect, use the following syntax to remove an individual user account:
  
```powershell
$userName="<display name>"
# Get the user
$userId = (Get-MgUser -Filter "displayName eq '$userName'").Id
# Remove the user
Remove-MgUser -UserId $userId -Confirm:$false
```

This example removes the user account *Caleb Sills*.

```powershell
$userName="Caleb Sills"
$userId = (Get-MgUser -Filter "displayName eq '$userName'").Id
Remove-MgUser -UserId $userId -Confirm:$false
```

## Restore a user account

To a restore a user account using Microsoft Graph PowerShell, first [connect to your Microsoft 365 tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-to-microsoft-365-powershell).

To restore a deleted user account, the permission scope *Directory.ReadWrite.All* is required. Connect to the tenant with this permission scope:

```powershell
# Connect to your tenant
Connect-MgGraph -Scopes Directory.ReadWrite.All
```

Deleted user accounts no longer exist except as objects in the directory, so you can't search for the user account to restore. Instead, use the following PowerShell script to search the directory for deleted objects of the type *microsoft.graph.user*:

```powershell
$DeletedUsers = Get-MgDirectoryDeletedItem -DirectoryObjectId microsoft.graph.user -Property '*'
$DeletedUsers = $DeletedUsers.AdditionalProperties['value']
foreach ($deletedUser in $DeletedUsers)
{
   $deletedUser | Format-Table
}
```

The output of this script, assuming any deleted user objects exist in the directory, will look like this:

```powershell
Key               Value
---               -----
businessPhones    {}
displayName       Caleb Sills
givenName         Caleb
mail              CalebS@litware.com
surname           Sills
userPrincipalName cdea706c3fdc4bbd95925d92d9f71eb8CalebS@litware.com
id                cdea706c-3fdc-4bbd-9592-5d92d9f71eb8
```

Use the following syntax to restore an individual user account:

```powershell
# Input user account ID
$userId = "<id>"
# Restore the user
Restore-MgDirectoryDeletedItem -DirectoryObjectId $userId
```

This example restores the user account *calebs\@litwareinc.com* using the value for ```$userID``` from the output of the above script.

```powershell
$userId = "cdea706c-3fdc-4bbd-9592-5d92d9f71eb8"
Restore-MgDirectoryDeletedItem -DirectoryObjectId $userId
```

The output of this command looks like this:

```powershell
Id                                   DeletedDateTime
--                                   ---------------
cdea706c-3fdc-4bbd-9592-5d92d9f71eb8
```

## See also

[Manage Microsoft 365 user accounts, licenses, and groups with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-user-accounts-and-licenses-with-microsoft-365-powershell)
  
[Manage Microsoft 365 with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-with-microsoft-365-powershell)
  
[Get started with PowerShell for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/getting-started-with-microsoft-365-powershell)
