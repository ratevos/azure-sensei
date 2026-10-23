# Activate your group membership or ownership in Privileged Identity Management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-activate-roles  
> Microsoft doc last updated: 04/23/2026


## Overview

You can use Privileged Identity Management (PIM) in Microsoft Entra ID to have just-in-time membership in the group or just-in-time ownership of the group.

This article is for eligible members or owners who want to activate their group membership or ownership in PIM.

> [!IMPORTANT]
> When a group membership or ownership is activated, Microsoft Entra PIM temporarily adds an active assignment. Microsoft Entra PIM creates an active assignment (adds user as member or owner of the group) within seconds. When deactivation (manual or through activation time expiration) happens, Microsoft Entra PIM removes the user’s group membership or ownership within seconds as well.
>
> An application might provide access to users based on their group membership. In some situations, application access might not immediately reflect the fact that user was added to the group or removed from it. If application previously cached the fact that user isn't member of the group – when user tries to access application again, access might not be provided. Similarly, if application previously cached the fact that user is member of the group – when group membership is deactivated, user might still get access. Specific situation depends on the application’s architecture. For some applications, signing out and signing back in might help to get access added or removed.

## PIM for Groups and ownership deactivation

## Activate a role

When you need to take on a group membership or ownership, you can request activation by using the **My roles** navigation option in PIM.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **ID Governance** > **Privileged Identity Management** > **My roles** > **Groups**. 
    > [!NOTE]
    > You might also use this [short link](https://aka.ms/pim) to open the **My roles** page directly.

1. In the **Eligible assignments** blade, review the list of groups that you have eligible membership or ownership for.

    

1. Select **Activate** for the eligible assignment you want to activate.

1. Depending on the group’s setting, you might be asked to provide multifactor authentication or another form of credential.

1. If necessary, specify a custom activation start time. The membership or ownership activates only after the selected time.

1. Depending on the group’s setting, justification for activation might be required. If needed, provide the justification in the **Reason** box.

    

1. Select **Activate**.

If the [role requires approval](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-approval-workflow) to activate, an Azure notification appears in the upper right corner of your browser informing you the request is pending approval.

## View the status of your requests

You can view the status of your pending requests to activate. It's important when your requests undergo approval of another person.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **ID Governance** > **Privileged Identity Management** > **My requests** > **Groups**. 

1. Review the list of requests.

    

## Cancel a pending request

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **ID Governance** > **Privileged Identity Management** > **My requests** > **Groups**. 

    

1. For the request that you want to cancel, select **Cancel**.

When you select **Cancel**, the request is canceled. To activate the role again, you have to submit a new request for activation.

## Next steps

- [Approve activation requests for group members and owners](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-approval-workflow)
