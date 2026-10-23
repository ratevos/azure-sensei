# az keyvault

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault  
> Microsoft doc last updated: unknown

Manage KeyVault keys, secrets, and certificates.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_keyvault_backup`, `az_keyvault_backup_start`, `az_keyvault_certificate`, `az_keyvault_certificate_backup`, `az_keyvault_certificate_contact`, `az_keyvault_certificate_contact_add`, `az_keyvault_certificate_contact_delete`, `az_keyvault_certificate_contact_list`, `az_keyvault_certificate_create`, `az_keyvault_certificate_delete`, `az_keyvault_certificate_download`, `az_keyvault_certificate_get-default-policy`, `az_keyvault_certificate_import`, `az_keyvault_certificate_issuer`, `az_keyvault_certificate_issuer_admin`, `az_keyvault_certificate_issuer_admin_add`, `az_keyvault_certificate_issuer_admin_delete`, `az_keyvault_certificate_issuer_admin_list`, `az_keyvault_certificate_issuer_create`, `az_keyvault_certificate_issuer_delete`, `az_keyvault_certificate_issuer_list`, `az_keyvault_certificate_issuer_show`, `az_keyvault_certificate_issuer_update`, `az_keyvault_certificate_list`, `az_keyvault_certificate_list-deleted`, `az_keyvault_certificate_list-versions`, `az_keyvault_certificate_pending`, `az_keyvault_certificate_pending_delete`, `az_keyvault_certificate_pending_merge`, `az_keyvault_certificate_pending_show`, `az_keyvault_certificate_purge`, `az_keyvault_certificate_recover`, `az_keyvault_certificate_restore`, `az_keyvault_certificate_set-attributes`, `az_keyvault_certificate_show`, `az_keyvault_certificate_show-deleted`, `az_keyvault_check-name`, `az_keyvault_create`, `az_keyvault_delete`, `az_keyvault_delete-policy`, `az_keyvault_ekm-connection`, `az_keyvault_ekm-connection_certificate`, `az_keyvault_ekm-connection_certificate_show`, `az_keyvault_ekm-connection_check`, `az_keyvault_ekm-connection_create`, `az_keyvault_ekm-connection_delete`, `az_keyvault_ekm-connection_show`, `az_keyvault_ekm-connection_update`, `az_keyvault_key`, `az_keyvault_key_backup`, `az_keyvault_key_create`, `az_keyvault_key_decrypt`, `az_keyvault_key_delete`, `az_keyvault_key_download`, `az_keyvault_key_encrypt`, `az_keyvault_key_get-attestation`, `az_keyvault_key_get-policy-template`, `az_keyvault_key_import`, `az_keyvault_key_list`, `az_keyvault_key_list-deleted`, `az_keyvault_key_list-versions`, `az_keyvault_key_purge`, `az_keyvault_key_random`, `az_keyvault_key_recover`, `az_keyvault_key_restore`, `az_keyvault_key_rotate`, `az_keyvault_key_rotation-policy`, `az_keyvault_key_rotation-policy_show`, `az_keyvault_key_rotation-policy_update`, `az_keyvault_key_set-attributes`, `az_keyvault_key_show`, `az_keyvault_key_show-deleted`, `az_keyvault_key_sign`, `az_keyvault_key_verify`, `az_keyvault_list`, `az_keyvault_list-deleted`, `az_keyvault_network-rule`, `az_keyvault_network-rule_add`, `az_keyvault_network-rule_list`, `az_keyvault_network-rule_remove`, `az_keyvault_network-rule_wait`, `az_keyvault_private-endpoint-connection`, `az_keyvault_private-endpoint-connection_approve`, `az_keyvault_private-endpoint-connection_delete`, `az_keyvault_private-endpoint-connection_list`, `az_keyvault_private-endpoint-connection_reject`, `az_keyvault_private-endpoint-connection_show`, `az_keyvault_private-endpoint-connection_wait`, `az_keyvault_private-link-resource`, `az_keyvault_private-link-resource_list`, `az_keyvault_purge`, `az_keyvault_recover`, `az_keyvault_region`, `az_keyvault_region_add`, `az_keyvault_region_add(keyvault-preview)`, `az_keyvault_region_list`, `az_keyvault_region_list(keyvault-preview)`, `az_keyvault_region_remove`, `az_keyvault_region_remove(keyvault-preview)`, `az_keyvault_region_wait`, `az_keyvault_region_wait(keyvault-preview)`, `az_keyvault_restore`, `az_keyvault_restore_start`, `az_keyvault_role`, `az_keyvault_role_assignment`, `az_keyvault_role_assignment_create`, `az_keyvault_role_assignment_delete`, `az_keyvault_role_assignment_list`, `az_keyvault_role_definition`, `az_keyvault_role_definition_create`, `az_keyvault_role_definition_delete`, `az_keyvault_role_definition_list`, `az_keyvault_role_definition_show`, `az_keyvault_role_definition_update`, `az_keyvault_secret`, `az_keyvault_secret_backup`, `az_keyvault_secret_delete`, `az_keyvault_secret_download`, `az_keyvault_secret_list`, `az_keyvault_secret_list-deleted`, `az_keyvault_secret_list-versions`, `az_keyvault_secret_purge`, `az_keyvault_secret_recover`, `az_keyvault_secret_restore`, `az_keyvault_secret_set`, `az_keyvault_secret_set-attributes`, `az_keyvault_secret_show`, `az_keyvault_secret_show-deleted`, `az_keyvault_security-domain`, `az_keyvault_security-domain_download`, `az_keyvault_security-domain_init-recovery`, `az_keyvault_security-domain_restore-blob`, `az_keyvault_security-domain_upload`, `az_keyvault_security-domain_wait`, `az_keyvault_set-policy`, `az_keyvault_setting`, `az_keyvault_setting_list`, `az_keyvault_setting_show`, `az_keyvault_setting_update`, `az_keyvault_show`, `az_keyvault_show-deleted`, `az_keyvault_update`, `az_keyvault_update-hsm`, `az_keyvault_update-hsm(keyvault-preview)`, `az_keyvault_wait`, `az_keyvault_wait-hsm`

## az keyvault check-name

Check that the given name is valid and is not already in use.

**Required parameters**

- `--name -n` — The name of the HSM within the specified resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--resource-type` — Type of resource. Default: hsm.

