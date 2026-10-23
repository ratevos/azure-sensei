# Enforce signed SAML authentication requests

> Source: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/howto-enforce-signed-saml-authentication  
> Microsoft doc last updated: 07/10/2025


SAML Request Signature Verification is a functionality that validates the signature of signed authentication requests. An App Admin can enable and disable the enforcement of signed requests and upload the public keys that should be used to do the validation.  

If enabled, Microsoft Entra ID validates the requests against the public keys configured. There are some scenarios where the authentication requests can fail:  

- Protocol not allowed for signed requests. Only SAML protocol is supported.  
- Request not signed, but verification is enabled.  
- No verification certificate configured for SAML request signature verification. For more information about the certificate requirements, see [Certificate signing options](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/certificate-signing-options).
- Signature verification failed.  
- Key identifier in request is missing and two most recently added certificates don't match with the request signature.  
- Request signed but algorithm missing.  
- No certificate matching with provided key identifier.
- Signature algorithm not allowed. Only RSA-SHA256 is supported.

> [!NOTE] 
> A `Signature` element in `AuthnRequest` elements is optional. If `Require Verification certificates` isn't checked, Microsoft Entra ID doesn't validate signed authentication requests if a signature is present. Requestor verification is provided for by only responding to registered Assertion Consumer Service URLs.

>  If `Require Verification certificates` is checked, SAML Request Signature Verification will work for SP-initiated(service provider/relying party initiated) authentication requests only. Only the application configured by the service provider will have the access to to the private and public keys for signing the incoming SAML Authentication Requests from the application. The public key should be uploaded to allow the verification of the request, in which case Microsoft Entra ID will have access to only the public key.

> Enabling `Require Verification certificates` will not allow IDP-initiated authentication requests (like SSO testing feature, MyApps or M365 app launcher) to be validated as the IDP would not possess the same private keys as the registered application.

## Prerequisites

To configure SAML request signature verification, you need:

- A Microsoft Entra user account. If you don't already have one, you can [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- One of the following roles: Cloud Application Administrator, Application Administrator, or owner of the service principal.

## Configure SAML Request Signature Verification

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator). 
1. Browse to **Entra ID** > **Enterprise apps** > **All applications**.
1. Enter the name of the existing application in the search box, and then select the application from the search results.
1. Navigate to **Single sign-on**.
1. In the **Single sign-on** screen, scroll to the subsection called **Verification certificates** under **SAML Certificates.** 
    
     
    
1. Select **Edit.**  

1. In the new pane, you're able to enable the verification of signed requests and opt-in for weak algorithm verification in case your application still uses RSA-SHA1 to sign the authentication requests.   

1. To enable the verification of signed requests, select **Require verification certificates** and upload a verification public key that matches with the private key used to sign the request. 
    
     

1. Once you have your verification certificate uploaded, select **Save**. 

1. When the verification of signed requests is enabled, the test experience is disabled as the service provider has to sign the request.  
    
     
    
1. If you want to see the current configuration of an enterprise application, you can navigate to the **Single Sign-on** screen and see the summary of your configuration under **SAML Certificates**. There you're able to see if the verification of signed requests is enabled and the count of Active and Expired verification certificates. 
    
     

## Related content

- Find out [How Microsoft Entra ID uses the SAML protocol](https://learn.microsoft.com/en-us/entra/identity-platform/saml-protocol-reference) 
- Learn the format, security characteristics, and contents of [SAML tokens in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/reference-saml-tokens)
