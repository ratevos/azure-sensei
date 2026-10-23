# Build Conditional Access policies in Microsoft Entra

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policies  
> Microsoft doc last updated: 03/24/2026


## Overview

As explained in the article [What is Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview), a Conditional Access policy is an if-then statement of **Assignments** and **Access controls**. A Conditional Access policy combines signals to make decisions and enforce organizational policies.

How does an organization create these policies? What is required? How are they applied?

Multiple Conditional Access policies can apply to an individual user at any time. In this case, all applicable policies must be satisfied. For example, if one policy requires multifactor authentication and another requires a compliant device, you must complete MFA, and use a compliant device. All assignments are logically combined using **AND**. If you have more than one assignment configured, all assignments must be satisfied to trigger a policy.

If a policy with "Require one of the selected controls" is selected, prompts appear in the defined order. Once the policy requirements are satisfied, access is granted.

All policies are enforced in two phases:

- **Phase 1**: Collect session details 
   - Gather session details, like network location and device identity necessary for policy evaluation. 
   - Phase 1 of policy evaluation occurs for enabled policies and policies in [report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only).
- **Phase 2**: Enforcement 
   - Use the session details gathered in phase 1 to identify any requirements that aren't met. 
   - If there's a policy that is configured with the **block** grant control, enforcement stops here and the user is blocked. 
   - The user is prompted to complete more grant control requirements that weren't satisfied during phase 1 in the following order, until policy is satisfied:  
      1. [Multifactor authentication​](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-multifactor-authentication)
      1. [Device to be marked as compliant](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-device-to-be-marked-as-compliant)
      1. [Microsoft Entra hybrid joined device](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-hybrid-azure-ad-joined-device)
      1. [Approved client app](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-approved-client-app)
      1. [App protection policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-app-protection-policy)
      1. [Password change](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-password-change)
      1. [Terms of use](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#terms-of-use)
      1. [Custom controls](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#custom-controls-preview)
   - Once all grant controls are satisfied, session controls are applied (App Enforced, Microsoft Defender for Cloud Apps, and token lifetime). 
   - Phase 2 of policy evaluation occurs for all enabled policies. 

## Assignments

The assignments section defines who, what, and where for the Conditional Access policy.

### Users and groups

[Users and groups](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-users-groups) assign who the policy include or exclude when applied. This assignment can include all users, specific groups of users, directory roles, or external guest users. Organizations with Microsoft Entra Workload ID licenses might target [workload identities](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview) as well.

Policies targeting roles or groups are evaluated only when a token is issued. This means:

- Newly added users to a role or group aren't subject to the policy until they get a new token.
- If a user already has a valid token before being added to the role or group, the policy doesn't apply retroactively.

The best practice is to trigger Conditional Access evaluation during role activation or group membership activation using [Microsoft Entra Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#on-activation-require-multifactor-authentication).

<a name='cloud-apps-or-actions'></a>

### Target resources

[Target resources](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps) can include or exclude cloud applications, user actions, or authentication contexts that are subjected to the policy.

<a name='locations'></a>

### Network

[Network](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-assignment-network) contains IP addresses, geographies, and [Global Secure Access' compliant network](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-compliant-network) to Conditional Access policy decisions. Admins can define locations and mark some as trusted, such as their organization's primary network locations.

### Conditions

A policy can contain multiple [conditions](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions).

#### Sign-in risk

For organizations with [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection), the risk detections generated there can influence your Conditional Access policies.

#### Device platforms

Organizations with multiple device operating system platforms might enforce specific policies on different platforms. 

The information used to determine the device platform comes from unverified sources, like user agent strings that can be changed.

#### Client apps

The software the user is employing to access the cloud app. For example, 'Browser' and 'Mobile apps and desktop clients'. By default, all newly created Conditional Access policies apply to all client app types even if the client apps condition isn't configured.

#### Filter for devices

This control allows targeting specific devices based on their attributes in a policy.

## Access controls

The access controls portion of the Conditional Access policy controls how a policy is enforced.

### Grant

[Grant](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant) provides administrators with a means of policy enforcement where they can block or grant access.

#### Block access

Block access blocks access under the specified assignments. This control is powerful and requires appropriate knowledge to use effectively.

#### Grant access

The grant control triggers enforcement of one or more controls. 

- Require multifactor authentication
- Require authentication strength
- Require device to be marked as compliant (Intune)
- Require Microsoft Entra hybrid joined device
- Require approved client app
- Require app protection policy
- Require password change
- Require terms of use

Administrators choose to require one of the previous controls or all selected controls using the following options. By default, multiple controls require all.

- Require all the selected controls (control and control)
- Require one of the selected controls (control or control)

### Session

[Session controls](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-session) can limit the experience of users.

- Use app enforced restrictions:
   - Works only with Exchange Online and SharePoint Online.
   - Passes device information to control the experience, granting full or limited access.
- Use Conditional Access App Control:
   - Uses signals from Microsoft Defender for Cloud Apps to do things like: 
      - Block download, cut, copy, and print of sensitive documents.
      - Monitor risky session behavior.
      - Require labeling of sensitive files.
- Sign-in frequency:
   - Ability to change the default sign-in frequency for modern authentication.
- Persistent browser session:
   - Allows users to remain signed in after closing and reopening their browser window.
- Customize continuous access evaluation.
- Disable resilience defaults. 

## Simple policies

A Conditional Access policy must include at least the following to be enforced:

- **Name** of the policy
- **Assignments**
   - **Users and/or groups** to apply the policy to
   - **Target resources** to apply the policy to
- **Access controls**
   - **Grant** or **Block** controls

The article [Common Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common) includes policies that might be useful to most organizations.

## Related content

- [Common Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)

- [Managing device compliance with Intune](https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started)

- [Microsoft Defender for Cloud Apps and Conditional Access](https://learn.microsoft.com/en-us/defender-cloud-apps/proxy-intro-aad)
