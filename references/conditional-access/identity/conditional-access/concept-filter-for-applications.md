# Filter for applications in Conditional Access policy

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-filter-for-applications  
> Microsoft doc last updated: 03/24/2026


## Overview

Currently Conditional Access policies can be applied to all apps or to individual apps. Organizations with a large number of apps might find this process difficult to manage across multiple Conditional Access policies.

Application filters for Conditional Access allow organizations to tag service principals with custom attributes. These custom attributes are then added to their Conditional Access policies. Filters for applications are evaluated at token issuance runtime, not configuration.

In this document, you create a custom attribute set, assign a custom security attribute to your application, and create a Conditional Access policy to secure the application.

## Assign roles

Custom security attributes are security sensitive and can only be managed by delegated users. One or more of the following roles should be assigned to the users who manage or report on these attributes.

| Role name | Description |
| --- | --- |
| [Attribute Assignment Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-administrator) | Assign custom security attribute keys and values to supported Microsoft Entra objects. |
| [Attribute Assignment Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-reader) | Read custom security attribute keys and values for supported Microsoft Entra objects. |
| [Attribute Definition Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-definition-administrator) | Define and manage the definition of custom security attributes. |
| [Attribute Definition Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-definition-reader) | Read the definition of custom security attributes. |

Assign the appropriate role to the users who manage or report on these attributes at the directory scope. For detailed steps, see [Assign Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal#assign-roles-with-tenant-scope).

> [!IMPORTANT]
> By default, [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) and other administrator roles do not have permissions to read, define, or assign custom security attributes.

## Create custom security attributes

Follow the instructions in the article, [Add or deactivate custom security attributes in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-add) to add the following **Attribute set** and **New attributes**.

- Create an **Attribute set** named *ConditionalAccessTest*.
- Create **New attributes** named *policyRequirement* that **Allow multiple values to be assigned** and **Only allow predefined values to be assigned**. Add the following predefined values:
   - legacyAuthAllowed
   - blockGuestUsers
   - requireMFA
   - requireCompliantDevice
   - requireHybridJoinedDevice
   - requireCompliantApp

> [!NOTE]
> Conditional Access filters for applications only work with custom security attributes of type `string`. Custom Security Attributes support creation of Boolean data type but Conditional Access Policy only supports `string`.

## Create a Conditional Access policy

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) and [Attribute Definition Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-definition-reader).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts.
   1. Select **Done**.
1. Under **Target resources**, select the following options:
   1. Select what this policy applies to **Resources (formerly cloud apps)**.
   1. Include **Select resources**.
   1. Select **Edit filter**.
   1. Set **Configure** to **Yes**.
   1. Select the **Attribute** created earlier called *policyRequirement*.
   1. Set **Operator** to **Contains**.
   1. Set **Value** to **requireMFA**.
   1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Grant access**, **Require multifactor authentication**, and select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Configure custom attributes

### Step 1: Set up a sample application

If you already have a test application that makes use of a service principal, you can skip this step.

Set up a sample application that, demonstrates how a job or a Windows service can run with an application identity, instead of a user's identity. Follow the instructions in the article [Quickstart: Get a token and call the Microsoft Graph API by using a console app's identity](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-daemon-app-call-api) to create this application.

### Step 2: Assign a custom security attribute to an application

When you don't have a service principal listed in your tenant, it can't be targeted. The Office 365 suite is an example of one such service principal.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) and [Attribute Assignment Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-administrator).
1. Browse to **Entra ID** > **Enterprise apps**.
1. Select the service principal you want to apply a custom security attribute to.
1. Under **Manage** > **Custom security attributes**, select **Add assignment**.
1. Under **Attribute set**, select **ConditionalAccessTest**.
1. Under **Attribute name**, select **policyRequirement**.
1. Under **Assigned values**, select **Add values**, select **requireMFA** from the list, then select **Done**.
1. Select **Save**.

### Step 3: Test the policy

Sign in as a user who the policy would apply to and test to see that MFA is required when accessing the application.

## Other scenarios

- Blocking legacy authentication
- Blocking external access to applications
- Requiring compliant device or Intune app protection policies
- Enforcing sign in frequency controls for specific applications
- Requiring a privileged access workstation for specific applications
- Require session controls for high risk users and specific applications

## Related content

[Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)

[Determine effect using Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)

[Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
