# Common scenarios in entitlement management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-scenarios  
> Microsoft doc last updated: 07/15/2024


There are several ways that you can configure entitlement management for your organization. However, if you're just getting started, it's helpful to understand the common scenarios for administrators, catalog owners, access package managers, approvers, and requestors.

## Delegate

### Administrator: Delegate management of resources

1. [Watch video: Delegation from IT to department manager](https://learn-video.azurefd.net/vod/player?id=0915072b-63ec-4c78-b2ca-aa5f54a54219)
1. [Delegate users to catalog creator role](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate-catalog)

### Catalog creator: Delegate management of resources

- [Create a new catalog](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create#create-a-catalog)

### Catalog owner: Delegate management of resources

1. [Add co-owners to the catalog](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create#add-more-catalog-owners)
1. [Add resources to the catalog](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create#add-resources-to-a-catalog)

### Catalog owner: Delegate management of access packages

1. [Watch video: Delegation from catalog owner to access package manager](https://learn-video.azurefd.net/vod/player?id=b999927c-7cfd-4029-8b3a-a59efa9f5e8c)
1. [Delegate users to access package manager role](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate-managers)

## Govern access for users in your organization

### Administrator: Assign employees access automatically

1. [Create a new access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#start-the-creation-process)
1. [Add groups, Teams, applications, or SharePoint sites to access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#select-resource-roles)
1. [Add an automatic assignment policy](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-auto-assignment-policy)

### Administrator: Assign employees access from lifecycle workflows

1. [Create a new access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#start-the-creation-process)
1. [Add groups, Teams, applications, or SharePoint sites to access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#select-resource-roles)
1. [Add a direct assignment policy](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#none-administrator-direct-assignments-only)
1. Add a task to [Request user access package assignment](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks#request-user-access-package-assignment) to a workflow when a user joins
1. Add a task to [Remove access package assignment for user](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks#remove-access-package-assignment-for-user) to a workflow when a user leaves

### Access package manager: Allow employees in your organization to request access to resources

1. [Create a new access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#start-the-creation-process)
1. [Add groups, Teams, applications, or SharePoint sites to access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#select-resource-roles)
1. [Add a request policy to allow users, service principals, and agent identities in your directory to request access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#allow-users-service-principals-and-agent-identities-in-your-directory-to-request-the-access-package)
1. [Specify expiration settings](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#specify-a-lifecycle)

### Requestor: Request access to resources

1. [Sign in to the My Access portal](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-access#sign-in-to-the-my-access-portal)
1. Find access package
1. [Request access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-access#request-an-access-package)

### Approver: Approve requests to resources

1. [Open request in My Access portal](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-approve#open-request)
1. [Approve or deny access request](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-approve#approve-or-deny-request)

### Requestor: View the resources you already have access to

1. [Sign in to the My Access portal](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-access#sign-in-to-the-my-access-portal)
1. View active access packages

## Govern access for users outside your organization

### Administrator: Collaborate with an external partner organization

1. [Read how access works for external users](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-external-users#how-access-works-for-external-users)
1. [Review settings for external users](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-external-users#settings-for-external-users)
1. [Add a connection to the external organization](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-organization)

### Access package manager: Collaborate with an external partner organization

1. [Create a new access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#start-the-creation-process)
1. [Add groups, Teams, applications, or SharePoint sites to access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources#add-resource-roles)
1. [Add a request policy to allow users not in your directory to request access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#for-users-not-in-your-directory)
1. [Specify expiration settings](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#specify-a-lifecycle)
1. [Copy the link to request the access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-settings)
1. Send the link to your external partner contact partner to share with their users

### Requestor: Request access to resources as an external user

1. Find the access package link you received from your contact
1. [Sign in to the My Access portal](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-access#sign-in-to-the-my-access-portal)
1. [Request access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-access#request-an-access-package)

### Approver: Approve requests to resources

1. [Open request in My Access portal](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-approve#open-request)
1. [Approve or deny access request](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-approve#approve-or-deny-request)

### Requestor: View the resources your already have access to

1. [Sign in to the My Access portal](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-access#sign-in-to-the-my-access-portal)
1. View active access packages

## Govern access for agents (preview)

Using [Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) for agent identities requires one of the following license plans:

- **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite, to provide governance of user and agent identities.
- **Microsoft Agent 365** license paired with at least Microsoft Entra P1 or Microsoft 365 E3.

For more information, see [Microsoft Agent 365 plans and pricing](https://www.microsoft.com/microsoft-agent-365#plans-and-pricing). For the full list of agent-specific capabilities, refer to the **Microsoft Agent 365** column in the [Microsoft Entra ID Governance licensing table](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

1. [Create a new access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#start-the-creation-process)
1. [Add groups or API permissions to access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#select-resource-roles)
1. [Add a request policy to allow service principals and agent identities in your directory to request access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-create#allow-users-service-principals-and-agent-identities-in-your-directory-to-request-the-access-package)

## Day-to-day management

### Administrator: View the connected organizations that are proposed and configured

1. [View the list of connected organizations](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-organization)

### Access package manager: Update the resources for a project

1. [Watch video: Day-to-day management: Things have changed](https://learn-video.azurefd.net/vod/player?id=cebe87cf-64db-4242-9527-f726b6d227f9)
1. Open the access package
1. [Add or remove groups, Teams, applications, or SharePoint sites](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources#add-resource-roles)

### Access package manager: Update the duration for a project

1. [Watch video: Day-to-day management: Things have changed](https://learn-video.azurefd.net/vod/player?id=cebe87cf-64db-4242-9527-f726b6d227f9)
1. Open the access package
1. [Open the lifecycle settings](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-lifecycle-policy#open-lifecycle-settings)
1. [Update the expiration settings](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-lifecycle-policy#specify-a-lifecycle) 

### Access package manager: Update how access is approved for a project

1. [Watch video: Day-to-day management: Things have changed](https://learn-video.azurefd.net/vod/player?id=cebe87cf-64db-4242-9527-f726b6d227f9)
1. [Open an existing policy's request settings](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#open-an-existing-access-package-and-add-a-new-policy-with-different-request-settings)
1. [Update the approval settings](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-approval-policy#change-approval-settings-of-an-existing-access-package-assignment-policy)

### Access package manager: Update the people for a project

1. [Watch video: Day-to-day management: Things have changed](https://learn-video.azurefd.net/vod/player?id=cebe87cf-64db-4242-9527-f726b6d227f9)
1. [Remove users that no longer need access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments)
1. [Open an existing policy's request settings](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#open-an-existing-access-package-and-add-a-new-policy-with-different-request-settings)
1. [Add identities that need access](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#for-users-service-principals-and-agent-identities-in-your-directory)

### Access package manager: Directly assign specific users to an access package

1. [If users need different lifecycle settings, add a new policy to the access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-request-policy#open-an-existing-access-package-and-add-a-new-policy-with-different-request-settings)
1. [Directly assign specific identities to the access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#directly-assign-an-identity)

## Assignments and reports

### Administrator: View who has assignments to an access package

1. Open an access package
1. [View assignments](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments#view-who-has-an-assignment)
1. [Archive reports and logs](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logs-and-reporting)

### Administrator: View resources assigned to users

1. [View access packages for a user](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-reports#view-access-packages-for-a-user)
1. [View resource assignments for a user](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-reports#view-resource-assignments-for-a-user)

## Programmatic administration

You can also manage access packages, catalogs, policies, requests, and assignments using Microsoft Graph. A user in an appropriate role with an application that has the delegated `EntitlementManagement.Read.All` or `EntitlementManagement.ReadWrite.All` permission can call the [entitlement management API](https://learn.microsoft.com/en-us/graph/api/resources/entitlementmanagement-overview). For more information, see the [Tutorial: manage access to resources - Microsoft Graph](https://learn.microsoft.com/en-us/graph/tutorial-access-package-api?toc=/azure/active-directory/governance/toc.json&bc=/azure/active-directory/governance/breadcrumb/toc.json). An application with the `EntitlementManagement.Read.All` or `EntitlementManagement.ReadWrite.All` application permissions can also use many of those API functions, except for managing resources in catalogs and access packages. An application that only needs to operate within specific catalogs can be added to the **Catalog owner** or **Catalog reader** roles of a catalog to be authorized to update or read within that catalog.

## Next steps

- [Delegation and roles](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate)
- [Request process and email notifications](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-process)
