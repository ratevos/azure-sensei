# Reacting to Azure Policy state change events

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/event-overview  
> Microsoft doc last updated: 03/04/2025


Azure Policy events enable applications to react to state changes. This integration is done without the need for complicated code or expensive and inefficient polling services. Instead, events are pushed through [Azure Event Grid](../../../event-grid/index.yml) to subscribers such as [Azure Functions](../../../azure-functions/index.yml), [Azure Logic Apps](../../../logic-apps/index.yml), or even to your own custom HTTP listener. Critically, you only pay for what you use.

Azure Policy events are sent to the Azure Event Grid, which provides reliable delivery services to your applications through rich retry policies and dead-letter delivery. Event Grid takes care of the proper routing, filtering, and multicasting of the events to destinations via Event Grid subscriptions. To learn more, see [Event Grid message delivery and retry](https://learn.microsoft.com/en-us/azure/event-grid/delivery-and-retry).

> [!NOTE]
> Azure Policy state change events are sent to Event Grid after an
> [evaluation trigger](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data#evaluation-triggers) finishes resource
> evaluation.
> 
> Event Grid notifications for resource compliance state changes can take up to 20 minutes.

## Event Grid Benefits
Event Grid has a few benefits for customers and services in the Azure ecosystem:
- Automation: To stay current with your policy environment, Event Grid offers an automated mechanism to generate alerts and trigger tasks depending on compliance states.
- Durable delivery: In order for services and user applications to respond in real-time to policy compliance events, Event Grid seeks to offer policy events with minimum latency. Event Grid retries transmission of an event if a subscriber's endpoint fails to acknowledge receipt of it or if it doesn't, according to a predetermined retry schedule and retry policy.
- Custom event producer: Event Grid  event producers and consumers don't need to be Azure or Microsoft services. External applications can receive an alert, show the creation of a remediation task or collect messages on who responds to the state change. See [Route policy state change events to Event Grid with Azure CLI](https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/route-state-change-events) for a full tutorial.

There are two primary entities when using Event Grid:
- Events: These events can be anything a user might want to react to for an Azure resource. For example, if a policy compliance state is created, changed, and deleted for a resource such as a virtual machine or storage accounts.
- Event Grid Subscriptions: These event subscriptions are user configured entities that direct the proper set of events from a publisher to a subscriber. Event subscriptions can filter events based on the resource path the event originated from and the type of event. Additionally, Event Subscriptions can also filter by scope between Azure subscription and Management group.

A common Azure Policy event scenario is tracking when the compliance state of a resource changes during policy evaluation. Event-based architecture is an efficient way to react to these changes and aids in the event based reaction to compliance state changes.

Another scenario is to automatically trigger remediation tasks without manually selecting _create remediation task_ on the policy page. Event Grid checks for compliance state and resources that are currently noncompliant can be remedied. Learn more about [remediation structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/remediation-structure). Remediation requires a managed identity and policies must be in `modify` or `deployIfNotExists` effect. [Learn more about effect types](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources).

Event Grid is helpful as an audit system to store state changes and understand cause of noncompliance over time. The scenarios for Event Grid are endless and based on the motivation, Event Grid is configurable.

## Practices for consuming events

Applications that handle Azure Policy events should follow these recommended practices:

> - Multiple subscriptions can be configured to route events to the same event handler, so don't
> assume events are from a particular source. Instead, check the topic of the message to ensure the
> policy assignment, policy definition, and resource the state change event is for.
> - Check the `eventType` and don't assume that all events you receive are the types you expect.
> - Use `data.timestamp` to determine the order of the events in Azure Policy, instead of the
> top-level `eventTime` or `time` properties.
> - Use the subject field to access the resource that had a policy state change.

## Next steps

Learn more about Event Grid and give Azure Policy state change events a try:

- [Route policy state change events to Event Grid with Azure CLI](https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/route-state-change-events)
- [Azure Policy schema details for Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-policy)
- [About Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview)
