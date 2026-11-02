# Get started with collecting files that match data loss prevention policies from devices

> Source: https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started  
> Microsoft doc last updated: 2026-06-26


This article walks you through the prerequisites and configuration steps for evidence collection for file activities on devices and introduces how to view the items that are copied and saved.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

Here are the high level steps for configuring and using evidence collection for file activities on devices.

1. Onboard devices
2. Understand your requirements
3. Create your managed Azure storage account
4. Add an Azure storage blob to your account
5. Enable and configure evidence collection on a storage account managed by Microsoft
6. Configure your DLP policy
7. View usage of Microsoft managed storage

## Before you begin

Before you start these procedures, you should review [Learn about evidence collection for file activities on devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-learn).

## Licensing requirements for evidence collection

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

See the prerequisites [licensing requirements for Microsoft Entra ID P1 or P2](https://learn.microsoft.com/en-us/en-us/azure/active-directory/roles/custom-enterprise-apps) needed to create custom role-based access control (RBAC).

## Permissions

Standard Microsoft Purview Data Loss Prevention (DLP) permissions are required. For more information, see [Permissions](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions).

### Permissions for preview or download of evidence

When you want to preview or download the evidence, the account used needs to be in these roles:

- Preview the evidence: Data Classification Content Viewer
- Download the evidence: Data Classification Content Download

The Data Classification Content Download role is preassigned to these built-in role groups:

- Data Security Management
- Information Protection
- Information Protection Investigators

If you need to manage users, roles and role groups, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/en-us/purview/purview-permissions).

## Onboard devices

