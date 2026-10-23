# Admin account security in Microsoft 365 for business

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-account-security-admins  
> Microsoft doc last updated: 01/06/2026


Although multifactor authentication (MFA) is [turned on by default for all accounts in Microsoft 365 for business organizations](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/multi-factor-authentication-microsoft-365#security-defaults), administrator or admin accounts require extra security considerations unrelated to MFA. Admin accounts have elevated privileges and are valuable targets for attackers. At the same time, admin accounts are fundamental to the operation and management of your organization.

The account you used to enroll in Microsoft 365 for business is automatically a Global Administrator (also known as a _global admin_). Global admins have ultimate control over user accounts and all the other settings in the Microsoft admin center (<https://admin.microsoft.com>). But there are many different kinds of admin capabilities with varying levels of access. For more information, see [About admin roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

Use the following guidance to make the most of admin accounts while protecting your organization from attackers:

- **Be sure to have more than one admin account**: We recommend at least two admin [emergency access accounts](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) in every organization that aren't assigned to specific individuals and are only used in emergencies. These accounts also need to be [excluded from MFA requirements](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication#step-3-adjust-mfa-exclusions) and therefore should have long, complex passwords (16 or more characters). These accounts are also known as "break glass accounts."

  For admin account creation instructions, see [Add an administrator](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/assign-admin-roles#add-an-administrator).

  > [!IMPORTANT]
  > Limit the number of admin accounts your organization. Too many admin accounts provide attackers with more opportunities to compromise your organization.
  >
  > Use the concept _least privilege_, which means you give users only the permissions required to do their jobs. For example, if a user needs to create user accounts, don't add them to the Global Administrator role; add them to the User Administrator role instead. For more information, see the following articles:
  >
  > - [Enhance security with the principle of least privilege](https://learn.microsoft.com/en-us/entra/identity-platform/secure-least-privileged-access)
  > - [About admin roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles)

- **Use ordinary user accounts for regular work tasks**: Admins should use non-admin accounts as primary accounts to sign in to their computers and do regular tasks like checking email and using Microsoft 365 Apps. Use your admin account only as needed.
  - Before using admin accounts, close all unrelated browser sessions and apps, including personal email accounts. You can also use InPrivate, Incognito, or Private browsing mode for admin tasks.
  - After completing admin tasks, be sure to sign out of the browser session.

  For account creation instructions, see [Add users and assign licenses at the same time](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users).

  > [!TIP]
  > Ordinary user accounts need Microsoft 365 for business licenses, but you don't need to license admin only accounts.
  >
  > Use a naming convention that doesn't advertise the fact that an account has admin privileges. For example, your regular user account is `alice.chavez@contoso.onmicrosoft.com`, and your admin account is `alicec@contoso.onmicrosoft.com`.

- **Use passwordless authentication for admin accounts**: For more information, see [Enable passwordless sign-in with Authenticator](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-passwordless-phone).
  - Microsoft 365 Business Basic and Microsoft 365 Business Standard organizations support the following passwordless authentication options via Microsoft Entra ID Free:
    - The [Microsoft Authenticator](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passwordless#microsoft-authenticator) app with push notifications and biometric or PIN verification.
    - [Passkeys (FIDO2)](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passwordless#passkeys-fido2)
    - [Windows Hello for Business](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passwordless#windows-hello-for-business)
  - Microsoft 365 Business Premium via Microsoft Entra ID P1 also allows you to _require_ passwordless authentication and authentication strength for admin accounts using Conditional Access. For more information, see [Conditional Access authentication strength](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths).
