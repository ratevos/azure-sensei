# Create policy to detect and alert on U.S. PII data exposure

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-detect-pii-data-exposure  
> Microsoft doc last updated: 2026-06-26


This scenario shows how to enhance an existing Microsoft Purview DLP policy by enabling **real-time alerting** for policy matches involving U.S. PII data. Alerts are configured to notify administrators each time a match occurs, improving visibility and response readiness while the policy continues to run without restricting user activity.

This scenario is for an unrestricted admin modifying a full directory scoped policy.

## Prerequisites and assumptions

This article applies the policy design process from [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to modify an existing Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

This scenario uses the *Confidential* sensitivity label, so it requires you to create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Human Resources* and a distribution group for the security team at Contoso.com.

This procedure uses alerts, see: [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, have already deployed a policy to monitor U.S. Personally Identifiable Information (PII) activity on endpoint devices in audit mode. After reviewing initial results, we now want to enhance our visibility by ensuring that administrators are proactively notified when policy matches occur.*

*To achieve this, we will modify the existing policy to generate alerts whenever low-volume PII-related activity is detected. These alerts will be sent in real time to administrators so they can quickly review and respond to potential risks. The policy will continue to operate without restricting user activity, maintaining the audit-first approach while improving incident awareness and response readiness.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to enhance our existing monitoring policy without changing its scope…” | - Administrative scope: Full directory (unchanged)- Where to monitor: Devices (unchanged)- Existing policy reused and edited |
| “We want to generate alerts when U.S. PII policy conditions are matched…” | - Rule edited: Low volume of content detected scenarios U.S. PII Data Enhanced- Condition: Existing PII detection logic from template retained |
| “We want administrators to be notified automatically when matches occur…” | - Incident reports: Enable ‘Send an alert to admins when a rule match occurs’- Recipients: Default admin and additional configured recipients |
| “We want immediate visibility into every matching event…” | - Alert frequency: Send alert every time an activity matches the rule |
| “We want to improve response readiness without disrupting users…” | - Protection actions: No blocking or restriction changes- Policy continues in audit/simulation behavior |
| “We want to validate alerting behavior alongside activity tracking…” | - Monitoring: Activity explorer used to correlate events and alerts- Testing: Trigger policy using test file with matching PII content |

## Steps to create policy

Perform the following steps to edit the existing policy and enable alerting:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Policies**.
2. Choose the **U.S. Personally Identifiable Information (PII) Data Enhanced** policy that you created in [Create an endpoint DLP policy to audit activity on devices](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-audit-activities). This policy must already exist in your environment before you proceed.
3. Choose **Edit policy**.
4. Go to the **Customize advanced DLP rules** page and edit the **Low volume of content detected scenarios U.S. PII Data Enhanced**.
5. Scroll down to the **Incident reports** section and toggle **Send an alert to admins when a rule match occurs** to **On**. Email alerts are automatically sent to the administrator and anyone else you add to the list of recipients.

    
6. For the purposes of this scenario, choose **Send alert every time an activity matches the rule**.
7. Choose **Save**.
8. Leave all other policy and rule settings unchanged. Choose **Next** through the remaining wizard pages, and then select **Submit** to save the policy changes.
9. Try to share a test item containing content that will trigger the U.S. Personally Identifiable Information (PII) Data Enhanced condition. Sharing the test item should trigger a policy match and generate an alert.
10. Check the activity explorer for the event.
