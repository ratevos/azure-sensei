# Learn about the Microsoft Purview extension for Chrome

> Source: https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about  
> Microsoft doc last updated: 2025-03-18


[Endpoint data loss prevention (endpoint DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about) extends the activity monitoring and protection capabilities of [Microsoft Purview Data Loss Prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) to sensitive items on Windows 10/11 devices. Once you onboard devices into the Microsoft Purview solutions, information about what users are doing with sensitive items is made visible in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). Then you can enforce protective actions on those items using [data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp).

After you install the Microsoft Purview extension for Chrome on a Windows 10/11 device, your organization can monitor attempts to access or upload a sensitive item to a cloud service in Google Chrome, and enforce protective actions via DLP.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Activities you can monitor and take action on

The extension enables you to audit and manage the following types of activities users take on sensitive items on devices running Windows 10/11.

| activity | description | supported policy actions |
| --- | --- | --- |
| file copied to cloud | Detects when a user attempts to upload a sensitive item to a restricted service domain through the Chrome browser | audit, block with override, block |
| file printed | Detects when a user attempts to print a sensitive item from the Chrome browser to a local or network printer | audit, block with override, block |
| file copied to clipboard | Detects when a user attempts to copy & paste information from a sensitive item in the Chrome browser into another app, process, or item. | audit, block with override, block |
| file copied to removable storage | Detects when a user attempts to copy a sensitive item or information from the Chrome browser to removable media or USB device | audit, block with override, block |
| file copied to network share | Detects when a user attempts to copy a sensitive item or information from the Chrome browser to a network share or mapped network drive. | audit, block with override, block |

Note

Microsoft Purview Insider Risk Management requires that this extension be installed to monitor and take action on activities in the Chrome browser. For more information, see [Learn about and configure Insider Risk Management browser signal detection](https://learn.microsoft.com/en-us/purview/insider-risk-management-browser-support).

### Purview Chrome extension behavior

The DLPEngine caches all files for about 15 minutes by default to prevent repeated upload attempts. During the cache period, the file is blocked from being uploaded to any domain, so if you upload to an unallowed domain and then immediately to an allowed domain, the cached response may block the upload.

Tip

Microsoft recommends that you use Microsoft Edge if you need to upload files in quick succession.

## Deployment process

1. [Get started with endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)
2. [Onboarding tools and methods for Windows 10/11 devices](https://learn.microsoft.com/en-us/purview/device-onboarding-overview)
3. [Install the extension for Chrome on your Windows 10/11 devices](https://learn.microsoft.com/en-us/purview/dlp-chrome-get-started)
    Note

    Command access for the user is a prerequisite for the Microsoft Purview Extension extension for Chrome to work.
4. [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) that restrict upload to cloud service, or access by unallowed browsers actions and apply them to your Windows 10/11 devices
