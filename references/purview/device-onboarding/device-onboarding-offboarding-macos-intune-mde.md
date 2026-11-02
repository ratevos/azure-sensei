# Onboard and offboard macOS devices into Purview solutions using Microsoft Intune for Microsoft Defender for Endpoint customers

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-intune-mde  
> Microsoft doc last updated: 2025-01-14


You can use Microsoft Intune to onboard macOS devices into Microsoft Purview solutions.

Important

Use this procedure ***if you have already deployed*** Microsoft Defender for Endpoint (MDE) to your macOS devices.

**Applies to:**

- Customers who have MDE deployed to their macOS devices.
- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

## Before you begin

- Make sure your [macOS devices are onboarded to Intune](https://learn.microsoft.com/en-us/en-us/mem/intune/fundamentals/deployment-guide-platform-macos) and enrolled in the [Company Portal app](https://learn.microsoft.com/en-us/en-us/mem/intune/user-help/enroll-your-device-in-intune-macos-cp).
- Make sure you have access to the [Microsoft Intune admin center](https://endpoint.microsoft.com/#home).
- OPTIONAL: Install the v95+ Microsoft Edge browser on your macOS devices.

Note

The three most recent major releases of macOS are supported.

## Onboard macOS devices into Microsoft Purview solutions using Microsoft Intune

Given that Microsoft Defender for Endpoints (MDE) has already been deployed to your macOS devices, you can still onboard the devices into Purview solutions by competing the following steps:

1. Validate existing FDA system configuration profile
2. Update MDE Preferences

### Validate existing system configuration profile

1. A full disk access (FDA) configuration profile should have been created and deployed previously for MDE. (For details, see [Intune-based deployment for Microsoft Defender for Endpoint on Mac](https://learn.microsoft.com/en-us/en-us/defender-endpoint/mac-install-with-intune#step-3-full-disk-access)).
2. Endpoint data loss prevention (DLP) *requires additional FDA permission* for the new application (`com.microsoft.dlp.daemon`). Validate that the `com.microsoft.dlp.daemon` is in the fulldisk.mobileconfig file

### Update MDE Preferences

1. Find the existing **MDE Preferences** configuration profile. See [Intune-based deployment for Microsoft Defender for Endpoint on Mac](https://learn.microsoft.com/en-us/en-us/defender-endpoint/mac-install-with-intune#step-9-microsoft-defender-for-endpoint-configuration-settings) for details.
2. Add the following key to the `com.microsoft.wdav` configuration profile file, then save the file.

    ```xml
    <key>features</key> 
    <dict> 
      <key>dataLossPrevention</key> 
      <string>enabled</string> 
    </dict> 
    ```

## Offboard macOS devices using Microsoft Intune

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data received from the device, including references to any alerts it has had, will be retained for up to six months.

1. In the **Microsoft Intune admin center**, open **Devices** &gt; **Configuration**. The policies you created display.
2. Choose the **MDE Preferences** policy.
3. Under **Properties &gt;** **Configuration Settings**, choose **Edit**
4. Remove these settings:

    ```xml
     <key>features</key>
     <dict>
         <key>dataLossPrevention</key>
         <string>enabled</string>
     </dict>
    ```
5. Choose \*\*Review+\*\***Save**. This will offboard the macOS devices from Purview solutions while not changing the macOS device enrollment in MDE.
