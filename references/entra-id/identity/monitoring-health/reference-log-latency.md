# Log latency for Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-log-latency  
> Microsoft doc last updated: 09/27/2024


Latency is the amount of time it takes for Microsoft Entra ID reporting data to appear in the Monitoring and health logs. This article describes the factors that can affect latency.

## Latency and first-time setup

When you upgrade from a free version of Microsoft Entra Premium P1 or P2, you should expect a delay of roughly 24 hours from when you upgrade your tenant before all premium reporting features show data. Many premium reporting features only begin retaining data after this 24-hour period following your upgrade.

When setting up a new storage account or security information and event management (SIEM) tool, you should also expect a delay of 24 hours before reporting data appears in those tools.

When routing activity logs to a Log Analytics workspace for analysis with Azure Monitor logs, you should expect a delay of up to three days before the logs appear in the workspace.

## Reporting latency factors

Many factors influence the latency of reporting data. The type of data, the amount of data, and the infrastructure that the reporting tools are built on can all influence latency. If there's a delay in the underlying infrastructure, Microsoft Entra reports might experience a delay in reporting data.

One key factor in log latency is the path that the data travels from the source event to the logs in the Microsoft Entra admin center. Log data travels through the following systems before it appears in the logs.

1. Customer signs in to a service that uses Microsoft Entra ID as the identity and access service.
1. Log processors read the event metadata and publish it to the Azure storage queue.
1. Event metadata is processed and reviewed for success or failure.
1. Successful events are published to partner services, such as Azure Monitor and Microsoft Graph.
1. IT admin views the data in the Microsoft Entra admin center, or their SIEM tool of choice.

There are many more steps in this process that aren't reflected here. Even with these summarized steps, it's easy to see how latency can be introduced into the system.

## Last sign-in

The last sign-in of a user is one of the most common questions related to log latency. This information is provided by the `signInActivity` property in Microsoft Graph. The signInActivity property provides the last interactive and non-interactive sign-in *attempt* for a user. This property might take up to 24 hours to update. For more information, see [signInActivity resource type](https://learn.microsoft.com/en-us/graph/api/resources/signinactivity?view=graph-rest-beta&preserve-view=true).

You must be using a [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs#prerequisites) that grants access to the sign-in logs to see this detail, which is found in several places:

- The **Sign-ins** tile in the **My Feed** section of the user's profile.

  

- The **Last interactive sign-in** and **Last non-interactive sign-in** columns in the **Users** list.

  

- The sign-in logs filtered for a particular user.

    

The last sign-in details that appear on the **Sign-ins** tile on the user profile and the **Last interactive sign-in** and **Last non-interactive sign-in** columns in the **Users** list are *not* real-time.

If you need to see the most recent sign-in date and time for a user, go to the sign-in logs and filter for that user.
