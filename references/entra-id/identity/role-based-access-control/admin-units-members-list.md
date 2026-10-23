# List users, groups, or devices in an administrative unit

> Source: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/admin-units-members-list  
> Microsoft doc last updated: 01/03/2025


In Microsoft Entra ID, you can list the users, groups, or devices in administrative units.

## Prerequisites

- Microsoft Entra ID P1 or P2 license for each administrative unit administrator
- Microsoft Entra ID Free licenses for administrative unit members
- [Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation) module when using PowerShell
- Admin consent when using Graph Explorer for Microsoft Graph API

For more information, see [Prerequisites to use PowerShell or Graph Explorer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites).

# [Admin center](#tab/admin-center)

You can list the users, groups, or devices in administrative units using the Microsoft Entra admin center.

### List the administrative units for a single user, group, or device

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **Entra ID**.

1. Browse to one of the following:

    - **Users** > **All users**
    - **Groups** > **All groups**
    - **Devices** > **All devices**

1. Select the user, group, or device you want to list their administrative units.

1. Select **Administrative units** to list all the administrative units where the user, group, or device is a member.

    

### List the users, groups, or devices for a single administrative unit

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **Entra ID** > **Roles & admins** > **Admin units**.

1. Select the administrative unit that you want to list the users, groups, or devices for.

1. Select one of the following:

    - **Users**
    - **Groups**
    - **Devices**

    

### List the devices for an administrative unit by using the All devices page

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **Entra ID** > **Devices** > **All devices**.

1. Select the filter for administrative unit.

1. Select the administrative unit whose devices you want to list.

    

### List the restricted management administrative units for a single user or group

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **Entra ID**.

1. Browse to one of the following:

    - **Users** > **All users**
    - **Groups** > **All groups**

1. Select the user or group you want to list their restricted management administrative units.

1. Select **Administrative units** to list all the administrative units where the user or group is a member.

1. In the **Restricted management** column, look for administrative units that are set to **Yes**.

    

# [PowerShell](#tab/ms-powershell)

Use the [Get-MgDirectoryAdministrativeUnit](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/get-mgdirectoryadministrativeunit) and [Get-MgDirectoryAdministrativeUnitMember](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/get-mgdirectoryadministrativeunitmember) commands to list users, groups, or devices for an administrative unit.

> [!NOTE]
> By default, [Get-MgDirectoryAdministrativeUnitMember](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/get-mgdirectoryadministrativeunitmember) returns only top members of an administrative unit. To retrieve all members, add the `-All:$true` parameter.

### List the administrative units for a user

```powershell
$userObj = Get-MgUser -Filter "UserPrincipalName eq 'bill@example.com'"
Get-MgDirectoryAdministrativeUnit | `
   where { Get-MgDirectoryAdministrativeUnitMember -AdministrativeUnitId $_.Id | `
   where {$_.Id -eq $userObj.Id} }
```

### List the administrative units for a group

```powershell
$groupObj = Get-MgGroup -Filter "DisplayName eq 'TestGroup'"
Get-MgDirectoryAdministrativeUnit | `
   where { Get-MgDirectoryAdministrativeUnitMember -AdministrativeUnitId $_.Id | `
   where {$_.Id -eq $groupObj.Id} }
```

### List the administrative units for a device

```powershell
$deviceObj = Get-MgDevice -Filter "DisplayName eq 'Test device'"
Get-MgDirectoryAdministrativeUnit | `
   where { Get-MgDirectoryAdministrativeUnitMember -AdministrativeUnitId $_.Id | `
   where {$_.Id -eq $deviceObj.Id} }
```

### List the users, groups, and devices for an administrative unit

```powershell
$adminUnitObj = Get-MgDirectoryAdministrativeUnit -Filter "DisplayName eq 'Test administrative unit 2'"
Get-MgDirectoryAdministrativeUnitMember -AdministrativeUnitId $adminUnitObj.Id
```

### List the groups for an administrative unit

```powershell
$adminUnitObj = Get-MgDirectoryAdministrativeUnit -Filter "DisplayName eq 'Test administrative unit 2'"
foreach ($member in (Get-MgDirectoryAdministrativeUnitMember -AdministrativeUnitId $adminUnitObj.Id)) 
{
    if($member.AdditionalProperties."@odata.type" -eq "#microsoft.graph.group")
    {
        Get-MgGroup -GroupId $member.Id
    }
}
```

### List the devices for an administrative unit

```powershell
$adminUnitObj = Get-MgDirectoryAdministrativeUnit -Filter "DisplayName eq 'Test administrative unit 2'"
foreach ($member in (Get-MgDirectoryAdministrativeUnitMember -AdministrativeUnitId $adminUnitObj.Id)) 
{
    if($member.AdditionalProperties.ObjectType -eq "Device")
    {
        Get-MgDevice -DeviceId $member.Id
    }
}
```

# [Graph API](#tab/ms-graph)

### List the administrative units for a user

Use the user [List memberOf](https://learn.microsoft.com/en-us/graph/api/user-list-memberof) API to list the administrative units a user is a direct member of.

```http
GET https://graph.microsoft.com/v1.0/users/{user-id}/memberOf/$/Microsoft.Graph.AdministrativeUnit
```

### List the administrative units for a group

Use the group [List memberOf](https://learn.microsoft.com/en-us/graph/api/group-list-memberof) API to list the administrative units a group is a direct member of.

```http
GET https://graph.microsoft.com/v1.0/groups/{group-id}/memberOf/$/Microsoft.Graph.AdministrativeUnit
```

### List the administrative units for a device

Use the [List device memberships](https://learn.microsoft.com/en-us/graph/api/device-list-memberof) API to list the administrative units a device is a direct member of.

```http
GET https://graph.microsoft.com/v1.0/devices/{device-id}/memberOf/$/Microsoft.Graph.AdministrativeUnit
```

### List the users, groups, or devices for an administrative unit

Use the [List members](https://learn.microsoft.com/en-us/graph/api/administrativeunit-list-members) API to list the users, groups, or devices for an administrative unit. For member type, specify `microsoft.graph.user`, `microsoft.graph.group`, or `microsoft.graph.device`.

```http
GET https://graph.microsoft.com/v1.0/directory/administrativeUnits/{admin-unit-id}/members/$/microsoft.graph.group
```

### List whether a single user is in a restricted management administrative unit

Use the [Get a user (beta)](https://learn.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&preserve-view=true) API to determine whether a user is in a restricted management administrative unit. Look at the value of the `isManagementRestricted` property. If the property is `true`, it is in a restricted management administrative unit. If the property is `false`, empty, or null, it is not in a restricted management administrative unit.

```http
GET https://graph.microsoft.com/beta/users/{user-id}
```

Response

```
{ 
  "displayName": "John",
  "isManagementRestricted": true,
  "userPrincipalName": "john@contoso.com", 
}
```

---

## Next steps

- [Add users, groups, or devices to an administrative unit](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/admin-units-members-add)
- [Assign Microsoft Entra roles with administrative unit scope](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal)
