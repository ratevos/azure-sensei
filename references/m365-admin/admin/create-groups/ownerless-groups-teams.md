# Manage ownerless Microsoft 365 groups and teams

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/ownerless-groups-teams  
> Microsoft doc last updated: 04/22/2026


A team in Microsoft Teams or a Microsoft 365 group can become ownerless if you delete an owner's account in Microsoft 365. Groups and teams need an owner to add or remove members and change group settings.

This article explains how to handle ownerless Microsoft 365 groups in the Microsoft 365 admin center.

## How the ownerless group policy works

An Exchange administrator or Groups administrator can create a policy that automatically asks the members who are the most active in the group if they accept ownership.

When a member accepts the invitation to become an owner, the action is logged in the Microsoft Purview portal audit log.

If there's no group activity, the policy asks random group members to accept ownership.

## Requirements of the ownerless group policy

To set up and manage the Microsoft 365 ownerless group policy, you need to meet **one** of the following requirements:

- **An eligible Microsoft 365 subscription**
   - Eligible plans include Microsoft 365 Business Premium, Microsoft 365 Enterprise E3 and E5, Office 365 and Microsoft 365 Government G3 and G5, Microsoft 365 Education A3 and A5, and Frontline F1 and F3.

- **An Azure P1 or P2 premium plan**
   - All notification options in the ownerless groups policy require an Azure premium plan because a security group is used to specify which group members receive ownership notifications. Security groups are a feature of Azure premium plans.

## Limitations of the ownerless group policy

Managing ownerless groups by using this policy has a few limitations. The following list explains these limitations:

- **The ownerless group policy only applies to Microsoft 365 groups.**
   - Not all SharePoint, Stream, and other apps' groups are Microsoft 365 groups. Viva Engage groups are Microsoft 365 groups if the tenant is in Native mode.

- **You can't batch update the groups the policy targets.**
   - You can only search for and add one Microsoft 365 group at a time to this policy.

## Set up the ownerless group or team policy

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), expand **Settings** and select **Org settings**.

1. On the [Services](https://go.microsoft.com/fwlink/p/?linkid=2053743) tab, select **Microsoft 365 Groups**.

1. Select the **When there's no owner, email and ask active group members to become an owner** checkbox.

1. If you want to keep the default configuration settings, select **Save**.

## Customize the ownerless group policy

1. On the **Microsoft 365 Groups** pane, select **Configure policy**.

1. On the **Weekly notification options** page, specify who can receive ownership notifications. If you choose to allow or block certain members, search for and add the security group that you want to use.

   1. To limit who can be invited to be an owner by using a security group, you need a Microsoft Azure P1 or P2 license for each Microsoft 365 group member in your organization, but you don't need to assign it.
   
   1. Type the number of active members that you want to notify, and select the number of weeks to send the notification. The notification list is created during the first notification and doesn't change.
   
   3. Select **Next**.

1. On the **Who is this email coming from** page, select a sender for the email, and then select **Next**.

   Shared mailboxes aren't supported. The sender must be either a user mailbox or a group mailbox.

1. On the **Subject and message** page, customize the email and optionally include a **policy guideline URL**, and then select **Next**.

   You can't have the notification's language change based on the recipient's country or region.

1. On the **Select which groups to target** page, select **Specific groups**, and choose the groups and teams that you want to include in this policy, or select **All groups**.

   You can select up to 50 groups.

1. Select **Next**.

1. On the **Review and finish** page, confirm your settings and select **Finish**, and then select **Done**.

## After you set up the ownerless group policy

Notifications are sent weekly starting within 24 hours of policy creation. The audit log tracks notifications and responses.

If a user is part of multiple ownerless groups, they can receive separate weekly notifications, one for each group they're an active member of.

### When someone accepts or declines group ownership

Up to two members per group can accept the invitation to become an owner. Once someone accepts ownership, the policy stops sending notifications to the group's members.

If a member declines ownership, they stop receiving the weekly notifications.

If a member doesn't accept or decline ownership, they keep receiving the weekly notifications for the number of weeks specified in the policy.

### When no one accepts group ownership

After the notification period specified in the policy ends, the policy stops sending notifications. In this scenario, the ownerless groups policy takes no further action. Tenant admins need to find and [assign an owner for each ownerless group](https://learn.microsoft.com/en-us/admin/create-groups/add-or-remove-members-from-groups).

## See which groups are ownerless

Admins can see which Microsoft 365 groups remain ownerless by searching the [audit log](https://learn.microsoft.com/en-us/purview/audit-search#get-started-with-search) in the Microsoft Purview portal. To search for ownerless groups, follow these steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/).

1. Select the **Audit** solution card.

   If the **Audit** solution card isn't displayed, select **View all solutions**, and then select **Audit** in the **Core** section.

1. On the **Search** page, in the **Activities - friendly names** field, select **Unattended ownerless group** from the dropdown list.

1. Select the **Search** button.

## Auditing changes to ownerless group policy

To find details about changes to the ownerless group policy, search for the **Updated the ownerless group policy** activity. 

1. Sign in to the [Microsoft Purview portal](https://sip.purview.microsoft.com/audit/auditsearch) and start a new audit log search.

   > [!NOTE]
   > For help with Microsoft Purview authentication, see [Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-portal).

1. Under **Activities – friendly names**, type **ownerless group**, and select the **Updated the ownerless group policy** activity. 

1. Specify the start and end dates for the audit log search.

   

   When the search finishes, you see the following result. 
    
   
    
   The following example shows an audit log entry for changes made:
    
   

## Common issues with the ownerless group policy

- **Exchange Online throttles policy notifications.**
   - Because this policy sends notifications from one mailbox, Exchange Online can throttle the policy's notification emails if there are too many ownerless groups in your organization. Exchange Online mailboxes are limited to 10,000 sent emails per day.

- **The action buttons *Yes* and *No* aren't available in a forwarded notification email.**
   - If a member forwards their notification email to a different member, the forward recipient can't accept or decline the invitation.

- **Member can't see *Yes* and *No* in the notification email.**
   - Members should open notification emails in a separate window, not a preview pane. If the member views the notification in an email preview pane, they can't see the **Yes** and **No** options.
   - Make sure that the user principal name (UPN) and primary email address of the sender are the same. For information about how to update the UPN or primary email address of a user, see [Change a user name and email address](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/change-a-user-name-and-email-address). If they don't match, the recipient can't see the **Yes** and **No** options.

- **The policy for ownerless groups is configured, but group members don't receive notifications.**
   - This problem occurs if the specified sender in the policy doesn't have a user or group mailbox provisioned in Exchange Online. If the sender has a user or group mailbox, check the [audit log](https://learn.microsoft.com/en-us/purview/audit-get-started#step-3-search-the-audit-log) in the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149) to trace whether email notifications were sent.
   - Members who don't have a user mailbox provisioned in Exchange Online don't receive notifications.

## Related articles

- [Overview of Microsoft 365 Groups for administrators](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/office-365-groups)

- [Compare types of groups in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups)

- [Search the audit log in the Microsoft Purview portal](https://learn.microsoft.com/en-us/microsoft-365/compliance/search-the-audit-log-in-security-and-compliance)
