# Prerequisites for integrating with Active Directory

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/prerequisites  
> Microsoft doc last updated: 09/29/2025

The following document provides the prerequisites for integrating with Active Directory.

## Cloud sync

### Hardware and software

|Requirement|Description and more requirements|
|-----|-----|
|Windows Server 2022, Windows Server 2019, or Windows Server 2016 |• 4-GB RAM or more</br>• .NET 4.7.1 runtime or greater</br>• domain-joined</br>• PowerShell execution policy set to **Undefined** or **RemoteSigned**</br>• TLS 1.2 enabled</br>|
|Active Directory|• On-premises AD that has a forest functional level 2003 or higher|
|Microsoft Entra tenant|• A tenant in Azure that's  used to synchronize from on-premises|

For more information on the cloud sync prerequisites, see [Cloud sync prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-prerequisites).

### Accounts

|Requirement|Description and more requirements|
|-----|-----|
|Domain/Enterprise administrator|Required to install the agent on the server and create the gMSA service account.|
|Hybrid Identity Administrator|Required to configure cloud sync. This account can't be a guest account.|
|gMSA service account|Required to run the agent.| 

For more information on the cloud sync accounts, and how to set up a custom gMSA account, see [Cloud sync prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-prerequisites).

<a name='azure-ad-connect'></a>

## Microsoft Entra Connect

### Hardware and software

|Requirement|Description and more requirements|
|-----|-----|
|Windows Server 2022, Windows Server 2019, and Windows Server 2016|• 4-GB RAM or more</br>• .NET 4.6.2 runtime or greater</br>• domain-joined</br>• PowerShell execution policy set to **RemoteSigned**</br>• TLS 1.2 enabled</br>• if federation is being used, the AD FS severs must be Windows Server 2012 R2 or higher and TLS/SSL certificates must be configured.|
|Active Directory|• On-premises AD that has a forest functional level 2003 or higher</br>• a writeable domain controller|
|Microsoft Entra tenant|• A tenant in Azure used to synchronize from on-premises|
|SQL Server|Microsoft Entra Connect requires a SQL Server database to store identity data. By default, a SQL Server 2019 Express LocalDB (a light version of SQL Server Express) is installed. For more information on using a SQL server, see [Microsoft Entra Connect SQL server requirements](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites#sql-server-used-by-azure-ad-connect)|

For more information on the cloud sync prerequisites, see [Microsoft Entra Connect prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites).

### Accounts

|Requirement|Description and more requirements|
|-----|-----|
|Enterprise administrator|Required to install Microsoft Entra Connect.|
|Hybrid Identity Administrator|Required to configure cloud sync.  This account can't be a guest account.  This account must be a school or organization account and can't be a Microsoft account.|
|Custom settings|If you use the custom settings installation path, you have more options. You can specify the following information:</br>• [AD DS Connector account](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-accounts-permissions)</br>• [ADSync Service account](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-accounts-permissions)</br>• [Microsoft Entra Connector account](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-accounts-permissions).  </br>For more information, see [Custom installation settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-accounts-permissions#custom-settings).|

For more information on the Microsoft Entra Connect accounts, see [Microsoft Entra Connect: Accounts and permissions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-accounts-permissions).

## Next steps
- [Common scenarios](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Tools for synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/sync-tools)
- [Choosing the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Steps to start](https://learn.microsoft.com/en-us/entra/identity/hybrid/get-started)
