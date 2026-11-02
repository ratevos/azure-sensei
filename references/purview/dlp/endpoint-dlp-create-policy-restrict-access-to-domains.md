# Help prevent risky user activity by monitoring or restricting access to sensitive service domains

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-access-to-domains  
> Microsoft doc last updated: 2026-06-26


## Overview

This scenario demonstrates how to monitor and control user interactions with sensitive websites using Microsoft Purview DLP. By defining **sensitive service domains**, organizations can audit or restrict actions such as copying, printing, or saving web content when users access these sites.

Policy enforcement occurs in a supported, DLP-aware browser environment, ensuring consistent control and user guidance. This enables organizations to protect sensitive data accessed through web applications while maintaining flexibility to tailor controls based on business needs.

Note

The following web browsers are supported:

- Microsoft Edge (Win/macOS)
- Chrome (Win/macOS)- Microsoft Purview extension for Chrome Windows only
- Firefox (Win/macOS)- Microsoft Purview extension for Firefox Windows only
- Safari (macOS only)

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

The policy configuration in this article uses alerts. To learn more, see [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, want to monitor and control how users interact with sensitive websites to reduce the risk of data exposure through browser-based activities. Specifically, we want to audit or restrict actions such as copying data, printing content, or saving web pages locally when users access designated sensitive service domains.*

*To achieve this, we will define a set of **sensitive service domains** and configure a policy that detects when users access these sites through supported browsers. When a match occurs, we will apply activity-specific controls—such as auditing or blocking printing, copying, or file-saving actions—while ensuring users are redirected to supported browsers (such as Microsoft Edge) where these controls can be enforced consistently.*

This approach enables granular control of in-browser data handling for sensitive sites, helping protect organizational data while maintaining flexibility in how policies are applied and tuned over time.

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to monitor and control user interactions with designated sensitive websites…” | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/devices (or scoped test users) |
| “We want to define which websites are considered sensitive for monitoring or restriction…” | - Endpoint settings: Configure **Service domains** and **Sensitive service domain groups**- Domains defined using URL/IP/IP range with wildcard support |
| “We want to detect when users access these sensitive sites in supported browsers…” | - Condition: **User accessed a sensitive site from Edge**- Browser coverage: Supported browsers with Microsoft Purview extensions where applicable |
| “We want to ensure policy enforcement occurs in a DLP-aware browser…” | - Browser handling: Redirect unsupported browsers (e.g., Chrome/Firefox) to **Microsoft Edge** when accessing sensitive domains |
| “We want to audit or restrict specific user activities performed on sensitive websites…” | - Actions: **Audit or restrict activities when users access sensitive sites**- Activity controls include: copy, print, save as local files |
| “We want fine-grained control over which activities are monitored or blocked…” | - Action configuration: Select individual user activities (copy, print, save)- Choose audit, block, or block with override depending on requirement |
| “We want to flexibly apply controls across different sets of sensitive domains…” | - Rule configuration: Assign one or more **Sensitive service domain groups**- Reusable group design for scalability |
| “We want to finalize and deploy the policy for immediate use…” | - Policy mode: Submit and enable policy- Deployment: Active policy with configured monitoring/restriction behavior |

## Steps to create the sensitive service domains policy

Perform the following steps to configure sensitive service domains and create the DLP policy.

### Configure Sensitive service domains

Use the following steps to define sensitive service domains and create a DLP policy that monitors or restricts user activity on those domains.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Settings** (gear icon in the upper left hand corner) &gt; **Data Loss Prevention** &gt; **Endpoint settings** &gt; **Browser and domain restrictions to sensitive data** &gt; **Service domains**.
2. Set **Service domains** to **Block**.
3. To control whether sensitive files can be uploaded to specific domains, select **Add cloud service domain**.
4. Enter the domain that you want to audit or block and choose the **+** button. Repeat for any additional domains. Choose **Save**.
5. Under **Sensitive service domain groups**, choose **Create sensitive service domain group**.
6. Give the group a name, select the **Match type** you want (you can select from **URL**, **IP address**, **IP address range**), and enter the URL, IP address, or IP address range to be audited or blocked. When matching a URL, you can add multiple websites to a group and use wildcards to cover subdomains. For example, `www.contoso.com` for just the top level website or \*.contoso.com for corp.contoso.com, hr.contoso.com, fin.contoso.com.
7. Select **Save**.
8. In the left navigation pane, select **Data loss prevention** &gt; **Policies**.
9. On the policy template page, select **Data stored in connected sources**.
10. Create and scope a policy that is applied only to the **Devices** location. For detailed steps on scoping a policy to the Devices location, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#define-policy-scope). Be sure to scope the **Admin units** to **Full directory**.
11. Create a rule that uses the condition **the user accessed a sensitive site from Edge**, and the action **Audit or restrict activities when users access sensitive sites in Microsoft Edge browser on Windows devices**.
12. In the action, under **Sensitive Site Restrictions**, select **Add or remove Sensitive site groups**.
13. Create and/or select the **Sensitive site groups** you want. Any website under the group(s) you select here will be redirected to Microsoft Edge when opened in Chrome or Firefox (so long as the Microsoft Purview extension is installed).
14. Select **Add**.
15. Select the user activities you want to monitor or restrict and the actions you want Microsoft Purview to take in response to those activities.
16. Finish configuring the rule and policy and choose **Submit** and then **Done**.
