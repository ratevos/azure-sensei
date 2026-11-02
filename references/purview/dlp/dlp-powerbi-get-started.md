# Get started with DLP for Fabric and Power BI

> Source: https://learn.microsoft.com/en-us/purview/dlp-powerbi-get-started  
> Microsoft doc last updated: 2025-05-28


This article provides a general overview of Microsoft Purview Data Loss Prevention (DLP) policies for Fabric and Power BI. The target audience is Fabric administrators, security and compliance teams, and Fabric data owners. If you're a data owner and want to know how to respond when a policy tip tells you your item has a DLP policy match, see [Respond to a DLP policy match in Fabric](https://learn.microsoft.com/en-us/en-us/fabric/governance/data-loss-prevention-respond). If you're a Fabric admin or a security and compliance admin and need to audit alerts on DLP policy matches, see [Monitor DLP policy matches in Fabric](https://learn.microsoft.com/en-us/en-us/fabric/governance/data-loss-prevention-monitor).

## Overview

To help organizations detect and protect their sensitive data, Fabric supports [Microsoft Purview Data Loss Prevention (DLP) policies](https://learn.microsoft.com/en-us/en-us/microsoft-365/compliance/dlp-learn-about-dlp). When a DLP policy for Fabric detects a supported item type containing sensitive information, the policy triggers the configured actions. These actions can include:

- Attaching a policy tip to the item that explains the nature of the sensitive content.
- Registering an alert for administrators on the data loss prevention **Alerts** page in the Microsoft Purview portal.
- Sending email alerts to administrators and specified users.
- Restricting access to the item.

For more detail, see How do DLP policies for Fabric and Power BI work.

For DLP policies, a *member of the organization* means a user with UserType = Member. This includes users who sign in with an external account. Because their UserType is Member, they’re treated as internal users. In contrast, users with UserType = Guest are considered external. The **Block only people outside your organization** setting applies to these Guest users.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Licensing and permissions

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

You can view data from DLP for Fabric and Power BI in [Activity explorer](https://learn.microsoft.com/en-us/en-us/microsoft-365/compliance/data-classification-activity-explorer). Four roles grant permission to Activity explorer; the account you use for accessing the data must be a member of any one of them.

To view the Activity explorer, your account must be a member of any of the following roles:

- Compliance administrator
- Security administrator
- Compliance data administrator

## Billing

DLP evaluation workloads impact capacity consumption. For information about how this consumption is metered and billed, see [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models).

## How DLP policies for Fabric and Power BI work

You define a DLP policy in the data loss prevention section of the Microsoft Purview portal. In the policy, you specify the conditions, such as which sensitivity labels and sensitive info types you want to detect. You also specify the actions that the system takes when it detects a policy match.

When DLP policies evaluate a supported item type, they check if it matches the conditions in a DLP policy. If it does, the policy's specified actions take place. DLP policies start with the following actions:

### Semantic models

DLP policies evaluate a semantic model whenever one of the following events occurs:

- Publish
- Republish
- On-demand refresh
- Scheduled refresh

Note

DLP evaluation of the semantic model doesn't occur if either of the following is true:

- An account using service principal authentication initiates the event (publish, republish, on-demand refresh, scheduled refresh).
- The semantic model owner is a service principal.

### Fabric Items

DLP policies evaluate a Fabric item, such as a lakehouse, SQL database, or Mirrored database, when the data within it changes. Changes include getting new data, connecting a new source, adding tables, updating existing tables, and more.

## What happens when a Fabric DLP policy flags an item

When a DLP policy detects an issue with an item, it takes the following actions:

If you enable **user notification** in the policy, Fabric marks the item with an icon that indicates a DLP policy detected an issue with the item. When you hover over the icon, a hover card appears that provides an option to see the full details in a side panel. For more information about what you see in the side panel, see [Respond to a DLP violation in Fabric](https://learn.microsoft.com/en-us/en-us/fabric/governance/data-loss-prevention-respond).



For semantic models, opening the details page shows a policy tip that explains the policy violation and how to handle the type of sensitive information detected. Selecting **View all** opens a side panel with all the policy details.



Note

If you hide the policy tip, it doesn't get deleted. It appears the next time you visit the page.

For Fabric items, such as lakehouses, the indication appears in the header in edit mode. Opening the flyout makes it possible to see more details about the policy tips affecting the item. Selecting **View all** opens a side panel with all the policy details.



If you enable alerts in the policy, an alert records on the data loss prevention **Alerts** page in the Microsoft Purview portal. If configured, an email is sent to administrators and/or specified users. For more information, see [Monitor and manage DLP policy violations](https://learn.microsoft.com/en-us/en-us/fabric/governance/data-loss-prevention-monitor).

## Supported actions

When Fabric items or semantic models meet the conditions in a DLP policy, the actions defined in the policy are applied. DLP policies for Fabric and Power BI support three actions:

- Notify the user through a policy tip.
- Generate an alert. Administrators and users can receive alert emails. Additionally, administrators can monitor and manage alerts on the **Alerts** tab in the Purview portal.
- Restrict access (preview). When you configure a policy with the restrict access action and a policy match occurs, the policy restricts access to the data owners or to members of the organization, depending on the policy configuration. All other users lose access to the item.

For information about what triggers DLP evaluation, see How DLP policies for Fabric and Power BI work.

## Supported item types

DLP policies for Fabric and Power BI currently support the following item types.

- Semantic models
- Lakehouses
- Warehouses
- KQL databases
- Mirrored databases
- SQL databases
- Cosmos databases

See Considerations and limitations for exceptions.

## Supported condition types

DLP policy rules for Fabric and Power BI support sensitivity labels and a subset of sensitive info types (see considerations and limitations) as conditions. Learn more about Purview [Sensitive Info Types and confidence levels](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about#fundamental-parts-of-a-sensitive-information-type).

## Configure a DLP policy for Fabric and Power BI

For information about creating a DLP policy for Fabric or Power BI, see [Help prevent sharing Power BI reports with credit card numbers](https://learn.microsoft.com/en-us/purview/dlp-create-policy-powerbi-cc-numbers#help-prevent-sharing-power-bi-reports-with-credit-card-numbers) and adapt it to your own scenario.

## Gain visibility into DLP activity and adoption

After deploying DLP policies, administrators can use Fabric [governance experiences in the OneLake catalog](https://learn.microsoft.com/en-us/en-us/fabric/governance/governance-compliance-overview) to understand how data loss prevention policies are being used across their organization. These insights can help organizations:

- Identify workspaces and items evaluated by DLP policies.
- Understand where sensitive information is being detected.
- Track policy adoption across business units and workspaces.
- Prioritize remediation of high-risk data assets.
- Measure the effectiveness of DLP investments and governance programs.

Together, DLP insights help security and compliance teams move beyond individual policy violations and understand their overall data protection posture.

## Considerations and limitations

- DLP policies apply to workspaces. Only workspaces hosted in Fabric or Premium capacities are supported. For more information, see [Microsoft Fabric concepts and licenses](https://learn.microsoft.com/en-us/en-us/fabric/enterprise/licenses).
- DLP policy templates aren't supported for Fabric DLP policies. When creating a DLP policy for Fabric, choose the custom policy option.
- DLP policies for Fabric aren't supported for sample semantic models, [streaming datasets](https://learn.microsoft.com/en-us/en-us/power-bi/connect-data/service-real-time-streaming), or semantic models that connect to their data source via [DirectQuery](https://learn.microsoft.com/en-us/en-us/power-bi/connect-data/desktop-use-directquery) or [live connection](https://learn.microsoft.com/en-us/en-us/power-bi/connect-data/desktop-directquery-about#live-connections). This limitation includes semantic models with mixed storage, where some of the data comes via import-mode and some comes via DirectQuery.
- DLP policies for Fabric apply only on data in tables stored in Delta format.
- Delta tables are treated as text files for the purpose of [scanning considerations](https://learn.microsoft.com/en-us/en-us/purview/dlp-policy-reference#dlp-platform-considersations).
- DLP policies for Fabric support all the primitive Delta types except *timestamp\_ntz*.
- DLP policies for Fabric aren't supported for the following Delta Parquet data types:
    - Binary, timestamp\_ntz, Struct, Array, List, Map, Json, Enum, Interval, Void.
    - Data with LZ4, Zstd, and Gzip compression codecs.
- Advanced classifiers, such as [exact data match (EDM)](https://learn.microsoft.com/en-us/en-us/microsoft-365/compliance/sit-learn-about-exact-data-match-based-sits), [trainable classifiers](https://learn.microsoft.com/en-us/en-us/microsoft-365/compliance/classifier-learn-about), [credential classifiers](https://learn.microsoft.com/en-us/en-us/purview/sit-defn-all-creds#all-credentials-sensitive-information-types), and [named entities](https://learn.microsoft.com/en-us/en-us/purview/sit-named-entities-learn) aren't supported by DLP for Fabric. If you select an advanced classifier in the condition of a policy, the policy returns no results even if the item contains data that satisfies the advanced classifier. Other classifiers specified in the policy return results if any.
- DLP policies for Fabric aren't supported in the China North region. See [How to find the default region for your organization](https://learn.microsoft.com/en-us/en-us/fabric/admin/find-fabric-home-region) to learn how to find your organization's default data region.
- Onboarding a new tenant to DLP can take a few hours, depending on the number of supported workspaces that are being onboarded.
