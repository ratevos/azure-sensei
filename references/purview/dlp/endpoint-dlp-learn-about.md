# Learn about Endpoint data loss prevention

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about  
> Microsoft doc last updated: 2026-08-05


You can use Microsoft Purview Data Loss Prevention (DLP) to monitor the actions that are being taken on items you've determined to be sensitive and to help prevent the unintentional sharing of those items.

**Endpoint data loss prevention** (Endpoint DLP) extends the activity monitoring and protection capabilities of DLP to Windows 10/11, macOS (the three latest released major versions) devices, and Windows certain server versions. Once devices are onboarded into the Microsoft Purview solutions, the information about what users are doing with sensitive items is made visible in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). You can then enforce protective actions on those items via [DLP policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy).

## When are files classified by Endpoint DLP?

Endpoint DLP classifies files under the following conditions:

- **Creation or Modification:** Every time a file is created or modified, it is fully scanned for sensitive information types (SITs) and labels. The file is then evaluated for matches against DLP policies and rules.
- **Reading an Already Classified File:** When an already classified file is read, Endpoint DLP checks for any changes to the policies, rules, or SITs. If there is a change in the DLP configuration, it re-evaluates the policies and rules, but it will not re-extract the text.

Tip

If you're looking for device control for removable storage, see [Microsoft Defender for Endpoint Device Control Removable Storage Access Control](https://learn.microsoft.com/en-us/en-us/defender-endpoint/device-control-overview?tabs=Removable#tabpanel_1_Removable).

Note

Endpoint DLP cannot detect the sensitivity label from another tenant on a document.

## Endpoint DLP Windows 10/11 and macOS support

Endpoint DLP allows you to onboard devices running Windows Server 2019 and later versions.

Note

Installing the supported Windows Server KBs disables the *Classification* feature on the server. This means that Endpoint DLP won't classify files on the server. However, Endpoint DLP will still protect those files on the server that were classified before those KBs were installed on server. To ensure this protection, install Microsoft Defender version 4.18.23100 (October 2023) or later.

