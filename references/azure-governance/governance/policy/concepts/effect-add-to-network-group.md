# Azure Policy definitions addToNetworkGroup effect

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-add-to-network-group  
> Microsoft doc last updated: 03/04/2025


The `addToNetworkGroup` effect is used in Azure Virtual Network Manager to define dynamic network group membership. This effect is specific to `Microsoft.Network.Data` [policy mode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#resource-provider-modes) definitions only.

With network groups, your policy definition includes your conditional expression for matching virtual networks meeting your criteria, and specifies the destination network group where any matching resources are placed. The `addToNetworkGroup` effect is used to place resources in the destination network group.

To learn more, go to [Configuring Azure Policy with network groups in Azure Virtual Network Manager](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-azure-policy-integration).

## Next steps

- Review examples at [Azure Policy samples](https://learn.microsoft.com/en-us/azure/governance/policy/samples/index).
- Review the [Azure Policy definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics).
- Understand how to [programmatically create policies](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/programmatically-create).
- Learn how to [get compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data).
- Learn how to [remediate non-compliant resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources).
- Review [Azure management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).
