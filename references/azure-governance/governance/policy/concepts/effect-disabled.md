# Azure Policy definitions disabled effect

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-disabled  
> Microsoft doc last updated: 03/04/2025


The `disabled` effect is useful for testing situations or for when the policy definition has parameterized the effect. This flexibility makes it possible to disable a single assignment instead of disabling all of that policy's assignments.

> [!NOTE]
> Policy definitions that use the `disabled` effect have the default compliance state **Compliant** after assignment.

An alternative to the `disabled` effect is `enforcementMode`, which is set on the policy assignment. When `enforcementMode` is `disabled`, resources are still evaluated. Logging, such as Activity logs, and the policy effect don't occur. For more information, see [policy assignment - enforcement mode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure#enforcement-mode).

## Next steps

- Review examples at [Azure Policy samples](https://learn.microsoft.com/en-us/azure/governance/policy/samples/index).
- Review the [Azure Policy definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics).
- Understand how to [programmatically create policies](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/programmatically-create).
- Learn how to [get compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data).
- Learn how to [remediate non-compliant resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources).
- Review [Azure management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).
