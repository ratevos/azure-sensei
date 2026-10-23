# Troubleshoot Microsoft Entra Connect install issues'

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-install-issues  
> Microsoft doc last updated: 04/09/2025


## **Recommended Steps**
Check which [Microsoft Entra Connect installation type](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-select-installation) is suitable for you. If you meet the criteria of express installation, then we highly recommend you to go with the express installation. The express installation gives you minimal options needed to finish the installation, and there's less likelihood of any issues. 

However, if you don’t meet the express installation criteria and must do the custom installation then here are some best practices you can follow to avoid common issues. For the sake of simplicity only selective options are mentioned here:

* Ensure you're an administrator on the machine on which you're installing Microsoft Entra Connect. Sign-in to the machine with same administrator credentials.
* Let all the options to be default on the following page, except for “Use an existing SQL Server”, if you want to use existing SQL Server. Here are [more details](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom) about how to use custom installation options. 

    

* On the following page, pick option “Create new AD account", to avoid any permission issues with existing account.

    

### **Common Issues**

* [Connectivity issues with on-premises Active Directory](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-adconnectivitytools).

* [Connectivity issues with online Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-connectivity).

* [Permission issues with on-premises Active Directory](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-configure-ad-ds-connector-account).

## **Recommended Documents**
* [Prerequisites for Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites)
* [Select which installation type to use for Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-select-installation)
* [Getting started with Microsoft Entra Connect using express settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-express)
* [Custom installation of Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom)
* [Microsoft Entra Connect: Upgrade from a previous version to the latest](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-upgrade-previous-version)
* [Microsoft Entra Connect: What is staging server?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-topologies#staging-server)
* [What is the `ADConnectivityTool` PowerShell module?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-adconnectivitytools)

## Next steps
- [Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis).
- [What is hybrid identity?](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity)
