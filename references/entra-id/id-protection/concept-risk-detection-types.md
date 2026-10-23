# Risk detection types and levels

> Source: https://learn.microsoft.com/en-us/entra/id-protection/concept-risk-detection-types  
> Microsoft doc last updated: 06/10/2026


Microsoft Entra ID Protection provides organizations with information about suspicious activity in their tenant and allows you to respond quickly to prevent further risk occurring. Risk detections are a powerful resource that can include any suspicious or anomalous activity related to user accounts and service principals in the directory. ID Protection risk detections can be linked to an individual user or sign-in event and contribute to the overall user risk score found in the [Risky users report](https://learn.microsoft.com/en-us/entra/id-protection/concept-risk-reports). 

User risk detections might flag a legitimate user account as at risk, when a potential threat actor gains access to an account by compromising their credentials or when anomalous user activity is detected. Sign-in risk detections represent the probability that a given authentication request isn't the authorized owner of the account. Having the ability to identify risk at the user and sign-in level is critical for customers to be empowered to secure their tenant.

> [!NOTE]
> For the full list of risk detections, how they're calculated, and their license requirements, see [**Risk detection and event types**](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks).

## Risk levels

ID Protection categorizes risk into three tiers: low, medium, and high. Risk levels are calculated by our machine learning algorithms and represent how confident Microsoft is that one or more of the user's credentials are known by an unauthorized entity.

Detections can fire at more than one risk level, depending on the confidence level. For example, [Unfamiliar sign-in properties](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#unfamiliar-sign-in-properties) might fire at high, medium, or low based on the level of familiarity with the sign-in properties. Other detections, like [Leaked Credentials](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#leaked-credentials) and [Verified Threat Actor IP](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks#verified-threat-actor-ip) are always delivered as high risk because we found proof of the leaked credential or the threat actor.

Risk level is important when deciding which detections to [prioritize, investigate, and remediate](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk#investigation-and-risk-remediation-framework). The risk level helps you prioritize your investigation and remediation efforts.

Risk levels also play a key role in [configuring risk-based Conditional Access policies](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#choosing-acceptable-risk-levels), as each policy can be set to trigger for low, medium, high, or no risk detected. Based on the risk tolerance of your organization, you can create Conditional Access policies that require MFA or password reset when ID Protection detects a certain risk level for one of your users. These policies can guide the user to self-remediate to resolve the risk.

> [!IMPORTANT] 
> **Low** level risk detections and users persist in the product for six months, after which they're automatically aged out to provide a cleaner investigation experience. **Medium** and **high** risk levels persist until remediated or dismissed.

A risk detection with risk level of:

- **High** signifies that Microsoft is highly confident that the account is compromised. Signals such as threat intelligence and known attack patterns factor into the confidence level of the risk detection.
- **Medium** indicates that one or more moderate-severity anomalies were detected, but there's less confidence that the account is compromised. Sign-in patterns, behaviors, and other signals factor into the confidence level of the risk detection.
- **Low** signifies that anomalies are present in the sign-in or a user's credential, but we're less confident the account hasn't been compromised. Sign-in patterns before and during the sign-in are used to determine if there's a pattern or if the sign-in is an anomaly.

## Real-time and offline detections

ID Protection utilizes techniques to increase the precision of user and sign-in risk detections by calculating some risks in real-time or offline after authentication. Detecting risk in real-time at sign-in gives the advantage of identifying risk early so that users can self-remediate during sign-in and admins can quickly investigate the potential compromise. Conditional Access policies triggered during sign-in can stop a bad actor before they gain access to the account.

Detections calculated offline can provide more insight into how the threat actor gained access to the account and the effect on the legitimate user. Some detections can be triggered both offline and during sign-in, which increases confidence in compromise detection.

Detections triggered in real-time take 5-10 minutes to surface details in the reports. Offline detections take up to 48 hours to surface in the reports, as it takes time to evaluate properties of the potential risk. It's important to remember that risk levels can change, because some risk detections are calculated offline after sign-in.

| Detection type | Sign-in risk | User risk |
|----------------|--------------|-----------|
| **Real-time**      | Suspicious sign-in is detected and can be remediated in real-time through a Conditional Access policy, such as to require MFA. | User risk is detected and can be remediated through a Conditional Access policy, such as to force a secure password change in real-time. |
| **Offline**        | Sign-in risk is identified after sign-in. If not remediated this risk might escalate into user risk if more risks are detected and aggregated into user risk. | User is deemed risky after sign-in. If Conditional Access policy is configured, the user is blocked until they perform self-service password reset the next time they authenticate. |

> [!NOTE]
> Our system might determine that the risk event that contributed to the user risk score was either: 
> 
> - A false positive, or
> - The user risk was [remediated by policy](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock) (by either completing multifactor authentication or a secure password change).
> 
> Our system dismisses the risk state and sets the risk detail to **AI confirmed sign-in safe**, so the risk state no longer contributes to the user's overall risk.

### Time detection

On risk-detailed data, **Time Detection** records the exact moment a risk is identified during a user's sign-in, which allows for real-time risk assessment and immediate policy application to safeguard the user and organization. **Detection last updated** shows the latest update to a risk detection, which could be due to new information, risk level changes, or administrative actions, and ensures up-to-date risk management.

These fields are essential for real-time monitoring, threat response, and maintaining secure access to organizational resources.

### Locations 

Location in risk detections is determined using IP address lookup. Sign-ins from trusted [named locations](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-assignment-network#trusted-locations) improve the accuracy of Microsoft Entra ID Protection's risk calculation, lowering a user's sign-in risk when they authenticate from a location marked as trusted.

> [!NOTE]
> Looking for the **Risk detections mapped to riskEventType** table? It moved to the new [**Risk detection and event types**](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) article.

## Agent detections

The **Risk detections** report includes a dedicated tab for **Agent detections** that displays risk detections specifically for autonomous AI agents using [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/identity-professional/what-is-microsoft-entra-agent-id). These detections help identify suspicious activities associated with agents, allowing administrators to monitor and respond to potential threats effectively. For a list of the risk detections associated with agents, see [ID Protection for agents](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents#activities-contributing-to-risk).

In agent on-behalf-of flows, where an agent acts using a user's delegated permissions, risky activity is attributed to the **user** rather than the agent. This approach targets remediation at the compromised user session without disrupting the agent for other users. Risk detections in this table apply specifically to autonomous agent activity.

## Related content

- [Learn about risk-based access policies](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies)
- [Learn how to investigate risk](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk)
- [Review all risk event types](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)
