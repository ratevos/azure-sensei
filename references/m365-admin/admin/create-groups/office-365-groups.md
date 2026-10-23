# Microsoft 365 Groups overview for administrators

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/office-365-groups  
> Microsoft doc last updated: 03/16/2026


Microsoft 365 Groups is the foundational membership service that underpins collaboration across Microsoft 365. It simplifies access management by automatically granting users permissions to shared resources when you add them to a group.

When you create a Microsoft 365 group, users can automatically access shared resources such as:

- **Communication and planning**
  - A shared Outlook inbox.
  - A shared calendar.
  - Planner.

- **Content and collaboration**
  - A SharePoint document library.
  - A OneNote notebook.
  - Microsoft Clipchamp.

- **Team-based experiences**
  - A Team (if created from Microsoft Teams).
    - Microsoft Viva Engage (if created from Microsoft Viva Engage).

- **Additional services**
  - Power BI.
  - Roadmap (if Project for the web is available).

## Microsoft 365 Groups roles and permissions

With a Microsoft 365 group, you don't need to manually assign permissions to individual resources. When you add users to the group, you automatically grant them the appropriate access.

Any user can create a group unless you [limit group creation to a specific set of people](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/manage-creation-of-groups). If you limit group creation, users can't create the following items:

- Microsoft SharePoint sites.
- Planner.
- Teams.
- Outlook group calendars.
- Clipchamp groups.
- Viva Engage groups.
- Shared libraries in OneDrive.
- Shared Microsoft Power BI workspaces.

These services require the creator to have permission to create Microsoft 365 groups. Users can still participate in group activities, such as creating tasks in Planner or using Teams chat, provided they're a member of the group.

Groups have the following roles:

- **Owners** - Manage group membership and settings. Owners can add or remove members, update the group name, description, or picture, and manage conversations in the shared inbox.

- **Members** - Access all group resources but can't change group settings. By default, members can invite guests, although that setting can be changed. For more information, see [Manage guest access in Microsoft 365 groups](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups).

- **Guests** - External users who are invited to participate in the group.

User admins and groups admins can create and manage groups in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). Delegated administrators, such as consultants acting on behalf of an organization, can't create or manage Microsoft 365 Groups.

As an administrator, you can:

- [Specify who can create groups](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/manage-creation-of-groups).
- [Create a naming policy for groups in your organization](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/groups-naming-policy).
- [Choose which domain to use when creating a group](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/choose-domain-to-create-groups).
- [Manage guest access to groups](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups).
- [Recover a deleted group](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/restore-deleted-group) (within 30 days of deletion).

## Microsoft 365 Groups expiration and lifecycle management

You can automate group cleanup by using expiration policies. When a group reaches its expiration date:

- Group owners receive renewal notifications 30 days, 15 days, and 1 day before expiration.
- Owners can renew the group if the group is still needed.
- Groups that aren't renewed are automatically deleted.

For more information, see [Microsoft 365 group Expiration Policy](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/microsoft-365-groups-expiration-policy).

You can administer your groups from the Microsoft 365 admin center or by using PowerShell. For more information, see [Manage Microsoft 365 Groups with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-groups-with-powershell).

If you have many users, such as in a large corporation or enterprise, you might have many users who create groups for various purposes. Review [Plan for governance in Microsoft 365 groups](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/collaboration-governance-overview) for best practices.

## Microsoft 365 Groups limits and restrictions

The following limits apply to Microsoft 365 Groups:

| **Maximum...**                                 | **Value** |
| ---------------------------------------------- | --------- |
| **Owners per group**                           | 100       |
| **Groups a user can create**                   | 250       |
| **Groups an admin can create**                 | There are no Microsoft 365 group specific limits. There's an overall Microsoft Entra object limit specific to each organization. A Microsoft Entra admin who can manage groups in the organization can create an unlimited number of Microsoft 365 groups up to the Microsoft Entra object limit. See [Microsoft Entra service limits and restrictions](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/directory-service-limits-restrictions). |
| **Number of members**                          | More than 1,000. Only 1,000 members can access group conversations concurrently. Users might experience delays in Outlook for large groups. |
| **Number of groups a user can be an owner of** | 7,000     |
| **Number of groups a user can be a member of** | 7,000     |
| **File storage**                               | 1 TB + 10 GB per subscribed user, plus any additional storage purchased. You can purchase an unlimited amount of extra storage. |
| **Group Mailbox size**                         | 50 GB     |

Managing your Microsoft 365 groups is more effective when you have actionable information about group usage. The Microsoft 365 admin center has a reporting tool that lets you see storage use, how many active groups you have, and how users are using the groups. For more information, see [Microsoft 365 Reports in the admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/office-365-groups).

## Sensitivity labels for Microsoft 365 Groups

You can create sensitivity labels that the users in your organization can set when they create a Microsoft 365 group. Sensitivity labels help enforce consistent security and access controls during group creation. By using sensitivity labels, you can configure:

- Privacy (public or private)
- Guest access
- Unmanaged device access

For example, you can create a label called *Highly Confidential* and specify that any group created with this label is private and doesn't allow guests. When users in your organization select this label during group creation, the group is set to private and group members aren't allowed to add guests to the group.

For information about creating, managing, and using sensitivity labels, see [Use sensitivity labels to protect content in Microsoft Teams, Microsoft 365 groups, and SharePoint sites](https://learn.microsoft.com/en-us/microsoft-365/compliance/sensitivity-labels-teams-groups-sites).

## Microsoft 365 plans that include Microsoft 365 Groups

Any Microsoft 365 subscription that includes Exchange Online and SharePoint in Microsoft 365 supports groups. This support includes the Business Basic, Business Standard, and Business Premium plans, as well as the Enterprise E1, E3, and Microsoft 365 E5 plans. The group adopts the licensing of the person who creates it. As long as the creator has the proper license for the features you want the group to have, that license extends to the group.

> [!NOTE]
>
> For more information about Microsoft 365 service families and plans, see [Microsoft 365 plan options](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/office-365-plan-options).

If you have an Exchange-only plan, you can still get the shared inbox and shared calendar features of groups in Outlook but you don't get the document library, Planner, or any of the other capabilities.

Microsoft 365 groups work with Microsoft Entra ID. The groups features you get depend on which Microsoft Entra ID subscription you have and what licenses are assigned to the person who created the group.

From an administrative perspective, creator's licenses and Microsoft Entra ID subscription determine group capabilities. Licenses assigned to individual group members don't determine group capabilities.

> [!IMPORTANT]
>
> For all the groups features, if you have a Microsoft Entra ID P1 or Microsoft Entra ID P2 subscription, users can join the group whether or not they have a Microsoft Entra ID P1 license assigned to them. Licensing isn't enforced.
>
> Periodically, Microsoft generates usage reports that tell you which users are missing a license and need one assigned to them to be compliant with the licensing requirements. For example, if a user doesn't have a license and they're added to a group where the naming policy is enforced, the report flags that they need a license.

## Related articles

- [Learn about Groups in Outlook](https://support.microsoft.com/office/b565caa1-5c40-40ef-9915-60fdb2d97fa2).
- [Manage Microsoft 365 Groups with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-microsoft-365-groups-with-powershell).
- [SharePoint limits](https://learn.microsoft.com/en-us/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).
- [Plan for governance in Microsoft 365 groups](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/collaboration-governance-overview).
