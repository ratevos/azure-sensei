# Manage guest access in Microsoft 365 groups

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups  
> Microsoft doc last updated: 04/22/2026


By default, guest access for Microsoft 365 groups is turned on for your organization. Administrators can control whether to allow guest access to groups for the whole organization or for individual groups.

When it's turned on, group members can invite guests to a Microsoft 365 group through Outlook on the web. The group owner receives the invitations for approval.

Once approved, the guest is added to the directory and the group.

> [!NOTE]
> Viva Engage Enterprise networks that are in Native Mode or within the [EU Geo](https://learn.microsoft.com/en-us/viva/engage/manage-security-and-compliance/manage-data-compliance) don't support network guests.
> Microsoft 365 Connected Viva Engage groups don't currently support guest access, but you can create nonconnected, external groups in your Viva Engage network. See [Create and manage external groups in Viva Engage](https://learn.microsoft.com/en-us/viva/engage/work-with-external-users/create-and-manage-external-groups) for instructions.

Guest access in groups is often used as part of a broader scenario that includes SharePoint or Teams. These services have their own guest sharing settings. For complete instructions for setting up guest sharing across groups, SharePoint, and Teams, see:

- [Collaborate with guests in a site](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/collaborate-in-site)
- [Collaborate with guests in a team](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/collaborate-as-team)

## Manage groups guest access

To enable or disable guest access in groups, use the [Groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) settings.

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Show all** > **Settings** > **Org settings**. On the [Services](https://go.microsoft.com/fwlink/p/?linkid=2053743) tab, select **Microsoft 365 Groups**.
  
1. On **Microsoft 365 Groups**, choose whether you want to let people outside your organization access group resources or let group owners add people outside your organization to groups.

## Add guests to a Microsoft 365 group in the admin center

If the guest already exists in your directory, you can add them to your groups from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2052855). You must [manage groups with dynamic membership in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-create-rule).
  
1. In the admin center, go to **Teams & groups** > [Active teams & groups](https://go.microsoft.com/fwlink/p/?linkid=2052855).

1. Select the group you want to add the guest to and select **Membership** > **Members**. 

1. Select **Add members** and choose the name of the guest you want to add.

1. Select **Save**.

To add a guest to the directory directly, you can [Add Microsoft Entra B2B collaboration users in the Azure portal](https://learn.microsoft.com/en-us/azure/active-directory/b2b/add-users-administrator).

To edit any of a guest's information, you can [Add or update a user's profile information using Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal).

## Remove a guest

When you're done collaborating with a guest, remove them so they no longer have access to your organization.

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), expand **Users** and select [Guest users](https://go.microsoft.com/fwlink/p/?linkid=2074830).

1. On the **Guest users** page, choose the user you want to remove and then choose **Delete a user**.

To remove users in the Microsoft Entra admin center, see [remove a guest and resources](https://learn.microsoft.com/en-us/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal#clean-up-resources).

## Related content

- [Block guests from a specific group](https://learn.microsoft.com/en-us/microsoft-365/solutions/per-group-guest-access)

- [Manage group membership in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/add-or-remove-members-from-groups)

- [Microsoft Entra access reviews](https://learn.microsoft.com/en-us/azure/active-directory/active-directory-azure-ad-controls-perform-access-review) 

- [Update-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/update-mguser)
