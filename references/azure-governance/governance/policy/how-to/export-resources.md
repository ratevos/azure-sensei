# Export Azure Policy resources

> Source: https://learn.microsoft.com/en-us/azure/governance/policy/how-to/export-resources  
> Microsoft doc last updated: 03/04/2025


This article provides information on how to export your existing Azure Policy resources. Exporting your resources is useful and recommended for backup, but is also an important step in your journey with Cloud Governance and treating your [policy-as-code](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-as-code). Azure Policy resources can be exported through [REST API](https://learn.microsoft.com/en-us/rest/api/policy), [Azure CLI](#export-with-azure-cli), and [Azure PowerShell](#export-with-azure-powershell).

> [!NOTE]
> The portal experience for exporting definitions to GitHub was deprecated in April 2023.

## Export with Azure CLI

Azure Policy definitions, initiatives, and assignments can each be exported as JSON with [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli). Each of these commands uses a `name` parameter to specify which object to get the JSON for. The `name` property is often a _GUID_ and isn't the `displayName` of the object.

The Azure CLI and Azure PowerShell example commands use a built-in Policy definition with the `name` `b2982f36-99f2-4db5-8eff-283140c09693` and the `displayName` _Storage accounts should disable public network access_.

- Definition - [az policy definition show](https://learn.microsoft.com/en-us/cli/azure/policy/definition#az-policy-definition-show).
- Initiative - [az policy set-definition show](https://learn.microsoft.com/en-us/cli/azure/policy/set-definition#az-policy-set-definition-show).
- Assignment - [az policy assignment show](https://learn.microsoft.com/en-us/cli/azure/policy/assignment#az-policy-assignment-show).

```azurecli-interactive
az policy definition show --name 'b2982f36-99f2-4db5-8eff-283140c09693'
```

## Export with Azure PowerShell

Azure Policy definitions, initiatives, and assignments can each be exported as JSON with [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/). Each of these cmdlets uses a `Name` parameter to specify which object to get the JSON for. The `Name` property is often a _GUID_ (Globally Unique Identifier) and isn't the `displayName` of the object.

- Definition - [Get-AzPolicyDefinition](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azpolicydefinition).
- Initiative - [Get-AzPolicySetDefinition](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azpolicysetdefinition).
- Assignment - [Get-AzPolicyAssignment](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azpolicyassignment).

```azurepowershell-interactive
Get-AzPolicyDefinition -Name 'b2982f36-99f2-4db5-8eff-283140c09693' | Select-Object -Property * | ConvertTo-Json -Depth 10
```

## Export to CSV with Resource Graph in Azure portal

Azure Resource Graph gives the ability to query at scale with complex filtering, grouping and sorting. Azure Resource Graph supports the policy resources table, which contains policy resources such as definitions, assignments and exemptions. Review our [sample queries.](https://learn.microsoft.com/en-us/azure/governance/policy/samples/resource-graph-samples#azure-policy). The Resource Graph explorer portal experience allows downloads of query results to CSV using the ["Download to CSV"](https://learn.microsoft.com/en-us/azure/governance/resource-graph/first-query-portal#download-query-results-as-a-csv-file) toolbar option.

## Next steps

- Review examples at [Azure Policy samples](https://learn.microsoft.com/en-us/azure/governance/policy/samples/index).
- Review the [Azure Policy definition structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/definition-structure-basics).
- Review [Understanding policy effects](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-basics).
- Understand how to [programmatically create policies](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/programmatically-create).
- Learn how to [remediate noncompliant resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources).
- Review what a management group is with [Organize your resources with Azure management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview).
