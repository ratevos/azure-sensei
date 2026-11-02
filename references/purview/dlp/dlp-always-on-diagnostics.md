# Always-on diagnostics for endpoint DLP

> Source: https://learn.microsoft.com/en-us/purview/dlp-always-on-diagnostics  
> Microsoft doc last updated: 2026-09-04


The Always-on diagnostics feature in Microsoft Purview enables continuous, automated trace logging for endpoint data loss prevention (DLP). This functionality significantly reduces administrative overhead by eliminating the need for manual log configuration and issue reproduction.

When a support case is opened with Microsoft, diagnostic logs are often required to assist with root cause analysis. With Always-on diagnostics enabled, comprehensive telemetry is already available, allowing administrators to bypass traditional data collection steps. This not only accelerates the support workflow but also improves accuracy in identifying and resolving issues.

Diagnostic logs can be securely uploaded directly to Microsoft Support, streamlining case submission and accelerating time-to-resolution. This proactive logging approach enhances operational efficiency and improves support responsiveness.

## Trace logs

When an admin turns on Always-on diagnostics, the feature is enabled on all onboarded Windows devices, including servers, and all onboarded macOS devices. When an Endpoint DLP policy does not behave as expected for an in-scope user or device, the customer opens a Microsoft support case. To expedite troubleshooting, Microsoft Support requests diagnostic trace logs, which the customer administrator collects from the affected device using documented procedures. The collected data is protected by Microsoft through restricted access controls and a proprietary log format.

### Understanding upload behavior and operational constraints

Trace uploads typically occur within a 24-hour polling window and require the device to remain online for the upload to complete. Only one active collection request is supported per device at any given time, and additional requests can be initiated only after the prior request completes, fails, or is deleted. Restart-based upload acceleration is supported, but restarting the device isn't required to complete an upload. It's intended only to speed up the process. Collection requests may remain pending if the device is offline, wiped, reimaged, reassigned, or otherwise unable to respond.

Admins are responsible for monitoring the status of collection requests and for taking action when failures occur. If a request fails, admins must retry or re‑initiate the request as needed to ensure successful data collection.

### Understanding log access, security, and data storage compliance

Logs aren’t available for direct download by admins and are stored in a proprietary Microsoft‑internal format that can only be decoded using Microsoft tools. Access to logs is restricted to Microsoft personnel who are members of designated access groups, and all such access is fully audited to ensure accountability and security.

Logs are stored in Microsoft‑managed Azure Blob Storage and comply with Microsoft security and privacy standards, including GDPR. Data remains within the tenant’s data residency region and is retained for 180 days unless manually deleted earlier. After the retention period, logs are automatically purged and can’t be recovered, and no backup or extended retention is supported.

Important

This feature is only for authorized eDLP troubleshooting scenarios (whether functioning or not). It must not be used for investigative or non-support purposes, including any activity outside approved troubleshooting workflows.

This feature is supported on Windows and macOS.

## Permissions required for always-on diagnostics

### Roles required to view and create log collection requests

There are multiple roles that allow you to view and create log collection requests. The account you use must be a member of any one of them.

#### Microsoft Entra roles

