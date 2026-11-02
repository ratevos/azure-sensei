# Configure endpoint DLP settings

> Source: https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings  
> Microsoft doc last updated: 2026-06-26


Centrally configured settings control many aspects of endpoint data loss prevention (DLP) behavior. These settings apply to all DLP policies for devices. Use these settings to control the following behaviors:

- Cloud egress restrictions
- Various types of restrictive actions on user activities per application
- File path exclusions for Windows and macOS devices
- Browser and domain restrictions
- Appearance of business justifications for overriding policies in policy tips
- Whether actions performed on Office, PDF, and CSV files are automatically audited

To access these settings, from the Microsoft Purview portal, go to **Data loss prevention** &gt; **Overview** &gt; **Data loss prevention settings** &gt; **Endpoint settings**.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

Important

For information about the Adobe requirements for using Microsoft Purview Data Loss Prevention (DLP) features with PDF files, see this article from Adobe: [Microsoft Purview Information Protection Support in Acrobat](https://helpx.adobe.com/enterprise/kb/mpip-support-acrobat.html).

## Advanced classification scanning and protection

When you turn on advanced classification scanning and protection, the Microsoft Purview cloud-based data classification service scans items, classifies them, and returns the results to the local machine. Because advanced classification runs in the cloud, you can take advantage of classification techniques such as [exact data match](https://learn.microsoft.com/en-us/purview/sit-learn-about-exact-data-match-based-sits) classification, [trainable classifiers](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with#get-started-with-trainable-classifiers), [credential classifiers](https://learn.microsoft.com/en-us/purview/sit-defn-all-creds#all-credential-types), and [named entities](https://learn.microsoft.com/en-us/purview/named-entities-learn) in your DLP policies.

Note

The **Paste to browser** action doesn't support advanced classification.

When you turn on advanced classification, the local device sends content to the cloud services for scanning and classification. If you're concerned about bandwidth usage, set a limit on how much bandwidth can be used in a rolling 24-hour period. You configure the limit in **Endpoint DLP settings** and it applies per device. If you set a bandwidth usage limit and that usage limit is exceeded, DLP stops sending the user content to the cloud. At that point, data classification continues locally on the device but classification by using exact data match, named entities, trainable classifiers, and credential classifiers isn't available. When the cumulative bandwidth usage drops below the rolling 24-hour limit, communication with the cloud services resumes.

If bandwidth usage isn't a concern, select **Do not limit bandwidth. Unlimited** to allow unlimited bandwidth use.

### Advanced classification file scanning size limits

Even if you enable **Do not limit bandwidth. Unlimited** for advanced classification, limits still exist on the size of individual files that the system can scan.

- There's a 64-MB limit on text files.
- There's a 50-MB limit on image files when Optical Character Recognition (OCR) is enabled.

Advanced classification doesn't work for text files larger than 64 MB, even if you set the bandwidth limit to **Do not limit bandwidth. Unlimited**.

The following Windows versions (and later versions) support advanced classification scanning and protection.

- All Windows 11 versions
- Windows 10 versions 20H1/21H1 or higher (KB 5006738)
- Windows 10 RS5 (KB 5006744)

Note

- Support for advanced classification is available for Office (Word, Excel, PowerPoint) and PDF file types.
- DLP policy evaluation always occurs in the cloud, even if user content isn't being sent.

Tip

To use advanced classification for Windows 10 devices, you must install KB5016688. To use advanced classification for Windows 11 devices, you must install KB5016691 on those Windows 11 devices. Additionally, you must enable advanced classification before **Activity explorer** displays contextual text for DLP rule-matched events. To learn more about contextual text, see the "Contextual summary" section in [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#contextual-summary).

## Advanced label-based protection for all files on devices

When you turn on advanced label-based protection, users can work on files - including files other than Office and PDF files - that have sensitivity labels applying access control settings in an unencrypted state, on their devices. Endpoint DLP continues to monitor and enforce access control and label-based protections on these files even in an unencrypted state. It automatically encrypts them before they're transferred outside from a user's device. For more information about advanced label-based protection, see [Learn about Advanced Label Based Protection](https://learn.microsoft.com/en-us/purview/dlp-learn-about-advanced-label-protection).

Note

Advanced label-based protection is supported only on onboarded Windows devices.

## File path exclusions

To exclude certain paths from DLP monitoring, DLP alerts, and DLP policy enforcement on your devices, set up file path exclusions to turn off those configuration settings. Files in excluded locations aren't audited. Any files that you create or modify in those locations aren't subject to DLP policy enforcement. To configure path exclusions in DLP settings, go to [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Overview** &gt; **Data loss prevention settings** &gt; **Endpoint settings** &gt; **File path exclusions for Windows**.

### File path exclusions for Windows

Use the following logic to construct your exclusion paths for Windows 10 and Windows 11 devices:

- A valid file path that ends with `\` means only files directly under the specified folder are excluded.  Example: `C:\Temp\`
- A valid file path that ends with `\*` means only files within subfolders of the specified folder are excluded. Files directly under the specified folder itself aren't excluded.  Example: `C:\Temp\*`
- A valid file path that ends without `\` or `\*` means all files directly under the specified folder and all of its subfolders are excluded.  Example: `C:\Temp`
- A path with a wildcard between `\` from each side.  Example: `C:\Users\*\Desktop\`
- A path with a wildcard between `\` from each side and with `(number)` to specify the exact number of subfolders to exclude.  Example: `C:\Users\*(1)\Downloads\`
- A path with SYSTEM environment variables.  Example: `%SystemDrive%\Test\*`
- A mix of all the patterns described here.  Example: `%SystemDrive%\Users\*\Documents\*(2)\Sub\`

#### Windows file paths excluded by default

- `%SystemDrive%\\Users\\*(1)\\AppData\\Roaming`
- `%SystemDrive%\\Users\\*(1)\\AppData\\Local`

### File path exclusions for Mac

You can also add your own exclusions for macOS devices.

- File path definitions are case insensitive, so `User` is the same as `user`.
- Wildcard values are supported. So a path definition can contain an asterisk (`*`) in the middle of the path or at the end of the path.  Example: `/Users/*/Library/Application Support/Microsoft/Teams/*`

#### macOS file paths excluded by default

`/System`

#### Recommended file path exclusions for macOS

For performance reasons, Endpoint DLP includes a list of recommended file path exclusions for macOS devices. If you set the **Include recommended file path exclusions for Mac** toggle to **On**, the following paths are also excluded:

- `/Applications`
- `/usr`
- `/Library`
- `/private`
- `/opt`
- `/Users/*/Library/Logs`
- `/Users/*/Library/Containers`
- `/Users/*/Library/Application Support`
- `/Users/*/Library/Group Containers`
- `/Users/*/Library/Caches`
- `/Users/*/Library/Developer`

Keep the **Include recommended file path exclusions for Mac** toggle set to **On**. However, you can stop excluding these paths by setting the **Include recommended file path exclusions for Mac** toggle to **Off**.

## Set up evidence collection for file activities on devices

When DLP identifies items that match policies on devices, it can copy them to an [Azure storage account](https://learn.microsoft.com/en-us/en-us/azure/storage/common/storage-account-overview). Copying matched items to an Azure storage account is useful for auditing policy activity and troubleshooting specific matches. Use the **Set up evidence collection for file activities on devices** settings to add the name and URL of the storage account.

Note

Before you enable evidence collection, create an Azure storage account and a container in that storage account. You must also configure permissions for the account. As you set up your Azure storage account, keep in mind that you probably want to use a storage account that's in the same Azure region or geopolitical boundary as your tenant. Consider configuring [Azure storage account access tiers](https://learn.microsoft.com/en-us/en-us/azure/storage/blobs/storage-blob-storage-tiers) and [Azure storage account pricing](https://learn.microsoft.com/en-us/en-us/azure/storage/common/storage-account-overview#pricing).

- For more information on copying matched items to Azure storage, see [Learn about collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-learn).
- For more information on how to configure this feature, see [Get started with collecting files that match data loss prevention policies from devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started).

## Network share coverage and exclusions

**Network share coverage and exclusions** extends endpoint DLP policies and actions to new and edited files on network shares and mapped network drives. If [just in time protection](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#just-in-time-protection) is also enabled, just in time protection coverage and exclusions are extended to network shares and mapped drives. To exclude a specific network path for all monitored devices, add the path value in **Exclude these network share paths**.

Important

To use **Network share coverage and exclusions**, devices must have the following updates applied:

- Windows 10 - [March 21, 2023—KB5023773 (OS Builds 19042.2788, 19044.2788, and 19045.2788) Preview](https://support.microsoft.com/topic/march-21-2023-kb5023773-os-builds-19042-2788-19044-2788-and-19045-2788-preview-5850ac11-dd43-4550-89ec-9e63353fef23), [March 28, 2023—KB5023774 (OS Build 22000.1761) Preview](https://support.microsoft.com/topic/march-28-2023-kb5023774-os-build-22000-1761-preview-67b4cfda-120a-422f-98c0-35124ddba839)
- Windows 11 - [March 28, 2023—KB5023778 (OS Build 22621.1485) Preview](https://support.microsoft.com/topic/march-28-2023-kb5023778-os-build-22621-1485-preview-d490bb51-492e-410c-871f-50ad01b0f765)
- Microsoft Defender [April-2023 (Platform: 4.18.2304.8 | Engine: 1.1.20300.3)](https://learn.microsoft.com/en-us/en-us/defender-endpoint/microsoft-defender-antivirus-updates#april-2023-platform-41823048--engine-11203003)
- macOS Last 3 OS versions supported; Minimum Defender app version supported - 101.24122.0005

The following table shows the default settings for network share coverage and exclusions.

| Network share coverage and exclusions | Just in time protection | Resultant behavior |
| --- | --- | --- |
| Enabled | Disabled | - DLP policies scoped to Devices are applied to all network shares and mapped drives that the device connects to. [Supported actions: Devices](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#supported-actions-devices) |
| Disabled | Enabled | - Just-in-time protection is applied only to the files on storage devices that are local to the endpoint. |
| Enabled | Enabled | - DLP policies scoped to Devices are applied to all network shares and mapped drives that the device connects to. [Supported actions: Devices](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#supported-actions-devices)- Just-in-time protection is applied to all network shares and mapped drives that the device connects to. |
|  |  |  |

**Network share coverage and exclusions** complements [DLP On-premises repository actions](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-learn#dlp-on-premises-repository-actions). The following table shows the exclusion settings and the resulting behavior depending on whether DLP is enabled or disabled for on-premises repositories.

| Network share coverage and exclusions | DLP on-premises repositories | Resultant behavior |
| --- | --- | --- |
| Enabled | Disabled | - DLP policies scoped to Devices are applied to all network shares and mapped drives that the device connects to. [Supported actions: Devices](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#supported-actions-devices) |
| Disabled | Enabled | - Policies that are scoped to On-premises repositories can enforce protective actions on on-premises data-at-rest in file shares and SharePoint document libraries and folders. [DLP On-premises repository actions](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-learn#dlp-on-premises-repository-actions) |
| Enabled | Enabled | - DLP policies scoped to Devices are applied to all network shares and mapped drives that the device connects to. [Supported actions: Devices](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#supported-actions-devices)- Policies that are scoped to On-premises repositories can enforce protective actions on on-premises data-at-rest in file shares and SharePoint document libraries and folders. [DLP On-premises repository actions](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-learn#dlp-on-premises-repository-actions) |
|  |  |  |

## Restricted apps and app groups

### Restricted apps

The **Restricted apps** list is a custom list of applications that you create. You configure what actions DLP takes when someone uses an app on the list to ***access*** a DLP-protected file on a device. The **Restricted apps** list is available for Windows 10/11 and macOS devices running any of the three latest macOS releases.

Some apps have a web-based interface in addition to a locally installed version of the application. In preview, when you add an app that users can access both locally and through a web-based interface to a **Restricted app group** or as a **Restricted app**, DLP enforces any applicable policies for accessing a protected file through Edge for the browser app interface and on the device for the application-based interface.

Important

- Don't include the path to the executable for Windows devices. Include only the executable name, such as `browser.exe`.
- The action (`audit`, `block with override`, or `block`) that you define for apps on the restricted apps list only applies when a user attempts to ***access*** a protected item.

When you select **Access by restricted apps** in a policy and a user uses an app on the restricted apps list to access a protected file, the activity is `audited`, `blocked`, or `blocked with override`, depending on how you configured the **Restricted apps** list. If an app on the **Restricted apps** list is also a member of a **Restricted app group**, the actions you configure for activities in the **Restricted app group** override the actions you configure for the **Restricted apps** list. All activity is audited and available for review in activity explorer.

Important

Endpoint DLP protections trigger when a restricted app tries to access a file, either by a user or by the application itself. To exclude a path from enforcement, add it to the exclusion list. This path is where the files identified in Activity Explorer are located.

### Restricted app groups

Restricted app groups are collections of apps that you create in DLP settings and then add to a rule in a policy. When you add a restricted app group to a policy, you can take the actions defined in the following table.

| Restricted App group option | What it allows you to do |
| --- | --- |
| Don't restrict file activity | Tells DLP to allow users to access DLP protected items using apps in the app group without taking any action when the user attempts to **Copy to clipboard**, **Copy to a USB removable drive**, **Copy to a network drive**, or **Print** from the app. |
| Apply a restriction to all activity | Tells DLP to `Audit only`, `Block with override`, or `Block` when a user attempts to access a DLP-protected item using an app that's in the relevant app group |
| Apply restrictions to a specific activity | This setting allows a user to access a DLP-protected item using an app that is in the app group. It also allows you to select a default action (`Audit only`, `Block`, or `Block with override`) for DLP to take when a user attempts to **Copy to clipboard**, **Copy to a USB removable drive**, **Copy to a network drive**, and **Print**. |

You can add a maximum of 50 apps into a single group and you can create a maximum of 10 groups. This gives a maximum of 500 apps that the policy actions can be assigned to.

Important

Settings in a restricted app *group* override any restrictions set in the restricted apps *list* when they are in the same rule. So, if an app is on the restricted apps list and is also a member of a restricted apps group, the settings of the restricted apps group is applied.

#### Block all apps except for a list of allowed apps

You can create a list of allowed applications and block all others. By creating a list of allowed applications and blocking all others, you don't need to create and manage a comprehensive list of untrusted applications. This feature helps simplify policy management and enhances your control over app-based file activities.

Note

Common background applications such as **teamsupdate.exe** or **svchost.exe** are preconfigured to bypass enforcement to prevent unintentional interference with essential operations.

In this procedure, you apply the restriction level of **Allow** to explicitly allow activity for a defined app group, and then block any apps that aren't on this list. Because the policy blocks apps that aren't in the allowed group, apps that have no restriction level defined are effectively blocked, and apps that have a restriction level defined as **Allow** are explicitly allowed. You define a restricted app group to allow that app group, but you also define the restricted app group to block any apps that have no defined restrictions.

1. Go to endpoint DLP settings.
2. Define allowed or sanctioned apps in the **Restricted Apps and app groups** list.
3. In your existing or new endpoint DLP policy, locate the **File activities for apps in restricted app groups** setting.
4. Add the desired restricted app group.
5. Select **Apply restriction to all activity**, and select **Allow**. Audit and Off will not work.
6. For all other apps, set the **Access by apps that aren’t on the 'unallowed apps' list** setting to **Block**.

### How DLP applies restrictions to activities

Interactions between **File activities for apps in restricted app groups**, **File activities for all apps**, and the **Restricted app activities** list are scoped to the same rule.

#### Restricted app groups overrides

Configurations defined in **File activities for apps in restricted app groups** override the configurations in the **Restricted app activities** list and **File activities for all apps** in the same rule.

#### Restricted app activities and File activities for all apps

The configurations of **Restricted app activities** and **File activities for all apps** work in concert if the action defined for **Restricted app activities** is either `Audit only`, or `Block with override` in the same rule. Why? Actions defined for **Restricted app activities** only apply when a user accesses a file using an app that's on the list. Once the user has access, the actions defined for activities in **File activities for all apps** apply.

For example, you add Notepad.exe to **Restricted apps** and configure **File activities for all apps** to **Apply restrictions to specific activity**. You configure both as shown in the following table:

| Setting in policy | App name | User activity | DLP action to take |
| --- | --- | --- | --- |
| Restricted app activities | Notepad | Access a DLP protected item | Audit only |
| File activities for all apps | All apps | Copy to clipboard | Audit only |
| File activities for all apps | All apps | Copy to a USB removeable device | Block |
| File activities for all apps | All apps | Copy to a network share | Audit only |
| File activities for all apps | All apps | Print | Block |
| File activities for all apps | All apps | Copy or move using unallowed Bluetooth app | Blocked |
| File activities for all apps | All apps | Remote desktop services | Block with override |
|  |  |  |  |

When User A opens a DLP-protected file using Notepad, DLP allows the access and audits the activity. While still in Notepad, User A then tries to copy content from the protected item to the clipboard. This action is successful, and DLP audits the activity. User A then tries to print the protected item from Notepad and the activity is blocked.

Note

When the DLP action to take in **Restricted app activities** is set to `block`, all access is blocked and the user can't perform any activities on the file.

#### File activities for all apps only

If an app *isn't* in the **File activities for apps in restricted app groups** or the **Restricted app activities** list, or *is* in the **Restricted app activities** list, with an action of either `Audit only`, or `Block with override`, any restrictions defined in the **File activities for all apps** are applied in the same rule.

### macOS devices

You can also prevent macOS apps from accessing sensitive data by adding them to the **Restricted app activities** list.

Note

Enter cross-platform apps with their unique paths for the OS they're running on.

To find the full path of Mac apps:

1. On the macOS device, open **Activity Monitor**. Find and double-click the process you want to restrict.
2. Select the **Open Files and Ports** tab.
3. Make a note of the full path name, including the name of the app. For example,

- `/System/Applications/TextEdit.app/Contents/MacOS/TextEdit`

### Auto-quarantine

To prevent sensitive items from syncing to the cloud by cloud sync apps such as *onedrive.exe*, add the cloud sync app to the **Restricted apps** list with **Auto-quarantine**.

When enabled, autoquarantine triggers when a restricted app attempts to access a DLP-protected sensitive item. Auto-quarantine moves the sensitive item to an admin-configured folder. If configured to do so, autoquarantine can leave a placeholder (`.txt`) file in place of the original. You can configure the text in the placeholder file to tell users the new location of the item, and other pertinent information.

Use the autoquarantine feature when an unallowed cloud-sync app tries to access an item that is protected by a blocking DLP policy. DLP might generate repeated notifications. You can avoid these repeated notifications by enabling **Auto-quarantine**.

You can also use autoquarantine to prevent an endless chain of DLP notifications for the user and admins. For more information, see [Help prevent exposure of sensitive files by configuring auto-quarantine for OneDrive sync](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-auto-quarantine-for-onedrive)

## Unsupported file extension exclusions

Use the **Document could not be scanned** condition together with **Apply restrictions to only unsupported file extensions** in your DLP policies to restrict activities involving files with extensions that aren't supported by endpoint DLP. Because this condition can potentially include many unsupported file extensions, refine detection by adding unsupported extensions to exclude. For more information, see [Help protect files that Endpoint Data Loss Prevention doesn't scan](https://learn.microsoft.com/en-us/purview/dlp-create-policy-files-edlp-doesnt-scan) and [Help protect against sharing of a defined set of unsupported files](https://learn.microsoft.com/en-us/purview/dlp-create-policy-sharing-set-unsupported-files).

Note

Don't add a `.` when you add an extension. Use the latest anti-malware client version.

Important

When you select **Actions** &gt; **Audit or restrict activities on devices** rule configuration, the **Apply restrictions to only unsupported file extensions** option appears. The **Apply restrictions to only unsupported file extensions** configuration option doesn't support scoping by **Device and device groups** in the policy location setting.

Blocking specific file extensions in DLP policies can lead to unexpected behavior if an application that is marked as unallowed needs to access files with those extensions as part of its normal operation. For example, certain apps might read or temporarily open files, like `.dll`, `.json`, `.tmp` during routine processes such as rendering, caching, or validating content. If you block these extensions, the app might fail to function properly, causing errors, incomplete workflows, or enforcement pop-ups unrelated to user intent. Before implementing extension-based restrictions, make sure you know which apps interact with these file types during standard operations, and whether alternative controls, such as app restrictions or contextual rules, can achieve the security goal without disrupting functionality.

## Unallowed Bluetooth apps

To prevent people from transferring files protected by your policies via specific Bluetooth apps, add those apps to the **Unallowed Bluetooth apps** list in Endpoint DLP settings.

## Browser and domain restrictions to sensitive data

Restrict sensitive files that match your policies from being shared with unrestricted cloud service domains.

### Unallowed browsers

For Windows devices, you can restrict the use of specified web browsers by their executable names. The specified browsers can't access files that match the conditions of an enforced DLP policy where the upload-to-cloud services restriction is set to `block` or `block override`. When these browsers are blocked from accessing a file, end users see a toast notification asking them to open the file through Microsoft Edge.

For macOS devices, you must add the full file path. To find the full path of Mac apps:

1. On the macOS device, open **Activity Monitor**. Find and double-click the process you want to restrict.
2. Choose the **Open Files and Ports** tab.
3. Make sure to make a note of the full path name, including the name of the app.

### Service domains

The **Service domains** setting works with the **Audit or restrict activities on devices** setting in the workflow for creating a rule within a DLP policy.

When you create a rule, use actions to protect your content when certain conditions are met. When creating rules for endpoint devices, choose the **Audit or restrict activities on devices** option, and select one of these options:

- Audit only
- Block with override
- Block

To control whether sensitive files that your policies protect can be uploaded to specific service domains, go to **Endpoint DLP Settings** &gt; **Browser and domain restrictions to sensitive data** and choose whether to *block* or *allow***Service domains** by default.

Note

The **Service domains** setting only applies to files uploaded by using Microsoft Edge, or by using instances of Google Chrome or Mozilla Firefox that have the [Microsoft Purview Chrome Extension](https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about) installed.

#### Block service domains

When you set the **Service domains** list to **Block**, use the **Add cloud service domain** to specify domains that you want to block. All other service domains are allowed. When the Service domains list is set to Block, DLP policy restrictions only apply when a user attempts to upload a sensitive file to any of the domains on the list.

For example, consider the following configurations:

- A DLP policy is configured to detect sensitive items that contain physical addresses and the **Audit or restrict activities on devices** option is set to **Audit only**.
- The **Service domains** setting is set to **Block**.
- contoso.com IS NOT on the list.
- wingtiptoys.com IS on the list.

In this case, if a user attempts to upload a sensitive file with physical addresses to contoso.com, the upload is allowed to complete and an audit event is generated but no alert is triggered.

In contrast, if a user attempts to upload a sensitive file with credit card numbers to wingtiptoys.com, the user activity - the upload - is also allowed to complete and both an audit event and an alert are generated.

Another example, consider the following configuration:

- A DLP policy is configured to detect sensitive items that contain physical addresses and the **Audit or restrict activities on devices** option is set to **Block**.
- The **Service domains** setting is set to **Block**.
- contoso.com IS NOT on the list.
- wingtiptoys.com IS on the list.

In this case, if a user attempts to upload a sensitive file with physical addresses to contoso.com, the upload is allowed to complete and an audit event is generated but no alert is triggered.

In contrast, if a user attempts to upload a sensitive file with credit card numbers to wingtiptoys.com, the user activity - the upload - is blocked and both an audit event and an alert are generated.

#### Allow service domains

When you set the **Service domains** list to **Allow**, use the **Add cloud service domain** to specify domains that are allowed. All other service domains have DLP policy restrictions enforced. When the Service domains list is set to Allow, DLP policies only apply when a user attempts to upload a sensitive file to any of the listed domains.

For example, here are two starting configurations:

- A DLP policy is configured to detect sensitive items that contain credit card numbers and the **Audit or restrict activities on devices** option is set to **Block with override**.
- The **Service domains** setting is set to **Allow**.
- contoso.com IS NOT on the **Allow** list.
- wingtiptoys.com IS on the **Allow** list.

In this case, if a user attempts to upload a sensitive file with credit card numbers to contoso.com, the upload is blocked, a warning displays, giving the user the option to override the block. If the user chooses to override the block, an audit event is generated and an alert is triggered.

However, if a user attempts to upload a sensitive file with credit card numbers to wingtiptoys.com, the policy restriction *isn't* applied. The upload is allowed to complete, and an audit event is generated but no alert is triggered.

- A DLP policy is configured to detect sensitive items that contain physical addresses and the **Audit or restrict activities on devices** option is set to **Audit only**.
- The **Service domains** setting is set to **Allow**.
- contoso.com IS NOT on the list.
- wingtiptoys.com IS on the list.

In this case, if a user attempts to upload a sensitive file with physical addresses to contoso.com, the upload is allowed to complete and both an audit event and an alert are generated.

In contrast, if a user attempts to upload a sensitive file with credit card numbers to wingtiptoys.com, the user activity - the upload - is also allowed to complete, an audit event is generated but no alert is triggered.

Important

When you set the service restriction mode to **Allow**, you must configure at least one service domain before the system enforces restrictions.

#### Summary table: Allow or block behavior

The following table shows how the system behaves depending on the settings listed.

| Endpoint DLP Service domain setting | DLP policy rule Audit or restrict activities on devices setting | User goes to a listed site | User goes to a site NOT listed |
| --- | --- | --- | --- |
| Allow | Audit only | - User activity is audited  - No alert is generated  - No DLP policies are applied | - User activity is audited  - An alert is generated  - DLP policies are applied in Audit mode |
| Allow | Block with override | - User activity is audited  - No alert is generated  - No DLP policies are applied | - User activity is audited  - An alert is generated  - DLP policies are applied in Block with override mode |
| Allow | Block | - User activity is audited  - No alert is generated  - No DLP policies are applied | - User activity is audited  - An alert is generated  - DLP policies are applied in Block mode |
| Block | Audit only | - User activity is audited  - An alert is generated  - DLP policies are applied in Audit mode | - User activity is audited  - No alert is generated  - No DLP policies are applied |
| Block | Block with override | - User activity is audited  - An alert is generated  - DLP policies are applied in Block with override mode | - User activity is audited - No alert is generated  - No DLP policies are applied |
| Block | Block | - User activity is audited  - An alert is generated  - DLP policies are applied in Block mode | - User activity is audited  - No alert is generated  - No DLP policies are applied |

When you add a domain to the list, use the FQDN format of the service domain without the ending period (`.`). Use `*.` as a wildcard to specify all domains or subdomains. Exclude the protocol (anything before `//`) from the domain. Only include the host name, without any subsites.

For example:

| Input | URL matching behavior |
| --- | --- |
| **contoso.com** | **Matches the specified domain name, and any subsite**: <br>://contoso.com<br><br>://contoso.com/<br><br>://contoso.com/anysubsite1 <br><br>://contoso.com/anysubsite1/anysubsite2 (etc.) <br><br>**Does not match sub-domains or unspecified domains**: <br><br>://anysubdomain.contoso.com <br><br>://anysubdomain.contoso.com.AU |
| \***.contoso.com** | **Matches the specified domain name, any subdomain, and any site**: <br>://contoso.com<br><br>://contoso.com/anysubsite<br><br>://contoso.com/anysubsite1/anysubsite2 <br><br>://anysubdomain.contoso.com/<br><br>://anysubdomain.contoso.com/anysubsite/<br><br>://anysubdomain1.anysubdomain2.contoso.com/anysubsite/<br><br>://anysubdomain1.anysubdomain2.contoso.com/anysubsite1/anysubsite2 (etc.)<br><br>**Does not match unspecified domains**<br><br>://anysubdomain.contoso.com.AU/ |
| **`www.contoso.com`** | **Matches the specified domain name**: <br>`www.contoso.com`<br><br>**Does not match unspecified domains or subdomains**<br><br>://anysubdomain.contoso.com/, in this case, you have to put the FQDN domain name itself `www.contoso.com` |

You can configure up to 50 domains under **Sensitive Service domains**.

Note

The Service domains list setting only applies to file uploads to websites. Actions like pasting into a browser don't follow the Service Domain list.

### Sensitive service domain groups

When you add a website to **Sensitive service domains**, you can set the policy to `audit`, `block with override`, or fully `block` user activity when users attempt to take any of the following actions:

- print from a website
- copy data from a website
- save a website as local files
- upload or drag/drop a sensitive file to an excluded website
- paste sensitive data to an excluded website

The following table shows which browsers support these features:

| Browser | Supported Feature |
| --- | --- |
| Microsoft Edge | - Print the site - Copy data from the site - Save the site as local files (save-as) - Paste to supported browsers- Upload to a restricted cloud service domain |
| Google Chrome (with the Microsoft Purview extension) | - Paste to supported browsers - Upload to a restricted cloud service domain |
| Mozilla Firefox (with the Microsoft Purview extension) | - Upload to a restricted cloud service - Paste to supported browsers |

For the **Paste to supported browsers** action, there might be a brief time lag between when the user attempts to paste text into a web page and when the system finishes classifying it and responds. If this classification latency happens, you might see both policy-evaluation and check-complete notifications in Microsoft Edge or policy-evaluation toast on Chrome and Firefox. Here are some tips for minimizing the number of notifications:

1. Notifications trigger when a policy for the target website is configured to **Block** or **Block with override** the **Paste to supported browsers** for that user. You can configure the overall action to **Audit** and then use the exceptions to **Block** the target websites. Alternately, you can set the overall action to **Block** and then use the exceptions to **Audit** the secure websites.
2. Use the latest Antimalware client version.
3. Ensure your version of Microsoft Edge is 120 or higher.
4. Install these Windows KBs:
    1. Windows 10: [KB5032278](https://support.microsoft.com/en-us/topic/november-30-2023-kb5032278-os-build-19045-3758-preview-0ae14f06-577e-4eb3-8fcb-c722f3f9dc29), [KB5023773](https://support.microsoft.com/en-us/topic/march-21-2023-kb5023773-os-builds-19042-2788-19044-2788-and-19045-2788-preview-5850ac11-dd43-4550-89ec-9e63353fef23)
    2. Windows 11 21H2: [KB5023774](https://support.microsoft.com/en-us/topic/march-28-2023-kb5023774-os-build-22000-1761-preview-67b4cfda-120a-422f-98c0-35124ddba839)
    3. Win 11 22H2: [KB5032288](https://support.microsoft.com/en-us/topic/december-4-2023-kb5032288-os-builds-22621-2792-and-22631-2792-preview-538fbe4a-e9de-4312-85cd-d870444341d0), [KB5023778](https://support.microsoft.com/en-us/topic/march-28-2023-kb5023778-os-build-22621-1485-preview-d490bb51-492e-410c-871f-50ad01b0f765)
5. On macOS, ensure your antimalware Client version is 101.25022.0003 or later.

The **Paste to supported browsers** action doesn't follow the behavior defined in the Service Domain list. However, if Sensitive Service Domain Groups are configured on the rule for Paste To Browser, the system honors the configured Sensitive Service Domain Groups.

Note

The **Service domains** setting only applies to files uploaded by using Microsoft Edge or an instance of Google Chrome or Mozilla Firefox that has the [Microsoft Purview Chrome Extension](https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about) installed. The Generative AI Websites group contains these [supported sites](https://learn.microsoft.com/en-us/en-us/purview/ai-microsoft-purview-supported-sites). The group is used for default policies within Data Security Posture Management for AI and can't be edited or deleted.

For devices, you must configure the **Sensitive service domains** list to use the **Upload to a restricted cloud service domain** action in a DLP policy. You can also define website groups that you want to assign policy actions to that are different from the global website group actions. You can add a maximum of 100 websites into a single group and you can create a maximum of 150 groups. This configuration gives a maximum of 15,000 websites that the policy actions can be assigned to. For more information, see [Help prevent risky user activity by monitoring or restricting access to sensitive service domains](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-access-to-domains).

Important

Regarding the **Paste to supported browser** action. If 'Collect original file as evidence for all selected file activities on Endpoint' is enabled on the rule for this feature, garbage characters might appear in the source text if the user's Windows device doesn't have Antimalware Client Version 4.18.23110 or newer installed. Select **Actions** &gt; **Download** to view the actual content.

For more information, see [Help prevent leakage of sensitive content by restricting paste actions into browsers](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-paste-in-browsers).

#### Supported syntax for designating websites in a website group

If you use URLs to identify websites, don't include the networking protocol as part of the URL (for instance, *https://* or *file://*). Instead, use a flexible syntax to include and exclude domains, subdomains, websites, and subsites in your website groups. For example,

- Use `*.` as a wildcard to specify all domains or all subdomains.
- Use `/` as a terminator at the end of a URL to scope to that specific site only.

When you add a URL without a terminating slash mark ( `/`), that URL is scoped to that site and all subsites. You can only add `*.` to the beginning of a domain. The `/` terminator is only supported at the end of a domain.

This syntax applies to all http/https websites. Here are some examples:

| URL added to the website group | URL matches | URL doesn't match |
| --- | --- | --- |
| contoso.com | http://contoso.com  https://contoso.com  https://contoso.com/  https://contoso.com/allsubsites1  https://contoso.com/allsubsites1/allsubsites2 | https://allsubdomains.contoso.com  https://allsubdomains.contoso.com.au  https://www.contoso.com |
| contoso.com/ | http://contoso.com  https://contoso.com  https://contoso.com/ | https://contoso.com/allsubsites1  https://contoso.com/allsubsites1/allsubsites2  https://allsubdomains.contoso.com  https://allsubdomains.contoso.com/au  https://www.contoso.com |
| \*.contoso.com | http://contoso.com  https://contoso.com  https://www.contoso.com  https://www.contoso.com/allsubsites  https://contoso.com/allsubsites1/allsubsites2  https://allsubdomains.contoso.com  https://allsubdomains.contoso.com/allsubsites  https://allsubdomains1.allsubdomains2.contoso.com/allsubsites1/allsubsites2 | https://allsubdomains.contoso.com.au |
| \*.contoso.com/xyz | http://contoso.com/xyz/  https://contoso.com/xyz/  https://contoso.com/xyz/allsubsites/  https://allsubdomains.contoso.com/xyz/  https://allsubdomains.contoso.com/xyz/allsubsites  https://allsubdomains1.allsubdomains2.contoso.com/xyz/allsubsites  https://allsubdomains1.allsubdomains2.contoso.com/xyz/allsubsites1/allsubsites2 | https://contoso.com/xyz  https://allsubdomains.contoso.com/xyz |
| \*.contoso.com/xyz/ | http://contoso.com/xyz  https://contoso.com/xyz  https://contoso.com/xyz/  https://allsubdomains.contoso.com/xyz  https://allsubdomains.contoso.com/xyz/ | https://contoso.com  https://contoso.com/xyz/allsubsites/  https://allsubdomains.contoso.com/xyz/allsubsites/  https://allsubdomains1.allsubdomains2.contoso.com/xyz/allsubsites/  https://allsubdomains1.allsubdomains2.contoso.com/xyz/allsubsites1/allsubsites2 |

#### Supported syntax for designating IP ranges or IP addresses (preview)

In preview, DLP supports using IP address and address ranges to identify websites. Set the Match type to *IP address* or *IP address range* and then enter a specific IP address or an IP range in the **Sensitive service domain** field. Select **Add site** to add the selection to the Sensitive service domain group.

Examples of supported syntax:

- 1.1.1.1
- 1.1.1.1-2.2.2.2
- 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- 2001:0db8:85a3:0000:0000:8a2e:0370:7320-2001:0db8:85a3:0000:0000:8a2e:0370:7334

Important

URLs support these actions:

- **Print the site**
- **Copy data from the site**
- **Save the site as local files (save-as)**
- **Paste to supported browsers**
- **Upload to a restricted cloud service domain**

> 
> IP address and IP address range support these actions:

- **Print the site**
- **Copy data from the site**
- **Save the site as local files (save-as)**
- **Upload to a restricted cloud service domain** (Windows only)

Sensitive service domain groups contain a preconfigured group for **Generative AI websites**. For a list of all the websites in this group, see [List of AI sites supported by Microsoft Purview Data Security Posture Management for AI](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-supported-sites).

## Additional settings for Endpoint DLP

### Business justification in policy tips

You can control how users interact with the business justification option in [Options for configuring policy tips](https://learn.microsoft.com/en-us/purview/dlp-use-notifications-and-policy-tips#options-for-configuring-policy-tips). This option appears when users perform an activity that's protected by the **Block with override** setting in a DLP policy. The business justification setting is global. Choose from one of the following options:

- **Show default options and custom text box**: By default, users can select either a built-in justification or enter their own text.
- **Only show default options**: Users can only select from a list of built-in justifications.
- **Only show custom text box**: Users can only enter a custom justification. The text box appears in the end-user policy tip notification, without a list of options.

#### Customizing the options in the drop-down menu

You can create up to five customized options that appear when users interact with the policy notification tip by selecting **Customize the options drop-down menu**.

| Option | Default text |
| --- | --- |
| option 1 | **This is part of an established business workflow** or enter customized text |
| option 2 | **My manager has approved this action** or enter customized text |
| option 3 | **Urgent access required; I'll notify my manager separately** or enter customized text |
| Show false positive option | **The information in these files is not sensitive** or enter customized text |
| option 5 | **Other** or enter customized text |

### Turn on automatic diagnostic logging for endpoint DLP

Microsoft Purview Always-on diagnostics feature automatically records comprehensive trace logs, saving you time and enabling faster troubleshooting. For more information, see [Always-on diagnostics for endpoint DLP](https://learn.microsoft.com/en-us/purview/dlp-always-on-diagnostics).

## Enable Endpoint DLP for Windows Servers

Endpoint DLP supports Windows Server 2019 and later versions.

After you [onboard a Windows Server](https://learn.microsoft.com/en-us/purview/device-onboarding-sccm#onboard-devices-using-configuration-manager), turn on Endpoint DLP support to apply endpoint protection.

To work with the DLP alert management dashboard:

1. In the Microsoft Purview portal, go to **Data loss prevention** &gt; **Overview**.
2. Choose **Settings** in the upper right corner.
3. On **Settings**, select **Endpoint settings** and expand **Endpoint DLP support for onboarded servers**.
4. Set the toggle to **On**.

## Always audit file activity for devices

By default, when you onboard devices, the system automatically audits activity for Office, PDF, and CSV files. You can review this activity in activity explorer. Turn off this feature if you want to audit this activity only when onboarded devices are included in an active policy. The **Always audit file activity for devices** setting enables the auditing of file activities for documents where a DLP Rule didn't match: File Created, File Modified, File Renamed, File created on removable media, and File created on network share.

The system always audits file activity for onboarded devices, regardless of whether they're included in an active policy.

## Printer groups

Use this setting to define groups of printers that you want to assign policy actions to that are different from the global printing actions.

The most common use case for creating printer groups is to use them for limiting the printing of contracts to only those printers in an organization's Legal department. After you define a printer group here, you can use it in all of your policies that are scoped to **Devices**. For more information on configuring policy actions to use authorization groups, see [Create policy to manage printer access using authorization groups](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-manage-printer-access).

You can create a maximum of 20 printer groups. Each group can contain a maximum of 50 printers.

Note

Printer groups are available for devices running any of the following Windows versions:

- Windows 10 and later (21H1, 21H2, and later) - [KB5020030](https://support.microsoft.com/topic/november-15-2022-kb5020030-os-builds-19042-2311-19043-2311-19044-2311-and-19045-2311-preview-237a9048-f853-4e29-a3a2-62efdbea95e2)
- Win 11 21H2 - [KB5019157](https://support.microsoft.com/topic/november-15-2022-kb5019157-os-build-22000-1281-preview-d64fb317-3435-49ff-b2c4-d0356a51a6b0)
- Win 11 22H2 - [KB5020044](https://support.microsoft.com/topic/november-29-2022-kb5020044-os-build-22621-900-preview-43f0bdf9-0b75-4110-bab3-3bd2433d84b3)
- Windows Server 2022 - [KB5020032](https://support.microsoft.com/topic/november-22-2022-kb5020032-os-build-20348-1311-preview-7ca1be57-3555-4377-9eb1-0e4d714d9c68)

Let's look at an example. Say you want your DLP policy to block printing of contracts to all printers except for those that are in the legal department.

1. Use the following parameters to assign printers in each group.

    - **Friendly printer** name - the Friendly printer name is the value showing on the UX when you select the Printer. Support both Windows and macOS.
    - **USB printer** - A printer connected through a computer's USB port. Select this option if you want to enforce any USB printer while leaving the USB product ID and USB vendor ID unselected. You can also assign a specific USB printer by specifying its USB product ID and USB vendor ID. Support both Windows and macOS.
    - **USB product ID** - Get the **Device Instance** path value from the printer device property details in device manager. Convert that value the to Product ID and Vendor ID format. For more information, see [Standard USB identifiers](https://learn.microsoft.com/en-us/en-us/windows-hardware/drivers/install/standard-usb-identifiers). Support both Windows and macOS.
    - **USB vendor ID** - Get the **Device Instance** path value from the printer device property details in device manager. Convert that value to the Product ID and Vendor ID format. For more information, see [Standard USB identifiers](https://learn.microsoft.com/en-us/en-us/windows-hardware/drivers/install/standard-usb-identifiers). Support both Windows and macOS.
    - **IP range** - Support both Windows and macOS.
    - **Print to file** - Microsoft Print to PDF or Microsoft XPS Document Writer. If you only want to enforce Microsoft Print to PDF, you should use Friendly printer name with 'Microsoft Print to PDF'. Only support Windows.
    - **Universal print deployed on a printer** - For more information on universal printers, see [Set up Universal Print](https://learn.microsoft.com/en-us/en-us/universal-print/fundamentals/universal-print-getting-started). Only support Windows.
    - **Corporate printer** - is a print queue shared through on-premises Windows print server in your domain. Its path might look like this: \print-server\contoso.com\legal\_printer\_001. Only support Windows.
    - **Print to local** - Any printer connecting through Microsoft print port but not any of above types. For example: print through remote desktop or redirect printer. Only support Windows.

Note

You shouldn't use multiple parameters of **USB printer**, **IP range**, **Print to file**, **Universal print deployed on a printer**, **Corporate printer**, and **Print to local**.

1. Assign each printer in the group a **Display name**. These names appear only in the Microsoft Purview console.
2. Create a printer group named **Legal printers** and add individual printers (with an alias) by their friendly name; for instance: `legal_printer_001`, `legal_printer_002`, and `legal_color_printer`. (You can select multiple parameters at once to help you unambiguously identify a specific printer.)
3. Assign the policy actions to the group in a DLP policy:

    - `Allow` (audit with no user notifications or alerts)
    - `Audit only` (you can add notifications and alerts)
    - `Block with override` (blocks the action, but the user can override)
    - Preview, a fix to address the unnecessary resubmission to queue the print job after initial override, has been implemented.
    - `Block` (blocks no matter what)

### Create a printer group

1. Open the [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data Loss Prevention** &gt; **Overview** &gt; settings gear icon in the upper right corner &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Printer groups**.
2. Select **+ Create printer group**.
3. Enter a name for the group.
4. Select **Add printer**.
5. Enter a **Friendly name** for the printer. Make sure the name matches the value from the printer's device property details in Device Manager.
6. Select the parameters and provide the values to unambiguously identify the specific printer.
7. Select **Add**.
8. Add other printers as needed.
9. Select **Save** and then **Close**.

## File extension groups

Use this setting to define groups of file extensions that you want to assign policy actions to. For example, you can apply a **File could not be scanned** policy only to file extensions in the created groups.

Note

Don't add a `.` when you add an extension.

## Disable classification

Use this setting to exclude specific file extensions from Endpoint DLP classification.

For files that are on the [Monitored files](https://learn.microsoft.com/en-us/en-us/purview/endpoint-dlp-learn-about) list, you can disable classification through this setting. When you add a file extension to this setting, Endpoint DLP doesn't scan content in files with this extension. As a result, Endpoint DLP doesn't perform policy evaluation based on the content of those files. You can't see content information for the purposes of conducting investigations.

Note

Don't add a `.` when you add an extension.

## Removable USB device groups

Use this setting to define groups of removable storage devices, such as USB thumb drives, that you want to assign policy actions to that are different from the global removable storage actions. For example, say you want your DLP policy to block items with engineering specifications from being copied to removable storage devices, except for designated USB-connected hard drives that are used to back up data for offsite storage.

You can create up to 20 groups, with up to 50 removable storage devices in each group.

Note

Removable USB device groups are available for devices running any of the following Windows versions:

- Windows 10 and later (21H1, 21H2) with KB 5018482
- Windows 11 21H2, 22H2 with KB 5018483
- Windows 10 RS5 (KB 5006744) and Windows Server 2022

Use the following parameters to define your removable storage devices.

- **Storage device friendly name** - Get the Friendly name value from the storage device property details in device manager. Wildcard values (\*) are supported.
- **USB product ID** - Get the Device Instance path value from the USB device property details in device manager. Convert it to Product ID and Vendor ID format. For more information, see [Standard USB identifiers](https://learn.microsoft.com/en-us/en-us/windows-hardware/drivers/install/standard-usb-identifiers).
- **USB vendor ID** - Get the Device Instance path value from the USB device property details in device manager. Convert it to Product ID and Vendor ID format. For more information, see [Standard USB identifiers](https://learn.microsoft.com/en-us/en-us/windows-hardware/drivers/install/standard-usb-identifiers).
- **Serial number ID** - Get the serial number ID value from the storage device property details in device manager. Wildcard values (\*) are supported.
- **Device ID** - Get the device ID value from the storage device property details in device manager. Wildcard values (\*) are supported.
- **Instance path ID** - Get the device ID value from the storage device property details in device manager. Wildcard values (\*) are supported.
- **Hardware ID** - Get the hardware ID value from the storage device property details in device manager. Wildcard values (\*) are supported.

You assign each removable storage device in the group an **Alias**. The alias is a friendly name that only appears in the Microsoft Purview console. So, continuing with the example, you create a removable storage device group named **Backup** and add individual devices (with an alias) by their friendly name, like `backup_drive_001`, and `backup_drive_002`.

You can multiselect the parameters and then the printer group includes all devices that satisfy those parameters.

You can assign these policy actions to the group in a DLP policy:

- `Allow` (audit with no user notifications or alerts)
- `Audit only` (you can add notifications and alerts)
- `Block with` override (blocks the action, but the user can override)
- `Block` (blocks no matter what)

### Create a removable USB device group

1. Open the [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data Loss Prevention** &gt; **Overview** &gt; settings gear icon in the upper right corner &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Removable USB device groups**.
2. Select **+ Create removable storage device group**.
3. Enter a **Group name**.
4. Select **Add removable storage device**.
5. Enter an **Alias**.
6. Select the parameters and enter the values to clearly identify the specific device.
7. Select **Add**.
8. Add other devices to the group as needed.
9. Select **Save** and then **Close**.

The most common use case for creating removable storage groups is to specify which removable storage devices users can copy files to. Generally, copying is only allowed for devices in a designated **Backup** group.

After you define a removable storage device group, you can use it in all of your policies that are scoped to **Devices**. For more information about configuring policy actions to use authorization groups, see [Create policy to manage printer access using authorization groups](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-manage-printer-access).

## Network share groups

Use this setting to define groups of network share paths that you want to assign policy actions to that are different from the global network share path actions. For example, say you want your DLP policy to prevent users from saving or copying protected files to network shares except the network shares in a particular group.

Note

Network share groups are available for devices running any of the following Windows versions:

- Windows 10 and later (21H1, 21H2) with KB 5018482
- Windows 11 21H2, 22H2 with KB 5018483
- Windows 10 RS5 (KB 5006744) and Windows Server 2022

To include network share paths in a group, define the prefix that they all the shares start with. For example:

- '\Library' matches:

    - \Library folder and all its subfolders.
- You can use wildcards, for example '\Users\*\Desktop' matches:

    - '\Users\user1\Desktop'
    - '\Users\user1\user2\Desktop'
    - '\Users\*\Desktop'
- You can also use environmental variables, for example:

    - %AppData%\app123
- Wildcard values are supported. So a path definition can contain an asterisk (`*`) in the middle of the path or at the end of the path.  Example: `\\Lib*` covers `\\Libray`

You can assign the following policy actions to the group in a DLP policy:

- `Allow` (audit with no user notifications or alerts)
- `Audit only` (you can add notifications and alerts)
- `Block with override` (blocks the action, but the user can override)
- `Block` (blocks no matter what)

After you define a network share group, you can use it in all of your DLP policies that are scoped to **Devices**. For more information about configuring policy actions to use authorization groups, see [Create policy to manage printer access using authorization groups](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-manage-printer-access).

### Create a Network Share group

1. Open [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data Loss Prevention** &gt; **Overview** &gt; settings gear icon in the upper right corner &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Network share groups**.
2. Select **+ Create network share group**.
3. Enter a **Group name**.
4. Add the file path to the share.
5. Select **Add**.
6. Add other share paths to the group as needed.
7. Select **Save** and then **Close**.

## VPN settings

Use the VPN list to control only those actions that are carried out over that VPN.

Note

VPN settings are available for devices running any of these versions of Windows:

- Windows 10 and later (21H1, 21H2) with KB 5018482
- Windows 11 21H2, 22H2 with KB 5018483
- Windows 10 RS5 (KB 5006744)

When you list a VPN in **VPN Settings**, you can assign the following policy actions to it:

- `Allow` (audit with no user notifications or alerts)
- `Audit only` (you can add notifications and alerts)
- `Block with override` (blocks the action, but the user can override)
- `Block` (blocks no matter what)

You can apply these actions individually or collectively to the following user activities:

- Copy to clipboard
- Copy to a USB removable device
- Copy to a network share
- Print
- Copy or move using unallowed (restricted) Bluetooth app
- Copy or move using RDP

When you configure a DLP policy to restrict activity on devices, you can control what happens to each activity performed when users are connected to your organization within any of the VPNs listed.

Use the **Server address** or **Network address** parameters to define the VPN allowed.

### Get the server address or network address

1. On a DLP monitored Windows device, open a **Windows PowerShell** window as an administrator.
2. Run the following cmdlet. It returns multiple fields and values.

```powershell
Get-VpnConnection
```

1. Among the results of the cmdlet, find the **ServerAddress** field and record that value. Use the **ServerAddress** when you create a VPN entry in the VPN list.
2. Find the **Name** field and record that value. The **Name** field maps to the **Network address** field when you create a VPN entry in the VPN list.

### Add a VPN

1. Open [Microsoft Purview portal](https://purview.microsoft.com) and go to **Data Loss Prevention** &gt; **Overview** &gt; settings gear icon in the upper right corner &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **VPN settings**.
2. Select **Add or edit VPN addresses**.
3. Enter either the **Server address** or **Network address** that you recorded after running `Get-VpnConnection`.
4. Select **Save**.
5. Close the item.

Important

Under the **Network restrictions** setting, you also see **Corporate network** as an option. **Corporate network** connections are all connections to your organization's resources. You can see if a device is using a **Corporate network** by running the `Get-NetConnectionProfile` cmdlet as an administrator. If the `NetworkCategoryId` in the output is `DomainAuthenticated`, it means the machine is connected to the **Corporate network**. If the output is anything else, the machine isn't. In some cases, a machine can be both VPN connected and **Corporate network** connected. If both are selected under the **Network restrictions**, Endpoint DLP applies the action based on the order. If you want the action for VPN to be the one that's applied, move the VPN entry above **Corporate network** to have higher priority than the action for **Corporate network**.

> 
> See [Create policy to manage file activities by implementing network exceptions](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-file-activities-using-network-exceptions) for more information on configuring policy actions to use network exceptions.
