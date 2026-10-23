# Roles across Microsoft services

> Source: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/m365-workload-docs  
> Microsoft doc last updated: 08/31/2024


Services in Microsoft 365 can be managed with administrative roles in Microsoft Entra ID. Some services also provide additional roles that are specific to that service. This article lists content, API references, and audit and monitoring references related to role-based access control (RBAC) for Microsoft 365 and other services.

## Microsoft Entra

Microsoft Entra ID and related services in Microsoft Entra.

### Microsoft Entra ID

> | Area | Content |
> | --- | --- |
> | Overview | [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference) |
> | Management API reference | **Microsoft Entra roles**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• When role is assigned to a group, manage group memberships with the [Microsoft Graph v1.0 groups API](https://learn.microsoft.com/en-us/graph/api/resources/groups-overview) |
> | Audit and monitoring reference | **Microsoft Entra roles**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category<br/>• When a role is assigned to a group, to audit changes to group memberships, see audits with category `GroupManagement` and activities `Add member to group` and `Remove member from group` |

### Entitlement management

> | Area | Content |
> | --- | --- |
> | Overview | [Entitlement management roles](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate#entitlement-management-roles) |
> | Management API reference | **Entitlement Management-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with: `microsoft.directory/entitlementManagement`<br/><br/>**Entitlement Management-specific roles**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `entitlementManagement` provider |
> | Audit and monitoring reference | **Entitlement Management-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category<br/><br/>**Entitlement Management-specific roles**<br/>In Microsoft Entra audit log, with category `EntitlementManagement` and Activity is one of:<br/>• `Remove Entitlement Management role assignment`<br/>• `Add Entitlement Management role assignment` |

## Microsoft 365

Services in the Microsoft 365 suite.

### Exchange

> | Area | Content |
> | --- | --- |
> | Overview | [Permissions in Exchange Online](https://learn.microsoft.com/en-us/exchange/permissions-exo/permissions-exo) |
> | Management API reference | **Exchange-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• Roles with permissions starting with: `microsoft.office365.exchange`<br/><br/>**Exchange-specific roles**<br/>[Microsoft Graph Beta roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement?view=graph-rest-beta&preserve-view=true)<br/>• Use `exchange` provider |
> | Audit and monitoring reference | **Exchange-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category<br/><br/>**Exchange-specific roles**<br/>Use the [Microsoft Graph Beta Security API](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-beta&preserve-view=true#audit-logs-query-preview) ([audit log query](https://learn.microsoft.com/en-us/graph/api/resources/security-auditlogquery)) and list audit events where recordType == `ExchangeAdmin` and Operation is one of:<br/>`Add-RoleGroupMember`, `Remove-RoleGroupMember`, `Update-RoleGroupMember`, `New-RoleGroup`, `Remove-RoleGroup`, `New-ManagementRole`, `Remove-ManagementRoleEntry`, `New-ManagementRoleAssignment` |

### SharePoint

Includes SharePoint, OneDrive, Delve, Lists, Project Online, and Loop.

> | Area | Content |
> | --- | --- |
> | Overview | [About the SharePoint Administrator role in Microsoft 365](https://learn.microsoft.com/en-us/sharepoint/sharepoint-admin-role)<br/>[Delve for admins](https://learn.microsoft.com/en-us/sharepoint/delve-for-office-365-admins)<br/>[Control settings for Microsoft Lists](https://learn.microsoft.com/en-us/sharepoint/control-lists)<br/>[Change permission management in Project Online](https://learn.microsoft.com/en-us/projectonline/change-permission-management-in-project-online) |
> | Management API reference | **SharePoint-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• Roles with permissions starting with: `microsoft.office365.sharepoint` |
> | Audit and monitoring reference | **SharePoint-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Intune

> | Area | Content |
> | --- | --- |
> | Overview | [Role-based access control (RBAC) with Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/fundamentals/role-based-access-control) |
> | Management API reference | **Intune-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• Roles with permissions starting with: `microsoft.intune`<br/><br/>**Intune-specific roles**<br/>[Microsoft Graph Beta roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement?view=graph-rest-beta&preserve-view=true)<br/>• Use `deviceManagement` provider<br/>• Alternatively, use Intune-specific [Microsoft Graph Beta RBAC management API](https://learn.microsoft.com/en-us/graph/api/resources/intune-rbac-conceptual?view=graph-rest-beta&preserve-view=true) |
> | Audit and monitoring reference | **Intune-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• `RoleManagement` category<br/><br/>**Intune-specific roles**<br/>[Intune auditing overview](https://learn.microsoft.com/en-us/mem/intune/fundamentals/monitor-audit-logs)<br/>API access to Intune-specific audit logs:<br/>• [Microsoft Graph Beta getAuditActivityTypes API](https://learn.microsoft.com/en-us/graph/api/intune-auditing-auditevent-getauditactivitytypes?view=graph-rest-beta&preserve-view=true)<br/>• First list activity types where category=`Role`, then use [Microsoft Graph Beta auditEvents API](https://learn.microsoft.com/en-us/graph/api/intune-auditing-auditevent-list?view=graph-rest-beta&preserve-view=true) to list all auditEvents for each activity type |

### Teams

Includes Teams, Bookings, Copilot Studio for Teams, and Shifts.

> | Area | Content |
> | --- | --- |
> | Overview | [Use Microsoft Teams administrator roles to manage Teams](https://learn.microsoft.com/en-us/microsoftteams/using-admin-roles) |
> | Management API reference | **Teams-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• Roles with permissions starting with: `microsoft.teams` |
> | Audit and monitoring reference | **Teams-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Purview suite

Includes Purview suite, Azure Information Protection, and Information Barriers.

> | Area | Content |
> | --- | --- |
> | Overview | [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions) |
> | Management API reference | **Purview-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with:<br/>`microsoft.office365.complianceManager`<br/>`microsoft.office365.protectionCenter`<br/>`microsoft.office365.securityComplianceCenter`<br/><br/>**Purview-specific roles**<br/>Use PowerShell: [Security & Compliance PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/scc-powershell). Specific cmdlets are:<br/>[Get-RoleGroup](https://learn.microsoft.com/en-us/powershell/module/exchange/get-rolegroup)<br/>[Get-RoleGroupMember](https://learn.microsoft.com/en-us/powershell/module/exchange/get-rolegroupmember)<br/>[New-RoleGroup](https://learn.microsoft.com/en-us/powershell/module/exchange/new-rolegroup)<br/>[Add-RoleGroupMember](https://learn.microsoft.com/en-us/powershell/module/exchange/add-rolegroupmember)<br/>[Update-RoleGroupMember](https://learn.microsoft.com/en-us/powershell/module/exchange/update-rolegroupmember)<br/>[Remove-RoleGroupMember](https://learn.microsoft.com/en-us/powershell/module/exchange/remove-rolegroupmember)<br/>[Remove-RoleGroup](https://learn.microsoft.com/en-us/powershell/module/exchange/remove-rolegroup) |
> | Audit and monitoring reference | **Purview-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category<br/><br/>**Purview-specific roles**<br/>Use the [Microsoft Graph Beta Security API](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-beta&preserve-view=true#audit-logs-query-preview) ([audit log query Beta](https://learn.microsoft.com/en-us/graph/api/resources/security-auditlogquery?view=graph-rest-beta&preserve-view=true)) and list audit events where recordType == `SecurityComplianceRBAC` and Operation is one of `Add-RoleGroupMember`, `Remove-RoleGroupMember`, `Update-RoleGroupMember`, `New-RoleGroup`, `Remove-RoleGroup` |

### Power Platform

Includes Power Platform, Dynamics 365, Flow, and Dataverse for Teams.

> | Area | Content |
> | --- | --- |
> | Overview | [Use service admin roles to manage your tenant](https://learn.microsoft.com/en-us/power-platform/admin/use-service-admin-role-manage-tenant)<br/>[Security roles and privileges](https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges) |
> | Management API reference | **Power Platform-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with:<br/>`microsoft.powerApps`<br/>`microsoft.dynamics365`<br/>`microsoft.flow`<br/><br/>**Dataverse-specific roles**<br/>[Perform operations using the Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api)<br/>• Query the [User (SystemUser) table/entity reference](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/systemuser)<br/>• Role assignments are part of the [systemuserroles_association](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/systemuser#BKMK_systemuserroles_association) tables |
> | Audit and monitoring reference | **Power Platform-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category<br/><br/>**Dataverse-specific roles**<br/>[Dataverse auditing overview](https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing)<br/>API to access dataverse-specific audit logs<br/>[Dataverse Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api)<br/>• [Audit table reference](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/audit)<br/>• Audits with [action codes](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/audit#action-choicesoptions):<br/>53 – Assign Role To Team<br/>54 – Remove Role From Team<br/>55 – Assign Role To User<br/>56 – Remove Role From User<br/>57 – Add Privileges to Role<br/>58 – Remove Privileges From Role<br/>59 – Replace Privileges In Role |

### Defender suite

Includes Defender suite, Secure Score, Cloud App Security, and Threat Intelligence.

> | Area | Content |
> | --- | --- |
> | Overview | [Microsoft Defender XDR Unified role-based access control (RBAC)](https://learn.microsoft.com/en-us/defender-xdr/manage-rbac) |
> | Management API reference | **Defender-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• The following roles have permissions ([reference](https://learn.microsoft.com/en-us/microsoft-365/security/defender/m365d-permissions)): Security Administrator, Security Operator, Security Reader, Global Administrator, and Global Reader<br/><br/>**Defender-specific roles**<br/>Workloads must be activated to use Defender unified RBAC. See [Activate Microsoft Defender XDR Unified role-based access control (RBAC)](https://learn.microsoft.com/en-us/microsoft-365/security/defender/activate-defender-rbac). Activating defender Unified RBAC will turn off individual Defender solution roles.<br/>• Can only be managed via security.microsoft.com portal. |
> | Audit and monitoring reference | **Defender-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Viva Engage

> | Area | Content |
> | --- | --- |
> | Overview | [Manage administrator roles in Viva Engage](https://learn.microsoft.com/en-us/viva/engage/eac-key-admin-roles-permissions) |
> | Management API reference | **Viva Engage-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with `microsoft.office365.yammer`.<br/><br/>**Viva Engage-specific roles**<br/>• Verified admin and Network admin roles can be managed via the Yammer admin center.<br/>• Corporate communicator role can be assigned via the Viva Engage admin center.<br/>• [Yammer Data Export API](https://learn.microsoft.com/en-us/rest/api/yammer/network-data-export) can be used to export admins.csv to read the list of admins |
> | Audit and monitoring reference | **Viva Engage-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category<br/><br/>**Viva Engage-specific roles**<br/>• Use [Yammer Data Export API](https://learn.microsoft.com/en-us/rest/api/yammer/network-data-export) to incrementally export admins.csv for a list of admins |

### Viva Connections

> | Area | Content |
> | --- | --- |
> | Overview | [Admin roles and tasks in Microsoft Viva](https://learn.microsoft.com/en-us/viva/microsoft-viva-admin-roles#viva-connections) |
> | Management API reference | **Viva Connections-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• The following roles have permissions: SharePoint Administrator, Teams Administrator, and Global Administrator |
> | Audit and monitoring reference | **Viva Connections-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Viva Learning

> | Area | Content |
> | --- | --- |
> | Overview | [Set up Microsoft Viva Learning in the Teams admin center](https://learn.microsoft.com/en-us/viva/learning/set-up-viva-learning#admin-roles-and-permissions) |
> | Management API reference | **Viva Learning-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with `microsoft.office365.knowledge` |
> | Audit and monitoring reference | **Viva Learning-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Viva Insights

> | Area | Content |
> | --- | --- |
> | Overview | [Roles in Viva Insights](https://learn.microsoft.com/en-us/viva/insights/advanced/setup-maint/user-roles) |
> | Management API reference | **Viva Insights-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with `microsoft.office365.insights` |
> | Audit and monitoring reference | **Viva Insights-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Search

> | Area | Content |
> | --- | --- |
> | Overview | [Set up Microsoft Search](https://learn.microsoft.com/en-us/microsoftsearch/setup-microsoft-search) |
> | Management API reference | **Search-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with `microsoft.office365.search` |
> | Audit and monitoring reference | **Search-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Universal Print

> | Area | Content |
> | --- | --- |
> | Overview | [Universal Print Administrator Roles](https://learn.microsoft.com/en-us/universal-print/fundamentals/universal-print-administrator-roles) |
> | Management API reference | **Universal Print-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with `microsoft.azure.print` |
> | Audit and monitoring reference | **Universal Print-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

### Microsoft 365 Apps suite management

Includes Microsoft 365 Apps suite management and Forms.

> | Area | Content |
> | --- | --- |
> | Overview | [Overview of the Microsoft 365 Apps admin center](https://learn.microsoft.com/en-us/microsoft-365-apps/admin-center/overview)<br/>[Administrator settings for Microsoft Forms](https://learn.microsoft.com/en-us/microsoft-forms/administrator-settings-microsoft-forms) |
> | Management API reference | **Microsoft 365 Apps-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• The following roles have permissions: Office Apps Administrator, Security Administrator, Global Administrator |
> | Audit and monitoring reference | **Microsoft 365 Apps-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with `RoleManagement` category |

## Azure

Azure role-based access control (Azure RBAC) for the Azure control plane and subscription information.

### Azure

Includes Azure and Sentinel.

> | Area | Content |
> | --- | --- |
> | Overview | [What is Azure role-based access control (Azure RBAC)?](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)<br/>[Roles and permissions in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/roles) |
> | Management API reference | **Azure service-specific roles in Azure**<br/>[Azure Resource Manager Authorization API](https://learn.microsoft.com/en-us/rest/api/authorization)<br/>• Role assignment: [List](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-rest), [Create/Update](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-rest), [Delete](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-remove#rest-api)<br/>• Role definition: [List](https://learn.microsoft.com/en-us/rest/api/authorization/role-definitions/list), [Create/Update](https://learn.microsoft.com/en-us/rest/api/authorization/role-definitions/create-or-update), [Delete](https://learn.microsoft.com/en-us/rest/api/authorization/role-definitions/delete)<br/><br/>• There is a legacy method to grant access to Azure resources called [classic administrators](https://learn.microsoft.com/en-us/azure/role-based-access-control/classic-administrators). Classic administrators are equivalent to the Owner role in Azure RBAC. Classic administrators will be retired in August 2024.<br/>• Note that an Microsoft Entra Global Administrator can gain unilateral access to Azure via [elevate access](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin). |
> | Audit and monitoring reference | **Azure service-specific roles in Azure**<br/>[Monitor Azure RBAC changes in the Azure Activity Log](https://learn.microsoft.com/en-us/azure/role-based-access-control/change-history-report)<br/>• [Azure Activity Log API](https://learn.microsoft.com/en-us/rest/api/monitor/activity-logs/list)<br/>• Audits with Event Category `Administrative` and Operation `Create role assignment`, `Delete role assignment`, `Create or update custom role definition`, `Delete custom role definition`.<br/><br/>[View Elevate Access logs in the tenant level Azure Activity Log](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin#view-elevate-access-log-entries-in-the-directory-activity-logs)<br/>• [Azure Activity Log API – Tenant Activity Logs](https://learn.microsoft.com/en-us/rest/api/monitor/tenant-activity-logs/list)<br/>• Audits with Event Category `Administrative` and containing string `elevateAccess`.<br/>• Access to tenant level activity logs requires using [elevate access](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin) at least once to gain tenant level access. |

## Commerce

Services related to purchasing and billing.

### Cost Management and Billing – Enterprise Agreements

> | Area | Content |
> | --- | --- |
> | Overview | [Managing Azure Enterprise Agreement roles](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-ea-roles) |
> | Management API reference | **Enterprise Agreements-specific roles in Microsoft Entra ID**<br/>Enterprise Agreements does not support Microsoft Entra roles.<br/><br/>**Enterprise Agreements-specific roles**<br/>[Billing Role Assignments API](https://learn.microsoft.com/en-us/rest/api/billing/role-assignments)<br/>• Enterprise Administrator (Role ID: 9f1983cb-2574-400c-87e9-34cf8e2280db)<br/>• Enterprise Administrator (read only) (Role ID: 24f8edb6-1668-4659-b5e2-40bb5f3a7d7e)<br/>• EA Purchaser (Role ID: da6647fb-7651-49ee-be91-c43c4877f0c4)<br/>[Enrollment Department Role Assignments API](https://learn.microsoft.com/en-us/rest/api/billing/enrollment-department-role-assignments)<br/>• Department Admin (Role ID: fb2cf67f-be5b-42e7-8025-4683c668f840)<br/>• Department Reader (Role ID: db609904-a47f-4794-9be8-9bd86fbffd8a)<br/>[Enrollment Account Role Assignments API](https://learn.microsoft.com/en-us/rest/api/billing/enrollment-account-role-assignments)<br/>• Account Owner (Role ID: c15c22c0-9faf-424c-9b7e-bd91c06a240b) |
> | Audit and monitoring reference | **Enterprise Agreements-specific roles**<br/>[Azure Activity Log API – Tenant Activity Logs](https://learn.microsoft.com/en-us/rest/api/monitor/tenant-activity-logs/list)<br/>• Access to tenant level activity logs requires using [elevate access](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin) at least once to gain tenant level access.<br/>• Audits where resourceProvider == `Microsoft.Billing` and operationName contains `billingRoleAssignments` or `EnrollmentAccount` |

### Cost Management and Billing – Microsoft Customer Agreements

> | Area | Content |
> | --- | --- |
> | Overview | [Understand Microsoft Customer Agreement administrative roles in Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-mca-roles)<br/>[Understand your Microsoft business billing account](https://learn.microsoft.com/en-us/microsoft-365/commerce/manage-billing-accounts#what-are-billing-account-roles) |
> | Management API reference | **Microsoft Customer Agreements-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• The following roles have permissions: Billing Administrator, Global Administrator.<br/><br/>**Microsoft Customer Agreements-specific roles**<br/>• By default, the Microsoft Entra Global Administrator and Billing Administrator roles are automatically assigned the Billing Account Owner role in Microsoft Customer Agreements-specific RBAC.<br/>• [Billing Role Assignment API](https://learn.microsoft.com/en-us/rest/api/billing/billing-role-assignments) |
> | Audit and monitoring reference | **Microsoft Customer Agreements-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with category `RoleManagement`<br/><br/>**Microsoft Customer Agreements-specific roles**<br/>[Azure Activity Log API – Tenant Activity Logs](https://learn.microsoft.com/en-us/rest/api/monitor/tenant-activity-logs/list)<br/>• Access to tenant level activity logs requires using [elevate access](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin) at least once to gain tenant level access.<br/>• Audits where resourceProvider == `Microsoft.Billing` and operationName one of the following (all prefixed with `Microsoft.Billing`):<br/>`/permissionRequests/write`<br/>`/billingAccounts/createBillingRoleAssignment/action`<br/>`/billingAccounts/billingProfiles/createBillingRoleAssignment/action`<br/>`/billingAccounts/billingProfiles/invoiceSections/createBillingRoleAssignment/action`<br/>`/billingAccounts/customers/createBillingRoleAssignment/action`<br/>`/billingAccounts/billingRoleAssignments/write`<br/>`/billingAccounts/billingRoleAssignments/delete`<br/>`/billingAccounts/billingProfiles/billingRoleAssignments/delete`<br/>`/billingAccounts/billingProfiles/customers/createBillingRoleAssignment/action`<br/>`/billingAccounts/billingProfiles/invoiceSections/billingRoleAssignments/delete`<br/>`/billingAccounts/departments/billingRoleAssignments/write`<br/>`/billingAccounts/departments/billingRoleAssignments/delete`<br/>`/billingAccounts/enrollmentAccounts/transferBillingSubscriptions/action`<br/>`/billingAccounts/enrollmentAccounts/billingRoleAssignments/write`<br/>`/billingAccounts/enrollmentAccounts/billingRoleAssignments/delete`<br/>`/billingAccounts/billingProfiles/invoiceSections/billingSubscriptions/transfer/action`<br/>`/billingAccounts/billingProfiles/invoiceSections/initiateTransfer/action`<br/>`/billingAccounts/billingProfiles/invoiceSections/transfers/delete`<br/>`/billingAccounts/billingProfiles/invoiceSections/transfers/cancel/action`<br/>`/billingAccounts/billingProfiles/invoiceSections/transfers/write`<br/>`/transfers/acceptTransfer/action`<br/>`/transfers/accept/action`<br/>`/transfers/decline/action`<br/>`/transfers/declineTransfer/action`<br/>`/billingAccounts/customers/initiateTransfer/action`<br/>`/billingAccounts/customers/transfers/delete`<br/>`/billingAccounts/customers/transfers/cancel/action`<br/>`/billingAccounts/customers/transfers/write`<br/>`/billingAccounts/billingProfiles/invoiceSections/products/transfer/action`<br/>`/billingAccounts/billingSubscriptions/elevateRole/action` |

### Business Subscriptions and Billing – Volume Licensing

> | Area | Content |
> | --- | --- |
> | Overview | [Manage volume licensing user roles Frequently Asked Questions](https://learn.microsoft.com/en-us/microsoft-365/commerce/licenses/user-roles-faq) |
> | Management API reference | **Volume Licensing-specific roles in Microsoft Entra ID**<br/>Volume Licensing does not support Microsoft Entra roles.<br/><br/>**Volume Licensing-specific roles**<br/>[VL users and roles](https://learn.microsoft.com/en-us/microsoft-365/commerce/licenses/user-roles-faq#how-do-i-manage-vl-users-and-roles) are managed in the M365 Admin Center. |

### Partner Center

> | Area | Content |
> | --- | --- |
> | Overview | [Roles, permissions, and workspace access for users](https://learn.microsoft.com/en-us/partner-center/permissions-overview) |
> | Management API reference | **Partner Center-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• The following roles have permissions: Global Administrator, User Administrator.<br/><br/>**Partner Center-specific roles**<br/>[Partner Center-specific roles](https://learn.microsoft.com/en-us/partner-center/permissions-overview#microsoft-entra-tenant-roles-and-non-azure-ad-roles) can only be managed via Partner Center. |
> | Audit and monitoring reference | **Partner Center-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with category `RoleManagement` |

## Other services

### Azure DevOps

> | Area | Content |
> | --- | --- |
> | Overview | [About permissions and security groups](https://learn.microsoft.com/en-us/azure/devops/organizations/security/about-permissions) |
> | Management API reference | **Azure DevOps-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with `microsoft.azure.devOps`.<br/><br/>**Azure DevOps-specific roles**<br/>Create/read/update/delete permissions granted via [Roleassignments API](https://learn.microsoft.com/en-us/rest/api/azure/devops/securityroles/roleassignments)<br/>• View permissions of roles with [Roledefinitions API](https://learn.microsoft.com/en-us/rest/api/azure/devops/securityroles/roledefinitions)<br/>• [Permissions reference topic](https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions)<br/>• When an Azure DevOps group (note: different from Microsoft Entra group) is assigned to a role, create/read/update/delete group memberships with the [Memberships API](https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/memberships) |
> | Audit and monitoring reference | **Azure DevOps-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with category `RoleManagement`<br/><br/>**Azure DevOps-specific roles**<br/>• [Accessing the AzureDevOps Audit Log](https://learn.microsoft.com/en-us/azure/devops/organizations/audit/azure-devops-auditing)<br/>• [Audit API reference](https://learn.microsoft.com/en-us/rest/api/azure/devops/audit/)<br/>• [AuditId reference](https://learn.microsoft.com/en-us/azure/devops/organizations/audit/auditing-events)<br/>• Audits with ActionId `Security.ModifyPermission`, `Security.RemovePermission`.<br/>• For changes to groups assigned to roles, audits with ActionId `Group.UpdateGroupMembership`, `Group.UpdateGroupMembership.Add`, `Group.UpdateGroupMembership.Remove` |

### Fabric

Includes Fabric and Power BI.

> | Area | Content |
> | --- | --- |
> | Overview | [Understand Microsoft Fabric admin roles](https://learn.microsoft.com/en-us/fabric/admin/roles) |
> | Management API reference | **Fabric-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 roleManagement API](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement)<br/>• Use `directory` provider<br/>• See roles with permissions starting with `microsoft.powerApps.powerBI`. |
> | Audit and monitoring reference | **Fabric-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with category `RoleManagement` |

### Unified Support Portal for managing customer support cases

Includes Unified Support Portal and Services Hub.

> | Area | Content |
> | --- | --- |
> | Overview | [Services Hub roles and permissions](https://learn.microsoft.com/en-us/services-hub/unified/getting-started/roles-permissions) |
> | Management API reference | Manage these roles in the Services Hub portal, https://serviceshub.microsoft.com. |

## Microsoft Graph application permissions

In addition to the previously mentioned RBAC systems, elevated permissions can be granted to Microsoft Entra application registrations and service principals using application permissions. For example, a non-interactive, non-human application identity can be granted the ability to read all mail in a tenant (the `Mail.Read` application permission). The following table lists how to manage and monitor application permissions. 

> | Area | Content |
> | --- | --- |
> | Overview | [Overview of Microsoft Graph permissions](https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http#application-permissions) |
> | Management API reference | **Microsoft Graph-specific roles in Microsoft Entra ID**<br/>[Microsoft Graph v1.0 servicePrincipal API](https://learn.microsoft.com/en-us/graph/api/resources/serviceprincipal)<br/>• Enumerate the [appRoleAssignments](https://learn.microsoft.com/en-us/graph/api/resources/approleassignment) for each [servicePrincipal](https://learn.microsoft.com/en-us/graph/api/resources/serviceprincipal) in the tenant.<br/>• For each appRoleAssignment, get information about the permissions granted by the assignment by reading the appRole property on the servicePrincipal object referenced by the resourceId and appRoleId in the appRoleAssignment.<br/>• Of specific interest are app permissions to the Microsoft Graph (servicePrincipal with appID == "00000003-0000-0000-c000-000000000000") which grant access to Exchange, SharePoint, Teams, and so on. Here is a reference for [Microsoft Graph permissions](https://learn.microsoft.com/en-us/graph/permissions-reference).<br/>• Also see [Microsoft Entra security operations for applications](https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications). |
> | Audit and monitoring reference | **Microsoft Graph-specific roles in Microsoft Entra ID**<br/>[Microsoft Entra activity log overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs)<br/>API access to Microsoft Entra audit logs:<br/>• [Microsoft Graph v1.0 directoryAudit API](https://learn.microsoft.com/en-us/graph/api/resources/directoryaudit)<br/>• Audits with category `ApplicationManagement` and Activity name `Add app role assignment to service principal` |

## Next steps

* [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal)
* [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
