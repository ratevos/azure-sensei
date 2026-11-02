# Get started with endpoint data loss prevention

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started  
> Microsoft doc last updated: 2026-08-20


Endpoint data loss prevention (Endpoint DLP) is part of the Microsoft Purview Data Loss Prevention (DLP) suite of features you can use to discover and protect sensitive items across Microsoft 365 services. For more information about all of Microsoft's DLP offerings, see [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp). To learn more about Endpoint DLP, see [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)

Microsoft Endpoint DLP allows you to monitor [onboarded Windows 10, and Windows 11](https://learn.microsoft.com/en-us/purview/device-onboarding-overview) and [onboarded macOS devices](https://learn.microsoft.com/en-us/purview/device-onboarding-macos-overview) running any of the three latest released versions. Once a device is onboarded, DLP detects when sensitive items are used and shared. This gives you the visibility and control you need to ensure that they're used and protected properly, and to help prevent risky behavior that might compromise them.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

### SKU/subscriptions licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

Important

Endpoint DLP policy targeting can be configured using a combination of users and devices. If a policy is scoped to devices where the signed-in users do not meet the [required criteria](https://learn.microsoft.com/en-us/purview/device-onboarding-overview#before-you-begin), ensure those users or devices or both are explicitly excluded from the policy. Failure to do so may lead to unintended policy enforcement behavior.

### Configure proxy on the Windows 10 or Windows 11 device

If you're onboarding Windows 10 or Windows 11 devices, check to make sure that the device can communicate with the cloud DLP service. For more information, see, [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp).

## Windows 10 and Windows 11 Onboarding procedures

For a general introduction to onboarding Windows devices, see:

- [Onboard Windows devices into Microsoft 365 overview](https://learn.microsoft.com/en-us/purview/device-onboarding-overview#onboard-windows-devices-into-microsoft-365-overview)

For specific guidance to onboarding Windows devices, see:

| Article | Description |
| --- | --- |
| [Onboard Windows 10 or 11 devices using Group Policy](https://learn.microsoft.com/en-us/purview/device-onboarding-gp) | Use Group Policy to deploy the configuration package on devices. |
| [Onboard Windows 10 or 11 devices using Microsoft Endpoint Configuration Manager](https://learn.microsoft.com/en-us/purview/device-onboarding-sccm) | You can use either use Microsoft Endpoint Configuration Manager (current branch) version 1606 or Microsoft Endpoint Configuration Manager (current branch) version 1602 or earlier to deploy the configuration package on devices. |
| [Onboard Windows 10 or 11 devices using Microsoft Intune](https://learn.microsoft.com/en-us/purview/device-onboarding-mdm) | Use Microsoft Intune to deploy the configuration package on device. |
| [Onboard Windows 10 or 11 devices using a local script](https://learn.microsoft.com/en-us/purview/device-onboarding-script) | Learn how to use the local script to deploy the configuration package on endpoints. |
| [Onboard non-persistent virtual desktop infrastructure (VDI) devices](https://learn.microsoft.com/en-us/purview/device-onboarding-vdi) | Learn how to use the configuration package to configure VDI devices. |

### Endpoint DLP support for virtualized environments

You can onboard virtual machines as monitored devices in Microsoft Purview portal. There's no change to the onboarding procedures listed above.

The table that follows lists the virtual operating systems that are supported by virtualization environments.

| Virtualizationplatform | Windows 10 | Windows 11 | Windows Server 2019 | Windows Server 202221H2, 22H2, Data Center |
| --- | --- | --- | --- | --- |
| Azure virtual desktop (AVD) | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | Single session and Multi session supported. | Supported |
| Windows 365 | - Supported for 21H2, 22H2 | - Supported for 21H2, 22H2 | Not applicable | Not applicable |
| Citrix Virtual Apps and Desktops 7 (2209 and higher) | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | - Single session supported for 21H2, 22H2<br>- Multi session supported for 21H2, 22H2 | Supported | Supported |
| Amazon workspaces | - Single session supported for 21H2, 22H2 | Not applicable | - Windows 10 powered by Windows Server 2019 | Not applicable |
| Hyper-V | - Single session supported for 21H2, 22H2<br>- Multi session with Hybrid AD join supported for 21H2, 22H2 | - Single session supported for 21H2, 22H2<br>- Multi session with Hybrid AD join supported for 21H2, 22H2 | Supported with Hybrid AD join | Supported with Hybrid AD join |

#### Known issues

1. You can't monitor **Copy to Clipboard** and **Enforcing Endpoint DLP** on Azure Virtual Desktop environments via browsers. However, the same egress operation will be monitored by **Endpoint DLP for actions via Remote Desktop Session (RDP)**.
2. Citrix XenApp doesn't support access by restricted app monitoring.

#### Limitations

1. Handling of USBs in virtualized environments: USB storage devices are treated as network shares. You need to include the **Copy to network share** activity to monitor **Copy to a USB device**. All activity explorer events for virtual devices and incident alerts show the **Copy to a network share** activity for all copy to USB events.

## macOS onboarding procedures

For a general introduction to onboarding macOS devices, see:

- [Onboard macOS devices into Microsoft Purview](https://learn.microsoft.com/en-us/purview/device-onboarding-macos-overview)

For specific guidance to onboarding macOS devices, see:

Important

There are important permission changes for Microsoft Purview Endpoint DLP in macOS 27. If you're onboarding or upgrading devices that run macOS 27, review the updated guidance before deployment. For more information, see [Microsoft Purview Endpoint DLP on macOS 27 (Preview)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-macos-27-changes).

| Article | Description |
| --- | --- |
| [Intune](https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-intune) | For macOS devices that are managed through Intune |
| [Intune for Microsoft Defender for Endpoint customers](https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-intune-mde) | For macOS devices that are managed through Intune and that have Microsoft Defender for Endpoint (MDE) deployed to them |
| [JAMF Pro)](https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro) | For macOS devices that are managed through JAMF Pro |
| [JAMF Pro for Microsoft Defender for Endpoint customers)](https://learn.microsoft.com/en-us/purview/device-onboarding-offboarding-macos-jamfpro-mde) | For macOS devices that are managed through JAMF Pro and that have Microsoft Defender for Endpoint (MDE) deployed to them |

Once a device is onboarded, it should be visible in the devices list, and should start reporting audit activity to Activity explorer.
