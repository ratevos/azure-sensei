# Understand Microsoft Entra Connect Sync

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis  
> Microsoft doc last updated: 10/06/2026

Microsoft Entra Connect Sync synchronizes identity data between your on-premises directories and Microsoft Entra ID. It includes an on-premises sync engine and a service component in Microsoft Entra ID. This article explains how Connect Sync works and how to customize it.

This topic is the home for **Microsoft Entra Connect Sync** (also called **sync engine**) and lists links to all other topics related to it. For links to Microsoft Entra Connect, see [Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).

The sync service consists of two components, the on-premises **Microsoft Entra Connect Sync** component and the service side in Microsoft Entra ID called **Microsoft Entra Connect Sync service**.

> [!IMPORTANT]
> Microsoft Entra Cloud Sync is a cloud-managed service for synchronizing users, groups, contacts, and devices from Active Directory to Microsoft Entra ID. It uses the Microsoft Entra provisioning agent instead of the Microsoft Entra Connect application. Microsoft Entra Cloud Sync is replacing Microsoft Entra Connect Sync, which will be retired after Cloud Sync has full functional parity with Connect Sync. The remainder of this article describes Microsoft Entra Connect Sync. Review Cloud Sync capabilities before deploying Connect Sync.
>
> For device synchronization, see [Configure device sync with Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync).
>
> To find out if you are already eligible for cloud sync, please verify your requirements in [this wizard](https://admin.microsoft.com/adminportal/home?Q=setupguidance#/modernonboarding/identitywizard).
>
> To learn more about Cloud Sync, read [What is Microsoft Entra Cloud Sync?](https://learn.microsoft.com/en-us/azure/active-directory/cloud-sync/what-is-cloud-sync) or watch this [short video](https://learn-video.azurefd.net/vod/player?id=2b0047aa-84ba-430d-8ce9-39cfdc55276d).
>

<a name='azure-ad-connect-sync-topics'></a>

## Feature and configuration reference
| Topic | What it covers and when to read |
| --- | --- |
| **Microsoft Entra Connect Sync fundamentals** | |
| [Understanding the architecture](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-architecture) |For those of you who are new to the sync engine and want to learn about the architecture and the terms used. |
| [Technical concepts](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-technical-concepts) |A short version of the architecture topic and briefly explains the terms used. |
| [Topologies for Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-topologies) |Describes the different topologies and scenarios the sync engine supports. |
| **Custom configuration** | |
| [Running the installation wizard again](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-installation-wizard) |Explains what options you have available when you run the Microsoft Entra Connect installation wizard again. |
| [Understanding Declarative Provisioning](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-declarative-provisioning) |Describes the configuration model called declarative provisioning. |
| [Understanding Declarative Provisioning Expressions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-declarative-provisioning-expressions) |Describes the syntax for the expression language used in declarative provisioning. |
| [Understanding the default configuration](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-default-configuration) |Describes the out-of-box rules and the default configuration. Also describes how the rules work together for the out-of-box scenarios to work. |
| [Understanding Users and Contacts](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-user-and-contacts) |Continues on the previous topic and describes how the configuration for users and contacts works together, in particular in a multi-forest environment. |
| [How to make a change to the default configuration](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-change-the-configuration) |Walks you through how to make a common configuration change to attribute flows. |
| [Best practices for changing the default configuration](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-best-practices-changing-default-configuration) |Support limitations and for making changes to the out-of-box configuration. |
| [Configure Filtering](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-configure-filtering) |Describes the different options for how to limit which objects are being synchronized to Microsoft Entra ID and step-by-step how to configure these options. |
| **Features and scenarios** | |
| [Prevent accidental deletes](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-prevent-accidental-deletes) |Describes the *prevent accidental deletes* feature and how to configure it. |
| [Scheduler](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-scheduler) |Describes the built-in scheduler, which is importing, synchronizing, and exporting data. |
| [Implement password hash synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-password-hash-synchronization) |Describes how password synchronization works, how to implement, and how to operate and troubleshoot. |
| [Device writeback](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-device-writeback) |Describes how device writeback works in Microsoft Entra Connect. |
| [Directory extensions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-directory-extensions) |Describes how to extend the Microsoft Entra schema with your own custom attributes. |
| [Microsoft 365 PreferredDataLocation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-preferreddatalocation) |Describes how to put the user's Microsoft 365 resources in the same region as the user. |
| **Sync Service** | |
| [Microsoft Entra Connect Sync service features](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-syncservice-features) |Describes the sync service side and how to change sync settings in Microsoft Entra ID. |
| [Duplicate attribute resiliency](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-syncservice-duplicate-attribute-resiliency) |Describes how to enable and use **userPrincipalName** and **proxyAddresses** duplicate attribute values resiliency. |
| **Operations and UI** | |
| [Synchronization Service Manager](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-service-manager-ui) |Describes the Synchronization Service Manager UI, including [Operations](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-service-manager-ui-operations), [Connectors](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-service-manager-ui-connectors), [Metaverse Designer](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-service-manager-ui-mvdesigner), and [Metaverse Search](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-service-manager-ui-mvsearch) tabs. |
| [Operational tasks and considerations](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-staging-server) |Describes operational concerns, such as disaster recovery. |
| **How To...** | |
| [Reset the Microsoft Entra account](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-azureadaccount) |How to reset the credentials of the service account used to connect from Microsoft Entra Connect Sync to Microsoft Entra ID. |
| **More information and references** | |
| [Ports](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-ports) |Lists which ports you need to open between the sync engine and your on-premises directories and Microsoft Entra ID. |
| [Attributes synchronized to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-sync-attributes-synchronized) |Lists all attributes being synchronized between on-premises AD and Microsoft Entra ID. |
| [Functions Reference](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-sync-functions-reference) |Lists all functions available in declarative provisioning. |

## Additional Resources
* [Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity)
