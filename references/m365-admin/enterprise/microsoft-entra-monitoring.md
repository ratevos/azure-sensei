# Microsoft Entra monitoring

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-entra-monitoring  
> Microsoft doc last updated: 05/05/2025


Microsoft Entra monitoring supports the following organizational scenarios with near real-time information:

- **Sign-ins requiring Cloud Multifactor Authentication (Completion Volume)**. Amount of users successfully completing interactive MFA sign ins using Microsoft Entra ID MFA cloud service (not counting MFA server activity). Users abandoning or canceling MFA requests, refreshing MFA sessions without doing interactive MFA, or using passwordless methods do not count in this chart at this time.

- **Sign-ins requiring a Conditional Access Compliant Device**. Amount of devices over time in your organization that successfully satisfy a conditional access policy that requires devices compliance. Compliant devices are managed by Microsoft Intune and can be mobile iOS/Android devices, tablets or cloud Microsoft Entra ID joined computers (not hybrid).

- **Sign-ins requiring a Conditional Access Managed Device**. Amount of devices over time in your organization that successfully satisfy a conditional access policy that requires devices are managed. Managed devices are computers joined to and managed by your on-premises directory and hybrid joined to Microsoft Entra ID.

- **Sign-ins to applications using SAML**. This signal helps you find potential health issues with user authentications that rely on Security Assertion Markup Language (SAML) single sign-on (SSO). It includes SAML 2.0 authentication successfully processed by the Microsoft Entra cloud service for your tenant. It does not include WS-FED/SAML 1.1 apps integrated with Microsoft Entra ID. The data in the graph is aggregated every 60 minutes.

Admins can use the information to correlate any Microsoft-reported issues with the usage data to confirm any actual impact to their organization. Also, admins can view any usage from the last two weeks of usage data to identify any anomalies.

**More information**

[How to investigate sign-ins requiring Microsoft Entra multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/scenario-health-sign-ins-mfa).

[How to investigate the sign-ins requiring a Compliant or Managed Device alert](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/scenario-health-sign-ins-compliant-managed-device).
