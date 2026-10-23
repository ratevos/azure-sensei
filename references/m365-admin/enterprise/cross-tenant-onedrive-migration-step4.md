# OneDrive Cross-tenant OneDrive migration Step 4

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step4  
> Microsoft doc last updated: 08/14/2025


This article is Step 4 in a solution designed to complete a Cross-tenant OneDrive migration. To learn more, see [Cross-tenant OneDrive migration overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration).

- Step 1: [Connect to the source and the target tenants](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step1)
- Step 2: [Establish trust between the source and the target tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step2) 
- Step 3: [Verify trust is established](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step3) 
- **Step 4: [Precreate users and groups](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step4)**  
- Step 5: [Prepare identity mapping](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step5)
- Step 6: [Start a Cross-tenant OneDrive migration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step6)
- Step 7: [Post migration steps](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step7)

## Identify users and groups to be migrated

To ensure that OneDrive permissions are retained as part of the migration, a mapping file needs to be created to align users from the source tenant to the target tenant.

1. Identify the full list of OneDrive sites to be migrated from the source to the target tenant.
2. Prepare a complete list of users and groups to be migrated to the target tenant.

## Precreate users and groups on the target tenant

1. Precreate users and groups as needed in the target tenant’s directory.
2. All users whose OneDrive accounts are migrating to the target tenant must have new user identities created for them in the target tenant.
3. All users whose OneDrive accounts are migrating to the target tenant must be assigned the appropriate OneDrive license.
4. Any users who remain in the source tenant but need access to resources migrating to the target tenant should have new guest identities created for them in the target tenant.
5. Precreated users must be added as members of any appropriate security groups or unified groups before the OneDrive migration begins.
6. If the user or group name already exists in the target tenant, create a user or group with a different name and make a note of it for the next step.
7. We recommend that OneDrive site creations are restricted in the target tenant to prevent users from creating OneDrive sites.

## For tenants with Multi-Geo

When creating Microsoft 365 group objects, we recommend you assign the group to the geo instance the site's to be migrated to at the time of creation. The "MailboxRegion" is used to set the residency of the group object. 

   ```powershell
   New-UnifiedGroup -DisplayName MultiGeoEUR -Alias "MultiGeoEUR" -AccessType Public -MailboxRegion EUR
   ```

>[!NOTE]
>If the group site is outside the default instance, the MailboxRegion (PDL) must be set.
>For more information, see [Create a Microsoft 365 Group with a specific preferred data location](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-add-group-with-pdl).

>[!NOTE]
>To learn more on restricting OneDrive site creation, see [Disable OneDrive creation for some users](https://learn.microsoft.com/en-us/sharepoint/manage-user-profiles#disable-onedrive-creation-for-some-users).

## Step 5: [Prepare the identity mapping file](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step5)
