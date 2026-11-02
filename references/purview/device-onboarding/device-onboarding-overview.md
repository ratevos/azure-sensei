# Onboard Windows devices into Microsoft 365 overview

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-overview  
> Microsoft doc last updated: 2026-06-26


**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

Endpoint data loss prevention (Endpoint DLP) and insider risk management require that Windows 10 and Windows 11 devices be onboarded into the service so that they can send monitoring data to the services.

Endpoint DLP allows you to monitor Windows 10 or Windows 11 devices and detect when sensitive items are used and shared. This gives you the visibility and control you need to ensure that they're used and protected properly, and to help prevent risky behavior that might compromise them. For more information about all of Microsoft’s DLP offerings, see [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp). To learn more about Endpoint DLP, see [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about).

Endpoint DLP also allows you to onboard devices running Windows Server 2019 and later versions.

Note

Installing the supported Windows Server KBs disables the *Classification* feature on the server. This means that Endpoint DLP won't classify files on the server. However, Endpoint DLP will still protect those files on the server that were classified before those KBs were installed on server. To ensure this protection, install Microsoft Defender version 4.18.23100 (October 2023) or later.

By default, Endpoint DLP isn't enabled for Windows servers when they're initially onboarded. Before you can see Endpoint DLP events for your servers in Activity Explorer, you must first turn on [Endpoint DLP support for onboarded servers](https://learn.microsoft.com/en-us/en-us/purview/dlp-configure-endpoint-settings).

Once properly configured, the same data loss protection policies can be automatically applied to both Windows PCs and Windows servers.

Insider risk management uses the full breadth of service and 3rd-party indicators to help you quickly identify, triage, and act on risky user activity. By using logs from Microsoft 365 and Microsoft Graph, insider risk management allows you to define specific policies to identify risk indicators and to take action to mitigate these risks. For more information, see [Learn about insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management).

Device onboarding is shared across Microsoft 365 and Microsoft Defender for Endpoint (MDE). If you've already onboarded devices to MDE, they appear in the managed devices list and no further steps are necessary to onboard those specific devices. Onboarding devices in Microsoft Purview portal also onboards them into MDE.

## Before you begin

### SKU/subscriptions licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

Important

For information on managing user licensing for devices see [Available plans](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#available-plans).

### Permissions

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

Caution

Device management currently only supports Entra roles. Purview roles are not supported.

To enable device management, the account you use must be a member of any one of these roles:

- Security admin
- Compliance admin
- Global admin

If you want to use a custom account to view the device management settings, it must be in one of these roles:

- Compliance admin
- Compliance data admin
- Global reader
- Security admin
- Global admin

If you want to use a custom account to access the onboarding/offboarding page, it must be in one of these roles:

- Compliance admin
- Security admin
- Global admin

If you want to use a custom account to turn on/off device monitoring, it must be in one of these roles:

- Compliance admin
- Security admin
- Global admin

### Prepare your Windows devices

Make sure that the Windows devices that you need to onboard meet these requirements.

1. Must be running one of the following builds of Windows or Windows Server:

    1. Windows (X64):

        1. Windows 11 24H2 ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-24h2-update-history-0929c747-1815-4543-8461-0160d16f15e5))
        2. Windows 11 23H2 ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-23h2-update-history-59875222-b990-4bd9-932f-91a5954de434))
        3. Windows 11 22H2 update ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-22h2-update-history-ec4229c3-9c5f-4e75-9d6d-9025ab70fcce))
        4. Windows 11 21H2 ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-21h2-update-history-a19cd327-b57f-44b9-84e0-26ced7109ba9))
        5. Windows 10 22H2 update ([See update details](https://support.microsoft.com/en-us/topic/windows-10-update-history-8127c2c6-6edf-4fdf-8b9f-0f7be1ef3562))
    2. Windows (ARM64):

        1. Windows 11 24H2 ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-24h2-update-history-0929c747-1815-4543-8461-0160d16f15e5))
        2. Windows 11 23H2 ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-23h2-update-history-59875222-b990-4bd9-932f-91a5954de434))
        3. Windows 11 22H2 update ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-22h2-update-history-ec4229c3-9c5f-4e75-9d6d-9025ab70fcce))
        4. Windows 11 21H2 ([See update details](https://support.microsoft.com/en-us/topic/windows-11-version-21h2-update-history-a19cd327-b57f-44b9-84e0-26ced7109ba9))
    3. Windows Server 2019 OS: 1809 onwards or Windows Server 2022 OS: 21H2 onwards.
    4. Anti-malware Client Version is 4.18.2110 or newer. Check your current version by opening Windows Security app, select the Settings icon, and then select About. The version number is listed under anti-malware Client Version. Update to the latest anti-malware Client Version by installing Windows Update KB4052623. For more information, see: [Microsoft Defender Antivirus in Windows](https://learn.microsoft.com/en-us/en-us/defender-endpoint/microsoft-defender-antivirus-windows). After a new anti-malware Client version or a new anti-malware Engine version is released, versions older than N-2 are no longer supported.

    Important

    None of Windows Security components need to be active, but the [Real-time protection and Behavior monitor](https://learn.microsoft.com/en-us/en-us/windows/security/threat-protection/microsoft-defender-antivirus/configure-real-time-protection-microsoft-defender-antivirus) must be enabled.

    After a new anti-malware Client version or a new anti-malware Engine version is released, versions older than N-2 are no longer supported.
2. All devices must be one of these:

    - [Microsoft Entra joined](https://learn.microsoft.com/en-us/en-us/azure/active-directory/devices/concept-azure-ad-join)
    - [Microsoft Entra hybrid joined](https://learn.microsoft.com/en-us/en-us/azure/active-directory/devices/concept-azure-ad-join-hybrid)
    - [Microsoft Entra registered](https://learn.microsoft.com/en-us/en-us/azure/active-directory/user-help/user-help-register-device-on-network)
3. A supported version of Microsoft 365 Apps is installed and up to date. For the most robust protection and user experience, ensure Microsoft 365 Apps version 16.0.14701.0 or later is installed.

    Note

    - If you're running Office 365 - KB 4577063 is required.
    - If you are on Monthly Enterprise Channel of Microsoft 365 Apps versions 2004-2008, you need to update to version 2009 or later. See [Update history for Microsoft 365 Apps (listed by date)](https://learn.microsoft.com/en-us/en-us/officeupdates/update-history-microsoft365-apps-by-date) for current versions. To learn more about known issue, see the Office Suite section of [Release notes for Current Channel releases in 2020](https://learn.microsoft.com/en-us/en-us/officeupdates/current-channel#version-2010-october-27).
4. If you have endpoints that use a device proxy to connect to the internet, follow the procedures in [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp).

    Important

    Make sure you allow *MpDlpService.exe* through your firewall, third-party antivirus software, or application control.
5. Here are the prerequisites for each feature.

| Feature | Prerequisite |
| --- | --- |
| Add hyperlink support in warn and block toast messages (Roadmap ID 480733) | Anti-malware Client Version 4.18.25010 or newer is required. |
| IP or IP address ranges support within Sensitive service domain groups (Roadmap ID 479759) | Anti-malware Client Version 4.18.25010 or newer is required. |
| Allow and Off modes in the policy (Roadmap ID 481356) | anti-malware Client Version 4.18.25010 or newer is required. |
| Device and Device group-based policy scoping support for Endpoint DLP (Roadmap ID 480732) | Windows 10: [See update details](https://support.microsoft.com/en-us/topic/april-8-2025-kb5055518-os-builds-19044-5737-and-19045-5737-6329246b-63bb-4d0a-9e95-e22926fbbe51)Windows 11 22H2: [See update details](https://support.microsoft.com/en-us/topic/april-22-2025-kb5055629-os-22621-5262-and-22631-5262-preview-40cbe5df-063a-4b89-94eb-c79c8975506d)Windows 11 23H2: [See update details](https://support.microsoft.com/en-us/topic/april-22-2025-kb5055629-os-22621-5262-and-22631-5262-preview-40cbe5df-063a-4b89-94eb-c79c8975506d)Windows 11 24H2: [See update details](https://support.microsoft.com/en-us/topic/april-25-2025-kb5055627-os-build-26100-3915-preview-9324a361-965a-4496-8fd8-ba8a9de9fc38) |
| Full file evidence support for restricted apps (Roadmap ID 479757) | Anti-malware Client Version 4.18.25020 or newer is required. |
| Pause and Resume support for printer (Roadmap ID 486369) | Anti-malware Client Version 4.18.25030 or newer is required. |
| Increase file type coverage to 100+ (Roadmap ID 416481) | Windows 10: [See update details](https://support.microsoft.com/en-us/topic/april-8-2025-kb5055518-os-builds-19044-5737-and-19045-5737-6329246b-63bb-4d0a-9e95-e22926fbbe51)Windows 11 22H2: [See update details](https://support.microsoft.com/en-us/topic/april-22-2025-kb5055629-os-22621-5262-and-22631-5262-preview-40cbe5df-063a-4b89-94eb-c79c8975506d)Windows 11 23H2: [See update details](https://support.microsoft.com/en-us/topic/april-22-2025-kb5055629-os-22621-5262-and-22631-5262-preview-40cbe5df-063a-4b89-94eb-c79c8975506d)Windows 11 24H2: [See update details](https://support.microsoft.com/en-us/topic/april-25-2025-kb5055627-os-build-26100-3915-preview-9324a361-965a-4496-8fd8-ba8a9de9fc38) |
| Endpoint DLP support for Teams | Anti-malware Client Version 4.18.25050 or newer is required. |
| Advanced label-based protection for all files on devices (Roadmap ID 487859) | Information protection client version: 3.1.309 or newer is required.Anti-malware Client Version 4.18.25050 or newer is required.Windows 10: [See update details](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060533-os-builds-19044-5965-and-19045-5965-eeae388c-ca1c-4569-95d7-3d7be2e0b8ba)Windows 11 22H2: [See update details](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060999-os-builds-os-builds-22621-5472-and-22631-5472-97dbff21-2edb-4566-be47-18f732a218b9)Windows 11 23H2: [See update details](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060999-os-builds-os-builds-22621-5472-and-22631-5472-97dbff21-2edb-4566-be47-18f732a218b9)Windows 11 24H2: [See update details](https://support.microsoft.com/en-us/topic/june-11-2025-kb5063060-os-build-26100-4351-out-of-band-b1746442-8c6c-425d-ac5a-3a8f51e372f3) |
| Network share/Removable media/Printer group support on Edge (Roadmap ID 486370) | Edge: 137 or newer is required.Anti-malware Client Version 4.18.25050 or newer is required. |
| OneDrive shadow file protection support (Roadmap ID 489842) | Anti-malware Client Version 4.18.26020 or newer is required. |
| Restricted apps and app groups support on Edge (Roadmap ID 485769) | Anti-malware Client Version 4.18.25080 or newer is required. |
| Logged-in user details (user email) on the device onboarding page (Roadmap ID 548669) | Anti-malware Client Version 4.18.26030 or newer is required.Windows 10: [See update details](https://support.microsoft.com/en-us/topic/windows-10-update-history-8127c2c6-6edf-4fdf-8b9f-0f7be1ef3562)Windows 11 22H2: [See update details](https://support.microsoft.com/en-us/topic/march-10-2026-kb5078883-os-build-22631-6783-7019f7bc-a58f-40dc-b1b0-ab187f433675)Windows 11 23H2: [See update details](https://support.microsoft.com/en-us/topic/march-10-2026-kb5078883-os-build-22631-6783-7019f7bc-a58f-40dc-b1b0-ab187f433675)Windows 11 24H2: [See update details](https://support.microsoft.com/en-us/topic/march-31-2026-kb5086672-os-builds-26200-8117-and-26100-8117-out-of-band-45cc1666-b34f-4ea6-bc93-f67defff8c38) |
| Device health details in the export function on the device onboarding page and in Advanced hunting on Security portal (Roadmap ID 542792) | Anti-malware Client Version 4.18.26030 or newer is required.Windows 10: [See update details](https://support.microsoft.com/en-us/topic/windows-10-update-history-8127c2c6-6edf-4fdf-8b9f-0f7be1ef3562)Windows 11 22H2: [See update details](https://support.microsoft.com/en-us/topic/march-10-2026-kb5078883-os-build-22631-6783-7019f7bc-a58f-40dc-b1b0-ab187f433675)Windows 11 23H2: [See update details](https://support.microsoft.com/en-us/topic/march-10-2026-kb5078883-os-build-22631-6783-7019f7bc-a58f-40dc-b1b0-ab187f433675)Windows 11 24H2: [See update details](https://support.microsoft.com/en-us/topic/march-31-2026-kb5086672-os-builds-26200-8117-and-26100-8117-out-of-band-45cc1666-b34f-4ea6-bc93-f67defff8c38) |
| Network share/Removable media/Printer group support on Edge (Roadmap ID 486370) | Edge: 137 or newer is required.Anti-malware Client Version 4.18.25050 or newer is required. |
| Hyperlink within toast messages for the Edge browser (Roadmap ID 558688) | Anti-malware Client Version 4.18.26040 or newer is required. |
| Print resume support for Just-in-time protection (JIT) | Anti-malware Client Version 4.18.26040 or newer is required. |

## Onboarding Windows 10 or Windows 11 devices

You must enable device monitoring and onboard your endpoints before you can monitor and protect sensitive items on a device. Both of these actions are done in the Microsoft Purview portal.

When you want to onboard devices that haven't been onboarded yet, you download the appropriate script and deploy it to those devices. Follow the device onboarding procedures below.

If you already have devices onboarded into [Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/en-us/windows/security/threat-protection/), they'll already appear in the managed devices list.

In this deployment scenario, you onboard Windows 10 or Windows 11 devices that haven't been onboarded yet.

1. Open the [Microsoft Purview portal](https://purview.microsoft.com). Choose **Settings** &gt; **Device onboarding** &gt; **Devices**.

    Note

    If you have previously deployed Microsoft Defender for Endpoint, all the devices that were onboarded during that process will be listed in the **Devices** list. There's no need to onboard them again. While it usually takes about 60 seconds for device onboarding to be enabled, allow up to 30 minutes before engaging with Microsoft support.
2. Choose **Turn on device onboarding**.
3. Choose **Onboarding** to begin the onboarding process.
4. Choose the way you want to deploy to these other devices from the **Deployment method** list and then **download package**.
5. Choose the appropriate procedure to follow from the table below:

    | Article | Description |
    | --- | --- |
    | [Intune](https://learn.microsoft.com/en-us/purview/device-onboarding-mdm) | Use Mobile Device Management tools or Microsoft Intune to deploy the configuration package on device. |
    | [Configuration Manager](https://learn.microsoft.com/en-us/purview/device-onboarding-sccm) | You can use either use Microsoft Endpoint Configuration Manager (current branch) version 1606 or Microsoft Endpoint Configuration Manager (current branch) version 1602 or earlier to deploy the configuration package on devices. |
    | [Group Policy](https://learn.microsoft.com/en-us/purview/device-onboarding-gp) | Use Group Policy to deploy the configuration package on devices. |
    | [Local script](https://learn.microsoft.com/en-us/purview/device-onboarding-script) | Learn how to use the local script to deploy the configuration package on endpoints. |
    | [Virtual desktop infrastructure (VDI) devices](https://learn.microsoft.com/en-us/purview/device-onboarding-vdi) | Learn how to use the configuration package to configure VDI devices. |

## Check device status

After onboarding your devices, you can monitor **Configuration status** and **Policy Sync status** to ensure devices are properly set up to receive policy updates. To learn what Configuration status and Policy sync status mean, see: [Understand device configuration and policy sync status values](https://learn.microsoft.com/en-us/purview/dlp-edlp-tshoot-sync#troubleshooting-endpoint-data-loss-prevention-configuration-and-policy-sync)

To view these details, go to **Device onboarding** &gt; **Devices**. From there, you can review each device's current configuration state and confirm whether policies have successfully synced. For guidance on resolving **Configuration** **status** or **Policy Sync status** issues, see: [Troubleshooting endpoint data loss prevention configuration and policy sync](https://learn.microsoft.com/en-us/purview/dlp-edlp-tshoot-sync#troubleshooting-endpoint-data-loss-prevention-configuration-and-policy-sync)

Note

Onboarded devices will continue to appear for 180 days after the device is offline.
