# View directory synchronization errors in Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/identify-directory-synchronization-errors  
> Microsoft doc last updated: 07/17/2024


You can view directory synchronization errors in the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>. Only the User object errors are displayed. To view errors with PowerShell, see [Identify objects with DirSyncProvisioningErrors](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-syncservice-duplicate-attribute-resiliency).

## View directory synchronization errors in the Microsoft 365 admin center

To view any errors in the Microsoft 365 admin center:
  
1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com) with a Hybrid Identity Administrator account.

2. On the **Home** page, you'll see the **User management** card.

    
  
3. On the card, choose **Sync errors** under **Microsoft Entra Connect** to see the errors on the **Directory sync errors** page.

    

4. Choose any of the errors to display the details pane with information about the error and tips on how to fix it.

   
  
After viewing, see [fixing problems with directory synchronization for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/fix-problems-with-directory-synchronization) to correct any identified issues.
