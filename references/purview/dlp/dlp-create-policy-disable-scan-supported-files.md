# Disable Purview Data Loss Prevention scanning for some supported files and apply controls

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-disable-scan-supported-files  
> Microsoft doc last updated: 2026-06-26


This article shows you how to create a Microsoft Purview data loss prevention (DLP) policy that disables scanning for selected supported file types and applies audit or restriction controls to those files, using the process described in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy). Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Disable scanning for some supported files and apply controls is in *preview*.

Use the disable-classification configuration to save local resource consumption by disabling scanning of some file types on the [Monitored files](https://learn.microsoft.com/en-us/en-us/purview/endpoint-dlp-learn-about) list. You can apply Audit, Block, or Block with override controls to those file types.

Important

This feature only supports the following action types:

- Upload to a restricted cloud service domain
- Copy to a removable USB device
- Copy to a network share
- Print

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Policy intent statement and mapping

*Bellows College needs to conserve resources on all our users Windows devices and cutting down on the scanning of files by DLP would be a big help. We have a list of file types that we know the contents of because they are auto generated. These file types are on the supported file types list. There's no need to scan these auto generated files, but we do want to prevent users from copying them to a USB device or to a network share. When they do try, we want to let them know, to educate them, that they are attempting a prohibited action.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “Bellows College needs to conserve resources on all our users Windows devices and cutting down on the scanning of files by DLP would be a big help...” | - Administrative scope: **Full directory**- Where to monitor: **Enterprise applications & devices**, **Devices**-Scope: **Allusers, groups, devices, device groups** |
| "...We have a list of file types that we know the contents of because they are auto generated. These file types are on the supported file types list. There's no need to scan these auto generated files..." | - Endpoint settings: create a **File extension group**- Disable classification |
| ...but we do want to prevent users from copying them to a USB device or to a network share... | - Conditions for a match: **Document could not be scanned** Action : select **audit or restrict activities on devices**- clear **Upload to a restriced cloud service domain or access from an unallowed browser**- select **Apply restrictions to specific activity**- select **Copy to a removable USB device**, &gt; **Block**- **Copy to a network share** &gt; **Block**- clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**- select **file could not be scanned**. |
| "...When they do try, we want to let them know, to educate them, that they are attempting a prohibited action..." | - Use notifications to inform your users and help educate them on the proper use of sensitive info: **On**- Endpoint devices &gt; Show users a policy tip notification when an activity is restricted...: **selected**- Customize the notification: **selected** &gt; **Notication Title**: Bellows College IT don't copy files &gt; **Notification Content**: FYI, Bellows College data loss prevention policies don't let you copy that type of file to USB device or a network share |

## Create a File extension group

Select the appropriate tab for the portal you're using. To learn more about the Microsoft Purview portal, see [Microsoft Purview portal](https://learn.microsoft.com/en-us/en-us/purview/purview-portal).

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Settings** &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **File extension groups**.
3. Select **Create file extension group** and enter a **Group name**. In this scenario, we use `Student Class Registration file extensions`.
4. Enter the extensions.
5. Select **Save**.
6. Close the item.

## Disable classification

Use the **Disable classification** setting to exclude specific file extensions from Endpoint DLP classification.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Settings** &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Disable classification**.
3. Select **Add or edit file extensions**.
4. Enter the extensions.
5. Select **Save**.
6. Close the item.

## Configure policy actions

Perform the following steps to configure the policy actions for this scenario.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data Loss Prevention** &gt; **Policies**.
3. Select **Create policy**.
4. Select **Enterprise applications & devices**.
5. Select **Custom** from the **Categories** then select **Custom policy** template from **Regulations**.
6. Name your new policy and provide a description.
7. Select **Full directory** under **Admin units**.
8. Scope the location to **Devices** only.
9. Create a rule where:
    1. In **Conditions**:
        1. **Document could not be scanned**.
    2. In **Actions**:
        1. Select: **Audit or restrict activities on devices**.
        2. Select: **Apply restrictions to specific activity**.
        3. Clear: **Copy to clipboard**.
        4. Select: **Copy to a removable USB device** &gt; **Block**.
        5. Select: **Copy to a network share** &gt; **Block**.
        6. Clear: **Print**.
        7. Clear: **Copy or move using unallowed Bluetooth app**.
        8. Clear: **Copy or move using RDP**.
        9. Clear: **Access by restricted apps**.
        10. Select: **Apply restrictions to only unsupported file extensions**.
        11. Select: **Add file extension group** and select `Student Class Registration file extensions`.
    3. **Save**.
10. Choose **Turn it on right away**. Choose **Next**.
11. Review your settings and choose **Submit**.

Important

You can't use the **Document could not be scanned** condition with other conditions in this policy scenario.
