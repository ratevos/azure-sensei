# How to customize a synchronization rule in Microsoft Entra Connect'

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-create-custom-sync-rule  
> Microsoft doc last updated: 04/09/2025


## **Recommended Steps**

You can use the synchronization rule editor to edit or create a new synchronization rule. You need to be an advanced user to make changes to synchronization rules. Any wrong changes may result in deletion of objects from your target directory. Please review the [Recommended Documents](#recommended-documents) section. To modify a synchronization rule, go through following steps:

* Launch the synchronization editor from the application menu in desktop as shown below:

    

* In order to customize a default synchronization rule, clone the existing rule by clicking the “Edit” button on the Synchronization Rules Editor, which will create a copy of the standard default rule and disable it. Save the cloned rule with a precedence less than 100.  Precedence determines what rule wins(lower numeric value) a conflict resolution if there's an attribute flow conflict.

    

* When modifying a specific attribute, ideally you should only keep the modifying attribute in the cloned rule.  Then enable the default rule so that modified attribute comes from cloned rule and other attributes are picked from default standard rule. 

* In the case where the calculated value of the modified attribute is NULL, in your cloned rule, and isn't NULL in the default standard rule then, the not NULL value will win and will replace the NULL value. If you don’t want a NULL value to be replaced with a not NULL value, then assign AuthoritativeNull in your cloned rule.

* To modify an **Outbound** rule, change filter from the synchronization rule editor.

## **Recommended Documents**
* [Microsoft Entra Connect Sync: Technical Concepts](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-technical-concepts)
* [Microsoft Entra Connect Sync: Understanding the architecture](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-architecture)
* [Microsoft Entra Connect Sync: Understanding Declarative Provisioning](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-declarative-provisioning)
* [Microsoft Entra Connect Sync: Understanding Declarative Provisioning Expressions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-declarative-provisioning-expressions)
* [Microsoft Entra Connect Sync: Understanding the default configuration](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-default-configuration)
* [Microsoft Entra Connect Sync: Understanding Users, Groups, and Contacts](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-user-and-contacts)
* [Microsoft Entra Connect Sync: Shadow attributes](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-syncservice-shadow-attributes)

## Next Steps
- [Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis).
- [What is hybrid identity?](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).
