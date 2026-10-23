# Exchange hybrid writeback with sync

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/exchange-hybrid-writeback  
> Microsoft doc last updated: 04/09/2025

A hybrid deployment offers organizations the ability to extend the feature-rich experience and administrative control they have with their existing on-premises Microsoft Exchange organization to the cloud. A hybrid deployment provides the seamless look and feel of a single Exchange organization between an on-premises Exchange organization and Exchange Online. 

To accomplish this scenario and allow your on-premises users to take full advantage of Exchange online, attributes from the cloud, must be written back to your on-premises users.  Both cloud sync or connect sync can write back the attributes.

 

## Cloud sync
You can enable this scenario using cloud sync by ensuring you're using the latest provisioning agent and following the documentation.  For more information, see [Exchange hybrid writeback with cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/exchange-hybrid)

## Connect sync
You can enable the connect sync scenario through the installer.  By selecting custom install, you can choose Exchange hybrid writeback.  For more information, see [custom install for connect sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom)

## Next steps
- [Exchange hybrid writeback with cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/exchange-hybrid)
- [Common scenarios](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Tools for synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/sync-tools)
- [Choosing the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/prerequisites)
