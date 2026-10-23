# Microsoft Entra Cloud Sync accidental deletes

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-accidental-deletes  
> Microsoft doc last updated: 04/09/2025


The following document describes the accidental deletion feature for Microsoft Entra Cloud Sync. The accidental delete feature is designed to protect you from accidental configuration changes and changes to your on-premises directory that would affect many users and groups. This feature allows you to:

- Configure the ability to prevent accidental deletes automatically. 
- Set the # of objects (threshold) beyond which the configuration takes effect.
- Set up a notification email address so they can get an email notification once the sync job in question is put in quarantine for this scenario.

>[!NOTE]
>If you have specified accidental delete prevention four group provisioning to Microsoft Entra ID, be aware this only prevents the group from being deleted. This does not prevent members from being deleted. To prevent members from being deleted, you should configure accidental delete prevention on synchronized users.

To use this feature, you set the threshold for the number of objects that, if deleted, synchronization should stop. So if this number is reached, the synchronization stops and a notification is sent to the email that is specified. This notification allows you to investigate what is going on.

For more information and an example, see the following video.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=2af05990-497c-46b5-ae3e-d20c8909bbe8]

## Configure accidental delete prevention
To use the new feature, follow the steps below.

 1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   
 3. Under **Configuration**, select your configuration.
 4. Select **Properties**.
 5. Click the pencil next to **Basics**
 6. On the right, fill in the following information.
	- **Notification email** - email used for notifications
	- **Prevent accidental deletions** - check this box to enable the feature
	- **Accidental deletion threshold** - enter the number of objects to stop synchronization and send a notification

## Recovering from an accidental delete instance
If you encounter an accidental delete you see this message on the status of your provisioning agent configuration. It says **Delete threshold exceeded**.
 

By clicking on **Delete threshold exceeded**, you'll see the sync status info. This action will provide more details. 
 
 

By right-clicking on the ellipses, you get the following options:
 - View provisioning log
 - View agent
 - Allow deletes

 

Using **View provisioning log**, you can see the **StagedDelete** entries and review the information provided on the users that have been deleted.
 
 

### Allowing deletes

The **Allow deletes** action, deletes the objects that triggered the accidental delete threshold. Use the following procedure to accept these deletes. 

1. Right-click on the ellipses and select **Allow deletes**.
2. Click **Yes** on the confirmation to allow the deletions.
 
 

3. You'll see confirmation that the deletions were accepted and the status will return to healthy with the next cycle. 
 
 

### Rejecting deletions

If you don't want to allow the deletions, you need to do the following actions:
- Investigate the source of the deletions.
- Fix the issue (example, OU was moved out of scope accidentally and you've now readded it back to the scope).
- Run **Restart sync** on the agent configuration.

## Next steps 

- [Microsoft Entra Cloud Sync troubleshooting?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-troubleshoot)
- [Microsoft Entra Cloud Sync error codes](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-error-codes)
