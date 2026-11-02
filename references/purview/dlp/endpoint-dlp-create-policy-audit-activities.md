# Create policy to audit activities using a template (audit only mode)

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-audit-activities  
> Microsoft doc last updated: 2026-06-26


This scenario shows how to create a Microsoft Purview DLP policy using the U.S. PII Data Enhanced template to monitor sensitive data on endpoint devices. The policy runs in audit-only (simulation) mode, enabling visibility into user activity and data risk without impacting users, while using policy tips and Activity explorer for validation and analysis.

This scenario assumes an unrestricted administrator creating a policy with full directory scope.

## Prerequisites and assumptions

This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

This scenario uses the *Confidential* sensitivity label, so you must create and publish sensitivity labels before proceeding. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Human Resources* and a distribution group for the security team at Contoso.com.

This policy-creation scenario uses alerts. To learn more, see [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started).

## Policy intent statement and mapping

*We, Contoso, want to begin evaluating how sensitive information—specifically U.S. Personally Identifiable Information (PII)—is being handled on endpoint devices across our organization. Before enforcing restrictions, we want visibility into user activity and potential data risk without impacting productivity.*

*To achieve this, we will create a policy that monitors activity on devices, detects when U.S. PII is involved, and records those events for analysis. When users perform actions that match the policy conditions, we want to show policy tips to raise awareness and educate them, but we do not want to block or restrict their actions at this stage.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to evaluate how sensitive (U.S. PII) data is being used on endpoint devices…” | - Administrative scope: Full directory- Where to monitor: Devices- Scope: All users, devices |
| “We want to detect content that matches U.S. Personally Identifiable Information (PII) definitions…” | - Template selection: U.S. Personally Identifiable Information (PII) Data Enhanced- Conditions for a match: Built-in sensitive information types included in the template |
| “We want to observe activity without impacting users or blocking business processes…” | - Protection actions: No restrictive actions configured- Mode: Audit-only behavior via simulation mode |
| “We want to capture and review events when policy conditions are met…” | - Monitoring and reporting: Activity explorer used to review matched events- Alerts/events generated for matching activities |
| “We want to educate users at the time of activity without enforcing restrictions…” | - User experience: Policy tips enabled (Show policy tips while in simulation mode)- No blocking or override prompts configured |
| “We want to safely test the policy before enforcing it in production…” | - Policy mode: Run in simulation mode- Deployment approach: Validate behavior before switching to enforcement |

## Steps to create policy

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com). &gt; **Data loss prevention** &gt; **Policies**.
2. Choose **+ Create policy**.
3. Select **Data stored in connected sources**.
4. For this scenario, under **Categories**, choose **Privacy**.
5. Under **Regulations** choose **U.S. Personally Identifiable Information (PII) Data Enhanced**, and then choose **Next**.
6. Give your new policy a **Name** and **Description**, and then choose **Next**.
7. Accept the default **Full directory** under **Admin units**. Select **Next**.
8. Select the **Devices** location and deselect all other locations and then choose **Next**.
9. On the **Define policy settings** page, choose **Next**.
10. On the **Info to protect page**, choose **Next**.
11. On the **Protection actions** page, choose **Next** again.
12. On the **Customize access and override settings** page, choose **Audit or restrict activities on Devices** and then choose **Next**.
13. On the **Policy mode** page, accept the default **Run the policy in simulation mode** and select **Show policy tips while in simulation mode**.
14. Choose **Next**.
15. Choose **Submit**.
16. Once the new policy is created, choose **Done**.

Now it’s time to test your policy:

1. On the **Data Loss Prevention** home page, open **Activity explorer**.
2. Try to share a test item from your Endpoint DLP device that contains content matching the sensitive information types in the **U.S. Personally Identifiable Information (PII) Data Enhanced** template. Sharing the test item should trigger the policy.
3. Back in **Activity explorer**, check the list of activities for the policy-match event generated by the test share action.
