# Onboard non-persistent virtual desktop infrastructure (VDI) devices

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-vdi  
> Microsoft doc last updated: 2023-09-18


**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)
- Virtual desktop infrastructure (VDI) devices

## Onboard VDI devices

Microsoft 365 supports non-persistent virtual desktop infrastructure (VDI) session onboarding.

Note

To onboard non-persistent VDI sessions, VDI devices must be on Windows 10 1809 or higher.

There might be associated challenges when onboarding VDIs. The following are typical challenges for this scenario:

- Instant early onboarding of short-lived sessions, which must be onboarded to Microsoft 365 prior to the actual provisioning.
- The device name is typically reused for new sessions.

VDI devices can appear in the Microsoft Purview portal as either:

- Single entry for each device. In this case, the *same* device name must be configured when the session is created, for example using an unattended answer file.
- Multiple entries for each device - one for each session.

The following steps guide you through onboarding VDI devices and will highlight steps for single and multiple entries.

Warning

Endpoint data loss prevention support for Windows Virtual Desktop supports both single session and multi-session scenarios. For environments where there are low resource configurations, the VDI boot procedure might slow the device onboarding process.

1. Get the VDI configuration package .zip file (*DeviceCompliancePackage.zip*) from [Microsoft Purview portal](https://purview.microsoft.com).
2. In the navigation pane, select **Settings** &gt; **Device onboarding** &gt; **Onboarding**.
3. In the **Deployment method** field, select **VDI onboarding scripts for non-persistent endpoints**.
4. Select **Download package** and save the .zip file.
5. Copy the files from the DeviceCompliancePackage folder extracted from the .zip file into the `golden` image under the path `C:\WINDOWS\System32\GroupPolicy\Machine\Scripts\Startup`.
6. If you aren't implementing a single entry for each device, copy DeviceComplianceOnboardingScript.cmd.
7. If you're implementing a single entry for each device, copy both Onboard-NonPersistentMachine.ps1 and DeviceComplianceOnboardingScript.cmd.

    Note

    If you don't see the `C:\WINDOWS\System32\GroupPolicy\Machine\Scripts\Startup` folder, it might be hidden. You need to choose the **Show hidden files and folders** option from File Explorer.
8. Open a Local Group Policy Editor window and navigate to **Computer Configuration** &gt; **Windows Settings** &gt; **Scripts** &gt; **Startup**.

    Note

    Domain Group Policy may also be used for onboarding non-persistent VDI devices.
9. Depending on the method you'd like to implement, follow the appropriate steps:

    **For single entry for each device**

    Select the **PowerShell Scripts** tab, then select **Add** (Windows Explorer opens directly in the path where you copied the onboarding script earlier). Navigate to onboarding PowerShell script `Onboard-NonPersistentMachine.ps1`.

    **For multiple entries for each device**:

    Select the **Scripts** tab, then select **Add** (Windows Explorer opens directly in the path where you copied the onboarding script earlier). Navigate to the onboarding bash script `DeviceComplianceOnboardingScript.cmd`.
10. Test your solution:

    1. Create a pool with one device.
    2. Sign in device.
    3. Sign out from device.
    4. Sign in device with another user.
    5. **For single entry for each device**: Check only one entry in Microsoft Defender Security Center. **For multiple entries for each device**: Check multiple entries in Microsoft Defender Security Center.
11. Select **Devices list** on the Navigation pane.
12. Use the search function by entering the device name and select **Device** as search type.

## Updating non-persistent virtual desktop infrastructure (VDI) images

As a best practice, we recommend using offline servicing tools to patch golden images.

For example, you can use the below commands to install an update while the image remains offline:

```cmd
DISM /Mount-image /ImageFile:"D:\Win10-1909.vhdx" /index:1 /MountDir:"C:\Temp\OfflineServicing"
DISM /Image:"C:\Temp\OfflineServicing" /Add-Package /Packagepath:"C:\temp\patch\windows10.0-kb4541338-x64.msu"
DISM /Unmount-Image /MountDir:"C:\Temp\OfflineServicing" /commit
```

For more information on DISM commands and offline servicing, please refer to the articles below:

- [Modify a Windows image using DISM](https://learn.microsoft.com/en-us/en-us/windows-hardware/manufacture/desktop/mount-and-modify-a-windows-image-using-dism)
- [DISM Image Management Command-Line Options](https://learn.microsoft.com/en-us/en-us/windows-hardware/manufacture/desktop/dism-image-management-command-line-options-s14)
- [Reduce the Size of the Component Store in an Offline Windows Image](https://learn.microsoft.com/en-us/en-us/windows-hardware/manufacture/desktop/reduce-the-size-of-the-component-store-in-an-offline-windows-image)

If offline servicing isn't a viable option for your non-persistent VDI environment, the following steps should be taken to ensure consistency and sensor health:

1. After booting the golden image for online servicing or patching, run an offboarding script to turn off the Microsoft 365 device monitoring sensor. For more information, see [Offboard devices using a local script](https://learn.microsoft.com/en-us/purview/device-onboarding-script#offboard-devices-using-a-local-script).
2. Ensure the sensor is stopped by running the command below in a CMD window:

    ```cmd
    sc query sense
    ```
3. Service the image as needed.
4. Run the below commands using PsExec.exe (which can be downloaded from https://download.sysinternals.com/files/PSTools.zip) to clean up the cyber folder contents that the sensor may have accumulated since boot:

    ```cmd
    PsExec.exe -s cmd.exe
    cd "C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Cyber"
    del *.* /f /s /q
    REG DELETE "HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection" /v senseGuid /f
    exit
    ```
5. Reseal the golden image as you normally would.
