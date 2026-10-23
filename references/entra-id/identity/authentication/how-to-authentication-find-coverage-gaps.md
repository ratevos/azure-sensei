# Find and address gaps in strong authentication coverage for your administrators in Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-find-coverage-gaps  
> Microsoft doc last updated: 03/04/2025


Requiring multifactor authentication (MFA) for the administrators in your tenant is one of the first steps you can take to increase the security of your tenant. In this article, we'll cover how to ensure all of your administrators are covered by multifactor authentication.

<a name='detect-current-usage-for-azure-ad-built-in-administrator-roles'></a>

## Detect current usage for Microsoft Entra Built-in administrator roles

The [Microsoft Entra ID Secure Score](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score) provides a score for **Require MFA for administrative roles** in your tenant. This improvement action tracks the MFA usage of those with [administrator roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference). 

There are different ways to check if your admins are covered by an MFA policy. 

- To troubleshoot sign-in for a specific administrator, you can use the sign-in logs. The sign-in logs let you filter **Authentication requirement** for specific users. Any sign-in where **Authentication requirement** is **Single-factor authentication** means there was no multifactor authentication policy that was required for the sign-in.

  

  When viewing the details of a specific sign-in, select the **Authentication details** tab for details about the MFA requirements. For more information, see [Sign-in log activity details](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-in-log-activity-details).
  
  

- To choose which policy to enable based on your user licenses, we have a new MFA enablement wizard to help you [compare MFA policies](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing#compare-multi-factor-authentication-policies) and see which steps are right for your organization. The wizard shows administrators who were protected by MFA in the last 30 days.

  

- You can run [this script](https://github.com/microsoft/AzureADToolkit/blob/main/src/Find-AADToolkitUnprotectedUsersWithAdminRoles.ps1) to programmatically generate a report of all users with directory role assignments who have signed in with or without MFA in the last 30 days. This script will enumerate all active built-in and custom role assignments, all eligible built-in and custom role assignments, and groups with roles assigned.

## Enforce multifactor authentication on your administrators

If you find administrators who aren't protected by multifactor authentication, you can protect them in one of the following ways:

- If your administrators are licensed for Microsoft Entra ID P1 or P2, you can [create a Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa) to enforce MFA for administrators. You can also update this policy to require MFA from users who are in custom roles.  

- Run the [MFA enablement wizard](https://aka.ms/MFASetupGuide) to choose your MFA policy.

- If you assign custom or built-in admin roles in [Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure), require multifactor authentication upon role activation.

## Use Passwordless and phishing resistant authentication methods for your administrators

After your admins are enforced for multifactor authentication and have been using it for a while, it's time to increase authentication strength and use Passwordless and phishing resistant authentication methods: 

- [Phone Sign-in (with Microsoft Authenticator)](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-authenticator-app)
- [FIDO2](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2)
- [Windows Hello for Business](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/)

You can read more about these authentication methods and their security considerations in [Microsoft Entra authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/overview-authentication).

## Next steps

[Enable passwordless sign-in with Microsoft Authenticator](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-passwordless-phone)
