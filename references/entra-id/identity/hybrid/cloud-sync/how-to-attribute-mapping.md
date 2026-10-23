# Attribute mapping in Microsoft Entra Cloud Sync

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-attribute-mapping  
> Microsoft doc last updated: 04/09/2025

You can use the cloud sync attribute mapping feature to map attributes between your on-premises user or group objects and the objects in Microsoft Entra ID. 

 

 The following document guides you through attribute scoping with Microsoft Entra Cloud Sync for provisioning from Active Directory to Microsoft Entra ID.  If you're looking for information on attribute mapping from Microsoft Entra ID to AD, see [Configure Microsoft Entra ID to Active Directory provisioning](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory).

You can customize (change, delete, or create) the default attribute mappings according to your business needs. For a list of attributes that are synchronized, see [Attributes synchronized to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-sync-attributes-synchronized).

> [!NOTE]
> This article describes how to use the Microsoft Entra admin center to map attributes.  For information on using Microsoft Graph, see [Transformations](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-transformation).

## Understand types of attribute mapping
With attribute mapping, you control how attributes are populated in Microsoft Entra ID. Microsoft Entra ID supports four mapping types:

|Mapping Type|Description|
|-----|-----|
|**Direct**|The target attribute is populated with the value of an attribute of the linked object in Active Directory.|
|**Constant**|The target attribute is populated with a specific string that you specify.|
|**Expression**|The target attribute is populated based on the result of a script-like expression. For more information, see [Expression Builder](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-expression-builder) and [Writing expressions for attribute mappings in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-expressions).|
|**None**|The target attribute is left unmodified. However, if the target attribute is ever empty, it's populated with the default value that you specify.|

Along with these basic types, custom attribute mappings support the concept of an optional *default* value assignment. The default value assignment ensures that a target attribute is populated with a value if Microsoft Entra ID or the target object doesn't have a value. The most common configuration is to leave this blank.

## Schema updates and mappings
Cloud sync occasionally updates the schema and the list of default attributes that are [synchronized](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-sync-attributes-synchronized).  These default attribute mappings  are available for new installations but won't automatically be added to existing installations.  To add these mappings, you can follow the steps below.

  1. Click on **add attribute mapping**
  2. Select the Target attribute dropdown
  3. You should see the new attributes that are available here.

The list of new mappings that were added.

Attribute Added | Mapping Type | Added with Agent Version
| ----- | -----| -----|
|preferredDatalocation|Direct|1.1.359.0|
|EmployeeNumber|Direct|1.1.359.0|
|UserType|Direct|1.1.359.0|

For more information on how to map UserType, see [Map UserType with cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-map-usertype).

## Understand properties of attribute mappings

Along with the type property, attribute mappings support certain attributes.  These attributes depend on the type of mapping you have selected.  The following sections describe the supported attribute mappings for each of the individual types.  The following type of attribute mapping is available.
- Direct
- Constant
- Expression

### Direct mapping attributes
The following are the attributes supported by a direct mapping:

- **Source attribute**: The user attribute from the source system (example: Active Directory).
- **Target attribute**: The user attribute in the target system (example: Microsoft Entra ID).
- **Default value if null (optional)**: The value that is passed to the target system if the source attribute is null. This value is provisioned only when a user is created. It won't be provisioned when you're updating an existing user.  
- **Apply this mapping**:
  - **Always**: Apply this mapping on both user-creation and update actions.
  - **Only during creation**: Apply this mapping only on user-creation actions.

### Constant mapping attributes
The following are the attributes supported by a constant mapping:

- **Constant value**: The value that you want to apply to the target attribute.
- **Target attribute**: The user attribute in the target system (example: Microsoft Entra ID).
- **Apply this mapping**:
  - **Always**: Apply this mapping on both user-creation and update actions.
  - **Only during creation**: Apply this mapping only on user-creation actions.

### Expression mapping attributes
The following are the attributes supported by an expression mapping:

- **Expression**: This expression is the expression that is going to be applied to the target attribute.  For more information, see [Expression Builder](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-expression-builder) and [Writing expressions for attribute mappings in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-expressions).
-  **Default value if null (optional)**: The value that is passed to the target system if the source attribute is null. This value is provisioned only when a user is created. It won't be provisioned when you're updating an existing user. 
- **Target attribute**: The user attribute in the target system (example: Microsoft Entra ID).
 
- **Apply this mapping**:
  - **Always**: Apply this mapping on both user-creation and update actions.
  - **Only during creation**: Apply this mapping only on user-creation actions.

## Add an attribute mapping - AD to Microsoft Entra ID
Use the following steps for configuring attribute mapping with a [AD to Microsoft Entra configuration](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure).

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   
 3. Under **Configuration**, select your configuration.
 4. On the left, select **Attribute mapping**.
 5. At the top, ensure that you have the correct object type selected.  That is, user, group, or contact.
 6. Click **Add attribute mapping**.

 

 7. Select the mapping type. This can be one of the following:
     - **Direct**: The target attribute is populated with the value of an attribute of the linked object in Active Directory.
     - **Constant**: The target attribute is populated with a specific string that you specify.
     - **Expression**: The target attribute is populated based on the result of a script-like expression. 
     - **None**: The target attribute is left unmodified. 
    
 8. Depending on what you have selected in the previous step, different options  are available for filling in.  
 9. Select when to apply this mapping, and then select **Apply**.
 

 10. Back on the **Attribute mappings** screen, you should see your new attribute mapping.
 11. Select **Save schema**.  You'll be notified that once you save the schema, a synchronization occurs.  Click **OK**.
 

 12. Once the save is successful you'll see a notification on the right.

 

## Test your attribute mapping

To test your attribute mapping, you can use [on-demand provisioning](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-on-demand-provision): 

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   
 3. Under **Configuration**, select your configuration.
 4. On the left, select **Provision on demand**.
 5. Enter the distinguished name of a user and select the **Provision** button.
 
     

 6. A success screen appears with four green check marks. Any errors appear to the left.

   

## Next steps

- [Microsoft Entra Cloud Sync?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync)
- [Expressions for attribute mappings](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-expressions)
- [Expression builder with cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-expression-builder)
- [Attributes synchronized to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-sync-attributes-synchronized)
