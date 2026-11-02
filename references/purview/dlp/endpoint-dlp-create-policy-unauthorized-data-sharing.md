# Help prevent unauthorized sensitive data sharing with block actions and allow overrides

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-unauthorized-data-sharing  
> Microsoft doc last updated: 2026-06-26


This scenario demonstrates how to transition an existing Microsoft Purview DLP policy from monitoring to enforcement by blocking the sharing of sensitive U.S. PII data. The policy is updated to use **block with override**, preventing high-risk actions while still allowing users to proceed when justified.

This approach strengthens data protection by reducing the risk of data exfiltration, while maintaining business continuity through controlled user overrides and continued visibility into user activity via Activity explorer.

This scenario is for an unrestricted admin modifying a full directory policy.

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

This procedure generates data loss prevention alerts when policy rules are triggered. To learn how to configure and review these alerts, see [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started).

## Policy intent statement and mapping

*We, Contoso, have already deployed and tuned a policy that detects U.S. Personally Identifiable Information (PII) on endpoint devices and provides visibility and alerting. After validating the policy behavior, we now want to move to enforcement by preventing users from sharing sensitive information outside the organization.*

*To achieve this, we will modify the existing policy so that when PII is detected in user actions involving service domains or browsers, the action is blocked. However, to maintain business flexibility, users will be allowed to override the block with justification.*

This ensures strong data protection while still enabling users to proceed in legitimate business scenarios when necessary.

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to transition from monitoring to enforcing protection of U.S. PII on endpoint devices…” | - Administrative scope: Full directory (unchanged)- Where to monitor: Devices (unchanged)- Existing policy reused and updated for enforcement |
| “We want to prevent users from sharing sensitive data outside the organization…” | - Actions: Audit or restrict activities on Windows devices- Activity types: Service domain and browser activities |
| “We want to block high-risk actions involving sensitive data…” | - Action configuration: Block with override enabled for service domain and browser activities |
| “We want to allow users to proceed in legitimate cases with accountability…” | - Override behavior: Allow override with user justification captured- User interaction: Prompt displayed on endpoint when action is blocked |
| “We want consistent enforcement across different sensitivity levels…” | - Rule coverage: Apply same block with override settings to both low-volume and high-volume detection rules |
| “We want to maintain visibility into enforcement events and user behavior…” | - Monitoring: Activity explorer logs blocked and overridden events- Alerts/events: Captured for investigation and auditing |
| “We want to validate enforcement behavior through testing…” | - Testing: Trigger policy using test file containing PII data and attempt external sharing- Expected result: User receives block prompt with override option |

## Steps to create policy

Perform the following steps to edit the existing policy and enable block with override behavior.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Policies**.
2. Choose your existing **U.S. Personally Identifiable Information (PII) Data** policy that you previously created for monitoring on endpoint devices.
3. Choose **Edit policy**.
4. Go to the **Customize advanced DLP rules** page and edit the **Low volume of content detected scenarios U.S. PII Data Enhanced**.
5. Scroll down to the **Actions** &gt; **Audit or restrict activities on Windows device** section and set both options under the **Service domain and browser activities** to **Block with override**.

    
6. Choose **Save**.
7. Edit the **High volume of content detected scenarios U.S. PII Data Enhanced** rule. Scroll down to **Actions** &gt; **Audit or restrict activities on Windows device**, set both options under **Service domain and browser activities** to **Block with override**, and then choose **Save**.
8. Leave all other existing policy settings unchanged by choosing **Next** through the rest of the wizard, and then select **Submit** to apply the policy changes.
9. Attempt to share a test item that contains content that will trigger the U.S. Personally Identifiable Information (PII) Data condition with someone outside your organization. This sharing attempt should trigger the policy.

    You see a popup like this on the client device:

    
10. Check Activity explorer for the blocked or overridden sharing event generated by the test action.
