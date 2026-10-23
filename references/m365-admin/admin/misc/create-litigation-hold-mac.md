# Place a mailbox on litigation hold

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/create-litigation-hold-mac  
> Microsoft doc last updated: 03/25/2026


You can place a mailbox on litigation hold to retain mailbox content, including deleted items and the original versions of modified items. When you place a user mailbox on litigation hold, content in the user's archive mailbox (if enabled) is also retained. 

When you create a hold, you can specify a hold duration (also called a *time-based hold*) so that deleted and modified items are retained for a specified period and then permanently deleted from the mailbox. Or, you can retain content indefinitely (called an *infinite hold*) or until the litigation hold is removed. 

If you specify a hold duration period, it's calculated from the date a message is received or a mailbox item is created.
  
Here's what happens when you create a litigation hold.
  
- Items that are permanently deleted by the user are retained in the **Recoverable Items** folder in the user's mailbox during the hold.
- Items that are purged from the **Recoverable Items** folder by the user are retained during the hold.
- The storage quota for the **Recoverable Items** folder is increased from 30 GB to 110 GB.
- Items in the user's primary and the archive mailboxes are retained

## Assign an Exchange Online Plan 2 license

To place an Exchange Online mailbox on litigation hold, that mailbox must be assigned an Exchange Online Plan 2 license. If a mailbox is assigned an Exchange Online Plan 1 license, you must assign that mailbox a separate Exchange Online Archiving license to place it on hold.

## Place a mailbox on litigation hold

1. Go to the [Microsoft 365 admin center](https://admin.microsoft.com) and sign in. 

2. Select **Users** > **Active users**, and then select the user for whom you want to place on litigation hold.

3. On the **Properties** flyout panel, select the **Mail** tab, and then under **More actions**, select **Manage litigation hold**.

   

4. On the **Manage litigation hold** flyout page, select the **Turn on litigation hold** checkbox, and then add the following optional information:

   - **Hold duration (days)**: Use this box to create a time-based hold and specify how long mailbox items are held when the mailbox is placed on Litigation hold. The duration is calculated from the date a mailbox item is received or created. When the hold duration expires for a specific item, that item is no longer preserved. If you leave this box blank, items are preserved indefinitely or until the hold is removed. Use days to specify the duration.

    - **Note visible to the user**: Use this box to inform the user their mailbox is on litigation hold. The note appears on the Account Information page in the user's mailbox if they're using Outlook 2010 or later. To access this page, users can select **File** in Outlook.

    - **Web page with more information for the user**: Use this box to direct the user to a website for more information about litigation hold. This URL appears on the Account Information page in the user's mailbox if they're using Outlook 2010 or later. To access this page, users can select **File** in Outlook.

5. Select **Save changes** on the **Litigation hold** flyout page to create the hold.

   The system displays a banner saying it might take up to 240 minutes for the change to take effect.
   
   > [!NOTE]
   > After a litigation hold is enabled, the "created by" field reflects the original user who enabled the hold, even when the hold is later modified.
   
### Create a litigation hold using PowerShell

You can also create a litigation hold by running the following command in [Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell):

```powershell
Set-Mailbox <username> -LitigationHoldEnabled $true
```

The previous command preserves items indefinitely because the hold duration isn't specified. To create a time-based hold, using the following command:

```powershell
Set-Mailbox <username> -LitigationHoldEnabled $true -LitigationHoldDuration <number of days>
```

You can also run the following command to verify if the mailbox is placed on litigation hold:

```powershell
Get-Mailbox <username> | FL LitigationHoldEnabled
```

A value of *True* indicates that the mailbox is on litigation hold.

For more information, see [Set-Mailbox](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/set-mailbox).

## How does litigation hold work?

In the normal deleted item workflow, a mailbox item is moved to the **Deletions** subfolder in the **Recoverable Items** folder when a user permanently deletes it (Shift + Delete) or deletes it from the **Deleted Items** folder. A deletion policy (which is a retention tag configured with a Delete retention action) also moves items to the **Deletions** subfolder when the retention period expires. 

When a user purges an item in the **Recoverable Items** folder, or when the deleted item retention period expires for an item, it moves to the **Purges** subfolder in the **Recoverable Items** folder, and is marked for permanent deletion. It's purged from Exchange the next time the mailbox is processed by the Managed Folder Assistant (MFA).

When a mailbox is placed on litigation hold, items in the **Purges** subfolder are preserved for the hold duration specified by the litigation hold. The hold duration is calculated from the original date an item was received or created, and defines how long items in the **Purges** subfolder are held. 

When the hold duration expires for an item in the **Purges** subfolder, the item is marked for permanent deletion and is purged from Exchange the next time the mailbox is processed by the MFA. If an indefinite hold is placed on a mailbox, items aren't purged from the **Purges** subfolder.

The following illustration shows the subfolders in the **Recoverable Items** folders and the hold workflow process.

> [!NOTE]
> - If a hold associated with an eDiscovery case is placed on a mailbox, purged items are moved from the **Deletions** subfolder to the **Discovery Holds** subfolder, and are preserved until the mailbox is released from the eDiscovery hold.
> - If you don't see the **Manage litigation hold** option in the Microsoft 365 admin center, it might be because the mailbox isn't assigned an Exchange Online Plan 2 license.
