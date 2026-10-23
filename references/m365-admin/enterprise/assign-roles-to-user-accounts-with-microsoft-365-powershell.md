# Assign roles to Microsoft 365 user accounts with PowerShell

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/assign-roles-to-user-accounts-with-microsoft-365-powershell  
> Microsoft doc last updated: 12/09/2024


*This article applies to both Microsoft 365 Enterprise and Office 365 Enterprise.*

You can easily assign roles to user accounts by using PowerShell for Microsoft 365.

>[!Note]
>Learn how to [assign admin roles](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/assign-admin-roles) to user accounts with the Microsoft 365 admin center.
>
>For a list of additional resources, see [Manage users and groups](https://learn.microsoft.com/en-us/admin).
>

## Assign roles to user accounts using Microsoft Graph PowerShell

> [!NOTE]
> The Azure Active Directory module is being replaced by the Microsoft Graph PowerShell SDK. You can use the Microsoft Graph PowerShell SDK to access all Microsoft Graph APIs. For more information, see [Get started with the Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started).

First, use a **Microsoft Entra DC admin** or **Cloud Application Admin** account to [connect to your Microsoft 365 tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-to-microsoft-365-powershell). The cmdlets in this article require the permission scope **RoleManagement.ReadWrite.Directory** or one of the other permissions listed in the ['List subscribedSkus' Graph API reference page](https://learn.microsoft.com/en-us/graph/api/subscribedsku-list). Some commands in this article may require different permission scopes, in which case this will be noted in the relevant section.

```powershell
Connect-MgGraph -Scopes "RoleManagement.ReadWrite.Directory"
```

For more information, see [About admin roles](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?).

Next, identify the sign-in name of the user account that you want to add to a role (example: fredsm\@contoso.com). This is also known as the user principal name (UPN).

Next, determine the name of the role. See [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference).

> [!NOTE]
> Some role names are different for Azure Active Directory (Azure AD) PowerShell. For example, the *SharePoint Administrator* role in the Microsoft 365 admin center is *SharePoint Service Administrator* in Azure AD PowerShell.
>

Next, fill in the user UPN and role names and run these commands:
  
```powershell
$userUPN="<user UPN>"
$roleName="<role name>"
$role = Get-MgDirectoryRole | Where-Object {$_.displayName -eq $roleName}
if ($role -eq $null) {
    $roleTemplate = (Get-MgDirectoryRoleTemplate | Where-Object {$_.displayName -eq $roleName}).id
    New-MgDirectoryRole -DisplayName $roleName -RoleTemplateId $roleTemplate
    $role = Get-MgDirectoryRole | Where-Object {$_.displayName -eq $roleName}
}
$userId = (Get-MgUser -Filter "userPrincipalName eq '$userUPN'").Id
$newRoleMember =@{
    "@odata.id"= "https://graph.microsoft.com/v1.0/users/$userId"
    }
New-MgDirectoryRoleMemberByRef -DirectoryRoleId $role.Id -BodyParameter $newRoleMember
```

Here's an example of a completed command set that assigns the Exchange Administrator role to the *adelev\@contoso.com* account:

```powershell
$userUPN="adelev@contoso.com"
$roleName="Exchange Administrator"
$role = Get-MgDirectoryRole | Where-Object {$_.displayName -eq $roleName}
if ($role -eq $null) {
    $roleTemplate = (Get-MgDirectoryRoleTemplate | Where-Object {$_.displayName -eq $roleName}).id
    New-MgDirectoryRole -DisplayName $roleName -RoleTemplateId $roleTemplate
    $role = Get-MgDirectoryRole | Where-Object {$_.displayName -eq $roleName}
}
$userId = (Get-MgUser -Filter "userPrincipalName eq '$userUPN'").Id
$newRoleMember =@{
    "@odata.id"= "https://graph.microsoft.com/v1.0/users/$userId"
    }
New-MgDirectoryRoleMemberByRef -DirectoryRoleId $role.Id -BodyParameter $newRoleMember
```

To display the list of user IDs for a specific admin role, use these commands.

```powershell
$roleName="<role name>"
Connect-MgGraph -Scopes "Directory.Read.All"
Get-MgDirectoryRole | Where-Object { $_.DisplayName -eq $roleName } | ForEach-Object { Get-MgDirectoryRoleMember -DirectoryRoleId $_.Id }
```

## See also

- [Manage Microsoft 365 user accounts, licenses, and groups with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-user-accounts-and-licenses-with-microsoft-365-powershell)
- [Manage Microsoft 365 with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-with-microsoft-365-powershell)
- [Get started with PowerShell for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/getting-started-with-microsoft-365-powershell)