## az keyvault create

Create a Vault or HSM.

**Required parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--administrators` — [HSM Only] Administrator role for data plane operations for Managed HSM. It accepts a space separated list of OIDs that will be assigned.
- `--bypass` — Bypass traffic for space-separated uses.
- `--change-reference` — The related change reference ID for this resource operation.
- `--default-action` — Default action to apply when no rule matches.
- `--enable-purge-protection` — Property specifying whether protection against purge is enabled for this vault/managed HSM pool. Setting this property to true activates protection against purge for this vault/managed HSM pool and its content - only the Key Vault/Managed HSM service may initiate a hard, irrecoverable deletion. The 
- `--enable-rbac-authorization` — Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be ignored. When false, the key vault will use the access policies specified in vau Default: True.
- `--enabled-for-deployment` — [Vault Only] Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.
- `--enabled-for-disk-encryption` — [Vault Only] Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
- `--enabled-for-template-deployment` — [Vault Only] Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.
- `--hsm-name` — Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them).
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--mi-user-assigned` — [HSM Only] Enable user-assigned managed identities for managed HSM. Accept space-separated list of identity resource IDs.
- `--name -n` — Name of the Vault.
- `--network-acls` — Network ACLs. It accepts a JSON filename or a JSON string. JSON format: `{\"ip\":[<ip1>, <ip2>...],\"vnet\":[<vnet_name_1>/<subnet_name_1>,<subnet_id2>...]}`.
- `--network-acls-ips` — Network ACLs IP rules. Space-separated list of IP addresses.
- `--network-acls-vnets` — Network ACLS VNet rules. Space-separated list of Vnet/subnet pairs or subnet resource ids.
- `--no-self-perms` — [Vault Only] Don't add permissions for the current user/service principal in the new vault.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--public-network-access` — Control permission for data plane traffic coming from public networks while private endpoint is enabled.
- `--retention-days` — Soft delete data retention days. It accepts >=7 and <=90. Defaults to 90 for keyvault creation. Required for MHSM creation.
- `--sku` — Required. SKU details. Allowed values for Vault: premium, standard. Default: standard. Allowed values for HSM: Standard_B1, Custom_B32, Custom_B6, Custom_C42, Custom_C10. Default: Standard_B1.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

*Create a key vault with network ACLs specified (use --network-acls to specify IP and VNet rules by using a JSON string).*
```azurecli
az keyvault create --location westus2 --name MyKeyVault --resource-group MyResourceGroup --network-acls "{\"ip\": [\"1.2.3.4\", \"2.3.4.0/24\"], \"vnet\": [\"vnet_name_1/subnet_name1\", \"vnet_name_2/subnet_name2\", \"/subscriptions/000000-0000-0000/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVNet/subnets/MySubnet\"]}"
```

*Create a key vault with network ACLs specified (use --network-acls to specify IP and VNet rules by using a JSON file).*
```azurecli
az keyvault create --location westus2 --name MyKeyVault --resource-group MyResourceGroup --network-acls network-acls-example.json
```

