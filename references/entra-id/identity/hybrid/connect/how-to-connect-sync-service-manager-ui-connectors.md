# Connectors in the Microsoft Entra Connect Sync Service Manager UI'

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-service-manager-ui-connectors  
> Microsoft doc last updated: 04/09/2025


The Connectors tab is used to manage all systems the sync engine is connected to.

## Connector actions
| Action | Comment |
| --- | --- |
| Create |Not supported. For connecting additional AD forests, use the configuration wizard. |
| Properties |Read-only. Connector properties for connectivity, domain and OU filtering and attribute selection and anchors. |
| Delete <br> (connector or connector space) |Not supported. For removing AD forests, reinstall the Microsoft Entra Connect product.|
| [Configure Run Profiles](#configure-run-profiles) |Read-only. Connector run profiles.|
| Run |Starts a one-off connector run profile.|
| Stop |Stops a connector run profile.|
| Export Connector |Read-only. Exports the connector configuration.|
| Import Connector |Not supported. |
| Update Connector |Not supported. |
| Refresh Schema |Not supported. Use the "Refresh directory schema" task in the configuration wizard which also updates sync rules.|
| [Search Connector Space](#search-connector-space) |Finds objects and shows object data across the Metaverse and other connected sources.|

> [!WARNING]
> Deleting a connector or connector space is **not supported** and can have serious consequences for your hybrid identity environment. Don't use these actions as a troubleshooting step.

### Configure Run Profiles
This option allows you to see the run profiles configured for a Connector.

### Search Connector Space
The search connector space action is useful to find objects and troubleshoot data issues.

Start by selecting a **scope**. You can search based on data (RDN, DN, Anchor, Sub-Tree), or state of the object (all other options).  
  
If you, for example, do a Sub-Tree search, you get all objects in one OU.  
  
From this grid you can select an object, select **properties**, and [follow it](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-object-not-syncing) from the source connector space, through the metaverse, and to the target connector space.

### Changing the AD DS account password
If you change the account password, the Synchronization Service will no longer be able to import/export changes to on-premises AD.   You may see the following:

- The import/export step for the AD connector fails with "no-start-credentials" error.
- Under Windows Event Viewer, the application event log contains an error with Event ID 6000 and message “The management agent “contoso.com” failed to run because the credentials were invalid.”

To resolve the issue, update the AD DS user account using the following:

1. Start the Synchronization Service Manager (START → Synchronization Service).
</br>
2. Go to the **Connectors** tab.
3. Select the AD Connector which is configured to use the AD DS account.
4. Under Actions, select **Properties**.
5. In the pop-up dialog, select Connect to Active Directory Forest:
6. The Forest name indicates the corresponding on premises AD.
7. The User name indicates the AD DS account used for synchronization.
8. Enter the new password of the AD DS account in the Password textbox

9. Select OK to save the new password and restart the Synchronization Service to remove the old password from memory cache.

## Next steps
Learn more about the [Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis) configuration.

Learn more about [Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).
