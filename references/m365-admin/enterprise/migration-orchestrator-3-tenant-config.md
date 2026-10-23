# Migration orchestrator source and tenant domain configuration

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/migration-orchestrator-3-tenant-config  
> Microsoft doc last updated: 02/25/2026


> [!IMPORTANT]
> Tenant-to-tenant migration is currently available in preview. Features and availability may change before general availability (GA).

## Prerequisites for source and target tenants

This article walks through all steps of preparing the tenants and users for a successful migration. Here are some other requirements we don't provide explicit steps for:

- Global administrator access for source and target admins on their respective tenant, which is required to manage the setup and migration.

- At least one mail-enabled security group is required in the source tenant.
  - These groups are used to:
    - Scope the list of users whose content can move from source tenant to the target tenant.
    - Inform the identity mapping service what users should be mapped.
  - This scoping allows the source tenant administrator to restrict access to a specific set of users whose content needs to be moved, preventing unintended users from being migrated or their data accessed.
- The Microsoft 365 tenant ID of your trusted partner organization. This tenant ID is used in the Organization Relationship DomainName field.

- To obtain the tenant ID of a subscription, sign in to the Microsoft 365 admin center and go to [Active Directory > Properties](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Properties). Select the copy icon for the Tenant ID property to copy it to the clipboard.

## Prepare both tenants for Mailbox migration

To prepare tenants for mailbox moves, see [Cross-tenant mailbox migration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-mailbox-migration#preparing-source-and-target-tenants).

## Prepare both tenants with Migration applications and permissions

To enable migration, add the applications for Cross-Tenant Migration Service, OneDrive Migration, Teams Chat Migration, and Teams Meeting Migration, add permissions to those applications, and run additional setup steps.

The following modules are prerequisites to importing the CrossTenantMigration module.

- Microsoft.Graph.Authentication

- Microsoft.Graph.Applications

- Microsoft.Graph.Identity.DirectoryManagement

- ExchangeOnlineManagement

- MicrosoftTeams

- Microsoft.Graph.Beta (minimum version 2.33.0)

Microsoft.Graph and Microsoft.Graph.Beta versions should all be the same.

For both tenants, perform the following steps:

1. Download the [CrossTenantMigration NuGet package](https://download.microsoft.com/download/1ded7541-fa8d-48f7-90c4-fa8a15a6b62b/CrossTenantMigration.nupkg)

2. Expand the CrossTenantMigration NuGet package and import the modules 

```powershell
Expand-Archive -Path ".\CrossTenantMigration.nupkg" -DestinationPath ".\CTModule" -Force

Import-Module -Name ".\CTModule\CrossTenantMigration" -Force
```

3. Set up the Cross-Tenant Migration Service Application on the **target tenant only**. Run `Grant-CTMSAppPermissions`

1. Set up the OneDrive Migration Application. Run `Grant-OneDriveAppPermissions`

5. Set up the Teams Chat Migration Application. Run `Grant-CTTMAppPermissions`

6. Set up the Teams Meeting Migration Application. On the source tenant, run `Grant-MMSAppPermissions -TenantType "source"` On the target tenant, run `Grant-MMSAppPermissions -TenantType "target"`

7. Turn on auto forwarding for meeting migration. Run `Enable-AutoForwardingMode`

1. Set calendar role-based access control (RBAC) roles on the **target tenant only.** Run `Set-CalendarRBACRoles`

## Prepare both tenants for OneDrive migration

> [!IMPORTANT]
> These instructions must be run from both the source and the target tenant.

The required setup steps for OneDrive Migration on both source and target are available in [Steps 1 - 3](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-onedrive-migration) of its public documentation. These steps establish trust for the tool and between tenants.

## Prepare both tenants for Teams Chat Migration

> [!IMPORTANT]
> These instructions must be run from both the source and the target tenant.
1. Install Microsoft Teams PowerShell: [Install Microsoft Teams PowerShell](https://learn.microsoft.com/en-us/MicrosoftTeams/teams-powershell-install).
2. Connect to Microsoft Teams PowerShell: `Connect-MicrosoftTeams`

3. Federated users must be allowed. Run the cmdlet:
`Set-CsTenantFederationConfiguration -AllowFederatedUsers $True`

4. If the tenant is a Trial tenant, it must also allow **External Access**. Run the cmdlet:
`Set-CsTenantFederationConfiguration -ExternalAccessWithTrialTenants "Allowed"`

5. Confirm the settings by running:
`Get-CsTenantFederationConfiguration`

## Prepare both tenants for Identity Mapping

> [!IMPORTANT]
> These instructions must be run from both the source and the target tenant.

Running Identity Mapping is a required step for migrating user data. Cross-Tenant Identity Mapping (CTIM) is a tool that allows source users to be mapped one-to-one to target users. It edits the users' properties, so they have the correct properties to successfully migrate. It also maintains a mapping file to reference so that the data for the correct source users is migrated to the correct target users.

To learn more about Identity Mapping, see [Cross-Tenant Identity Mapping](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-identity-mapping).

> [!IMPORTANT]
> Use CTIM after creating target users and before migrating data to ensure accuracy and avoid manual errors.

## What permissions are added?

When you run the tenant configuration steps, there are many permissions added to your tenant and applications.

### Cross-Tenant Migration Service (CTMS) permissions

The CrossTenantMigration Production AAD app is added with service principals. The Resource Identity Mapping service app service principals are added. The identity mapping service app role is granted to the CTMS app.

### OneDrive permissions

The following are retrieved when setting permissions: the SharePoint Online (SPO) resource app service principal, the migration app service principal, and the cross-tenant identity mapping (CTIM) app service principal.

### Teams Chat Migration (CTTM) permissions

The CTTM permissions granted are as follows:

1. Cross Tenant Teams Migration app role
1. Identity Mapping Service app role
1. Chat.Create
1. Chat.Read.All
1. Teamwork.Migrate.All
1. ChatMember.ReadWrite.All
1. User.Read.All
1. CrossTenantMigrationAuthorization-Internal.Read

### Teams Meeting Migration (MMS) permissions

1. Grant-MMSAppPermissions adds Service Principals for:

   1. Cross Tenant Teams Migration app
   
   1. Meeting Migration Service app
   1. Identity Mapping Service app
1. Grant-MMSAppPermissions adds App Roles for:
   1. Cross Tenant Teams Migration app role from Cross Tenant Teams Migration app assigned to target Meeting Migration Service App
   1. Identity Mapping Service app role from Identity Mapping Service app to target Meeting Migration Service app
   1. CrossTenantMigrationAuthorization-Internal.Read
1. Grant-MMSAppPermissions adds the Graph permissions for:
   1. Online.ReadWrite.All
   1. User.Read.All
   1. RoleManagement.Read.Directory
   1. Chat.ReadBasic.All
   1. Application.Read.All
1. Grant-MMSAppPermissions also adds the Exchange Admin Directory Role and Application access policies to MMS Application.

1. Enable-AutoForwardingMode turns autoforwarding is set to On for Default Outbound Spam Filter.

1. Set-CalendarRBACRoles assigns an RBAC role to the MMS App to allow Calendar Read Write Permissions.

### Cross-Tenant Migration Service (CTMS) permissions

The CrossTenantMigration Production Azure Active Directory (AAD) App is added with service principals. The Resource Identity Mapping service app service principals are added. The Identity Mapping service app role is granted to the CTMS app.

## Next steps

For information on preparing users for migration, see [Preparing users for tenant-to-tenant migration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/migration-orchestrator-4-user-prep).
