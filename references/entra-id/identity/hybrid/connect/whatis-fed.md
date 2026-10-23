# What is federation with Microsoft Entra ID?

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-fed  
> Microsoft doc last updated: 04/09/2025


Federation is a collection of domains that have established trust. The level of trust may vary, but typically includes authentication and almost always includes authorization. A typical federation might include several organizations with established trust for shared access to a set of resources.

You can federate your on-premises environment with Microsoft Entra ID and use this federation for authentication and authorization. This sign-in method ensures that all user authentication occurs on-premises. This method allows administrators to implement more rigorous levels of access control. Federation with AD FS and PingFederate is available.

> [!TIP]
> If you decide to use Federation with Active Directory Federation Services (AD FS), you can optionally set up password hash synchronization as a backup in case your AD FS infrastructure fails.

## Next Steps

- [What is hybrid identity?](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity)
- [What is Microsoft Entra Connect and Connect Health?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect)
- [What is password hash synchronization?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-phs)
- [What is federation?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-fed)
- [What is single-sign on?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso)
- [How federation works](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-whatis)
- [Federation with PingFederate](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom#configuring-federation-with-pingfederate)
