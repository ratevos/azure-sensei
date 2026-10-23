# How to troubleshoot sign-up errors

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-troubleshoot-sign-up-errors  
> Microsoft doc last updated: 06/30/2025


**Applies to**:  External tenants ([learn more](https://learn.microsoft.com/en-us/entra/external-id/tenant-configurations))

Microsoft Entra sign-up logs help you troubleshoot sign-up failures for users of applications in your external tenant. This article describes how to isolate sign-up failures and understand the root causes.

### Sign-up error codes

To research information about specific sign-up error codes, you can use the following tools:

- Enter the error code into the **[Error code lookup tool](https://login.microsoftonline.com/error)** to get the error code description and remediation information.

- Search for an error code in the **[authentication and authorization error codes reference](https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes)**.

The following error codes are associated with sign-up events, but this list isn't exhaustive:

- **50181**: Unable to validate the OTP.
  - This error code appears when the one-time passcode the user is trying to enter can't be validated.
  - The user should request a new one-time passcode.

- **50182**: OTP is already expired.
  - This error code appears when the one-time passcode the user is trying to enter is expired.
  - The user should request a new one-time passcode.

- **1002027**: Some of the collected attributes were invalid.
  - One or more attributes entered by the user during sign-up weren't in a valid format.
  - The user should reenter the attributes.

- **399279**: User creation failed during self-service sign-up.
  - The user's account couldn't be created.
  - The user should retry the sign-up process.

The following codes are not actual errors. They indicate expected interruptions that occur due to the interactive nature of the sign-up process.

- **1002013**: User is prompted to enter Email One-Time-Passcode to verify ownership of email address.
  - This is an expected part of the signup flow, where a user is prompted to enter the one-time-passcode emailed to them to verify ownership of email address.

- **50140**: User is prompted with option to 'Keep me signed in' during the sign-in following sign-up.
  - This is an expected part of the sign-in flow, where a user is asked if they want to remain signed into this browser to make further sign-ins easier.

If an issue persists despite taking the recommended course of action, open a support request. For more information, see [how to get support for Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-get-support).

## Next steps

- [Sign-ins error codes reference](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins)
- [Sign-ins report overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins)
- [How to use the Sign-in diagnostics](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-sign-in-diagnostics)
