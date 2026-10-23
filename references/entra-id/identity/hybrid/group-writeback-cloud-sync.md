# Group writeback with Microsoft Entra Cloud Sync

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/group-writeback-cloud-sync  
> Microsoft doc last updated: 04/09/2025


With the release of provisioning agent [1.1.1370.0](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-version-history#1113700), cloud sync now has the ability to perform group writeback. This feature means that cloud sync can provision groups directly to your on-premises Active Directory environment.  You can also now use identity governance features to govern access to AD-based applications, such as by including a [group in an entitlement management access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-group-writeback).

 

>[!IMPORTANT]
>The preview of Group Writeback v2 in Microsoft Entra Connect Sync is deprecated and no longer supported.
> 
>You can use Microsoft Entra Cloud Sync to provision cloud security groups to on-premises Active Directory Domain Services (AD DS).
> 
>If you use Group Writeback v2 in Microsoft Entra Connect Sync, you should move your sync client to Microsoft Entra Cloud Sync. To check if you're eligible to move to Microsoft Entra Cloud Sync, use the user synchronization wizard.
> 
>If you can't use Microsoft Cloud Sync as recommended by the wizard, you can run Microsoft Entra Cloud Sync side-by-side with Microsoft Entra Connect Sync. In that case, you might run Microsoft Entra Cloud Sync only to provision cloud security groups to on-premises AD DS.
> 
>If you provision Microsoft 365 groups to AD DS, you can keep using Group Writeback v1.

## Provision Microsoft Entra ID to Active Directory Domain Services - Prerequisites
The following prerequisites are required to implement provisioning groups to Active Directory Domain Services (AD DS).

## License requirements
Using this feature requires Microsoft Entra ID P1 licenses. To find the right license for your requirements, see [Compare generally available features of Microsoft Entra ID](https://www.microsoft.com/security/business/identity-access-management/azure-ad-pricing).

## General requirements

 - Microsoft Entra account with at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) role.
 - On-premises AD DS schema with the *msDS-ExternalDirectoryObjectId* attribute, which is available in Windows Server 2016 and later.  
 - Provisioning agent with build version [1.1.2334.0](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-version-history#1123340) or later.

 > [!NOTE]
 > The permissions to the service account are assigned during clean install only. If you're upgrading from the previous version, then permissions need to be assigned manually by using PowerShell: 
 > 
 > ```powershell
 > $credential = Get-Credential  
 >
 > Set-AADCloudSyncPermissions -PermissionType UserGroupCreateDelete -TargetDomain "FQDN of domain" -EACredential $credential
 > ```
 >If the permissions are set manually, you need to assign Read, Write, Create, and Delete all properties for all descendant Groups and User objects. 
 >
 >These permissions aren't applied to AdminSDHolder objects by default. For more information, see [Microsoft Entra provisioning agent gMSA PowerShell cmdlets](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-gmsa-cmdlets#grant-permissions-to-a-specific-domain). 

 - The provisioning agent must be installed on a server that runs Windows Server 2022, Windows Server 2019, or Windows Server 2016.
 - The provisioning agent must be able to communicate with one or more domain controllers on ports TCP/389 (LDAP) and TCP/3268 (Global Catalog).
     - Required for Global Catalog lookup to filter out invalid membership references
 - Microsoft Entra Connect Sync with build version [2.2.8.0](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history#2280)
     - Required to support on-premises user membership synchronized using Microsoft Entra Connect Sync
     - Required to synchronize `AD DS:user:objectGUID` to `AAD DS:user:onPremisesObjectIdentifier`

## Scale limits for Provisioning groups to Active Directory

Group Provision to Active Directory feature's performance is impacted by the size of the tenant and the number of groups and memberships that are in scope for provisioning to Active Directory. This section provides guidance on how to determine if GPAD supports your scale requirement and how to pick the right group scoping mode to achieve quicker initial and delta sync cycles. 

### What is not supported?
- Groups that are larger than 50K members aren't supported.
- The use of "All security groups" scoping without applying attribute scope filtering is not supported.

### Scale limits

|Scoping Mode  |Number of in-scope groups | Number of membership links (Direct members only)  |Notes  |
|---------|---------|---------|---------|
|"Selected security groups" mode    |  Up to 10K groups. The CloudSync pane in Microsoft Entra portal only allows selecting up to 999 groups as well as displaying up to 999 groups. If you need to add more than 1000 groups into scope, see: [Expanded group selection via API](#expanded-group-selection-via-api).    |    Up to 250K total members across all the groups **in scope**.     |  Use this scoping mode if your tenant exceeds ANY of these limits<br> 1. Tenant has more than 200k users<br>2. Tenant has more than 40K groups<br> 3. Tenant has more than 1M group memberships.|
|“All Security groups” mode with at least one attribute scoping filter.     |   Up to 20K groups.      |   Up to 500K total members across all the groups **in scope**.     |  Use this scoping mode if your tenant satisfies ALL the below limits:<br>1. Tenant has less than 200k users<br>2. Tenant has less than 40K groups<br>3. Tenant has less than 1M group memberships. |

### What to do if you exceed limits
Exceeding the recommended limits will slow initial and delta sync, possibly causing sync errors. If this happens, follow these steps:

### Too many groups or group members in ‘Selected security groups’ scoping mode:

Reduce the number of in-scope groups (target higher value groups), **or split provisioning into multiple, distinct jobs** with disjoint scopes.

### Too many groups or group members in ‘All security groups’ scoping mode:

Use **Selected security groups** scoping mode as recommended.

### Some group exceeds 50K members:

**Split membership** across multiple groups or adopt staged groups (for example, by region or business unit) to keep each group under the cap.

### Expanded group selection via API

If you need to select more than 999 groups, you must use the [Grant an appRoleAssignment for a service principal](https://learn.microsoft.com/en-us/graph/api/serviceprincipal-post-approleassignedto) API call. 

An example of the API calls is as follows:

```https
POST https://graph.microsoft.com/v1.0/servicePrincipals/{servicePrincipalID}/appRoleAssignedTo
Content-Type: application/json

{
  "principalId": "",
  "resourceId": "",
  "appRoleId": ""
}

```

where:

- **principalId**: Group object ID.
- **resourceId**: Job's service principal ID.
- **appRoleId**: Identifier of app role exposed by the resource service principal.

The following table is a list of App Role IDs for Clouds:

|Cloud  |appRoleId  |
|---------|---------|
|Public     |   1a0abf4d-b9fa-4512-a3a2-51ee82c6fd9f      |
|AzureUSGovernment     |  d8fa317e-0713-4930-91d8-1dbeb150978f       |
|AzureUSNatCloud     |   50a55e47-aae2-425c-8dcb-ed711147a39f      |
|AzureUSSecCloud     |   52e862b9-0b95-43fe-9340-54f51248314f     |

### More information

Here are more points to consider when you provision groups to AD DS.

- Group membership written to AD DS includes only members that have an AD DS account. Those members can be on-premises synchronized users, cloud-managed users that Cloud Sync provisions to AD DS because they're in scope of user provisioning, or other cloud-created security groups. A cloud-managed user that has no AD DS account is skipped.
- On-premises synchronized users must have the *onPremisesObjectIdentifier* attribute set on their account.
- The *onPremisesObjectIdentifier* must match a corresponding *objectGUID* in the target AD DS environment. 
- An on-premises user *objectGUID* attribute can be synchronized to a cloud user *onPremisesObjectIdentifier* attribute by using either sync client.
- Only global Microsoft Entra ID tenants can provision from Microsoft Entra ID to AD DS. Tenants such as B2C aren't supported.
- The provisioning job is scheduled to run every 20 minutes.

## Supported scenarios for group writeback with Microsoft Entra Cloud Sync
The following sections describe the supported scenarios for group writeback with Microsoft Entra Cloud Sync.

- [Migrate Microsoft Entra Connect Sync group writeback V2 to Microsoft Entra Cloud Sync](#migrate-microsoft-entra-connect-sync-group-writeback-v2-to-microsoft-entra-cloud-sync)
- [Govern on-premises Active Directory based apps (Kerberos) using Microsoft Entra ID Governance](#govern-on-premises-active-directory-based-apps-kerberos-using-microsoft-entra-id-governance)

###  Migrate Microsoft Entra Connect Sync group writeback V2 to Microsoft Entra Cloud Sync

**Scenario:**  Migrate group writeback using Microsoft Entra Connect Sync (formerly Azure AD Connect) to Microsoft Entra Cloud Sync. This scenario is **only** for customers who are currently using Microsoft Entra Connect group writeback v2. The process outlined in this document pertains only to cloud-created security groups that are written back with a universal scope. Mail-enabled groups and DLs written back using Microsoft Entra Connect group writeback V1 or V2 aren't supported.

For more information see [Migrate Microsoft Entra Connect Sync group writeback V2 to Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/migrate-group-writeback).

### Govern on-premises Active Directory based apps (Kerberos) using Microsoft Entra ID Governance 

**Scenario:**  Manage on-premises applications with Active Directory groups that are provisioned from and managed in the cloud. Microsoft Entra Cloud Sync allows you to fully govern application assignments in AD while taking advantage of Microsoft Entra ID Governance features to control and remediate any access related requests. 

For more information see [Govern on-premises Active Directory based apps (Kerberos) using Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/govern-on-premises-groups).

## Next steps
- [Provision groups to Active Directory using Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory)
- [Govern on-premises Active Directory based apps (Kerberos) using Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/govern-on-premises-groups)
- [Migrate Microsoft Entra Connect Sync group writeback V2 to Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/migrate-group-writeback)
- [Configure scoping filters and attribute mapping - Microsoft Entra ID to Active Directory](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory)