*Create a key vault with network ACLs specified (use --network-acls-ips to specify IP rules).*
```azurecli
az keyvault create --location westus2 --name MyKeyVault --resource-group MyResourceGroup --network-acls-ips 3.4.5.0/24 4.5.6.0/24
```

*Create a key vault with network ACLs specified (use --network-acls-vnets to specify VNet rules).*
```azurecli
az keyvault create --location westus2 --name MyKeyVault --resource-group MyResourceGroup --network-acls-vnets vnet_name_2/subnet_name_2 vnet_name_3/subnet_name_3 /subscriptions/000000-0000-0000/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/vnet_name_4/subnets/subnet_name_4
```

*Create a key vault with network ACLs specified (use --network-acls, --network-acls-ips and --network-acls-vnets together, redundant rules will be removed, finally there will be 4 IP rules and 3 VNet rules).*
```azurecli
az keyvault create --location westus2 --name MyKeyVault --resource-group MyResourceGroup --network-acls "{\"ip\": [\"1.2.3.4\", \"2.3.4.0/24\"], \"vnet\": [\"vnet_name_1/subnet_name1\", \"vnet_name_2/subnet_name2\"]}" --network-acls-ips 3.4.5.0/24 4.5.6.0/24 --network-acls-vnets vnet_name_2/subnet_name_2 vnet_name_3/subnet_name_3 /subscriptions/000000-0000-0000/resourceGroups/MyResourceGroup/providers/Microsoft.Network/virtualNetworks/vnet_name_4/subnets/subnet_name_4
```

*Create a key vault. (autogenerated)*
```azurecli
az keyvault create --location westus2 --name MyKeyVault --resource-group MyResourceGroup
```

## az keyvault delete

Delete a Vault or HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them).
- `--name -n` — Name of the Vault.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group.

*Delete a key vault. (autogenerated)*
```azurecli
az keyvault delete --name MyKeyVault --resource-group MyResourceGroup
```

## az keyvault delete-policy

Delete security policy settings for a Key Vault.

**Required parameters**

- `--name -n` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--application-id` — Application ID of the client making request on behalf of a principal. Exposed for compound identity using on-behalf-of authentication flow.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--object-id` — A GUID that identifies the principal that will receive permissions.
- `--resource-group -g` — Name of resource group.
- `--spn` — Name of a service principal that will receive permissions.
- `--upn` — Name of a user principal that will receive permissions.

## az keyvault list

List Vaults and/or HSMs.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — When --resource-type is not present the command will list all Vaults and HSMs. Possible values for --resource-type are vault and hsm.

## az keyvault list-deleted

