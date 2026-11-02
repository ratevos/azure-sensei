# Learn about data loss prevention simulation mode

> Source: https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn  
> Microsoft doc last updated: 2024-03-27


**Run the policy in simulation mode**, otherwise known as simulation mode, for Microsoft Purview Data Loss Prevention (DLP) policies replaces the **Test** and **Test with policy tips** policy states. When a policy is in simulation mode, it's run as if it were being enforced, without any actual enforcement. Unlike the **Test** modes, all matched items and alerts are reported in a separate dashboard. This makes it easy to see the impact of the policy before you enforce it by keeping all the simulation results separate from the results of policies that are being enforced.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

Simulation mode provides:

- An isolated experience to run and assess policies.
- A summary dashboard that gives you visibility into the impact of the policies across different locations and shows which items were matched.
- A flat list of matched items at a policy level.

Simulation mode for DLP policies is a tool you can use for [tuning your data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-test-dlp-policies) at any time. You should incorporate it into your [policy creation and deployment](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) process. Using simulation mode to tune a policy reduces false positives without impact to your users or business processes. Use it as part of your deployment process for new policies, use it to test changes to existing policies before enforcing those changes in production.

For example:

DLP policy *Protect Credit Cards v1* is in production, but is throwing too many false positives. You think you know what is wrong, but you don't want to experiment with changes to it in production to find out. You can make a copy of policy *Protect Credit Cards v1*, call it *Protect Credit Cards v2*, make tuning changes, and then run *v2* in simulation mode. If it the changes have the desired result, then you can turn off *v1* and set *v2* to enforce mode.

Important

Simulations can run for up to 15 days so the results are not a point in time snapshot. For SharePoint Online and OneDrive for Business locations, all existing and new/changed items are evaluated. For Exchange, Teams, Devices locations only items that are new during simulation are evaluated. Fabric items that are updated or refreshed after a simulation starts are evaluated. Data from a simulation run is kept for 30 days.

## Placing a policy in simulation mode

See [Get started with the data loss prevention simulation mode](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-get-started) for the procedures to manage simulation mode for a policy.

## Simulation results

See [Get started with the data loss prevention simulation mode](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-get-started) for the steps to access simulation results. Simulation results are presented across three pages.

### Simulation overview

The **Simulation overview** tab gives you basic information on:

- the status of the policy simulation (complete, in progress or expired)
- status of scanning per location
- total items scanned
- total matches found
- matched items for each location
- links to the matched items

and other information.



## Items for review

The **Items for review** tab shows a flat list of the items that matched the policy in simulation and lets you read the source item along with item metadata much like [Content explorer](https://learn.microsoft.com/en-us/purview/data-classification-content-explorer).



## Alerts

The simulation mode alerts tab shows a flat list of all the alerts that were generated when an item matched the policy in simulation. It has the same format as the [DLP alerts console](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started).



Important

While a policy is in simulation mode, all simulation alerts are only surfaced in the simulation alerts tab. They don't show up in the DLP alerts console and they don't flow into the Microsoft Defender portal.
