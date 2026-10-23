# SharePoint Cross-tenant SharePoint migration Step 1

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-sharepoint-migration-step1  
> Microsoft doc last updated: 10/01/2025


This article is Step 1 in a solution designed to complete a **Cross-tenant SharePoint migration**. To learn more, see [Cross-tenant SharePoint migration overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration).

- **Step 1: [Connect to the source and the target tenants](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step1)**
- Step 2: [Establish trust between the source and the target tenant](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step2) 
- Step 3: [Verify trust is established](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step3) 
- Step 4: [Precreate users and groups](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step4)  
- Step 5: [Prepare identity mapping](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step5)
- Step 6: [Start a Cross-tenant SharePoint migration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step6)
- Step 7: [Post migration steps](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step7)

## Before you begin

- **Microsoft SharePoint Powershell**. Confirm you have the most recent version installed. If not, [Download SharePoint Management Shell from Official Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=35588).
- Be a SharePoint admin or Microsoft 365 Global admin on both the source and target tenants.

> [!IMPORTANT]
> Microsoft recommends that you use roles with the fewest permissions. This usage helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

### Connect to both tenants

1. Sign in to the SharePoint Management Shell as a SharePoint admin or Microsoft 365 Global admin.
2. Run the following entering the **source** tenant URL: 

    ```powershell
    Connect-SPOService -url https://<TenantName>-admin.sharepoint.com
    ```

3. When prompted, sign in to the **source** tenant using your Admin username and password.
 
4. Run the following entering the **target** tenant URL: 

    ```powershell
    Connect-SPOService -url https://<TenantName>-admin.sharepoint.com
    ```

5. When prompted, sign in to the **target** tenant using your Admin username and password.

> [!IMPORTANT]
> **Microsoft 365 Multi-Geo customers:** You must treat each geography as a separate tenant. Provide the correct geography-specific URLs throughout the migration process.

## Step 2: [Establish trust between the source and target tenants](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-SharePoint-migration-step2)