Get information about the deleted Vaults or HSMs in a subscription.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--resource-type` — When --resource-type is not present the command will list all deleted Vaults and HSMs. Possible values for --resource-type are vault and hsm.

## az keyvault purge

Permanently delete the specified Vault or HSM. Aka Purges the deleted Vault or HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the deleted HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them).
- `--location -l` — Location of the deleted Vault or HSM.
- `--name -n` — Name of the deleted Vault.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az keyvault recover

Recover a Vault or HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the deleted HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them).
- `--location -l` — Location of the deleted Vault or HSM.
- `--name -n` — Name of the deleted Vault.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Resource group of the deleted Vault or HSM.

*Recover a key vault. (autogenerated)*
```azurecli
az keyvault recover --location westus2 --name MyKeyVault --resource-group MyResourceGroup
```

## az keyvault set-policy

Update security policy settings for a Key Vault.

**Required parameters**

- `--name -n` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--application-id` — Application ID of the client making request on behalf of a principal. Exposed for compound identity using on-behalf-of authentication flow.
- `--certificate-permissions` — Space-separated list of certificate permissions to assign.
- `--change-reference` — The related change reference ID for this resource operation.
- `--key-permissions` — Space-separated list of key permissions to assign.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--object-id` — A GUID that identifies the principal that will receive permissions.
- `--resource-group -g` — Name of resource group.
- `--secret-permissions` — Space-separated list of secret permissions to assign.
- `--spn` — Name of a service principal that will receive permissions.
- `--storage-permissions` — Space-separated list of storage permissions to assign.
- `--upn` — Name of a user principal that will receive permissions.

*Assign key permissions `get`, `list`, `import` and secret permissions `backup`, `restore` to an object id.*
```azurecli
az keyvault set-policy -n MyVault --key-permissions get list import --secret-permissions backup restore --object-id {GUID}
```

*Assign key permissions `get`, `list` to a UPN (User Principal Name).*
```azurecli
az keyvault set-policy -n MyVault --key-permissions get list --upn {UPN}
```

*Assign key permissions `get`, `list` to a SPN (Service Principal Name).*
```azurecli
az keyvault set-policy -n MyVault --key-permissions get list --spn {SPN}
```

## az keyvault show

Show details of a Vault or HSM.

**Optional parameters**

- `--hsm-name` — Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them).
- `--name -n` — Name of the Vault.
- `--resource-group -g` — Name of resource group.

*Show details of a key vault. (autogenerated)*
```azurecli
az keyvault show --name MyKeyVault
```

## az keyvault show-deleted

Show details of a deleted Vault or HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the deleted HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them).
- `--location -l` — Location of the deleted Vault or HSM.
- `--name -n` — Name of the deleted Vault.

*Show details of a deleted key vault.*
```azurecli
az keyvault show-deleted --name MyKeyVault
```

## az keyvault update

Update the properties of a Vault.

**Required parameters**

- `--name -n` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`. Default: [].
- `--bypass` — Bypass traffic for space-separated uses.
- `--change-reference` — The related change reference ID for this resource operation.
- `--default-action` — Default action to apply when no rule matches.
- `--enable-purge-protection` — Property specifying whether protection against purge is enabled for this vault/managed HSM pool. Setting this property to true activates protection against purge for this vault/managed HSM pool and its content - only the Key Vault/Managed HSM service may initiate a hard, irrecoverable deletion. The 
- `--enable-rbac-authorization` — Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be ignored. When false, the key vault will use the access policies specified in vau
- `--enabled-for-deployment` — [Vault Only] Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.
- `--enabled-for-disk-encryption` — [Vault Only] Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
- `--enabled-for-template-deployment` — [Vault Only] Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--public-network-access` — Control permission for data plane traffic coming from public networks while private endpoint is enabled.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`. Default: [].
- `--resource-group -g` — Name of resource group.
- `--retention-days` — Soft delete data retention days. It accepts >=7 and <=90.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`. Default: [].

*Update the properties of a Vault. (autogenerated)*
```azurecli
az keyvault update --enabled-for-disk-encryption true --name MyKeyVault --resource-group MyResourceGroup
```

## az keyvault update-hsm

Update the properties of a HSM.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`. Default: [].
- `--bypass` — Bypass traffic for space-separated uses.
- `--change-reference` — The related change reference ID for this resource operation.
- `--default-action` — Default action to apply when no rule matches.
- `--enable-purge-protection -e` — Property specifying whether protection against purge is enabled for this vault/managed HSM pool. Setting this property to true activates protection against purge for this vault/managed HSM pool and its content - only the Key Vault/Managed HSM service may initiate a hard, irrecoverable deletion. The 
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON. Default: False.
- `--mi-user-assigned` — Enable user-assigned managed identities for managed HSM. Accept space-separated list of identity resource IDs.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--public-network-access` — Control permission for data plane traffic coming from public networks while private endpoint is enabled.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`. Default: [].
- `--resource-group -g` — Name of resource group.
- `--secondary-locations` — --secondary-locations extends/contracts an HSM pool to listed regions. The primary location where the resource was originally created CANNOT be removed.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`. Default: [].

*Update the properties of a HSM.*
```azurecli
az keyvault update-hsm --enable-purge-protection true --hsm-name MyHSM --resource-group MyResourceGroup
```

## az keyvault update-hsm  (extension: aks-preview etc.)

Update the properties of a HSM.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`. Default: [].
- `--bypass` — Bypass traffic for space-separated uses.
- `--change-reference` — The related change reference ID for this resource operation.
- `--default-action` — Default action to apply when no rule matches.
- `--enable-purge-protection -e` — Property specifying whether protection against purge is enabled for this managed HSM pool. Setting this property to true activates protection against purge for this managed HSM pool and its content - only the Managed HSM service may initiate a hard, irrecoverable deletion. The setting is effective o
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`. Default: [].
- `--resource-group -g` — Proceed only if Key Vault belongs to the specified resource group.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`. Default: [].

*Update the properties of a HSM.*
```azurecli
az keyvault update-hsm --enable-purge-protection true --hsm-name MyHSM --resource-group MyResourceGroup
```

## az keyvault wait

Place the CLI in a waiting state until a condition of the Vault is met.

**Required parameters**

- `--name -n` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--resource-group -g` — Name of resource group.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Pause CLI until the vault is created.*
```azurecli
az keyvault wait --name MyVault --created
```

## az keyvault wait-hsm

Place the CLI in a waiting state until a condition of the HSM is met.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--resource-group -g` — Proceed only if HSM belongs to the specified resource group.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Pause CLI until the HSM is created.*
```azurecli
az keyvault wait-hsm --hsm-name MyHSM --created
```
