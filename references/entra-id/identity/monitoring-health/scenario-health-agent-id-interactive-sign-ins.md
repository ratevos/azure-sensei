# Investigate Agent ID interactive sign-ins

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/scenario-health-agent-id-interactive-sign-ins  
> Microsoft doc last updated: 10/08/2026


Microsoft Entra Health Monitoring provides tenant-level health signals and alerts when it detects a significant change in your tenant's activity. The **Agent ID interactive sign-ins** scenario helps you investigate failures in agent sign-ins with user-delegated context.

This article explains how to interpret the scenario, correlate an alert with sign-in and audit logs, and mitigate common issues. For the shared investigation workflow, see [Investigate Microsoft Entra Health monitoring alerts](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts).

> [!IMPORTANT]
> Microsoft Entra Health scenario monitoring and alerts are currently in preview.
> This information relates to a prerelease product that might be substantially modified before release. Microsoft makes no warranties, expressed or implied, with respect to the information provided here.

## Understand what interactive means

In Health Monitoring, *interactive* describes the agent's user-delegated context. It doesn't mean that a human enters a password or completes an MFA prompt for every agent token request. An interactive agent can act on behalf of a human user with delegated permissions to access resources for that user. For that authentication flow, see [Authenticate users and acquire tokens for interactive agents](https://learn.microsoft.com/en-us/entra/agent-id/interactive-agent-authentication-authorization-flow).

To investigate this health scenario, distinguish the calling identity from the token subject. The [agent sign-in properties](https://learn.microsoft.com/en-us/graph/api/resources/agentic-agentsignin?view=graph-rest-beta&preserve-view=true) provide both dimensions:

| Property | Question it answers | How to use it |
|---|---|---|
| `agent.agentType` | Who signed in? | Identify the calling identity, such as an agent identity instance (`agenticAppInstance`). |
| `agent.agentSubjectType` | On whose behalf was the token requested? | Identify the token subject. The interactive health scenario selects `agentIDuser` subjects. |
| `agent.agentSubjectParentId` | Which parent identity is associated with the subject? | Correlate an agent's user account with its parent identity when this value is available. |
| `agent.parentAppId` | Which parent application is associated with the calling agent? | Correlate the calling agent with its blueprint when this value is available. |

> [!NOTE]
> An **Agent ID user** is an [agent's user account](https://learn.microsoft.com/en-us/entra/agent-id/agent-users), not a human user's account. It lets an agent operate with user context and delegated permissions. The Health Monitoring selection `agentSubjectType = agentIDuser` isn't a test for every agent acting on behalf of a human through the on-behalf-of (OBO) flow. Don't treat an agent's user account and a human OBO token subject as interchangeable.

**Agent ID autonomous sign-ins** is a separate health scenario for agents signing in and acting as themselves, rather than with the user-delegated context monitored here. Agent identities and designated service principals can represent these agents. For the application-permission flow, see [Authenticate and acquire tokens for autonomous agents](https://learn.microsoft.com/en-us/entra/agent-id/autonomous-agent-authentication-authorization-flow).

### Health scenarios aren't sign-in log categories

The [four sign-in log types](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins#what-are-the-types-of-sign-in-logs) describe how authentication occurs:

| Sign-in log type | Authentication activity |
|---|---|
| Interactive user sign-in | A user provides an authentication factor, such as a password or an MFA response. |
| Non-interactive user sign-in | An application or operating system component authenticates on behalf of a user without prompting them. |
| Service principal sign-in | An application identity authenticates. |
| Managed identity sign-in | A managed identity authenticates. |

Agent activity can appear across these log types. In particular, the **Agent ID interactive sign-ins** health scenario uses agent-user activity in the **User sign-ins (non-interactive)** logs. Filtering only **User sign-ins (interactive)** or `isInteractive = true` can miss the failures relevant to this scenario. For more information, see [Microsoft Entra Agent ID logs](https://learn.microsoft.com/en-us/entra/agent-id/sign-in-audit-logs-agents).

## Prerequisites

Use the least privileged role for each investigation task. Viewing an alert doesn't grant permission to change an agent's credentials, consent, or Conditional Access policies.

- A tenant with a [Microsoft Entra P1 or P2 license](https://learn.microsoft.com/en-us/entra/fundamentals/get-started-premium) is required to view health scenario signals.
- A tenant with a non-trial Microsoft Entra P1 or P2 license and at least 100 monthly active users is required to view alerts and receive alert notifications.
- [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader) is the least privileged role to view health signals, alerts, alert configurations, and sign-in logs.
- [Helpdesk Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#helpdesk-administrator) is the least privileged role to update alerts and alert notification configurations.
- For Microsoft Graph, use `HealthMonitoringAlert.Read.All` to read alerts, or `HealthMonitoringAlert.ReadWrite.All` to read and update them. These permissions don't grant access to sign-in logs.
- Use `AuditLog.Read.All` to read sign-in logs with Microsoft Graph. Reading applied Conditional Access policies requires additional permissions and a supported role. See [List signIns permissions](https://learn.microsoft.com/en-us/graph/api/signin-list?view=graph-rest-beta&preserve-view=true#permissions).

For the complete health role requirements, see [Microsoft Entra Health least privileged roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-by-task#microsoft-entra-health-least-privileged-roles).

## Investigate the signals and alert

Start with the alert's timeframe and affected entities, then use the logs to determine whether a configuration change or token acquisition problem caused the failures.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a Reports Reader.
1. Browse to **Entra ID** > **Monitoring & health** > **Health**, and select **Health Monitoring**.
1. Select **Agent ID interactive sign-ins**. If the scenario isn't listed among active alerts, select **All scenarios** to view its signals.

    

1. Review the **Agent ID interactive sign-ins completion volume** and **Agent ID interactive sign-ins failure volume** graphs. Compare the change with the agent's expected usage and recent deployments.
1. From the scenario overview, select an active **Large increase in Agent ID interactive sign-in failures** alert. Record the anomaly timeframe and review the **Signals** and **Affected entities** sections.

    

1. Under **Affected entities**, select **View** for applications and users. Use those identities to narrow your log investigation. The lists are samples of affected entities, not a list of every failed request.
1. Browse to **Entra ID** > **Agents**, and select **Sign-in logs** in the Agents blade. Select **User sign-ins (non-interactive)**, set the date range to the anomaly timeframe, and filter **Status** to **Failure**.

    

1. Correlate the affected application and user with individual events. Review the agent details described in [Microsoft Entra Agent ID logs](https://learn.microsoft.com/en-us/entra/agent-id/sign-in-audit-logs-agents). If a calling-identity filter excludes the events, inspect the `agentSubjectType` through Microsoft Graph instead of assuming there are no matching failures.
1. Open a failed event and review its error code, failure reason, application, resource, and Conditional Access result. Record the request ID, correlation ID, and timestamp if you need to escalate the issue. See [Sign-in log activity details](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-in-log-activity-details).
1. Review the [audit logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs) for changes to the agent identity, blueprint, agent's user account, delegated permission grants, and relevant policies shortly before the failures started.

An increase in failure volume isn't, by itself, proof of an outage or an attack. Compare the failure and completion trends with rollout activity, and confirm the cause in individual sign-in events before changing access.

### Correlate the alert with Microsoft Graph

Use the [health monitoring API](https://learn.microsoft.com/en-us/graph/api/resources/healthmonitoring-overview?view=graph-rest-beta&preserve-view=true) to retrieve the selected alert and its enrichment. Review the impact summary and any supporting queries supplied with the alert. Replace `{alertId}` with the selected alert's ID. The expansion retrieves a sample of affected resources, which isn't returned by default. See [Get a health monitoring alert](https://learn.microsoft.com/en-us/graph/api/healthmonitoring-alert-get?view=graph-rest-beta&preserve-view=true).

```http
GET https://graph.microsoft.com/beta/reports/healthMonitoring/alerts/{alertId}?$expand=enrichment/impacts/microsoft.graph.healthmonitoring.directoryobjectimpactsummary/resourceSampling
Prefer: include-unknown-enum-members
```

For aggregated non-interactive user activity, use [getSummarizedNonInteractiveSignIns](https://learn.microsoft.com/en-us/graph/api/auditlogroot-getsummarizednoninteractivesignins?view=graph-rest-beta&preserve-view=true). The following request uses the documented application filter to narrow the results to an affected application. Replace `{application-client-id}` with the application's `appId`, not its service principal object ID.

```http
GET https://graph.microsoft.com/beta/auditLogs/getSummarizedNonInteractiveSignIns(aggregationWindow='h1')?$filter=appId eq '{application-client-id}'
Prefer: include-unknown-enum-members
```

Include the `Prefer` header to receive `agentIDuser` from the evolvable enumeration. Follow any `@odata.nextLink` returned in the response. In the returned data, select rows where `agent.agentSubjectType` is `agentIDuser` and `status.errorCode` is nonzero. Review the `appId`, `userPrincipalName`, `agent`, and `signInCount` properties. Don't require `agent.agentType` to have one particular value when selecting the interactive scenario's subjects.

The [summarizedSignIn resource](https://learn.microsoft.com/en-us/graph/api/resources/summarizedsignin?view=graph-rest-beta&preserve-view=true) aggregates events across multiple dimensions. Use `signInCount` to understand request volume; don't count response rows as individual sign-ins or unique affected users. Aggregation and log availability can differ from the health graphs, so don't expect the totals to match exactly.

For individual events, explicitly include the non-interactive event type and replace the example UTC timestamps with your investigation interval. Without an event-type filter, the [List signIns API](https://learn.microsoft.com/en-us/graph/api/signin-list?view=graph-rest-beta&preserve-view=true) returns only interactive user sign-ins by default.

```http
GET https://graph.microsoft.com/beta/auditLogs/signIns?$filter=createdDateTime ge 2026-10-05T10:00:00Z and createdDateTime lt 2026-10-05T11:00:00Z and signInEventTypes/any(t: t eq 'nonInteractiveUser')
Prefer: include-unknown-enum-members
```

In the returned events, correlate `agent.agentSubjectType = agentIDuser` with the affected application, user, and nonzero error code. Use the individual event's failure reason and additional details to choose a mitigation.

> [!NOTE]
> These Microsoft Graph examples use `/beta`. Beta APIs are subject to change and aren't supported for production applications.

## Mitigate common issues

Use the error code from a matching sign-in event, not only the alert title. The following examples are starting points, not an exhaustive list. Error meanings are defined in the [Microsoft identity platform error reference](https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes).

### Delegated permission consent is missing

`AADSTS65001` indicates that the user or administrator hasn't consented to the application. Check the affected application, resource, and requested scopes. A permission granted to a different agent identity or for a different resource doesn't establish the intended access.

1. Confirm the delegated permissions the agent needs and whether it uses explicit grants or permissions inherited from its blueprint.
1. Ask an authorized administrator or the appropriate consenting user to grant only the required permissions, according to your tenant's consent policies.
1. Retry the token request and confirm that new matching sign-in events succeed.

For configuration guidance, see [Grant agent access to Microsoft 365](https://learn.microsoft.com/en-us/entra/agent-id/grant-agent-access-microsoft-365) and [Configure inheritable permissions for agent identity blueprints](https://learn.microsoft.com/en-us/entra/agent-id/configure-inheritable-permissions-blueprints).

### Token assertions are expired or invalid

`AADSTS500133` indicates that an assertion isn't within its valid time range. `AADSTS50013` indicates an invalid assertion and can have multiple causes, including an expired or malformed token. Don't assume that every assertion error has the same cause.

1. Review the failure reason and identify the token exchange stage that failed.
1. Ask the agent developer to check assertion validity, expiration, and audience, and acquire a fresh token through the appropriate flow instead of repeatedly submitting the same invalid assertion.
1. For human-user OBO, verify that the incoming user token targets the agent identity blueprint, not the downstream resource. See [On-behalf-of flow in agents](https://learn.microsoft.com/en-us/entra/agent-id/agent-on-behalf-of-oauth-flow).
1. For an agent's user account, verify the parent identity and token chain against the [agent's user account impersonation protocol](https://learn.microsoft.com/en-us/entra/agent-id/agent-user-oauth-flow). Don't instruct the agent's user account to sign in with a password; it doesn't support human-user credentials.

### Conditional Access blocks token issuance

`AADSTS53003` indicates that Conditional Access blocked token issuance. A block might be intentional, so don't disable a policy solely to reduce failure volume.

1. Review the failed event's **Conditional Access** details, including the target resource and policy result.
1. Compare the policy's intended scope with the affected identities. Review the audit logs for recent policy or assignment changes.
1. If the block is intended, maintain the security control. If the scope is unintended, ask the policy owner to correct only the affected assignment or configuration.

See [Troubleshoot Conditional Access sign-in problems](https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access) and [Investigate Conditional Access policy changes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-policy-changes-audit-log).

### Blueprint credentials are invalid or expired

`AADSTS7000215` indicates an invalid client secret. `AADSTS7000222` indicates expired client secret keys. A failure in the blueprint's credential chain can prevent downstream token acquisition.

1. Ask the agent developer to identify the credential and client ID used by the failing request. Verify that the request uses the expected tenant and blueprint.
1. Correct the invalid credential or rotate an expired credential using the approved deployment process. Credentials belong on the blueprint, not on the agent identity or agent's user account.
1. Validate a new token request before removing the old credential from the deployment.

For the credential model and supported authentication options, see [Agent identity blueprints](https://learn.microsoft.com/en-us/entra/agent-id/agent-blueprint) and [Microsoft agent identity platform error codes](https://learn.microsoft.com/en-us/entra/agent-id/error-codes).

## Confirm recovery

After you correct the cause, confirm that new sign-in events for the affected application and subject succeed, and that failure volume returns toward its expected pattern. Account for processing delay before comparing new logs with the health graph.

Mark the alert as **Dismissed** only after you investigate it. Dismissing an alert doesn't fix the underlying sign-in problem. For alert status and notification guidance, see [Investigate Microsoft Entra Health monitoring alerts](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts) and [Configure health alert notifications](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-configure-health-alert-notifications).

## Related content

- [Agent ID autonomous sign-ins](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/scenario-health-agent-id-autonomous-sign-ins).
- [Microsoft Entra Agent ID logs](https://learn.microsoft.com/en-us/entra/agent-id/sign-in-audit-logs-agents).
- [Agent's user accounts](https://learn.microsoft.com/en-us/entra/agent-id/agent-users).
- [Authenticate users and acquire tokens for interactive agents](https://learn.microsoft.com/en-us/entra/agent-id/interactive-agent-authentication-authorization-flow).
- [Troubleshoot common sign-in errors](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-troubleshoot-sign-in-errors).
