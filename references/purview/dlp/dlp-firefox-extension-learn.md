# Learn about the Microsoft Purview extension for Firefox

> Source: https://learn.microsoft.com/en-us/purview/dlp-firefox-extension-learn  
> Microsoft doc last updated: 2024-08-21


[Endpoint data loss prevention (endpoint DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about) extends the activity monitoring and protection capabilities of [Microsoft Purview data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) to sensitive items that are on Windows 10/11 devices. Once you onboard devices to the Microsoft Purview solutions, the information about what users are doing with sensitive items is made visible in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). Then you can enforce protective actions on those items via [DLP policies](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp).

After you install the Firefox extension on a Windows 10/11 device, your organization can monitor when a user attempts to access or upload a sensitive item to a cloud service using Mozilla Firefox, and enforce protective actions via DLP.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Activities you can monitor and take action on

The extension enables you to audit and manage the following types of activities users take on sensitive items on devices running Mozilla Firefox in Windows 10.

| activity | description | supported policy actions |
| --- | --- | --- |
| file copied to cloud | Detects when a user attempts to upload a sensitive item to a restricted service domain through the Firefox browser | audit, block with override, block |
| file printed | Detects when a user attempts to print a sensitive item that is open in the Firefox browser to a local or network printer | audit, block with override, block |
| file copied to clipboard | Detects when a user attempts to copy information from a sensitive item in the Firefox browser into another app, process, or item. | audit, block with override, block |
| file copied to removable storage | Detects when a user attempts to copy a sensitive item or information from a sensitive item in the Firefox browser to removable media or USB device | audit, block with override, block |
| file copied to network share | Detects when a user attempts to copy a sensitive item or information from the Firefox browser to a network share or mapped network drive. | audit, block with override, block |

## Deployment process

1. [Get started with endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)
2. [Onboarding tools and methods for Windows 10 devices](https://learn.microsoft.com/en-us/purview/device-onboarding-overview)
3. [Install the extension for Firefox extension on your Windows 10 devices](https://learn.microsoft.com/en-us/purview/dlp-firefox-extension-get-started)
4. [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) that restrict upload to cloud service, or access by unallowed browsers actions and apply them to your Windows 10 devices
