# Restore a deleted Microsoft 365 group

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/restore-deleted-group  
> Microsoft doc last updated: 01/06/2026


If you delete a group, by default, it's retained for 30 days. This 30-day period is considered a "soft-delete" because you can still restore the group. After 30 days, the group and its associated contents are permanently deleted and can't be restored.

When a group is restored, the following content is restored:
  
- Microsoft Entra Microsoft 365 Groups object, properties, and members
- Group's e-mail addresses
- Exchange Online shared Inbox and calendar
- SharePoint Online team site and files
- OneNote notebook
- Planner
- Teams
- Viva Engage group and group content (If the Microsoft 365 group was created from Viva Engage)
- Power BI [Classic workspace](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-workspaces)

> [!NOTE]
> This article describes how to restore Microsoft 365 groups only.

## Restore a group

You can restore a group in Outlook, the Microsoft 365 admin center, or PowerShell.

### Restore a group in Outlook

If you're the owner of a Microsoft 365 group, you can restore the group yourself in Outlook on the web by following these steps:

1. In Outlook, on the [deleted groups page](https://outlook.office.com/people/group/deleted), select the **Manage groups** option under the **Groups** node, and then choose **Deleted**.

2. Select the **Restore** tab next to the group you want to restore.

If the deleted group doesn't appear here, contact an administrator.

### Restore a group in the Microsoft 365 admin center

If you're a groups administrator, you can restore a deleted group in the Microsoft 365 admin center:

1. Go to the [Microsoft 365 admin center](https://admin.cloud.microsoft/) and sign in.

2. Expand **Groups**, and then select **Deleted groups**.

3. Select the group that you want to restore, and then select **Restore group**.

> [!NOTE]
> In some cases, it can take as long as 24 hours for the group and all of its data to be restored. 

### Restore a group by using PowerShell

To use PowerShell to restore a deleted group, see [Restore a deleted Microsoft 365 group or cloud security group in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/users/groups-restore-deleted#view-the-deleted-microsoft-365-groups-that-are-available-to-restore-by-using-powershell).

## Do you have questions about Microsoft 365 Groups?

Visit the [Microsoft Tech Community](https://techcommunity.microsoft.com/t5/microsoft-365-groups/bd-p/Microsoft365Groups) to post questions and participate in conversations about Microsoft 365 groups.
  
## Related content

- [Restore deleted email conversations](https://learn.microsoft.com/en-us/Exchange/recipients-in-exchange-online/restore-deleted-items-group)

- [Manage Microsoft 365 Groups with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-groups-with-powershell)

- [Delete groups using the Remove-UnifiedGroup cmdlet](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/remove-unifiedgroup)

- [Manage your group-connected team site settings](https://support.microsoft.com/office/8376034d-d0c7-446e-9178-6ab51c58df42)

- [Delete a group in Outlook](https://support.microsoft.com/office/ca7f5a9e-ae4f-4cbe-a4bc-89c469d1726f)