By default, Endpoint DLP isn't enabled for Windows servers when they're initially onboarded. Before you can see Endpoint DLP events for your servers in Activity Explorer, you must first [Enable Endpoint DLP for Windows Servers](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#enable-endpoint-dlp-for-windows-servers).

Once properly configured, the same data loss protection policies can be automatically applied to both Windows PCs and Windows servers.

| Setting | Subsetting | Windows 10, 1809 and later, Windows 11, Windows Server 2019 and later versions for Endpoints (X64) | macOS (three latest released versions) | Notes |
| --- | --- | --- | --- | --- |
| **Advanced classification scanning and protection** | **Allocated bandwidth limits** | Supported | Supported | Advanced classification enables these features for macOS: - [Document Fingerprinting](https://learn.microsoft.com/en-us/purview/sit-document-fingerprinting)- [Exact data match based sensitive information types](https://learn.microsoft.com/en-us/purview/sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types)- [Trainable classifiers](https://learn.microsoft.com/en-us/purview/trainable-classifiers-learn-about)- [Learn about named entities](https://learn.microsoft.com/en-us/purview/sit-named-entities-learn) |
| **File path exclusions for Windows** | n/a | Supported | n/a |  |
| **File path exclusions for Mac** | n/a | n/a | Supported | macOS includes a recommended list of exclusions that is on by default |
| **Setup evidence collection for file activities on devices** | **Set evidence cache on device** | Supported | Preview |  |
| **Network share coverage and exclusions** | n/a | Supported | Supported |  |
| **Restricted apps and app groups** | **Restricted app groups** | Supported | Supported |  |
| **Restricted apps and app groups** | **Restricted apps** | Supported | Supported |  |
| **Access by apps not included in restricted apps list or any restricted app groups added to rule** | n/a | Supported | Not supported |  |
| **Restricted apps and app groups** | **Auto-quarantine settings** | Supported | Supported |  |
| **Unallowed Bluetooth apps** | n/a | Supported | Supported |  |
| **Browser and domain restrictions to sensitive data** | **Unallowed browsers** | Supported | Supported |  |
| **Browser and domain restrictions to sensitive data** | **Service domains** | Supported | Supported |  |
| **Browser and domain restrictions to sensitive data** | **Sensitive service domain groups** | Supported | Supported |  |
| **Additional settings for Endpoint DLP** | **Business justification in policy tips** | Supported | Supported |  |
| **Always audit file activity for devices** | n/a | Supported | Supported |  |
| **Printer groups** | n/a | Supported | Supported | Following parameters are only supported on Windows: - Print to file - Universal print deployed on a printer - Corporate printer- Print to local |
| **Removable USB device groups** | n/a | Supported | Supported |  |
| **Network share groups** | n/a | Supported | Supported |  |
| **VPN settings** | n/a | Supported | Not supported |  |

### Scoping DLP policies for endpoints

Microsoft Purview Data Loss Prevention (DLP) policies can be applied to multiple locations, including endpoint devices. When a DLP policy includes the **Devices** location, the policy can be scoped by both users and devices. For a DLP policy to be enforced on an endpoint, both the user and the device must be included in the policy scope.

| Device in scope | User in scope | Policy applied |
| --- | --- | --- |
| Yes | Yes | Yes |
| No | Yes | No |
| No | Yes | No |

This enables more precise data protection controls based on who is accesing data and from which device. For more information, see [Device scoping](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#device-scoping).

For implementation details see [Create policy using device scoping](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-device-scoping).

### Other settings

| Setting | Windows 10/11, Windows 10, 1809 and later, Windows 11 | Windows Server 2019 and later versions for Endpoints (X64) | macOS (three latest released versions) |
| --- | --- | --- | --- |
| Archive file | Supported | Supported | Supported |
| File type and File extension | Supported | Supported | Supported |
| Enable Endpoint DLP for Windows Servers | Not supported | Supported | Not supported |

Note

Endpoint DLP is not supported on Windows Servers configured as Domain Controllers or Windows Servers with the Core Server option selected during installation.

## Endpoint activities you can monitor and take action on

Endpoint DLP enables you to audit and manage the following types of activities users take on sensitive items that are physically stored Windows 10, Windows 11, or macOS devices.

| Activity | Description | Windows 10 (21H2, 22H2), Windows 11 (21H2, 22H2), Windows Server 2019 and later versions for Endpoints (X64) | Windows 11 (21H2, 22H2) for Endpoints (ARM64) | macOS three latest released versions | Auditable/Restrictable |
| --- | --- | --- | --- | --- | --- |
| Upload to a restricted cloud service domain or access from an unallowed browser | Detects when a user attempts to upload an item to a restricted service domain or access an item through a browser. If they're using an unallowed browser, the upload activity is blocked and the user is redirected to use Microsoft Edge. Microsoft Edge then either allows or blocks the upload or access based on the DLP policy configuration. You can block, warn, or audit when protected files can be uploaded or prevented from being uploaded to cloud services based on the allow/unallowed domains list in **Data loss prevention settings**. When the configured action is set to warn or block, other browsers (defined on the unallowed browsers list under **Data loss prevention settings**) are blocked from accessing the file. | Supported | Supported | Supported | Auditable and restrictable |
| Paste to supported browsers | Detects when a user attempts to paste content to a restricted service domain. Evaluation is performed on the content that is being pasted. This evaluation is independent of how the source item that the content came from is classified. | Supported | Supported | Preview | Auditable and restrictable |
| Copy to clipboard | When a user attempts to copy content from a protected file, you can block, block with override, or audit the copying of protected files to a clipboard on an endpoint device. If the rule is configured to **Block** or **Block with override** copying is blocked when the source content is sensitive except when the destination is within the same Microsoft 365 Office app. This activity also applies to redirected clipboards when using Azure Virtual Desktop with Windows 365. | Supported | Supported | Supported | Auditable and restrictable |
| Copy to USB removable device | When this activity is detected, you can block, warn, or audit the copying or moving of protected files from an endpoint device to USB removable media. | Supported | Supported | Supported | Auditable and restrictable |
| Copy to a network share | When this activity is detected, you can block, warn, or audit the copying or moving of protected files from an endpoint device to any network share, including redirected USB devices that are displayed as network shares on an Azure Virtual Desktop with Windows 365. | Supported | Supported | Supported | Auditable and restrictable |
| Print | When this activity is detected, you can block, warn, or audit the printing of protected files from an endpoint device. This activity also applies to redirected printers when using Azure Virtual Desktop together with Windows 365. | Supported | Supported | Supported | Auditable and restrictable |
| Copy or move using unallowed Bluetooth app | Detects when a user attempts to copy an item to an unallowed Bluetooth app (as defined in the list of unallowed Bluetooth apps in **Data loss prevention settings** &gt; **Endpoint settings**). | Supported | Supported | Supported | Auditable and restrictable |
| Copy or move using RDP | Detects when a user attempts to copy an item to a remote desktop session. | Supported | Supported | Not supported | Auditable and restrictable |
| Create an item | Detects the creation of an item. | Supported | Supported | Supported | Auditable |
| Rename an item | Detects the renaming of an item. | Supported | Supported | Supported | Auditable |
| Access by restricted apps | Detects when an application that is on the restricted apps list (as defined in [restricted apps and app groups](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings)) attempts to access protected files on an endpoint device. | Supported | Supported | Supported |  |
| Create Windows Recall snapshots (in preview) | Detects when there is an item or Teams message that contains a sensitive information type or has a senstivity label applied that would be included in a [Windows Recall](https://learn.microsoft.com/en-us/en-us/windows/client-management/manage-recall) snapshot. | Supported | Not supported | Not supported | Auditable and restrictable |

### Copy to clipboard behavior

When you configure a rule to **Block** or **Block with override** when a user attempts the Copy to clipboard activity on content from a file that matches the policy, end users see this behavior with these configurations:

- Word file 123 contains sensitive information that matches the copy to clipboard Block rule.
- Excel file 123 contains sensitive information that matches the copy to clipboard Block rule.
- PowerPoint file 123 contains sensitive information that matches the copy to clipboard Block rule.
- Word file 789 doesn't contain sensitive information.
- Excel file 789 doesn't contain sensitive information.
- PowerPoint file 789 doesn't contain sensitive information.
- Notepad (or any non Microsoft Office based app or process) file XYZ contains sensitive information that matches the copy to clipboard Block rule.
- Notepad (or any non Microsoft Office based app or process) file ABC doesn't contain sensitive information.

| Source | Destination | Behavior |
| --- | --- | --- |
| Word file 123/Excel file 123/PowerPoint file 123 | Word file 123/Excel file 123/PowerPoint file 123 | copy and paste are allowed, in other words intra file copy and paste is allowed. |
| Word file 123/Excel File 123/PowerPoint file 123 | Word file 789/Excel file 789/PowerPoint file 789 | copy and paste are blocked, in other words inter file copy and paste is blocked. |
| Word file 789/Excel file 789/PowerPoint file 789 | Word file 123/Excel File 123/PowerPoint file 123 | copy and paste are allowed |
| Word file 123/Excel file 123/PowerPoint file 123 | Notepad file ABC | copy and paste are blocked |
| Notepad file XYZ | any | copy is blocked |
| Notepad file ABC | any | copy and paste are allowed |

Note

When a DLP rule that blocks copying is applied to an open file, copying from any other file within the same application (even files with no DLP rules applied) is restricted while the DLP blocked file is open.

### Endpoint DLP and Unsaved Files

If data is never saved to a file on the local device, Endpoint DLP cannot scan or classify it. For example, if a user opens a document in Word and saves it directly to a USB device without first storing it locally, Endpoint DLP cannot inspect or block that action.

## Best practice for endpoint DLP policies

Say you want to block all items that contain credit card numbers from leaving endpoints of Finance department users. We recommend:

- Create a policy and scope it to endpoints and to that group of users.
- Create a rule in the policy that detects the type of information that you want to protect. In this case, set **content contains** to *Sensitive information type*\*, and select **Credit Card**.
- Set the actions for each activity to **Block**.

For more information on designing your DLP policies, see [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) .

Note

In Microsoft Purview, DLP policy evaluation of sensitive items occurs centrally, so there's no time lag for policies and policy updates to be distributed to individual devices. When a policy is updated in Microsoft Purview portal, it generally takes about an hour for those updates to be synchronized across the service. Once policy updates are synchronized, items on targeted devices are automatically reevaluated the next time they're accessed or modified. In preview, you can also use [on-demand classification](https://learn.microsoft.com/en-us/purview/on-demand-classification) to identify and classifies sensitive content in historical data stored in SharePoint and OneDrive. For Authorized Groups changes, the policy needs 24 hours to sync.

## Monitored files

### Files monitored via policy

Endpoint DLP monitors these file types policy in Windows 10, 11:

| File Type | Format | Monitored file extensions |
| --- | --- | --- |
| Word processing | Word | `.doc, .docx, .docm, .dot, .dotx, .dotm, .docb, .obd, obt` |
| Spreadsheet | Excel, CSV, TSV | `.xls, .xlsx, .xlt, .xlm, .xlsm, .xlsb, .xlb, .xlc, .csv, .tsv` |
| Presentation | PowerPoint | `.ppt, .pptx, .pptm, .pps, .ppsx, .ppsm, .pot, .potx, .potm, .ppam, .pos` |
| Archive | Zip, RAR, 7z, TAR | `.zip, .rar, .7z, .tar, .gz, .arj, .bz2, .cab, .chm, .lzh, .lzma, .mhtml, .xar, .xz` |
| Adobe PDF | PDF | `.pdf` |
| Text | Text | `.asm, .bat, .c, .cmd, .cpp, .cs, .csv, .cxx, .def, .dic, .h, .hpp, .hxx, .idl, .inc, .inx, .java, .m3u, .mpx, .php, .pl, .pos, .txt, .vcf, .vcs` |
| HTML | HTML | `.ascx, .asp, .aspx, .hta, .htm, .htw, .htx, .jhtml, .html` |
| JSON | JSON | `.json, .adaptivecard, .messagecard` |
| Mail | Mail | `.eml, .msg, .nws` |
| XML | XML | `.infopathml, .jsp, .mspx` |
| Microsoft Office xml | Microsoft Office xml | `.excelml, .powerpointml, .wordml` |
| Protected Files | PFile | `.pbmp, .pgif, .pjfif, .pjpe, .pjpeg, .pjpg, .ppng, .ptif, .ptiff, .ptxt, .pxla, .pxlam, .pxml` |
| Other | Other | `.dfx, .dxf, .fluid, .mime, .pointpub, .rtf, .vtt` |

Endpoint DLP monitors these file types policy in the latest three major releases of macOS:

| File Type | Format | Monitored file extensions |
| --- | --- | --- |
| Word processing | Word | `.doc, .docx, .docm, .dot, .dotx, .dotm, .docb ` |
| Spreadsheet | Excel, CSV, TSV | `.xls, .xlsx, .xlt, .xltx, .xltm, .xlw, .xlm, .xlsm, .xlsb, .xlb, .xlc, .csv, .tsv` |
| Presentation | PowerPoint | `.ppt, .pptx, .pptm, .pps, .ppsx, .ppsm, .pot, .potx, .potm, .ppam, .pos` |
| Archive | Zip, RAR, 7z, TAR | `.zip, .zipx, .rar, .7z, .tar` |
| Adobe PDF | PDF | `.pdf` |
| Text | Text | `.asm, .bat, .c, .cmd, .cpp, .cs, .csv, .cxx, .dic, .h, .hpp, .hxx, .idl, .inc, .inx, .inf, .inx, .java, .m3u, .mpx, .php, .pl, .pos, .txt, .vcf, .vcs` |
| HTML | HTML | `.ascx, .asp, .aspx, .css, .hta, .htm, .htw, .htx, .jhtml, .html, .mht` |
| JSON | JSON | `.json, .adaptivecard, .messagecard` |
| Mail | Mail | `.eml, .msg, .nws` |
| XML | XML | `.infopathml, .jsp, .mspx` |
| Microsoft Office xml | Microsoft Office xml | `.excelml, .powerpointml, .wordml` |
| Other | Other | ` .pointpub, .rtf, .vtt` |

These file types can be monitored through policy settings in Windows 10, 11 and macOS devices, if [OCR](https://learn.microsoft.com/en-us/purview/ocr-learn-about#learn-about-optical-character-recognition-in-microsoft-purview) is enabled:

`.jpg, .png, .tif, .tiff, .bmp, .jpeg`

Endpoint DLP scans files with the specified extensions listed above. If you need to protect or monitor files not listed, use the 'Apply restrictions to only unsupported file extensions' feature. The key differences between this feature and the **File extension is** condition are:

- Endpoint DLP scans content for the **File extension is** condition, allowing you to see Sensitive info type values in events or alerts. In contrast, the **Apply restrictions to only unsupported file extensions** feature does not scan file content.
- The **File extension is** condition triggers content scanning, which may consume higher machine resources like CPU and memory, potentially causing performance issues for some file types. For more details on the **Apply restrictions to only unsupported file extensions** feature, refer to the following resources:
- [Help protect files that Endpoint Data Loss Prevention doesn't scan](https://learn.microsoft.com/en-us/purview/dlp-create-policy-files-edlp-doesnt-scan#help-protect-files-that-endpoint-data-loss-prevention-doesnt-scan)
- [Help protect against sharing of a defined set of unsupported files](https://learn.microsoft.com/en-us/purview/dlp-create-policy-sharing-set-unsupported-files#help-protect-against-sharing-of-a-defined-set-of-unsupported-files)

### Files audited regardless of policy match

Activities can be audited on these file types in Windows 10, 11, and in the latest three major releases of macOS, even if no policy match exists:

| Windows 10, 11 | macOS |
| --- | --- |
| `.doc, .docx, .docm, .dot, .dotx, .dotm, .docb, .xls, .xlsx, .xlt, .xlm, .xlsm, .xltx, .xltm, .xlsb, .xlw, .ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx, .pbix, .pdf, .csv, .tsv, .zip, .rar, .7z, .tar, .war, .gz, .dlp` | `.doc, .docx, .docm, .dot, .dotx, .dotm, .docb, .xls, .xlsx, .xlt, .xlm, .xlsm, .xltx, .xltm, .xlsb, .xlw, .ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx, .pbix, .pdf, .csv, .tsv` |

Note

These file types can be audited, regardless of a policy match, in Windows 10, 11 and macOS devices, so long as [OCR](https://learn.microsoft.com/en-us/purview/ocr-learn-about#learn-about-optical-character-recognition-in-microsoft-purview) is enabled:

`.jpg, .png, .tif, .tiff, .bmp, .jpeg`

Important

For information about the Adobe requirements for using Microsoft Purview Data Loss Prevention (DLP) features with PDF files, see this article from Adobe: [Microsoft Purview Information Protection Support in Acrobat](https://helpx.adobe.com/enterprise/kb/mpip-support-acrobat.html).

If you only want to monitor data from policy matches, you can turn off the **Always audit file activity for devices** in the **Data loss prevention settings** &gt; **Endpoint settings**.

If the **Always audit file activity for devices** setting is on, activities on any Word, PowerPoint, Excel, PDF, and .csv files are always audited, even if the device isn't targeted by any policy.

To ensure activities are audited for all supported file types, create a [custom DLP policy](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy).

Endpoint DLP monitors activity-based on MIME type, so activities are captured, even if the file extension is changed, for these files types:

After the extension is changed to any other file extension:

- `.doc`
- `.docx`
- `.xls`
- `.xlsx`
- `.ppt`
- `.pptx`
- `.pdf`

If the extension is changed only to supported file extensions:

- `.txt`
- `.msg`
- `.rtf`
- `.c`
- `.cpp`
- `.h`
- `.cs`
- `.java`
- `.tsv`

### Unsupported File types

Endpoint DLP does not support monitoring for the following file types:

- `.sys`
- `.lib`
- `.obj`
- `.mui`
- `.drv`
- `.pf`
- `.crdownload`
- `.ini`

## What's different in Endpoint DLP

There are a few extra concepts that you need to be aware of before you dig into Endpoint DLP.

### Enabling Device management

Device management is the functionality that enables the collection of telemetry from devices and brings it into Microsoft Purview solutions like Endpoint DLP and [insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management). You need to onboard all the devices you want to use as locations in your DLP policies.



Onboarding and offboarding are handled via scripts that you download from the device management center. The device management center has custom scripts for each of the following deployment methods:

- Local script (up to 10 machines)
- Group policy
- System Center Configuration Manager (version 1610 or later)
- Mobile Device Management/Microsoft Intune
- VDI onboarding scripts for non-persistent machines



Use the procedures in [Getting started with Microsoft 365 Endpoint DLP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started) to onboard devices.

Onboarding devices to Defender also onboards them to DLP. So, if you have onboarded devices through [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/en-us/defender-endpoint/onboarding), those devices show up automatically in the list of devices. You need only **Turn on device monitoring** to use endpoint DLP.



### Viewing Endpoint DLP data

You can view alerts related to DLP policies enforced on endpoint devices by going to the [DLP Alerts Management Dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) and [Investigate data loss incidents with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender).



You can also view details of the associated event, with rich metadata, in the same dashboard



Once a device is onboarded, information about audited activities flows into Activity explorer even before you configure and deploy any DLP policies that have devices as a location.



Endpoint DLP collects extensive information on audited activity.

For example, if a file is copied to removable USB media, you'd see these attributes in the activity details:

- activity type
- client IP
- target file path
- happened timestamp
- file name
- user
- file extension
- file size
- sensitive information type (if applicable)
- sha1 value
- sha256 value
- previous file name
- location
- parent
- filepath
- source location type
- platform
- device name
- destination location type
- application that performed the copy
- Microsoft Defender for Endpoint device ID (if applicable)
- removable media device manufacturer
- removable media device model
- removable media device serial number



### Why are all endpoint policies on all onboarded devices?

A device can support multiple user accounts. Because endpoint policies are scoped to users, different users of the device may have different policies scoped to them. Therefore, the device must have access to all endpoint DLP policies in order to evaluate items. All devices that are onboarded into Purview are scanned regardless if the user is in scope.

## Endpoint DLP and offline devices

When a Windows endpoint device is offline, existing policies continue to be enforced on existing files. Additionally, with just-in-time protection enabled and in "block" mode, when a new *file* is created on an offline device, the file is still prevented from being shared until the device connects to the data classification service and evaluation completes. If a new *policy* is created on the server, or an existing policy is modified, those changes are updated on the device once it reconnects to the internet.

Important

This functionality isn't supported on macOS endpoint devices.

Consider the following use cases.

1. Policies that have been pushed to a device will continue to be applied to files already classified as sensitive even after the device goes offline.
2. Policies that are updated while a device is offline won't be pushed to that device. Similarly, such policies won't be enforced on that device, until the device is back online. However, the outdated policy that exists on the offline device will still be enforced. Just-in-time protection

If notifications are configured to display, they'll always display when DLP policies are triggered, regardless of whether or not the device is online.

Note

While policies that have already been pushed to an offline device are enforced, the enforcement events don't appear in activity explorer until the device is back online.

DLP policies regularly sync to endpoint devices. If a device is offline, the policies can't be synchronized. In this case, the **Devices list** reflects that the device is out of sync with the policies in on the server.

## Just-in-time protection

Just-in-time protection blocks egress activities on these monitored files until policy evaluation completes successfully:

- Items that have never been evaluated.
- Items on which the evaluation has gone stale. These are previously evaluated items that haven't been reevaluated by the current, updated cloud versions of the policies.

For more information on how just-in-time protection works,see [Learn about just-in-time protection](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit), and [Get started with Microsoft Purview Data Loss Prevention just-in-time protection](https://learn.microsoft.com/en-us/purview/endpoint-dlp-get-started-jit).