Before you can use copy matched items you have to onboard Windows 10/11 devices or macOS devices (Preview) into Purview, see [Onboard Windows devices into Microsoft 365 overview](https://learn.microsoft.com/en-us/purview/device-onboarding-overview#onboard-windows-devices-into-microsoft-365-overview).

## Understand your requirements

Important

Each container inherits the permissions of the storage account that it is in. You can't set different permissions per container. If you need to configure different permissions for different regions, you must create multiple storage accounts, not multiple containers.

You should have answers to the following question before setting up your Azure storage and scoping the feature to users.

### Do you need to compartmentalize items and access along role or departmental lines?

For example, if your organization wants to have one set of administrators or DLP event investigators who can view saved files from your senior leadership and another set of administrators or DLP event investigators for saved items from human resources, you should create one Azure storage account for your organization's senior leadership and another for the Human Resources department. This ensures that the Azure storage admins or DLP event investigators can only see the items that matched DLP policies from their respective groups.

### Do you want to use containers to organize saved items?

You can create multiple evidence containers within the same storage account for sorting saved files. For example, one for files saved from the HR department and another for those from the IT department.

### What is your strategy for protecting against saved item deletion or modification?

In Azure Storage, data protection refers to both the strategies for protecting the storage account and data within it from being deleted or modified and to restoring data after it's deleted or modified. Azure storage also offers options for disaster recovery, including multiple levels of redundancy, to protect your data from service outages due to hardware problems or natural disasters. It can also protect your data using customer-managed failover if the data center in the primary region becomes unavailable. For more information, see [Data protection overview](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/data-protection-overview).

You can also configure immutability policies for your blob data that protects against the saved items being overwritten or deleted. For more information, see [Store business-critical blob data with immutable storage](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/immutable-storage-overview)

## Supported file types for storing and previewing evidence

The following table shows which file types can be stored and previewed as evidence.

| Can be Stored | Can be Previewed |
| --- | --- |
| All file types provided they match the policy | All file types supported for [previewing files in OneDrive, SharePoint, and Teams](https://support.microsoft.com/office/file-types-supported-for-previewing-files-in-onedrive-sharepoint-and-teams-e054cd0f-8ef2-4ccb-937e-26e37419c5e4) |

Note

To understand how to create policies for different file types see [Create and deploy DLP policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy)

## Save matched items to your preferred storage

To save the evidence that Microsoft Purview detects when your data loss prevention policies are applied, you need to set up storage. There are two ways to set up storage for evidence collection:

1. Create customer-managed storage
2. Create Microsoft-managed storage

For more information and a comparison of these two types of storage, see [Storing evidence when sensitive information is detected](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-learn#storing-evidence-when-sensitive-information-is-detected).

### Create customer-managed storage

The procedures for setting up your Azure storage account, container, and blobs are documented in the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/). Here are links to relevant articles you can refer to help you get started:

1. [Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/storage-blobs-introduction)
2. [Create a storage account](https://learn.microsoft.com/en-us/en-us/azure/storage/common/storage-account-create)
3. [Default to and authorize access to blobs using Microsoft Entra ID](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/authorize-access-azure-active-directory)
4. [Manage blob containers using the Azure portal](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/blob-containers-portal)
5. [Manage block blobs with PowerShell](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/blob-powershell)

Note

Make sure to select **Enable public access from all networks while creating the storage account**. Support for Virtual networks and IP addresses and use of private access isn't available

Be sure to save the name and URL of the Azure blob container. To view the URL, open the Azure storage portal &gt; **Home** &gt; **Storage Accounts** &gt; **Container** &gt; **Properties**

The format for the Azure blob container URL is:`https://storageAccountName.blob.core.windows.net/containerName`.

### Add an Azure storage blob to your account

There are several ways you can add an Azure storage blob to your account. Chose *one* of the methods below.

1. Sign in to the Microsoft Purview portal and choose the **Settings** gear in the menu bar.
2. Choose **Data Loss Prevention**.
3. Select **Endpoint DLP settings**.
4. Expand **Setup evidence collection for file activities on devices**.
5. Change the toggle from **Off** to **On**.
6. In the **Set evidence cache on device** field, select the amount of time evidence should be saved locally when the device is offline. You can choose **7**, **30**, or **60** days.
7. Select a **storage type** (*Customer managed store* or *Microsoft managed store*) and then select **+ Add storage**.
    1. For **Customer-managed storage**:
        1. Choose **Customer managed store**: and then choose **+ Add storage**.
        2. Enter give the account a name and enter the **URL** for the storage blob.
        3. Choose **Save**.
    2. For **Microsoft-managed storage**:
        1. Choose **Microsoft managed store**

To add Azure blob storage using the DLP policy creation workflow in the Microsoft Purview portal:

1. Sign in to the Microsoft Purview portal and choose **Data Loss Prevention**.
2. Follow the steps to create a new policy.
3. At the **Locations** step, make sure that only the **Devices** location is selected, and then choose **Next**.
4. At the Policy settings step, select Create or customize advanced DLP rules.
5. Select **+Create rule** and add **Conditions**, **Actions**, **User notifications** and **User overrides** with values of your choosing.
6. In the **Incident reports** section, the **Send an alert to admins when a rule match occurs** toggle should be **On** by default. (If it isn’t, turn it on.)
7. Select the checkbox next to **Collect original file as evidence for all selected file activities on Endpoint**.
8. Select the activities you want to collect evidence for.
9. Select **Add storage** next to the checkbox item.
10. On the **Endpoint DLP settings** page, expand **Setup evidence collection for file activities on devices** and make sure that the option is toggled to **On**.

### Set permissions on the Azure blob storage

Using Microsoft Entra authorization, you must configure two sets of permissions (role groups) on the blobs:

1. One for the administrators and investigators so they can view and manage evidence
2. One for users who need to upload items to Azure from their devices

Best practice is to enforce *least privilege* for all users, regardless of role. By enforcing least privilege, you ensure that user permissions are limited to only those permissions necessary for their role. To configure user permissions, [create roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](https://learn.microsoft.com/en-us/en-us/microsoft-365/security/office-365-security/scc-permissions).

#### Permissions on Azure blob for administrators and investigators

Once you create the role group for DLP incident investigators, you must configure the permissions described in the Investigator actions and Investigator data actions sections that follow.

For more information on configuring blob access, see these articles:

- [How to authorize access to blob data in the Azure portal](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/authorize-data-operations-portal)
- [Assign share-level permissions](https://learn.microsoft.com/en-us/en-us/azure/storage/files/storage-files-identity-ad-ds-assign-permissions?tabs=azure-portal.md).

##### Investigator actions

Configure these object and action permissions for the investigator role:

| Object | Permissions |
| --- | --- |
| Microsoft.Storage/storageAccounts/blobServices | Read: List Blob Services |
| Microsoft.Storage/storageAccounts/blobServices | Read: Get blob service properties or statistics |
| Microsoft.Storage/storageAccounts/blobServices/containers | Read: Get blob container |
| Microsoft.Storage/storageAccounts/blobServices/containers | Read: List of blob containers |
| Microsoft.Storage/storageAccounts/blobServices/containers/blobs | Read: Read blob |
| Microsoft.Storage/storageAccounts/blobServices/generateUserDelegationKey/action | Other: Generate a user delegation key |

##### Investigator data actions

Assign the following data actions to the investigator role.

| Object | Permissions |
| --- | --- |
| Microsoft.Storage/storageAccounts/blobServices/containers/blobs | Read: Read Blob |

Your JSON for the investigator role group should look like this:

```json
"permissions": [
            {
                "actions": [
                 "Microsoft.Storage/storageAccounts/blobServices/read",
                 "Microsoft.Storage/storageAccounts/blobServices/containers/read",
                 "Microsoft.Storage/storageAccounts/blobServices/generateUserDelegationKey/action"
                ],
                "notActions": [],
                "dataActions": [
                    "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read"
                ],
                "notDataActions": []
            }
        ]
```

#### Permissions on Azure blob for users

Assign these object and action permissions to the Azure blob for the user role:

##### User actions

Assign the following object and action permissions to the user role.

| Object | Permissions |
| --- | --- |
| Microsoft.Storage/storageAccounts/blobServices | Read: List Blob Services |
| Microsoft.Storage/storageAccounts/blobServices/containers | Read: Get blob container |
| Microsoft.Storage/storageAccounts/blobServices/containers | Write: Put blob container |

##### User data actions

Assign the following data actions to the user role.

| Object | Permissions |
| --- | --- |
| Microsoft.Storage/storageAccounts/blobServices/containers/blobs | Write: Write Blob |
| Microsoft.Storage/storageAccounts/blobServices/containers/blobs | Other: Add blob content |

The JSON for user role group should look like this:

```json
"permissions": [
  {
     "actions": [
       "Microsoft.Storage/storageAccounts/blobServices/containers/read",
       "Microsoft.Storage/storageAccounts/blobServices/containers/write",
       "Microsoft.Storage/storageAccounts/blobServices/read"
     ],
     "notActions": [],
     "dataActions": [
         "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action",
         "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write"
     ],
     "notDataActions": []
    }
 ]

```

### Enable and configure evidence collection on a storage account managed by Microsoft

To enable and configure evidence collection on a storage account managed by Microsoft from within the Microsoft Purview portal:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Settings** gear in the menu bar.
2. Choose **Data Loss Prevention**.
3. Select **Endpoint DLP settings**.
4. Expand **Setup evidence collection for file activities on devices** and set the toggle to **On**.
5. Under **Select storage type**, choose **Microsoft managed storage**.

Tip

After you configure Microsoft-managed storage, you can use [Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-search#endpoint-dlp-evidence-collection-preview) to query and analyze evidence collected from endpoint DLP policies across multiple users and time periods.

### Configure your DLP Policy

Create a DLP policy as you normally would. For policy configuration examples, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy).

Configure your policy using these settings:

- Make sure that **Devices** is the only location selected.
- In **Incident reports**, toggle **Send an alert to admins when a rule match occurs** to **On**.
- In **Incident reports**, select **Collect original file as evidence for all selected file activities on Endpoint**.
- Select the storage account you want.
- Select the activities for which you want to copy matched items to Azure storage, such as:
    - **Access by restricted apps (preview)**
    - **Paste to supported browsers**
    - **Upload to cloud service domains or access unallowed browsers**
    - **Copy to a removable USB device**
    - **Copy to a network share**
    - **Print**
    - **Copy or move using an unallowed Bluetooth app**
    - **Copy or move using RDP**
    - **FTP and SFTP transfers**

## View usage of Microsoft Managed Storage

You can view and export the daily usage for past 6 months for Microsoft Managed storage.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Settings** gear in the menu bar.
2. Choose **Data Loss Prevention**.
3. Select **Endpoint DLP settings**.
4. Expand **Setup evidence collection for file activities on devices**.
5. Click on **View Usage** button, a panel will open. Here you can see month wise graph of daily usage and also export the usage data.

## Preview and Download the evidence

There are different ways to preview your evidence, depending on which type of storage you select.

| Storage Type | Preview options |
| --- | --- |
| Customer-managed | - Use activity explorer - Use the Microsoft Purview portal |
| Microsoft Managed | - Use activity explorer - Use the Purview portal |

Note

Reminder, the account you use to preview and download needs to be in these roles:

- Preview the evidence: Data Classification Content Viewer
- Download the evidence: Data Classification Content Download

### Preview evidence via Activity explorer

Use the following steps to preview evidence in Activity explorer.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Activity explorer**.
2. Using the **Date** dropdown, select the **Start** and **End** dates for the period you’re interested in.
3. In the list of results, double-click the line item of the activity you want to investigate.
4. In the flyout pane, the link to the Azure blob where the evidence is stored appears under **Evidence file**.
5. Select the Azure blob storage link to display the file that was matched.

### Preview evidence via the Purview portal Alerts page

Use the following steps to preview evidence from the Alerts page in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Alerts**.
2. Using the **Date** dropdown, select the **Start** and **End** dates for the period you’re interested in.
3. In the list of results, double-click the line item of the activity you want to investigate.
4. In the flyout pane, select **View details**.
5. Select the **Events** tab.
6. In the **Detail** pane, select the **Source tab**. The file that was matched displays.

Note

If the file that was matched already exists in the Azure storage blob, it won't be uploaded again until changes are made to the file and a user takes an action on it.

## Known issues

- The maximum size for files that can be uploaded from a device is 500 MB.
- If [Just-in-Time Protection](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#just-in-time-protection) is triggered on a scanned file, OR if the file is stored on a network share, the evidence file is not collected.
- When multiple files are opened in the same process (non-office apps) and one of the files matching a policy is egressed, DLP events are triggered for all files. No evidence is captured.
- If multiple policy rules are detected in a single file, the evidence file is only stored if the most restrictive policy rule is configured to collect evidence.
