# Overview of Microsoft Entra role-based access control (RBAC)

> Source: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-overview  
> Microsoft doc last updated: 10/01/2026


This article describes how to understand Microsoft Entra role-based access control. Microsoft Entra roles allow you to grant granular permissions to your admins, abiding by the principle of least privilege. Microsoft Entra built-in and custom roles operate on concepts similar to those you find in [the role-based access control system for Azure resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) (Azure roles). The [difference between these two role-based access control systems](https://learn.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles) is:

- Microsoft Entra roles control access to Microsoft Entra resources such as users, groups, and applications using the Microsoft Graph API
- Azure roles control access to Azure resources such as virtual machines or storage using Azure Resource Management

Both systems contain similarly used role definitions and role assignments. However, Microsoft Entra role permissions can't be used in Azure custom roles and vice versa.

<a name='understand-azure-ad-role-based-access-control'></a>

## Understand Microsoft Entra role-based access control

Microsoft Entra ID supports two types of roles definitions:

* [Built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
* [Custom roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create)

Built-in roles are out of box roles that have a fixed set of permissions. These role definitions cannot be modified. There are many [built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) that Microsoft Entra ID supports, and the list is growing. To round off the edges and meet your sophisticated requirements, Microsoft Entra ID also supports [custom roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create). Granting permission using custom Microsoft Entra roles is a two-step process that involves creating a custom role definition and then assigning it using a role assignment. A custom role definition is a collection of permissions that you add from a preset list. These permissions are the same permissions used in the built-in roles.  

Once you’ve created your custom role definition (or using a built-in role), you can assign it to a user by creating a role assignment. A role assignment grants the user the permissions in a role definition at a specified scope. This two-step process allows you to create a single role definition and assign it many times at different scopes. A scope defines the set of Microsoft Entra resources the role member has access to. The most common scope is organization-wide (org-wide) scope. A custom role can be assigned at org-wide scope, meaning the role member has the role permissions over all resources in the organization. A custom role can also be assigned at an object scope. An example of an object scope would be a single application. The same role can be assigned to one user over all applications in the organization and then to another user with a scope of only the Contoso Expense Reports app.  

<a name='how-azure-ad-determines-if-a-user-has-access-to-a-resource'></a>

### How Microsoft Entra ID determines if a user has access to a resource

The following are the high-level steps that Microsoft Entra ID uses to determine if you have access to a management resource. Use this information to troubleshoot access issues.

1. A user (or service principal) acquires a token to the Microsoft Graph endpoint.
1. The user makes an API call to Microsoft Entra ID via Microsoft Graph using the issued token.
1. Depending on the circumstance, Microsoft Entra ID takes one of the following actions:
   - Evaluates the user’s role memberships based on the [wids claim](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) in the user’s access token.
   - Retrieves all the role assignments that apply for the user, either directly or via group membership, to the resource on which the action is being taken.
1. Microsoft Entra ID determines if the action in the API call is included in the roles the user has for this resource.
1. If the user doesn't have a role with the action at the requested scope, access is not granted. Otherwise access is granted.

## Role assignment

A role assignment is a Microsoft Entra resource that attaches a *role definition* to a *security principal* at a particular *scope* to grant access to Microsoft Entra resources. Access is granted by creating a role assignment, and access is revoked by removing a role assignment. At its core, a role assignment consists of three elements:

- Security principal - An identity that gets the permissions. It could be a user, group, or a service principal. 
- Role definition - A collection of permissions. 
- Scope - A way to constrain where those permissions are applicable.

You can [create role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal) and [list the role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/view-assignments) using the Microsoft Entra admin center, [Microsoft Graph PowerShell](https://learn.microsoft.com/en-us/powershell/microsoftgraph/overview), or Microsoft Graph API. Azure CLI is not supported for Microsoft Entra role assignments.

The following diagram shows an example of a role assignment. In this example, Chris has been assigned the App Registration Administrator custom role at the scope of the Contoso Widget Builder app registration. The assignment grants Chris the permissions of the App Registration Administrator role for only this specific app registration.

### Security principal

A security principal represents a user, group, or service principal that is assigned access to Microsoft Entra resources. A user is an individual who has a user profile in Microsoft Entra ID. A group is a new Microsoft 365 or security group that has been set as a [role-assignable group](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/groups-concept). A service principal is an identity created for use with applications, hosted services, and automated tools to access Microsoft Entra resources.

### Role definition

A role definition, or role, is a collection of permissions. A role definition lists the operations that can be performed on Microsoft Entra resources, such as create, read, update, and delete. There are two types of roles in Microsoft Entra ID:

- Built-in roles created by Microsoft that can't be changed.
- Custom roles created and managed by your organization.

### Scope

A scope is a way to limit the permitted actions to a particular set of resources as part of a role assignment. For example, if you want to assign a custom role to a developer, but only to manage a specific application registration, you can include the specific application registration as a scope in the role assignment.

When you assign a role, you specify one of the following types of scope:

- Tenant
- [Administrative unit](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units)
- Microsoft Entra resource

If you specify a Microsoft Entra resource as a scope, it can be one of the following:

- Microsoft Entra groups
- Enterprise applications
- Application registrations

When a role is assigned over a container scope, such as the Tenant or an Administrative Unit, it grants permissions over the objects they contain but not on the container itself. On the contrary, when a role is assigned over a resource scope, it grants permissions over the resource itself but it does not extend beyond (in particular, it does not extend to the members of a Microsoft Entra group).

For more information, see [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal).

## Role assignment options

Microsoft Entra ID provides multiple options for assigning roles:

- You can assign roles to users directly, which is the default way to assign roles. Both built-in and custom Microsoft Entra roles can be assigned to users, based on access requirements. For more information, see [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal).
- With Microsoft Entra ID P1, you can create role-assignable groups and assign roles to these groups. Assigning roles to a group instead of individuals allows for easy addition or removal of users from a role and creates consistent permissions for all members of the group. For more information, see [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal).
- With Microsoft Entra ID P2, you can use Microsoft Entra Privileged Identity Management (Microsoft Entra PIM) to provide just-in-time access to roles. This feature allows you to grant time-limited access to a role to users who require it, rather than granting permanent access. It also provides detailed reporting and auditing capabilities. For more information, see [Assign Microsoft Entra roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user).

## Understand who has access to what

Listing role assignments is one part of answering the broader question: "who has access to what in my organization?" Microsoft Entra ID provides several tools that, when used together, give you visibility into access across your tenant.

- **Role assignments.** Use the procedures in [List Microsoft Entra role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/view-assignments) to list who holds Microsoft Entra roles at the tenant, application, or administrative unit scope. You can [download role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/view-assignments#download-role-assignments) as a CSV for offline analysis, or query them programmatically with the [List unifiedRoleAssignments](https://learn.microsoft.com/en-us/graph/api/rbacapplication-list-roleassignments) Microsoft Graph API.
- **App role assignments and consent grants.** Use [Assign users and groups to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal) to see which users and groups can access a given enterprise application. Use [Review permissions granted to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions) to inspect the delegated and application permissions that users or administrators have consented to.
- **Custom security attributes.** Use [custom security attributes](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-overview) to tag users and service principals with business-specific attributes that you define for your tenant. You can then filter and query the directory by attribute to build a business-attribute view of access that complements role-based queries.
- **Access reviews.** Use [access reviews](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview) to periodically verify that users still need their current group memberships and assignments to enterprise applications. Use [Privileged Identity Management (PIM) access reviews](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-create-roles-and-resource-roles-review) to review users and service principals assigned to Microsoft Entra or Azure resource roles. Reviewers approve or deny continued access for each user. Access reviews require Microsoft Entra ID Governance or Microsoft Entra Suite; some capabilities operate with Microsoft Entra ID P2. For details, see [License requirements](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview#license-requirements). Reviewing service principals via PIM additionally requires Microsoft Entra Workload ID Premium.
- **Entitlement management.** Use [entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview) to see which users have been granted access through access packages. Access packages are organized into catalogs, which are containers of related resources and access packages that you can use to delegate and govern access. Entitlement management requires Microsoft Entra ID Governance or Microsoft Entra Suite; some capabilities operate with Microsoft Entra ID P2. For details, see [License requirements](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview#license-requirements).
- **Sign-in and audit logs.** Use [sign-in logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins) to see who has been actively accessing resources and under what conditions. Use [audit logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs) to track changes to role assignments, group memberships, and other directory objects over time. Audit logs record configuration changes, while sign-in logs record sign-in events — together they help you distinguish between granted access and exercised access. For richer tracing of Microsoft Graph API calls, see [Microsoft Graph activity logs](https://learn.microsoft.com/en-us/graph/microsoft-graph-activity-logs-overview).

> [!TIP]
> For large tenants, stream logs to a [Log Analytics workspace](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs.yml) so you can query and analyze access patterns across thousands of users and roles.

## Govern access for workload identities

A complete authorization-at-scale strategy must cover workload identities — applications, service principals, and managed identities — not just users. Microsoft Entra supports several methods for establishing machine identities, each suited to a different scenario:

- **[App registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).** Register an [application object](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals) to create a service principal that authenticates with a client secret, certificate, or federated credential. Use for traditional applications and platform integrations.
- **[Managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).** Use system-assigned or user-assigned managed identities for workloads running in Azure. Azure manages the credentials for you, so no secrets are stored in code or configuration.
- **[Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation).** Configure trust between Microsoft Entra and an external identity provider so workloads outside Azure — or workloads in Azure that authenticate as app registrations — can access Microsoft Entra protected resources without storing secrets.
- **[Flexible federated identity credentials (preview)](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-flexible-federated-identity-credentials).** Extend the secretless pattern for app registrations to scenarios that require wildcard or claims-based matching against tokens issued by GitHub, GitLab, or Terraform Cloud.

Govern these identities at scale with the same layered controls you apply to users:

- Apply [Conditional Access for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) to restrict where and when a service principal can authenticate. This capability requires Workload Identities Premium licenses and applies only to single-tenant service principals registered in your tenant — managed identities and multitenant or third-party SaaS apps aren't in scope.
- Run [access reviews of groups and applications](https://learn.microsoft.com/en-us/entra/id-governance/create-access-review) to confirm that users assigned to those resources still need their access, and use [PIM access reviews](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-create-roles-and-resource-roles-review) to review service principals assigned to Microsoft Entra and Azure resource roles. Reviews of groups and applications require Microsoft Entra ID Governance or Microsoft Entra Suite (some capabilities are available with Microsoft Entra ID P2); for details, see [License requirements](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview#license-requirements). Reviews of service principals additionally require Microsoft Entra Workload ID Premium.
- Tag service principals for your registered applications with [custom security attributes](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-overview) so you can build a filterable inventory and drive [Azure ABAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-custom-security-attributes) decisions from business attributes.
- Enable [app instance property lock](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks) on single-tenant and multitenant apps to prevent unauthorized modification of sensitive properties on the service principal.

## License requirements

Using built-in roles in Microsoft Entra ID is free. Using custom roles require a Microsoft Entra ID P1 license for every user with a custom role assignment. To find the right license for your requirements, see [Comparing generally available features of the Free and Premium editions](https://www.microsoft.com/security/business/identity-access-management/azure-ad-pricing).

## Next steps

- [Understand Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/concept-understand-roles)
- [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal)
- [Microsoft Entra forum](https://feedback.azure.com/d365community/forum/22920db1-ad25-ec11-b6e6-000d3a4f0789)