- Compliance Administrator
- Security Administrator
- Global Administrator

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](https://learn.microsoft.com/en-us/purview/purview-permissions).

#### Purview roles for viewing and creating log collection requests

Must be assigned at the tenant level; scoped admins are not supported:

- OrganizationConfiguration
- ManageAlerts
- ViewOnlyManageAlerts
- InformationProtectionAdmin
- InformationProtectionAnalyst
- InformationProtectionInvestigator

### Roles required to enable the feature

The account that you use must be a member of any one of the following roles to turn on Always-on diagnostics.

#### Microsoft Entra roles for enabling always-on diagnostics

- Compliance Administrator
- Security Administrator
- Global Administrator

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](https://learn.microsoft.com/en-us/purview/purview-permissions).

#### Purview roles (tenant-level only)

The following tenant-level Purview roles can enable Always-on diagnostics:

- OrganizationConfiguration
- ComplianceAdmin
- SecurityAdmin
- DLPComplianceManagement
- InformationProtectionAdmin

## Prerequisites

The device must be onboarded to Microsoft Purview and actively reporting with Always‑on Diagnostics enabled. It must maintain continuous network connectivity and be able to reach Microsoft upload endpoints, including \*.blob.core.windows.net. Outbound HTTPS traffic to Microsoft services must not be blocked by firewalls, proxies, or security policies, and any proxy configuration must allow outbound HTTPS traffic without interception or modification that would prevent uploads.

If you are using Windows Server, you must [enable endpoint DLP for Windows Servers](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#enable-endpoint-dlp-for-windows-servers) before turning on Always-on diagnostics, because endpoint DLP is disabled by default on Windows Server.

If you are using macOS, the device must be onboarded to Microsoft Purview through Intune, JAMF Pro, or another MDM solution. For more information, see [Onboard macOS devices into Microsoft Purview](https://learn.microsoft.com/en-us/purview/device-onboarding-macos-overview).

## Supported Windows operating systems

The following table lists the supported Windows client and server versions for Always-on diagnostics.

| OS | Version | Minimum Build |
| --- | --- | --- |
| Windows 11 | 24H2 | [Build 26100.4202](https://support.microsoft.com/en-us/topic/may-28-2025-kb5058499-os-build-26100-4202-preview-d4c2f1ee-8138-4038-b705-546945076f92) |
| Windows 11 | 23H2 | [Build 22621.5039 and 22631.5039](https://support.microsoft.com/en-us/topic/may-27-2025-kb5058502-os-22621-5413-and-22631-5413-preview-6291789c-1eea-4227-9740-a701af6de688) |
| Windows 11 | 22H2 | [Build 22621.5039 and 22631.5039](https://support.microsoft.com/en-us/topic/may-27-2025-kb5058502-os-22621-5413-and-22631-5413-preview-6291789c-1eea-4227-9740-a701af6de688) |
| Windows 10 | 22H2 | [Build 19045.5917](https://support.microsoft.com/en-us/topic/may-28-2025-kb5058481-os-build-19045-5917-preview-7698d6e7-dd65-494d-b523-aa4c6aa913a2) |
| Windows 10 | 21H2 | [Build 19045.5917](https://support.microsoft.com/en-us/topic/may-28-2025-kb5058481-os-build-19045-5917-preview-7698d6e7-dd65-494d-b523-aa4c6aa913a2) |
| Windows Server 2019 | - | [Build 17763.7434](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060531-os-build-17763-7434-32fce7e7-305d-4d32-913f-3fdc0709a763) |
| Windows Server 2022 | - | [Build 20348.3807](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060526-os-build-20348-3807-4e9453c4-6602-48ea-b349-689cd66dfdb9) |
| Windows Server 2025 | - | [Build 26100.4349](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060842-os-build-26100-4349-d7d4793c-bb41-4e4a-bfbd-a0dbdb2f6055) |

Important

Endpoint DLP is disabled by default on Windows Server. You must [enable endpoint DLP for Windows Servers](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#enable-endpoint-dlp-for-windows-servers) to support always-on diagnostics.

## Supported macOS versions

Always-on diagnostics is supported on onboarded macOS devices running any of the three latest released versions. Always-on diagnostics requires build 101.26042.xxxx or later.

### Supported processors

macOS devices with x64 and M1, M2, and M3 (ARM64) processors are supported.

## Turn on Always-on diagnostics and enable upload

Perform the following steps to turn on Always-on diagnostics and enable log upload. These settings apply to both Windows and macOS devices.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Navigate to **Settings** &gt; **Data Loss Prevention** &gt; **Always-on diagnostics (preview)**.
3. Select **On**.
4. Set the cache storage period. A 90-day cache storage period is recommended.
5. Set the maximum storage for the device. The value must be between 500 and 1,500 MB.
6. Select **Save**.
7. To enable upload, under **Automatically upload device logs** select **Share diagnostics with Microsoft**.

## Request device logs

When you identify an issue and open a support case with Microsoft, you can request that the log files be sent to Microsoft Support. The procedure is the same for Windows and macOS devices.

1. In Purview, select one of the locations to initiate a request for log files.
    1. From **Settings &gt; Device onboarding &gt; Devices**, select a device from the list.
    2. From **Data Loss Prevention &gt; Alerts &gt; Events**, select an event from the list.
    3. From **Data Loss Prevention &gt; Explorers &gt; Activity explorer**, select an alert from the list.
2. Based on the location you chose, under **Always-on Diagnostics** select **Request device log**.
3. Select the date range and provide a short description.
4. Select **Submit collection request**.
5. After you submit the request, you must wait until the request is complete. Navigate to **Settings** &gt; **Data Loss Prevention** &gt; **Always-on diagnostics (preview)**.
6. From the list, identify the device under investigation. When the status is complete, provide the associated request number to Microsoft Support.
