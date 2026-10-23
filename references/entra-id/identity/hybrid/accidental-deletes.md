# Configure accidental deletion prevention with Active Directory

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/accidental-deletes  
> Microsoft doc last updated: 04/09/2025


When installing either cloud sync or Microsoft Entra Connect, this feature is enabled by default and configured to not allow an export with more than 500 deletes. This feature is designed to protect you from accidental configuration changes and changes to your on-premises directory that would affect many users and other objects.

You can change the default behavior and tailor it to your organizations needs.

## Configure accidental delete prevention with cloud sync
To use the new feature, follow the steps below.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   
 3. Under **Configuration**, select your configuration.
 4. Select **View default properties**.
 5. Click the pencil next to **Basics**
 6. On the right, fill in the following information.
	 - **Notification email** - email used for notifications
	- **Prevent accidental deletions** - check this box to enable the feature
	- **Accidental deletion threshold** - enter the number of objects to stop synchronization and send a notification

For more information, see [Accidental delete prevention with cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-accidental-deletes)

<a name='configure-accidental-delete-prevention-with-azure-ad-connect'></a>

## Configure accidental delete prevention with Microsoft Entra Connect
The default value of 500 objects can be changed with PowerShell using `Enable-ADSyncExportDeletionThreshold`, which is part of the [AD Sync module](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-adsync) installed with Microsoft Entra Connect. You should configure this value to fit the size of your organization. Since the sync scheduler runs every 30 minutes, the value is the number of deletes seen within 30 minutes.

For more information, see [Accidental delete prevention with Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-prevent-accidental-deletes).
