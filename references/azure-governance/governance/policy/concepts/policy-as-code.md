# Design Azure Policy as Code workflows

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-as-code  
> Microsoft doc last updated: 03/04/2025


As you progress on your journey with Cloud Governance, you'll want to shift from manually managing
each policy assignment in the Azure portal or through the various SDKs to something more manageable
and repeatable at an enterprise scale. Two of the predominant approaches to managing systems at scale
in the cloud are:

- Infrastructure as Code: The practice of treating the content that defines your environments,
  everything from Azure Resource Manager templates (ARM templates) to Azure Policy definitions to
  Azure Blueprints, as source code.
- DevOps: The union of people, process, and products to enable continuous delivery of value to our
  end users.

Azure Policy as Code is the combination of these ideas. Essentially, keep your policy definitions in
source control and whenever a change is made, test, and validate that change. However, that
shouldn't be the extent of policies involvement with Infrastructure as Code or DevOps.

The validation step should also be a component of other continuous integration or continuous
deployment (CI/CD) workflows, like deploying an application environment or virtual infrastructure. By making Azure Policy validation an early component of the build and deployment process, the application and operations teams discover if their changes are behaving as expected long
before it's too late and they're attempting to deploy in production.

## Definitions and foundational information

Before getting into the details of Azure Policy as Code workflow, it's important to understand some fundamental concepts, like how to author policy definitions and initiative definitions, and how to leverage exemptions on assignments of those definitions:

- [Policy definition](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics)
- [Initiative definition](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/initiative-definition-structure)
- [Policy exemption](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/exemption-structure)

The file names correspond with certain portions of policy or initiative definitions and other policy resources:

| File format                   | File contents                       |
| :--                           | :--                                 |
| `policy-v#.json`              | The entire policy definition for that version        |
| `policyset-v#.json`              | The entire initiative definition for that version   |
| `policy-v#.parameters.json`      | The `properties.parameters` portion of the policy definition               |
| `policyset-v#.parameters.json`   | The `properties.parameters` portion of the initiative definition           |
| `policy-v#.rules.json`           | The `properties.policyRule` portion of the policy definition               |
| `policyset-v#.definitions.json`  | The `properties.policyDefinitions` portion of the initiative definition    |
| `exemptionName.json`          | The policy exemption that targets a particular resource or scope  |

## Workflow overview

The recommended general workflow of Azure Policy as Code looks like this diagram:

### Source control

