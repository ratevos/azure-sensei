# Onboard and offboard macOS devices into Microsoft Purview solutions using JAMF Pro

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro  
> Microsoft doc last updated: 2024-06-26


You can use JAMF Pro to onboard macOS devices into Microsoft Purview solutions such as Endpoint data loss prevention (DLP).

Important

Use this procedure if you ***do not*** have Microsoft Defender for Endpoint (MDE) deployed to your macOS devices.

**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

## Before you begin

- Make sure your [macOS devices are managed through JAMF pro](https://www.jamf.com/resources/product-documentation/jamf-pro-installation-guide-for-mac/) and are associated with an identity (Microsoft Entra joined UPN) through [JAMF Connect](https://www.jamf.com/products/jamf-connect).
- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices for native Endpoint DLP support on Microsoft Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard devices into Microsoft Purview solutions using JAMF Pro

### Prerequisites

Download the following files.

| File | Description |
| --- | --- |
| [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) | This is the bundled file. |
| [schema.json](https://github.com/microsoft/mdatp-xplat/blob/master/macos/settings/data_loss_prevention/schema.json) | This is the MDE preference file. |

Tip

We recommend downloading the bundled [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) file, rather than the [individual](https://github.com/microsoft/mdatp-xplat/tree/master/macos/mobileconfig/profiles)*.mobileconfig* files. The bundled file includes the following required files:

- accessibility.mobileconfig
- fulldisk.mobileconfig
- netfilter.mobileconfig
- sysext.mobileconfig

If any of these files are updated, you need to either download the updated bundle, or download each updated file individually.

### Get the device onboarding and installation packages



1. In the Purview portal, open **Settings** &gt; **Device Onboarding** and then choose **Onboarding**.
2. For the **Select operating system to start onboarding process** value, choose **macOS**.
3. For **Deployment method**, choose **Mobile Device Management/Microsoft Intune**.
4. Choose **Download onboarding package** and then extract the contents of the device onboarding package. the *DeviceComplianceOnboarding.plist* file is downloaded to the JAMF folder.
5. Choose **Download installation package**.

### Deploy onboarding packages

Create a new configuration profile in JAMF Pro. Use the following values:

- **Name:***MDATP onboarding for macOS*
- **Description:** \**MDATP EDR onboarding for macOS*
- **Category:***none*
- **Distribution method:** \*`*install automatically*
- **Level:***computer level*

For help with performing steps within the Jamf Pro console, refer to the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

### Configure application preferences

Important

You must use *com.microsoft.wdav* as the **Preference Domain** value. Microsoft Defender for Endpoint uses this name and *com.microsoft.wdav.ext* to load the managed settings.

For information about how to create a new configuration profile in JAMF Pro, refer to the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/). Or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

Use these values:

- **Name:***MDATP MDAV configuration settings*
- **Description:***Leave this blank*
- **Category:***none*
- **Distribution method:***install automatically*
- **Level:***computer level*

### Deploy system configuration profiles

For information about how to deploy system configuration profiles in JAMF Pro, refer to the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

## Offboard macOS devices using JAMF Pro

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

1. If you aren't using MDE, uninstall the application. See the **Package Deployment** section in the [JAMF Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/).
2. Restart the macOS device. (Some applications may lose printing functionality until they're restarted.)
