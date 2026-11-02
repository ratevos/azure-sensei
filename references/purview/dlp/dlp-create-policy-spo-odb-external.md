# Help prevent sharing sensitive items via SharePoint and OneDrive with external users

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-spo-odb-external  
> Microsoft doc last updated: 2026-06-26


This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy that helps prevent users from sharing sensitive items via SharePoint and OneDrive with external users. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

For SharePoint and OneDrive, you create a policy to help prevent sharing of sensitive items with external users via SharePoint and OneDrive.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

This scenario uses the *Confidential* sensitivity label, so it requires you to create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Human Resources* and a distribution group for the security team at Contoso.com.

The policy creation procedure in this article uses alerts. To learn more, see [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We need to block all sharing of SharePoint and OneDrive items to all external recipients that contain social security numbers, credit card data or have the "Confidential" sensitivity label. We don't want this to apply to anyone on the Human Resources team. We also have to meet alerting requirements. We want to notify our security team with an email every time a file is shared and then blocked. In addition, we want the user to be alerted via email and within the interface if possible. Lastly, we don’t want any exceptions to the policy and need to be able to see this activity within the system.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We need to block all sharing of SharePoint and OneDrive items to all external recipients...” | - Administrative scope: **Full directory**- Where to monitor: **Enterprise applications & devices**, **SharePoint sites**, **OneDrive accounts**- Conditions for a match: First **Condition** &gt; **Shared outside my org**- Action: **Restrict access or encrypt the content in Microsoft 365 locations** &gt; **Block users from receiving email or accessing shared SharePoint, OneDrive** &gt; **Block only people outside your organization** |
| "...that contain social security numbers, credit card data or have the "Confidential" sensitivity label...” | - What to monitor: use the **Custom** template - Condition for a match: Create a second condition that is joined to the first condition with a boolean AND - Conditions for a match: Second condition, first condition group &gt; **Content contains Sensitive info types** &gt; **U.S. Social Security Number (SSN)**, **Credit Card Number**- **Condition group configuration** Create a second Condition group connected to the first by boolean OR - Condition for a match: Second condition group, second condition &gt; **Content contains any of these sensitivity labels** &gt; **Confidential**. |
| “...We don't want this to apply to anyone on the Human Resources team...” | - Where to apply: exclude the Human Resources Team OneDrive accounts |
| "...We want to notify our Security team with an email every time a file is shared and then blocked..." | - Incident reports: **Send an alert to admins when a rule match occurs**- Send email alerts to these people (optional): add the Security team - Send an alert every time an activity matches the rule: **selected**- Use email incident reports to notify you when a policy match occurs: **On**- Send notifications to these people: add individual admins as desired - You can also include the following information in the report: select **all options** |
| "...In addition, we want the user to be alerted via email and within the interface if possible...” | - User notifications: **On**- Notify users in Office 365 with a policy tip: **selected** |
| “...Lastly, we don’t want any exceptions to the policy and need to be able to see this activity within the system...” | -User overrides: **not selected** |

When you configure the conditions, the summary looks like this:



## Steps to create policy

Important

For this policy creation procedure, leave the policy turned off. Change these settings when you deploy the policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Data loss prevention** &gt; **Policies** &gt; **+ Create policy**.
3. Select **Enterprise applications & devices**.
4. Select **Custom** from both the **Categories** list and the **Regulations** list.
5. Select **Next**.
6. Enter a **Name** and a **Description** for the policy. You can use the policy intent statement here.

Important

You can't rename policies.

1. Select **Next**.
2. Accept the default **Full directory** on the **Assign admin units** page.
3. Select **Next**.
4. Choose where to apply the policy.
    1. Ensure that the **SharePoint sites** and **OneDrive accounts** locations are selected.
    2. Deselect all other locations.
    3. Select **Edit** in the **Actions** column next to **OneDrive accounts**.
    4. Select **All users and groups** and then select **Exclude users and groups**.
    5. Select **+Exclude** and then **Exclude groups**.
    6. Select **Human Resources**.
5. Select **Done** and then select **Next**.
6. On the **Define policy settings** page, the **Create or customize advanced DLP rules** option should already be selected. Select **Next**.
7. On the **Customize advanced DLP rules** page, select **+ Create rule**.
8. Give the rule a **Name** and a **description**.
9. Select **Add condition**and use these values:
    1. Select **Content is shared from Microsoft 365**.
    2. Select **with people outside my organization**.
10. Select **Add condition**to create a second condition and use these values.
    1. Select **Content contains**.
11. Select **Add** &gt; **Sensitivity labels** &gt; and then **Confidential**.
12. Select **Add**.
13. Under **Actions**, add an action with these values:
    1. **Restrict access or encrypt the content in Microsoft 365 locations**.
    2. **Block only people outside your organization**.
14. Set the **User Notifications** toggle to **On**.
15. Select **Notify users in Office 365 services with a policy tip** and then select **Notify the user who sent, shared, or last modified the content**.
16. Under **User overrides**, make sure that **Allow override from M365 services** is *NOT* selected.
17. Under **Incident reports**:
    1. Set **Use this severity level in admin alerts and reports** to **Low**.
    2. Set the toggle for **Send an alert to admins when a rule match occurs** to **On**.
18. Under **Send email alerts to these people (optional)**, choose **+ Add or remove users** and then add the email address of the security team.
19. Select **Save** and then select **Next**.
20. On the **Policy mode** page, choose **Run the policy in simulation mode** and **Show policy tips while in simulation mode**.
21. Select **Next** and then select **Submit**.
22. Select **Done**.

## Variant: Block specific external domains or users (public preview)

This variant uses the same scenario as the main SharePoint and OneDrive external sharing policy but swaps the action to demonstrate the **Block access for specific external domains or users** suboption, available in public preview for SharePoint and OneDrive only. Use this variant when you need to block access for a specific list of external domains or user SMTPs rather than blocking all external recipients.

### Policy intent statement (variant)

*We need to block sharing of SharePoint and OneDrive items containing social security numbers, credit card data, or the "Confidential" sensitivity label to people on our list of restricted external domains (for example, `adatum.com`) and to specific guest SMTPs (for example, `j.doe@firstupconsultants.com`). All other external recipients are allowed. We don't want this to apply to anyone on the Human Resources team. Alerting is supported for this action. User notification and override capability are not supported for this action.*

### Configuration mapping (variant)

The following table maps the variant policy intent to the corresponding configuration choices.

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| "...block sharing... to people on our list of restricted external domains... and to specific guest SMTPs..." | - Action: **Restrict access or encrypt the content in Microsoft 365 locations** &gt; **Block users from receiving email or accessing shared SharePoint, OneDrive** &gt; **Block access for specific external domains or users**- Specify each restricted domain with **Domain IS** (for example, `adatum.com`).- Specify each restricted user with **User IS** (for example, `j.doe@firstupconsultants.com`).- (Optional) Use **Domain IS NOT** or **User IS NOT** to explicitly allow specific domains or users that would otherwise match a block list. |

All other mapping rows from the main SharePoint and OneDrive external sharing scenario — administrative scope, conditions, exclusions, incident reports, user notifications, and user overrides — are unchanged.

### Steps to create the variant policy

Follow the same procedure in Steps to create policy, with one change at the **Actions** step:

- Under **Actions**, add an action with these values:
    1. **Restrict access or encrypt the content in Microsoft 365 locations**.
    2. **Block access for specific external domains or users**.
    3. Add each restricted domain by using **Domain IS** (for example, `adatum.com`).
    4. Add each restricted user by using **User IS** (for example, `j.doe@firstupconsultants.com`).
    5. (Optional) Use **Domain IS NOT** or **User IS NOT** to add allow entries that override a block entry.

Note

When you use **Block access for specific external domains or users**: if a user or domain appears in both allow and block lists, the block takes effect (most restrictive wins). If a file matches both an allow rule and a block rule, evaluation is per rule — allowed users and domains are permitted, blocked users and domains are denied, and users in neither list are blocked by default. Internal users and domains can't be blocked with this suboption; use **Block everyone** for internal users.

Important

Public preview limitations: image files aren't protected by this suboption, and multiple audit records can be generated for certain actions on a blocked file by a blocked user.
