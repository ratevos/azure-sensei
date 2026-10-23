# What is password hash synchronization with Microsoft Entra ID?

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-phs  
> Microsoft doc last updated: 04/09/2025

Password hash synchronization is one of the sign-in methods used to accomplish hybrid identity. Microsoft Entra Connect synchronizes a hash of a user's password from an on-premises Active Directory instance to a cloud-based Microsoft Entra instance.

Password hash synchronization is an extension to the directory synchronization feature implemented by Microsoft Entra Connect Sync. You can use this feature to sign in to Microsoft Entra services like Microsoft 365. You sign in to the service by using the same password you use to sign in to your on-premises Active Directory instance.

Password hash synchronization helps by reducing the number of passwords, your users need to maintain to just one. Password hash synchronization can:

* Improve the productivity of your users.
* Reduce your helpdesk costs.  

Password Hash Sync also enables [leaked credential detection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#leaked-credentials) for your hybrid accounts. Microsoft works alongside dark web researchers and law enforcement agencies to find publicly available username/password pairs. If any of these pairs match those of our users, the associated account is moved to high risk. 

>[!NOTE]
> Only new leaked credentials found after you enable PHS will be processed against your tenant. Verifying against previously found credential pairs is not performed.

Optionally, you can set up password hash synchronization as a backup if you decide to use [Federation with Active Directory Federation Services (AD FS)](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-whatis) as your sign-in method.

To use password hash synchronization in your environment, you need to:

* Install the Microsoft Entra Cloud Sync agent.  
* Configure directory synchronization between your on-premises Active Directory instance and your Microsoft Entra instance.
* Enable password hash synchronization.

For more information, see [What is hybrid identity?](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).

## Next Steps

- [What is hybrid identity?](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity)
- [What is Microsoft Entra Connect and Connect Health?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect)
- [What is pass-through authentication (PTA)?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta)
- [What is federation?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-fed)
- [What is single-sign on?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso)
- [How Password hash synchronization works](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-password-hash-synchronization)
