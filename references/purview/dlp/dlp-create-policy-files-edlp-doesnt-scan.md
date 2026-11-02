# Help protect files that Endpoint Data Loss Prevention doesn't scan

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-files-edlp-doesnt-scan  
> Microsoft doc last updated: 2026-06-26


This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy that helps protect files that Endpoint DLP doesn't support. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Apply controls to all unsupported files, is in *preview*.

Use the "Apply controls to all unsupported files" scenario to apply Audit, Block, or Block with override controls on user activities for files that aren't on the [Monitored files](https://learn.microsoft.com/en-us/en-us/purview/endpoint-dlp-learn-about) list without enumerating all the file extensions through the **File extension is** condition. Use the **Apply restrictions to only unsupported file extensions** configuration to create a blanket policy to place controls on files like .mp3, .wav, and .dat.

Caution

The ability to apply controls to all files is a powerful capability. If you implement this capability without proper caution, the policy might have unintended consequences. Test this policy in a nonproduction environment before deploying it to your production environment. The unsupported-files policy example also shows how you can (optionally) exclude specific file extensions from the scope of the policy.

Important

When you select the **Audit or restrict activities on devices** action in the policy configuration **Actions**, the **Apply restrictions to only unsupported file extensions** shows up. **Apply restrictions to only unsupported file extensions** configuration option ***DOES NOT*** support scoping by **Device and device groups** in the policy location setting.

These actions are supported:

- Upload to a restricted cloud service domain
- Copy to a removable USB device
- Copy to a network share
- Print

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Policy intent statement and mapping

*There are many types of files that endpoint DLP doesn't scan, more than we can track. We don't know if there is sensitive information in those files, and so we want to have a checkpoint in place before our user try to copy those files to a USB device or to a network share. We don't want to disrupt users workflow for the **abc** file type which is well known to us and poses no threat of data leakage.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “There are many types of files that endpoint DLP doesn't scan,...” | - Administrative scope: **Full directory**- Where to monitor: **Enterprise applications & devices**, **Devices**- Scope: **Allusers, groups, devices, device groups** |
| "...We don't want to disrupt users workflow for the **abc** file type which is well known to us and poses no threat of data leakage." | - Endpoint settings: create a Unsupported file extension exclusions list and add the file extension **abc** to the list. |
| "...more than we can track. We don't know if there is sensitive information in those files, and so we want to have a checkpoint in place before they try to copy those files to a USB device or to a network share..." | - Conditions for a match: **Document could not be scanned** action : select **audit or restrict activities on devices**- clear **Upload to a restriced cloud service domain or access from an unallowed browser**- select **Apply restrictions to specific activity**- select **Copy to a removable USB device**, and **Block with override**- select **Copy to a network share and Block with override**- clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**- select **file could not be scanned**. - select **apply restrictions to only unsupported file extensions**. |

Important

The difference between the **Apply restrictions to only unsupported file extensions** option and the **File extension is** condition is:

- Endpoint DLP scans content for **File extension is** condition. For example, you see **Sensitive info type** value on the event or alert; on the other hand, the **Apply restrictions to only unsupported file extensions** option doesn't scan file content.
- **File extension is** condition triggering content scanning might consume higher machine resource, like CPU and memory, and might cause application performance issue for some file types.

## Steps to add a file type to unsupported file extension exclusions

Use the **Unsupported file extension exclusions** setting to exclude file extensions from the policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com)
2. Open **Settings** &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Unsupported file extension exclusions**.
3. Select **Add file extensions**.
4. Provide extensions.
5. Select **Save**.
6. Close the item.

## Steps to configure policy actions

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data Loss Prevention** &gt; **Policies**.
3. Select **Enterprise applications & devices**.
4. Select **Create policy** and select the **Custom** from the **Categories** then **Custom policy** template from **Regulations**.
5. Name your new policy and provide a description.
6. Select **Full directory** under **Admin units**.
7. Scope the location to **Devices** only.
8. Create a rule where:
    1. In **Conditions**:
        1. Select **Document could not be scanned**.
    2. In **Actions**:
        1. Select **Audit or restrict activities on devices**.
        2. Clear **Upload to a restriced cloud service domain or access from an unallowed browser**.
        3. Select **Apply restrictions to specific activity**.
        4. Select **Copy to a removable USB device**, and **Block with override**.
        5. Select **Copy to a network share**, and **Block with override**.
        6. Clear **Copy to clipboard**, **Print**, **Copy or move using unallowed Bluetooth app**, and **Copy or move using RDP**.
        7. Select **Apply restrictions to only unsupported file extensions**.
9. **Save**.
10. Choose **Turn on the policy immediately**. Choose **Next**.
11. Review your settings and choose **Submit**.

Important

You can't use **Document could not be scanned** together with other conditions in the "Apply controls to all unsupported files" scenario.