Existing [policy and initiative definitions can be exported](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/export-resources) different ways such as through PowerShell, CLI, or [Azure Resource Graph (ARG)](https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview) queries. The source control management environment of choice to store these definitions can be one of many options, including a [GitHub](https://www.github.com) or [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops).

### Create and update policy definitions

The policy definitions are created using JSON, and stored in source control. Each policy has its
own set of files, such as the parameters, rules, and environment parameters that should be stored
in the same folder. The following structure is a recommended way of keeping your policy definitions
in source control.

```text
.
|
|- policies/  ________________________ # Root folder for policy resources
|  |- policy1/  ______________________ # Subfolder for a policy
|     |- versions_____________________ # Subfolder for versions of definition
|       |- policy-v#.json _________________ # Policy definition
|       |- policy-v#.parameters.json ______ # Policy definition of parameters
|       |- policy-v#.rules.json ___________ # Policy rule
|     |- assign.<name1>.json _________ # Assignment 1 for this policy definition
|     |- assign.<name2>.json _________ # Assignment 2 for this policy definition
|     |- exemptions.<name1>/__________ # Subfolder for exemptions on assignment 1
        | - exemptionName.json________ # Exemption for this particular assignment
      |- exemptions.<name2>/__________ # Subfolder for exemptions on assignment 2
        | - exemptionName.json________ # Exemption for this particular assignment
|
|  |- policy2/  ______________________ # Subfolder for a policy
|     |- versions_____________________ # Subfolder for versions of definition
|       |- policy-v#.json _________________ # Policy definition
|       |- policy-v#.parameters.json ______ # Policy definition of parameters
|       |- policy-v#.rules.json ___________ # Policy rule
|     |- assign.<name1>.json _________ # Assignment 1 for this policy definition
|     |- exemptions.<name1>/__________ # Subfolder for exemptions on assignment 1
        | - exemptionName.json________ # Exemption for this particular assignment
|
```

When a new policy or new version is added or an existing one is updated, the workflow should automatically update the
policy definition in Azure. Testing of the new or updated policy definition comes in a later step.

### Create and update initiative definitions

Initiative definitions are also created using JSON files that should be stored in the same folder as policy definitions. The initiative definition requires the policy definition to already exist, so it can't be
created or updated until the source for the policy has been updated in source control and then
updated in Azure. The following structure is a recommended way of keeping your initiative
definitions in source control:

```text
.
|
|- initiatives/ ______________________ # Root folder for initiatives
|  |- init1/ _________________________ # Subfolder for an initiative
|     |- versions ____________________ # Subfolder for versions of initiative
|       |- policyset.json ______________ # Initiative definition
|       |- policyset.definitions.json __ # Initiative list of policies
|       |- policyset.parameters.json ___ # Initiative definition of parameters
|     |- assign.<name1>.json _________ # Assignment 1 for this policy initiative
|     |- assign.<name2>.json _________ # Assignment 2 for this policy initiative
|     |- exemptions.<name1>/__________ # Subfolder for exemptions on assignment 1
        | - exemptionName.json________ # Exemption for this particular assignment
      |- exemptions.<name2>/__________ # Subfolder for exemptions on assignment 2
        | - exemptionName.json________ # Exemption for this particular assignment
|
|  |- init2/ _________________________ # Subfolder for an initiative
|     |- versions ____________________ # Subfolder for versions of initiative
|       |- policyset.json ______________ # Initiative definition
|       |- policyset.definitions.json __ # Initiative list of policies
|       |- policyset.parameters.json ___ # Initiative definition of parameters
|     |- assign.<name1>.json _________ # Assignment 1 for this policy initiative
|     |- exemptions.<name1>/__________ # Subfolder for exemptions on assignment 1
        | - exemptionName.json________ # Exemption for this particular assignment
|
```

Like with policy definitions, the workflow should
automatically update the initiative definition in Azure when an existing initiative is added or updated. Testing of the new or updated initiative
definition comes in a later step.

> [!NOTE]
> It's recommended to use a centralized deployment mechanism like GitHub workflows or Azure
> Pipelines to deploy policies. This helps to ensure only reviewed policy resources are deployed
> to your environment and that a gradual and central deployment mechanism is used. _Write_ permissions
> to policy resources can be restricted to the identity used in the deployment.

### Test and validate the updated definition

Once automation has taken your newly created or updated policy or initiative definitions and made
the update to the object in Azure, it's time to test the changes that were made. Either the policy
or the initiative(s) it's part of should then be assigned to resources in the environment farthest
from production. This environment is typically _Dev_.

>[!NOTE]
> In this step, we are conducting integration testing of the policy definition within your Azure environment, this is separate from [verifying the functionality of the policy definition](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/evaluate-impact#test-your-policys-effectiveness) which should occur during the definition creation process.

The assignment should use [enforcementMode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure#enforcement-mode) of
_disabled_ so that resource creation and updates aren't blocked, but that existing resources are
still audited for compliance to the updated policy definition. Even with enforcementMode, it's
recommended that the assignment scope is either a resource group or a subscription that is
specifically for validating policies.

> [!NOTE]
> While enforcement mode is helpful, it's not a replacement for thoroughly testing a policy
> definition under various conditions. The policy definition should be tested with `PUT` and `PATCH`
> REST API calls, compliant and non-compliant resources, and edge cases like a property missing from
> the resource.

After the assignment is deployed, use the Azure Policy SDK, the
[Azure Pipelines Security and Compliance Assessment task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/deploy/azure-policy), or [Azure Resource Graph (ARG)](https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview) queries (see [samples](https://learn.microsoft.com/en-us/azure/governance/policy/samples/resource-graph-samples)) to [get compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data) for the new assignment. The environment
used to test the policies and assignments should have resources with varying compliance states.
Like a good unit test for code, you want to test that resources are evaluated as expected with no false-positives or false-negatives. If you test and validate only for what you expect, there
may be unexpected and unidentified impact from the policy. For more information, see
[Evaluate the impact of a new Azure Policy definition](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/evaluate-impact).

### Enable remediation tasks

If validation of the assignment meets expectations, the next step is to validate remediation.
Policies that use either [deployIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deploy-if-not-exists) or
[modify](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-modify) can have an associated remediation task triggered to correct resources from a non-compliant state and bring them into compliance.

The first step to remediating resources is to grant the policy assignment the role assignment
defined in the policy definition. This role assignment gives the policy assignment managed identity
enough rights to make the needed changes to make the resource compliant.

Once the policy assignment has appropriate rights, use the Policy SDK to trigger a remediation task
against a set of resources that are known to be non-compliant. Three tests should be completed
against these remediated tasks before proceeding:

- Validate that the remediation task completed successfully
- Run policy evaluation to see that policy compliance results are updated as expected
- Run an environment unit test against the resources directly to validate their properties have
  changed

Testing both the updated policy evaluation results and the environment directly provide confirmation
that the remediation tasks changed what was expected and that the policy definition saw the
compliance change as expected.

### Update to enforced assignments

After all validation gates have completed, update the assignment to use **enforcementMode** of
_enabled_. It's recommended to make this change initially in the same environment far from
production. Validate that the desired effects are applied during resource creation and resource update. Once that environment is validated as working as expected, the change should then be
scoped to include the next environment, and so on, until the policy is deployed to production
resources.

## Process integrated evaluations

The general workflow for Azure Policy as Code is for developing and deploying policies and
initiatives to an environment at scale. However, policy evaluation should be part of the deployment
process for any workflow that deploys or creates resources in Azure, such as deploying applications
or running ARM templates to create infrastructure.

In these cases, after the application or infrastructure deployment is done to a test subscription or
resource group, policy evaluation should be done for that scope checking validation of all existing
policies and initiatives. While they may be configured as **enforcementMode** _disabled_ in such an
environment, it's useful to know early if an application or infrastructure deployment is in
violation of policy definitions early. This policy evaluation should therefore be a step in those
workflows, and fail deployments that create non-compliant resources.

## Review

This article covers the general workflow for Azure Policy as Code and also where policy evaluation
should be part of other deployment workflows. This workflow can be used in any environment that
supports scripted steps and automation based on triggers.

## Next steps

- Learn about the [policy definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics).
- Learn about the [policy assignment structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure).
- Understand how to [programmatically create policies](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/programmatically-create).
- Learn how to [get compliance data](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data).
- Learn how to [remediate non-compliant resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources).
- Under how to [follow policy safe deployment practices](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/policy-safe-deployment-practices)
