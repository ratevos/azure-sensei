# Onboard and offboard macOS devices into Purview solutions using Jamf Pro for Microsoft Defender for Endpoint customers

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro-mde  
> Microsoft doc last updated: 2024-06-26


You can use Jamf Pro to onboard macOS devices into Microsoft Purview solutions.

Important

Use this procedure ***if you have*** deployed Microsoft Defender for Endpoint (MDE) to your macOS devices

**Applies to:**

- Customers who have MDE deployed to their macOS devices.
- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

## Before you begin

- Make sure your [macOS devices are managed through Jamf pro](https://www.jamf.com/resources/product-documentation/jamf-pro-installation-guide-for-mac/) and are associated with an identity (Microsoft Entra joined UPN) through Jamf Connect.
- OPTIONAL: Install the v95+ Edge browser on your macOS devices to have native Endpoint DLP support on Edge.

Note

The three most recent major releases of macOS are supported.

## Onboard devices into Microsoft Purview solutions using Jamf Pro

Onboarding a macOS device into Purview solutions is a multi-phase process.

1. Update the existing MDE Preference domain profile using the Jamf Pro console
2. Enable full-disk access
3. Enable accessibility access to Microsoft Purview data loss prevention
4. Check the macOS device

### Prerequisites

Download the following files:

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

### Update the existing MDE Preference domain profile using the Jamf Pro console

For information about how to replace the *schema.json* file in the MDE deployment with the updated version, and configure the settings in the Jamf Pro console, refer to the [Jamf Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).

### Enable full-disk access

To update the existing full disk access profile with the `fulldisk.mobileconfig` file, upload `fulldisk.mobileconfig` to Jamf. For more information, refer to [Set up the Microsoft Defender for Endpoint on macOS policies in Jamf Pro](https://learn.microsoft.com/en-us/en-us/defender-endpoint/mac-jamfpro-policies).

### Enable accessibility access to Microsoft Purview data loss prevention

To grant accessibility access to DLP, upload the `accessibility.mobileconfig` file you downloaded previously to Jamf, as described in [Deploy system configuration profiles](https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro#deploy-system-configuration-profiles).

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

## Offboard macOS devices using Jamf Pro

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

For information about how to offboard a macOS device using Jamf Pro, refer to the [Jamf Pro documentation](https://www.jamf.com/resources/product-documentation/jamf-pro-administrators-guide/), or contact [Jamf Pro support](https://www.jamf.com/resources/jamf-pro-support/).
