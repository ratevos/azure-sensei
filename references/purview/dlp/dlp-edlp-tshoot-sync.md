# Troubleshooting endpoint data loss prevention configuration and policy sync

> Source: https://learn.microsoft.com/en-us/purview/dlp-edlp-tshoot-sync  
> Microsoft doc last updated: 2026-06-02


This article provides detailed instructions for:

1. Determining the device configuration and policy sync status values for [Windows devices](https://learn.microsoft.com/en-us/purview/device-onboarding-overview) and [macOS](https://learn.microsoft.com/en-us/purview/device-onboarding-macos-overview) devices that are successfully onboarded into Microsoft Purview Data Loss Prevention (DLP).
2. Identifying and resolving any issues with the configuration status and the policy sync status.
3. Reviewing and understanding the device attribute that are available for each device and their meaning.

## Device configuration and policy sync status values

**Configuration status** and the **Policy sync status** of all your onboarded devices have three possible values.

The **Configuration status** value shows you if the device is configured correctly, is sending a heartbeat signal to Purview, and the last time the configuration was validated. For Windows devices, configuration includes checking the status of [Microsoft Defender Antivirus always-on protection and behavior monitoring](https://learn.microsoft.com/en-us/en-us/microsoft-365/security/defender-endpoint/configure-real-time-protection-microsoft-defender-antivirus).

The **Policy sync status** shows you if the device received the latest policy version, or if the corresponding policies synced successfully to the device.

| Field value | Configuration status | Policy sync status |
| --- | --- | --- |
| Updated | Device health parameters are enabled and correctly set. This status indicates that the device's configuration is up to date with the recommended settings. | Device is up to date with the current versions of policies. |
| Not updated | Certain settings need attention. Follow the steps in the workflow diagram to address issues. You might need to enable the configuration settings for this device. Follow the procedures in [Microsoft Defender Antivirus always-on protection](https://learn.microsoft.com/en-us/en-us/microsoft-365/security/defender-endpoint/configure-real-time-protection-microsoft-defender-antivirus) | This device isn't synced the latest policy updates. It might take up to 2 hours for the status in the devices list to update. Follow the steps in the workflow diagram to address issues. |
| Not available | Device properties aren't available in the device list. This condition might be because the device doesn't meet the minimum OS version to provide visibility into its properties, or configuration, or if the device was just onboarded. Follow the steps in the workflow to address issues. | Device properties aren't available in the device list. This condition might be because the device doesn't meet the minimum OS version to provide visibility into its properties, or configuration, or if the device was just onboarded. Follow the steps in the workflow to address issues.  System shows **Not available** if there is no Endpoint DLP policy. |

Important

Devices must be online for the policy update to happen. If the status isn't updating, check the last time the device was seen.

## Device attribute details

To maintain overall device health from a DLP perspective, go beyond determining the configuration and policy sync status and troubleshooting any issues found. You need to understand the attributes of an onboarded device. The values for these attributes can provide useful information to help you track the device health.

| Device attribute | Note |
| --- | --- |
| Last seen | The most recent time that the device was determined to be online. |
| Last policy sync time | The timestamp of the previous instance when the device downloaded the latest policy versions. |
| OS | The current operating system. |
| Defender engine version | The version of the antivirus engine on the device. |
| Defender Mocamp version | The version of the Defender client. |
| MDATP device ID | The unique identifier assigned to this device. |
| Valid user | This indicates if the currently logged on user has a corresponding Entra ID account and is in scope of a DLP policy that's targeted at Devices. |
| Sensitive Data Activity | This provides a view all sensitive data activity for this device for the last 30 days. |
| Advanced classification bandwidth usage exceeded | This attribute shows if the bandwidth usage limit for Advanced Classification has been exceeded in the past 24 hours. |
| Endpoint DLP status | Shows if Endpoint DLP is enabled or disabled for the device. |

## Access device attribute data using Advanced Hunting

In addition to viewing device attributes in the Microsoft Purview portal, you can access the same Endpoint DLP device data through the [DeviceInfo table in Advanced hunting](https://learn.microsoft.com/en-us/en-us/defender-xdr/advanced-hunting-deviceinfo-table).

Previously, you could get device attribute data manually through the **Export** functionality on the Device onboarding page in the Microsoft Purview portal.

With the `DeviceInfo` table, you can:

- Query device attribute data using KQL
- Retrieve up-to-date information without manual exports
- Analyze device status across your environment
- Integrate device data into custom dashboards and third-party reporting platforms

### Access device data

To retrieve device attribute data:

1. Go to the **Microsoft Defender portal**
2. Navigate to **Investigation & response** &gt; **Hunting** &gt; **Advanced hunting**
3. Query the **`DeviceInfo`** table
4. Expand the **`DlpInfo`** column to view Endpoint DLP device details

Sample query:

```kusto
DeviceInfo 
| where DlpInfo != ""
| project DlpInfo
```

#### DlpInfo

The **DlpInfo** column contains Endpoint Data Loss Prevention device information in JSON format. The JSON object can be used to query and report on device configuration status, policy synchronization status, Endpoint DLP enablement, and other configuration details for onboarded devices. These values correspond to the device information available in the DLP device onboarding page.

Example value:

```json
{
 "IsDlpConfigurationValid": true,
 "DlpPolicyLastModifiedTimeUTC": "2026-01-14T20:00:47Z",
 "IsDlpEnabled": true,
 "IsDefenderRealTimeProtectionEnabled": true,
 "IsDefenderBehaviorMonitoringEnabled": true,
 "HasDlpACBandwidthExceeded": false,
 "HasDlpValidUpn": true,
 "DlpUpn": "user@contoso.com"
}
```

The following properties can be returned in the `DlpInfo` object:

| Property | Data type | Description |
| --- | --- | --- |
| IsDlpConfigurationValid | `boolean` | Indicates whether the device configuration health is valid. |
| DlpPolicyLastModifiedTimeUTC | `datetime` | Timestamp of the most recent DLP policy modification associated with the device, in Coordinated Universal Time (UTC). |
| IsDlpEnabled | `boolean` | Indicates whether Endpoint DLP is enabled on the device. |
| IsDefenderRealTimeProtectionEnabled | `boolean` | Indicates whether Microsoft Defender Real-time Protection is enabled on the device. |
| IsDefenderBehaviorMonitoringEnabled | `boolean` | Indicates whether Microsoft Defender Behavior Monitoring is enabled on the device. |
| HasDlpACBandwidthExceeded | `boolean` | Indicates whether the device has exceeded the DLP Advanced Classification bandwidth threshold. |
| HasDlpValidUpn | `boolean` | Indicates whether the device is associated with a valid user principal name (UPN). |
| DlpUpn | `string` | User principal name (UPN) associated with the device. |

#### Relationship to device attribute details

The fields in the `DlpInfo` column correspond directly to the device attributes described earlier. This correspondence enables you to investigate configuration and policy sync issues across multiple devices without relying on point-in-time exports.

Use this data to:

- Identify devices with invalid configurations
- Detect devices that aren't ready for Endpoint DLP enforcement
- Perform large-scale analysis beyond what the portal UI offers

## Configuration and policy sync troubleshooting workflow

This diagram provides a workflow that walks you through the steps for diagnosing and resolving configuration and policy synchronization status for onboarded devices.



## Check configuration status and resolve issues

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Settings** (gear icon in the upper right corner) &gt; **Device onboarding** &gt; **Devices**.
2. Apply filters to narrow down the list of devices and simplify your investigation.
3. Select a device to open the details pane for more information on the configuration status.
4. If the status is **Updated**, the device is configured correctly. No further action is required. You can move on to Check policy sync status and resolve issues.
5. If the status is **Not available** or **Not updated**, follow the remediation steps in the details pane and the steps in the workflow diagram.

## Check policy sync status and resolve issues

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Settings** (gear icon in the upper right corner) &gt; **Device onboarding** &gt; **Devices**.
2. Apply filters to narrow down the list of devices and simplify your investigation.
3. Select a device to open the details pane for more information on the policy sync status.
4. If the status is **Updated**, the device successfully received the latest policy version. No further action is required. You can move on to Check device details.
5. If the status is **Not updated** or **Not available**, follow the remediation steps in the details pane and the steps in the workflow diagram.

Tip

You can see the overall status of how policy sync to devices is working on the **Policy status** report. The **Policy status** report is available in the Microsoft Purview compliance portal on the &gt; **Data loss prevention** &gt; **Overview** page.

## Check device details

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Settings** (gear icon in the upper right corner) &gt; **Device onboarding** &gt; **Devices**.
2. Apply filters to narrow down the list of devices and simplify your investigation.
3. Select a device to open the details pane for more information on the specific device attributes under **Device details**.

## Collect evidence for a support ticket

If self-remediation isn't successful, gather evidence and open a support ticket for comprehensive support analysis.

From the **Device details** section, record the values for these fields:

- **OS**
- **Defender engine version**
- **Defender client version**
- **MDATP device ID**
- **Valid user**

For more guidance, see:

- [Run the client analyzer on Windows](https://learn.microsoft.com/en-us/en-us/defender-endpoint/run-analyzer-windows)
- [Run the client analyzer on macOS and Linux](https://learn.microsoft.com/en-us/en-us/defender-endpoint/run-analyzer-macos-linux)
