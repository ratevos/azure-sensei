# Uninstall Microsoft Entra Connect

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-uninstall  
> Microsoft doc last updated: 04/09/2025


This document describes how to correctly uninstall Microsoft Entra Connect.

<a name='uninstall-azure-ad-connect-from-the-server'></a>

## Uninstall Microsoft Entra Connect from the server
The first thing you need to do is remove Microsoft Entra Connect from the server that it's running on. Use the following steps:

 1. On the server running Microsoft Entra Connect, navigate to **Control Panel**.
 2. Select **Uninstall a program**
 </br>
 
 3. Select **Microsoft Entra Connect**.
 </br>
 
 4. When prompted, select **Yes** to confirm.
 5. This confirmation brings up the Microsoft Entra Connect screen. Select **Remove**.
 </br>
 
 6. Once this action completes, select **Exit**.
 7. </br>
 
 8. Back in **Control Panel** select **Refresh** and all of the components should be removed.

## Next steps

- Learn more about [Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).
- [Install Microsoft Entra Connect using an existing ADSync database](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-existing-database)
- [Install Microsoft Entra Connect using SQL delegated administrator permissions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-sql-delegation)
