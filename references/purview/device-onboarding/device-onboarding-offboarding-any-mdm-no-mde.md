# Any mobile device management tool for customers without Microsoft Defender for Endpoint

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-any-mdm-no-mde  
> Microsoft doc last updated: 2025-05-05


You can use any mobile device management (MDM) solution to onboard macOS devices into Microsoft Purview solutions such as Endpoint data loss prevention (DLP).

Important

Use this procedure if you ***do not*** have Microsoft Defender for Endpoint (MDE) deployed to your macOS devices.

**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)

## Before you begin

- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices for native Endpoint DLP support on Microsoft Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard devices into Microsoft Purview solutions using any MDM

### Prerequisites

- You must have Microsoft Defender Antimalware client version 101.25012.0005 or newer installed on the device.
- Download the following files.

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



1. In the Microsoft Purview portal, open **Settings** &gt; **Device Onboarding** and then choose **Onboarding**.
2. For the **Select operating system to start onboarding process** value, choose **macOS**.
3. For **Deployment method**, choose **Mobile Device Management/Microsoft Intune**.
4. Choose **Download onboarding package** and then extract the contents of the device onboarding package. the *DeviceComplianceOnboarding.plist* file is downloaded to the JAMF folder.
5. Choose **Download installation package**.

### Deploy onboarding packages

1. Create a new configuration profile in your MDM. Use the following values (if applicable):

- **Name:***MDATP onboarding for macOS*
- **Description:** \**MDATP EDR onboarding for macOS*
- **Category:***none*
- **Distribution method:** \*`*install automatically*
- **Level:***computer level*

1. Upload *DeviceComplianceOnboarding.plist* as a custom settings
2. Enter `com.microsoft.wdav.atp` as the **Preference Domain**,
3. Choose **Save**. Refer to your MDM documentation on creating configuration profile.

### Configure application preferences

Important

You must use *com.microsoft.wdav* as the **Preference Domain** value. Microsoft Defender for Endpoint uses this name and *com.microsoft.wdav.ext* to load the managed settings.

For information about how to create a new configuration profile, refer to your MDM documentation.

1. Create a new configuration profile. Use these values (if applicable):

- **Name:***MDATP MDAV configuration settings*
- **Description:***Leave this blank*
- **Category:***none*
- **Distribution method:***install automatically*
- **Level:***computer level*

1. Add the `schema.json` as a custom schema in the configuration profile.
2. Under **Preference Domain Properties**, locate **Data Loss Prevention** and select `enabled`.
3. Save the profile after adjusting other MDE settings (if necessary).

### Deploy system configuration profiles

For information about how to deploy system configuration profiles, refer to your MDM documentation.

1. Create a new configuration profile by uploading the `mdatp.mobileconfig` file into your MDM.

### Register Identity

Depending on your configuration, you register the Microsoft Entra identity of the using one of these two methods.

#### Method 1: Register without the Microsoft Intune Company Portal

1. Install any Microsoft application such as Microsoft Office, or Teams, or Microsoft Edge. When the user logs in using valid Microsoft Entra account, that account is registered as the UPN for DLP policy evaluation. Personal Microsoft accounts aren't considered as valid. The device may need to restart to complete the registration.

#### Method 2: Register with the Microsoft Intune Company Portal

This method is for users whose macOS devices don't use Microsoft apps.

You can [Get the Microsoft Intune Company Portal](https://learn.microsoft.com/en-us/en-us/intune/intune-service/user-help/sign-in-to-the-company-portal) if you don't already have it.

1. Deploy [Microsoft Enterprise SSO plug-in for Apple devices](https://learn.microsoft.com/en-us/en-us/entra/identity-platform/apple-sso-plugin) to their managed macOS devices using your MDM solution. The Microsoft Intune Company Portal for macOS provides the SSO plugin for smooth user experience. So, the Microsoft Intune Company Portal must be installed on the macOS device, but the user doesn't need to be signed into the Intune Company portal. When the user signs-in to any non-Microsoft Authentication Library (MSAL) application, like Safari browser, the SSO plugin is enabled to register the UPN. The device may need to restart to complete the registration.

For information on troubleshooting the Microsoft Enterprise SSO Extension, go to [Troubleshooting the Microsoft Enterprise SSO Extension plugin on Apple devices](https://learn.microsoft.com/en-us/en-us/entra/identity/devices/troubleshoot-mac-sso-extension-plugin?tabs=flowchart-ios).

## Offboard macOS devices using any MDM

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

1. If you aren't using MDE, uninstall the application. Refer to your MDM documentation for any MDM specific instructions for uninstallation.
2. Restart the macOS device. (Some applications may lose printing functionality until they're restarted.)
