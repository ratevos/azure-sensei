# Microsoft Entra directory extensions for provisioning to AD

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/custom-attribute-mapping-entra-to-active-directory  
> Microsoft doc last updated: 08/11/2026


You can use directory extensions to extend the schema of users and groups, and then use those attributes for scoping and attribute mapping. If you're looking for directory extensions when provisioning from Active Directory to Microsoft Entra ID, see [Cloud sync directory extensions and custom attribute mapping](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/custom-attribute-mapping).

> [!IMPORTANT]
> Directory extensions for Microsoft Entra Cloud Sync are supported only for applications with the identifier URI `api://<tenantId>/CloudSyncCustomExtensionsApp` and the [Tenant Schema Extension App](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-directory-extensions#configuration-changes-in-azure-ad-made-by-the-wizard) created by Microsoft Entra Connect.

For step-by-step examples of extending the schema and then using directory extension attributes with cloud sync provisioning to Active Directory, see [Use directory extensions when provisioning to Active Directory](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/tutorial-directory-extension-group-provisioning). That article covers both users and groups.

## Ways to create directory extensions

You can create directory extensions in Microsoft Entra ID in several different ways. The following table provides links and additional information.

|Method|Description|URL|
|-----|-----|-----|
|Microsoft Graph|Create extensions using Microsoft Graph|[Create extensionProperty](https://learn.microsoft.com/en-us/graph/api/application-post-extensionproperty?view=graph-rest-1.0&tabs=http&preserve-view=true)|
|PowerShell|Create extensions using PowerShell|[New-MgApplicationExtensionProperty](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.applications/new-mgapplicationextensionproperty)|
|Microsoft Entra Connect|Create extensions using Microsoft Entra Connect|[Create an extension attribute using Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/user-provisioning-sync-attributes-for-mapping#create-an-extension-attribute-using-azure-ad-connect)|

## Next step

> [Use directory extensions when provisioning to Active Directory](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/tutorial-directory-extension-group-provisioning)

## Related content

- [Microsoft Entra schema and custom expressions](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/concept-attributes)
- [Microsoft Entra Connect Sync: Directory extensions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-directory-extensions)
- [Scoping filter and attribute mapping - Microsoft Entra ID to Active Directory](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure-entra-to-active-directory)
