# Turn off directory synchronization for Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/turn-off-directory-synchronization  
> Microsoft doc last updated: 09/03/2024


You can use PowerShell to turn off directory synchronization and convert your synchronized users and groups to cloud-only. However, it isn't recommended that you turn off directory synchronization as a troubleshooting step. If you need assistance with troubleshooting directory synchronization, see the [Fixing problems with directory synchronization for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/fix-problems-with-directory-synchronization) article. 
  
[Contact support](https://support.office.com/article/32a17ca7-6fa0-4870-8a8d-e25ba4ccfd4b) if you need help with this procedure.

> [!NOTE]
> If your goal is to permanently disable synchronization in the tenant, you should first uninstall the synchronization client (such as Connect Sync or Cloud Sync).
> Disabling synchronization before uninstalling the sync client might result in the Entra Id Portal showing directory synchronization as **disabled**, but optional features such as Password Hash Synchronization show as **enabled**. Although this shouldn't cause any issues, and the optional feature wouldn't work when directory synchronization is disabled, it may lead to an unexpected status in the Portal.
  
## Turn off directory synchronization

To turn off directory synchronization:
  
1. First, install the required software and connect to your Microsoft 365 subscription. For instructions, see [Connect with the Microsoft Graph PowerShell module for Windows PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-to-microsoft-365-powershell#connect-with-microsoft-graph-powershell).

2. Use **Update-MgOrganization** to disable directory synchronization:

  ```powershell
    # Install v1.0 Microsoft Graph PowerShell module 
    Install-Module Microsoft.Graph -Force
    
    # Connect With Hybrid Identity Administrator Account
    Connect-MgGraph -scopes "Organization.ReadWrite.All,Directory.ReadWrite.All" 
    
    # Verify the current status of the DirSync Type
    Get-MgOrganization | Select OnPremisesSyncEnabled 
    
    # Store the Tenant ID in a variable named organizationId
    $organizationId = (Get-MgOrganization).Id 
    
    # Store the False value for the DirSyncEnabled Attribute
    $params = @{
    	onPremisesSyncEnabled = $false
    }
    
    # Perform the update
    Update-MgOrganization -OrganizationId $organizationId -BodyParameter $params 
    
    # Check that the command worked
    Get-MgOrganization | Select OnPremisesSyncEnabled
  ```

> [!Note]
> If you use this command, you must wait 72 hours before you can turn directory synchronization back on.
> This process will clear the following on-premises properties:
>   - DnsDomainName
>   - NetBiosName
>   - OnPremisesDistinguishedName
>   - OnPremisesSamAccountName
>   - OnpremisesUserPrincipalName
