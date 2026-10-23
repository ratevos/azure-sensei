# User Testing in Multi-Geo

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-multi-geo-user-testing  
> Microsoft doc last updated: 05/09/2025


In Microsoft Entra there are two types of user objects: cloud only users and synchronized users. Follow the appropriate instructions for your type of user.

>[!TIP]
>We recommend that you begin validations with a test user or small group of users before rolling out multi-geo to your broader organization.

<a name='synchronize-users-preferred-data-location-using-azure-ad-connect'></a>

## Synchronize user's Preferred Data Location (PDL) using Microsoft Entra Connect

If your company's users are synchronized from an on-premises Active Directory system to Microsoft Entra ID, their PreferredDataLocation must be populated in AD and synchronized to Microsoft Entra ID.

Follow the process in <a href="/azure/active-directory/hybrid/how-to-connect-sync-feature-preferreddatalocation" target="_blank">Azure Active Directory Connect sync: Configure preferred data location for Microsoft 365 resources</a> to configure Preferred Data Location sync from your on-premises Active Directory Domain Services (AD DS) to Microsoft Entra ID.

We recommend that you include setting the user's Preferred Data Location (PDL) as a part of your standard user creation workflow.

>[!IMPORTANT]
>For new users with no OneDrive provisioned, license the account and wait at least 48 hours after a user's PDL is synchronized to Microsoft Entra ID for the changes to propagate before the user logs in to OneDrive. (Setting the preferred data location before the user logs in to provision their OneDrive ensures that the user's new OneDrive will be provisioned in the correct location.)

## Setting Preferred Data Location (PDL) for cloud only users

>[!NOTE]
> The Azure Active Directory module is being replaced by the Microsoft Graph PowerShell SDK. You can use the Microsoft Graph PowerShell SDK to access all Microsoft Graph APIs. For more information, see [Get started with the Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/powershell/microsoftgraph/get-started).

First, use a **Microsoft Entra DC admin** or **Cloud Application Admin** account to [connect to your Microsoft 365 tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-to-microsoft-365-powershell).

```powershell
Connect-Graph -Scopes User.ReadWrite.All
```

Use the following script format:

```PowerShell
$userUPN="<user's UPN>"
$user = Get-MgUser -UserId $userUPN
Update-MgUser -UserId $user.Id -PreferredDataLocation <international location code>
```

In this example, you set the user adelev@contoso.com's preferred data location to EUR:

```powershell
$userUPN="adelev@contoso.com"
$user = Get-MgUser -UserId $userUPN
Update-MgUser -UserId $user.Id -PreferredDataLocation EUR
```

You can check to confirm that the preferred data location was updated properly by navigating to the Microsoft 365 Admin Center and selecting **Settings > Users > Active Users > [username]**. Select the user from the list, and you'll find Preferred Data Location under the **Account** tab of the user's page.

We recommend that you include setting the user's Preferred Data Location as a part of your standard user creation workflow.

>[!IMPORTANT]
>For new users with no OneDrive provisioned, license the account and wait at least 48 hours after a user's PDL is set for the changes to propagate before the user logs in to OneDrive. (Setting the preferred data location before the user logs in to provision their OneDrive ensures that the user's new OneDrive will be provisioned in the correct location.)

## OneDrive Provisioning and the effect of PDL

If the user already has a OneDrive site created in the _Tenant_, setting their PDL won't automatically move their existing OneDrive. To move a user's OneDrive, see [OneDrive Geo Move](https://learn.microsoft.com/en-us/microsoft-365/enterprise/move-onedrive-between-geo-locations).

> [!NOTE]
> Exchange Online automatically relocates the user's mailbox if the PDL changes and the MailboxRegion no longer matches the Mailbox Database Geo Location code. For more information, see [Administering Exchange Online mailboxes in a multi-geo environment](https://learn.microsoft.com/en-us/microsoft-365/enterprise/administering-exchange-online-multi-geo).

If the user doesn't have a OneDrive site within the _Tenant_, OneDrive will be provisioned for them in accordance to their PDL value, assuming the PDL for the user matches one of the company's satellite locations.
