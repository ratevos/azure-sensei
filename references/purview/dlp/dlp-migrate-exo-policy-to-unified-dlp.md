# Design a data loss prevention policy

> Source: https://learn.microsoft.com/en-us/purview/dlp-migrate-exo-policy-to-unified-dlp  
> Microsoft doc last updated: 2025-04-08


Taking the time to design a policy before you implement it gets you to the desired results faster, with fewer unintended issues, than creating it and then tuning by trial and error alone. Having your policy designs documented will help you in communications, policy reviews, troubleshooting, and further tuning.

If you're new to Microsoft Purview DLP, it's helpful to work through these articles before you start designing a policy:

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

1. [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units)
2. [Learn about Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
3. [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#plan-for-data-loss-prevention-dlp)- by working through this article you will:
    1. [Identify stakeholders](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#identify-stakeholders)
    2. [Describe the categories of sensitive information to protect](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#describe-the-categories-of-sensitive-information-to-protect)
    3. [Set goals and strategy](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#set-goals-and-strategy)
4. [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview)
5. [Collection policy reference](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference)
6. [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference) - this article introduces all the components of a DLP policy and how each one influences the behavior of a policy
7. [Design a DLP policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) - this article walks you through creating a policy intent statement and mapping it to a specific policy configuration.
8. [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) - This article presents some common policy intent scenarios that you map to configuration options, then it walks you through configuring those options.
9. [Learn about investigating data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn) - This article introduces you to the lifecycle of alerts from creation, through final remediation and policy tuning. It also introduces you to the tools you use to investigate alerts.

## Policy design overview

Designing a policy is mostly about clearly defining your business needs, documenting them in a policy intent statement, and then mapping those needs to policy configuration. You use the decisions you made in your planning phase to inform some of your policy design decisions.

### Define intent for the policy

You should be able to summarize, in a single statement, the business intent for every policy you have. Developing this statement drives conversations in your organization and, when fully fleshed out, this statement directly links the policy to a business purpose and provides a roadmap for policy design. The steps in the [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#overview-of-planning-process) article helps you get started on your policy intent statement.

Remember that, as described in the [DLP policy configuration overview](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#dlp-policy-configuration-overview), all DLP policies require you to:

- Choose what you want to monitor
- Choose the [Policy Scoping](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#policy-scoping).
- Choose where you want to monitor .
- Choose the conditions that must be matched for a policy to be applied to an item.
- Choose the action to take when the policy conditions are met.

For example, here's a fictitious first draft of an intent statement that provides answers to all five questions:

*"We're a U.S. based organization, and we need to detect Office documents that contain sensitive health care information covered by HIPAA that are stored in OneDrive/SharePoint and to protect against that information being shared in Teams chat and channel messages and restrict everyone from sharing them with unauthorized third parties".*

As you develop a policy design, you'll likely modify and extend the statement.

### Map business needs to policy configuration

Let's break down the example draft statement and map it to DLP policy configuration points. This example assumes that you're using an unrestricted DLP admin account and that administrative units aren't configured.

Important

Be sure you understand the difference between an *unrestricted administrator* and an *administrative unit restricted administrator* by reading [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units) before you start.

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| "We're a U.S. based organization, and we need to detect Office documents that contain sensitive health care information covered by HIPAA... | - **What to monitor**: Office docs, use the [U.S. Health Insurance Act (HIPAA)](https://learn.microsoft.com/en-us/purview/dlp-policy-templates-include#us-health-insurance-act-hipaa-enhanced) template - **Conditions for a match**: (preconfigured but editable) - item contains U.S. SSN and Drug Enforcement Agency (DEA) number, International Classification of Diseases (ICD-9-CM), International Classification of Diseases (ICD-10-CM), content is shared with people outside my organization  - drives conversations to clarify the triggering threshold for detection like [confidence levels](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about#more-on-confidence-levels), and [instance count](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#content-contains) (called leakage tolerance). |
| ...that are stored in OneDrive/SharePoint and protect against that information being shared in Teams chat and channel messages... | - **Where to monitor**: [Location scoping](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#locations) by including or excluding OneDrive and SharePoint sites and Teams chat/channel accounts or distribution groups. **Policy scoping** (preview): [Full directory](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#policy-scoping) |
| ...and restrict everyone from sharing those items with unauthorized third parties." | - **Actions to take**: [You add](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#actions)*Restrict access or encrypt the content in Microsoft 365 locations* - drives conversation on what actions to take when a policy is triggered including protective actions like sharing restrictions, awareness actions like notifications and alerts, and user empowerment actions like allow user overrides of a blocking action |

This example doesn't cover all the configuration points of a DLP policy; it would need to be expanded. However, it should get you thinking in the right direction as you develop your own DLP policy intent statements.

Important

Keep in mind that the location(s) you pick impact whether you can use sensitive information types, sensitivity labels, and retention labels. The location(s) you pick also impact the actions that are available. See [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference) for more information.

### Complex rule design

The above HIPAA content in SharePoint and OneDrive is a simple example of a DLP policy. The DLP rule builder supports boolean logic (AND, OR, NOT) and nested groups.

Important

- All existing **Exceptions** are replaced with a NOT condition in a nested group inside of the **Conditions**.
- You need to create groups in order to use multiple operators.

Important

When an action in Office desktop client apps, (Word, Outlook, Excel, and PowerPoint) matches a policy that uses complex conditions, the user will only see policy tips for rules that use the **Content contains sensitive information** condition.

- *Example 1 We need to block emails to all recipients that contain credit card numbers, OR that have the 'highly confidential' sensitivity label applied, but do NOT block the email if it is sent from someone on the finance team to adele.vance@contoso.com*
- *Example 2 Contoso needs to block all emails that contain a password protected file OR a zip document file extension ('zip' or '7z'), but do NOT block the email if the recipient is in the contoso.com domain OR the fabrikam.com domain, OR the sender is a member of the Contoso HR group.*

Important

- Using the NOT condition in a nested group replaces the **Exceptions** functionality.
- You need to create groups in order to use multiple operators.

Important

When an action in Office desktop client apps (Word, Outlook, Excel, and PowerPoint) matches a policy that uses complex conditions, the user will only see policy tips for rules that use the **Content contains sensitive information** condition.

## Policy Design Process

1. Complete the steps in [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#plan-for-data-loss-prevention-dlp) - by working through this article you will:

    1. [Identify your stakeholders](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#identify-stakeholders)
    2. [Describe the categories of sensitive information to protect](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#describe-the-categories-of-sensitive-information-to-protect)
    3. [Set goals and strategy](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#set-goals-and-strategy)
    4. [Define your policy deployment plan](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#policy-deployment)
2. Familiarize yourself with [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference) so that you understand all the components of a DLP policy and how each one influences the behavior of a policy.
3. Familiarize yourself with [what the DLP policy templates include](https://learn.microsoft.com/en-us/purview/dlp-policy-templates-include#what-the-dlp-policy-templates-include).
4. Develop your policy intent statement with your key stakeholders. Refer to the example earlier in this article.
5. Determine how this policy fits into your overall DLP policy strategy.
6. Map the items in your policy intent statement to configuration options.
7. Decide which policy template you start from: predefined or custom.
8. Go through the template and assemble all information required before you create the policy. It's likely that you will find that there are some configuration points that aren't covered in your policy intent statement. That's ok. Go back to your stakeholders to iron out the requirements for any missing configuration points.
9. Document the configuration of all the policy settings and review them with your stakeholders. You can reuse your policy intent statement mapping to configuration points, which is now fully fleshed out.
10. [Create a draft policy](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) and refer back to your [policy deployment](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#policy-deployment) plan.
