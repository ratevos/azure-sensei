# SharePoint Cross-tenant SharePoint migration Step 3

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-sharepoint-migration-step3  
> Microsoft doc last updated: 10/01/2025


This article is Step 3 in a solution designed to complete a **Cross-tenant SharePoint migration.** To learn more, see [Cross-tenant SharePoint migration overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration).

- Step 1: [Connect to the source and the target tenants](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step1)
- Step 2: [Establish trust between the source and the target tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step2) 
- **Step 3: [Verify trust is established](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step3)** 
- Step 4: [Precreate users and groups](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step4)  
- Step 5: [Prepare identity mapping](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step5)
- Step 6: [Start a Cross-tenant SharePoint migration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step6)
- Step 7: [Post migration steps](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step7)

Before proceeding with your migration,  you need to verify the trust is complete. A status of *GoodToProceed* confirms that the trust is verified.

## To verify trust is established

1. On the **source tenant** run:
 
```powershell

Verify-SPOCrossTenantRelationship -Scenario MnA -PartnerRole Target -PartnerCrossTenantHostUrl <TARGETCrossTenantHostUrl>

```
2. On the **target tenant** run:

```powershell 

Verify-SPOCrossTenantRelationship -Scenario MnA -PartnerRole Source -PartnerCrossTenantHostUrl <SOURCECrossTenantHostUrl>
```

## Troubleshooting trust issues

When you verify the trust, the possible values are:

|Value                   |Description                                                                       |
|:-----------------------|:---------------------------------------------------------------------------------|
|NotEstablished          |Trust wasn't requested locally.                                                   |
|NotEstablishedByPartner |Partner didn't request the Trust.                                                 |
|DormantByPartner        |Partner’s requested trust is within the seven days waiting period after creation. |
|CouldNotContactPartner  |Couldn't contact the partner to determine status.                                 |
|GoodToProceed           |Verified to proceed.                                                              |

## Step 4: [Precreate users and groups](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step4)
