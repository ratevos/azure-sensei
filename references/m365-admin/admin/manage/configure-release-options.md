# Configure new Standard and Deferred release options for Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/configure-release-options  
> Microsoft doc last updated: 04/20/2026


Microsoft 365 delivers updates continuously, enabling organizations to adopt new capabilities without large, infrequent upgrades. To help IT admins manage this pace of change, Microsoft 365 offers a new three-tier, audience-based release model—**Frontier, Standard, and Deferred**—so organizations can balance early access with readiness and control.

> [!IMPORTANT]
> The modern release options of standard and deferred initially applies to Microsoft 365 Copilot updates that have been identified as both a major change and deferred capable in the Message center. We’ll expand this approach across all Microsoft 365 services over time. For release information for Microsoft 365 apps, see [Overview of update channels for Microsoft 365 Apps](https://learn.microsoft.com/en-us/deployoffice/overview-update-channels).

With **Standard release**, your organization receives new features as soon as they’re generally available (GA). Standard release is the default option and should be the primary release channel for most customers. Microsoft thoroughly tests and validates all features and services before we release them. Your organization is configured as standard release by default.

If you have additional validation requirements, your organization might want to consider **Deferred release** for all or some users. Features available in deferred release are major Microsoft 365 releases and are considered "deferred-capable," meaning admins will have 30 days to prepare for the release after broad release in standard begins. After 30 days, generally available Microsoft 365 features appear to your users. You can see which features are deferred-capable in the Message center.

For pre-release availability, the [Microsoft Frontier program](https://www.microsoft.com/microsoft-365-copilot/frontier-program) provides early access to innovative and emerging AI capabilities in Microsoft 365 before those features reach general availability.

You can use these new release options so you can align feature delivery with your organization’s readiness, governance requirements, and overall change management strategy.

> [!NOTE]
> Currently, the modern release options of standard and deferred release channels aren’t available for GCC, GCC High, and DoD cloud environments. Check this article for updates regarding future support.

## How release validation works

Microsoft feature teams validate each new release first, followed by the Microsoft 365 feature team, and then that feature rolls out to all of Microsoft. At each release phase, Microsoft collects feedback and further validates quality by monitoring key usage metrics before it goes to the public. This series of progressive validations helps make sure the worldwide rollout to general availability (standard release) is as robust as possible.

As shown in the following figure, you can now use a modern, audience-based release model that includes the Frontier program, Standard release, and Deferred release as release options.

For a comparison of release options, see the following table:

| Release audience | Primary purpose | Feature readiness | Key considerations for IT admins |
| ----------------- | ----------------- | ------------------- | ---------------------------------- |
| Frontier program | Early experimentation and feedback | Pre-GA, not fully supported | Frontier features are pre-release, subject to change, and not governed by GA SLAs. IT admins can control which users have access to which Frontier features and agents. |
| Standard release<br/>(default) | Default GA rollout | Fully supported GA features | Features are supported, communicated through Message Center and release notes, and expected to remain available under standard lifecycle policies. Recommended for most organizations. |
| Deferred release | Delayed GA for additional preparation | Fully supported GA features (delayed) | Same functionality as standard release, with timing delayed for 30 days after standard GA for major features to organizations with additional validation requirements. |

For significant updates, Microsoft first notifies you through the [Microsoft 365 Roadmap](https://products.office.com/business/office-365-roadmap). Before rollout, Microsoft notifies you through the <a href="https://go.microsoft.com/fwlink/p/?linkid=2070717" target="_blank">Microsoft 365 Message center</a>.

> [!NOTE]
> If your organization is using targeted release for other Microsoft 365 services, you can continue to do so as we drive towards our converged release strategy. We recommend configuring release preferences for frontier, standard, and deferred audiences to align with the new release model as Microsoft begins delivering an increasing number of major features through it over time. Use the Microsoft Message Center to keep up with new products and services using this audience-based release model.
>
> For more information about targeted release for other Microsoft 365 services, see [Configure standard and targeted release](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/release-options-in-office-365).

## Prerequisites

You must have one of the following roles in Microsoft 365 admin center to configure standard and deferred release options:

- Office Apps Admin
- Security Admin
- AI Admin

For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Release option best practices

We recommend that you use the release options in the following ways to balance early access with organizational readiness:

- To get the latest Microsoft 365 improvements as soon as they reach general availability, enroll your organization in standard release. Optionally, assign business-critical users to deferred release to give them more time to prepare for major changes.
- If you need extra time to validate deferred-capable features before broad rollout, use deferred release. Assign a subset of IT pros or power users to standard release to evaluate new features for privacy and compliance readiness.
- Plan release phases around user impact and readiness, not individual feature controls, to help manage risk and set clear expectations for users.
- Align your release configuration with your change management and support readiness, including documentation, training, and help desk preparation.
- Review and adjust audience assignments over time as your organization’s readiness and change tolerance evolve.

## Configure release options in Microsoft 365 admin center

By default, use standard release for Microsoft 365 service updates. This option meets the needs of most customers. To better manage your organization’s readiness and testing needs, you can change the default release selection at any time in the Microsoft 365 admin center. It can take up to 24 hours for the following changes to take effect in Microsoft 365.

> [!NOTE]
> Currently, Deferred release option only supports Microsoft 365 Copilot-related features. For information on which features are Deferred-capable, check Message Center posts. We'll update this documentation as more features are supported.

To assign users to the Deferred release audience, follow these steps:

1. Sign in to the Microsoft 365 admin center.
1. In the left navigation, expand **Copilot** and select **Settings**.

    

1. Under the **All Settings** tab, select **Copilot release preferences: General Availability**.
1. Choose either **Standard Release** or **Deferred Release**.
1. Add any user exceptions. You can add up to 100 user exceptions to Standard release or Deferred release.
    - If you want to only assign a specific user to deferred release, select **Standard Release**, search for the user, and select their name.

      

    - If you want to only assign a specific user to standard release, select **Deferred Release**, search for the user, and select their name.

      

1. Select **Save**.

> [!NOTE]
> If you move users from standard release to deferred release, they might lose access to features that aren't available yet in deferred release.

## Related articles

[Modern change management for Microsoft 365 - Overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/plan-for-change-management)

[Get started with the Microsoft Release Communications MCP Server](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/mrc-mcp)

[Overview of Microsoft MCP Server for Enterprise](https://learn.microsoft.com/en-us/graph/mcp-server/overview)

[What's new in Message center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/message-center-updates)

[Set up the standard or targeted release options for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/release-options-in-office-365)
