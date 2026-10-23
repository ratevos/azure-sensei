# Tutorial: Create a custom policy definition

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/create-custom-policy-definition  
> Microsoft doc last updated: 03/04/2025


A custom policy definition allows customers to define their own rules for using Azure. These rules often enforce:

- Security practices.
- Cost management.
- Organization-specific rules (like naming or locations).

Whatever the business driver for creating a custom policy, the steps are the same for defining the new custom policy.

Before creating a custom policy, check the [policy samples](https://learn.microsoft.com/en-us/azure/governance/policy/samples/index) to see whether a policy that matches your needs already exists.

The approach to creating a custom policy follows these steps:

> - Identify your business requirements
> - Map each requirement to an Azure resource property
> - Map the property to an alias
> - Determine which effect to use
> - Compose the policy definition

## Prerequisites

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.

## Identify requirements

Before creating the policy definition, it's important to understand the intent of the policy. For this tutorial, use a common enterprise security requirement as the goal to illustrate the steps involved:

- Each storage account must be enabled for HTTPS.
- Each storage account must be disabled for HTTP.

Your requirements should clearly identify both the "to be" and the "not to be" resource states.

While we defined the expected state of the resource, we haven't defined what we want done with non-compliant resources. Azure Policy supports many [effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics). For this tutorial, we define the business requirement as preventing the creation of resources if they aren't compliant with the business rules. To meet this goal, we use the [deny](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deny) effect. We also want the option to suspend the policy for specific assignments. Use the [disabled](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-disabled) effect and make the effect a [parameter](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-parameters) in the policy definition.

## Determine resource properties

Based on the business requirement, the Azure resource to audit with Azure Policy is a storage account. However, we don't know the properties to use in the policy definition. Azure Policy evaluates against the JSON representation of the resource, so we need to understand the properties available on that resource.

There are many ways to determine the properties for an Azure resource. We look at each for this tutorial:

- Azure Policy extension for VS Code.
- Azure Resource Manager templates (ARM templates).
  - Export existing resource.
  - Creation experience.
  - Quickstart templates (GitHub).
  - Template reference docs.
- Azure Resource Explorer.

### View resources in VS Code extension

The [VS Code extension](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/extension-for-vscode#search-for-and-view-resources) can be used to browse resources in your environment and see the Resource Manager properties on each resource.

### ARM templates

There are several ways to look at an
[ARM template](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-use-template-reference) that includes the property you're looking to manage.

#### Existing resource in the portal

The simplest way to find properties is to look at an existing resource of the same type. Resources already configured with the setting you want to enforce also provide the value to compare against. Look at the **Export template** page, in **Settings**, in the Azure portal for that specific resource.

> [!WARNING]
> The ARM template exported by Azure portal can't be plugged straight into the `deployment` property
> for an ARM template in a [deployIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-deploy-if-not-exists) policy
> definition.

Doing so for a storage account reveals a template similar to this example:

```json
"resources": [
  {
    "comments": "Generalized from resource: '/subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/mystorageaccount'.",
    "type": "Microsoft.Storage/storageAccounts",
    "sku": {
      "name": "Standard_LRS",
      "tier": "Standard"
    },
    "kind": "Storage",
    "name": "[parameters('storageAccounts_mystorageaccount_name')]",
    "apiVersion": "2018-07-01",
    "location": "westus",
    "tags": {
      "ms-resource-usage": "azure-cloud-shell"
    },
    "scale": null,
    "properties": {
      "networkAcls": {
        "bypass": "AzureServices",
        "virtualNetworkRules": [],
        "ipRules": [],
        "defaultAction": "Allow"
      },
      "supportsHttpsTrafficOnly": false,
      "encryption": {
        "services": {
          "file": {
            "enabled": true
          },
          "blob": {
            "enabled": true
          }
        },
        "keySource": "Microsoft.Storage"
      }
    },
    "dependsOn": []
  }
]
```

Under `properties` is a value named `supportsHttpsTrafficOnly` set to `false`. This property looks like it might be the property we're looking for. Also, the `type` of the resource is `Microsoft.Storage/storageAccounts`. The type lets us limit the policy to only resources of this type.

#### Create a resource in the portal

Another way through the portal is the resource creation experience. When you create a storage account through the portal, an option under the **Advanced** tab is **Security transfer required**. This property has _Disabled_ and _Enabled_ options. The info icon has more text that confirms this option is likely the property we want. But the portal doesn't tell us the property name on this screen.

On the **Review + create** tab, a link is at the bottom of the page to **Download a template for automation**. Selecting the link opens the template that creates the resource we configured. In this case, we see two key pieces of information:

```json
...
"supportsHttpsTrafficOnly": {
  "type": "bool"
}
...
"properties": {
  "accessTier": "[parameters('accessTier')]",
  "supportsHttpsTrafficOnly": "[parameters('supportsHttpsTrafficOnly')]"
}
...
```

This information tells us the property type and also confirms `supportsHttpsTrafficOnly` is the property we're looking for.

#### Quickstart templates on GitHub

The [Azure Quickstart Templates](https://github.com/Azure/azure-quickstart-templates) on GitHub has hundreds of ARM templates built for different resources. These templates can be a great way to find the resource property you're looking for. Some properties might appear to be what you're looking for, but control something else.

#### Resource reference docs

To validate `supportsHttpsTrafficOnly` is correct property, check the ARM template reference for the [storage account resource](https://learn.microsoft.com/en-us/azure/templates/microsoft.storage/storageaccounts) on the storage provider. The properties object has a list of valid parameters. Selecting the `StorageAccountPropertiesCreateParameters` object link shows a table of acceptable properties. `supportsHttpsTrafficOnly` is present and the description matches what we're looking for in regard to the business requirements.

### Azure Resource Explorer

Another way to explore your Azure resources is through the [Azure Resource Explorer](https://resources.azure.com) (Preview). This tool uses the context of your subscription, so you need to authenticate to the website with your Azure credentials. Once authenticated, you can browse by providers, subscriptions, resource groups, and resources.

Locate a storage account resource and look at the properties. We see the `supportsHttpsTrafficOnly` property here as well. Selecting the **Documentation** tab, we see that the property description matches what we found in the reference docs earlier.

## Find the property alias

We identified the resource property, but we need to map that property to an [alias](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-alias).

There are a few ways to determine the aliases for an Azure resource. We look at each for this tutorial:

- Azure Policy extension for VS Code.
- Azure CLI.
- Azure PowerShell.

### Get aliases in VS Code extension

The Azure Policy extension for VS Code extension makes it easy to browse your resources and [discover aliases](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/extension-for-vscode#discover-aliases-for-resource-properties).

> [!NOTE]
> The VS Code extension only exposes Resource Manager mode properties and doesn't display any
> [Resource Provider mode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#mode) properties.

### Azure CLI

In Azure CLI, the `az provider` command group is used to search for resource aliases. We filter for the `Microsoft.Storage` namespace based on the details we got about the Azure resource earlier.

```azurecli-interactive
# Login first with az login if not using Cloud Shell

# Get Azure Policy aliases for type Microsoft.Storage
az provider show --namespace Microsoft.Storage --expand "resourceTypes/aliases" --query "resourceTypes[].aliases[].name"
```

In the results, we see an alias supported by the storage accounts named `supportsHttpsTrafficOnly`. This existence of this alias means we can write the policy to enforce our business requirements!

### Azure PowerShell

In Azure PowerShell, the `Get-AzPolicyAlias` cmdlet is used to search for resource aliases. Filter for the `Microsoft.Storage` namespace based on the details we got about the Azure resource earlier.

```azurepowershell-interactive
# Login first with Connect-AzAccount if not using Cloud Shell

# Use Get-AzPolicyAlias to list aliases for Microsoft.Storage
(Get-AzPolicyAlias -NamespaceMatch 'Microsoft.Storage').Aliases
```

Like Azure CLI, the results show an alias supported by the storage accounts named `supportsHttpsTrafficOnly`.

## Determine the effect to use

Deciding what to do with your non-compliant resources is nearly as important as deciding what to evaluate in the first place. Each possible response to a non-compliant resource is called an [effect](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics). The effect controls if the non-compliant resource is logged, blocked, has data appended, or has a deployment associated to it for putting the resource back into a compliant state.

For our example, `deny` is the effect we want as we don't want non-compliant resources created in our Azure environment. Audit is a good first choice for a policy effect to determine what the effect of a policy is before setting it to `deny`. One way to make changing the effect per assignment easier is to parameterize the effect. See [parameters](#parameters) for the details.

## Compose the definition

We now have the property details and alias for what we plan to manage. Next, we compose the policy rule itself. If you aren't familiar with the policy language, reference [policy definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics) for how to structure the policy definition. Here's an empty template of what a policy definition looks like:

```json
{
  "properties": {
    "displayName": "<displayName>",
    "description": "<description>",
    "mode": "<mode>",
    "parameters": {
              <parameters>
    },
    "policyRule": {
      "if": {
              <rule>
      },
      "then": {
        "effect": "<effect>"
      }
    }
  }
}
```

### Metadata

The first three components are policy metadata. These components are easy to provide values for since we know what we are creating the rule for. [Mode](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics#mode) is primarily about tags and resource location. Since we don't need to limit evaluation to resources that support tags, use the _all_ value for `mode`.

```json
"displayName": "Deny storage accounts not using only HTTPS",
"description": "Deny storage accounts not using only HTTPS. Checks the supportsHttpsTrafficOnly property on StorageAccounts.",
"mode": "all",
```

### Parameters

While we didn't use a parameter for changing the evaluation, we do want to use a parameter to allow changing the `effect` for troubleshooting. You define an `effectType` parameter and limit it to only `deny` and `disabled`. These two options match our business requirements. The finished parameters block looks like this example:

```json
"parameters": {
  "effectType": {
    "type": "string",
    "defaultValue": "Deny",
    "allowedValues": [
      "Deny",
      "Disabled"
    ],
    "metadata": {
      "displayName": "Effect",
      "description": "Enable or disable the execution of the policy"
    }
  }
},
```

### Policy rule

Composing the [policy rule](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-policy-rule) is the final step in building our custom policy definition. We identified two statements to test for:

- The storage account `type` is `Microsoft.Storage/storageAccounts`.
- The storage account `supportsHttpsTrafficOnly` isn't `true`.

Since we need both of these statements to be true, use the `allOf` [logical operator](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-policy-rule#logical-operators). Pass the `effectType` parameter to the effect instead of making a static declaration. Our finished rule looks like this example:

```json
"if": {
  "allOf": [
    {
      "field": "type",
      "equals": "Microsoft.Storage/storageAccounts"
    },
    {
      "field": "Microsoft.Storage/storageAccounts/supportsHttpsTrafficOnly",
      "notEquals": "true"
    }
  ]
},
"then": {
  "effect": "[parameters('effectType')]"
}
```

### Completed definition

With all three parts of the policy defined, here is our completed definition:

```json
{
  "properties": {
    "displayName": "Deny storage accounts not using only HTTPS",
    "description": "Deny storage accounts not using only HTTPS. Checks the supportsHttpsTrafficOnly property on StorageAccounts.",
    "mode": "all",
    "parameters": {
      "effectType": {
        "type": "string",
        "defaultValue": "Deny",
        "allowedValues": [
          "Deny",
          "Disabled"
        ],
        "metadata": {
          "displayName": "Effect",
          "description": "Enable or disable the execution of the policy"
        }
      }
    },
    "policyRule": {
      "if": {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.Storage/storageAccounts"
          },
          {
            "field": "Microsoft.Storage/storageAccounts/supportsHttpsTrafficOnly",
            "notEquals": "true"
          }
        ]
      },
      "then": {
        "effect": "[parameters('effectType')]"
      }
    }
  }
}
```

The completed definition can be used to create a new policy. Portal and each SDK (Azure CLI, Azure PowerShell, and REST API) accept the definition in different ways, so review the commands for each to validate correct usage. Then assign it, using the parameterized effect, to appropriate resources to manage the security of your storage accounts.

## Clean up resources

If you're done working with resources from this tutorial, use the following steps to delete any of the assignments or definitions you created:

1. Select **Definitions** (or **Assignments** if you're trying to delete an assignment) under **Authoring** in the left side of the Azure Policy page.

1. Search for the new initiative or policy definition (or assignment) you want to remove.

1. Right-click the row or select the ellipses at the end of the definition (or assignment), and select **Delete definition** (or **Delete assignment**).

## Review

In this tutorial, you successfully accomplished the following tasks:

> - Identified your business requirements
> - Mapped each requirement to an Azure resource property
> - Mapped the property to an alias
> - Determined the effect to use
> - Composed the policy definition

## Next steps

Next, use your custom policy definition to create and assign a policy:

> [Create and assign a policy definition](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/programmatically-create#create-and-assign-a-policy-definition)
