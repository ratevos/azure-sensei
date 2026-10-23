# Govern access with an organizational role model

> Source: https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-organizational-roles  
> Microsoft doc last updated: 12/10/2024


Role-based access control (RBAC) provides a framework for classifying users and IT resources. This framework allows you to make explicit their relationship and the access rights that are appropriate according to that classification. For example, by assigning to a user attributes that specify the users job title and project assignments, the user can be granted access to tools needed for the user's job and data that the user needs to contribute to a particular project. When the user assumes a different job and different project assignments, changing the attributes that specify the user's job title and projects automatically blocks access to the resources only required for the users previous position.

In Microsoft Entra ID, you can use role models in several ways to manage access at scale through identity governance.

 * You can use access packages to represent organizational roles in your organization, such as "sales representative". An access package representing that organizational role would include all the access rights that a sales representative might typically need, across multiple resources.
 * Applications [can define their own roles](https://learn.microsoft.com/en-us/entra/identity-platform/howto-add-app-roles-in-apps). For example, if you had a sales application, and that application included the app role "salesperson" in its manifest, you could then [include that role from the app manifest in an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources).  Applications can also use security groups in scenarios where an identity could have multiple application-specific roles simultaneously.
 * You can use roles for [delegating administrative access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate).  If you have a catalog for all the access packages needed by sales, you could assign someone to be responsible for that catalog, by assigning them a catalog-specific role.

This article discusses how to model organizational roles, using entitlement management access packages, so you can migrate your role definitions to Microsoft Entra ID to enforce access.

## Migrating an organizational role model

The following table illustrates how concepts in organizational role definitions you might be familiar with in other products correspond to capabilities in entitlement management.

| Concept in organizational role modeling | Representation in Entitlement Management |
| --- | --- |
| Delegated role management | [Delegate to catalog creators](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate-catalog) |
| Collection of permissions across one or more applications | [Create an access package with resource roles](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create) |
| Restrict duration of access a role provides | [Set an access package's policy lifecycle settings to have an expiration date](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-lifecycle-policy) |
| Individual assignment to a role | [Create a direct assignment to an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#directly-assign-an-identity) |
| Assignment of roles to users based on properties (such as their department) | [Establish automatic assignment to an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-auto-assignment-policy) |
| Users can request and be approved for a role | [Configure policy settings for who can request an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy) |
| Access recertification of role members | [Set recurring access review settings in an access package policy](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-reviews-create) |
| Separation of duties between roles | [Define two or more access packages as incompatible](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-incompatible)|

For example, an organization may have an existing organizational role model similar to the following table.

|Role Name|Permissions the role provides|Automatic assignment to the role|Request-based assignment to the role|Separation of duties checks|
|:--|-|-|-|-|
|*Salesperson*|Member of **Sales** Team|Yes|No|None|
|*Sales Solution Manager*|The permissions of *Salesperson*, and **Solution manager** app role in the Sales application|None|A salesperson can request, requires manager approval and quarterly review|Requestor can't be a *Sales Account Manager*|
|*Sales Account Manager*|The permissions of *Salesperson*, and **Account manager** app role in the Sales application|None|A salesperson can request, requires manager approval and quarterly review|Request can't be a *Sales Solution Manager*|
|*Sales Support*|Same permissions as a *Salesperson*|None|Any nonsalesperson can request, requires manager approval and quarterly review|Requestor can't be a *Salesperson*|

This could be represented in Microsoft Entra ID Governance as an access package catalog containing four access packages.

|Access package|Resource roles|Policies|Incompatible access packages|
|:--|--|--|--|
|*Salesperson*|Member of **Sales** Team|Auto-assignment||
|*Sales Solution Manager*|**Solution manager** app role in the Sales application|Request-based|*Sales Account Manager*|
|*Sales Account Manager*|**Account manager** app role in the Sales application|Request-based|*Sales Solution Manager*|
|*Sales Support*|Member of **Sales** Team|Request-based|*Salesperson*|

The next sections outline the process for migration, creating the Microsoft Entra ID and Microsoft Entra ID Governance artifacts to implement the equivalent access of an organizational role model.

<a name='connect-apps-whose-permissions-are-referenced-in-the-organizational-roles-to-azure-ad'></a>

### Connect apps whose permissions are referenced in the organizational roles to Microsoft Entra ID

If your organizational roles are used to assign permissions that control access to non-Microsoft SaaS apps, on-premises apps or your own cloud apps, then you'll need to connect your applications to Microsoft Entra ID.

In order for an access package representing an organizational role to be able to refer to an application's roles as the permissions to include in the role, for an application that  has multiple roles and supports modern standards such as SCIM, you should [integrate the application with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-integrate) and ensure that the application's roles are listed in the application manifest.

If the application only has a single role, then you should still [integrated the application with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-integrate).  For applications that don't support SCIM, Microsoft Entra ID can write users into an application's existing directory or SQL database, or add AD users into an AD group.

<a name='populate-azure-ad-schema-used-by-apps-and-for-user-scoping-rules-in-the-organizational-roles'></a>

### Populate Microsoft Entra schema used by apps and for user scoping rules in the organizational roles

If your role definitions include statements of the form "all users with these attribute values get assigned to the role automatically" or "users with these attribute values are allowed to request", then you'll need to ensure those attributes are present in Microsoft Entra ID.

You can [extend the Microsoft Entra schema](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/user-provisioning-sync-attributes-for-mapping) and then populate those attributes either from on-premises AD, via Microsoft Entra Connect, or from an HR system such as Workday or SuccessFactors.

### Create catalogs for delegation

If the ongoing maintenance of roles is delegated, then you can delegate the administration of access packages by [creating a catalog](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create) for each part of the organization you'll be delegating to.

If you have multiple catalogs to create, you can use a PowerShell script to [create each catalog](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create#create-a-catalog-with-powershell).

If you aren't planning to delegate the administration of the access packages, then you can keep the access packages in a single catalog.

### Add resources to the catalogs

Now that you have the catalogs identified, then [add the applications, groups or sites](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create#add-resources-to-a-catalog) that are included in the access packages representing the organization roles to the catalogs.

If you have many resources, you can use a PowerShell script to [add each resource to a catalog](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create#add-a-resource-to-a-catalog-with-powershell).  For more information, see [Create an access package in entitlement management for an application with a single role using PowerShell](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create-app).

### Create access packages corresponding to organizational role definitions

Each organizational role definition can be represented with an [access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create) in that catalog.

You can use a PowerShell script to [create an access package in a catalog](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#create-an-access-package-by-using-microsoft-powershell).

Once you've created an access package, then you link one or more of the roles of the resources in the catalog to the access package.  This represents the permissions of the organizational role.

In addition, you'll [create a policy for direct assignment](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#none-administrator-direct-assignments-only), as part of that access package that can be used to track the identities who already have individual organizational role assignments.

### Create access package assignments for existing individual organizational role assignments

If some of your identities already have organizational role memberships, that they wouldn't receive via automatic assignment, then you should [create direct assignments](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#directly-assign-an-identity) for those identities to the corresponding access packages.

If you have many identities who need assignments, you can use a PowerShell script to [assign each user to an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#assign-a-user-to-an-access-package-with-powershell).  This would link the users to the direct assignment policy.

### Add policies to those access packages for auto assignment

If your organizational role definition includes a rule based on identity attributes to assign and remove access automatically based on those attributes, you can represent this using an [automatic assignment policy](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-auto-assignment-policy). An access package can have at most one automatic assignment policy.

If you have many role definitions that each have a role definition, you can use a PowerShell script to [create each automatic assignment policy](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-auto-assignment-policy#create-an-access-package-assignment-policy-through-powershell) in each access package.

### Set access packages as incompatible for separation of duties

If you have separation of duties constraints that prevent an identity from taking on one organizational role when they already have another, then you can prevent the identity from requesting access in entitlement management by [marking those access package combinations as incompatible](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-incompatible).

For each access package that is to be marked as incompatible with another, you can use a PowerShell script to [configure access packages as incompatible](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-incompatible#configure-incompatible-access-packages-through-microsoft-powershell).

### Add policies to access packages for identities to be allowed to request

If identities who don't already have an organizational role are allowed to request and be approved to take on a role, then you can also configure entitlement management to allow identities to request an access package. You can [add additional policies to an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#choose-between-one-or-multiple-policies), and in each policy specify which identities can request and who must approve.

### Configure access reviews in access package assignment policies

If your organizational roles require regular review of their membership, you can [configure recurring access reviews](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-reviews-create) in the request-based and direct assignment policies.

## Next steps

- [What is Microsoft Entra entitlement management?](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview)
- [Define governance policies](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-define)
- [Integrate an application with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-integrate)
- [Deploy governance policies](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-applications-deploy)
