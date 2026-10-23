# Delegate Azure role assignment management to others with conditions - Azure ABAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-portal  
> Microsoft doc last updated: 03/30/2026


As an administrator, you might get several requests to grant access to Azure resources that you want to delegate to someone else. You could assign a user the [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) roles, but these are highly privileged roles. This article describes a more secure way to [delegate role assignment management](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-overview) to other users in your organization, but add restrictions for those role assignments. For example, you can constrain the roles that can be assigned or constrain the principals the roles can be assigned to.

The following diagram shows how a delegate with conditions can only assign (or remove) the Backup Contributor or Backup Reader roles to only the Marketing or Sales groups.

## Prerequisites

To assign Azure roles, you must have:

- `Microsoft.Authorization/roleAssignments/write` permissions, such as [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator) or [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator)

## Step 1: Determine the permissions the delegate needs

To help determine the permissions the delegate needs, answer the following questions:

- What roles can the delegate assign?
- What role assignments can the delegate remove?
- What types of principals can the delegate assign roles to?
- Which principals can the delegate assign roles to?

Once you know the permissions that delegate needs, you use the following steps to add a condition to the delegate's role assignment. For example conditions, see [Examples to delegate Azure role assignment management with conditions](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-examples).

> [!NOTE]
> The conditions you add in these steps apply to assigning specific roles, but they also typically apply to removing role assignments for those same roles.

## Step 2: Start a new role assignment

1. Sign in to the [Azure portal](https://portal.azure.com).

1. Follow the steps to [open the Add role assignment page](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

1. On the **Roles** tab, select the **Privileged administrator roles** tab.

1. Select the **Role Based Access Control Administrator** role.

    The **Conditions** tab appears.

    You can select any role that includes the `Microsoft.Authorization/roleAssignments/write` or `Microsoft.Authorization/roleAssignments/delete` actions, such as [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator), but [Role Based Access Control Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator) has fewer permissions.

1. On the **Members** tab, find and select the delegate.

## Step 3: Add a condition

There are two ways that you can add a condition. You can use a condition template or you can use an advanced condition editor.

# [Template](#tab/template)

1. On the **Conditions** tab under **What user can do**, select the **Allow user to only assign selected roles to selected principals (fewer privileges)** option.

    

1. Select **Select roles and principals**.

    The Add role assignment condition page appears with a list of condition templates.

    

1. Select a condition template and then select **Configure**.

    | Condition template | Select this template to |
    | --- | --- |
    | [Constrain roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-examples#example-constrain-roles) | Allow user to only assign roles you select<br/>Allow user to only remove role assignments for the selected roles |
    | [Constrain roles and principal types](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-examples#example-constrain-roles-and-principal-types) | Allow user to only assign roles you select<br/>Allow user to only assign these roles to principal types you select (users, groups, or service principals)<br/>Allow user to only remove role assignments for the selected roles and principal types |
    | [Constrain roles and principals](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-examples#example-constrain-roles-and-specific-groups) | Allow user to only assign roles you select<br/>Allow user to only assign these roles to principals you select<br/>Allow user to only remove role assignments for the selected roles and principals |
    | Allow all except specific roles | Allow user to assign all roles except the roles you select<br/>Allow user to remove role assignments for all roles except the selected roles |

1. In the configure pane, add the required configurations.

    

1. Select **Save** to add the condition to the role assignment.

# [Condition editor](#tab/condition-editor)

If the condition templates don't work for your scenario or if you want more control, you can use the condition editor.

### Open condition editor

1. On the **Conditions** tab under **What user can do**, select the **Allow user to only assign selected roles to selected principals (fewer privileges)** option.

    

1. Select **Select roles and principals**.

    The Add role assignment condition page appears with a list of condition templates.

    

1. Select **Open advanced condition editor**.

    The Add role assignment condition page appears.

1. For the **Editor type** option, leave the default **Visual** selected.

### Add action

1. In the **Add action** section, select **Add action**.

    The Select an action pane appears. This pane is a filtered list of actions based on the role assignment that will be the target of your condition.

    

1. Select the **Create or update role assignments** action you want to allow if the condition is true.

    > [!TIP]
    > If you select both **Create or update role assignments** and **Delete a role assignment** actions, you won't be able add a condition expression. If you want to target both of these actions, you must add two conditions. For more information, see [Example: Constrain roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-examples#example-constrain-roles).

### Build expressions

1. In the **Build expression** section, select **Add expression**.

    Here is where you build the expression to constrain role assignments the delegate can add.

1. In the **Attribute source** list, select **Request**.

1. In the **Attribute** list, select one of the following attributes for the left side of the expression.

    - [Role definition ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#role-definition-id) is used to constrain the roles the delegate can assign.
    - [Principal ID](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-id) is used to constrain the specific principals the delegate can assign roles to.
    - [Principal type](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes#principal-type) is used to constrain the types of principals (users, groups, or service principals) that the delegate can assign roles to.

1. In the **Operator** list, select an operator.

    Depending on the attribute and the expression you want to build, you typically select these operators, which allow you to select one or more values for the right side of the expression.

    | Attribute | Common operator |
    | --- | --- |
    | **Role definition ID** | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues)<br/>[ForAnyOfAllValues:GuidNotEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofallvalues) |
    | **Principal ID** | [ForAnyOfAnyValues:GuidEquals](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |
    | **Principal type** | [ForAnyOfAnyValues:StringEqualsIgnoreCase](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-format#foranyofanyvalues) |

1. In the **Value** box, enter one or more values for the right side of the expression.

    

1. Add additional expressions as needed.

    > [!TIP]
    > When you add multiple expressions to delegate role assignment management with conditions, you typically use the **And** operator between expressions instead of the default **Or** operator.

1. Select **Save** to add the condition to the role assignment.

---

## Step 4: Assign role with condition to delegate

1. On the **Review + assign** tab, review the role assignment settings.

1. Select **Review + assign** to assign the role.

   After a few moments, the delegate is assigned the Role Based Access Control Administrator role with your role assignment conditions.

## Step 5: Delegate assigns roles with conditions

- Delegate can now follow steps to [assign roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

    

    When the delegate tries to assign roles in the Azure portal, the list of roles will be filtered to just show the roles they can assign.

    

    If there is a condition for principals, the list of principals available for assignment are also filtered.

    

    If the delegate attempts to assign a role that is outside the conditions using an API, the role assignment fails with an error. For more information, see [Symptom - Unable to assign a role](https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting#symptom---unable-to-assign-a-role).

## Edit a condition

There are two ways that you can edit a condition. You can use the condition template or you can use the condition editor.

1. In the Azure portal, open **Access control (IAM)** page for the role assignment that has a condition that you want to view, edit, or delete.

1. Select the **Role assignments** tab and find the role assignment.

1. In the **Condition** column, select **View/Edit**.

    If you don't see the **View/Edit** link, be sure you're looking at the same scope as the role assignment.

    

    The **Add role assignment condition** page appears. This page will look different depending on whether the condition matches an existing template.

1. If the condition matches an existing template, select **Configure** to edit the condition.
    
    

1. If the condition doesn't match an existing template, use the advanced condition editor to edit the condition.

    For example, to edit a condition, scroll down to the build expression section and update the attributes, operator, or values.

    

    To edit the condition directly, select the **Code** editor type and then edit the code for the condition.

    

1. When finished, click **Save** to update the condition. 

## Next steps

- [Delegate Azure access management to others](https://learn.microsoft.com/en-us/azure/role-based-access-control/delegate-role-assignments-overview)
- [Authorization actions and attributes](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-authorization-actions-attributes)
