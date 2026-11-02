# Help protect files that Endpoint Data Loss Prevention fails to scan

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-edlp-scan-fails  
> Microsoft doc last updated: 2026-06-26


This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy that helps protect files on supported Windows and macOS devices where the scanning process fails. Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Note

Applying controls to supported files that fail scanning is currently in preview.

Use this scenario when you want to apply Audit, Block, or Block with override controls on user activities for files that are on the [Monitored files](https://learn.microsoft.com/en-us/en-us/purview/endpoint-dlp-learn-about) list but fail to be scanned by Endpoint DLP.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

This scenario requires that you already have devices onboarded and reporting into activity explorer. If you haven't onboarded devices yet, see [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started).

Important

This feature only supports following action types:

- Upload to a restricted cloud service domain
- Copy to a removable USB device
- Copy to a network share
- Print

## Policy intent statement and mapping

*Sometimes scanning fails for files that endpoint DLP supports. There might be sensitive information in those files, but we don't know. When scanning fails for a file on any of our onboarded devices, we want to prevent users from copying that file to a USB device or to a network share.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “When scanning fails for a file on any of our onboarded devices ...” | - Administrative scope: **Full directory**- Where to monitor: **Enteprise applications & devices**, **Devices**-Scope: **Allusers, groups, devices, device groups**- Conditions: **Document could not be scanned** |
| "...we want to prevent users from copying that file to a USB device or to a network share." | - Action : select **audit or restrict activities on devices**- clear **Upload to a restriced cloud service domain or access from an unallowed browser**- select **Apply restrictions to specific activity**- select **Copy to a removable USB device**, and **Block with override**- select **Copy to a network share** and **Block with override** clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP** |

When you configure the conditions, the summary looks like this:



## Steps to configure policy actions

Perform the following steps to configure the policy actions for this scenario.

Important

For the purposes of this policy creation procedure, leave the policy turned off. Change the policy activation settings when you deploy the policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data Loss Prevention** &gt; **Policies**.
3. Select **Create policy**.
4. Select **Enterprise applications & devices**.
5. Select the **Custom** from the **Categories** then **Custom policy** template from **Regulations**.
6. Name your new policy and provide a description.
7. Select **Full directory** under **Admin units**.
8. Scope the location to **Devices** only.
9. Create a rule where:
    1. In **Conditions**:
        1. Select **Document could not be scanned**
    2. In **Actions**:
        1. Select **Audit or restrict activities on devices**.
        2. Clear **Upload to a restriced cloud service domain or access from an unallowed browser**
        3. Select **Apply restrictions to specific activity**
        4. Select **Copy to a removable USB device**, and **Block with override**
        5. Select **Copy to a network share**, and **Block with override**
        6. Clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**
10. **Save**.
11. Choose **Turn on the policy immediately**. Choose **Next**.
12. Review your settings and choose **Submit**.
