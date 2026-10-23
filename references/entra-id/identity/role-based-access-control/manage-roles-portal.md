# Assign Microsoft Entra roles

> Source: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal  
> Microsoft doc last updated: 06/04/2025


This article describes how to assign Microsoft Entra roles to users and groups using the Microsoft Entra admin center, Microsoft Graph PowerShell, or Microsoft Graph API. It also describes how to assign roles at different scopes, such as tenant, application registration, and administrative unit scopes.

You can assign both direct and indirect role assignments to a user. If a user is assigned a role by a group membership, add the user to the group to add the role assignment. For more information, see [Use Microsoft Entra groups to manage role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/groups-concept).

In Microsoft Entra ID, roles are typically assigned to apply to the entire tenant. However, you can also assign Microsoft Entra roles for different resources, such as application registrations or administrative units. For example, you could assign the Helpdesk Administrator role so that it just applies to a particular administrative unit and not the entire tenant. The resources that a role assignment applies to is also called the scope. Restricting the scope of a role assignment is supported for built-in and custom roles. For more information about scope, see [Overview of role-based access control (RBAC) in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-overview#scope).

## Microsoft Entra roles in PIM

If you have a Microsoft Entra ID P2 license and [Privileged Identity Management (PIM)](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure), you have additional capabilities when assigning roles, such as making a user eligible for a role assignment or defining the start and end time for a role assignment. For information about assigning Microsoft Entra roles in PIM, see these articles:

| Method | Information |
| --- | --- |
| Microsoft Entra admin center | [Assign Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user) |
| Microsoft Graph PowerShell | [Tutorial: Assign Microsoft Entra roles in Privileged Identity Management using Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/tutorial-pim) |
| Microsoft Graph API | [Manage Microsoft Entra role assignments using PIM APIs](https://learn.microsoft.com/en-us/graph/api/resources/privilegedidentitymanagementv3-overview)<br/>[Assign Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user#assign-a-role-using-microsoft-graph-api) |

## Prerequisites

- Privileged Role Administrator
- [Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation) module when using PowerShell
- Admin consent when using Graph Explorer for Microsoft Graph API

For more information, see [Prerequisites to use PowerShell or Graph Explorer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites).

## Assign roles with tenant scope

This section describes how to assign roles at tenant scope.

# [Admin center](#tab/admin-center)

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1. Browse to **Identity** > **Roles & admins**.

    

1. Select a role name to open the role. Don't add a check mark next to the role.

    

1. Select **Add assignments** and then select the users, groups, or agent identities you want to assign to this role.

    Only role-assignable groups are displayed. If a group isn't listed, you'll need to create a role-assignable group. For more information, see [Create a role-assignable group in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/groups-create-eligible).

    For a list of roles that you can assign to agent identities, see [Authorization in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/identity-professional/authorization-agent-id).

    If your experience is different than the following screenshot, you might have Microsoft Entra ID P2 and PIM. For more information, see [Assign Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user).

    

1. Select **Add** to assign the role.

# [PowerShell](#tab/ms-powershell)

Follow these steps to assign Microsoft Entra roles using PowerShell.

1. Open a PowerShell window. If necessary, use [Install-Module](https://learn.microsoft.com/en-us/powershell/module/powershellget/install-module) to install Microsoft Graph PowerShell. For more information, see [Prerequisites to use PowerShell or Graph Explorer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites).

    ```powershell
    Install-Module Microsoft.Graph -Scope CurrentUser
    ```

1. In a PowerShell window, use [Connect-MgGraph](https://learn.microsoft.com/en-us/powershell/microsoftgraph/authentication-commands#using-connect-mggraph) to sign in to your tenant.

    ```powershell
    Connect-MgGraph -Scopes "RoleManagement.ReadWrite.Directory"
    ```

1. Use [Get-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/get-mguser) to get the user.

    ```powershell
    $user = Get-MgUser -Filter "userPrincipalName eq 'alice@contoso.com'"
    ```

    Use [Get-MgGroup](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.groups/get-mggroup) to get the role-assignable group.

    ```powershell
    $group = Get-MgGroup -Filter "DisplayName eq 'Contoso Helpdesk'"
    ```

1. Use [Get-MgRoleManagementDirectoryRoleDefinition](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.governance/get-mgrolemanagementdirectoryroledefinition) to get the role you want to assign.

    To see the list of role definition IDs for all built-in roles, see [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

    ```powershell
    $roleDefinition = Get-MgRoleManagementDirectoryRoleDefinition -Filter "displayName eq 'Billing Administrator'"
    ```

1. Set tenant as scope of role assignment.

    ```powershell
    $directoryScope = '/'
    ```

1. Use [New-MgRoleManagementDirectoryRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.governance/new-mgrolemanagementdirectoryroleassignment) to assign the role.

    ```powershell
    $roleAssignment = New-MgRoleManagementDirectoryRoleAssignment `
       -DirectoryScopeId $directoryScope -PrincipalId $user.Id `
       -RoleDefinitionId $roleDefinition.Id
    ```

    ```powershell
    $roleAssignment = New-MgRoleManagementDirectoryRoleAssignment `
        -DirectoryScopeId $directoryScope -PrincipalId $group.Id `
        -RoleDefinitionId $roleDefinition.Id
    ```

    Here's another way that you can assign a role.

    ```powershell
    $params = @{
       "directoryScopeId" = "/" 
       "principalId" = $group.Id
       "roleDefinitionId" = $roleDefinition.Id
    }
    $roleAssignment = New-MgRoleManagementDirectoryRoleAssignment -BodyParameter $params
    ```

# [Graph API](#tab/ms-graph)

Follow these instructions to assign a role using the Microsoft Graph API in [Graph Explorer](https://aka.ms/ge).

1. Sign in to the [Graph Explorer](https://aka.ms/ge).

1. Use [List users](https://learn.microsoft.com/en-us/graph/api/user-list) API to get the user.

    ```http
    GET https://graph.microsoft.com/v1.0/users?$filter=userPrincipalName eq 'alice@contoso.com'
    ```

    Use [List groups](https://learn.microsoft.com/en-us/graph/api/group-list) API to get the role-assignable group.

    ```http
    GET https://graph.microsoft.com/v1.0/groups?$filter=displayName eq 'Contoso Helpdesk'
    ```

1. Use the [List unifiedRoleDefinitions](https://learn.microsoft.com/en-us/graph/api/rbacapplication-list-roledefinitions) API to get the role you want to assign.

    To see the list of role definition IDs for all built-in roles, see [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

    ```http
    GET https://graph.microsoft.com/v1.0/rolemanagement/directory/roleDefinitions?$filter=displayName eq 'Billing Administrator'
    ```

1. Use the [Create unifiedRoleAssignment](https://learn.microsoft.com/en-us/graph/api/rbacapplication-post-roleassignments) API to assign the role.

    ```http
    POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments
    {
        "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
        "principalId": "<Object ID of user or group>",
        "roleDefinitionId": "<ID of role definition>",
        "directoryScopeId": "/"
    }
    ```

    Response
    
    ```http
    HTTP/1.1 201 Created
    Content-type: application/json
    {
        "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignments/$entity",
        "id": "<Role assignment ID>",
        "roleDefinitionId": "<ID of role definition>",
        "principalId": "<Object ID of user or group>",
        "directoryScopeId": "/"
    }
    ```
    
    If the principal or role definition doesn't exist, the response is not found.
    
    Response
    
    ```http
    HTTP/1.1 404 Not Found
    ```

---

## Assign roles with app registration scope

Built-in roles and custom roles are assigned by default at tenant scope to grant access permissions over all app registrations in your organization. Additionally, custom roles and some relevant built-in roles (depending on the type of Microsoft Entra resource) can also be assigned at the scope of a single Microsoft Entra resource. This allows you to give the user the permission to update credentials and basic properties of a single app without having to create a second custom role.

This section describes how to assign roles at an application registration scope.

# [Admin center](#tab/admin-center)

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Application Developer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-developer).

1. Browse to **Entra ID** > **App registrations**.

1. Select an application. You can use search box to find the desired app.

    You might have to select **All applications** to see the complete list of app registrations in your tenant.

    

1. Select **Roles and administrators** from the left navigation menu to see the list of all roles available to be assigned over the app registration.
    
    

1. Select the desired role.

    > [!TIP]
    > You won't see the entire list of Microsoft Entra built-in or custom roles here. This is expected. We show the roles which have permissions related to managing app registrations only.

1. Select **Add assignments** and then select the users or groups you want to assign this role to.

    

1. Select **Add** to assign the role scoped over the app registration.

# [PowerShell](#tab/ms-powershell)

Follow these steps to assign Microsoft Entra roles at application scope using PowerShell.

1. Open a PowerShell window. If necessary, use [Install-Module](https://learn.microsoft.com/en-us/powershell/module/powershellget/install-module) to install Microsoft Graph PowerShell. For more information, see [Prerequisites to use PowerShell or Graph Explorer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites).

    ```powershell
    Install-Module Microsoft.Graph -Scope CurrentUser
    ```

1. In a PowerShell window, use [Connect-MgGraph](https://learn.microsoft.com/en-us/powershell/microsoftgraph/authentication-commands#using-connect-mggraph) to sign in to your tenant.

    ```powershell
    Connect-MgGraph -Scopes "Application.Read.All","RoleManagement.Read.Directory","User.Read.All","RoleManagement.ReadWrite.Directory"
    ```

1. Use [Get-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/get-mguser) to get the user.

    ```powershell
    $user = Get-MgUser -Filter "userPrincipalName eq 'alice@contoso.com'"
    ```

    To assign the role to a service principal instead of a user, use the [Get-MgServicePrincipal](https://learn.microsoft.com/en-us/powershell/module/Microsoft.Graph.Applications/Get-MgServicePrincipal) command.

1. Use [Get-MgRoleManagementDirectoryRoleDefinition](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.governance/get-mgrolemanagementdirectoryroledefinition) to get the role you want to assign.

    ```powershell
    $roleDefinition = Get-MgRoleManagementDirectoryRoleDefinition `
       -Filter "displayName eq 'Application Administrator'"
    ```

1. Use [Get-MgApplication](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.applications/get-mgapplication) to get the app registration you want the role assignment to be scoped to.

    ```powershell
    $appRegistration = Get-MgApplication -Filter "displayName eq 'f/128 Filter Photos'"
    $directoryScope = '/' + $appRegistration.Id
    ```

1. Use [New-MgRoleManagementDirectoryRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.governance/new-mgrolemanagementdirectoryroleassignment) to assign the role.

    ```powershell
    $roleAssignment = New-MgRoleManagementDirectoryRoleAssignment `
       -DirectoryScopeId $directoryScope -PrincipalId $user.Id `
       -RoleDefinitionId $roleDefinition.Id 
    ```

# [Graph API](#tab/ms-graph)

Follow these instructions to assign a role at application scope using the Microsoft Graph API in [Graph Explorer](https://aka.ms/ge).

1. Sign in to the [Graph Explorer](https://aka.ms/ge).

1. Use [List users](https://learn.microsoft.com/en-us/graph/api/user-list) API to get the user.

    ```http
    GET https://graph.microsoft.com/v1.0/users?$filter=userPrincipalName eq 'alice@contoso.com'
    ```

1. Use the [List unifiedRoleDefinitions](https://learn.microsoft.com/en-us/graph/api/rbacapplication-list-roledefinitions) API to get the role you want to assign.

    ```http
    GET https://graph.microsoft.com/v1.0/rolemanagement/directory/roleDefinitions?$filter=displayName eq 'Application Administrator'
    ```

1. Use the [List applications](https://learn.microsoft.com/en-us/graph/api/application-list) API to get the application you want the role assignment to be scoped to.

    ```http
    GET https://graph.microsoft.com/v1.0/applications?$filter=displayName eq 'f/128 Filter Photos'
    ```

1. Use the [Create unifiedRoleAssignment](https://learn.microsoft.com/en-us/graph/api/rbacapplication-post-roleassignments) API to assign the role.

    ```http
    POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments

    {
        "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
        "principalId": "<Object ID of user>",
        "roleDefinitionId": "<ID of role definition>",
        "directoryScopeId": "/<Object ID of app registration>"
    }
    ```

    Response
    
    ```http
    HTTP/1.1 201 Created
    ```

    > [!NOTE]
    > In this example, `directoryScopeId` is specified as `/<ID>`, unlike the administrative unit section. It is by design. The scope of `/<ID>` means the principal can manage that Microsoft Entra object. The scope `/administrativeUnits/<ID>` means the principal can manage the members of the administrative unit (based on the role the principal is assigned), not the administrative unit itself.

---

## Assign roles with administrative unit scope

In Microsoft Entra ID, for more granular administrative control, you can assign a Microsoft Entra role with a scope that's limited to one or more [administrative units](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units). When a Microsoft Entra role is assigned at the scope of an administrative unit, role permissions apply only when managing members of the administrative unit itself, and don't apply to tenant-wide settings or configurations.

For example, an administrator who is assigned the Groups Administrator role at the scope of an administrative unit can manage groups that are members of the administrative unit, but they can't manage other groups in the tenant. They also can't manage tenant-level settings related to groups, such as expiration or group naming policies.

This section describes how to assign Microsoft Entra roles with administrative unit scope.

### Prerequisites

- Microsoft Entra ID P1 or P2 license for each administrative unit administrator
- Microsoft Entra ID Free licenses for administrative unit members
- Privileged Role Administrator
- Microsoft Graph PowerShell module when using PowerShell
- Admin consent when using Graph Explorer for Microsoft Graph API

For more information, see [Prerequisites to use PowerShell or Graph Explorer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites).

### Roles that can be assigned with administrative unit scope

The following Microsoft Entra roles can be assigned with administrative unit scope. Additionally, any [custom role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create) can be assigned with administrative unit scope as long as the custom role's permissions include at least one permission relevant to users, groups, or devices.

| Role | Description |
| -----| ----------- |
| [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) | Has access to view, set, and reset authentication method information for any non-admin user in the assigned administrative unit only. |
| [Attribute Assignment Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-administrator) | Can read and update custom security attribute assignments (from any attribute set) for users or service principals within the administrative unit only. |
| [Attribute Assignment Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-reader) | Can read custom security attributes (from any attribute set) for users or service principals within the administrative unit only. |
| [Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator) | Limited access to manage devices in Microsoft Entra ID. |
| [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) | Can manage all aspects of groups in the assigned administrative unit only. |
| [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) | Can reset passwords for non-administrators in the assigned administrative unit only. |
| [License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) | Can assign, remove, and update license assignments within the administrative unit only. |
| [Password Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#password-administrator) | Can reset passwords for non-administrators within the assigned administrative unit only. |
| [Printer Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#printer-administrator) | Can manage printers and printer connectors. For more information, see [Delegate administration of printers in Universal Print](https://learn.microsoft.com/en-us/universal-print/portal/delegated-admin#scoped-admin-vs-tenant-printer-admin). |
| [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) | Can access to view, set and reset authentication method information for any user (admin or non-admin). |
| [SharePoint Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator) | Can manage Microsoft 365 groups in the assigned administrative unit only. For SharePoint sites associated with Microsoft 365 groups in an administrative unit, can also update site properties (site name, URL, and external sharing policy) using the Microsoft 365 admin center. Cannot use the SharePoint admin center or SharePoint APIs to manage sites. |
| [Teams Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator) | Can manage Microsoft 365 groups in the assigned administrative unit only. Can manage team members in the Microsoft 365 admin center for teams associated with groups in the assigned administrative unit only. Cannot use the Teams admin center. |
| [Teams Devices Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#teams-devices-administrator) | Can perform management related tasks on Teams certified devices. |
| [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) | Can manage all aspects of users and groups, including resetting passwords for limited admins within the assigned administrative unit only. Cannot currently manage users' profile photographs. |
| [&lt;Custom role&gt;](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create) | Can perform actions that apply to users, groups, or devices, according to the definition of the custom role. |

Certain role permissions apply only to nonadministrator users when assigned with the scope of an administrative unit. In other words, administrative unit scoped [Helpdesk Administrators](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) can reset passwords for users in the administrative unit only if those users don't have administrator roles. The following permissions are restricted when the target of an action is a user with another role or an administrator:

- Read and modify user authentication methods
- Reset user passwords
- Modify sensitive user properties such as telephone numbers, alternate email addresses, or Open Authorization (OAuth) secret keys
- Delete or restore user accounts

### Security principals that can be assigned with administrative unit scope

The following security principals can be assigned to a role with an administrative unit scope:

- Users
- Microsoft Entra role-assignable groups
- Service principals

### Service principals and guest users

Service principals and guest users won't be able to use a role assignment scoped to an administrative unit unless they're also assigned corresponding permissions to read the objects. This is because service principals and guest users don't receive directory read permissions by default, which are required to perform administrative actions. To enable a service principal or guest user to use a role assignment scoped to an administrative unit, you must assign the [Directory Readers](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#directory-readers) role (or another role that includes read permissions) at a tenant scope.

It isn't currently possible to assign directory read permissions scoped to an administrative unit. For more information about default permissions for users, see [default user permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions). 

### Assign roles with administrative unit scope

This section describes how to assign roles at administrative unit scope.

# [Admin center](#tab/admin-center)

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1. Browse to **Entra ID** > **Roles & admins** > **Admin units**.

1. Select an administrative unit.

    

1. Select **Roles and administrators** from the left navigation menu to see the list of all roles available to be assigned over an administrative unit.
    
    

1. Select the desired role.

    > [!TIP]
    > You won't see the entire list of Microsoft Entra built-in or custom roles here. This is expected. We show the roles which have permissions related to the objects that are supported within the administrative unit. To see the list of objects supported within an administrative unit, see [Administrative units in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units).

1. Select **Add assignments** and then select the users or groups you want to assign this role to.

1. Select **Add** to assign the role scoped over the administrative unit.

# [PowerShell](#tab/ms-powershell)

Follow these steps to assign Microsoft Entra roles at administrative unit scope using PowerShell.

1. Open a PowerShell window. If necessary, use [Install-Module](https://learn.microsoft.com/en-us/powershell/module/powershellget/install-module) to install Microsoft Graph PowerShell. For more information, see [Prerequisites to use PowerShell or Graph Explorer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites).

    ```powershell
    Install-Module Microsoft.Graph -Scope CurrentUser
    ```

1. In a PowerShell window, use [Connect-MgGraph](https://learn.microsoft.com/en-us/powershell/microsoftgraph/authentication-commands#using-connect-mggraph) to sign in to your tenant.

    ```powershell
    Connect-MgGraph -Scopes "Directory.Read.All","RoleManagement.Read.Directory","User.Read.All","RoleManagement.ReadWrite.Directory"
    ```

1. Use [Get-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/get-mguser) to get the user.

    ```powershell
    $user = Get-MgUser -Filter "userPrincipalName eq 'alice@contoso.com'"
    ```

1. Use [Get-MgRoleManagementDirectoryRoleDefinition](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.governance/get-mgrolemanagementdirectoryroledefinition) to get the role you want to assign.

    ```powershell
    $roleDefinition = Get-MgRoleManagementDirectoryRoleDefinition `
       -Filter "displayName eq 'User Administrator'"
    ```

1. Use [Get-MgDirectoryAdministrativeUnit](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.directorymanagement/get-mgdirectoryadministrativeunit) to get the administrative unit you want the role assignment to be scoped to.

    ```powershell
    $adminUnit = Get-MgDirectoryAdministrativeUnit -Filter "displayName eq 'Seattle Admin Unit'"
    $directoryScope = '/administrativeUnits/' + $adminUnit.Id
    ```

1. Use [New-MgRoleManagementDirectoryRoleAssignment](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.identity.governance/new-mgrolemanagementdirectoryroleassignment) to assign the role.

    ```powershell
    $roleAssignment = New-MgRoleManagementDirectoryRoleAssignment `
       -DirectoryScopeId $directoryScope -PrincipalId $user.Id `
       -RoleDefinitionId $roleDefinition.Id
    ```

# [Graph API](#tab/ms-graph)

Follow these instructions to assign a role at administrative unit scope using the Microsoft Graph API in [Graph Explorer](https://aka.ms/ge).

#### Assign role using Create unifiedRoleAssignment API

1. Sign in to the [Graph Explorer](https://aka.ms/ge).

1. Use [List users](https://learn.microsoft.com/en-us/graph/api/user-list) API to get the user.

    ```http
    GET https://graph.microsoft.com/v1.0/users?$filter=userPrincipalName eq 'alice@contoso.com'
    ```

1. Use the [List unifiedRoleDefinitions](https://learn.microsoft.com/en-us/graph/api/rbacapplication-list-roledefinitions) API to get the role you want to assign.

    ```http
    GET https://graph.microsoft.com/v1.0/rolemanagement/directory/roleDefinitions?$filter=displayName eq 'User Administrator'
    ```

1. Use the [List administrativeUnits](https://learn.microsoft.com/en-us/graph/api/directory-list-administrativeunits) API to get the administrative unit you want the role assignment to be scoped to.

    ```http
    GET https://graph.microsoft.com/v1.0/directory/administrativeUnits?$filter=displayName eq 'Seattle Admin Unit'
    ```

1. Use the [Create unifiedRoleAssignment](https://learn.microsoft.com/en-us/graph/api/rbacapplication-post-roleassignments) API to assign the role.

    ```http
    POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments
    {
        "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
        "principalId": "<Object ID of user>",
        "roleDefinitionId": "<ID of role definition>",
        "directoryScopeId": "/administrativeUnits/<Object ID of administrative unit>"
    }
    ```

    Response
    
    ```http
    HTTP/1.1 201 Created
    ```

    If the role isn't supported, the response is bad request.

    ```http
    HTTP/1.1 400 Bad Request
    {
        "odata.error":
        {
            "code":"Request_BadRequest",
            "message":
            {
                "message":"The given built-in role is not supported to be assigned to a single resource scope."
            }
        }
    }
    ```

    > [!NOTE]
    > In this example, `directoryScopeId` is specified as `/administrativeUnits/<ID>`, instead of `/<ID>`. It is by design. The scope `/administrativeUnits/<ID>` means the principal can manage the members of the administrative unit (based on the role that the principal is assigned), not the administrative unit itself. The scope of `/<ID>` means the principal can manage that Microsoft Entra object itself. In the app registration section, you see that the scope is `/<ID>` because a role scoped over an app registration grants the privilege to manage the object itself.

#### Assign role using Add a scopedRoleMember API

Alternatively, you can use the [Add a scopedRoleMember](https://learn.microsoft.com/en-us/graph/api/administrativeunit-post-scopedrolemembers) API to assign a role with administrative unit scope.

Request

```http
POST /directory/administrativeUnits/{admin-unit-id}/scopedRoleMembers
```

Body

```http
{
  "roleId": "roleId-value",
  "roleMemberInfo": {
    "id": "id-value"
  }
}
```

---

## Next steps

- [List Microsoft Entra role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/view-assignments)
- [Assign Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user)
- [Use Microsoft Entra groups to manage role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/groups-concept)
- [Troubleshoot Microsoft Entra roles assigned to groups](groups-faq-troubleshooting.yml)
