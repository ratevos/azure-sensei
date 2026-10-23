# Group naming policy quickstart

> Source: https://learn.microsoft.com/en-us/entra/identity/users/groups-quickstart-naming-policy  
> Microsoft doc last updated: 12/16/2024


## Overview

In this quickstart, in Microsoft Entra ID, part of Microsoft Entra, you set up naming policy in your Microsoft Entra organization for user-created Microsoft 365 groups, to help you sort and search your groups. For example, you could use the naming policy to:

* Communicate the function of a group, membership, geographic region, or who created the group.
* Help categorize groups in the address book.
* Block specific words from being used in group names and aliases.

If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

## Configure the group naming policy

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator).
1. Select **Microsoft Entra ID**.
1. Select **Groups** > **All groups**, then select **Naming policy** to open the **Naming policy** page.

    

### View or edit the Prefix-suffix naming policy

1. On the **Naming policy** page, select **Group naming policy**.
1. You can view or edit the current prefix or suffix naming policies individually by selecting the attributes or strings you want to enforce as part of the naming policy.
1. To remove a prefix or suffix from the list, select the prefix or suffix, then select **Delete**. Multiple items can be deleted at the same time.
1. Select **Save** for your changes to the policy to go into effect.

### View or edit the custom blocked words

1. On the **Naming policy** page, select **Blocked words**.

    

1. View or edit the current list of custom blocked words by selecting **Download**.
1. Upload the new list of custom blocked words by selecting the file icon.
1. Select **Save** for your changes to the policy to go into effect.

That's it. You've set up your naming policy and added your custom blocked words.

## Clean up resources

To remove the naming policy, use the following steps.

### Remove the naming policy

1. On the **Naming policy** page, select **Delete policy**.
1. After you confirm the deletion, the naming policy is removed, including all prefix-suffix naming policy and any custom blocked words.

## Next steps

Advance to the next article for more information including the PowerShell cmdlets for naming policy, technical constraints, adding a list of custom blocked words, and the end user experiences across Microsoft 365 apps.

> [Naming policy PowerShell](https://learn.microsoft.com/en-us/entra/identity/users/groups-naming-policy)
