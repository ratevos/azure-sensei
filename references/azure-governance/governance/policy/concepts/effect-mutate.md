# Azure Policy definitions mutate effect

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-mutate  
> Microsoft doc last updated: 03/04/2025


Mutation is used in Azure Policy for Kubernetes to remediate Azure Kubernetes Service (AKS) cluster components, like pods. This effect is specific to _Microsoft.Kubernetes.Data_ [policy mode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#resource-provider-modes) definitions only.

To learn more, go to [Understand Azure Policy for Kubernetes clusters](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes).

## Mutate properties

- `mutationInfo` (optional)
  - Can't be used with `constraint`, `constraintTemplate`, `apiGroups`, or `kinds`.
  - Can't be parameterized.
  - `sourceType` (required)
    - Defines the type of source for the constraint. Allowed values: `PublicURL` or `Base64Encoded`.
    - If `PublicURL`, paired with property `url` to provide location of the mutation template. The location must be publicly accessible.
      > [!WARNING]
      > Don't use SAS URIs or tokens in `url` or anything else that could expose a secret.

## Next steps

- Review examples at [Azure Policy samples](https://learn.microsoft.com/en-us/azure/governance/policy/samples/index).
- Review the [Azure Policy definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics).
- Understand how to [programmatically create policies](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/programmatically-create).
- Learn how to [get compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data).
- Learn how to [remediate non-compliant resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources).
- Review [Azure management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).
