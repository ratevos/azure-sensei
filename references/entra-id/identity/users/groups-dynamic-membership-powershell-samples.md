# PowerShell samples for dynamic membership processing

> Source: https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-membership-powershell-samples  
> Microsoft doc last updated: 06/11/2026


When dynamic membership rules cause unintended changes or processing delays in your Microsoft Entra tenant, you can pause rule processing to contain the issue and resume it in a controlled order during recovery. These samples cover both dynamic groups and dynamic administrative units.

## Overview

These PowerShell samples help you pause and resume dynamic membership rule processing for groups and administrative units in your Microsoft Entra tenant when you need to mitigate ongoing membership update issues or unintended rule changes. Pausing stops rule evaluation; resuming restores it. Each script runs in two phases: groups first, then administrative units. At the start of each phase, the script asks for confirmation; enter `yes` to run that phase or anything else to skip it. This lets you target only groups, only administrative units, or both in a single run.

These samples use the [Microsoft Graph PowerShell module](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation).

## Prerequisites

- PowerShell 5.1 (x64) or later.
- The Microsoft Graph PowerShell module:

  ```powershell
  Install-Module Microsoft.Graph -Scope CurrentUser
  ```

- A signed-in account that can manage the collections you target. The groups phase needs the [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) Microsoft Entra role and the `Group.ReadWrite.All` Microsoft Graph scope. The administrative units phase needs the [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) Microsoft Entra role and the `AdministrativeUnit.ReadWrite.All` scope. Each script requests only the scopes for the phases you run.

> [!IMPORTANT]
> Verify all steps in a test environment before you run any of these scripts in production.

> [!NOTE]
> In large tenants, these scripts might trigger Microsoft Graph throttling. They include built-in retry handling, so expect a longer runtime rather than a failure. Don't cancel a running script unless you see an explicit error.

## Pause dynamic membership processing

| Sample | Description |
|---|---|
| [Pause all groups and administrative units with dynamic membership](https://learn.microsoft.com/en-us/entra/identity/users/scripts/powershell-pause-all-dynamic-membership) | Pauses every group and administrative unit that has dynamic membership rules in your tenant. Use this sample when you suspect a tenant-wide unintended change or widespread membership processing delays. |
| [Pause specific groups and administrative units with dynamic membership](https://learn.microsoft.com/en-us/entra/identity/users/scripts/powershell-pause-specific-dynamic-membership) | Pauses only the groups and administrative units whose IDs you supply. Use this sample when you need to halt processing for a known subset of collections. |
| [Pause all groups and administrative units with dynamic membership except specified](https://learn.microsoft.com/en-us/entra/identity/users/scripts/powershell-pause-all-except-dynamic-membership) | Pauses every group and administrative unit with dynamic membership except the IDs you exclude. Use this sample to keep critical collections running while halting everything else. |

## Resume dynamic membership processing

| Sample | Description |
|---|---|
| [Resume specific critical groups and administrative units with dynamic membership](https://learn.microsoft.com/en-us/entra/identity/users/scripts/powershell-resume-specific-critical-dynamic-membership) | Resumes processing for the critical groups and administrative units you specify. Run this sample first when recovering from a pause. |
| [Resume noncritical groups and administrative units with dynamic membership in batches](https://learn.microsoft.com/en-us/entra/identity/users/scripts/powershell-resume-noncritical-dynamic-membership) | Resumes processing for paused noncritical groups and administrative units, up to 100 of each per run. Run this sample after critical collections are restored and at least 12 hours have passed since pausing. |

## Related content

- [Understand and manage dynamic group processing in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/users/manage-dynamic-group)
- [Dynamic membership rules for groups](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-membership)
- [Administrative units in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units)
- [Microsoft Graph PowerShell module installation](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation)
