# Validate rules for dynamic membership groups

> Source: https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-rule-validation  
> Microsoft doc last updated: 12/19/2024


## Overview

Microsoft Entra ID provides the means to validate rules for dynamic membership groups. On the **Validate rules** tab, you can validate a rule against sample group members to confirm that the rule is working as expected.

When you create or update rules for dynamic membership groups, you want to know whether a user or a device is a member of the group. This knowledge helps you evaluate whether a user or device meets the rule criteria. It also helps you troubleshoot when membership isn't expected.

## Prerequisites

To evaluate the rule for dynamic membership groups, the administrator must be at least a [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator).

> [!WARNING]
> Assigning one of the required roles via indirect role assignment isn't supported.

## Validate a rule for dynamic membership groups

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a Groups Administrator.

1. Browse to **Entra ID** > **Groups** > **All groups**.

1. Select an existing dynamic group or create a new dynamic group, and then select **Dynamic membership rules**.

    

1. On the **Validate Rules** tab, select users to validate their memberships. You can select 20 users or devices at one time.

    

1. After you finish selecting users or devices, choose **Select**. Validation automatically starts. The validation results show whether a user is a member of the group or not.

    

1. If the rule isn't valid or if there's a network problem, the results show **Unknown**. If the value is **Unknown**, select **View details**. The detailed error message describes the problem and the necessary actions.

    

1. You can modify the rule to trigger a new validation of memberships. To see why a user isn't a member of the group, select **View details**. Verification details show the result of each expression that composes the rule. Select **OK** to close the details.

## Related content

- [Manage rules for dynamic membership groups in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-membership)
