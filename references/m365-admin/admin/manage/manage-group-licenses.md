# Assign or unassign licenses to a group in the Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-group-licenses  
> Microsoft doc last updated: 04/17/2026


If you have security groups, mail enabled groups, or Microsoft 365 groups, you can assign or unassign licenses for those groups on the **Licenses** page in the Microsoft 365 admin center. We refer to this as *group-based licensing*.

> [!NOTE]
> Some Microsoft services aren't available in all locations. Before a license can be assigned to a user, the administrator must specify the  user's location setting. For group-based licensing, any users without a specific location inherit the location of the tenant. If you have users in multiple locations, we recommend that you always set the user location as part of your user creation flow. For more information, see [Add users and assign licenses in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users).

## Before you begin

- You must be at least a Groups Administrator, License Administrator, or User Administrator to assign licenses.
- In addition to the steps described in this article, you can also use the Microsoft Graph PowerShell SDK to assign or unassign Microsoft 365 licenses to groups. For more information, see [Set-MgGroupLicense](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.groups/set-mggrouplicense).
- Group-based licensing doesn't currently support nested groups (groups that contain other groups). If you assign licenses to a nested group, only users in the first-level group are assigned licenses.
- When you assign or modify licenses for a large group, like 100,000 users, it can affect performance. In certain high load situations, it might take a long time to process license changes for groups or membership changes to groups with existing licenses.

## Limitations of group-based licensing in the Microsoft 365 admin center

- You can assign licenses to a maximum of 20 groups at a time.
- When you select **Reprocess** to resolve issues with group license assignment, the feature attempts to reprocess licenses up to a maximum of 20 users at a time.
- The lists of users who were and who weren't successfully assigned licenses are paginated lists that display 999 users at a time. You must scroll to the bottom of the list to load the next set of users.

## Assign licenses to a group

1. Sign in to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a> as at least a License Administrator.
1. Go to the **Billing** > <a href="https://go.microsoft.com/fwlink/p/?linkid=842264" target="_blank">Licenses</a> page.
1. On the **Licenses** page, select **Assign licenses**.
1. In the side panel, search for the group that you want to assign licenses to, then select the name from the dropdown list.
1. Select the subscription that the assigned licenses should come from.
1. To assign or remove access to specific items, select **Turn apps and services on or off**.
1. When you're finished, select **Assign licenses**.

## Manage group-based licensing errors

If you receive any errors during license assignment, you can view them on the product details page.

1. In the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>, go to the **Billing** > <a href="https://go.microsoft.com/fwlink/p/?linkid=842264" target="_blank">Licenses</a> page.
2. Select the product that you want to view licenses for.
3. Select the **Errors & issues** tab to see a list of users who have license assignment problems.
4. Select a user to inspect what type of error they encountered.

For a full description of each error type, including insufficient licenses, conflicting service plans, missing dependencies, proxy address issues, and usage location problems, along with steps for how to resolve them, see [Identify and resolve license assignment problems for a group](https://learn.microsoft.com/en-us/entra/fundamentals/licensing-groups-resolve-problems).

## Unassign licenses from a group

1. In the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>, go to the **Billing** > <a href="https://go.microsoft.com/fwlink/p/?linkid=842264" target="_blank">Licenses</a> page.
2. Select the product that you want to unassign licenses for.
3. On the product details page, find the group in the list.
4. Select the three dots (more actions) on the group's row, then select **Unassign**.
5. In the confirmation dialog, select **Unassign**.

## Related content

[Assign or unassign licenses for users in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users) (article)\
[Buy or remove licenses for a Microsoft business subscription](https://learn.microsoft.com/en-us/microsoft-365/commerce/licenses/buy-licenses) (article)\
[Identify and resolve license assignment problems for a group](https://learn.microsoft.com/en-us/entra/fundamentals/licensing-groups-resolve-problems) (article)
