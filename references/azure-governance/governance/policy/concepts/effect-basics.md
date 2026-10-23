# Azure Policy definitions effect basics

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics  
> Microsoft doc last updated: 03/04/2025


Each policy definition in Azure Policy has a single `effect` in its `policyRule`. That `effect` determines what happens when the policy rule is evaluated to match. The effects behave differently if they are for a new resource, an updated resource, or an existing resource.

The following are the supported Azure Policy definition effects:

- [addToNetworkGroup](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-add-to-network-group)
- [append](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-append)
- [audit](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-audit)
- [auditIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-audit-if-not-exists)
- [deny](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny)
- [denyAction](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny-action)
- [deployIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deploy-if-not-exists)
- [disabled](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-disabled)
- [manual](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-manual)
- [modify](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-modify)
- [mutate](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-mutate)

## Interchanging effects

Sometimes multiple effects can be valid for a given policy definition. Parameters are often used to specify allowed effect values (`allowedValues`) so that a single definition can be more versatile during assignment. However, it's important to note that not all effects are interchangeable. Resource properties and logic in the policy rule can determine whether a certain effect is considered valid to the policy definition. For example, policy definitions with effect `auditIfNotExists` require other details in the policy rule that aren't required for policies with effect `audit`. The effects also behave differently. `audit` policies assess a resource's compliance based on its own properties, while `auditIfNotExists` policies assess a resource's compliance based on a child or extension resource's properties.

The following list is some general guidance around interchangeable effects:

- `audit`, `deny`, and either `modify` or `append` are often interchangeable.
- `auditIfNotExists` and `deployIfNotExists` are often interchangeable.
- `manual` isn't interchangeable.
- `disabled` is interchangeable with any effect.

## Order of evaluation

Azure Policy's first evaluation is for requests to create or update a resource. Azure Policy creates a list of all assignments that apply to the resource and then evaluates the resource against each definition. For a [Resource Manager mode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#resource-manager-modes), Azure Policy processes several of the effects before handing the request to the appropriate Resource Provider. This order prevents unnecessary processing by a Resource Provider when a resource doesn't meet the designed governance controls of Azure Policy. With a [Resource Provider mode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#resource-provider-modes), the Resource Provider manages the evaluation and outcome and reports the results back to Azure Policy.

- `disabled` is checked first to determine whether the policy rule should be evaluated.
- `append` and `modify` are then evaluated. Since either could alter the request, a change made might prevent an audit or deny effect from triggering. These effects are only available with a Resource Manager mode.
- `deny` is then evaluated. By evaluating deny before audit, double logging of an undesired resource is prevented.
- `audit` is evaluated.
- `manual` is evaluated.
- `auditIfNotExists` is evaluated.
- `denyAction` is evaluated last.

After the Resource Provider returns a success code on a Resource Manager mode request, `auditIfNotExists` and `deployIfNotExists` evaluate to determine whether more compliance logging or action is required.

`PATCH` requests that only modify `tags` related fields restricts policy evaluation to policies containing conditions that inspect `tags` related fields.

## Layering policy definitions

Several assignments can affect a resource. These assignments might be at the same scope or at different scopes. Each of these assignments is also likely to have a different effect defined. The condition and effect for each policy is independently evaluated. For example:

- Policy 1
  - Restricts resource location to `westus`
  - Assigned to subscription A
  - Deny effect
- Policy 2
  - Restricts resource location to `eastus`
  - Assigned to resource group B in subscription A
  - Audit effect

This setup would result in the following outcome:

- Any resource already in resource group B in `eastus` is compliant to policy 2 and non-compliant to policy 1
- Any resource already in resource group B not in `eastus` is non-compliant to policy 2 and non-compliant to policy 1 if not in `westus`
- Policy 1 denies any new resource in subscription A not in `westus`
- Any new resource in subscription A and resource group B in `westus` is created and non-compliant on policy 2

If both policy 1 and policy 2 had effect of deny, the situation changes to:

- Any resource already in resource group B not in `eastus` is non-compliant to policy 2
- Any resource already in resource group B not in `westus` is non-compliant to policy 1
- Policy 1 denies any new resource in subscription A not in `westus`
- Any new resource in resource group B of subscription A is denied

Each assignment is individually evaluated. As such, there isn't an opportunity for a resource to slip through a gap from differences in scope. The net result of layering policy definitions is considered to be **cumulative most restrictive**. As an example, if both policy 1 and 2 had a `deny` effect, a resource would be blocked by the overlapping and conflicting policy definitions. If you still need the resource to be created in the target scope, review the exclusions on each assignment to validate the right policy assignments are affecting the right scopes.

## Next steps

- Review examples at [Azure Policy samples](https://learn.microsoft.com/en-us/azure/governance/policy/samples/index).
- Review the [Azure Policy definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics).
- Understand how to [programmatically create policies](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/programmatically-create).
- Learn how to [get compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data).
- Learn how to [remediate non-compliant resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources).
- Review [Azure management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).
