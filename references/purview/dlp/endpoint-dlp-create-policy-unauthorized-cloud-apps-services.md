# Help prevent sharing of sensitive items with unauthorized cloud apps and services

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-unauthorized-cloud-apps-services  
> Microsoft doc last updated: 2026-06-26


This scenario demonstrates how to restrict unintentional sharing of sensitive information to unapproved cloud applications and services using Microsoft Purview DLP. By defining **sensitive service domains** and enforcing controls through supported browsers, organizations can monitor and guide how sensitive data is uploaded or accessed.

Note

The following web browsers are supported:

- Microsoft Edge (Win/macOS)
- Chrome (Win/macOS)- Microsoft Purview extension for Chrome Windows only
- Firefox (Win/macOS)- Microsoft Purview extension for Firefox Windows only
- Safari (macOS only)

When a policy is configured for the **Devices** location, unsupported browsers are prevented from accessing sensitive content, and users are redirected to Microsoft Edge, where DLP controls can block or restrict actions based on policy conditions. This browser-aware enforcement helps reduce the risk of data exfiltration while maintaining a consistent and guided user experience.

To implement this approach, you define restricted destinations (domains, services, or IPs), specify unsupported browsers, and configure DLP rules that detect sensitive content and apply controls such as **Upload to cloud services** and **Access from unallowed browser**.

The sensitive service domain and browser-restriction configuration enables organizations to audit user behavior, refine policies, and progressively enforce stricter controls as needed, while minimizing disruption to legitimate business activities.

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

The policy-creation procedure in this article uses alerts. For more information, see [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, want to prevent users from unintentionally sharing sensitive information to unapproved cloud applications and services from endpoint devices. At the same time, we want to ensure users can continue to access and work with non-sensitive data without unnecessary restrictions.*

*To achieve this, we will define a set of **restricted cloud service domains** and enforce controls when sensitive information is detected in user activity. When users attempt to upload sensitive content to these unapproved services—or access such content through unsupported browsers—we will audit the activity and guide users toward supported, compliant workflows (such as using Microsoft Edge).*

Using restricted cloud service domains with audit-first enforcement allows us to gradually enforce controls by first auditing user behavior, understanding risk patterns, and refining the policy before moving to stricter enforcement if needed.

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to prevent users from sharing sensitive information to unapproved cloud apps and services…” | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/devices (or targeted users for testing) |
| “We want to define which cloud services are considered unallowed for sensitive data sharing…” | - Endpoint settings: Create **Sensitive service domain group**- Domains defined using URL/IP/IP range (with wildcard support)- Group reused in policy rules |
| “We want to detect sensitive content being shared to these services…” | - Conditions: Content contains selected **Sensitive info types**- Detection logic: Built-in or custom sensitive information types |
| “We want to monitor attempts to upload sensitive content or access it through unsupported browsers…” | - Actions: **Upload to a restricted cloud service domain or access from an unallowed browser**- Browser control integrated with Endpoint DLP |
| “We want to initially observe user behavior without blocking business processes…” | - Action mode: **Audit only** for service domain and browser activities- No blocking or override enforced at this stage |
| “We want to redirect users toward supported, policy-aware browsers…” | - Endpoint behavior: Unallowed browsers are prevented from accessing sensitive content- User experience: Redirection to Microsoft Edge where DLP controls are enforced |
| “We want to maintain flexibility to extend protections over time…” | - Design capability: Add more domain groups, apps, and policies as needed- Policy extensibility: Supports future transition to block or block with override |
| “We want to monitor and optionally control other file activities across apps…” | - Additional actions: Configure **File activities for all apps** as needed- Fine-grained monitoring or restriction of endpoint behaviors |
| “We want this policy to be active immediately for evaluation…” | - Policy mode: **Turn it on right away**- Deployment: Immediate enforcement in audit mode |

## Steps to create policy

Perform the following steps to create the sensitive service domain group and configure the DLP policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Settings** (gear icon in the upper left hand corner) &gt; **Data Loss Prevention** &gt; **Endpoint DLP settings** &gt; **Browser and domain restrictions to sensitive data** &gt; **Sensitive service domain groups**.
2. Select **Create sensitive service domain group**.
3. Name the group.
4. Enter the **Sensitive service domain** for the group. You can add multiple websites to a group and use wildcards to cover subdomains. For example, `www.contoso.com` for just the top level website, or: \*.contoso.com for corp.contoso.com, hr.contoso.com, fin.contoso.com.
5. Select the **Match type** you want. You can select from **URL**, **IP address**, **IP address range**.
6. Select **Save**.
7. In the left navigation pane, select **Data loss prevention** &gt; **Policies**.
8. On the **Choose locations to apply the policy** page, select **Data stored in connected sources** and then choose **Next**.
9. Create and scope a policy that is applied only to the **Devices** location. For more information on how to create a policy, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy). Be sure to scope the **Admin units** to **Full directory**.
10. On the **Define policy settings** page, select **Create or customize advanced DLP rules** and choose **Next**.
11. Create a rule, as follows:

    1. Under **Conditions**, select **+ Add condition** and select **Content contains** from the drop-down menu.
    2. Give the group a name.
    3. Choose **Add** and then select **Sensitive info types**.
    4. Select a **Sensitive info type** from the flyout pane, then choose **Add**.
    5. Add the action **Audit or restrict activities on devices**.
    6. Under **Service domain and browser activities**, choose **Upload to a restricted cloud service domain or access from an unallowed browser** and set the action to **Audit only**.
    7. Select **+ Choose different restrictions for sensitive service domains** and then choose **Add group**.
    8. On **the Choose sensitive service domain groups** flyout, select the sensitive service domain group(s) you want, choose **Add** and then choose **Save**.
    9. Under **File activities for all apps**, select the user activities you want to monitor or restrict and the actions for DLP to take in response to those activities.
    10. Finish creating the rule and choose **Save** and then **Next**.
    11. On the confirmation page, choose **Done**.
    12. On the **Policy mode** page, choose **Turn it on right away**. Choose **Next** and then **Submit**.
