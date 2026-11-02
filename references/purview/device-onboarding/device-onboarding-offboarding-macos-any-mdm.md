# Any mobile device management tool for Microsoft Defender for Endpoint customers

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-any-mdm  
> Microsoft doc last updated: 2025-04-28


You can use any MDM to onboard macOS devices into Microsoft Purview solutions.

Important

Use this procedure ***if you have*** deployed Microsoft Defender for Endpoint (MDE) to your macOS devices

**Applies to:**

- Customers who have MDE deployed to their macOS devices.
- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)

## Before you begin

- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices to have native Endpoint DLP support on Microsoft Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard devices into Microsoft Purview solutions using any MDM solution

Onboarding a macOS device into Purview solutions is a multi-phase process.

1. Update any existing MDE Preference domain profile by setting `com.microsoft.wdav` as Preference domain to enable Data Loss Prevention. Refer to update preference domain profile.
2. Enable full-disk access
3. Enable accessibility access to Microsoft Purview Data Loss Prevention
4. Register identity
5. Check the macOS device

### Prerequisites

- Device must have Microsoft Defender Antimalware client version 101.25012.0005 or newer installed.
- Download the following files:

| File | Description |
| --- | --- |
| [accessibility.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/profiles/accessibility.mobileconfig) | Accessibility |
| [fulldisk.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/profiles/fulldisk.mobileconfig) | Full disk access (FDA) |
| [schema.json](https://github.com/microsoft/mdatp-xplat/blob/master/macos/schema/schema.json) | MDE preference |

If any of these individual files are updated, you must download the updated bundled file and redeploy as described.

Tip

We recommend downloading the bundled [mdatp.mobileconfig](https://github.com/microsoft/mdatp-xplat/blob/master/macos/mobileconfig/combined/mdatp.mobileconfig) file, rather than the [individual](https://github.com/microsoft/mdatp-xplat/tree/master/macos/mobileconfig/profiles)*.mobileconfig* files. The bundled file includes the following required files:

- accessibility.mobileconfig
- fulldisk.mobileconfig
- netfilter.mobileconfig
- sysext.mobileconfig

If any of these files are updated, you need to either download the updated bundle, or download each updated file individually.

### Update the existing MDE Preference domain profile

1. Replace the *schema.json* file in the MDE deployment with the updated version that you just downloaded. For information about how to replace the *schema.json* file in the MDE deployment with the updated version, and configure the settings in your MDM solution, refer to your MDM solution documentation.

### Enable full-disk access

To update the existing full disk access profile with the `fulldisk.mobileconfig` file, upload `fulldisk.mobileconfig` to your MDM solution to enable full disk access for Data Loss Prevention.

### Enable accessibility access to Microsoft Purview Data Loss Prevention

To grant accessibility access to DLP, upload the `accessibility.mobileconfig` file you downloaded previously to your MDM solution. This should be similar to what is described in [Deploy system configuration profiles](https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro#deploy-system-configuration-profiles).

### Register Identity

Depending on your configuration, you'll register the Microsoft Entra identity of the using one of these two methods.

#### Method 1: Register without the Microsoft Intune Company Portal

1. Install any Microsoft application such as Microsoft Office, or Teams, or Microsoft Edge. When the user logs in using valid Microsoft Entra account, that account is registered as the UPN for DLP policy evaluation. Personal Microsoft accounts aren't considered as valid.

#### Method 2: Register with the Microsoft Intune Company Portal

This method is for users whose macOS devices don't use Microsoft apps.

You can [Get the Microsoft Intune Company Portal](https://learn.microsoft.com/en-us/en-us/intune/intune-service/user-help/sign-in-to-the-company-portal) if you don't already have it.

1. Deploy [Microsoft Enterprise SSO plug-in for Apple devices](https://learn.microsoft.com/en-us/en-us/entra/identity-platform/apple-sso-plugin) to their managed macOS devices using your MDM solution. The Microsoft Intune Company Portal for macOS provides the SSO plugin for smooth user experience. So, the Microsoft Intune Company Portal must be installed on the macOS device, but the user doesn't need to be signed into the Intune Company portal. When the user signs-in to any non-Microsoft Authentication Library (MSAL) application, like Safari browser, the SSO plugin is enabled to register the UPN.

For information on troubleshooting the Microsoft Enterprise SSO Extension, go to [Troubleshooting the Microsoft Enterprise SSO Extension plugin on Apple devices](https://learn.microsoft.com/en-us/en-us/entra/identity/devices/troubleshoot-mac-sso-extension-plugin?tabs=flowchart-ios).

### Check the macOS device

1. Restart the macOS device.
2. Verify that the following profiles are listed under Profiles in System Settings:
    - Accessibility
    - MAU
    - MDATP Onboarding
    - MDE Preferences
    - Management profile
    - Network filter
    - Notifications
    - System extension profile

## Offboard macOS devices

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

For information about how to offboard a macOS using any MDM solution, refer to the documetentation of your MDM solution.
