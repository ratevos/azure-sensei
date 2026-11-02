# Create and deploy a data loss prevention policy

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy  
> Microsoft doc last updated: 2026-10-23


Microsoft Purview Data Loss Prevention (DLP) policies include many configuration options. Each option changes the policy's behavior. The articles in this series cover some of the most common DLP policy scenarios. They walk you through configuring those options to give you hands-on experience with the DLP policy creation process. When you familiarize yourself with these scenarios, you gain the foundational skills that you need to use the DLP policy creation UX to create your own policies.

How you deploy a policy is as important policy design. You have multiple options to control policy deployment, including policy state, actions, and scope, as described in the Deploy and manage DLP policies section of this article. This article shows you how to use these options so that the policy achieves your intent while avoiding costly business disruptions.

*In preview* You can change the display name of DLP policies and rules. Once you rename a policy or a rule, any existing records retain their previous name in activity explorer events, in alerts and in audit records. New records will reflect the new name in activity explorer events, in alerts and in audit records. These names will remain until the items age out of the system.

## Orient yourself to DLP

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

### SKU/subscriptions licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to create and deploy policies must be a member of one of these role groups:

- Compliance administrator
- Compliance data administrator
- Information Protection
- Information Protection Admin
- Security administrator

Important

Before you start, make sure you understand the difference between an *unrestricted administrator* and an *administrative unit restricted administrator* by reading [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units).

#### Granular Roles and Role Groups

You can use these roles and role groups to fine tune your access controls.

Here's a list of applicable roles. To learn more, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- DLP Compliance Management
- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

Here's a list of applicable role groups. To learn more, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

## Policy creation scenarios for Enterprise applications & devices

The previous article, [Design a DLP policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design), introduces you to the methodology of creating a policy intent statement and then mapping that intent statement to policy configuration options.

