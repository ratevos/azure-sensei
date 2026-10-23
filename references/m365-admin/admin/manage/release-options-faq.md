# Frequently asked questions about modern release options for Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/release-options-faq  
> Microsoft doc last updated: 04/14/2026


This article provides answers to frequently asked questions that IT admins might have about release options in Microsoft 365. For more information about modern release options in Microsoft 365, see [Modern change management for Microsoft 365 - Overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/plan-for-change-management) and [Configure modern release options](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/configure-release-options).

> [!NOTE]
> Deferred release only supports features identified as both major updates *and* that are deferred-capable. For information on which features are deferred-capable, check Message Center posts.

## Can I choose which users get Microsoft 365 features earlier vs later?

Yes, within the same tenant, you can choose from the following options:

- Assign most users to standard release and assign a subset of users to deferred release, or
- Assign most users to deferred release and assign a small group of early adopters to standard release

This allows you to:

- Test changes with IT or pilot groups first
- Give business-critical users more time before receiving changes

## Can I defer individual features?

No, you can’t defer individual features. Deferred release applies to eligible major features that Microsoft identifies as "deferred‑capable."

If your tenant is configured for deferred release, all eligible major features follow the deferred timeline automatically.

You can still use existing admin controls (when available) to manage specific features in your tenant.

## When does the 30‑day deferred period begin?

The 30‑day timer starts when the feature *begins* rolling out in GA to standard release users globally. The deferred period doesn't begin when the standard global rollout completes. Standard users can begin evaluating the feature immediately, but users that are in deferred release receive the feature 30 days later.

## What if feature rollout takes weeks or months to reach all users?

Microsoft rolls out Microsoft 365 features in stages to help ensure quality.

When we roll out a feature for general availability, standard release users receive the feature before deferred release users. Users assigned to standard release can start evaluating the feature as soon as it reaches your standard release users.

Deferred release users receive the deferred-capable feature 30 days after the rollout to Standard release begins. This delay gives IT admins and power users more time to test, validate, and prepare before the feature reaches your deferred release users.

## Will tenant-wide features respect standard and deferred user settings?

Most Microsoft 365 features are delivered at the user level and respect your standard and deferred assignments. However, some features are deployed at the tenant level. Tenant-wide changes might apply to all users at once, regardless of release audience assignment.

## What happens if a feature needs to be rolled back?

If Microsoft finds a quality issue during rollout:

- Microsoft pauses the rollout.
- Users who haven’t received the feature won’t get it.
- If needed, Microsoft might remove the feature from users who already received it.

Deferred release users won't receive a feature that Microsoft rolls back before it reaches them.

## Does deferred release replace admin controls?

No, deferred release provides time to evaluate production-ready, generally available features. It works alongside existing admin controls, feature-level enable/disable settings (when available).

You can still request additional controls through your Microsoft account team if needed.

## How does Message center support deferred release?

For deferred release, we've updated the Message center to do the following actions:

- Clearly identify deferred-eligible features
- Include a **Rollout timing** column to help you plan for updates
- Send out announcements closer to the start of GA to ensure accuracy

These updates can help reduce shifting timelines, improve readiness planning, and align communications with generally available and fully supported features. For information about Message center updates, see [What's new in Message center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/message-center-updates).

## Can I assign most of my organization to standard release and specific users to deferred release?

Yes, if your organization needs more time for validating deferred-capable features, you can leverage assigning specific users to deferred release in the audience-based release model. For more information about configuring modern release options, see [Configure modern release options for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/configure-release-options).

## Does deferred release apply to features that aren't major changes?

No, even if you have users in deferred release, a feature that isn’t classified as a major change and deferred-eligible via Message center still releases to users when the feature is broadly available.

## How does deferred release affect Frontier features?

Deferred release doesn't apply to Frontier program features. Deferred release enables customers to delay delivery of eligible features at general availability (GA). Frontier provides preview access for early adopters to evaluate new experiences and provide feedback. Frontier access is managed separately from deferred release. Although Frontier features are pre-release, they run within an otherwise generally available (GA) environment. For more information, see [Get started with the Microsoft Frontier program](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier).

## Where can I find guidance on these new features and updates?

Check for updates to this article, [Modern change management for Microsoft 365 - Overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/plan-for-change-management), Message Center posts, and the [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) for more information about modern change communications coming to Microsoft 365.

## Do standard release and deferred release options affect Microsoft 365 App release options?

No. For information about release options for Microsoft 365 Apps, see [Overview of update channels for Microsoft 365 Apps](https://learn.microsoft.com/en-us/deployoffice/overview-update-channels).

## How does this impact targeted release?

If your organization is using [targeted release](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/release-options-in-office-365) for other Microsoft 365 services, you can continue to do so as we drive towards our converged release strategy. We recommend configuring release preferences for frontier, standard, and deferred audiences to align with the new release model as Microsoft begins delivering an increasing number of major features through it over time. Use the Microsoft Message center to keep up with new products and services using this audience-based release model.

## Related articles

[Configure modern release options for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/configure-release-options)

[Modern change management for Microsoft 365 - Overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/plan-for-change-management)

[Get started with the Microsoft Release Communications MCP Server](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/mrc-mcp)

[What's new in Message center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/message-center-updates)
