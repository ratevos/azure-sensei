# Onboard Windows 10 and Windows 11 devices via Group Policy

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-gp  
> Microsoft doc last updated: 2026-06-26


**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)
- Group Policy

Note

To use Group Policy (GP) updates to deploy the package, you must be on Windows Server 2008 R2 or later.

For Windows Server 2019, you may need to replace NT AUTHORITY\Well-Known-System-Account with NT AUTHORITY\SYSTEM of the XML file that the Group Policy preference creates.

This article explains how to use Group Policy to deploy the Microsoft Purview device configuration package on Windows 10 and Windows 11 devices. After onboarding, devices can be monitored by endpoint data loss prevention and insider risk management features. The procedures cover both onboarding and offboarding scenarios. This guidance is intended for IT administrators who manage device policies through Group Policy Objects (GPOs).

## Onboard devices using Group Policy

Use the following steps to download and deploy the Group Policy onboarding package:

1. Open the [Purview portal](https://purview.microsoft.com).
2. In the navigation pane, select **Settings** &gt; **Device Onboarding**.
3. In the **Deployment method** field, select **Group policy**.
4. Click **Download package** and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the device. You should have a folder called *OptionalParamsPolicy* and the file *DeviceComplianceLocalOnboardingScript.cmd*.
6. Open the [Group Policy Management Console](https://learn.microsoft.com/en-us/en-us/internet-explorer/ie11-deploy-guide/group-policy-and-group-policy-mgmt-console-ie11) (GPMC), right-click the Group Policy Object (GPO) you want to configure and click **Edit**.
7. In the **Group Policy Management Editor**, go to **Computer configuration**, then **Preferences**, and then **Control panel settings**.
8. Right-click **Scheduled tasks**, point to **New**, and then click **Immediate Task (At least Windows 7)**.
9. In the **Task** window that opens, go to the **General** tab. Under **Security options** click **Change User or Group** and type SYSTEM and then click **Check Names** then **OK**. NT AUTHORITY\SYSTEM appears as the user account the task will run as.
10. Select **Run whether user is logged on or not** and check the **Run with highest privileges** check box.
11. Go to the **Actions** tab and click **New...** Ensure that **Start a program** is selected in the **Action** field. Enter the file name and location of the shared *WindowsDefenderATPOnboardingScript.cmd* file.
12. Click **OK** and close any open GPMC windows.

## Offboard devices using Group Policy

For security reasons, the package used to offboard devices will expire 30 days after the date it was downloaded. Expired offboarding packages sent to a device will be rejected. When downloading an offboarding package you will be notified of the packages expiry date and it will also be included in the package name.

Important

Offboarding causes the device to stop sending sensor data to the portal. However, data from the device, including references to any alerts it has had, will be retained for up to six months.

Note

Onboarding and offboarding policies must not be deployed on the same device at the same time. Deploying both policies simultaneously causes unpredictable collisions.

1. Get the offboarding package from [Microsoft Purview portal](https://purview.microsoft.com/compliancesettings/deviceonboarding).
2. In the navigation pane, select **Settings** &gt; **//Device onboarding** &gt; **Offboarding**.
3. In the **Deployment method** field, select **Group policy**.
4. Click **Download package** and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the device. You should have a file named *DeviceComplianceOffboardingScript\_valid\_until\_YYYY-MM-DD.cmd*.
6. Open the [Group Policy Management Console](https://learn.microsoft.com/en-us/en-us/internet-explorer/ie11-deploy-guide/group-policy-and-group-policy-mgmt-console-ie11) (GPMC), right-click the Group Policy Object (GPO) you want to configure and click **Edit**.
7. In the **Group Policy Management Editor**, go to **Computer configuration,** then **Preferences**, and then **Control panel settings**.
8. Right-click **Scheduled tasks**, point to **New**, and then click **Immediate task**.
9. In the **Task** window that opens, go to the **General** tab. Choose the local SYSTEM user account (BUILTIN\SYSTEM) under **Security options**.
10. Select **Run whether user is logged on or not** and check the **Run with highest privileges** check-box.
11. Go to the **Actions** tab and click **New...**. Ensure that **Start a program** is selected in the **Action** field. Enter the file name and location of the shared *DeviceComplianceOffboardingScript\_valid\_until\_YYYY-MM-DD.cmd* file.
12. Click **OK** and close any open GPMC windows.

## Monitor device configuration

With Group Policy there isn’t an option to monitor deployment of policies on the devices. Monitoring can be done directly in the Microsoft Purview portal, or by using other deployment tools such as Microsoft Endpoint Configuration Manager or Mobile Device Management tools.

## Monitor devices using the portal

To verify that onboarded devices are reporting correctly, use the following steps:

1. Go to the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149).
2. Click **Devices** list.
3. Verify that devices are appearing.

Note

It can take several days for devices to start showing on the **Devices list**. This includes the time it takes for the policies to be distributed to the device, the time it takes before the user logs on, and the time it takes for the endpoint to start reporting.
