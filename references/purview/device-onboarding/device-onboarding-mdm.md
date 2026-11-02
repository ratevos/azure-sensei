# Onboard Windows 10 and Windows 11 devices using Mobile Device Management tools

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-mdm  
> Microsoft doc last updated: 2023-04-03


**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

You can use mobile device management (MDM) solutions to configure devices. Microsoft 365 information protection supports MDM solutions by providing OMA-URIs to create policies to manage devices.

## Before you begin

If you're using Microsoft Intune, the device must be enrolled in MDM.

For more information on enabling MDM with Microsoft Intune, see [Device enrollment (Microsoft Intune)](https://learn.microsoft.com/en-us/en-us/mem/intune/enrollment/device-enrollment).

## Onboard devices using Microsoft Intune

Follow the instructions from [Intune](https://learn.microsoft.com/en-us/en-us/mem/intune/protect/advanced-threat-protection-configure).

Note

The **Health Status for onboarded devices** policy uses read-only properties and can't be remediated.

## Offboard and monitor devices using Mobile Device Management tools

For security reasons, the package used to offboard devices will expire 30 days after the date it was downloaded. Expired offboarding packages sent to a device will be rejected. When you download an offboarding package, you're notified of the package's expiry date. The expiry date is also included in the package name.

Note

Onboarding and offboarding policies must not be deployed on the same device at the same time. If they are, unpredictable collisions result.

1. Get the offboarding package from the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149).
2. In the navigation pane, select **Settings** &gt; **Device onboarding** &gt; **Offboarding**.
3. In the **Deployment method** field, select **Mobile Device Management / Microsoft Intune**.
4. Select **Download package**, and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the network administrators who deploy the package. You should have a file named *DeviceCompliance\_valid\_until\_YYYY-MM-DD.offboarding*.
6. Use the Microsoft Intune custom configuration policy to deploy the following supported OMA-URI settings.

    ```console
    OMA-URI: ./Device/Vendor/MSFT/WindowsAdvancedThreatProtection/Offboarding
    Date type: String
    Value: [Copy and paste the value from the content of the DeviceCompliance_valid_until_YYYY-MM-DD.offboarding file]
    ```

    Note

    If Microsoft Defender for Endpoint is already configured, you can **Turn on device onboarding**. If you do this, step 6 isn't required.

Note

The **Health Status for offboarded devices** policy uses read-only properties and can't be remediated.

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including reference to any alerts received, will be retained for up to six months.
