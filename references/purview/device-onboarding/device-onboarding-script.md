# Onboard Windows 10 and Windows 11 devices using a local script

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-script  
> Microsoft doc last updated: 2023-09-13


**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

You can also manually onboard individual devices to Microsoft 365. You might want to do this first when testing the service before you commit to onboarding all devices in your network.

Important

This script has been optimized for use on up to 10 devices.

To deploy at scale, use [other deployment options](https://learn.microsoft.com/en-us/purview/device-onboarding-overview). For example, you can deploy an onboarding script to more than 10 devices in production with the script available in [Onboard Windows 10 devices using Group Policy](https://learn.microsoft.com/en-us/purview/device-onboarding-gp).

## Onboard devices

1. Get the configuration package .zip file (*DeviceComplianceOnboardingPackage.zip*) package from [Microsoft Purview portal](https://purview.microsoft.com)
2. In the navigation pane, select [**Settings**](https://go.microsoft.com/fwlink/p/?linkid=2174201) &gt; **Device onboarding**.
3. In the **Deployment method** field, select **Local Script**.
4. Click **Download package** and save the .zip file.
5. Extract the contents of the configuration package to a location on the device you want to onboard (for example, the Desktop). You should have a file named *DeviceComplianceLocalOnboardingScript.cmd*.
6. Open an elevated command-line prompt on the device and run the script:
7. Go to **Start** and type **cmd**.
8. Right-click **Command prompt** and select **Run as administrator**.

    
9. Type the location of the script file. If you copied the file to the desktop, type: *%userprofile%\Desktop\DeviceComplianceLocalOnboardingScript.cmd*
10. Press the **Enter** key or click **OK**.

For information on how you can manually validate that the device is compliant and correctly reports sensor data see, [Troubleshoot Microsoft Defender Advanced Threat Protection onboarding issues](https://learn.microsoft.com/en-us/en-us/windows/security/threat-protection/microsoft-defender-atp/troubleshoot-onboarding).

## Offboard devices using a local script

For security reasons, the package used to Offboard devices will expire 30 days after the date it was downloaded. Expired offboarding packages sent to a device will be rejected. When downloading an offboarding package you will be notified of the packages expiry date and it will also be included in the package name.

Note

Onboarding and offboarding policies must not be deployed on the same device at the same time, otherwise this will cause unpredictable collisions.

1. Get the offboarding package from [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149).
2. In the navigation pane, select [**Settings**](https://go.microsoft.com/fwlink/p/?linkid=2174201) &gt; **Device offboarding**.
3. In the **Deployment method** field, select **Local Script**.
4. Click **Download package** and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the devices. You should have a file named *DeviceComplianceOffboardingScript\_valid\_until\_YYYY-MM-DD.cmd*.
6. Open an elevated command-line prompt on the device and run the script:
7. Go to **Start** and type **cmd**.
8. Right-click **Command prompt** and select **Run as administrator**.

    
9. Type the location of the script file. If you copied the file to the desktop, type: *%userprofile%\Desktop\WindowsDefenderATPOffboardingScript\_valid\_until\_YYYY-MM-DD.cmd*
10. Press the **Enter** key or click **OK**.

Important

Offboarding causes the device to stop sending sensor data to the portal.

## Monitor device configuration

You can follow the different verification steps in the [Troubleshoot onboarding issues](https://learn.microsoft.com/en-us/purview/(/windows/security/threat-protection/microsoft-defender-atp/troubleshoot-onboarding) to verify that the script completed successfully and the agent is running.

Monitoring can also be done directly on the portal, or by using the different deployment tools.

### Monitor devices using the portal

1. Go to [Microsoft Purview portal](https://compliance.microsoft.com).
2. Choose **Settings** &gt; **Device onboarding** &gt; **Devices**.
3. Go to Microsoft Purview portal, and select [**Settings**](https://go.microsoft.com/fwlink/p/?linkid=2174201) &gt; **Device onboarding** &gt; **Devices**.
4. Verify that devices are appearing.
