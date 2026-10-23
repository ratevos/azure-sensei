# Remove users, groups, or devices from an administrative unit

> Source: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/admin-units-members-remove  
> Microsoft doc last updated: 01/03/2025


When users, groups, or devices in an administrative unit no longer need access, you can remove them.

## Prerequisites

- Microsoft Entra ID P1 or P2 license for each administrative unit administrator
- Microsoft Entra ID Free licenses for administrative unit members
- Privileged Role Administrator
- [Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation) module when using PowerShell
- Admin consent when using Graph Explorer for Microsoft Graph API

For more information, see [Prerequisites to use PowerShell or Graph Explorer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites).

# [Admin center](#tab/admin-center)

You can remove users, groups, or devices from administrative units individually using the Microsoft Entra admin center. You can also remove users in a bulk operation.

### Remove a single user, group, or device from administrative units

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1. Browse to **Entra ID**.

1. Browse to one of the following:

    - **Users** > **All users**
    - **Groups** > **All groups**
    - **Devices** > **All devices**

1. Select the user, group, or device you want to remove from an administrative unit.

1. Select **Administrative units**.

1. Add check marks next to the administrative units you want to remove the user, group, or device from.

1. Select **Remove from administrative unit**.

    

### Remove users, groups, or devices from a single administrative unit

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1. Browse to **Entra ID** > **Roles & admins** > **Admin units**.

1. Select the administrative unit that you want to remove users, groups, or devices from.

1. Select one of the following:

    - **Users**
    - **Groups**
    - **Devices**

1. Add check marks next to the users, groups, or devices you want to remove.

1. Select **Remove member**, **Remove**, or **Remove device**.

    

### Remove users from an administrative unit in a bulk operation

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1. Browse to **Entra ID** > **Roles & admins** > **Admin units**.

1. Select the administrative unit that you want to remove users from.

1. Select **Users** > **Bulk operations** > **Bulk remove members**.

    

1. In the **Bulk remove members** pane, download the comma-separated values (CSV) template.

1. Edit the downloaded CSV template with the list of users you want to remove.

    Add one user principal name (UPN) in each row. Don't remove the first two rows of the template.

1. Save your changes and upload the CSV file.

1. Select **Submit**.

# [PowerShell](#tab/ms-powershell)

Use the [Remove-MgDirectoryAdministrativeUnitMemberByRef](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/remove-mgdirectoryadministrativeunitmemberbyref) command to remove users, groups, or devices from an administrative unit.

### Remove users from an administrative unit

```powershell
$adminUnitObj = Get-MgDirectoryAdministrativeUnit -Filter "DisplayName eq 'Test administrative unit 2'"
$userObj = Get-MgUser -Filter "UserPrincipalName eq 'bill@example.com'"
Remove-MgDirectoryAdministrativeUnitMemberByRef -AdministrativeUnitId $adminUnitObj.Id -DirectoryObjectId $userObj.Id
```

### Remove groups from an administrative unit

```powershell
$adminUnitObj = Get-MgDirectoryAdministrativeUnit -Filter "DisplayName eq 'Test administrative unit 2'"
$groupObj = Get-MgGroup -Filter "DisplayName eq 'TestGroup'"
Remove-MgDirectoryAdministrativeUnitMemberByRef -AdministrativeUnitId $adminUnitObj.Id -DirectoryObjectId $groupObj.Id
```

### Remove devices from an administrative unit

```powershell
Remove-MgDirectoryAdministrativeUnitMemberByRef -AdministrativeUnitId $adminUnitObj.Id -DirectoryObjectId $deviceObj.Id
```

# [Graph API](#tab/ms-graph)

Use the [Remove a member](https://learn.microsoft.com/en-us/graph/api/administrativeunit-delete-members) API to remove users, groups, or devices from an administrative unit. For `{member-id}`, specify the user, group, or device ID.

```http
DELETE https://graph.microsoft.com/v1.0/directory/administrativeUnits/{admin-unit-id}/members/{member-id}/$ref
```

---

## Next steps

- [Add users, groups, or devices to an administrative unit](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/admin-units-members-add)
- [Assign Microsoft Entra roles with administrative unit scope](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal)
