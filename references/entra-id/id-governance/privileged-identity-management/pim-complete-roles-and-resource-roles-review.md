# Complete an access review of Azure resource and Microsoft Entra roles in PIM

> Source: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-complete-roles-and-resource-roles-review  
> Microsoft doc last updated: 04/23/2026


## Overview

Privileged Role Administrators can review privileged access once an [access review starts](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-create-roles-and-resource-roles-review). Privileged Identity Management (PIM) in Microsoft Entra ID automatically sends an email that prompts users to review their access. If a user doesn't receive an email, you can send them the instructions for [how to perform an access review](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-perform-roles-and-resource-roles-review).

Once the review has been created, follow the steps in this article to complete the review and see the results.

## Complete access reviews

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a user that is assigned to one or more prerequisite roles.

1. Browse to **ID Governance** > **Privileged Identity Management**. 

1. For **Microsoft Entra roles**, select **Microsoft Entra roles**. For **Azure resources**, select **Azure resources**.

1. Select the access review that you want to manage. Below is a sample screenshot of the **Review Access** overview for both **Azure resources** and **Microsoft Entra roles**.

    

On the detail page, the following options are available for managing the review of **Azure resources** and **Microsoft Entra roles**:

### Stop an access review

All access reviews have an end date, but you can use the **Stop** button to finish it early. The **Stop** button is only selectable when the review instance is active. You can't restart a review after it's been stopped.

### Reset an access review

When the review instance is active and at least one decision has been made by reviewers, you can reset the access review by selecting the **Reset** button to remove all decisions that were made on it. After you've reset an access review, all users are marked as not reviewed again.

### Apply an access review

After an access review is completed, either because you've reached the end date or stopped it manually, the **Apply** button removes denied users' access to the role. If a user's access was denied during the review, this is the step that removes their role assignment. If the **Auto apply** setting is configured on review creation, this button is always disabled because the review will be applied automatically instead of manually.

### Delete an access review

If you aren't interested in the review any further, delete it. To remove the access review from the Privileged Identity Management service, select the **Delete** button.

> [!IMPORTANT]
> You aren't required to confirm this destructive change, so verify that you want to delete that review.

## Results

On the **Results** page, you can view and download a list of your review results.

> [!NOTE]
> **Microsoft Entra roles** have a concept of role-assignable groups, where a group can be assigned to the role. When this happens, the group will show up in the review instead of expanding the members of the group, and a reviewer will either approve or deny the entire group.

> [!NOTE]
>If a group is assigned to **Azure resource roles**, the reviewer of the Azure resource role will see the expanded list of the users in a nested group. Should a reviewer deny a member of a nested group, that deny result won't be applied successfully because the user will not be removed from the nested group.

## Reviewers

On the **Reviewers** page, you can view and add reviewers to your existing access review. You can also remind reviewers to complete their reviews here.

> [!NOTE]
> If the reviewer type selected is user or group, you can add more users or groups as the primary reviewers at any point. You can also remove primary reviewers at any point. If the reviewer type is manager, you can add users or groups as the fallback reviewers to complete reviews on users who don't have managers. Fallback reviewers cannot be removed.

## Next steps

- [Create an access review of Azure resource and Microsoft Entra roles in PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-create-roles-and-resource-roles-review)
- [Perform an access review of Azure resource and Microsoft Entra roles in PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-perform-roles-and-resource-roles-review)
