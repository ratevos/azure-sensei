# OneDrive Cross-tenant OneDrive migration Step 2

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step2  
> Microsoft doc last updated: 10/13/2023


This article is Step 2 in a solution designed to complete a Cross-tenant OneDrive migration. To learn more, see [Cross-tenant OneDrive migration overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration).

- Step 1: [Connect to the source and the target tenants](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step1)
- **Step 2: [Establish trust between the source and the target tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step2)**
- Step 3: [Verify trust is established](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step3)
- Step 4: [Precreate users and groups](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step4)
- Step 5: [Prepare identity mapping](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step5)
- Step 6: [Start a Cross-tenant OneDrive migration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step6)
- Step 7: [Post migration steps](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step7)

After you connect to the source and target tenant, the next step in performing a cross-tenant OneDrive migration is establishing trust between the tenants.

To establish trust, each SharePoint tenant administrator must run specific commands on both source and target tenants. Once the trust is requested, the administrator of the target tenant receives an email informing them that another tenant is trying to establish a trust relationship.

> [!NOTE]
> The "trust" command is specific to SharePoint. It only grants permission for the SharePoint administrator on the source tenant to execute OneDrive Migration operations to the identified target tenant.
>
> Granting trust *doesn't* give the administrator any visibility, permission, or ability to collaborate between the source tenant and the target tenant.

> [!IMPORTANT]
> If you're a Microsoft 365 Multi-Geo customer, you must establish trust between each geography involved in your migration project.

## Before you begin

Before running the trust commands, obtain the cross-tenant host URLs for both the source and target tenants. You need these URLs when establishing the trust relationship between source-to-target and target-to-source.

**To obtain the cross-tenant host URLs:**

On both the source and target tenants, run:

```powershell
Get-SPOCrossTenantHostURL
```

*Example:* Run command on Source tenant:

 

*Example:* Run command on target tenant:

## Run the trust commands

These commands send a request to the tenant with whom you want to establish trust.

1. On the source tenant, run this command to send a trust request to the target tenant:

   ```powershell
   Set-SPOCrossTenantRelationship -Scenario MnA -PartnerRole Target -PartnerCrossTenantHostUrl <TARGETCrossTenantHostUrl>
   ```

2. On the target tenant, run this command to send a trust request to the source tenant:

   ```powershell
   Set-SPOCrossTenantRelationship -Scenario MnA -PartnerRole Source -PartnerCrossTenantHostUrl <SOURCECrossTenantHostUrl>
   ```

### Parameter definitions

|Parameter                 |Definition |
|--------------------------|-----------|
|PartnerRole               |Roles of the partner tenant you're establishing trust with. Use *source* if partner tenant is the source of the OneDrive migrations, and *target* if the partner tenant is the Destination. |
|PartnerCrossTenantHostURL |The cross-tenant host URL of the partner tenant. You can determine the URL by running: *Get-SPOCrossTenantHostURL* on each of the tenants.|

## Sample trust email

The following screenshot is an example of the email sent to global admins:

**Subject:**  SPO Tenant [https://a830edad9050849mnaus093022-my.sharepoint.com/] [setuporupdate] Organization Relation [Scenario=MnA, Role=Source] with us

**Message:**  SPO Tenant [https://a830edad9050849mnaus093022-my.sharepoint.com/] [setuporupdate] Organization Relation [Scenario=MnA, Role=Source] with us

> [!IMPORTANT]
> Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

## Step 3: [Verify that trust is established](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration-step3)
