# How to find your tenant ID

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant  
> Microsoft doc last updated: 01/14/2025


## Overview

Azure subscriptions have a trust relationship with Microsoft Entra ID. Microsoft Entra ID is trusted to authenticate the subscription's users, services, and devices. Each subscription has a tenant ID associated with it, and there are a few ways you can find the tenant ID for your subscription.

## Find tenant ID through the Microsoft Entra admin center

Follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader).

1. Browse to **Entra ID** > **Overview** > **Properties**.

    

1. Scroll down to the **Tenant ID** section and you can find your tenant ID in the box.

## Find tenant ID through the Azure portal

Follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com).

1. Browse to **Microsoft Entra ID** > **Properties**.

1. Scroll down to the **Tenant ID** section and you can find your tenant ID in the box.

    

## Find tenant ID with PowerShell

To find the tenant ID with Azure PowerShell, use the cmdlet `Get-AzTenant`.

```azurepowershell-interactive
Connect-AzAccount
Get-AzTenant
```

For more information, see the [Get-AzTenant](https://learn.microsoft.com/en-us/powershell/module/az.accounts/get-aztenant) cmdlet reference.

## Find tenant ID with CLI

Use the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) or [Microsoft 365 CLI](https://github.com/pnp/cli-microsoft365) to find the tenant ID.

For Azure CLI, use one of the commands `az login`, `az account list`, or `az account tenant list`. All commands included below return the `tenantId` property for each of your subscriptions.

```azurecli-interactive
az login
az account list
az account tenant list
```

For more information, see [az login](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) command reference, [az account](https://learn.microsoft.com/en-us/cli/azure/account) command reference, or [az account tenant](https://learn.microsoft.com/en-us/cli/azure/account/tenant) command reference.

For Microsoft 365 CLI, use the cmdlet `tenant id` as shown in the following example:

```cli
m365 tenant id get
```

## Related content

- [Create a new tenant in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/create-new-tenant)
- [Associate or add an Azure subscription to your Microsoft Entra tenant](https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory)
- [Find the user object ID](https://learn.microsoft.com/en-us/partner-center/find-ids-and-domain-names#find-the-user-object-id)
