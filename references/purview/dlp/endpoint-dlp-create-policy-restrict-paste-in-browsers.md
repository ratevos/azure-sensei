# Help prevent leakage of sensitive content by restricting paste actions into browsers

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-paste-in-browsers  
> Microsoft doc last updated: 2026-06-26


This scenario demonstrates how to restrict users from pasting sensitive content into browser-based applications using Microsoft Purview DLP. By evaluating content at the moment it is pasted, organizations can detect and control sensitive information in real time, regardless of where the content originated.

Using **Paste to browser** controls with **Sensitive service domain groups**, this approach enables flexible enforcement—such as auditing, warning, or blocking paste actions—based on the destination website. This approach helps reduce the risk of accidental data exposure while allowing policies to be tailored for different levels of risk.

The **Paste to browser** activity operates independently of the source file’s classification and requires rules configured with **Sensitive service domain groups**. It is not supported with the **Service domains** endpoint DLP setting. For more information, see [Endpoint activities you can monitor and take action on](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on)

Note

The following web browsers are supported:

- Microsoft Edge (Win/macOS)
- Chrome (Win/macOS)- Microsoft Purview extension for Chrome Windows only
- Firefox (Win/macOS)- Microsoft Purview extension for Firefox Windows only
- Safari (macOS only)

Important

- If you have configured [evidence collection for file activities on devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-learn#learn-about-evidence-collection-for-file-activities-on-devices) and your Antimalware Client Version on the device is older than 4.18.23110, when you implement this scenario, *Restrict pasting sensitive content into a browser*, you will see random characters when you attempt to view the source file in Alert details. To see the actual source file text, you should download the file.
- If **Document could not be scanned** is selected as the action for the matched rule, the evidence file will not be captured.

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

The policy configuration procedure uses alerts, see: [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, want to prevent users from unintentionally exposing sensitive information by pasting it into web forms or browser-based applications. Sensitive data—such as personally identifiable information or other regulated content—can be copied from local files or applications and pasted into websites, creating a potential data exfiltration risk.*

*To address this, we will create a policy that evaluates content dynamically at the moment it is pasted into a supported browser. Based on the sensitivity of the pasted content and the destination website, we will audit, warn, or block the action. We will also use **Sensitive service domain groups** to apply different levels of enforcement depending on the target websites. This allows us to balance security and usability by applying stricter controls to higher-risk domains while allowing flexibility for trusted sites.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to prevent sensitive data from being pasted into web forms or browser fields…” | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/devices or targeted users |
| “We want to evaluate content at the time it is pasted, regardless of its source…” | - Condition: Content contains selected **Sensitive info types**- Evaluation: Real-time classification at paste event (independent of source file classification) |
| “We want to control paste actions based on the sensitivity of the content…” | - Action: **Audit or restrict activities on devices**- Activity type: **Paste to supported browsers** |
| “We want different levels of enforcement depending on the destination website…” | - Endpoint settings: Create **Sensitive service domain groups**- Rule design: Associate paste restrictions with specific domain groups |
| “We want to audit, warn, or block paste actions based on risk level…” | - Action configuration: Set to **Audit**, **Block with override**, or **Block** depending on enforcement needs |
| “We want flexibility to tailor restrictions across different categories of websites…” | - Policy design: Multiple URL/domain groups (e.g., trusted vs untrusted sites)- Use exceptions or multiple rules for granular control |
| “We want to ensure enforcement occurs consistently across supported browsers…” | - Browser support: Microsoft Edge, Chrome, Firefox (with extensions), Safari- Endpoint DLP integration ensures policy enforcement in supported browsers |
| “We want users to be informed when paste actions are evaluated or restricted…” | - User experience: Policy tips or notifications triggered during paste evaluation- Behavior note: Possible brief delay while classification completes |
| “We want to deploy and test the policy with appropriate enforcement level…” | - Policy mode: Configurable (test, audit, or enforce)- Deployment: Submit policy and validate behavior with test scenarios |

## Steps to create policy

You can set up different levels of enforcement when it comes to blocking data from being pasted into a browser. To do this, create different URL groups. For instance, you can create a policy that warns users against posting U.S. Social Security Numbers (SSN) to any website, and that triggers an audit action for websites in Group A. You can create another policy that completely blocks the paste action--without giving a warning--for all of the websites in Group B.

### Create a URL group

Perform the following steps to create a sensitive service domain group for browser paste restrictions.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Settings** (gear icon in the upper left hand corner) &gt; **Data Loss Prevention** &gt; **Endpoint settings**, and scroll down to **Browser and domain restrictions to sensitive data**. Expand the section.
2. Scroll down to **Sensitive service domain groups**.
3. Choose **Create sensitive service domain group**.

    1. Enter a **Group name**.
    2. In the **Sensitive service domain** field, enter the URL for the first website you want to monitor and then choose **Add site**.
    3. Continue adding URLs for the rest of the websites you want to monitor in this group.
    4. When you are finished adding all URLs to your group, choose **Save**.
4. Create as many separate groups of URLs as you need.

### Restrict pasting content into a browser

Use the following steps to create a DLP policy that restricts pasting sensitive content into a browser.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Policies**.
2. Under **Data stored in connected sources**, select **Devices**.
3. Create a DLP policy scoped to **Devices**. For information on how to create a DLP policy, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#create-and-deploy-data-loss-prevention-policies).
4. On the [Define policy settings page](https://sip.compliance.microsoft.com/datalossprevention/policies) in the DLP policy creation flow, select **Create or customize advanced DLP rules** and then choose **Next**.
5. On the **Customize advanced DLP rules** page, choose **Create rule**.
6. Enter a name and description for the rule.
7. Expand **Conditions**, choose **Add condition**, and then select the **Sensitive info types**.
8. Under **Content Contains**, scroll down and select the new sensitive information type that you previously chose or created.
9. Scroll down to the **Actions** section, and choose **Add an action**.
10. Choose **Audit or restrict activities on devices**
11. In the **Actions** section, under **Service domain and browser activities**, select **Paste to supported browsers**.
12. Set the restriction to **Audit**, **Block with override**, or **Block**, and then choose **Add**.
13. Choose **Save**.
14. Choose **Next**
15. Choose whether you want to test your policy, turn it on right away, or keep it off, and then choose **Next**.
16. Choose **Submit**.

Important

There may be a brief time lag between when the user attempts to paste text into a web page and when the system finishes classifying it and responds. If this classification latency happens, you may see both policy-evaluation and check-complete notifications in Edge or policy-evaluation toast on Chrome and Firefox. Here are some tips for minimizing the number of notifications:

1. Notifications are triggered when policy for the target website is configured to **Block** or **Block with override** paste to browser for that user. You can configure setting the overall action to **Audit** and then list the target websites using the exceptions as **Block**. Alternately, you can set the overall action to **Block** and then list secure websites using the exceptions as **Audit**.
2. Use latest Antimalware client version.
3. Use latest Edge browser version, especially Edge 120.
4. Install these Windows KBs

- Windows 10: [KB5032278](https://support.microsoft.com/en-us/topic/november-30-2023-kb5032278-os-build-19045-3758-preview-0ae14f06-577e-4eb3-8fcb-c722f3f9dc29)
- Windows 11: [KB5032288](https://support.microsoft.com/en-us/topic/december-4-2023-kb5032288-os-builds-22621-2792-and-22631-2792-preview-538fbe4a-e9de-4312-85cd-d870444341d0)
