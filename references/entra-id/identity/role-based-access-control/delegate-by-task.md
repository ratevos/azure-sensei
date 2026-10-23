# Least privileged roles by task

> Source: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-by-task  
> Microsoft doc last updated: 06/17/2026


This article describes the least privileged role you should use for several tasks in Microsoft Entra ID. You will find tasks organized by feature area and the least privileged role required to perform each task, along with additional non-Global Administrator roles that can perform the task.

You can further restrict permissions by assigning roles at smaller scopes or by creating your own custom roles. For more information, see [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal) or [Create a custom role in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create).

## Application proxy least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra application proxy](https://learn.microsoft.com/en-us/entra/identity/app-proxy/overview-what-is-app-proxy).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Configure application proxy app | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |
> | Configure connector group properties | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |
> | Create application registration when ability is disabled for all users | [Application Developer](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-developer) | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Create connector group | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |
> | Delete connector group | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |
> | Disable application proxy | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |
> | Download connector service | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |
> | Read all configuration | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |

## External Identities/Azure AD B2C least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview) and [Azure Active Directory B2C](https://learn.microsoft.com/en-us/azure/active-directory-b2c/overview).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Create Azure AD B2C directories | [All non-guest users](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |  |
> | Create enterprise applications | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Create, read, update, and delete B2C policies | [B2C IEF Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#b2c-ief-policy-administrator) |  |
> | Create, read, update, and delete identity providers | [External Identity Provider Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-identity-provider-administrator) |  |
> | Create, read, update, and delete password reset user flows | [External ID User Flow Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-id-user-flow-administrator) |  |
> | Create, read, update, and delete profile editing user flows | [External ID User Flow Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-id-user-flow-administrator) |  |
> | Create, read, update, and delete sign-in user flows | [External ID User Flow Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-id-user-flow-administrator) |  |
> | Create, read, update, and delete sign-up user flow | [External ID User Flow Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-id-user-flow-administrator) |  |
> | Create, read, update, and delete user attributes | [External ID User Flow Attribute Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-id-user-flow-attribute-administrator) |  |
> | Create, read, update, and delete users | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | [Configure B2B external collaboration settings - Guest user access](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure) | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | [Configure B2B external collaboration settings - Guest invite settings](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure) | [Guest Inviter](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#guest-inviter) | [External ID User Flow Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-id-user-flow-administrator) |
> | [Configure B2B external collaboration settings - External user leave settings](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure) | [External Identity Provider Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-identity-provider-administrator) |  |
> | [Configure B2B external collaboration settings - Collaboration restrictions](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure) | [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) |  |
> | Read all configuration | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |
> | [Read B2C audit logs](https://learn.microsoft.com/en-us/azure/active-directory-b2c/faq) | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |

> [!NOTE]
> Azure AD B2C Global Administrators do not have the same permissions as Microsoft Entra Global Administrators. If you have Azure AD B2C Global Administrator privileges, make sure that you are in an Azure AD B2C directory and not a Microsoft Entra directory.

## Company branding least privileged roles

Here are the least privileged roles you should use when performing tasks for [company branding](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-customize-branding) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Configure company branding | [Organizational Branding Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#organizational-branding-administrator) |  |
> | Read all configuration | [Directory Readers](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#directory-readers) | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |

## Connect least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Passthrough authentication | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |  |
> | Read all configuration | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |
> | Seamless single sign-on | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |  |

## Connect Sync least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Manage on-premises directory synchronization | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |  |

## Cloud Provisioning least privileged roles

Here are the least privileged roles you should use when performing tasks for [identity provisioning](https://learn.microsoft.com/en-us/entra/identity/hybrid/what-is-provisioning) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Passthrough authentication | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |  |
> | Read all configuration | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |
> | Seamless single sign-on | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |  |

## Connect Health least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra Connect Health](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | [Add or delete services](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-operations) | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |  |
> | Apply fixes to sync error | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor) | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | Configure notifications | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor) | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | [Configure settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-operations) | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |  |
> | Configure sync notifications | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor) | [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | Read ADFS security reports | [Security Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#security-reader) | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)<br/>[Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | Read all configuration | [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)<br/>[Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | Read sync errors | [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)<br/>[Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | Read sync services | [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)<br/>[Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | View metrics and alerts | [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)<br/>[Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | View metrics and alerts | [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)<br/>[Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |
> | View sync service metrics and alerts | [Reader](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) | [Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor)<br/>[Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) |

## Custom domain names least privileged roles

Here are the least privileged roles you should use when performing tasks for [custom domain names](https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Manage domains | [Domain Name Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#domain-name-administrator) |  |
> | Read all configuration | [Directory Readers](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#directory-readers) | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |

## Domain Services least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Create Microsoft Entra Domain Services instance | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)<br>[Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator)<br> [Domain Services Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#domain-services-contributor)|   |
> | Perform all Microsoft Entra Domain Services tasks | [AAD DC Administrators group](https://learn.microsoft.com/en-us/entra/identity/domain-services/tutorial-create-management-vm#administrative-tasks-you-can-perform-on-a-managed-domain) |  |
> | Read all configuration | Reader on Azure subscription containing AD DS service |  |

## Devices least privileged roles

Here are the least privileged roles you should use when performing tasks for [device identity](https://learn.microsoft.com/en-us/entra/identity/devices/overview) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Delete device | [Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator) | [Intune Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator) |
> | Disable device | [Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator) | [Intune Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator) |
> | Enable device | [Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator) | [Intune Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator) |
> | Read basic configuration | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |  |
> | Read BitLocker keys | [Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator) | [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator)<br/>[Intune Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator)<br/>[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |
> | Provision and manage IoT devices | [IoT Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#iot-device-administrator) | [Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator) |
> | Manage IoT device templates | [IoT Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#iot-device-administrator) | [Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator) |

## Enterprise applications least privileged roles

Here are the least privileged roles you should use when performing tasks for [application management](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-application-management) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Consent to any delegated permissions | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Consent to application permissions not including Microsoft Graph | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Consent to application permissions to Microsoft Graph | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | Consent to applications accessing own data | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |  |
> | Create enterprise application | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Manage Application Proxy | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |  |
> | Read access review of a group or of an app | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Read all configuration | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |  |
> | Update enterprise application assignments | [Enterprise application owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)<br/>[User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Update enterprise application owners | [Enterprise application owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Update enterprise application properties | [Enterprise application owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Update enterprise application provisioning | [Enterprise application owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Update enterprise application self-service | [Enterprise application owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Update single sign-on properties | [Enterprise application owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Create and modify custom authentication extensions | [Authentication Extensibility Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-extensibility-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |

> [!NOTE]
> In practice, consenting to Microsoft Graph application permissions typically requires the Global Administrator role. Privileged Role Administrator may not be sufficient depending on tenant consent policies, permission scopes, or Graph protection requirements.

## Entitlement management least privileged roles

Here are the least privileged roles you should use when performing tasks for [entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview) in Microsoft Entra ID Governance.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Tasks in Entitlement Management | [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator). For roles lesser privilege than this within the Entitlement Management system, see: [Delegation and roles in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate). | |

## Groups least privileged roles

Here are the least privileged roles you should use when performing tasks for [groups](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Assign license | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Create group | [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Create, update, or delete access review of a group or of an app | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Manage group expiration | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Manage group settings | [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Read all configuration (except hidden membership) | [Directory Readers](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#directory-readers) | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |
> | Read hidden membership | Group member | [Group owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership)<br/>[Password Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#password-administrator)<br/>[Exchange Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator)<br/>[SharePoint Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator)<br/>[Teams Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator)<br/>[User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Read membership of groups with hidden membership | [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator)<br/>[Teams Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator) |
> | Revoke license | [License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Update dynamic membership groups | [Group owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Update group owners | [Group owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Update group properties | [Group owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Delete group | [Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |

## Licenses least privileged roles

Here are the least privileged roles you should use when performing tasks for [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Assign license | [License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Read all configuration | [Directory Readers](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#directory-readers) | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |
> | Revoke license | [License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Try or buy subscription | [Billing Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) |  |

## Lifecycle Workflows least privileged roles

Here are the least privileged roles you should use when performing tasks for [lifecycle workflows](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows) in Microsoft Entra ID Governance.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Create a workflow | [Lifecycle workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator) |  |
> | Add a custom extension to a workflow | [Lifecycle workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator). You must also have either the [Logic App contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/integration#logic-app-contributor) or [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/integration#logic-app-operator) Azure Resource Manager role.  |  |

## Microsoft Entra Health least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra Health monitoring](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-microsoft-entra-health).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | View scenario monitoring signals and alert configurations | [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader)<br>[Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)<br>[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br>[Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator)<br>[Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader)<br>|
> | Update alerts and alert email configurations | [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) |  |

<a name='identity-protection'></a>

## Microsoft Entra ID Protection least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Configure alert notifications| [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Configure and enable or disable MFA policy| [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Configure and enable or disable sign-in risk policy| [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Configure and enable or disable user risk policy | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Configure weekly digests | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Dismiss all risk detections | [Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)|  |
> | Fix or dismiss vulnerability | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Read all configuration | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |
> | Read all risk detections | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |
> | Read vulnerabilities | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |

## Monitoring and health - Audit and sign-in logs least privileged roles

Here are the least privileged roles you should use when performing tasks for audit and sign-in logs in [Microsoft Entra monitoring](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Read audit and sign-in logs | [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)<br/>[Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator)<br/>[Global Secure Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator)<br/>[Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator)<br/>[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)<br/>[Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |

## Monitoring and health - Provisioning logs least privileged roles

Here are the least privileged roles you should use when performing tasks for [Microsoft Entra provisioning logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-provisioning-logs).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Read provisioning logs | [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) | [Enterprise application owner](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#object-ownership)<br/>[Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)<br/>[Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator)<br/>[Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator)<br/>[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)<br/>[Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |

## Monitoring and health - Recommendations least privileged roles

Here are the least privileged roles you should use when performing tasks for [Microsoft Entra identity recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Read recommendations | [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader)<br/>[Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader)<br/>[Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator)<br/>[Service Support Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#service-support-administrator)<br/>[User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Update recommendations | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)<br/>[Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator)<br/>[Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator)<br/>[Exchange Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator)<br/>[Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator)<br/>[Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator)<br/>[Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator)<br/>[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)<br/>[SharePoint Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator) |
> | Read Identity Secure Score improvement action | [Service Support Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#service-support-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[Exchange Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator) |
> | Update Identity Secure Score improvement action | [SharePoint Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator) | [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator)<br/>[User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator)<br/>[Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader)<br/>[Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)<br/>[Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |

## Monitoring and health - Sign-in diagnostic tool

Here are the least privileged roles you should use when running the [sign-in diagnostic tool](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-sign-in-diagnostics).

> | Task | Least privileged roles | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Use sign-in diagnostic from **Diagnose and solve problems** | [Billing Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)<br/>[Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Cloud Device Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-device-administrator)<br/>[Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator)<br/>[Customer LockBox Access Approver](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#customer-lockbox-access-approver)<br/>[Groups Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#groups-administrator)<br>[License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator)<br/>[Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader)<br/>[Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator)<br/>[Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator)<br/>[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Use sign-in diagnostic from the **Sign-in logs** | BOTH [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) AND [Billing Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) | [Global Secure Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator)<br/>[Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator)<br/>[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator)<br/>[Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |

## Multifactor authentication least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/overview-authentication).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Delete all existing app passwords generated by the selected users | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) |
> | [Disable per-user MFA](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-userstates) | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) |
> | [Enable per-user MFA](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-userstates) | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator)  | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) | 
> | Manage MFA service settings | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Require selected users to provide contact methods again | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) |  |
> | Restore multifactor authentication on all remembered devices  | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) |  |

## MFA Server least privileged roles

Here are the least privileged roles you should use when performing tasks in [MFA Server](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-migrate-mfa-server-to-azure-mfa).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Block/unblock users | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure account lockout | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure caching rules | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure fraud alert | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure notifications | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure one-time bypass | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure phone call settings | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure providers | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure server settings | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Read activity report | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |
> | Read all configuration | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |
> | Read server status | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |

## Organizational relationships least privileged roles

Here are the least privileged roles you should use when performing tasks for [external collaboration settings](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure) in Microsoft Entra External ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Manage identity providers | [External Identity Provider Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#external-identity-provider-administrator) |  |
> | Read all configuration | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |

## Password reset least privileged roles

Here are the least privileged roles you should use when performing tasks for [password reset](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Configure authentication methods | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure customization | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure notification | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure on-premises integration | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Configure password reset properties | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |
> | Configure registration | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | Read all configuration | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |

## Privileged Identity Management least privileged roles

Here are the least privileged roles you should use when performing tasks for [Microsoft Entra Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) in Microsoft Entra ID Governance.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Assign users to roles | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | Configure role settings | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | View audit activity | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |
> | View role memberships | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |

## Roles and administrators least privileged roles

Here are the least privileged roles you should use when performing tasks for [roles and administrators](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Manage role assignments | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | Read access review of a Microsoft Entra role  | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)<br/>[Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |
> | Read all configuration | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |  |

## Security - Authentication methods least privileged roles

Here are the least privileged roles you should use when performing tasks for [authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/overview-authentication) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Enable or disable authentication methods | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |
> | View, provision on behalf of, and manage individual user authentication methods | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) |
> | Configure password protection | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Configure smart lockout | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Read all configuration | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |

## Security - Conditional Access least privileged roles

Here are the least privileged roles you should use when performing tasks for [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Configure MFA trusted IP addresses | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) |  |
> | Create custom controls | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Create named locations | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Create policies | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Create terms of use | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Create VPN connectivity certificate | [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) |
> | Delete classic policy | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Restore a soft-deleted policy | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Delete terms of use | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Delete VPN connectivity certificate | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Disable classic policy | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Manage custom controls | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Manage named locations | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Manage terms of use | [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Read all configuration | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |
> | Read named locations | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |
> | Read terms of use | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |
> | Read which terms of use were accepted by the signed-in user | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |  |

## Security - Identity Security Score least privileged roles

Here are the least privileged roles you should use when performing tasks for [Identity Secure Score](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles | 
> | ---- | --------------------- | ---------------- |
> | Read all configuration | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Read security score | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Update event status | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |

## Security - Risky sign-ins least privileged roles

Here are the least privileged roles you should use when performing tasks for [risky sign-ins](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) in Microsoft Entra ID Protection.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Read all configuration | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |
> | Read risky sign-ins | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |

## Security - Users flagged for risk least privileged roles

Here are the least privileged roles you should use when performing tasks for [users flagged for risk](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-notifications) in Microsoft Entra ID Protection.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Dismiss all events | [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |  |
> | Perform identity containment actions for SOC incident response | [Entra SOC Identity Responder](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#entra-soc-identity-responder) |  |
> | Read all configuration | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |
> | Read users flagged for risk | [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader) |  |

## Temporary Access Pass least privileged roles

Here are the least privileged roles you should use when performing tasks for [Temporary Access Pass](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Create, delete, or view a Temporary Access Pass for admins or members (except themselves) | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) |  |
> | Create, delete, or view a Temporary Access Pass for members (except themselves) | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) |  |
> | View a Temporary Access Pass details for a user (without reading the code itself) | [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader) |  |
> | Configure or update the Temporary Access Pass authentication method policy | [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) |  |

## Tenants least privileged roles

Here are the least privileged roles you should use when performing tasks in [Microsoft Entra tenants](https://learn.microsoft.com/en-us/entra/fundamentals/create-new-tenant).

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Create Microsoft Entra ID or Azure AD B2C Tenant | [Tenant Creator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator) |  |
> | Update Microsoft Entra tenant properties | [Billing Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) |  |
> | [Manage privacy statement and contact](https://learn.microsoft.com/en-us/entra/fundamentals/properties-area) | [Billing Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator) |  |

## Users least privileged roles

Here are the least privileged roles you should use when performing tasks for [users](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Add user to directory role | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | Add user to group | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Assign license | [License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Create guest user | [Guest Inviter](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#guest-inviter) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Reset guest user invite | [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Create user | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Delete users | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Invalidate refresh tokens of limited admins | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Invalidate refresh tokens of non-admins | [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) |  [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) <br/> [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) |
> | Invalidate refresh tokens of privileged admins | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) |  |
> | Read basic configuration | [Default user role](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions) |  |
> | Reset password for limited admins | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Reset password of non-admins | [Password Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#password-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Reset password of privileged admins | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) |  |
> | Revoke license | [License Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |
> | Update all properties except User Principal Name | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Update On-premises sync enabled property | [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) |  |
> | Update profile photos and people settings | [People Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#people-administrator) |  |
> | Update User Principal Name for limited admins | [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |  |
> | Update User Principal Name property on privileged admins | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) |  |
> | Update user settings - Default user role permissions | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | [Update user settings - Guest user access](https://learn.microsoft.com/en-us/entra/identity/users/users-restrict-guest-permissions) | [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) |  |
> | Update user settings - Administration center | [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) |  |
> | [Update user settings - LinkedIn account connections](https://learn.microsoft.com/en-us/entra/identity/users/linkedin-integration) | [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) |  |
> | [Update user settings - Show keep user signed in](../../fundamentals/how-to-manage-stay-signed-in-prompt.yml) | [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) |  |
> | Update Authentication methods | [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator) | [Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator) |

## Support least privileged roles

Here are the least privileged roles you should use when performing tasks for [support](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-get-support) in Microsoft Entra ID.

> | Task | Least privileged role | Additional roles |
> | ---- | --------------------- | ---------------- |
> | Submit support ticket | [Service Support Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#service-support-administrator) | [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)<br/>[Azure Information Protection Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#azure-information-protection-administrator)<br/>[Billing Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator)<br/>[Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)<br/>[Compliance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#compliance-administrator)<br/>[Dynamics 365 Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#dynamics-365-administrator)<br/>[Desktop Analytics Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#desktop-analytics-administrator)<br/>[Exchange Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator)<br/>[Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator)<br/>[Intune Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator)<br/>[Password Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#password-administrator)<br/>[Fabric Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#fabric-administrator)<br/>[Privileged Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-authentication-administrator)<br/>[SharePoint Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator)<br/>[Skype for Business Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#skype-for-business-administrator)<br/>[Teams Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#teams-administrator)<br/>[Teams Communications Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#teams-communications-administrator)<br/>[User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) |

## Next steps

- [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal)
- [Create a custom role in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create)
- [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
