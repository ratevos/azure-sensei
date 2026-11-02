# Get started with data loss prevention simulation mode

> Source: https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-get-started  
> Microsoft doc last updated: 2026-10-21


You can use Microsoft Purview Data Loss Prevention (DLP) simulation mode to see:

- The impact of a policy on your production environment without enforcement.
- All the items that would be matched by a policy if it were enforced.

This article walks you through simulation mode prerequisites, configuration options and how to view simulation results.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

The account you use to interact with simulation mode must be in the Information Protection admin role. For more information on the roles and role groups necessary to use simulation mode, see [Permissions](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions). For more information on roles and role groups in Microsoft Purview compliance, see [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview compliance](https://learn.microsoft.com/en-us/en-us/microsoft-365/security/office-365-security/scc-permissions)

## Configure system settings for DLP simulation mode

To see matched items from endpoint devices in their native application on the **Items for review**, you must configure [evidence collection for file activities on devices](https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-learn#learn-about-evidence-collection-for-file-activities-on-devices).

## Manage DLP simulation mode

You can set a policy to be in simulation mode when you create it or after it's been created. You can also turn off simulation mode for a policy that's already in simulation mode.

1. Use the steps in [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) to create a new policy or edit an existing policy.
2. The last step in the policy configuration workflow is **Simulate or turn on the policy**. Select **Run the policy in simulation mode** to enable simulation mode. Select either **Turn it on right away** or **Keep it off**to disable simulation mode. You can further select:
    1. **Show policy tips with in simulation mode** to help educate your users when they take actions that might trigger policy actions.
    2. **Turn the policy on if it's not edited within fifteen days of the simulation** to turn the policy on without further interaction.
3. Select **Next** and **Submit**.

After disabling simulation mode, it can take up to 24 hours for the insights to stop appearing on the Overview page.

## Viewing DLP policies in simulation mode

Perform the following steps to view a policy that is running in simulation mode.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data Loss Prevention** &gt; **Policies**.
2. Select a policy with a status of **In simulation** or **In simulation with notifications** to open the fly-out pane.
3. Select **View simulation** to see the **Simulation overview**, **Items for review**, and **Alerts** tabs.

## Simulation mode status messages

Note

Scan results from running a policy in simulation mode are saved for 30 days. You can continue to run the policy in simulation mode longer than that, but only the results for the most recent 30-day period are displayed.

When a policy runs in simulation mode, content scanning in most locations occurs in real time, that is, it occurs when an email or Teams message is sent. Content scanning for the SharePoint and OneDrive locations works a little differently. In addition to scanning content when documents are uploaded to these locations, policies running in simulation mode can display three additional progress messages: *Completed*, *In progress*, and *Expired*. The following table identifies and describes the status messages available for each location:

### Simulation mode scan status by location

The following table lists the scan status messages by location.

| Location | Status message descriptions |
| --- | --- |
| Exchange | **Real-time** - Content is scanned when message is sent |
| SharePoint | **Completed** - Signifies that scanning the existing content in Sharepoint and/or OneDrive is complete. This status message only displays when SharePoint and/or OneDrive are the only locations in scope. **In progress** - Signifies that the simulation is running. Results are updated as more matches are found. |
| OneDrive | **Completed** - Signifies that scanning the existing content in Sharepoint and/or OneDrive is complete. This status message only displays when SharePoint and/or OneDrive are the only locations in scope. **In progress** - Signifies that the simulation is running. Results are updated as more matches are found. |
| Teams chat and channel messages | **Real-time** - Content is scanned when message is sent |
| Devices | **Real-time** - Content is scanned when transferred off the device |
| Fabric and Power BI | **Real-time** - Content is scanned when uploaded |

The following table explains the status messages related to the progress of the overall policy simulation.

### Overall simulation mode status

The following table explains the overall simulation status values.

| Simulation status | Description |
| --- | --- |
| Completed | Only available when a DLP policy scope is limited to SharePoint, OneDrive, or both. Indicates that all data at rest has been scanned. |
| In progress | Simulation scanning is underway. Results are updated as additional policy matches are detected. |
| Expired | The policy being simulated is more than 30 days old. Microsoft Purview retains simulation data for only 30 days. To get scan results for data at rest scanned prior to the most recent 30-day window, re-run the scan. |

For SharePoint and OneDrive, **Items for review** shows up to 100 matched items per site for each policy rule. Because this limit applies to each site and rule, the list can contain more than 100 items in total. It might not include every match, so the number of items shown might differ from the total number of matched items.

Simulation events are displayed up in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). You can filter on *Policy mode*, which has *TestWithNotifyUser*, *TestWithoutNotifyUser* and *enforce* values.
