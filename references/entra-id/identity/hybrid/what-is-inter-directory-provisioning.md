# What is inter-directory provisioning with Microsoft Entra ID?

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/what-is-inter-directory-provisioning  
> Microsoft doc last updated: 04/09/2025


A directory is a shared information infrastructure and is used for locating, managing, administering, and organizing items and network resources. Examples of applications that use directory services are Microsoft Active Directory and Microsoft Entra ID. Identities help directory systems make determinations such as who has access to what, and who is allowed to use specific resources.

Inter-directory provisioning is provisioning an identity between two different directory services systems. The most common scenario for inter-directory provisioning is when a user already in Active Directory is provisioned into Microsoft Entra ID. This provisioning can be accomplished by agents such as Microsoft Entra Connect Sync or Microsoft Entra Connect cloud provisioning.

Inter-directory provisioning allows us to create [hybrid identity](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity) environments.

<a name='what-types-of-inter-directory-provisioning-does-azure-ad-support'></a>

## What types of inter-directory provisioning does Microsoft Entra ID support

Microsoft Entra ID currently supports three methods for accomplishing inter-directory provisioning. These methods are:

- [Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync) -a new Microsoft agent designed to meet and accomplish your hybrid identity goals. It provides a light-weight inter -directory provisioning experience between Active Directory and Microsoft Entra ID and is configured via the portal.

- [Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect) - the Microsoft tool designed to meet and accomplish your hybrid identity, including inter-directory provisioning from Active Directory to Microsoft Entra ID.

- [Microsoft Identity Manager](https://learn.microsoft.com/en-us/microsoft-identity-manager/microsoft-identity-manager-2016) - Microsoft's on-premises identity and access management solution that helps you manage the users, credentials, policies, and access within your organization. Additionally, MIM provides advanced inter-directory provisioning to achieve hybrid identity environments for Active Directory, Microsoft Entra ID, and other directories.

### Key benefits

This capability of inter-directory provisioning offers the following significant business benefits:

- [Password hash synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-phs) - A sign-in method that synchronizes a hash of a users on-premises AD password with Microsoft Entra ID.
- [Pass-through authentication](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta) - A sign-in method that allows users to use the same password on-premises and in the cloud, but doesn't require the additional infrastructure of a federated environment.
- [Federation integration](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-whatis) - can be used to configure a hybrid environment using an on-premises AD FS infrastructure. It also provides AD FS management capabilities such as certificate renewal and more AD FS server deployments.
- [Synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis) - Responsible for creating users, groups, and other objects. Also for making sure identity information for your on-premises users and groups is matching the cloud. This synchronization also includes password hashes.
- [Health Monitoring](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect) - can provide robust monitoring and provide a central location in the [Microsoft Entra admin center](https://entra.microsoft.com) to view this activity. 

### Common scenarios
For a list of common hybrid synchronization scenarios, see [Common scenarios](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios).

## Next steps 
- [What is identity lifecycle management](https://learn.microsoft.com/en-us/entra/id-governance/scenarios/govern-the-employee-lifecycle)
- [What is provisioning?](https://learn.microsoft.com/en-us/entra/identity/hybrid/what-is-provisioning)
- [What is HR driven provisioning?](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/what-is-hr-driven-provisioning)
- [What is app provisioning?](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/user-provisioning)
