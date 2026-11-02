# Monitor Endpoint DLP Device Health in Microsoft Purview

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-health-reports-dashboard  
> Microsoft doc last updated: 2026-06-03


The device health reporting dashboard in Microsoft Purview gives compliance and security administrators a centralized view of device readiness for Endpoint Data Loss Prevention (Endpoint DLP). Use the dashboard to monitor device onboarding status, policy update readiness, and feature readiness for Endpoint DLP.

The dashboard helps you find devices that might not be ready to receive or enforce Endpoint DLP policies because of configuration, connectivity, or version issues. It consolidates device health insights, reducing manual troubleshooting across multiple pages.

## Before you begin

To access the device health reporting dashboard, you must have one of the following roles:

- Compliance Administrator
- Security Administrator
- Global Administrator

Tip

Use the least-privileged role that meets your needs. For most organizations, the Compliance Administrator or Security Administrator role is sufficient.

Devices must also:

- Be onboarded to Endpoint DLP
- Be actively reporting device telemetry

For information about onboarding devices, see [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/en-us/purview/endpoint-dlp-getting-started).

## Open the device health reporting dashboard

To open the device health reporting dashboard, follow these steps:

1. Go to the Microsoft Purview portal.
2. Select **Settings** &gt; **Device onboarding** &gt; **Device report**.

## What the dashboard shows

The dashboard displays data from devices that reported within the past 30 days. It updateevery hour. Each section is interactive — select **View devices** to open a side pane with device categories, then select a category to open a filtered list of matching devices.

| Visualization | Description | Use case |
| --- | --- | --- |
| **Device onboarding** | Provides an overview of onboarded devices, including: total onboarded devices, onboarded devices running Endpoint DLP, onboarded devices with configuration issues. | Use this section to quickly understand overall onboarding coverage and identify devices that may require configuration remediation. |
| **Device readiness to receive policy updates** | Shows devices that may not be ready to receive future Endpoint DLP policy updates because of: offline status during the past day, outdated Microsoft Defender Antivirus versions, configuration issues. These indicators don't confirm whether a device failed to receive a policy update, but instead highlight devices that may be at risk of not receiving future updates. | Use this section to proactively identify devices that may require remediation to remain ready for future policy updates. |
| **Last time devices were seen online** | Provides a breakdown of devices based on when each device was last seen online. Devices are grouped into separate, non-cumulative buckets based on their latest *Last seen* timestamp, including devices seen in the last 24 hours, 3 days, 7 days, and 30 days. Each device is counted only once in the most recent applicable bucket. This visualization helps you understand device activity, connectivity, and reporting recency across your organization. | Use this section to understand how recently devices have been active or reporting activity across your organization. |
| **Device readiness for feature** | Displays readiness information for supported Endpoint DLP features. Currently, this section supports readiness reporting for: Just-in-time protection, Paste to supported browsers. This section shows how many devices are ready for each feature, and how many require updates before a feature can be used. Additional Endpoint DLP features will be added to this section in future releases. | Use this section to validate readiness before enabling or deploying Endpoint DLP features across devices. |

## Monitor device readiness

Use the dashboard to monitor device posture at scale, find misconfigured devices, detect devices that might not receive Endpoint DLP policy updates, and validate readiness before deploying new features.

To investigate device health issues, follow this typical workflow:

1. Review dashboard summaries to identify problem areas.
2. Select a dashboard segment to open a filtered list of affected devices.
3. Investigate individual devices.
4. Identify root cause issues such as:

    - Outdated versions
    - Connectivity issues
    - Invalid configurations

## Common scenarios

### Monitor device posture across your organization

Organizations need to monitor device health and readiness at scale to ensure devices remain ready to receive the latest policies and supported Endpoint DLP features. Use the dashboard to continuously monitor onboarding status, policy update readiness, feature readiness, and recent device activity. The dashboard helps you find devices that need remediation.

### Identify onboarded devices with configuration issues

Onboarded devices may still have configuration issues that affect Endpoint DLP enforcement or feature readiness. Use the **Device onboarding** visualization to review Endpoint DLP coverage and find devices with configuration issues that need remediation.

### Identify devices that may not be ready to receive policy updates

Some devices may not be ready to receive Endpoint DLP policy updates because of connectivity, Defender version, or configuration issues. These indicators don't confirm whether a device failed to receive an update, but highlight devices at risk of not receiving future updates. Use the **Device readiness to receive policy updates** visualization to find these devices and plan remediation.

### Monitor device connectivity

Device connectivity affects readiness for policy updates and Endpoint DLP features. Use the **Last time devices were seen** visualization to view when devices were last seen online — in the past 24 hours, 3 days, 7 days, or 30 days. This breakdown helps you evaluate device activity patterns across your organization.

### Validate readiness before enabling Endpoint DLP features

Some Endpoint DLP features require devices to meet specific configuration or version requirements. Use the **Device readiness for feature** visualization to validate whether devices are ready for supported features, including Just-in-time protection and Paste to supported browsers.

## Best practices

- **Review the dashboard regularly.** Frequent checks help you catch device health trends before they become widespread issues.
- **Investigate devices that haven't reported recently.** Devices offline for extended periods may miss critical policy updates.
- **Validate readiness before deploying new policies or features.** Confirm that devices meet configuration and version requirements to avoid failed deployments.
- **Prioritize remediation for devices with outdated Defender versions.** Outdated Microsoft Defender Antivirus versions can prevent devices from receiving Endpoint DLP policies.
