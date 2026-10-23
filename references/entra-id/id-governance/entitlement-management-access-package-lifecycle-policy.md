# Change lifecycle settings for an access package in entitlement management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-lifecycle-policy  
> Microsoft doc last updated: 06/26/2025


As an access package manager, you can change the lifecycle settings for assignments in an access package at any time by editing an existing policy. If you change the expiration date for assignments on a policy, the expiration date for requests that are already in a pending approval or approved state won't change.

This article describes how to change the lifecycle settings for an existing access package assignment policy.

## Open requestor information
To ensure identities have the right access to an access package, custom questions can be configured to ask identities requesting access to certain access packages. Configuration options include: localization, required/optional, and text/multiple choice answer formats. Requestors  see the questions when they request the package and approvers see the answers to the questions to help them make their decision. Use the following steps to configure questions in an access package:

## Open lifecycle settings

To change the lifecycle settings for an access package, you need to open the corresponding policy. Follow these steps to open the lifecycle settings for an access package.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
    > [!TIP]
    > Other least privilege roles that can complete this task include the Catalog owner and the Access package manager.
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. On the Access packages page, open the access package that you want to edit.

1. Select **Policies** and then select the policy that has the lifecycle settings you want to edit.

    The Policy details pane opens at the bottom of the page.

    

1. Select **Edit** to edit the policy.

    

1. Select the **Lifecycle** tab to open the lifecycle settings.

## Specify a lifecycle

On the **Lifecycle** tab, you specify when an identity's assignment to the access package expires. You can also specify whether identities can extend their assignments.

1. In the **Expiration** section, set **Access package assignments expire** to **On date**, **Number of days**, **Number of hours**, or **Never**.

    - For **On date**, select an expiration date in the future.
    - For **Number of days**, specify a number from 0 to 3660 days.
    - For **Number of hours**, specify how many hours.

    Based on your selection, a user's assignment to the access package expires on a certain date, some days after they're approved, or never.

1. If you want the user to request a specific start and end date for their access, select **Yes** for the **Users can request specific timeline** toggle.

1. Select **Show advanced expiration settings** to show more settings.

    

1. To allow the user to extend their assignments, set **Allow users to extend access** to **Yes**.

    If extensions are allowed in the policy, the user receives an email 14 days before, and then one day before, their access package assignment is set to expire. The email prompts the user to extend the assignment. The user must still be in the scope of the policy at the time that they request an extension.

    Also, if the policy has an explicit end date for assignments, and a user submits a request to extend access, the extension date in the request must be at or before when assignments expire. The policy that you used to grant the user access to the access package defines whether the extension date is at or before the assignment expiration. For example, if the policy indicates that assignments are set to expire on June 30, the maximum extension that a user can request is June 30.

    If a user's access is extended, they won't be able to request the access package after the specified extension date (the date set in the time zone of the user who created the policy).

1. To require approval to grant an extension, set **Require approval to grant extension** to **Yes**.

    This approval will use the same approval settings that you specified on the **Requests** tab.

1. If you want to **Require an access review** for this access package, move the toggle to **Yes**. Refer to the [detailed article on configuring the access review](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-reviews-create) and then return back here to finish setting up the access package.
  
3. If you didn't require an access review, or once you have configured it, select **Next** or **Update**.

## Next steps

- [Change request and approval settings for an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy)
