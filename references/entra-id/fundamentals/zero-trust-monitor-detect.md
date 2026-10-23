# Security guidance - Monitor and detect cyberthreats

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-monitor-detect  
> Microsoft doc last updated: 09/11/2025


Having robust health monitoring and threat detection capabilities is one of the six pillars of the [Secure Future Initiative](https://www.microsoft.com/trust-center/security/secure-future-initiative?msockid=2bad2df65a416adb0e5838355b3e6b95#SFI-pillars). These guidelines are designed to help you set up a comprehensive logging system for archival and analysis. We include recommendations related to the triage of risky sign-ins, risky users, and authentication methods.

The first step to aligning with this pillar is to configure diagnostic settings for all Microsoft Entra logs so all changes made in your tenant are stored and accessible for analysis. Other recommendations in this pillar focus on the timely triage of risk alerts and Microsoft Entra recommendations. The key takeaway is to know what logs, reports, and health monitoring tools are available and to monitor them regularly.

## Security guidance

### Diagnostic settings are configured for all Microsoft Entra logs
The activity logs and reports in Microsoft Entra can help detect unauthorized access attempts or identify when tenant configuration changes. When logs are archived or integrated with Security Information and Event Management (SIEM) tools, security teams can implement powerful monitoring and detection security controls, proactive threat hunting, and incident response processes. The logs and monitoring features can be used to assess tenant health and provide evidence for compliance and audits.

If logs aren't regularly archived or sent to a SIEM tool for querying, it's challenging to investigate sign-in issues. The absence of historical logs means that security teams might miss patterns of failed sign-in attempts, unusual activity, and other indicators of compromise. This lack of visibility can prevent the timely detection of breaches, allowing attackers to maintain undetected access for extended periods.

**Remediation action**

- [Configure Microsoft Entra diagnostic settings](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-configure-diagnostic-settings)
- [Integrate Microsoft Entra logs with Azure Monitor logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs)
- [Stream Microsoft Entra logs to an event hub](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-stream-logs-to-event-hub)

### Privileged role activations have monitoring and alerting configured
Organizations without proper activation alerts for highly privileged roles lack visibility into when users access these critical permissions. Threat actors can exploit this monitoring gap to perform privilege escalation by activating highly privileged roles without detection, then establish persistence through admin account creation or security policy modifications. The absence of real-time alerts enables attackers to conduct lateral movement, modify audit configurations, and disable security controls without triggering immediate response procedures.

**Remediation action**

- [Configure Microsoft Entra role settings in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#require-justification-on-activation)

### Activation alert for Global Administrator role assignments
Without activation alerts for Global Administrator role assignments, threat actors can escalate privileges undetected. This lack of visibility creates a blind spot where attackers can activate the most privileged role and perform malicious actions such as creating backdoor accounts, modifying security policies, or accessing sensitive data.

Monitoring these activation alerts can help security teams distinguish between authorized and unauthorized privilege escalation activities. 

**Remediation action**

- [Configure notifications for privileged roles](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#require-justification-on-active-assignment)

### Activation alert for all privileged role assignments
Without activation alerts for privileged role assignments, threat actors can escalate privileges undetected. This lack of visibility creates a blind spot where attackers can activate the most privileged role and perform malicious actions such as creating backdoor accounts, modifying security policies, or accessing sensitive data.

Monitoring these activation alerts can help security teams distinguish between authorized and unauthorized privilege escalation activities. 

**Remediation action**

- [Configure notifications for privileged roles](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#require-justification-on-active-assignment)

### Privileged users sign in with phishing-resistant methods
Without phishing-resistant authentication methods, privileged users are more vulnerable to phishing attacks. These types of attacks trick users into revealing their credentials to grant unauthorized access to attackers. If non-phishing-resistant authentication methods are used, attackers might intercept credentials and tokens, through methods like adversary-in-the-middle attacks, undermining the security of the privileged account.

Once a privileged account or session is compromised due to weak authentication methods, attackers might manipulate the account to maintain long-term access, create other backdoors, or modify user permissions. Attackers can also use the compromised privileged account to escalate their access even further, potentially gaining control over more sensitive systems.

**Remediation action**

- [Get started with a phishing-resistant passwordless authentication deployment](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication)
- [Ensure that privileged accounts register and use phishing resistant methods](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths#authentication-strengths)
- [Deploy a Conditional Access policy to target privileged accounts and require phishing resistant credentials](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa)
- [Monitor authentication method activity](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-usage-insights-report#authentication-methods-activity)

### All high-risk users are triaged
Users considered at high risk by Microsoft Entra ID Protection have a high probability of compromise by threat actors. Threat actors can gain initial access via compromised valid accounts, where their suspicious activities continue despite triggering risk indicators. This oversight can enable persistence as threat actors perform activities that normally warrant investigation, such as unusual login patterns or suspicious inbox manipulation. 

A lack of triage of these risky users allows for expanded reconnaissance activities and lateral movement, with anomalous behavior patterns continuing to generate uninvestigated alerts. Threat actors become emboldened as security teams show they aren't actively responding to risk indicators.

**Remediation action**

- [Investigate high risk users](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk) in Microsoft Entra ID Protection
- [Remediate high risk users and unblock](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock) in Microsoft Entra ID Protection

### All high-risk sign-ins are triaged
Risky sign-ins flagged by Microsoft Entra ID Protection indicate a high probability of unauthorized access attempts. Threat actors use these sign-ins to gain an initial foothold. If these sign-ins remain uninvestigated, adversaries can establish persistence by repeatedly authenticating under the guise of legitimate users. 

A lack of response lets attackers execute reconnaissance, attempt to escalate their access, and blend into normal patterns. When untriaged sign-ins continue to generate alerts and there's no intervention, security gaps widen, facilitating lateral movement and defense evasion, as adversaries recognize the absence of an active security response.

**Remediation action**

- [Investigate risky sign-ins](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk)
- [Remediate risks and unblock users](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock)

### All risky workload identities are triaged
Compromised workload identities (service principals and applications) allow threat actors to gain persistent access without user interaction or multifactor authentication. Microsoft Entra ID Protection monitors these identities for suspicious activities like leaked credentials, anomalous API traffic, and malicious applications. Unaddressed risky workload identities enable privilege escalation, lateral movement, data exfiltration, and persistent backdoors that bypass traditional security controls. Organizations must systematically investigate and remediate these risks to prevent unauthorized access. 

**Remediation action**

- [Investigate and remediate risky workload identities](https://learn.microsoft.com/en-us/entra/id-protection/concept-workload-identity-risk#investigate-risky-workload-identities)
- [Apply Conditional Access policies for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity)

### Tenant creation events are triaged
Tenant creation events should be monitored and triaged to detect unauthorized tenant creation. Users with sufficient permissions can create new tenants, which could be used to establish shadow environments outside your organization's security monitoring. Routing audit logs to a SIEM and configuring alerts for tenant creation events enables security teams to quickly investigate and respond to potentially malicious activity.

**Remediation action**

- [Review and restrict permissions to create tenants](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
- [Stream audit logs to an event hub for SIEM integration](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-stream-logs-to-event-hub)
- [Configure monitoring and alerting for audit events](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)

### All user sign-in activity uses strong authentication methods
Attackers might gain access if multifactor authentication (MFA) isn't universally enforced or if there are exceptions in place. Attackers might gain access by exploiting vulnerabilities of weaker MFA methods like SMS and phone calls through social engineering techniques. These techniques might include SIM swapping or phishing, to intercept authentication codes.

Attackers might use these accounts as entry points into the tenant. By using intercepted user sessions, attackers can disguise their activities as legitimate user actions, evade detection, and continue their attack without raising suspicion. From there, they might attempt to manipulate MFA settings to establish persistence, plan, and execute further attacks based on the privileges of compromised accounts.

**Remediation action**

- [Deploy multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted)
- [Get started with a phishing-resistant passwordless authentication deployment](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication)
- [Deploy a Conditional Access policy to require phishing-resistant MFA for all users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-mfa-strength)
- [Review authentication methods activity](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-usage-insights-report?tabs=microsoft-entra-admin-center#authentication-methods-activity)

### High priority Microsoft Entra recommendations are addressed
Leaving high-priority Microsoft Entra recommendations unaddressed can create a gap in an organization’s security posture, offering threat actors opportunities to exploit known weaknesses. Not acting on these items might result in an increased attack surface area, suboptimal operations, or poor user experience. 

**Remediation action**

- [Address all high priority recommendations in the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations#how-does-it-work)

### ID Protection notifications are enabled
If you don't enable ID Protection notifications, your organization loses critical real-time alerts when threat actors compromise user accounts or conduct reconnaissance activities. When Microsoft Entra ID Protection detects accounts at risk, it sends email alerts with **Users at risk detected** as the subject and links to the **Users flagged for risk** report. Without these notifications, security teams remain unaware of active threats, allowing threat actors to maintain persistence in compromised accounts without being detected. You can feed these risks into tools like Conditional Access to make access decisions or send them to a security information and event management (SIEM) tool for investigation and correlation. Threat actors can use this detection gap to conduct lateral movement activities, privilege escalation attempts, or data exfiltration operations while administrators remain unaware of the ongoing compromise. The delayed response enables threat actors to establish more persistence mechanisms, change user permissions, or access sensitive resources before you can fix the issue. Without proactive notification of risk detections, organizations must rely solely on manual monitoring of risk reports, which significantly increases the time it takes to detect and respond to identity-based attacks.   

**Remediation action**

- [Configure users at risk detected alerts](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-notifications#configure-users-at-risk-detected-alerts)

### No legacy authentication sign-in activity
Legacy authentication protocols such as basic authentication for SMTP and IMAP don't support modern security features like multifactor authentication (MFA), which is crucial for protecting against unauthorized access. This lack of protection makes accounts using these protocols vulnerable to password-based attacks, and provides attackers with a means to gain initial access using stolen or guessed credentials.

When an attacker successfully gains unauthorized access to credentials, they can use them to access linked services, using the weak authentication method as an entry point. Attackers who gain access through legacy authentication might make changes to Microsoft Exchange, such as configuring mail forwarding rules or changing other settings, allowing them to maintain continued access to sensitive communications.

Legacy authentication also provides attackers with a consistent method to reenter a system using compromised credentials without triggering security alerts or requiring reauthentication.

From there, attackers can use legacy protocols to access other systems that are accessible via the compromised account, facilitating lateral movement. Attackers using legacy protocols can blend in with legitimate user activities, making it difficult for security teams to distinguish between normal usage and malicious behavior.

**Remediation action**

- [Exchange protocols can be deactivated in Exchange](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/disable-basic-authentication-in-exchange-online)
- [Legacy authentication protocols can be blocked with Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication)
- [Sign-ins using legacy authentication workbook to help determine whether it's safe to turn off legacy authentication](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/workbook-legacy-authentication)

### All Microsoft Entra recommendations are addressed
Microsoft Entra recommendations give organizations opportunities to implement best practices and optimize their security posture. Not acting on these items might result in an increased attack surface area, suboptimal operations, or poor user experience.

**Remediation action**

- [Address all active or postponed recommendations in the Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations#how-does-it-work)

### Network access activity is visible to security operations for threat detection and response
Without Global Secure Access logs integrated into a Microsoft Sentinel workspace, security operations teams lack centralized visibility into network traffic patterns, connection attempts, and access anomalies across Private Access, Internet Access, and Microsoft 365 traffic forwarding. Threat actors who compromise user credentials or devices can use these network access paths to perform reconnaissance, move laterally, or exfiltrate data without detection.

Without this integration:

- Security teams can't correlate network-layer activities with identity-based signals in Microsoft Entra ID or endpoint detections.
- Security information and event management (SIEM) systems can't apply behavioral analytics, threat intelligence correlation, or automated response playbooks to Global Secure Access traffic.
- Security teams can't investigate historical network access patterns or hunt for threats across network and identity signals.

**Remediation action**

- [Configure Microsoft Entra diagnostic settings](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-sentinel-integration) to send Global Secure Access logs to a Log Analytics workspace for Microsoft Sentinel integration.
- [Enable all required Global Secure Access identity log categories](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-diagnostic-settings-logs-options), including `NetworkAccessTrafficLogs`, `EnrichedOffice365AuditLogs`, `RemoteNetworkHealthLogs`, `NetworkAccessAlerts`, `NetworkAccessConnectionEvents`, and `NetworkAccessGenerativeAIInsights` in diagnostic settings.
- [Integrate Microsoft Entra activity logs with Azure Monitor](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) for centralized log collection.
- [Configure a Microsoft Sentinel workspace](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) and install the Global Secure Access solution from the content hub.

### Network access logs are retained for security analysis and compliance requirements
Without extended retention for Global Secure Access audit and traffic logs, threat actors can operate beyond the default 30-day retention window, knowing that their activities are automatically purged before detection occurs. Security investigations often require historical analysis spanning weeks or months to identify compromise vectors, lateral movement patterns, and data exfiltration channels.

Without adequate log retention:

- Security teams can't establish baseline behavior patterns, perform retrospective threat hunting, or correlate network access events across extended timeframes.
- Organizations subject to regulatory frameworks like [GDPR](https://learn.microsoft.com/en-us/compliance/regulatory/gdpr), HIPAA, PCI DSS, and SOX face compliance violations when they're unable to produce audit trails for mandated retention periods.
- Root cause analysis during incident response is limited, potentially allowing threat actors to maintain persistence while organizations focus on visible symptoms.

**Remediation action**

- [Configure diagnostic settings with a Log Analytics workspace](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) for an extended retention of 90-730 days, with query capabilities.
- [Configure Log Analytics workspace retention](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive) to meet organizational security and compliance requirements (minimum 90 days recommended).
- [Enable table-level retention](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive#configure-table-level-retention) for specific Global Secure Access tables to extend beyond workspace defaults.

### Global Secure Access deployment logs are populated and reviewed
Global Secure Access deployment logs track the status and progress of configuration changes across the global network. These changes include forwarding profile redistributions, remote network updates, filtering profile changes, and changes to Conditional Access settings. If deployment logs show failed deployments, threat actors can exploit inconsistent security configurations where some edge locations have outdated or misconfigured policies.

If you don't monitor deployment logs:

- Failed deployments can leave security gaps such as outdated forwarding profiles that don't route traffic through security inspection, or filtering profiles that don't block malicious destinations.
- Administrators might remain unaware of outdated configurations, believing that changes are applied uniformly.
- Deployment failures that create exploitable gaps can go undetected.

**Remediation action**

- Follow the steps in [How to use the Global Secure Access deployment logs](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-deployment-logs) to:
    - Access and review deployment logs in the Microsoft Entra admin center to identify failed deployments.
    - For failed deployments, examine the error message in the `status.message` field and retry the configuration change that triggered the failure.
    - Monitor deployment notifications that appear in the admin center when making configuration changes to catch failures in real-time.
- If deployments consistently fail for remote networks, [review the underlying remote network configuration](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-remote-networks) for errors.
- For forwarding profile deployment failures, [verify traffic forwarding configuration](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding).
