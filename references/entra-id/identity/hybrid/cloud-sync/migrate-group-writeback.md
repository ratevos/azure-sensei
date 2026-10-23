# Migrate Microsoft Entra Connect Sync Group Writeback v2 to Microsoft Entra Cloud Sync

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/migrate-group-writeback  
> Microsoft doc last updated: 09/29/2025


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

This article describes how to migrate Group Writeback by using Microsoft Entra Connect Sync (formerly Azure Active Directory Connect) to Microsoft Entra Cloud Sync. This scenario is *only* for customers who are currently using Microsoft Entra Connect Group Writeback v2. The process outlined in this article pertains only to cloud-created security groups that are written back with a universal scope.

This scenario is only supported for:

- Cloud-created [security groups](https://learn.microsoft.com/en-us/entra/fundamentals/concept-learn-about-groups#group-types).
- Groups written back to Active Directory with the scope of [universal](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope).

> [!IMPORTANT]
> During migration, don't remove written-back groups, the Group Writeback target OU, or related referenced objects from Microsoft Entra Connect Sync scope until Microsoft Entra Cloud Sync is configured and validated to provision those groups to Active Directory.
>
> The supported coexistence model is to keep Microsoft Entra Connect Sync aware of the existing written-back groups and use the `cloudNoFlow` and `JoinNoFlow` rules in this article to preserve the join relationship while Microsoft Entra Cloud Sync takes over group provisioning.
>
> `JoinNoFlow` isn't a full staging (read-only) mode. It prevents object adds, object deletes, and non-reference attribute updates. However, reference attribute updates, such as group membership references, can still flow for reference resolution. Removing groups or referenced objects from Microsoft Entra Connect Sync scope before cutover can cause Microsoft Entra Connect Sync to drop references or deprovision on-premises group objects unexpectedly.

Mail-enabled groups and distribution lists written back to Active Directory continue to work with Microsoft Entra Connect Group Writeback but revert to the behavior of Group Writeback v1. In this scenario, after you disable Group Writeback v2, all Microsoft 365 groups are written back to Active Directory independently of the **Writeback Enabled** setting in the Microsoft Entra admin center. For more information, see [Provision to Active Directory with Microsoft Entra Cloud Sync FAQ](reference-provision-to-active-directory-faq.yml).

## Prerequisites

- A Microsoft Entra account with at least a [Hybrid Identity administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) role.
 - An on-premises Active Directory account with at least domain administrator permissions.
     
   Required to access the `adminDescription` attribute and copy it to the `msDS-ExternalDirectoryObjectId` attribute.

 - On-premises Active Directory Domain Services environment that runs Windows Server 2022, Windows Server 2019, or Windows Server 2016.
     
   Required for the Active Directory Schema attribute `msDS-ExternalDirectoryObjectId`.

 - Provisioning agent with build version [1.1.1367.0](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-version-history) or later.
 - The provisioning agent must be able to communicate with the domain controllers on ports TCP/389 (LDAP) and TCP/3268 (global catalog).
     
   Required for global catalog lookup to filter out invalid membership references.

## Naming convention for groups written back

By default, Microsoft Entra Connect Sync uses the following format when naming groups are written back:

- **Default format:** `CN=Group_<guid>,OU=<container>,DC=<domain component>`
- **Example:** `CN=Group_3a5c3221-c465-48c0-95b8-e9305786a271,OU=WritebackContainer,DC=Contoso,DC=com`

To make it easier to find groups being written back from Microsoft Entra ID to Active Directory, Microsoft Entra Connect Sync added an option to write back the group name by using the cloud display name. To use this option, select **Writeback Group Distinguished Name with Cloud Display Name** during initial setup of Group Writeback v2. If this feature is enabled, Microsoft Entra Connect uses the following new format instead of the default format:

- **New format:** `CN=<display name>_<last 12 digits of object ID>,OU=<container>,DC=<domain component>`

- **Example:** `CN=Sales_e9305786a271,OU=WritebackContainer,DC=contoso,DC=com`

By default, Microsoft Entra Cloud Sync uses the new format, even if the Writeback Group Distinguished Name with Cloud Display Name feature isn't enabled in Microsoft Entra Connect Sync. If you use the default Microsoft Entra Connect Sync naming and then migrate the group so that it's managed by Microsoft Entra Cloud Sync, the group is renamed to the new format. Use the following section to allow Microsoft Entra Cloud Sync to use the default format from Microsoft Entra Connect.

### Use the default format

If you want Microsoft Entra Cloud Sync to use the same default format as Microsoft Entra Connect Sync, you need to modify the attribute flow expression for the `CN` attribute. The two possible mappings are:

|Expression|Syntax|Description|
|-----|-----|-----|
|Cloud sync default expression by using `DisplayName`|`Append(Append(Left(Trim([displayName]), 51), "_"), Mid([objectId], 25, 12))`|The default expression used by Microsoft Entra Cloud Sync (that is, the new format).|
|Cloud sync new expression without using `DisplayName`|`Append("Group_", [objectId])`|The new expression to use the default format from Microsoft Entra Connect Sync.|

For more information, see [Change other attribute mappings as needed](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory#change-other-attribute-mappings-as-needed).

## Step 1: Copy adminDescription to msDS-ExternalDirectoryObjectID

To validate group membership references, Microsoft Entra Cloud Sync must query the Active Directory global catalog for the `msDS-ExternalDirectoryObjectID` attribute. This indexed attribute replicates across all global catalogs within the Active Directory forest.

1. In your on-premises environment, open **ADSI Edit**.

1. Copy the value that's in the group's `adminDescription` attribute.

   

1. Paste the value in the `msDS-ExternalDirectoryObjectID` attribute.

   

You can use the following PowerShell script to help automate this step. This script takes all of the groups in the `OU=Groups,DC=Contoso,DC=com` container and copies the `adminDescription` attribute value to the `msDS-ExternalDirectoryObjectID` attribute value. Before you use this script, update the variable `$gwbOU` with the `DistinguishedName` value of your group writeback's target organizational unit (OU).

```powershell

# Provide the DistinguishedName of your Group Writeback target OU
$gwbOU = 'OU=Groups,DC=Contoso,DC=com'

# Get all groups written back to Active Directory
$properties = @('displayName', 'Samaccountname', 'adminDescription', 'msDS-ExternalDirectoryObjectID')
$groups = Get-ADGroup -Filter * -SearchBase $gwbOU -Properties $properties | 
    Where-Object {$_.adminDescription -ne $null} |
        Select-Object $properties

# Set msDS-ExternalDirectoryObjectID for all groups written back to Active Directory 
foreach ($group in $groups) {
    Set-ADGroup -Identity $group.Samaccountname -Add @{('msDS-ExternalDirectoryObjectID') = $group.adminDescription}
} 

```

You can use the following PowerShell script to check the results of the preceding script. You can also confirm that all groups have the `adminDescription` value equal to the `msDS-ExternalDirectoryObjectID` value.

```powershell

# Provide the DistinguishedName of your Group Writeback target OU
$gwbOU = 'OU=Groups,DC=Contoso,DC=com'

# Get all groups written back to Active Directory
$properties = @('displayName', 'Samaccountname', 'adminDescription', 'msDS-ExternalDirectoryObjectID')
$groups = Get-ADGroup -Filter * -SearchBase $gwbOU -Properties $properties | 
    Where-Object {$_.adminDescription -ne $null} |
        Select-Object $properties

$groups | select displayName, adminDescription, 'msDS-ExternalDirectoryObjectID', @{Name='Equal';Expression={$_.adminDescription -eq $_.'msDS-ExternalDirectoryObjectID'}}

```

## Step 2: Place the Microsoft Entra Connect Sync server in staging mode and disable the sync scheduler

1. Start the Microsoft Entra Connect Sync wizard.
1. Select **Configure**.
1. Select **Configure staging mode** and select **Next**.
1. Enter Microsoft Entra credentials.
1. Select the **Enable staging mode** checkbox and select **Next**.
  
   
 
1. Select **Configure**.
1. Select **Exit**.

   

1. On your Microsoft Entra Connect server, open a PowerShell prompt as an administrator.
1. Disable the sync scheduler:

   ``` PowerShell 
   Set-ADSyncScheduler -SyncCycleEnabled $false  
   ``` 

## Step 3: Create a custom group inbound rule

In the Microsoft Entra Connect Synchronization Rules Editor, create an inbound sync rule that targets cloud-created groups that are currently mastered in Microsoft Entra ID and have a `NULL` mail attribute. This inbound sync rule is a join rule that sets the `cloudNoFlow` attribute to `True`.

The purpose of this rule is to flag these groups so Microsoft Entra Connect Sync continues to recognize them as joined objects after Group Writeback is disabled. This prevents the existing on-premises group objects from being treated as out of scope during the transition from Group Writeback in Microsoft Entra Connect Sync to group provisioning in Microsoft Entra Cloud Sync.

You can create this sync rule by using either the user interface or PowerShell with the provided script.

### Create a custom group inbound rule in the user interface

 1. On the **Start** menu, start the Synchronization Rules Editor.
 1. Under **Direction**, select **Inbound** from the dropdown list, and select **Add new rule**.
 1. On the **Description** page, enter the following values and select **Next**:

    - **Name**: Give the rule a meaningful name.
    - **Description**: Add a meaningful description.
    - **Connected System**: Choose the Microsoft Entra connector for which you're writing the custom sync rule.
    - **Connected System Object Type**: Select **group**.
    - **Metaverse Object Type**: Select **group**.
    - **Link Type**: Select **Join**.
    - **Precedence**: Provide a value that's unique in the system. We recommend that you use a value lower than 100 so that it takes precedence over the default rules.
    - **Tag:** Leave the field empty.

     

1. On the **Scoping filter** page, add the following values and select **Next**:

   |Attribute|Operator|Value|
   |-----|----|----|
   |`cloudMastered`|`EQUAL`|`true`|
   |`mail`|`ISNULL`||
   

     

1. On the **Join rules** page, select **Next**.
1. On the **Add transformations** page, for **FlowType**, select **Constant**. For **Target Attribute**, select **cloudNoFlow**. For **Source**, select **True**.

     

1. Select **Add**.

### Create a custom group inbound rule in PowerShell

1. On your Microsoft Entra Connect server, open a PowerShell prompt as an administrator.
1. Import the module.

   ``` PowerShell 
   Import-Module ADSync
   ```
1. Provide a unique value for the sync rule precedence (0-99).

   ``` PowerShell 
   # Provide the sync rule precedence (0-99)
   [int] $inboundSyncRulePrecedence = 88
   ```
1. Run the following script:

   ``` PowerShell 
    New-ADSyncRule  `
    -Name 'In from AAD - Group SOAinAAD coexistence with Cloud Sync' `
    -Identifier 'e4eae1c9-b9bc-4328-ade9-df871cdd3027' `
    -Description 'https://learn.microsoft.com/entra/identity/hybrid/cloud-sync/migrate-group-writeback' `
    -Direction 'Inbound' `
    -Precedence $inboundSyncRulePrecedence `
    -PrecedenceAfter '00000000-0000-0000-0000-000000000000' `
    -PrecedenceBefore '00000000-0000-0000-0000-000000000000' `
    -SourceObjectType 'group' `
    -TargetObjectType 'group' `
    -Connector 'b891884f-051e-4a83-95af-2544101c9083' `
    -LinkType 'Join' `
    -SoftDeleteExpiryInterval 0 `
    -ImmutableTag '' `
    -OutVariable syncRule

    Add-ADSyncAttributeFlowMapping  `
    -SynchronizationRule $syncRule[0] `
    -Source @('true') `
    -Destination 'cloudNoFlow' `
    -FlowType 'Constant' `
    -ValueMergeType 'Update' `
    -OutVariable syncRule

    New-Object  `
    -TypeName 'Microsoft.IdentityManagement.PowerShell.ObjectModel.ScopeCondition' `
    -ArgumentList 'cloudMastered','true','EQUAL' `
    -OutVariable condition0

    New-Object  `
    -TypeName 'Microsoft.IdentityManagement.PowerShell.ObjectModel.ScopeCondition' `
    -ArgumentList 'mail','','ISNULL' `
    -OutVariable condition1

    Add-ADSyncScopeConditionGroup  `
    -SynchronizationRule $syncRule[0] `
    -ScopeConditions @($condition0[0],$condition1[0]) `
    -OutVariable syncRule

    Add-ADSyncRule  `
    -SynchronizationRule $syncRule[0]

    Get-ADSyncRule  `
    -Identifier 'e4eae1c9-b9bc-4328-ade9-df871cdd3027'
   ``` 

## Step 4: Create a custom group outbound rule

You also need an outbound sync rule with a link type of `JoinNoFlow` and a scoping filter that selects groups where `cloudNoFlow` is set to `True`. 
This outbound rule maintains the join relationship after Group Writeback is disabled in Microsoft Entra Connect Sync, and prevents object adds, object deletes, and non-reference attribute updates from being exported for those groups.

Without this rule, previously written-back groups might be interpreted as no longer in scope and deleted from on-premises Active Directory during the next sync cycle. This rule is required to safely retire Group Writeback v2 while allowing Microsoft Entra Cloud Sync to take over group provisioning responsibilities.

You can create this sync rule by using either the user interface or PowerShell with the provided script.

### Create a custom group outbound rule in the user interface

 1. Under **Direction**, select **Outbound** from the dropdown list, and then select **Add rule**.
 1. On the **Description** page, enter the following values and select **Next**:

    - **Name**: Give the rule a meaningful name.
    - **Description**: Add a meaningful description.
    - **Connected System**: Choose the Active Directory connector for which you're writing the custom sync rule.
    - **Connected System Object Type**: Select **group**.
    - **Metaverse Object Type**: Select **group**.
    - **Link Type**: Select **JoinNoFlow**.
    - **Precedence**: Provide a value that's unique in the system. We recommend that you use a value lower than 100 so that it takes precedence over the default rules.
    - **Tag**: Leave the field empty.

    

1. On the **Scoping filter** page, for **Attribute**, select **cloudNoFlow**. For **Operator** select **EQUAL**. For **Value**, select **True**. Then select **Next**.

     

1. On the **Join rules** page, select **Next**.
1. On the **Transformations** page, select **Add**.

### Create a custom group inbound rule in PowerShell

1. On your Microsoft Entra Connect server, open a PowerShell prompt as an administrator.
1. Import the module.

   ``` PowerShell 
   Import-Module ADSync
   ```
1. Provide a unique value for the sync rule precedence (0-99).

   ``` PowerShell 
   # Provide the sync rule precedence (0-99)
   [int] $outboundSyncRulePrecedence = 89
   ```
   
1. Get the Active Directory connector for Group Writeback.

   ``` PowerShell 
   # Provide the name of your Active Directory Connector
   $connectorAD = Get-ADSyncConnector -Name "Contoso.com"
   ```
   
1. Run the following script:

   ``` PowerShell 
    New-ADSyncRule  `
    -Name 'Out to AD - Group SOAinAAD coexistence with Cloud Sync' `
    -Identifier '419fda18-75bb-4e23-b947-8b06e7246551' `
    -Description 'https://learn.microsoft.com/entra/identity/hybrid/cloud-sync/migrate-group-writeback' `
    -Direction 'Outbound' `
    -Precedence $outboundSyncRulePrecedence `
    -PrecedenceAfter '00000000-0000-0000-0000-000000000000' `
    -PrecedenceBefore '00000000-0000-0000-0000-000000000000' `
    -SourceObjectType 'group' `
    -TargetObjectType 'group' `
    -Connector $connectorAD.Identifier `
    -LinkType 'JoinNoFlow' `
    -SoftDeleteExpiryInterval 0 `
    -ImmutableTag '' `
    -OutVariable syncRule

    New-Object  `
    -TypeName 'Microsoft.IdentityManagement.PowerShell.ObjectModel.ScopeCondition' `
    -ArgumentList 'cloudNoFlow','true','EQUAL' `
    -OutVariable condition0

    Add-ADSyncScopeConditionGroup  `
    -SynchronizationRule $syncRule[0] `
    -ScopeConditions @($condition0[0]) `
    -OutVariable syncRule

    Add-ADSyncRule  `
    -SynchronizationRule $syncRule[0]

    Get-ADSyncRule  `
    -Identifier '419fda18-75bb-4e23-b947-8b06e7246551'
   ``` 

## Step 5: Use PowerShell to finish configuration

1. On your Microsoft Entra Connect server, open a PowerShell prompt as an administrator.
1. Import the `ADSync` module:

   ``` PowerShell 
   Import-Module ADSync
   ``` 

1. Run a full sync cycle:

   ``` PowerShell 
   Start-ADSyncSyncCycle -PolicyType Initial
   ``` 

1. Disable the Group Writeback feature for the tenant.

   > [!WARNING]
   > This operation is irreversible. After you disable Group Writeback v2, all Microsoft 365 groups are written back to Active Directory, independently of the **Writeback Enabled** setting in the Microsoft Entra admin center.
   ``` PowerShell 
   Set-ADSyncAADCompanyFeature -GroupWritebackV2 $false 
   ```
   
1. Run a full sync cycle again:

   ``` PowerShell 
   Start-ADSyncSyncCycle -PolicyType Initial
   ``` 

1. Reenable the sync scheduler:

   ``` PowerShell 
   Set-ADSyncScheduler -SyncCycleEnabled $true  
   ``` 

     

## Step 6: Remove the Microsoft Entra Connect Sync server from staging mode

1. Start the Microsoft Entra Connect Sync wizard.
1. Select **Configure**.
1. Select **Configure staging mode** and select **Next**.
1. Enter Microsoft Entra credentials.
1. Clear the **Enable staging mode** checkbox and select **Next**.
1. Select **Configure**.
1. Select **Exit**.

## Step 7: Configure Microsoft Entra Cloud Sync

Now that Microsoft Entra Connect Sync has the no-flow rules configured for the existing written-back groups, set up and configure Microsoft Entra Cloud Sync to take over provisioning of the security groups to Active Directory. For more information, see [Provision groups to Active Directory by using Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory).

Before you decommission Microsoft Entra Connect Sync Group Writeback, verify that Microsoft Entra Cloud Sync provisions the groups and maintains their memberships in Active Directory.

## Related content

- [Provision groups to Active Directory by using Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory)
- [Govern on-premises Active Directory-based apps (Kerberos) by using Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/govern-on-premises-groups)
- [Provisioning to Active Directory with Microsoft Entra Cloud Sync FAQ](reference-provision-to-active-directory-faq.yml)
