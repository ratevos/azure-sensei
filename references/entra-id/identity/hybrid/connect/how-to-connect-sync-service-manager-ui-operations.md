# Microsoft Entra Connect Synchronization Service Manager Operations

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-service-manager-ui-operations  
> Microsoft doc last updated: 04/09/2025


The operations tab shows the results from the most recent operations. This tab is key to understand and troubleshoot issues.

## Understand the information visible in the operations tab
The top half shows all runs in chronological order. By default, the operations log keeps information about the last seven days, but this setting can be changed with the [scheduler](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-scheduler). You want to look for any run that doesn't show a success status. You can change the sorting by selecting the headers.

The **Status** column is the most important information and shows the most severe problem for a run. Here is a quick summary of the most common statuses in order of priority to investigate (where * indicate several possible error strings).

| Status | Comment |
| --- | --- |
| stopped-\* |The run couldn't complete. For example, if the remote system is down and can't be contacted. |
| stopped-error-limit |There are more than 5,000 errors. The run was automatically stopped due to the large number of errors. |
| completed-\*-errors |The run completed, but there are errors (fewer than 5,000) that should be investigated. |
| completed-\*-warnings |The run completed, but some data isn't in the expected state. If you have errors, then this message is only a symptom. Until you address the errors, you shouldn't investigate warnings. |
| success |No issues. |

When you select a row, the bottom updates to show the details of that run. To the far left of the bottom, you might have a list saying **Step #**. This list only appears if you have multiple domains in your forest where each domain is represented by a step. The domain name can be found under the heading **Partition**. Under **Synchronization Statistics**, you can find more information about the number of changes that were processed. You can select the links to get a list of the changed objects. If you have objects with errors, the errors show up under **Synchronization Errors**.

For more information, see [troubleshoot an object that isn't synchronizing](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-object-not-syncing)

## Next steps
Learn more about the [Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis) configuration.

Learn more about [Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).
