# Security guidance | accelerate response and remediation

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-response-remediation  
> Microsoft doc last updated: 09/12/2025


The ability to rapidly detect, respond to, and remediate security threats is critical in today's evolving threat landscape. As one of the pillars of the [Secure Future Initiative](https://www.microsoft.com/trust-center/security/secure-future-initiative?msockid=2bad2df65a416adb0e5838355b3e6b95#SFI-pillars), accelerating response and remediation encourages organizations to minimize the time between threat detection and containment.

This pillar emphasizes automated, risk-based responses that reduce manual intervention and help prevent security incidents from escalating. The following Microsoft Entra Zero Trust assessment checks ensure your organization has the necessary controls in place to quickly identify and mitigate high-risk scenarios, protecting both user identities and workload identities through proactive security policies.

## Zero Trust security recommendations

### Workload Identities are configured with risk-based policies
Set up risk-based Conditional Access policies for workload identities based on risk policy in Microsoft Entra ID to make sure only trusted and verified workloads use sensitive resources. Without these policies, threat actors can compromise workload identities with minimal detection and perform further attacks. Without conditional controls to detect anomalous activity and other risks, there's no check against malicious operations like token forgery, access to sensitive resources, and disruption of workloads. The lack of automated containment mechanisms increases dwell time and affects the confidentiality, integrity, and availability of critical services.   

**Remediation action**
Create a risk-based Conditional Access policy for workload identities.
- [Create a risk-based Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity#create-a-risk-based-conditional-access-policy)

### Restrict high risk sign-ins
When high-risk sign-ins are not properly restricted through Conditional Access policies, organizations expose themselves to security vulnerabilities. Threat actors can exploit these gaps for initial access through compromised credentials, credential stuffing attacks, or anomalous sign-in patterns that Microsoft Entra ID Protection identifies as risky behaviors. Without appropriate restrictions, threat actors who successfully authenticate during high-risk scenarios can perform privilege escalation by misusing the authenticated session to access sensitive resources, modify security configurations, or conduct reconnaissance activities within the environment. Once threat actors establish access through uncontrolled high-risk sign-ins, they can achieve persistence by creating additional accounts, installing backdoors, or modifying authentication policies to maintain long-term access to the organization's resources. The unrestricted access enables threat actors to conduct lateral movement across systems and applications using the authenticated session, potentially accessing sensitive data stores, administrative interfaces, or critical business applications. Finally, threat actors achieve impact through data exfiltration, or compromise business-critical systems while maintaining plausible deniability by exploiting the fact that their risky authentication was not properly challenged or blocked.

**Remediation action**

- [Deploy a Conditional Access policy to require MFA for elevated sign-in risk](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-sign-in)

### Restrict access to high risk users
Assume high risk users are compromised by threat actors. Without investigation and remediation, threat actors can execute scripts, deploy malicious applications, or manipulate API calls to establish persistence, based on the potentially compromised user's permissions. Threat actors can then exploit misconfigurations or abuse OAuth tokens to move laterally across workloads like documents, SaaS applications, or Azure resources. Threat actors can gain access to sensitive files, customer records, or proprietary code and exfiltrate it to external repositories while maintaining stealth through legitimate cloud services. Finally, threat actors might disrupt operations by modifying configurations, encrypting data for ransom, or using the stolen information for further attacks, resulting in financial, reputational, and regulatory consequences.

Organizations using passwords can rely on password reset to automatically remediate risky users.

Organizations using passwordless credentials already mitigate most risk events that accrue to user risk levels, thus the volume of risky users should be considerably lower. Risky users in an organization that uses passwordless credentials must be blocked from access until the user risk is investigated and remediated.

**Remediation action**

- [Deploy a Conditional Access policy to require a secure password change for elevated user risk](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user).
- Use Microsoft Entra ID Protection to [investigate risk further](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk).
