# az ad ds

> Source: https://learn.microsoft.com/en-us/cli/azure/ad/ds  
> Microsoft doc last updated: unknown

Manage domain service with azure active directory.

Subgroups and commands: `az_ad_ds_create`, `az_ad_ds_delete`, `az_ad_ds_list`, `az_ad_ds_show`, `az_ad_ds_update`, `az_ad_ds_wait`

## az ad ds create  (Experimental; extension: aks-preview etc.)

Create a new domain service with the specified parameters.

**Required parameters**

- `--domain` — The name of the Azure domain that the user would like to deploy Domain Services to.
- `--name -n` — The name of the domain service.
- `--replica-sets` — List of ReplicaSets.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--domain-config-type` — Domain Configuration Type.
- `--external-access` — A flag to determine whether or not Secure LDAP access over the internet is enabled or disabled.
- `--filtered-sync` — Enabled or Disabled flag to turn on Group-based filtered sync.
- `--ldaps` — A flag to determine whether or not Secure LDAP is enabled or disabled.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--notify-dc-admins` — Should domain controller admins be notified.
- `--notify-global-admins` — Should global admins be notified.
- `--notify-others` — The list of additional recipients.
- `--ntlm-v1` — A flag to determine whether or not NtlmV1 is enabled or disabled.
- `--pfx-cert` — The certificate required to configure Secure LDAP. The parameter passed here should be the file path to the certificate pfx file or a base64encoded representation of the certificate pfx file.
- `--pfx-cert-pwd` — The password to decrypt the provided Secure LDAP certificate pfx file.
- `--resource-forest` — Resource Forest.
- `--settings` — List of settings for Resource Forest. This can be either a JSON-formatted string or the location to a file containing the JSON object.
- `--sku` — Sku Type.
- `--sync-kerberos-pwd` — A flag to determine whether or not SyncKerberosPasswords is enabled or disabled.
- `--sync-ntlm-pwd` — A flag to determine whether or not SyncNtlmPasswords is enabled or disabled.
- `--sync-on-prem-pwd` — A flag to determine whether or not SyncOnPremPasswords is enabled or disabled.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--tls-v1` — A flag to determine whether or not TlsV1 is enabled or disabled.

*Create Domain Service*
```azurecli
az ad ds create --domain "TestDS.com" --replica-sets location="West US" subnet-id="<subnetId>" --name "TestDS.com" --resource-group "rg"
```

*Create Domain Service with specified settings (Line breaks for legibility only)*
```azurecli
az ad ds create --domain "TestDS.com" --replica-sets location="West US" subnet-id="<subnetId>" --name "TestDS.com" --resource-group "rg"
--ntlm-v1 "Enabled" --sync-ntlm-pwd "Enabled" --tls-v1 "Disabled" --filtered-sync "Enabled" --external-access "Enabled"
--ldaps "Enabled" --pfx-cert "cert or path to cert" --pfx-cert-pwd "<pfxCertificatePassword>"
--notify-others "a@gmail.com" "b@gmail.com" --notify-dc-admins "Enabled" --notify-global-admins "Enabled"
```

## az ad ds delete  (Experimental; extension: aks-preview etc.)

The Delete Domain Service operation deletes an existing Domain Service.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--name -n` — The name of the domain service.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete Domain Service*
```azurecli
az ad ds delete --name "TestDomainService.com" --resource-group "TestResourceGroup"
```

## az ad ds list  (Experimental; extension: aks-preview etc.)

List domain services in resource group or in subscription.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*List Domain Service By Group*
```azurecli
az ad ds list --resource-group "TestResourceGroup"
```

*List Domain Service By Sub*
```azurecli
az ad ds list
```

## az ad ds show  (Experimental; extension: aks-preview etc.)

Get the specified domain service.

**Optional parameters**

- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--name -n` — The name of the domain service.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.

*Get Domain Service*
```azurecli
az ad ds show --name "TestDomainService.com" --resource-group "TestResourceGroup"
```

## az ad ds update  (Experimental; extension: aks-preview etc.)

Update the existing deployment properties for domain service.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--domain-config-type` — Domain Configuration Type.
- `--external-access` — A flag to determine whether or not Secure LDAP access over the internet is enabled or disabled.
- `--filtered-sync` — Enabled or Disabled flag to turn on Group-based filtered sync.
- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--ldaps` — A flag to determine whether or not Secure LDAP is enabled or disabled.
- `--name -n` — The name of the domain service.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--notify-dc-admins` — Should domain controller admins be notified.
- `--notify-global-admins` — Should global admins be notified.
- `--notify-others` — The list of additional recipients.
- `--ntlm-v1` — A flag to determine whether or not NtlmV1 is enabled or disabled.
- `--pfx-cert` — The certificate required to configure Secure LDAP. The parameter passed here should be the file path to the certificate pfx file or a base64encoded representation of the certificate pfx file.
- `--pfx-cert-pwd` — The password to decrypt the provided Secure LDAP certificate pfx file.
- `--replica-sets` — List of ReplicaSets.
- `--resource-forest` — Resource Forest.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--settings` — List of settings for Resource Forest. This can be either a JSON-formatted string or the location to a file containing the JSON object.
- `--sku` — Sku Type.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.
- `--sync-kerberos-pwd` — A flag to determine whether or not SyncKerberosPasswords is enabled or disabled.
- `--sync-ntlm-pwd` — A flag to determine whether or not SyncNtlmPasswords is enabled or disabled.
- `--sync-on-prem-pwd` — A flag to determine whether or not SyncOnPremPasswords is enabled or disabled.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--tls-v1` — A flag to determine whether or not TlsV1 is enabled or disabled.

*Update sku*
```azurecli
az ad ds update --name "TestDS.com" --resource-group "rg" --sku "Enterprise"
```

*Update domain security settings*
```azurecli
az ad ds update --name "TestDS.com" --resource-group "rg" --ntlm-v1 "Enabled" --tls-v1 "Disabled"
```

*Update ldaps settings*
```azurecli
az ad ds update --name "TestDS.com" --resource-group "rg" --external-access "Enabled" --ldaps "Enabled" --pfx-cert "MIIDPDCCAiSg..." --pfx-cert-pwd "<pfxCertificatePassword>"
```

*Update notification settings*
```azurecli
az ad ds update --name "TestDS.com" --resource-group "rg" --notify-dc-admins "Enabled" --notify-global-admins "Disabled"
```

## az ad ds wait  (Experimental; extension: aks-preview etc.)

Place the CLI in a waiting state until a condition of the ad ds is met.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--interval` — Polling interval in seconds. Default: 30.
- `--name -n` — The name of the domain service.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Pause executing next line of CLI script until the ad ds is successfully created.*
```azurecli
az ad ds wait --name "TestDomainService.com" --resource-group "TestResourceGroup" --created
```

*Pause executing next line of CLI script until the ad ds is successfully updated.*
```azurecli
az ad ds wait --name "TestDomainService.com" --resource-group "TestResourceGroup" --updated
```

*Pause executing next line of CLI script until the ad ds is successfully deleted.*
```azurecli
az ad ds wait --name "TestDomainService.com" --resource-group "TestResourceGroup" --deleted
```
