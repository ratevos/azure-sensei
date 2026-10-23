# Block Microsoft 365 user accounts with PowerShell

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/block-user-accounts-with-microsoft-365-powershell  
> Microsoft doc last updated: 12/09/2024


*This article applies to both Microsoft 365 Enterprise and Office 365 Enterprise.*

When you block access to a Microsoft 365 account, you prevent anyone from using the account to sign in and access the services and data in your Microsoft 365 organization. You can use PowerShell to block access to individual or multiple user accounts.

## Block access to individual user accounts

>[!NOTE]
> The Azure Active Directory module is being replaced by the Microsoft Graph PowerShell SDK. You can use the Microsoft Graph PowerShell SDK to access all Microsoft Graph APIs. For more information, see [Get started with the Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started).

First, [connect to your Microsoft 365 tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-to-microsoft-365-powershell).

Blocking and unblocking user accounts requires the **User.ReadWrite.All** permission scope or one of the other permissions listed in the ['List subscribedSkus' Graph API reference page](https://learn.microsoft.com/en-us/graph/api/subscribedsku-list).

```powershell
Connect-Graph -Scopes User.ReadWrite.All
```

Use the following syntax to block an individual user account:

```powershell
$params = @{
	accountEnabled = $false
}
Update-MgUser -UserId <sign-in name of the user account> -BodyParameter $params
```

> [!NOTE]
> The *-UserId* parameter in the **Update-MgUser** cmdlet accepts either the account sign-in name, also known as the User Principal Name, or the account's object ID.

This example blocks access to the user account *fabricec@litwareinc.com*.

```powershell
$params = @{
	accountEnabled = $false
}
Update-MgUser -UserId "fabricec@litwareinc.com" -BodyParameter $params
```

To unblock this user account, run the following command:

```powershell
$params = @{
	accountEnabled = $true
}
Update-MgUser -UserId "fabricec@litwareinc.com" -BodyParameter $params
```

To display the user account UPN based on the user's display name, use the following commands:

```powershell
$userName="<display name>"
Write-Host (Get-MgUser -All | where {$_.DisplayName -eq $userName}).UserPrincipalName

```

This example displays the user account UPN for the user  *Caleb Sills*.

```powershell
$userName="Caleb Sills"
Write-Host (Get-MgUser -All | where {$_.DisplayName -eq $userName}).UserPrincipalName
```

To block an account based on the user's display name, use the following commands:

```powershell
$userName="<display name>"
$user = Get-MgUser -Filter "displayName eq '$userName'"
$params = @{
	accountEnabled = $false
}
Update-MgUser -UserId $user.Id -BodyParameter $params
```

To check the blocked status of a user account use the following command:

```powershell
Get-MgUser -UserId <UPN of user account> -Property "displayName,accountEnabled" | Select displayName, accountEnabled
```

### Block multiple user accounts

To block access for multiple user accounts, create a text file that contains one account sign-in name on each line like this:

  ```powershell
akol@contoso.com
tjohnston@contoso.com
kakers@contoso.com
  ```

In the following commands, the example text file is *C:\My Documents\Accounts.txt*. Replace this file name with the path and file name of your text file.

To block access to the accounts listed in the text file, run the following command:

```powershell
$params = @{
	accountEnabled = $false
}
Get-Content "C:\My Documents\Accounts.txt" | ForEach {Update-MgUser -UserId $_ -BodyParameter $params}
```

To unblock the accounts that are listed in the text file, run the following command:

```powershell
$params = @{
	accountEnabled = $true
}
Get-Content "C:\My Documents\Accounts.txt" | ForEach {Update-MgUser -UserId $_ -BodyParameter $params}
```

## See also

[Manage Microsoft 365 user accounts, licenses, and groups with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-user-accounts-and-licenses-with-microsoft-365-powershell)

[Manage Microsoft 365 with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-with-microsoft-365-powershell)

[Get started with PowerShell for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/getting-started-with-microsoft-365-powershell)
