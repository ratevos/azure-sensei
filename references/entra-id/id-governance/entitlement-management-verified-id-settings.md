# Configure Verified ID settings for an access package in entitlement management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-verified-id-settings  
> Microsoft doc last updated: 10/17/2024


When setting up an access package policy, admins can specify whether it’s for users in the directory, connected organizations, or any external user. Entitlement Management determines if the person requesting the access package is within the scope of the policy. 

Sometimes you might want users to present extra identity proofs during the request process such as a training certification, work authorization, or citizenship status. As an access package manager, you can require that requestors present a verified ID containing those credentials from a trusted issuer. Approvers can then quickly view if a user’s verifiable credentials were validated at the time that the user presented their credentials and submitted the access package request. 

As an access package manager, you can include verified ID requirements for an access package at any time by editing an existing policy or adding a new policy for requesting access. 

>[!VIDEO https://www.youtube.com/embed/gH9z6amIlv8]

This article describes how to configure the verified ID requirement settings for an access package.

## Prerequisites

Before you begin, you must set up your tenant to use the [Microsoft Entra Verified ID service](https://learn.microsoft.com/en-us/entra/verified-id/decentralized-identifier-overview). You can find detailed instructions on how to do that here: [Configure your tenant for Microsoft Entra Verified ID](https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-configure-tenant-quick). 

## License requirements

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Create an access package with verified ID requirements

To add a verified ID requirement to an access package, you must start from the access package’s requests tab. Follow these steps to add a verified ID requirement to a new access package.

**Prerequisite role**: Global Administrator

> [!NOTE]
> Identity Governance Administrator, User Administrator, Catalog owner, or Access package manager will be able to add verified ID requirements to access packages soon.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator).

1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. On the Access packages page, select **+ New access package**.

1. On the **Requests** tab, scroll to the **Required Verified Ids** section.

1. Select **+ Add issuer** and choose an issuer from the Microsoft Entra Verified ID network. If you want to issue your own credentials to users, see: [Issue Microsoft Entra Verified ID credentials from an application](https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-configure-issuer).
    

1. Select the **credential type(s)** you want users to present during the request process.
    
    > [!NOTE]
    > If you select multiple credential types from one issuer, users are required to present credentials of all selected types. Similarly, if you include multiple issuers, users are required to present credentials from each of the issuers you include in the policy. To give users the option of presenting different credentials from various issuers, configure separate policies for each issuer/credential type you accept.
1. Select **Add** to add the verified ID requirement to the access package policy.
1. If you want users to complete a Face Check, select **Require Face Check**. This asks users requesting the access package to perform a real-time, privacy compliant selfie check against the photo that is stored on their Verified ID. Once you select the checkbox, it asks you to select the claim name that maps to the photo on the ID. For more information on Face Check, see [Use Face Check with Microsoft Entra Verified ID](https://learn.microsoft.com/en-us/entra/verified-id/using-facecheck).

    
   
1. Once you finish configuring the rest of the settings, you can review your selections on the **Review + create** tab. You can see all verified ID requirements for this access package policy in the **Verified IDs** section.
    

## Request an access package with verified ID requirements

Once an access package is configured with a verified ID requirement, end-users who are within the scope of the policy are able to request access using the My Access portal. Similarly, approvers are able to see the claims of the VCs presented by requestors when reviewing requests for approval.

The requestor steps are as follows:

1. Go to [`myaccess.microsoft.com`](https://myaccess.microsoft.com) and sign in.

1. Search for the access package you want to request access to (you can browse the listed packages or use the search bar at the top of the page) and select **Request**.

1. If the access package requires you to present a verified ID, you should see a grey information banner as shown here:
    
1. Select **Request Access**. You should now see a QR code. Use your phone to scan the QR code. This launches Microsoft Authenticator, where you're prompted to share your credentials.
    

1. If Face Check is required for the access package, the requesting user needs to perform a real-time selfie check against the photo stored on their Verified ID. Face Check protects user privacy by sharing only the match results and not any sensitive identity data.

1. After you share your credentials, My Access will automatically take you to the next step of the request process.

## Entitlement Management and Verified ID Security Partner integration
 
 
1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator).
 
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.
 
1. On the Access packages page, select **+ New access package**.
 
1. On the **Requests** tab, scroll to the **Required Verified Ids** section.
 
1. Select **+ Add issuer** and choose an issuer from the Microsoft Entra Verified ID network. If you want to issue your own credentials to users, see: [Issue Microsoft Entra Verified ID credentials from an application](https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-configure-issuer).
    
 
1. Step1 allows the selection of issuers under two types - "Select the type of issuer".
    1. Microsoft Entra Verified ID Network - this could be any Microsoft Entra Verified ID issuer from the drop-down list
        
    1. Security Partners (Third Party providers) - Government ID verification partners that are available via [Microsoft Security Store](https://learn.microsoft.com/en-us/security/store/what-is-security-store) integration. This is a simple select to configure option where you could add presentation of Verified ID issued from one of the selected IDV partners. The following drop-down selection requires the administrator to purchase the respective Identity verification offer from the partner
        
 
1. For "Microsoft Entra Verified ID Network" selection in Step1: Search for the issuer and then Select the **credential type(s)** you want users to present during the request process.
 
1. For "Security Partners (Third Party providers)" selection in Step1, If the admin is selecting the issuer for the first time, they'll get a link to Security Store to purchase the offer.
    
    > [!NOTE]
    > If you select multiple credential types from one issuer, users are required to present credentials of all selected types. Similarly, if you include multiple issuers, users are required to present credentials from each of the issuers you include in the policy. To give users the option of presenting different credentials from various issuers, configure separate policies for each issuer/credential type you accept.
1. Select **Add** to add the verified ID requirement to the access package policy.
 
1. If you want users to complete a Face Check, select **Require Face Check**. This asks users requesting the access package to perform a real-time, privacy compliant selfie check against the photo that is stored on their Verified ID. Once you select the checkbox, it asks you to select the claim name that maps to the photo on the ID. For more information on Face Check, see: [Using Face Check with Microsoft Entra Verified ID and unlocking high assurance verifications at scale](https://learn.microsoft.com/en-us/entra/verified-id/using-facecheck).
    
1. Complete rest of the settings for this access package policy.

## Next steps

- [Delegate access governance to access package managers](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate-managers)
- [What's new in Microsoft Entra Verified ID](https://learn.microsoft.com/en-us/entra/verified-id/whats-new)
- [What is Microsoft Security Store?](https://learn.microsoft.com/en-us/security/store/what-is-security-store)
- [Microsoft Entra Verified ID Identity Verification partners](https://learn.microsoft.com/en-us/entra/verified-id/idv-partners)
