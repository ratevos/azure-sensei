# Help prevent exposure of sensitive files by configuring auto-quarantine for OneDrive sync

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-auto-quarantine-for-onedrive  
> Microsoft doc last updated: 2026-06-26


This scenario shows how to configure Endpoint DLP to prevent synchronization of **Highly Confidential** files to cloud sync apps like OneDrive while avoiding repeated notifications. By using **auto‑quarantine** and restricted app controls, sensitive files are automatically moved to a secure location and replaced with a placeholder, enabling effective protection without creating a poor user experience from repeated sync attempts.

This scenario is for an unrestricted admin creating a full directory policy.

## Prerequisites and assumptions

This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

This scenario uses the *Confidential* sensitivity label, so it requires you to create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Human Resources* and a distribution group for the security team at Contoso.com.

This scenario uses alerts. For more information, see [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, want to prevent users from synchronizing highly sensitive files to cloud synchronization applications such as OneDrive from endpoint devices. In this scenario, files labeled **Highly Confidential** must not be synchronized to cloud storage through restricted sync apps.*

*At the same time, we want to avoid repeated DLP notifications and poor user experience caused by failed sync retries. To do that, we will use **Endpoint DLP auto-quarantine** so that when a restricted sync app attempts to process a protected file, the original file is automatically moved to a quarantine location and replaced with a placeholder text file. This both prevents exfiltration and stops the sync client from repeatedly retrying the same blocked file.*

*We also want users to be informed when the action is blocked, and we want administrators to be able to validate and investigate the resulting events through **Activity explorer**.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to prevent users from synchronizing files labeled Highly Confidential to cloud sync apps such as OneDrive…” | - Administrative scope: Full directory- Where to monitor: Devices- Policy scope: Devices only, with optional targeting to specific test users- Condition: Content contains the sensitivity label **Highly Confidential** |
| “We want to treat cloud synchronization apps as restricted applications for these sensitive files…” | - Endpoint settings: Create a restricted app group named **Cloud Sync apps**- Restricted apps include OneDrive executables for Windows and macOS- Restricted app group is referenced by the DLP rule |
| “We want to block restricted apps from performing file activities on these sensitive items…” | - Rule action: **Audit or restrict activities on devices**- Activity type: **File activities for apps in restricted app groups**- Restriction: **Apply a restriction to all activity &gt; Block** |
| “We want to avoid looping DLP notifications and repeated cloud sync retries for blocked sensitive files…” | - Endpoint DLP setting: Enable **Auto-quarantine for unallowed apps**- Quarantine behavior: Move the original file to a configured quarantine folder- File handling: Append date/time stamp to quarantined file name |
| “We want the user to understand what happened to the blocked file…” | - Auto-quarantine response: Replace the original file with a **.txt placeholder file** containing a custom message- Placeholder message includes tokens such as **%%FileName%%**, **%%PolicyName%%**, and **%%QuarantinePath%%** |
| “We want users to be notified in real time when the sync action is blocked…” | - User notifications: Turn **User notifications** On- Endpoint behavior: Show users a **policy tip notification** when the blocked activity occurs |
| “We want this protection to apply immediately once the rule is active…” | - Policy creation: Custom policy with advanced DLP rules- Deployment mode: **Turn it on right away** |
| “We want to validate that blocking, quarantine, and user messaging all work together correctly…” | - Test procedure: Create a Word document, apply the **Highly Confidential** label, and copy it into the local OneDrive sync folder- Expected outcome: User sees a notification toast, the source file is replaced by a placeholder text file, and the original file appears in the quarantine folder |
| “We want administrators to be able to review the enforcement event after testing…” | - Monitoring and investigation: Use **Activity explorer**- Filters: Set location to **Devices** and filter by the policy name to review the policy match and action outcome |

## Steps to create policy

Complete the following procedures to configure Endpoint DLP settings, create the policy, and test auto-quarantine.

### Before you begin

In this Endpoint DLP auto-quarantine scenario, synchronizing files with the **Highly Confidential** sensitivity label to OneDrive is blocked. This is a complex scenario with multiple components and procedures. You need:

- A Microsoft Entra user account to target and an onboarded Windows 10/11 or macOS computer that is already synchronizing a local OneDrive folder with OneDrive cloud storage.
- Sensitivity labels configured and published—see [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels#get-started-with-sensitivity-labels) and [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels#create-and-configure-sensitivity-labels-and-their-policies).

There are three procedures.

1. Configure the Endpoint DLP Autoquarantine settings.
2. Create a policy that blocks sensitive items that have the **Highly Confidential** sensitivity label.
3. Create a Word document on the Windows 10/11 or macOS device that the policy targets, apply the label, and copy the document to the user account's local OneDrive folder that is being synchronized.

### Configure Endpoint DLP unallowed app and Autoquarantine settings

Perform the following steps to create a restricted app group and configure auto-quarantine settings for cloud sync apps.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Settings** (gear in the upper left hand corner) &gt; **Data loss prevention** &gt; **Endpoint settings**.
2. Expand **Restricted apps and app groups**.
3. Under **Restricted app groups**, choose **Add restricted app group**. Enter *Cloud Sync apps* as the group name.
4. Select the **Auto-quarantine** box.
5. For the **App name**, enter *OneDrive*. For the Windows **Executable name**, enter *onedrive.exe*, then choose the **+** button. For the macOS **Executable name**, enter */Applications/OneDrive.app/Contents/MacOS/OneDrive*, then choose the **+** button. This disallows onedrive application on devices from accessing items with the **Highly Confidential** label.

    Note

    To restrict other common cloud sync app on macOS devices, add the below path

    - Box: `/Applications/Box Sync.app/Contents/MacOS/Box Sync`
    - Dropbox: `/Applications/Dropbox.app/Contents/MacOS/Dropbox`
    - Google Drive: `/Applications/Google Drive.app/Contents/MacOS/Google Drive`
    - iCloud: `System/Library/PrivateFrameworks/CloudDocsDaemon.framework/Versions/A/Support/bird`
6. Choose **Save**.
7. Under **Auto-quarantine settings** choose **Edit auto-quarantine settings**.
8. Enable **Auto-quarantine for unallowed apps**.
9. Enter the path to the folder on local machines where you want the original sensitive files to be moved to. For example:

> 
> `%homedrive%%homepath%\Microsoft DLP\Quarantine` for the username *Isaiah Langer* will place the moved items in a folder named:
> 
> *C:\Users\IsaiahLanger\Microsoft DLP\Quarantine\OneDrive*
> 
> A separate path for the macOS device is required, such as `/System/Applications/Microsoft DLP/Quarantine`

1. Append a date and time stamp to the original file name.

    Note

    DLP auto-quarantine will create sub-folders for the files for each unallowed app. So if you have both *Notepad* and *OneDrive* in your unallowed apps list, a sub-folder will be created for **\OneDrive** and another sub-folder for **\Notepad**.
2. Choose **Replace the files with a .txt file that contains the following text** and enter the text you want in the placeholder file. For example for a file named *auto quar 1.docx*, you could enter:

> 
> %%FileName%% contains sensitive info that your organization is protecting with the data loss prevention (DLP) policy %%PolicyName%%. The file was moved to the quarantine folder: %%QuarantinePath%%

    will leave a text file that contains this message:

> 
> auto quar 1.docx contains sensitive info that your organization is protecting with the data loss prevention (DLP) policy. It was moved to the quarantine folder: C:\Users\IsaiahLanger\Microsoft DLP\Quarantine\OneDrive\auto quar 1.docx.
3. Choose **Save**.

### Configure a policy to block OneDrive synchronization of files with the sensitivity label "Highly Confidential"

Use the following steps to create a DLP policy that blocks OneDrive synchronization for files labeled **Highly Confidential**.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Policies**.
2. Select **Create policy**.
3. **Data stored in connected sources**.
4. For this scenario, choose **Custom**, then **Custom policy**. Choose **Next**.
5. Fill in the **Name** and **Description** fields, choose **Next**.
6. Select **Full directory** under **Admin units**.
7. Toggle the **Status** field to off for all locations except **Devices**. If you have a specific end user account that you want to test this from, be sure to select it in the scope. Choose **Next**.
8. Accept the default **Create or customize advanced DLP rules** selection and choose **Next**.
9. Create a rule with these values:

    1. **Name** &gt; *Scenario 4 Autoquarantine*.
    2. Under **Conditions** choose **Add condition** and then **Content Contains**.
    3. Enter a group name, for example *Highly Confidential Sensitivity Labels* and then choose **Add**.
    4. Select **Sensitivity labels** then **Highly Confidential** and choose **Add**.
    5. Under **Actions** choose **Add an action**.
    6. Select **Audit or restrict activities on devices** &gt; **File activities for apps in restricted app groups**.
    7. Choose **Add restricted app group** then choose the *Cloud Sync Apps* group you created previously.
    8. Choose **Apply a restriction to all activity** &gt; **Block**. For the purposes of this scenario, clear all the other activities.
    9. Under **User notifications**, toggle **User notifications** to **On** and under **Endpoint devices** choose **Show users a policy tip notification when an activity** if not already enabled.
10. Choose **Save** and **Next**.
11. Choose **Turn it on right away**. Choose **Next**.
12. Review your settings and choose **Submit**.

    Note

    Allow at least an hour for the new policy to be replicated and applied to the target Windows 10 computer.
13. The new DLP policy appears in the policy list.

### Test Autoquarantine on the Windows 10/11 device

Perform the following steps to verify that auto-quarantine blocks the sync attempt and replaces the file with a placeholder. Before testing, wait at least an hour for the new policy to replicate and apply to the target device.

1. Sign in to the Windows 10/11 computer with the user account you included in the **Devices** scope for the policy.
2. Create a folder whose contents won't be synchronized to OneDrive. For example:

> 
> *C:\auto-quarantine source folder*
3. Open Microsoft Word and create a file in the autoquarantine source folder. Apply the **Highly confidential** sensitivity label; see [Apply sensitivity labels to your files and email in Office](https://support.microsoft.com/topic/apply-sensitivity-labels-to-your-files-and-email-in-office-2f96e7cd-d5a4-403b-8bd7-4cc636bae0f9).
4. Copy the file you created to your OneDrive synchronization folder. A user notification toast should appear telling you that the action isn't allowed and that the file will be quarantined. For example, for user name *Isaiah Langer*, and a document titled *autoquarantine doc 1.docx* you would see this message:

    

    The message reads:

> 
> Opening auto-quarantine doc 1.docx with this app is not allowed. The file will be quarantined to *C:\Users\IsaiahLanger\Microsoft DLP\OneDrive*
5. Choose **Dismiss**.
6. Open the place holder text file. It is named **auto-quarantine doc 1.docx\_*date\_time*.txt**.
7. Open the quarantine folder and confirm that the original file is there.
8. Check Activity explorer for data from the monitored endpoints. Set the location filter for devices and add the policy, then filter by policy name to see the effect of the *Scenario 4 Autoquarantine* policy. For information on using activity explorer, see [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer).
9. Check Activity explorer for the event.
