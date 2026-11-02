# Get started with data loss prevention analytics

> Source: https://learn.microsoft.com/en-us/purview/dlp-analytics-get-started  
> Microsoft doc last updated: 2026-06-26


Microsoft Purview data loss prevention (DLP) analytics helps customers understand top data protection risks, blind spots, and policy and posture improvement opportunities in their organization. It can help you investigate these risks using intelligent Purview features, and mitigate them in a few simple steps.

This section introduces DLP analytics concepts, prerequisites, and configuration steps to start using it.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

DLP analytics shows customers their top data loss risks and vulnerabilities and how to mitigate them through new or improved policies. DLP analytics helps mitigate risks in three ways:

- It communicates the top item oversharing risks through the **Risk Spotlighting** card on the DLP overview page in the Microsoft Purview portal. Analytics reports on top risks, blind spots, and policy improvement opportunities based on past 30 days data.
- Help prevent users from sharing additional sensitive information externally by creating new DLP policies with one click. Policy creation recommendations are based on industry best practices and risks found in the tenant.
- Improve the accuracy of existing policies via the **Policy Improvement** card with one click.

Risks and recommendations are refreshed every week.

When DLP analytics is enabled, it scans signals on user activity, sensitive data sharing patterns, and policy information to generate insights that help you set up and refine DLP policies. It takes seven days to generate recommendations after you turn on DLP analytics.

## Before you begin

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

To see DLP analytics your account must be one of these two roles:

- Global admin
- Compliance Administrator

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

## Enable DLP risk-detection analytics

DLP analytics is turned **Off** by default. You need to explicitly opt in. Scans run every hour on your data present in audit logs and policy data.

Note

It takes seven days to start seeing analytics and recommendations in your tenant once analytics are re-enabled.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Overview**
2. Check the **Turn on analytics for risk detection and policy refinement opportunities (preview)** option.
3. Select **Turn on analytics**

## Disable DLP analytics

After disabling DLP analytics, it can take up to 24 hours for the insights to stop appearing on the Data loss prevention **Overview** page.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Settings** (gear in the menu bar) &gt; **Data Loss Prevention** &gt; **Analytics (preview)**.
2. Set the **Activate analytics** toggle to **Off**.

### View policies created by DLP analytics

To identify policies created by DLP analytics, perform the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data Loss Prevention** &gt; **Policies**.
2. Look for policy names in this format: *RiskSpotlighting-YYYY-MM-DD*.

### Review policies updated by DLP analytics

When you tell DLP analytics to update an existing policy, it makes all updates in a new version of the policy. The name of the original policy is appended with *\_copy* and the original policy is turned off. The new version is then deployed. For example:

1. There's a policy named *All credit cards* that is generating too many false positives.
2. DLP analytics suggests changes to the policy to reduce false positives.
3. You tell DLP analytics to update the policy.
4. DLP analytics creates a new version of the policy named *All credit cards*
5. DLP analytics renames the original version of the policy to *All credit cards\_copy* and sets its status to **Keep it off**.
6. DLP analytics deploys the new version of the policy named *All credit cards* and sets it status to **Turn it on**.
