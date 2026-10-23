# Turn off Basic Mobility and Security enforcement

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-turn-off  
> Microsoft doc last updated: 08/14/2025


You can't completely turn off or disable Basic Mobility and Security in your organization after you [enable](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-set-up) and [configure](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-policies-configure#create-policies-in-basic-mobility-and-security) it. But you can remove the enforcement of Basic Mobility and Security on devices in your organization by using either of the following methods:

- **Remove security group assignments from all Basic Mobility and Security policies**: This method works up to a certain point, because a policy must be assigned to at least one security group. You have the following options:
  - Create a new security group with no members and assign all policies to that group. For security group creation instructions, see [Create, edit, or delete a security group](https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-edit-or-delete-a-security-group).
  - Assign the policy to no one (select **We'll save this policy, but it won't be applied to any devices in your organization**).
- **Remove all Basic Mobility and Security policies**: This option works up to a certain point, because you can't remove the last remaining policy in the organization. You have the following options:
  - Create a new security group with no members and assign the last remaining policy to that group. For security group creation instructions, see [Create, edit, or delete a security group](https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-edit-or-delete-a-security-group).
  - Assign the last remaining policy to no one (select **We'll save this policy, but it won't be applied to any devices in your organization**).
  - Create a new policy with no restrictions assigned to no one or an empty security group, and then remove all other policies.

The rest of this article describes how to use these methods to effectively disable Basic Mobility and Security enforcement in an organization.

For more information about Basic Mobility and Security, see [Overview of Basic Mobility and Security in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview).

> [!IMPORTANT]
> Be aware of the effect on user devices when you turn off Basic Mobility and Security enforcement. For example, email profiles and cached email might be removed. For more information, see [What happens when you delete a policy or remove a user from a policy?](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-policies-configure#what-happens-when-you-delete-a-policy-or-remove-a-user-from-a-policy).

## What do you need to know before you begin?

- You open the **Basic Mobility and Security** page at <https://compliance.microsoft.com/basicmobilityandsecurity>.

- You need to be assigned permissions before you can do the procedures in this article. You have the following options:
  - [Microsoft Entra permissions](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal): Membership in the **Global Administrator**<sup>\*</sup> or **Compliance Administrator** roles gives users the required permissions _and_ permissions for other features in Microsoft 365.

    > [!IMPORTANT]
    > <sup>\*</sup> Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

- You can't use a delegated admin account to manage Basic Mobility and Security. For more information about delegated administration, see [Partners: Offer delegated administration](https://support.microsoft.com/office/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e).

- Questions? See the [Basic Mobility and Security FAQ](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview#basic-mobility-and-security-faq).

## Remove security group assignments from all Basic Mobility and Security policies

1. On the **Basic Mobility and Security** page at <https://compliance.microsoft.com/basicmobilityandsecurity>, select the **Policies** tab.

2. On the **Policies** tab, select a policy by clicking anywhere in the row other than the check box next to the name to open the details flyout for the policy.

3. In the details flyout, select **Edit deployment** in the **Deployment** section.

4. In the **Edit deployment** flyout that opens, make one of the following selections:
   - Remove any existing groups below the **Include these groups** box, start typing the name of the designated security group with no members in the box, and then select it when it appears.
   - Select **We'll save this policy, but it won't be applied to any devices in your organization**

   When you're finished on the **Edit deployment** flyout, select **Save**.

5. Back on the details flyout, select **Close**.

Repeat these steps as many times as necessary.

## Remove all Basic Mobility and Security policies

1. On the **Basic Mobility and Security** page at <https://compliance.microsoft.com/basicmobilityandsecurity>, select the **Policies** tab.

2. On the **Policies** tab, select the policy to remove by selecting the check box next to the name.

3. Select  **More actions** \> **Delete selected policies**.

4. Select **Yes** in the warning dialog that opens.

5. Repeat the previous steps until only one policy remains, then do one of the following steps:
   - Create a new policy with no restrictions assigned to no one or an empty security group. After you create this policy, remove the last remaining "real" policy. For policy creation instructions, see [Create policies in Basic Mobility and Security](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-policies-configure#create-policies-in-basic-mobility-and-security).
   - Assign the last remaining policy to no one or an empty security group as described in the [Remove security group assignments from all Basic Mobility and Security device policies](#remove-security-group-assignments-from-all-basic-mobility-and-security-policies) section.
