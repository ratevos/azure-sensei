# Onboard macOS devices into Microsoft 365 overview

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-macos-overview  
> Microsoft doc last updated: 2026-06-26


MacOS devices can be onboarded into Microsoft Purview solutions using either Intune, JAMF Pro, or any other MDM solutions. The onboarding procedures differ depending on which management solution you use. If your macOS devices have already been onboarded into Microsoft Defender for Endpoint (MDE), there are fewer steps. See Next steps for links to the appropriate procedures for you.

**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

## Before you begin

Before you get started with Endpoint DLP on macOS devices (the three latest versions), familiarize yourself with these articles:

- [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)

If you aren't familiar with DLP at all, you should familiarize yourself with these articles as well:

- [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#learn-about-data-loss-prevention)
- [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#plan-for-data-loss-prevention-dlp)
- [Data loss prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference)

If you aren't familiar with Insider Risk, read these articles:

- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)
- [Plan for insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management-plan#plan-for-insider-risk-management)

Your macOS devices must already be managed through Intune, JAMF Pro or any other MDM solutions.

- To onboard into Intune, see [Deployment guide: Manage macOS devices in Microsoft Intune](https://learn.microsoft.com/en-us/en-us/mem/intune/fundamentals/deployment-guide-platform-macos) and [Enroll your Mac with Intune Company Portal](https://learn.microsoft.com/en-us/en-us/mem/intune/user-help/enroll-your-device-in-intune-macos-cp).
- To onboard into JAMF Pro see, [JAMF Pro administrators guide](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/) and [JAMF Pro Installation and Configuration Guide for Mac](https://www.jamf.com/resources/product-documentation/jamf-pro-installation-guide-for-mac/)
- To onboard into other MDM solution see,

To take advantage of the classification improvements on file read access on macOS devices, [roadmap ID 476099](https://www.microsoft.com/en-us/microsoft-365/roadmap?msockid=137a11efdbbc69db1da30575dadd68bb&amp;filters=%5B%22Microsoft+Purview+compliance+portal%22%5D&amp;searchterms=476099), the device must have Microsoft Defender Antimalware client version 101.25012.008 or newer installed.

### Supported processors

macOS devices with x64 and M1, M2 and M3 (ARM64) processors are supported.

### Supported browsers

Endpoint DLP supports these browsers on macOS (three latest released versions):

- Microsoft Edge (latest version)
- Safari (latest version, macOS only)
- Chrome (latest version)
- Firefox (latest version)

## Licensing guidance

See, [Microsoft 365 licensing guidance for information protection](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-protection-data-loss-prevention-for-exchange-online-sharepoint-online-and-onedrive-for-business).

## Prerequisites for each feature

Here are the prerequisites for each feature.

| Feature | Prerequisite |
| --- | --- |
| Device and Device group-based policy scoping support for Endpoint DLP (Roadmap ID 526792) | 101.25072 or newer build is required |

## Conditions supported on macOS

Once a macOS device is onboarded into Microsoft Purview solutions, you can use the following condition with data loss prevention (DLP) policies:

**Content Contains** – Applies to documents that contain sensitive information types and sensitivity labels.

**Content is not labeled** - Applies to documents that do not contain any sensitivity labels as defined by Microsoft Purview Data Loss Prevention (DLP) policies.

Note

'**Content is not labeled**' condition only works for doc/docx, xls/xlsx, ppt/pptx, and pdf file for Endpoint DLP.

**File type is** - This condition allows you to specify which types of files you want to monitor, restrict, or apply certain rules to, based on their format.

**File extension is** - This condition allows you to create policies that target files based on their extensions such as pdf, docx etc.

**Document name contains words** - Detects documents where the file name contains specific words or phrases such as ‘credit’.

**Document could not be scanned** - Applies to documents when their content wasn't scanned. Examples include password protected files, files for which text extraction failed, files that exceed file size limit (64 MB for non-archive, 256 MB for archive)

**Document or Attachment is password protected** - Detects documents that are password protected.

**Document couldn't complete scanning** - Applies to documents when their content was scanned, however the entire document was not scanned. Examples include files for which extracted text exceeded the limits/thresholds.

**Document Size equals or is greater than** - Detects documents with file sizes that are greater than or equal to the specified value.

## Activities that can be audited and restricted on macOS

Once a macOS device is onboarded into Microsoft Purview solutions, you can monitor and restrict the following actions using data loss prevention (DLP) policies.

**Copy to a USB removable media** – When enforced, this action blocks, warns, or audits the copying or moving of protected files from an endpoint device to USB removable media.

**Copy to network shares** – When enforced, this action blocks, warns, or audits the copying or moving of protected files from an endpoint device to any network share.

**Print** – When enforced, this action blocks, warns, or audits when protected files are printed from an endpoint device.

**Copy to clipboard** – When enforced, this action blocks, warns, or audits data in protected file that is being copied to a clipboard on an endpoint device.

**Upload to cloud** – This action blocks, warns, or audits when protected files are uploaded or prevented from being uploaded to cloud services based on the allow/unallowed domains list in global settings. When this action is set to warn or block, other browsers (defined on the unallowed browsers list under Global settings) are blocked from accessing the file.

**Accessed by unallowed apps** – When enforced, this action prevents applications that are on the unallowed apps list (as defined in Global settings) from accessing protected files on an endpoint device.

## Onboarding devices into device management

You must enable device monitoring and onboard your endpoints before you can monitor and protect sensitive items on a device. Both of these actions are done in the Microsoft Purview portal.

When you want to onboard devices that haven't been onboarded yet, download the appropriate script and deploy it to those devices.

1. Open the [Microsoft Purview portal](https://purview.microsoft.com)**Settings** page, expand **Device onboarding**, select **Devices**, and choose **Enable device monitoring**.

Note

While it usually takes about 60 seconds for device onboarding to be enabled, please allow up to 30 minutes before engaging with Microsoft support.

1. Once device Monitoring is enabled, choose **Turn on macOS device monitoring**.
