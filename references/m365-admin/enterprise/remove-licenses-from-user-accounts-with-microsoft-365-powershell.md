# Remove Microsoft 365 licenses from user accounts with PowerShell

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/remove-licenses-from-user-accounts-with-microsoft-365-powershell  
> Microsoft doc last updated: 12/05/2024


*This article applies to both Microsoft 365 Enterprise and Office 365 Enterprise.*

>[!Note]
>[Learn how to remove licenses from user accounts](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users) with the Microsoft 365 admin center. For a list of additional resources, see [Manage users and groups](https://learn.microsoft.com/en-us/admin).
>

## Use the Microsoft Graph PowerShell SDK

First, [connect to your Microsoft 365 tenant](https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started?view=graph-powershell-1.0#authentication).

Assigning and removing licenses for a user requires the User.ReadWrite.All permission scope or one of the other permissions listed in the ['Assign license' Graph API reference page](https://learn.microsoft.com/en-us/graph/api/user-assignlicense).

The Organization.Read.All permission scope is required to read the licenses available in the tenant.

```powershell
Connect-Graph -Scopes User.ReadWrite.All, Organization.Read.All
```

To view the licensing plan information in your organization, see the following articles:

- [View licenses and services with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-licenses-and-services-with-microsoft-365-powershell)

- [View account license and service details with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-account-license-and-service-details-with-microsoft-365-powershell)

### Removing licenses from user accounts

To remove licenses from an existing user account, use the following syntax:
  
```powershell
Set-MgUserLicense -UserId "<Account>" -RemoveLicenses @("<AccountSkuId1>") -AddLicenses @{}
```

This example removes the **SPE_E5** (Microsoft 365 E5) licensing plan from the user **BelindaN@litwareinc.com**:

```powershell
$e5Sku = Get-MgSubscribedSku -All | Where SkuPartNumber -eq 'SPE_E5'
Set-MgUserLicense -UserId "belindan@litwareinc.com" -RemoveLicenses @($e5Sku.SkuId) -AddLicenses @{}
```

To remove all licenses from a group of existing licensed users, use the following syntax:

```powershell
$licensedUsers = Get-MgUser -Filter 'assignedLicenses/$count ne 0' `
    -ConsistencyLevel eventual -CountVariable licensedUserCount -All `
    -Select UserPrincipalName,DisplayName,AssignedLicenses

foreach($user in $licensedUsers)
{
    $licensesToRemove = $user.AssignedLicenses | Select -ExpandProperty SkuId
    $user = Set-MgUserLicense -UserId $user.UserPrincipalName -RemoveLicenses $licensesToRemove -AddLicenses @{} 
}
```

To remove a specific license from a list of users in a `CSV` file, perform the following steps. This example removes the **SPE_E5** (Microsoft 365 Enterprise E5) license from the user accounts defined in the `CSV` file C:\My Documents\Accounts.csv.

  1. Create and save a CSV file to C:\My Documents\Accounts.csv that contains one account on each line under the `UserPrincipalName` header like this:

     ```powershell
     UserPrincipalName
     akol@contoso.com
     tjohnston@contoso.com
     kakers@contoso.com
     ```

  2. Use the following command:

     ```powershell
     $usersList = Import-CSV -Path "C:\My Documents\Accounts.csv"
     $e5Sku = Get-MgSubscribedSku -All | Where SkuPartNumber -eq 'SPE_E5'
     foreach($user in $usersList) {
       Set-MgUserLicense -UserId $user.UserPrincipalName -RemoveLicenses @($e5Sku.SkuId) -AddLicenses @{}
     }
     ```

Another way to free up a license is by deleting the user account. For more information, see [Delete and restore user accounts with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/delete-and-restore-user-accounts-with-microsoft-365-powershell).
  
## See also

[Manage Microsoft 365 user accounts, licenses, and groups with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-user-accounts-and-licenses-with-microsoft-365-powershell)
  
[Manage Microsoft 365 with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-with-microsoft-365-powershell)
  
[Getting started with PowerShell for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/getting-started-with-microsoft-365-powershell)