- [Help prevent sharing credit card numbers through email](https://learn.microsoft.com/en-us/purview/dlp-create-policy-cc-email#help-prevent-sharing-credit-card-numbers-through-email)
- [Help prevent sharing sensitive items via SharePoint and OneDrive with external users](https://learn.microsoft.com/en-us/purview/dlp-create-policy-spo-odb-external#help-prevent-sharing-sensitive-items-via-sharepoint-and-onedrive-with-external-users)
- [Help protect files that Endpoint Data Loss Prevention fails to scan](https://learn.microsoft.com/en-us/purview/dlp-create-policy-edlp-scan-fails#help-protect-files-that-endpoint-data-loss-prevention-fails-to-scan)
- [Help protect files that Endpoint Data Loss Prevention doesn't scan](https://learn.microsoft.com/en-us/purview/dlp-create-policy-files-edlp-doesnt-scan#help-protect-files-that-endpoint-data-loss-prevention-doesnt-scan)
- [Help protect against sharing of a defined set of unsupported files](https://learn.microsoft.com/en-us/purview/dlp-create-policy-sharing-set-unsupported-files#help-protect-against-sharing-of-a-defined-set-of-unsupported-files)
- [Disable Microsoft Purview data loss prevention scanning for some supported files and apply controls](https://learn.microsoft.com/en-us/purview/dlp-create-policy-disable-scan-supported-files#disable-microsoft-purview-data-loss-prevention-scanning-for-some-supported-files-and-apply-controls)
- [Help prevent sharing Power BI reports with credit card numbers](https://learn.microsoft.com/en-us/purview/dlp-create-policy-powerbi-cc-numbers#help-prevent-sharing-power-bi-reports-with-credit-card-numbers)

## Policy creation scenarios for Inline web traffic

The following scenarios show how to create DLP policies for inline web traffic.

- [Help prevent sharing via Microsoft Edge for Business to unmanaged AI apps from managed devices](https://learn.microsoft.com/en-us/purview/dlp-create-policy-block-to-ai-via-edge#help-prevent-sharing-via-microsoft-edge-for-business-to-unmanaged-ai-apps-from-managed-devices)
- [Help Prevent Users from Sharing Sensitive Info with Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-create-policy-prevent-cloud-sharing-from-edge-biz)
- [Help prevent sharing sensitive information with unmanaged AI apps via network data security](https://learn.microsoft.com/en-us/purview/dlp-create-policy-ai-network-data-security)

## Deploy and manage DLP policies

A successful policy deployment isn't just about getting the policy into your environment to enforce controls on user actions. A haphazard, rushed deployment can negatively impact business processes and annoy your users. Those consequences slow acceptance of DLP technology in your organization and the safer behaviors it promotes. Ultimately, those consequences make your sensitive items less safe in the long run.

Before you start your deployment, make sure you read through [Policy deployment](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#policy-deployment). It gives you a broad overview of the policy deployment process and general guidance.

The following guidance covers the three types of deployment controls—state, actions, and scope—that you use in concert to manage your policies in production. You can change any of these controls at any time, not just during policy creation.

### Three axes of deployment management

Use three axes to control the policy deployment process: scope, state, and actions. Always take an incremental approach to deploying a policy, starting from the least impactful [DLP simulation mode](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn) through full enforcement.

#### Recommended deployment control configurations

The following table summarizes recommended combinations of policy state, scope, and action impact during deployment.

| When your policy state is | Your policy scope can be | Impact of policy actions |
| --- | --- | --- |
| Run the policy in simulation mode | Policy scope of locations can be narrow or broad | - You can configure any action  - No user impact from configured actions - Admin sees alerts and can track activities |
| Run the policy in simulation mode with policy tips | Policy should be scoped to target a pilot group and then expand the scope as you tune the policy | - You can configure any action - No user impact from configured actions  - Users can receive policy tips and alerts - Admin sees alerts and can track activities |
| Turn it on | All targeted location instances | - All configured actions are enforced on user activities - Admin sees alerts and can track activities |
| Keep it off | n/a | n/a |

#### Policy state

State is the primary control you use to roll out a policy. When you finish creating your policy, set the state of the policy to **Keep it off**. Leave it in this state while you work on the policy configuration and until you get a final review and sign off. Set the state to:

- **Run the policy in simulation mode**: No policy actions are enforced, events are audited. While in this state, you can monitor the impact of the policy in the DLP simulation mode overview and the DLP **Activity explorer** console.
- **Run the policy in simulation mode and show policy tips while in simulation mode**: No actions are enforced, but users receive policy tips and notification emails to raise their awareness and educate them.
- **Turn it on right away**: This is full enforcement mode.
- **Keep it off**: The policy is inactive. Use this state while developing and reviewing your policy before deployment.

You can change the state of a policy at any time.

#### Policy actions

Actions are what a policy does in response to user activities on sensitive items. Because you can change these actions at any time, you can start with the least impactful, *Allow* (for devices) and **Audit only** (for all other locations), gather and review the audit data, and use it to tune the policy before moving to more restrictive actions.

- **Allow**: The user activity is allowed to occur, so no business processes are impacted. You get audit data and there aren't any user notifications or alerts.

    Note

    The **Allow** action is only available for policies that are scoped to the **Devices** location.
- **Audit only**: The user activity is allowed to occur, so no business processes are impacted. You get audit data and you can add notifications and alerts to raise awareness and train your users to know that what they're doing is a risky behavior. If your organization intends to enforce more restrictive actions later on, you can tell your users that too.
- **Block with override**: The user activity is blocked by default. You can audit the event, raise alerts and notifications. This action impacts the business process, but your users are given the option to override the block and provide a reason for the override. Because you get direct feedback from your users, this action can help you identify false positive matches, which you can use to further tune the policy.

    Note

    For Exchange online and SharePoint in Microsoft 365, you configure overrides in the user notification section.
- **Block**: The user activity is blocked no matter what. You can audit the event, raise alerts and notifications.

#### Define policy scope

Every policy is scoped to one or more locations, such as Exchange, SharePoint in Microsoft 365, Teams, and Devices. By default, when you select a location, all instances of that location fall under the scope and none are excluded. You can further refine which instances of the location (such as sites, groups, accounts, distribution groups, mailboxes, and devices) that the policy is applied to by configuring the include/exclude options for the location. To learn more about your include/exclude scoping options, see [DLP policy locations](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#locations).

In general, you have more flexibility with scoping while the policy is in **Run the policy in simulation mode** state because no actions are taken. You can start with just the scope you designed the policy for or go broad to see how the policy would impact sensitive items in other locations.

When you change the state to **Run the policy in simulation mode and show policy tips**, narrow your scope to a pilot group that can give you feedback and be early adopters who can be a resource for others when they come onboard.

When you move the policy to **Turn it on right away**, you broaden the scope to include all the instances of locations that you intended when the policy was designed.

### Policy deployment steps

Use the following steps to roll out a DLP policy safely from initial review through full enforcement.

1. After you've created the policy and set its state to **Keep it off**, do a final review with your stakeholders.
2. Change the state to **Run the policy in simulation mode**. The location scope can be broad at this point so you can gather data on the behavior of the policy across multiple locations or just start with a single location.
3. Tune the policy based on the behavior data so that it better meets the business intent.
4. Change the state to **Run the policy in simulation mode and show policy tips**. Refine the scope of locations to support a pilot group if needed and make use of includes/excludes so that the policy is first rolled out to that pilot group.
5. Gather user feedback and alert and event data. If needed, tune the policy and your plans. Make sure you address all the issues that your users bring up. Your users will most likely encounter issues and raise questions about things that you didn't think of during the design phase. Develop a group of super users at this point. They can be a resource to help train other users as the scope of the policy is increased and more users come onboard. Before you go to the next stage of deployment, make sure that the policy is achieved your control objectives.
6. Change the state to **Turn it on right away**. The policy is fully deployed. Monitor DLP alerts and DLP activity explorer. Address alerts.

#### Reordering DLP policies

Microsoft Purview DLP lets you reorder policies to change their priority without changing their rules, conditions, or actions.

DLP uses internal ordering values with gaps between them to maintain the priority order displayed in the portal. These gaps allow the service to move a policy without updating every policy in the list.

After repeated moves, a gap can become too small to accommodate another move. When this happens, the service redistributes the internal ordering values to create new gaps. This preserves your chosen policy order but can require additional policies to be updated and synchronized, including policies you didn’t move.

Affected policies may show a new Last modified timestamp or a change in Policy sync status while the updates are distributed. These changes reflect updates to policy ordering, not changes to the policies’ rules, conditions, or actions. There is no fixed number of moves that triggers this process; it depends on the existing order and which policies you move.
