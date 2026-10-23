# Configure Microsoft Entra for increased security

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/configure-security  
> Microsoft doc last updated: 04/30/2026


In Microsoft Entra, we group our security recommendations into multiple themes based on the Secure Future Initiative (SFI). This structure allows organizations to logically break up projects into related consumable chunks.

> [!TIP]
> Some organizations might take these recommendations exactly as written, while others might choose to make modifications based on their own business needs. In our initial release of this guidance, we focus on traditional [workforce tenants](https://learn.microsoft.com/en-us/entra/external-id/tenant-configurations#workforce-tenants). These workforce tenants are for your employees, internal business apps, and other organizational resources. 

We recommend that all of the following controls be implemented where licenses are available. These patterns and practices help to provide a foundation for other resources built on top of this solution. More controls will be added to this document over time.

## Automated assessment

Manually checking this guidance against a tenant's configuration can be time-consuming and error-prone. The Zero Trust Assessment transforms this process with automation to test for these security configuration items and more. Learn more in [What is the Zero Trust Assessment?](https://learn.microsoft.com/en-us/security/zero-trust/assessment/overview)

## Protect identities and secrets

Reduce credential-related risk by implementing modern identity standards.

| Check | Minimum required license |
|---|---|
| [Applications don't have client secrets configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#applications-dont-have-client-secrets-configured) | None (included with Microsoft Entra ID) |
| [Service principals don't have certificates or credentials associated with them](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#service-principals-dont-have-certificates-or-credentials-associated-with-them) | None (included with Microsoft Entra ID) |
| [Applications don't have certificates with expiration longer than 180 days](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#applications-dont-have-certificates-with-expiration-longer-than-180-days) | None (included with Microsoft Entra ID) |
| [Application certificates must be rotated on a regular basis](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#application-certificates-must-be-rotated-on-a-regular-basis) | None (included with Microsoft Entra ID) |
| [Enforce standards for app secrets and certificates](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#enforce-standards-for-app-secrets-and-certificates) | None (included with Microsoft Entra ID) |
| [Microsoft services applications don't have credentials configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#microsoft-services-applications-dont-have-credentials-configured) | None (included with Microsoft Entra ID) |
| [User consent settings are restricted](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#user-consent-settings-are-restricted) | None (included with Microsoft Entra ID) |
| [Admin consent workflow is enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#admin-consent-workflow-is-enabled) | None (included with Microsoft Entra ID) |
| [High Global Administrator to privileged user ratio](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#high-global-administrator-to-privileged-user-ratio) | None (included with Microsoft Entra ID) |
| [Administrative privileges are tightly limited to prevent compromise](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#administrative-privileges-are-tightly-limited-to-prevent-compromise) | Microsoft Entra ID P1 |
| [Application admin rights are constrained to specific Private Access apps](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#application-admin-rights-are-constrained-to-specific-private-access-apps) | Microsoft Entra Internet Access or Microsoft Entra Private Access |
| [Privileged accounts are cloud native identities](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#privileged-accounts-are-cloud-native-identities) | None (included with Microsoft Entra ID) |
| [All privileged role assignments are activated just in time and not permanently active](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#all-privileged-role-assignments-are-activated-just-in-time-and-not-permanently-active) | Microsoft Entra ID P2 |
| [All Microsoft Entra privileged role assignments are managed with PIM](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#all-microsoft-entra-privileged-role-assignments-are-managed-with-pim) | Microsoft Entra ID P2 |
| [Passkey authentication method enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#passkey-authentication-method-enabled) | None (included with Microsoft Entra ID) |
| [Security key attestation is enforced](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#security-key-attestation-is-enforced) | None (included with Microsoft Entra ID) |
| [Privileged accounts have phishing-resistant methods registered](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#privileged-accounts-have-phishing-resistant-methods-registered) | Microsoft Entra ID P1 |
| [Privileged Microsoft Entra built-in roles are targeted with Conditional Access policies to enforce phishing-resistant methods](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#privileged-microsoft-entra-built-in-roles-are-targeted-with-conditional-access-policies-to-enforce-phishing-resistant-methods) | Microsoft Entra ID P1 |
| [Conditional Access policies enforce strong authentication for private apps](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#conditional-access-policies-enforce-strong-authentication-for-private-apps) | Microsoft Entra Private Access |
| [Application Proxy applications require preauthentication to block anonymous access](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#application-proxy-applications-require-preauthentication-to-block-anonymous-access) | Microsoft Entra ID P1 |
| [Require password reset notifications for administrator roles](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#require-password-reset-notifications-for-administrator-roles) | Microsoft Entra ID P1 |
| [Block legacy authentication policy is configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#block-legacy-authentication-policy-is-configured) | Microsoft Entra ID P1 |
| [Temporary access pass is enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#temporary-access-pass-is-enabled) | Microsoft Entra ID P1 |
| [Restrict Temporary Access Pass to Single Use](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#restrict-temporary-access-pass-to-single-use) | Microsoft Entra ID P1 |
| [Migrate from legacy MFA and SSPR policies](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#migrate-from-legacy-mfa-and-sspr-policies) | Microsoft Entra ID P1 |
| [Block administrators from using SSPR](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#block-administrators-from-using-sspr) | Microsoft Entra ID P1 |
| [Self-service password reset doesn't use security questions](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#self-service-password-reset-doesnt-use-security-questions) | Microsoft Entra ID P1 |
| [SMS and Voice Call authentication methods are disabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#sms-and-voice-call-authentication-methods-are-disabled) | Microsoft Entra ID P1 |
| [Secure the MFA registration (My Security Info) page](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#secure-the-mfa-registration-my-security-info-page) | Microsoft Entra ID P1 |
| [Use cloud authentication](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#use-cloud-authentication) | Microsoft Entra ID P1 |
| [All users are required to register for MFA](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#all-users-are-required-to-register-for-mfa) | Microsoft Entra ID P2 |
| [Users have strong authentication methods configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#users-have-strong-authentication-methods-configured) | Microsoft Entra ID P1 |
| [Reduce the user-visible password surface area](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#reduce-the-user-visible-password-surface-area) | Microsoft Entra ID P1 |
| [User sign-in activity uses token protection](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#user-sign-in-activity-uses-token-protection) | Microsoft Entra ID P1 |
| [Token protection policies are configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#token-protection-policies-are-configured) | Microsoft Entra ID P1 |
| [All user sign-in activity uses phishing-resistant authentication methods](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#all-user-sign-in-activity-uses-phishing-resistant-authentication-methods) | Microsoft Entra ID P1 |
| [All sign-in activity comes from managed devices](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#all-sign-in-activity-comes-from-managed-devices) | Microsoft Entra ID P1 |
| [Security key authentication method enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#security-key-authentication-method-enabled) | None (included with Microsoft Entra ID) |
| [Privileged roles aren't assigned to stale identities](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#privileged-roles-arent-assigned-to-stale-identities) | Microsoft Entra ID P2 |
| [Microsoft Authenticator app shows sign-in context](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#microsoft-authenticator-app-shows-sign-in-context) | Microsoft Entra ID P1 |
| [Microsoft Authenticator app report suspicious activity setting is enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#microsoft-authenticator-app-report-suspicious-activity-setting-is-enabled) | Microsoft Entra ID P1 |
| [Password expiration is disabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#password-expiration-is-disabled) | Microsoft Entra ID P1 |
| [Smart lockout threshold set to 10 or less](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#smart-lockout-threshold-set-to-10-or-less) | Microsoft Entra ID P1 |
| [Smart lockout duration is set to a minimum of 60](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#smart-lockout-duration-is-set-to-a-minimum-of-60) | Microsoft Entra ID P1 |
| [Add organizational terms to the banned password list](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#add-organizational-terms-to-the-banned-password-list) | Microsoft Entra ID P1 |
| [Require multifactor authentication for device join and device registration using user action](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#require-multifactor-authentication-for-device-join-and-device-registration-using-user-action) | Microsoft Entra ID P1 |
| [Local Admin Password Solution is deployed](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#local-admin-password-solution-is-deployed) | Microsoft Entra ID P1 |
| [Entra Connect Sync is configured with Service Principal Credentials](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#entra-connect-sync-is-configured-with-service-principal-credentials) | None (included with Microsoft Entra ID) |
| [Directory sync account is locked down to specific named location](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#directory-sync-account-is-locked-down-to-specific-named-location) | Microsoft Entra ID P1 |
| [No usage of ADAL in the tenant](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#no-usage-of-adal-in-the-tenant) | None (included with Microsoft Entra ID) |
| [Block legacy Azure AD PowerShell module](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#block-legacy-azure-ad-powershell-module) | None (included with Microsoft Entra ID) |
| [Enable Microsoft Entra ID security defaults for free tenants](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-identities#enable-microsoft-entra-id-security-defaults-for-free-tenants) | None (included with Microsoft Entra ID) |

## Protect tenants and isolate production systems

| Check | Minimum required license |
|---|---|
| [Permissions to create new tenants are limited to the Tenant Creator role](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#permissions-to-create-new-tenants-are-limited-to-the-tenant-creator-role) | None (included with Microsoft Entra ID) |
| [Enable protected actions to secure Conditional Access policy creation and changes](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#enable-protected-actions-to-secure-conditional-access-policy-creation-and-changes) | Microsoft Entra ID P1 |
| [Guest access is limited to approved tenants](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guest-access-is-limited-to-approved-tenants) | Microsoft Entra ID Free |
| [Guests are not assigned high privileged directory roles](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guests-are-not-assigned-high-privileged-directory-roles) | Microsoft Entra ID Free<br>Microsoft Entra ID P2 or Microsoft ID Governance for PIM |
| [Guests can't invite other guests](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guests-cant-invite-other-guests) | Microsoft Entra ID Free |
| [Guests have restricted access to directory objects](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guests-have-restricted-access-to-directory-objects) | Microsoft Entra ID Free |
| [App instance property lock is configured for all applications](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#app-instance-property-lock-is-configured-for-all-applications) | Microsoft Entra ID Free |
| [Guests don't have long lived sign-in sessions](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guests-dont-have-long-lived-sign-in-sessions) | Microsoft Entra ID P1 |
| [Guest access is protected by strong authentication methods](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guest-access-is-protected-by-strong-authentication-methods) | Microsoft Entra ID Free<br>Microsoft Entra ID P1 recommended for Conditional Access |
| [Guest self-service sign-up via user flow is disabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guest-self-service-sign-up-via-user-flow-is-disabled) | Microsoft Entra ID Free |
| [Outbound cross-tenant access settings are configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#outbound-cross-tenant-access-settings-are-configured) | Microsoft Entra ID Free<br>Microsoft Entra ID P1 recommended for Conditional Access |
| [Guests don't own apps in the tenant](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#guests-dont-own-apps-in-the-tenant) |  None (included with Microsoft Entra ID) |
| [All guests have a sponsor](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#all-guests-have-a-sponsor) | Microsoft Entra ID Free |
| [Inactive guest identities are disabled or removed from the tenant](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#inactive-guest-identities-are-disabled-or-removed-from-the-tenant) | Microsoft Entra ID Free |
| [All entitlement management policies have an expiration date](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#all-entitlement-management-policies-have-an-expiration-date) | Microsoft Entra ID P2 or Microsoft ID Governance for entitlement managed and access reviews |
| [All entitlement management assignment policies that apply to external users require connected organizations](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#all-entitlement-management-assignment-policies-that-apply-to-external-users-require-connected-organizations) | Microsoft Entra ID P2 or Microsoft ID Governance for entitlement managed and access reviews |
| [All entitlement management assignment policies that apply to external users require approval](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#all-entitlement-management-assignment-policies-that-apply-to-external-users-require-approval) | Microsoft Entra ID P2 or Microsoft ID Governance for entitlement managed and access reviews |
| [All entitlement management packages that apply to guests have expirations or access reviews configured in their assignment policies](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#all-entitlement-management-packages-that-apply-to-guests-have-expirations-or-access-reviews-configured-in-their-assignment-policies) | Microsoft Entra ID P2 or Microsoft ID Governance for entitlement managed and access reviews |
| [Manage the local administrators on Microsoft Entra joined devices](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#manage-the-local-administrators-on-microsoft-entra-joined-devices) | None (included with Microsoft Entra ID) |
| [Restrict nonadministrator users from recovering the BitLocker keys for their owned devices](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-tenants#restrict-nonadministrator-users-from-recovering-the-bitlocker-keys-for-their-owned-devices) | None (included with Microsoft Entra ID) |

## Protect networks

Protect your network perimeter.

| Check | Minimum required license |
|---|---|
| [Named locations are configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#named-locations-are-configured) | Microsoft Entra ID P1 |
| [Tenant restrictions v2 policy is configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#tenant-restrictions-v2-policy-is-configured) | Microsoft Entra ID P1 |
| [Internet Access forwarding profile is enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#internet-access-forwarding-profile-is-enabled) | Microsoft Entra Internet Access |
| [Web content filtering policies are configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#web-content-filtering-policies-are-configured) | Microsoft Entra Internet Access |
| [Web content filtering uses category-based rules](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#web-content-filtering-uses-category-based-rules) | Microsoft Entra Internet Access |
| [Web content filtering policies are linked to security profiles](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#web-content-filtering-policies-are-linked-to-security-profiles) | Microsoft Entra Internet Access |
| [Web content filtering integrates with Conditional Access](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#web-content-filtering-integrates-with-conditional-access) | Microsoft Entra Internet Access |
| [Web content filtering blocks high-risk categories](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#web-content-filtering-blocks-high-risk-categories) | Microsoft Entra Internet Access |
| [TLS inspection is enabled and correctly configured for outbound traffic](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#tls-inspection-is-enabled-and-correctly-configured-for-outbound-traffic) | Microsoft Entra Internet Access |
| [TLS inspection bypass rules are regularly reviewed](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#tls-inspection-bypass-rules-are-regularly-reviewed) | Microsoft Entra Internet Access |
| [TLS inspection certificates have a sufficient validity period](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#tls-inspection-certificates-have-a-sufficient-validity-period) | Microsoft Entra Internet Access |
| [TLS inspection failure rate is below 1%](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#tls-inspection-failure-rate-is-below-1) | Microsoft Entra Internet Access |
| [TLS inspection custom bypass rules don't duplicate system bypass destinations](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#tls-inspection-custom-bypass-rules-dont-duplicate-system-bypass-destinations) | Microsoft Entra Internet Access |
| [Threat intelligence filtering protects internet traffic](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#threat-intelligence-filtering-protects-internet-traffic) | Microsoft Entra Internet Access |
| [File transfer policies are configured to prevent data exfiltration](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#file-transfer-policies-are-configured-to-prevent-data-exfiltration) | Microsoft Entra Internet Access |
| [AI Gateway protects enterprise generative AI applications from prompt injection attacks](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#ai-gateway-protects-enterprise-generative-ai-applications-from-prompt-injection-attacks) | Microsoft Entra Internet Access |
| [Global Secure Access cloud firewall protects branch office internet traffic](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#global-secure-access-cloud-firewall-protects-branch-office-internet-traffic) | Microsoft Entra Internet Access |
| [Internet traffic is inspected across all Secure Web Gateway defense layers](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#internet-traffic-is-inspected-across-all-secure-web-gateway-defense-layers) | Microsoft Entra Internet Access |
| [Network validation is configured through Universal Continuous Access Evaluation](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#network-validation-is-configured-through-universal-continuous-access-evaluation) | Microsoft Entra Internet Access or Microsoft Entra Private Access |
| [Global Secure Access client is deployed on all managed endpoints](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#global-secure-access-client-is-deployed-on-all-managed-endpoints) | Microsoft Entra Internet Access or Microsoft Entra Private Access |
| [Global Secure Access licenses are available in the tenant and assigned to users](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#global-secure-access-licenses-are-available-in-the-tenant-and-assigned-to-users) | Microsoft Entra Internet Access or Microsoft Entra Private Access |
| [Microsoft 365 traffic is actively flowing through Global Secure Access](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#microsoft-365-traffic-is-actively-flowing-through-global-secure-access) | Microsoft Entra Suite |
| [Universal tenant restrictions block unauthorized external tenant access](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#universal-tenant-restrictions-block-unauthorized-external-tenant-access) | Microsoft Entra Internet Access |
| [Conditional Access policies use compliant network controls](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#conditional-access-policies-use-compliant-network-controls) | Microsoft Entra ID P1 |
| [Global Secure Access signaling for Conditional Access is enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#global-secure-access-signaling-for-conditional-access-is-enabled) | Microsoft Entra Internet Access |
| [Network traffic is routed through Global Secure Access for security policy enforcement](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#network-traffic-is-routed-through-global-secure-access-for-security-policy-enforcement) | Microsoft Entra Internet Access or Microsoft Entra Private Access |
| [Traffic forwarding profiles are scoped to appropriate users and groups for controlled deployment](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#traffic-forwarding-profiles-are-scoped-to-appropriate-users-and-groups-for-controlled-deployment) | Microsoft Entra Internet Access or Microsoft Entra Private Access |
| [Private network connectors are active and healthy to maintain Zero Trust access to internal resources](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#private-network-connectors-are-active-and-healthy-to-maintain-zero-trust-access-to-internal-resources) | Microsoft Entra Private Access |
| [Private network connectors are running the latest version](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#private-network-connectors-are-running-the-latest-version) | Microsoft Entra Private Access |
| [At least two Private Access connectors are active and healthy per connector group](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#at-least-two-private-access-connectors-are-active-and-healthy-per-connector-group) | Microsoft Entra Private Access |
| [Private DNS is configured for internal name resolution](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#private-dns-is-configured-for-internal-name-resolution) | Microsoft Entra Private Access |
| [DNS traffic for internal domains is routed through Private Access](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#dns-traffic-for-internal-domains-is-routed-through-private-access) | Microsoft Entra Private Access |
| [Intelligent Local Access is enabled and configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#intelligent-local-access-is-enabled-and-configured) | Microsoft Entra Private Access |
| [Quick Access is enabled and bound to a connector](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#quick-access-is-enabled-and-bound-to-a-connector) | Microsoft Entra Private Access |
| [Quick Access is bound to a Conditional Access policy](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#quick-access-is-bound-to-a-conditional-access-policy) | Microsoft Entra Private Access |
| [Entra Private Access Application segments are defined to enforce least-privilege access](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#entra-private-access-application-segments-are-defined-to-enforce-least-privilege-access) | Microsoft Entra Private Access |
| [Domain controller RDP access is protected by phishing-resistant authentication through Global Secure Access](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#domain-controller-rdp-access-is-protected-by-phishing-resistant-authentication-through-global-secure-access) | Microsoft Entra Private Access |
| [Private Access sensors are enforcing strong authentication policies on domain controllers](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#private-access-sensors-are-enforcing-strong-authentication-policies-on-domain-controllers) | Microsoft Entra Private Access |
| [Quick Access has user or group assignments](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#quick-access-has-user-or-group-assignments) | Microsoft Entra Private Access |
| [All Private Access apps have user or group assignments](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-networks#all-private-access-apps-have-user-or-group-assignments) | Microsoft Entra Private Access |

## Protect engineering systems

Protect software assets and improve code security.

| Check | Minimum required license |
|---|---|
| [Emergency access accounts are configured appropriately](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#emergency-access-accounts-are-configured-appropriately) | Microsoft Entra ID P1 |
| [Global Administrator role activation triggers an approval workflow](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#global-administrator-role-activation-triggers-an-approval-workflow) | Microsoft Entra ID P2 |
| [Global Administrators don't have standing access to Azure subscriptions](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#global-administrators-dont-have-standing-access-to-azure-subscriptions) | None (included with Microsoft Entra ID) |
| [Creating new applications and service principals is restricted to privileged users](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#creating-new-applications-and-service-principals-is-restricted-to-privileged-users) | Microsoft Entra ID P1 |
| [Inactive applications don't have highly privileged Microsoft Graph API permissions](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#inactive-applications-dont-have-highly-privileged-microsoft-graph-api-permissions) | Microsoft Entra ID P1 |
| [Inactive applications don't have highly privileged built-in roles](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#inactive-applications-dont-have-highly-privileged-built-in-roles) | Microsoft Entra ID P1 |
| [App registrations use safe redirect URIs](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#app-registrations-use-safe-redirect-uris) | Microsoft Entra ID P1 |
| [Service principals use safe redirect URIs](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#service-principals-use-safe-redirect-uris) | Microsoft Entra ID P1 |
| [App registrations must not have dangling or abandoned domain redirect URIs](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#app-registrations-must-not-have-dangling-or-abandoned-domain-redirect-uris) | Microsoft Entra ID P1 |
| [Resource-specific consent is restricted](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#resource-specific-consent-is-restricted) | Microsoft Entra ID P1 |
| [Workload Identities are not assigned privileged roles](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#workload-identities-are-not-assigned-privileged-roles) | Microsoft Entra ID P1 |
| [Enterprise applications must require explicit assignment or scoped provisioning](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#enterprise-applications-must-require-explicit-assignment-or-scoped-provisioning) | Microsoft Entra ID P1 |
| [Enterprise applications have owners](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#enterprise-applications-have-owners) | None (included with Microsoft Entra ID) |
| [Limit the maximum number of devices per user to 10](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#limit-the-maximum-number-of-devices-per-user-to-10) | None (included with Microsoft Entra ID) |
| [Conditional Access policies for Privileged Access Workstations are configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-protect-engineering-systems#conditional-access-policies-for-privileged-access-workstations-are-configured) | Microsoft Entra ID P1 |

## Monitor and detect cyberthreats

Collect and analyze security logs and triage alerts.

| Check | Minimum required license |
|--- | --- |
| [Diagnostic settings are configured for all Microsoft Entra logs](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#diagnostic-settings-are-configured-for-all-microsoft-entra-logs) | Microsoft Entra ID P1 |
| [Privileged role activations have monitoring and alerting configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#privileged-role-activations-have-monitoring-and-alerting-configured) | Microsoft Entra ID P2 |
| [Activation alert for Global Administrator role assignments](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#activation-alert-for-global-administrator-role-assignments) | Microsoft Entra ID P2 |
| [Activation alert for all privileged role assignments](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#activation-alert-for-all-privileged-role-assignments) | Microsoft Entra ID P2 |
| [Privileged users sign in with phishing-resistant methods](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#privileged-users-sign-in-with-phishing-resistant-methods) | Microsoft Entra ID P1 |
| [All high-risk users are triaged](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#all-high-risk-users-are-triaged) | Microsoft Entra ID P2 |
| [All high-risk sign-ins are triaged](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#all-high-risk-sign-ins-are-triaged) | Microsoft Entra ID P2  |
| [All risky workload identities are triaged](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#all-risky-workload-identities-are-triaged) | Microsoft Entra ID P2 |
| [Tenant creation events are triaged](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#tenant-creation-events-are-triaged) | Microsoft Entra ID P1 |
| [All user sign-in activity uses strong authentication methods](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#all-user-sign-in-activity-uses-strong-authentication-methods) | Microsoft Entra ID P1 |
| [High priority Microsoft Entra recommendations are addressed](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#high-priority-microsoft-entra-recommendations-are-addressed) | Microsoft Entra ID P1 |
| [ID Protection notifications are enabled](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#id-protection-notifications-are-enabled) | Microsoft Entra ID P2 |
| [No legacy authentication sign-in activity](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#no-legacy-authentication-sign-in-activity) | Microsoft Entra ID P1 |
| [All Microsoft Entra recommendations are addressed](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#all-microsoft-entra-recommendations-are-addressed) | Microsoft Entra ID P1 |
| [Network access activity is visible to security operations for threat detection and response](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#network-access-activity-is-visible-to-security-operations-for-threat-detection-and-response) | Microsoft Entra ID P1 |
| [Network access logs are retained for security analysis and compliance requirements](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#network-access-logs-are-retained-for-security-analysis-and-compliance-requirements) | Microsoft Entra ID P1 |
| [Global Secure Access deployment logs are populated and reviewed](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect#global-secure-access-deployment-logs-are-populated-and-reviewed) | Microsoft Entra Internet Access or Microsoft Entra Private Access |

## Accelerate response and remediation

Improve security incident response and incident communications.

| Check | Minimum required license |
|---|---|
| [Workload Identities are configured with risk-based policies](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-response-remediation#workload-identities-are-configured-with-risk-based-policies) | Microsoft Entra Workload ID |
| [Restrict high risk sign-ins](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-response-remediation#restrict-high-risk-sign-ins) | Microsoft Entra ID P2 |
| [Restrict access to high risk users](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-response-remediation#restrict-access-to-high-risk-users) | Microsoft Entra ID P2 |

## AI

Secure AI agents and agent-based workloads with identity controls.

| Check | Minimum required license |
|---|---|
| [Require Microsoft Entra ID authentication to interact with agents](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai#require-microsoft-entra-id-authentication-to-interact-with-agents) | Microsoft Entra ID P1 |
| [Conditional Access policies cover both agent identities and agents' user accounts](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai#conditional-access-policies-cover-both-agent-identities-and-agents-user-accounts) | Microsoft Entra ID P1 |
| [Risk-based Conditional Access blocks risky agent identities](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai#risk-based-conditional-access-blocks-risky-agent-identities) | Microsoft Entra ID P2 |
| [Custom security attributes for agent identities are present](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai#custom-security-attributes-for-agent-identities-are-present) | None (included with Microsoft Entra ID) |
| [Identity governance for agent identity sponsors is configured](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai#identity-governance-for-agent-identity-sponsors-is-configured) | Microsoft Entra ID P1 |
| [Agent identities and blueprint principals have assigned technical owners and no disabled agents remain in the directory](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai#agent-identities-and-blueprint-principals-have-assigned-technical-owners-and-no-disabled-agents-remain-in-the-directory) | None (included with Microsoft Entra ID) |
| [AI administrative roles have assigned principals](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai#ai-administrative-roles-have-assigned-principals) | None (included with Microsoft Entra ID) |

## Related content

- [Microsoft Entra deployment plans](https://learn.microsoft.com/en-us/entra/architecture/deployment-plans)
- [Microsoft Entra operations reference guide](https://learn.microsoft.com/en-us/entra/architecture/ops-guide-intro)
